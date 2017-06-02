import time as ttime
import datetime
import os
import epics
from ophyd import (PVPositioner, EpicsSignal, EpicsSignalRO, EpicsMotor,
                   Device, Signal, PseudoPositioner, PseudoSingle)
from ophyd.utils.epics_pvs import set_and_wait
from ophyd.ophydobj import StatusBase, MoveStatus
from ophyd.pseudopos import (pseudo_position_argument, real_position_argument)
from ophyd import Component as Cpt
from scipy.interpolate import InterpolatedUnivariateSpline

ring_current = EpicsSignalRO('SR:C03-BI{DCCT:1}I:Real-I', name='ring_current')
cryo_v19 = EpicsSignal('XF:05IDA-UT{Cryo:1-IV:19}Sts-Sts', name='cryo_v19')

class UVDone(Signal):
    def __init__(self, parent, brake, readback, err, stp, **kwargs):
        super().__init__(parent=parent, value=1, **kwargs)
        self._rbv = readback
        self._brake = brake
        self._started = False
        self._err = err
        self._stp = stp
        self.target = None

    def put(self, *arg, **kwargs):
        raise TypeError("You con not tell an undulator it is done")

    def _put(self, *args, **kwargs):
        return super().put(*args, **kwargs)

    def _watcher(self, obj=None, value=None, **kwargs):
        target = self.target
        rbv = getattr(self.parent, self._rbv)
        cur_value = rbv.get()
        brake = getattr(self.parent, self._brake)
        brake_on = brake.get()

        err_str = getattr(self.parent, self._err).get()
        if not self._started:
            self._started = not brake_on
        # come back and check this threshold value
        #if brake_on and abs(target - cur_value) < 0.002:
        if abs(target - cur_value) < 0.001:
            self._put(1)
            rbv.clear_sub(self._watcher)
            brake.clear_sub(self._watcher)
            self._started = False

        elif brake_on:
            if err_str:
                self._put(1)
                rbv.clear_sub(self._watcher)
                brake.clear_sub(self._watcher)
                self._started = False
            elif self._started:
                print(self.parent.name, ": reactuated due to not reaching target")
                self.parent.actuate.put(self.parent.actuate_value)

    def _stop_watcher(self, *arg, **kwargs):
        '''Call back to be installed on the stop signal

        if this gets flipped, clear all of the other callbacks and tell
        the status object that it is done.

        TODO: mark status object as failed
        TODO: only trigger this on 0 -> 1 transposition
        '''
        print('STOPPED')
        # set the target to None and remove all callbacks
        self.reset(None)
        # flip this signal to 1 to signal it is done
        self._put(1)
        # push stop again 'just to be safe'
        # this is paranoia related to the re-kicking the motor is the
        # other callback
        stop = getattr(self.parent, self._stp)
        stop.put(1)

    def reset(self, target):
        self.target = float(target)
        self._put(0)
        self._remove_cbs()
        self._started = False
 
    def _remove_cbs(self):
        rbv = getattr(self.parent, self._rbv)
        stop = getattr(self.parent, self._stp)
        moving = getattr(self.parent, self._brake)

        rbv.clear_sub(self._watcher)
        moving.clear_sub(self._watcher)
        stop.clear_sub(self._stop_watcher)

    def stop(self):
        self.reset(None)
        self._put(1)
        

class URealPos(Device):
    #undulator real position, gap and taper
    ds_low = Cpt(EpicsSignalRO, '}REAL_POSITION_DS_LOWER')
    ds_upp = Cpt(EpicsSignalRO, '}REAL_POSITION_DS_UPPER')
    us_low = Cpt(EpicsSignalRO, '}REAL_POSITION_US_LOWER')
    us_upp = Cpt(EpicsSignalRO, '}REAL_POSITION_US_UPPER')


class UPos(Device):
    #undulator positions, gap and taper
    ds_low = Cpt(EpicsSignalRO, '}POSITION_DS_LOWER')
    ds_upp = Cpt(EpicsSignalRO, '}POSITION_DS_UPPER')
    us_low = Cpt(EpicsSignalRO, '}POSITION_US_LOWER')
    us_upp = Cpt(EpicsSignalRO, '}POSITION_US_UPPER')

class GapPos(Device):
    gap_avg = Cpt(EpicsSignalRO, '}GAP_AVG')
    gap_ds = Cpt(EpicsSignalRO, '}GAP_DS')
    gap_us = Cpt(EpicsSignalRO, '}GAP_US')
    gap_taper = Cpt(EpicsSignalRO, '}GAP_TAPER')


