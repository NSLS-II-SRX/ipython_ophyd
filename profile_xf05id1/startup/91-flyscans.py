#####
# Pseudocode for fly scanning
# User supplies:
# X start       Xstart is used for gating, Xo is an X stage value where the scan
#   will start
# Y start       Ystart is used for gating, Yo is an Y stage value where the scan
#   will start
# range X       scan X size
# dwell         time spent per atom, range X and dwell give stage speed
# range Y       scan Y size
#####

#Transverse flyer for SRX: fly X, step Y
#Aerotech X stage, DC motor need to set desired velocity
#Zebra staged, data read and written to file, file registered
#Options:  open and write to Xspress3 HDF5, write to HDF5 and link in 
#   Xspress3 data, write separately in some format and register later
#
import copy
from bluesky.plans import (one_1d_step, kickoff, collect, complete, scan, wait,
                           monitor_during_wrapper, stage_decorator, abs_set,
                           run_decorator)
from bluesky.examples import NullStatus
import filestore.commands as fs
from bluesky.callbacks import LiveTable, LivePlot, CallbackBase, LiveRaster
from ophyd import Device
import uuid
import h5py

class SRXFlyer1Axis(Device):
    LARGE_FILE_DIRECTORY_READ_PATH = '/tmp/test_data'
    LARGE_FILE_DIRECTORY_WRITE_PATH = '/tmp/test_data'
    "This is the Zebra."
    def __init__(self, encoder, *, fs=fs):
        super().__init__('', parent=None)
        self._mode = 'idle'
        self._encoder = encoder
        self._filestore_resource = None

        # gating info for encoder capture
        self.stage_sigs[self._encoder.pc.gate_num] = 1
        self.stage_sigs[self._encoder.pc.pulse_start] = 0

        #pc gate output is 31 for zebra.  use it to trigger xspress3 and I0
        self.stage_sigs[self._encoder.output1.ttl.addr] = 31
        self.stage_sigs[self._encoder.output3.ttl.addr] = 31
        
        self.stage_sigs[self._encoder.pc.enc_pos1_sync] = 1 

        self._encoder.pc.block_state_reset.put(1)

    def stage(self):
        super().stage()

    def describe_collect(self):

        if self._filestore_resource is not None:
            ext_spec = 'FileStore::{!s}'.format(self._filestore_resource['id'])
        else:
            ext_spec = 'FileStore:'

        spec = {'external': ext_spec,
            'dtype' : 'array',
            'shape' : [self._npts],
            'source': ''  # make this the PV of the array the det is writing
        }

        desc = OrderedDict()
        for chan in ('time','enc1'):
            desc[chan] = spec
            desc[chan]['source'] = getattr(self._encoder.pc.data, chan).pvname

        return {'stream0':desc}

    def kickoff(self, *, xstart, xstop, xnum, dwell):
        self._mode = 'kicked off'
        self._npts = int(xnum)
        extent = xstop - xstart
        self._encoder.pc.gate_start.put(xstart)
        self._encoder.pc.gate_step.put(extent)
        self._encoder.pc.gate_width.put(extent)
        self._encoder.pc.pulse_max.put(xnum)
        self._encoder.pc.pulse_step.put(dwell)
        self._encoder.pc.pulse_width.put(dwell - 0.005)
        self._encoder.pc.arm.put(1)
        st = NullStatus()  # TODO Return a status object *first* and do the above asynchronously.
        return st

    def complete(self):
        """
        Call this when all needed data has been collected. This has no idea
        whether that is true, so it will obligingly stop immediately. It is
        up to the caller to ensure that the motion is actually complete.
        """
        # Our acquisition complete PV is : XF:05IDD-ES:1{Dev:Zebra1}:ARRAY_ACQ
        while self._encoder.pc.data_in_progress is 1:
            poll()
        self._mode = 'complete'
        # self._encoder.pc.arm.put(0)  # sanity check; this should happen automatically
        # this does the same as the above, but also aborts data collection
        self._encoder.pc.block_state_reset.put(1)
        return NullStatus()
    
    def collect(self):
        # Create records in the FileStore database.
        # move this to stage because I thinkt hat describe_collect needs the
        # resource id
        self.__filename = '{}.h5'.format(uuid.uuid4())
        self.__read_filepath = os.path.join(self.LARGE_FILE_DIRECTORY_READ_PATH, self.__filename)
        self.__write_filepath = os.path.join(self.LARGE_FILE_DIRECTORY_WRITE_PATH, self.__filename)
        self.__filestore_resource = fs.insert_resource('ZEBRA_HDF51', self.__read_filepath)
        time_datum_id = str(uuid.uuid4())
        enc1_datum_id = str(uuid.uuid4())
        fs.insert_datum(self.__filestore_resource, time_datum_id, {'column': 'time'})
        fs.insert_datum(self.__filestore_resource, enc1_datum_id, {'column': 'enc1'})

        # Write the file.
        export_zebra_data(self._encoder, self.__write_filepath)

        # Yield a (partial) Event document. The RunEngine will put this
        # into metadatastore, as it does all readings.
        yield {'time': time.time(), 'seq_num': 1,
               'data': {'time': time_datum_id,
                        'enc1': enc1_datum_id},
               'timestamps': {'time': time_datum_id,  # not a typo
                              'enc1': time_datum_id}}
        self._mode = 'idle'
    
    def stop(self):
        pass

    def pause(self):
        "Pausing in the middle of a kickoff nukes the partial dataset."
        self._encoder.arm.put(0)
        self._mode = 'idle'
        self.unstage()

    def resume(self):
        self.stage()


