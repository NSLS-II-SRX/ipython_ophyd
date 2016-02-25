# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:57:20 2016

@author: xf05id1
"""

from bluesky.suspenders import PVSuspendFloor, PVSuspendCeil, PVSuspendBoolHigh

ring_current_pv = 'SR:C03-BI{DCCT:1}I:Real-I'
cryo_v19_pv = 'XF:05IDA-UT{Cryo:1-IV:19}Sts-Sts'
fe_shutter_status_pv = 'XF:05ID-PPS{Sh:WB}Sts:Cls-Sts' #0 = open, 1 = close
a_shutter_status_pv = 'XF:05IDA-PPS:1{PSh:2}Sts:Cls-Sts' 
b_shutter_status_pv = 'XF:05IDB-PPS:1{PSh:4}Sts:Cls-Sts'

#PVSuspendFloor(RE, ring_current.pvname, 120, resume_thresh=149, sleep = 10*60)
#PVSuspendCeil(RE, cryo_v19_pv, 0.8, resume_thresh=0.2, sleep = 20*60)
#PVSuspendBoolHigh(RE, fe_shutter_status_pv, sleep = 10*60)
#PVSuspendBoolHigh(RE, a_shutter_status_pv, sleep = 60)
#PVSuspendBoolHigh(RE, b_shutter_status_pv, sleep = 10)