class Girder(Device):
    lower_tilt = Cpt(EpicsSignalRO, '}GIRDER_LOWER_TILT')
    upper_tile = Cpt(EpicsSignalRO, '}GIRDER_UPPER_TILT')
    tilt_error = Cpt(EpicsSignalRO, '}GIRDER_TILT_ERROR')
    tilt_limit = Cpt(EpicsSignalRO, '}GIRDER_TILT_LIMIT')


class Elev(Device):
    ct_us =     Cpt(EpicsSignalRO, '-LEnc:1}Pos')
    offset_us = Cpt(EpicsSignalRO, '-LEnc:1}Offset:RB')
    ct_ds =     Cpt(EpicsSignalRO, '-LEnc:6}Pos')
    offset_ds = Cpt(EpicsSignalRO, '-LEnc:6}Offset:RB')


class FixedPVPositioner(PVPositioner):
    """This subclass ensures that the setpoint is really set before
    """
    def _move_async(self, position, **kwargs):
        '''Move and do not wait until motion is complete (asynchronous)'''
        if self.actuate is not None:
            set_and_wait(self.setpoint, position)
            self.actuate.put(self.actuate_value, wait=False)
        else:
            self.setpoint.put(position, wait=False)
    
    def move(self, v, *args, **kwargs):
        kwargs['timeout'] = None
        self.done.reset(v)
        ret = super().move(v, *args, **kwargs)
        self.brake_on.subscribe(self.done._watcher,
                                event_type=self.brake_on.SUB_VALUE)
        self.readback.subscribe(self.done._watcher,
                                event_type=self.readback.SUB_VALUE)

        self.stop_signal.subscribe(self.done._stop_watcher,
                                   event_type=self.stop_signal.SUB_VALUE, run=False)
        return ret


class Undulator(FixedPVPositioner):
    # positioner signals
    setpoint = Cpt(EpicsSignal, '-Mtr:2}Inp:Pos')
    readback = Cpt(EpicsSignalRO, '-LEnc}Gap')
    stop_signal = Cpt(EpicsSignal, '-Mtrc}Sw:Stp')
    actuate = Cpt(EpicsSignal, '-Mtr:2}Sw:Go')
    actuate_value = 1
    done = Cpt(UVDone, None, brake='brake_on',
               readback='readback', err='err', stp='stop_signal',
               add_prefix=())

    # correction function signals, need to be merged into single object
    corrfunc_en = Cpt(EpicsSignal, '-MtrC}EnaAdj:out')
    corrfunc_dis = Cpt(EpicsSignal, '-MtrC}DisAdj:out')
    corrfunc_sta = Cpt(EpicsSignal, '-MtrC}AdjSta:RB')

    # brake status
    brake_on = Cpt(EpicsSignalRO, '-Mtr:2}Rb:Brk')

    # low-level positional information about undulator
    real_pos = Cpt(URealPos, '')
    pos = Cpt(UPos, '')
    girder = Cpt(Girder, '')
    elevation = Cpt(Elev, '')

    # error status
    err = Cpt(EpicsSignalRO, '-Motor}Err:GetCerr_.VALA', string=True)

    def move(self, v, *args, moved_cb=None, **kwargs):
        kwargs['timeout'] = None
        if np.abs(v - self.position) < .001:
            self._started_moving = True
            self._moving = False
            self._done_moving()
            st = MoveStatus(self, v)
            if moved_cb:
                moved_cb(obj=self)
            st._finished()
            return st
        return super().move(v, *args, moved_cb=moved_cb, **kwargs)

    def __init__(self, *args, calib_path=None, calib_file=None, **kwargs):
        super().__init__(*args, **kwargs)
        # todo make these error messages look more like standard exceptions
        if calib_path is None:
            raise TypeError("must provide calib_dir")
        if calib_file is None:
            raise TypeError("must provide calib_file")

        with open(os.path.join(calib_path, calib_file), 'r') as f:
            next(f)
            uposlistIn=[]
            elistIn=[]
            for line in f:
                num = [float(x) for x in line.split()]
                uposlistIn.append(num[0])
                elistIn.append(num[1])

        self.etoulookup = InterpolatedUnivariateSpline(elistIn, uposlistIn)
        self.utoelookup = InterpolatedUnivariateSpline(uposlistIn, elistIn)

    def _move_changed(self, timestamp=None, value=None, sub_type=None,
                      **kwargs):
        was_moving = self._moving
        self._moving = (value != self.done_value)

        started = False
        if not self._started_moving:
            started = self._started_moving = (not was_moving and self._moving)

        if started:
            self._run_subs(sub_type=self.SUB_START, timestamp=timestamp,
                           value=value, **kwargs)

        if not self.put_complete:
            success = not bool(self.err.get())
            # In the case of put completion, motion complete
            if was_moving and not self._moving:
                self._done_moving(success=success, timestamp=timestamp,
                                  value=value)

    def stop(self, success=True):
        self.done.stop()
        return super().stop(success=success)

