# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 08:32:39 2016
set up all user specific information

@author: xf05id1
"""
import os
import scanoutput
import time
import shutil

#user experiment will be put into the Start Document for every scan

proposal_num = None
proposal_title = None
PI_lastname = None
saf_num = None


#proposal_num = 302249
#proposal_title = 'Fast in-situ Probing Local Synthesis Reactions using X-ray Fluorescence Microscopy'
#PI_lastname = 'Wang'
#saf_num = 302307

proposal_num = 302925
proposal_title = 'Routine Setup and Testing for Beamline 5-ID'
PI_lastname = 'Chu'
saf_num = 301967

"""
proposal_num = 303140
proposal_title = 'Teacher and Student Workshop: Imaging with a New Light'
PI_lastname = 'Perez'
saf_num = 302695
"""
"""
proposal_num = 302314
proposal_title = 'Investigation of space-weathered minerals'
PI_lastname = 'Legett'
saf_num = 302682
"""

#proposal_num = 302204
#proposal_title = 'Determining the Provenance of Glacial Erratics found on the North Shore of Long Island Based on XRF Geochronology of he #Mineral Monazite'
#PI_lastname = 'Mozer'
#saf_num = 302185

#proposal_num = 302217
#proposal_title = 'Using X-Ray Fluorescence and Absorption Spectroscopy to Analyze Heavy Element and Metal Contaminants in the Tissues of #Predatory Arachnids Residing Near the Forge River Polluted Water System in Shirley, New York'
#PI_lastname = 'DAmbrosia'
#saf_num = 302142

#proposal_num = 303121
#proposal_title = 'In-situ studies of the local phase transformation dynamics within single particles during the calcination of layered Ni-#rich oxides'
#PI_lastname = 'Zhang'
#saf_num = 302608

#proposal_num = 301962
#proposal_title = 'Characterization of single crystal growth in glass by laser heating'
#PI_lastname = 'Jain'
#saf_num = 302040

#proposal_num = 302659
#proposal_title = 'Resolving the Electroactive Interface of CuFe2O4 composite battery electrodes: An Operando XRF mapping / XANES Investigation'
#PI_lastname = 'Bock'
#saf_num = 302104

#proposal_num = 302712
#proposal_title = 'Modeling Microscale Arsenic Reactivity in Complex Soil Matrices'
#PI_lastname = 'Sharma'
#saf_num = 302059

#proposal_num = 302252
#proposal_title = 'Spectro-microscopic study of intermetallic particles in aluminum alloys'
#PI_lastname = 'Chou'
#saf_num = 302074

#proposal_num = 302825
#proposal_title = 'Use of X-ray spectromicroscopic techniques on understanding the effect of sea-level rise on the production and breakdown of natural organohalogens in coastal wetlands'
#PI_lastname = 'Schlesinger'
#saf_num = 302026

#proposal_num = 302315
#proposal_title = 'Elucidating nanoparticle-plant leaf interactions, uptake, and mobility for designing highly efficient foliar-applied #agrochemicals'
#PI_lastname = 'Avellan'
#saf_num = 302330

#proposal_num = 302773
#proposal_title = 'Understanding Copper Speciation in Brain Amyloid Deposits Involved in Cognitive Impairment'
#PI_lastname = 'Miller'
#saf_num = 302361


logfilename_postfix = str(saf_num)

cycle = '2018_cycle2'

RE.md['proposal']  = {  'proposal_num': str(proposal_num),
                         'proposal_title': str(proposal_title),
                            'PI_lastname': str(PI_lastname),
                                'saf_num': str(saf_num),
                                  'cycle': str(cycle)
                        }


userdatadir = '/nfs/xf05id1/userdata/'+str(cycle)+'/'+str(saf_num)+'_'+str(PI_lastname)+'/'
scriptdir = '/nfs/xf05id1/src/bluesky_scripts/'
scanoutput._DEFAULT_FILEDIR = userdatadir

try:
    os.makedirs(userdatadir, exist_ok=True)
except Exception as e:
    print(e)
    print('cannot create directory:' + userdatadir)
    sys.exit()


userlogfile = userdatadir+'logfile'+logfilename_postfix+'.txt'

import os.path
if not os.path.exists(userlogfile):
    userlogf = open(userlogfile, 'w')
    userlogf.close()

for f in ['simple_batch.py','fly_batch.py']:
    if not os.path.exists(userdatadir+f):
        shutil.copyfile(scriptdir+f,userdatadir+f)
try:
    os.unlink('/home/xf05id1/current_user_data')
except FileNotFoundError:
    print("[W] Previous user data directory link did not exist!")

os.symlink(userdatadir,'/home/xf05id1/current_user_data')
def logscan(scantype):
    h=db[-1]
    scan_id = h.start['scan_id']
    uid = h.start['uid']

    userlogf = open(userlogfile, 'a')
    userlogf.write(str(scan_id)+'\t'+uid+'\t'+scantype+'\n')
    userlogf.close()

def logscan_event0info(scantype, event0info = []):
    h=db[-1]
    scan_id = h.start['scan_id']
    uid = h.start['uid']

    userlogf = open(userlogfile, 'a')
    userlogf.write(str(scan_id)+'\t'+uid+'\t'+scantype)
    events = list(db.get_events(h, stream_name='primary'))

    for item in event0info:
        userlogf.write('\t'+item+'='+str(events[0]['data'][item])+'\t')
    userlogf.write('\n')
    userlogf.close()

def metadata_record():
    RE.md['beamline_status']  = {'energy':  energy.energy.position
                                #'slt_wb': str(slt_wb.position),
                                #'slt_ssa': str(slt_ssa.position)
                                }

    RE.md['initial_sample_position'] = {'hf_stage_x': hf_stage.x.position,
                                       'hf_stage_y': hf_stage.y.position,
                                       'hf_stage_z': hf_stage.z.position}
    RE.md['wb_slits'] = {'v_gap' : slt_wb.v_gap.position,
                            'h_gap' : slt_wb.h_gap.position,
                            'v_cen' : slt_wb.v_cen.position,
                            'h_cen' : slt_wb.h_cen.position
                            }
    RE.md['hfm'] = {'y' : hfm.y.position,
                               'bend' : hfm.bend.position}
    RE.md['ssa_slits'] = {'v_gap' : slt_ssa.v_gap.position,
                            'h_gap' : slt_ssa.h_gap.position,
                            'v_cen' : slt_ssa.v_cen.position,
                            'h_cen' : slt_ssa.h_cen.position
                             }

def logscan_detailed(scantype):
    h=db[-1]
    scan_id = h.start['scan_id']
    uid = h.start['uid']

    userlogf = open(userlogfile, 'a')
    userlogf.write(str(scan_id)+'\t'+uid+'\t'+scantype+'\t'+str(h['start']['scan_params'])+'\n')
    userlogf.close()

def scantime(scanid, printresults=True):
    '''
    input: scanid
    return: start and stop time stamps as strings
    '''
    start_str = 'scan start: '+time.ctime(db[scanid].start['time'])
    stop_str  = 'scan stop : '+time.ctime(db[scanid].stop['time'])
    totaltime = db[scanid].stop['time'] - db[scanid].start['time']
    scannumpt = len(list(db.get_events(db[scanid])))

    if printresults is True:
        print(start_str)
        print(stop_str)
        print('total time:', totaltime, 's')
        print('number of points:', scannumpt)
        print('scan time per point:', totaltime/scannumpt, 's')
    return db[scanid].start['time'], db[scanid].stop['time'], start_str, stop_str

def timestamp_batchoutput(filename = 'timestamplog.text', initial_scanid = None, final_scanid = None):
    f = open(filename,'w')
    for scanid in range(initial_scanid, final_scanid+1):
        f.write(str(scanid)+'\n')
        try:
            start_t, stop_t = scantime(scanid)
            f.write(start_t)
            f.write('\n')
            f.write(stop_t)
            f.write('\n')
        except:
            f.write('scan did no finish correctly.\n')
    f.close()

def scantime_batchoutput(filename = 'scantimelog.txt', scanlist = []):

    f = open(filename, 'w')
    f.write('scanid\tstartime(s)\tstoptime(s)\tstartime(date-time)\tstoptime(date-time)\n')
    for i in scanlist:
        starttime_s, endtime_s, starttime, endtime = scantime(i, printresults=False)
        f.write(str(i)+'\t'+str(starttime_s)+'\t'+str(endtime_s)+'\t'+starttime[12::]+'\t'+endtime[12::]+'\n')
    f.close()