flying_zebra = SRXFlyer1Axis(zebra)


def export_zebra_data(zebra, filepath):
    data = zebra.pc.data.get()
    size = (len(data.time),)
    with h5py.File(filepath, 'w') as f:
        dset0 = f.create_dataset("time",size,dtype='f')
        dset0[...] = np.array(data.time)
        dset1 = f.create_dataset("enc1",size,dtype='f')
        dset1[...] = np.array(data.enc1)
        dset0.flush()
        dset1.flush()
        f.close()


class ZebraHDF5Handler:
    def __init__(self, resource_fn):
        self._handle = h5py.File(resource_fn, 'r')

    def __call__(self, *, column):
        return self._handle[column]


db.fs.register_handler('ZEBRA_HDF51', ZebraHDF5Handler, overwrite=True)


class LiveZebraPlot(CallbackBase):
    """
    This is a really dumb approach but it gets the job done. To fix later.
    """

    def __init__(self, ax=None):
        self._uid = None
        self._desc_uid = None
        if ax is None:
            fig, ax = plt.subplots()
        self.ax = ax
        self.legend_title = 'sequence #'

    def start(self, doc):
        self._uid = doc['uid']

    def descriptor(self, doc):
        if doc['name'] == 'stream0':
            self._desc_uid = doc['uid']

    def bulk_events(self, docs):
        # Don't actually use the docs, but use the fact that they have been
        # emitted as a signal to go grab the data from the databroker now.
        event_uids = [doc['uid'] for doc in docs[self._desc_uid]]
        events = db.get_events(db[self._uid], stream_name='stream0', fill=True)
        for event in events:
            if event['uid'] in event_uids:
                self.ax.plot(event['data']['time'], event['data']['enc1'], label=event['seq_num'])
        self.ax.legend(loc=0, title=self.legend_title)

    def stop(self, doc):
        self._uid = None
        self._desc_uid = None


def scan_and_fly(xstart, xstop, xnum, ystart, ystop, ynum, dwell, *,
                 delta=None,
                 xmotor=hf_stage.x, ymotor=hf_stage.y,
                 xs=xs, ion=current_preamp.ch2,
                 flying_zebra=flying_zebra, md=None):
    """

    Monitor IO.
    Zebra buffers x(t) points as a flyer.
    Xpress3 is our detector.
    The aerotech has the x and y positioners.
    """
    if md is None:
        md = {}
    if delta is None:
        delta=0.01
    md = ChainMap(md, {
        'plan_name': 'scan_and_fly',
        'detectors': [zebra.name,xs.name,ion.name],
        'dwell' : dwell,
        }
    )

    from bluesky.plans import stage, unstage
    @stage_decorator([xs])
    def fly_each_step(detectors, motor, step):
        "See http://nsls-ii.github.io/bluesky/plans.html#the-per-step-hook"
        # First, let 'scan' handle the normal y step, including a checkpoint.
        yield from one_1d_step(detectors, motor, step)

        # Now do the x steps.
        yield from abs_set(xmotor, xstart - delta, wait=True) # ready to move
        v = (xstop - xstart) / xnum / dwell  # compute "stage speed"
        yield from abs_set(xmotor.velocity, v)  # set the "stage speed"
        yield from abs_set(xs.hdf5.num_capture, xnum)
        yield from abs_set(xs.settings.num_images, xnum)
        # arm the Zebra (start caching x positions)
        yield from kickoff(flying_zebra, xstart=xstart, xstop=xstop, xnum=xnum, dwell=dwell, wait=True)
        yield from abs_set(xs.settings.acquire, 1)  # start acquiring images
        yield from abs_set(xmotor, xstop+delta, wait=True)  # move in x
        yield from abs_set(xs.settings.acquire, 0)  # stop acquiring images
        yield from complete(flying_zebra)  # tell the Zebra we are done
        yield from collect(flying_zebra)  # extract data from Zebra
        yield from abs_set(xmotor.velocity, 3.)  # set the "stage speed"

    @subs_decorator([LiveTable([ymotor]), LiveRaster((ynum, xnum), ion.name), LiveZebraPlot()])
    #@subs_decorator([LiveTable([ymotor]), LiveRaster((ynum, xnum), xs.channel1.rois.roi03.value.name), LiveZebraPlot()])
    @monitor_during_decorator([ion], run=False)  # monitor values from ion
    #@monitor_during_decorator([xs], run=False)  # monitor values from xs
    @stage_decorator([flying_zebra])  # Below, 'scan' stage ymotor.
    @run_decorator(md=md)
    def plan():
        #yield from abs_set(xs.settings.trigger_mode, 'TTL Veto Only')
        yield from abs_set(xs.external_trig, True)
        for step in np.linspace(ystart, ystop, ynum):
            yield from fly_each_step([], ymotor, step)
        #yield from abs_set(xs.settings.trigger_mode, 'Internal')
        yield from abs_set(xs.external_trig, False)

    return (yield from plan())