_undulator_kwargs = dict(name='ivu1_gap', read_attrs=['readback'],
                         calib_path='/nfs/xf05id1/UndulatorCalibration/',
                         #calib_file='SRXUgapCalibration20150411_final.text',
                         #calib_file='SRXUgapCalibration20160608_final.text',                                                  
                         calib_file='SRXUgapCalibration20170131.txt',                                                  
                         configuration_attrs=['corrfunc_sta', 'pos', 'girder',
                                              'real_pos', 'elevation'])


ANG_OVER_EV = 12.3984

class Energy(PseudoPositioner):
    # synthetic axis
    energy = Cpt(PseudoSingle)
    # real motors
    u_gap = Cpt(Undulator, 'SR:C5-ID:G1{IVU21:1', add_prefix=(), **_undulator_kwargs)
    bragg = Cpt(EpicsMotor, 'XF:05IDA-OP:1{Mono:HDCM-Ax:P}Mtr', add_prefix=(),
                read_attrs=['user_readback'])
    c2_x = Cpt(EpicsMotor, 'XF:05IDA-OP:1{Mono:HDCM-Ax:X2}Mtr', add_prefix=(),
                read_attrs=['user_readback'])
    epics_d_spacing = EpicsSignal('XF:05IDA-CT{IOC:Status01}DCMDspacing.VAL', 
        name='epics_d_spacing')
    epics_bragg_offset = EpicsSignal('XF:05IDA-CT{IOC:Status01}BraggOffset.VAL', 
        name='epics_bragg_offset')
    # motor enable flags
    move_u_gap = Cpt(Signal, None, add_prefix=(), value=True)
    move_c2_x = Cpt(Signal, None, add_prefix=(), value=True)
    harmonic = Cpt(Signal, None, add_prefix=(), value=None)

    # experimental
    detune = Cpt(Signal, None, add_prefix=(), value=0)

    def energy_to_positions(self, target_energy, undulator_harmonic, u_detune):
        """Compute undulator and mono positions given a target energy

        Paramaters
        ----------
        target_energy : float
            Target energy in keV

        undulator_harmonic : int, optional
            The harmonic in the undulator to use

        uv_mistune : float, optional
            Amount to 'mistune' the undulator in keV.  Will settings such that the
            peak of the undulator spectrum will be at `target_energy + uv_mistune`.

        Returns
        -------
        bragg : float
             The angle to set the monocromotor
        """
        # set up constants
        Xoffset = self._xoffset
        d_111 = self._d_111
        delta_bragg = self._delta_bragg
        C2Xcal = self._c2xcal
        T2cal = self._t2cal
        etoulookup = self.u_gap.etoulookup


        #calculate Bragg RBV
        BraggRBV = np.arcsin((ANG_OVER_EV / target_energy)/(2 * d_111))/np.pi*180 - delta_bragg

        #calculate C2X
        Bragg = BraggRBV + delta_bragg
        T2 = Xoffset * np.sin(Bragg * np.pi / 180)/np.sin(2 * Bragg * np.pi / 180)
        dT2 = T2 - T2cal
        C2X = C2Xcal - dT2

        #calculate undulator gap
        # TODO make this more sohpisticated to stay a fixed distance off the
        # peak of the undulator energy
        ugap = float(etoulookup((target_energy + u_detune)/undulator_harmonic))

        return BraggRBV, C2X, ugap

    def undulator_energy(self, harmonic=3):
        """Return the current enegry peak of the undulator at the given harmonic

        Paramaters
        ----------
        harmanic : int, optional
            The harmonic to use, defaults to 3
        """
        ugap = self.u_gap.get().readback
        utoelookup = self.u_gap.utoelookup

        fundemental = float(utoelookup(ugap))

        energy = fundemental * harmonic

        return energy

    def __init__(self, *args,
                 xoffset=None, d_111=None, delta_bragg=None, C2Xcal=None, T2cal=None,
                 **kwargs):
        super().__init__(*args, **kwargs)
        self._xoffset = xoffset
        self._d_111 = d_111
        self._delta_bragg = delta_bragg
        self._c2xcal = C2Xcal
        self._t2cal = T2cal


    def crystal_gap(self):
        """Return the current physical gap between first and second crystals
        """
        C2X = self.c2_x.get().user_readback
        bragg = self.bragg.get().user_readback

        T2cal = self._t2cal
        delta_bragg = self._delta_bragg
        d_111 = self._d_111
        c2x_cal = self._c2xcal

        Bragg = np.pi/180 * (bragg + delta_bragg)

        dT2 = c2x_cal - C2X
        T2 = dT2 + T2cal

        XoffsetVal = T2/(np.sin(Bragg)/np.sin(2*Bragg))

        return XoffsetVal

    @pseudo_position_argument
    def forward(self, p_pos):
        energy = p_pos.energy
        harmonic = self.harmonic.get()
        detune = self.detune.get()
        if energy <= 4.4:
            raise ValueError("The energy you entered is too low ({} keV). "
                             "Minimum energy = 4.4 keV".format(energy))
