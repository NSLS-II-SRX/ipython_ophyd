# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:57:20 2016

Define suspenders that will be loaded

@author: xf05id1
"""
from bluesky.suspenders import SuspendFloor, SuspendCeil, SuspendBoolHigh, SuspendBoolLow
import bluesky.plans as bp
import bluesky.plan_stubs as bps
import bluesky.preprocessors as bpp

def shuttergenerator(shutter, value):
    return (yield from bpp.rewindable_wrapper(bps.mv(shutter, value), False))

#ring current suspender
# old values 140, resume=160
susp_rc = SuspendFloor(ring_current, 140, resume_thresh=160, sleep=10*60,
                       pre_plan=list(shuttergenerator(shut_b, 'Close')),
                       post_plan=list(shuttergenerator(shut_b, 'Open'))
                       )
#susp_rc = SuspendFloor(ring_current, 140, resume_thresh=140, sleep=10*60,
#                       pre_plan=bp.abs_set(shut_b, 0), post_plan=bp.mv(shut_b, 1)
#                      ) 

#cryo cooler suspender
#cryo_v19 = EpicsSignal('XF:05IDA-UT{Cryo:1-IV:19}Sts-Sts', name='cryo_v19')
susp_cryo = SuspendCeil(cryo_v19, 0.8, resume_thresh=0.2, sleep=15*60,
                        pre_plan=list(shuttergenerator(shut_b, 'Close')),
                        post_plan=list(shuttergenerator(shut_b, 'Open'))
)
#susp_cryo = SuspendCeil(cryo_v19, 0.8, resume_thresh=0.2, sleep=15*60,
#                        pre_plan=bp.abs_set(shut_b, 0), post_plan=bp.mv(shut_b, 1)
#                       ) 

#shutter status suspender
#susp_shut_fe = SuspendBoolHigh(shut_fe.close_status, sleep = 5*60,
#                               pre_plan=list(shuttergenerator(shut_b, 'Close')),
#                               post_plan=list(shuttergenerator(shut_b, 'Open')))
susp_shut_a = SuspendBoolHigh(shut_a.close_status, sleep = 10)
susp_shut_b = SuspendBoolHigh(shut_b.close_status, sleep = 10)
#susp_shut_fe = SuspendBoolHigh(shut_fe.close_status, sleep = 10)

susp_shut_fe = SuspendBoolHigh(shut_fe.close_status, sleep = 0,
                            pre_plan=list(shuttergenerator(shut_a, 'Close')),
                            post_plan=list(shuttergenerator(shut_a, 'Open'))
)
#susp_shut_a = SuspendBoolHigh(shut_a.close_status, sleep = 10,
#                              pre_plan=list(shuttergenerator(shut_b, 'Close')),
#                              post_plan=list(shuttergenerator(shut_b, 'Open'))
#                              ) 

#HDCM bragg temperature suspender
#dcm_bragg_temp = EpicsSignal('XF:05IDA-OP:1{Mono:HDCM-Ax:P}T-I', name='dcm_bragg_temp')
#susp_dcm_bragg_temp = SuspendCeil(dcm_bragg_temp, 120, resume_thresh=70, sleep = 10)
#susp_dcm_bragg_temp = SuspendCeil(dcm.temp_pitch, 120, resume_thresh=70, sleep = 10)
#susp_dcm_bragg_temp = SuspendCeil(dcm.temp_pitch, 120, resume_thresh=70, sleep = 1)
susp_dcm_bragg_temp = SuspendCeil(dcm.temp_pitch, 120, resume_thresh=118, sleep = 1)
#susp_dcm_bragg_temp = SuspendCeil(dcm.temp_pitch, 100, resume_thresh=98, sleep = 10,
#                        pre_plan=bp.mv(shut_b, 0), post_plan=bp.mv(shut_b, 1)
#                       ) 

# 
RE.install_suspender(susp_rc)
RE.install_suspender(susp_shut_fe)
RE.install_suspender(susp_dcm_bragg_temp)

#RE.install_suspender(susp_cryo)
#RE.install_suspender(susp_shut_a)
#RE.install_suspender(susp_shut_b)

#example:
#gv = EpicsSignal('XF:05IDA-VA:1{BPM:1-GV:1}Pos-Sts')
#susp_gv = SuspendBoolLow(gv)
#RE.install_suspender(susp_gv)