#        if energy >= 25:
#            raise ValueError('The energy you entered is too high ({} keV). '
#                             'Maximum energy = 25.0 keV'.format(energy))
        if (energy > 25.):
            if (energy < 4400.) or (energy > 25000.):
            #energy is invalid
                raise ValueError('The requested photon energy is invalid ({} keV). '
                             'Values must be in the range of 4.4 - 25 keV'.format(energy))
            else:
            #energy is in eV
                energy = energy / 1000.

        if harmonic is None:
            harmonic = 3
            #choose the right harmonic
            braggcal, c2xcal, ugapcal = self.energy_to_positions(energy, harmonic, detune)
            # try higher harmonics until the required gap is too small
            while True:
                braggcal, c2xcal, ugapcal = self.energy_to_positions(energy, harmonic + 2, detune)
                if ugapcal < 6.4:
                    break
                harmonic += 2

        # compute where we would move everything to in a perfect world
        bragg, c2_x, u_gap = self.energy_to_positions(energy, harmonic, detune)

        # sometimes move the crystal gap
        if not self.move_c2_x.get():
            c2_x = self.c2_x.position

        # sometimes move the undulator
        if not self.move_u_gap.get():
            u_gap = self.u_gap.position

        return self.RealPosition(bragg=bragg, c2_x=c2_x, u_gap=u_gap)

    @real_position_argument
    def inverse(self, r_pos):
        bragg = r_pos.bragg
        e = ANG_OVER_EV / (2 * self._d_111 * math.sin(math.radians(bragg + self._delta_bragg)))
        return self.PseudoPosition(energy=float(e))

    @pseudo_position_argument
    def set(self, position):
        return super().set([float(_) for _ in position])

    def synch_with_epics(self):
        self.epics_d_spacing.put(self._d_111)
        self.epics_bragg_offset.put(self._delta_bragg)

# change it to a better way to pass the calibration
cal_data_2016cycle1 = {'d_111': 3.12961447804,
                       'delta_bragg': 0.322545952931,
                       'C2Xcal': 3.6,
                       'T2cal': 13.463294326,
                       'xoffset': 25.2521}

cal_data_2016cycle1_2 = {'d_111': 3.12924894907,  # 2016/1/27 (Se, Cu, Fe, Ti)
                       'delta_bragg': 0.315532509387,  # 2016/1/27 (Se, Cu, Fe, Ti)
                       'delta_bragg': 0.317124613301,  # ? before 8/18/2016
                       #'delta_bragg': 0.357124613301,  # 2016/8/16 (Cu)
                       # not in energy axis but for the record
                       # 'C1Rcal' :  -4.88949983261, # 2016/1/29
                       'C2Xcal': 3.6,  # 2016/1/29
                       'T2cal': 13.7187120636,
                       #'xoffset': 25.01567531283996 #2016 Jan
                       #'xoffset': 24.756374595028607 #2016/2/25 on Rh stripe, y=10 mm
                       #'xoffset': 24.908823293008666 #2016/2/26 on Si stripe, y=5 mm
                       #'xoffset': 24.621311485825125 #2016/3/10 Fe edge
                       #'xoffset': 24.661899615539824 #2016/3/13 Pt edge
                       #'xoffset': 24.761023845083287 #2016/3/17 Zr edge, 18.2 keV
                       #'xoffset': 24.741174927854445 #2016/3/23 15 keV
                       #'xoffset': 24.593840056028178 #2016/3/26 10.5 keV W
                       #'xoffset': 24.773110163531658 #2016/3/26 18.0 keV U
                       #'xoffset':  24.615016005680289 #2016/4/06 12.8 keV Se
                       #'xoffset': 24.672213516710034
                       #'xoffset': 24.809807128906538
                       #mono warmed up at 4/12/16
                       #'xoffset': 24.809838976060604 #17keV
                       #'xoffset': 24.887490886653893 #8.2 keV
                       #'xoffset': 24.770168843970197 #12.5 keV
                       }  # 2016/1/29}

                        #2016-2
cal_data_2016cycle2  ={ #'d_111': 3.13130245128, #2016/6/9 (Ti, Cr, Fe, Cu, Se)
                        'd_111': 3.12929567478, #2016/8/1 (Ti, Fe, Cu, Se)
                        #'delta_bragg' : 0.309366522013,
                        #'delta_bragg' : 0.32936652201300004,
                        #'delta_bragg': 0.337124613301, 
                        'delta_bragg': 0.317124613301, #2016/8/16 (Ti, Cr, Fe, Cu, Se)
                        #'xoffset': 24.864494684263519,                                             
                        'C2Xcal': 3.6,  # 2016/1/29
                        'T2cal': 14.2470486188,
                        #'xoffset': 25.941277803299684
                        #'xoffset': 25.921698318063775
                        #'xoffset': 25.802588306223701 #2016/7/5 17.5 keV 
                        #'xoffset': 25.542954465467645 #2016/7/6 17.5 keV fullfield
                        #'xoffset': 25.39464922124886 #2016/7/20 13.5/6 keV microscopy
                        #'xoffset': 25.354968816872358 #2016/7/28 12-14 keV microscopy
                        #'xoffset': 25.414219669872864 #2016/8/2 14 keV
                        #'xoffset': 25.175826062860775 #2016/8/2 18 keV
                        'xoffset': 25.527059255709876 #2016/8/16 9 keV
                        #'xoffset': 25.487723997622723 #2016/8/18 11 keV
                        #'xoffset': 25.488305806234468, #2016/8/21 9.2 keV, aligned by Garth on 2016/8/20
                        #'C1Rcal':-4.7089492561 for the record
                      }

cal_data_2016cycle3  ={'d_111': 3.12941028109, #2016/10/3 (Ti, Fe, Cu, Se)
                       'delta_bragg': 0.317209816326, #2016/10/3 (Ti, Fe, Cu, Se)
                        'C2Xcal': 3.6,  # 2016/1/29
                        'T2cal': 14.2470486188,
#                        'xoffset': 25.056582386746765, #2016/10/3 9 keV
#                        'xoffset': 25.028130552150312, #2016/10/12 8 keV
#                        'xoffset': 25.182303347383915, #2016/10/24 7.4 keV
#                        'xoffset': 25.531497575767418, #2016/10/24 7.4 keV
                        'xoffset': 25.491819462118674, #2016/11/4 12.8 keV
                        #'C1Rcal': -5.03023390228  #for the record, 2016/10/3
                      }


cal_data_2017cycle1  ={#'d_111': 3.12988412345, #2017/1/17 (Ti, Cr, Fe, Cu, Se)
#                        'd_111': 3.13246886211,
#                        'delta_bragg': 0.298805934621, # Cu, Se 3/17/2017
#                        'd_111': 3.11630891423,
#                        'delta_bragg': 0.357259819067, # {'Cu':3941, 'Se':3940, 'V':3937, 'Ti':3946, 'Mn':3951} 3/23/2017
                        'd_111': 3.12969964541,
                        'delta_bragg': 0.306854237528, # {'Ni':4156, 'Co':4154, 'Mn':4152} 4/10/2017
#                        'd_111': 3.14434282312,
#                        'delta_bragg': 0.265291543541, # {'Se':4002, 'Ti':4004, 'Mn':4000} 4/05/2017 bad
#                       'delta_bragg': 0.314906135851, #2017/1/17 (Ti, Cr, Fe, Cu, Se)
#                       'delta_bragg': 0.33490613585100004, #2017/3/9 (peakup spectrum)
#                       'delta_bragg': 0.309906135851, #2017/3/17 (Cu)
                        'C2Xcal': 3.6,  # 2017/1/17
                        'T2cal': 15.0347755916,  # 2017/1/17
                        'xoffset': 25.4253705456081, #2017/1/17 12.6 keV
                        #'C1Rcal': -4.98854110244  #for the record, #2017/1/17
                      }
cal_data_2017cycle2 = {
 'd_111': 3.12894833524,
 'delta_bragg': 0.309484915727, #{'Ti':4843,'Mn':4845,'Cu':4847,'Se':4848} 20170525
 'C2Xcal': 3.6,
 'T2cal': 15.0347755916,
 'xoffset': 24.581644618999363, #value for Ti worked best using the C2 pitch to correct at higher E
}
energy = Energy(prefix='', name='energy', **cal_data_2017cycle2)
energy.synch_with_epics()


# Front End Slits (Primary Slits)
class SRXSlitsFE(Device):
    top = Cpt(EpicsMotor, '3-Ax:T}Mtr')
    bot = Cpt(EpicsMotor, '4-Ax:B}Mtr')
    inb = Cpt(EpicsMotor, '3-Ax:I}Mtr')
    out = Cpt(EpicsMotor, '4-Ax:O}Mtr')

fe = SRXSlitsFE('FE:C05A-OP{Slt:', name='fe')

_time_fmtstr = '%Y-%m-%d %H:%M:%S'

class TwoButtonShutter(Device):
    # TODO this needs to be fixed in EPICS as these names make no sense
    # the vlaue comingout of the PV do not match what is shown in CSS
    open_cmd = Cpt(EpicsSignal, 'Cmd:Opn-Cmd', string=True)
    open_val = 'Open'

    close_cmd = Cpt(EpicsSignal, 'Cmd:Cls-Cmd', string=True)
    close_val = 'Not Open'

    status = Cpt(EpicsSignalRO, 'Pos-Sts', string=True)

    close_status = Cpt(EpicsSignalRO, 'Sts:Cls-Sts')
    fail_to_close = Cpt(EpicsSignalRO, 'Sts:FailCls-Sts', string=True)
    fail_to_open = Cpt(EpicsSignalRO, 'Sts:FailOpn-Sts', string=True)
    # user facing commands
    open_str = 'Open'
    close_str = 'Close'

    def set(self, val):
        if self._set_st is not None:
            raise RuntimeError('trying to set while a set is in progress')

        cmd_map = {self.open_str: self.open_cmd,
                   self.close_str: self.close_cmd}
        target_map = {self.open_str: self.open_val,
                      self.close_str: self.close_val}

        cmd_sig = cmd_map[val]
        target_val = target_map[val]

        st = self._set_st = DeviceStatus(self)
        enums = self.status.enum_strs

        def shutter_cb(value, timestamp, **kwargs):
            value = enums[int(value)]
            if value == target_val:
                self._set_st._finished()
                self._set_st = None
                self.status.clear_sub(shutter_cb)
        uid = str(uuid.uuid4())
        cmd_enums = cmd_sig.enum_strs
        count = 0
        def cmd_retry_cb(value, timestamp, **kwargs):
            nonlocal count
            value = cmd_enums[int(value)]
            # ts = datetime.datetime.fromtimestamp(timestamp).strftime(_time_fmtstr)
            # print('sh', ts, val, st)
            if count > 5:
                cmd_sig.clear_sub(cmd_retry_cb)
                st._finished(success=False)
            if value == 'None':
                if not st.done:
                    time.sleep(1)
                    count += 1
                    cmd_sig.set(1)
                else:
                    cmd_sig.clear_sub(cmd_retry_cb)

        cmd_sig.subscribe(cmd_retry_cb, run=False)
        cmd_sig.set(1)
        self.status.subscribe(shutter_cb)
        return st

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._set_st = None
        self.read_attrs = ['status']



shut_fe = TwoButtonShutter('XF:05ID-PPS{Sh:WB}', name='shut_fe')
shut_a = TwoButtonShutter('XF:05IDA-PPS:1{PSh:2}', name='shut_a')
shut_b = TwoButtonShutter('XF:05IDB-PPS:1{PSh:4}', name='shut_b')

