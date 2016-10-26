from ophyd import EpicsMotor, EpicsSignalRO, EpicsSignal, PVPositionerPC
from ophyd import Device
from ophyd import Component as Cpt
#motors for xrf, tomo, etc. go here

#piezo_jena_settle_time = 0.7 #conservative
piezo_jena_settle_time = 0.7

#High Flux KB mirrors

class SRX_M2(Device):
    """Class for 
    """
    yaw = Cpt(EpicsMotor, 'Yaw}Mtr')
    pitch = Cpt(EpicsMotor, 'P}Mtr')
    roll = Cpt(EpicsMotor, 'R}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    xu = Cpt(EpicsMotor, 'XU}Mtr')
    xd = Cpt(EpicsMotor, 'XD}Mtr')


class SRX_M2_All(SRX_M2):
    # This is here because it does not work right and gets stuck
    x = Cpt(EpicsMotor, 'X}Mtr')
    # the following are read-only signals because they shall not be moved indvidually 
    yui = Cpt(EpicsSignalRO, 'YUI}Mtr.VAL')
    yuo = Cpt(EpicsSignalRO, 'YUO}Mtr.VAL')
    ydi = Cpt(EpicsSignalRO, 'YDI}Mtr.VAL')
    ydo = Cpt(EpicsSignalRO, 'YDO}Mtr.VAL')


m2 = SRX_M2('XF:05IDD-OP:1{Mir:2-Ax:', name='m2')
m2_all = SRX_M2_All('XF:05IDD-OP:1{Mir:2-Ax:', name='m2_all')
relabel_motors(m2)
relabel_motors(m2_all)

class SRX_M3(Device):
    """Class for 
    """
    x = Cpt(EpicsMotor, 'X}Mtr')
    pitch = Cpt(EpicsMotor, 'P}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    xu = Cpt(EpicsMotor, 'XU}Mtr')
    xd = Cpt(EpicsMotor, 'XD}Mtr')

m3 = SRX_M3('XF:05IDD-OP:1{Mir:3-Ax:', name='m3')
relabel_motors(m3)


#High flux sample stages
class HFSampleStage(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')    
    z = Cpt(EpicsMotor, 'Z}Mtr')
    # for NPoint
    # fine_x = 
    # fine_y = 

hf_stage = HFSampleStage('XF:05IDD-ES:1{Stg:Smpl1-Ax:', name='hf_stage')
relabel_motors(hf_stage)

#SDD motion
class SRXUpStreamGantry(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')

sdd_pos = SRXUpStreamGantry('XF:05IDD-ES:1{Det:1-Ax:', name='sdd_pos')
relabel_motors(sdd_pos)

# PCOEdge detector motion
class SRXDownStreamGantry(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    z = Cpt(EpicsMotor, 'Z}Mtr')
    focus = Cpt(EpicsMotor, 'Foc}Mtr')

pcoedge_pos = SRXDownStreamGantry('XF:05IDD-ES:1{Det:3-Ax:', name='pcoedge_pos')
relabel_motors(pcoedge_pos)

class PICOECC100(PVPositionerPC):
    setpoint = Cpt(EpicsSignal,'CMD:TARGET')
    readback = Cpt(EpicsSignalRO, 'POSITION')


# tomography setup
class SRXTomo(Device):
    y = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:Y}Mtr')
    theta = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:Theta}Mtr')
    roll = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:R}Mtr')
    pitch = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:P}Mtr')

    #Attobcube ECS5050 
    #XF:05IDD-ES:1{Stg:Tomo-Ax:X}Mtr.RBV
    x = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:X}Mtr')
    z = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:Z}Mtr')
#    x = PICOECC100('XF:05IDD-ES:1{Stg:Tomo-Ax:X}')
#    z = PICOECC100('XF:05IDD-ES:1{Stg:Tomo-Ax:Z}')

    #Attobcube ECS3030
    #XF:05IDD-ES:2{Stg:Tomo-Ax:XFB}Mtr.RBV
    finex_bot = Cpt(EpicsMotor, ':2{Stg:Tomo-Ax:XFB}Mtr')
    finez_bot = Cpt(EpicsMotor, ':2{Stg:Tomo-Ax:ZFB}Mtr')
#    finex_bot = PICOECC100('XF:05IDD-ES:1{Stg:Tomo-Ax:XFB}')
#    finez_bot = PICOECC100('XF:05IDD-ES:1{Stg:Tomo-Ax:ZFB}')

    #PiezoJena   
    finex_top = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:XFT}Mtr', settle_time = piezo_jena_settle_time)
    finey_top = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:YFT}Mtr', settle_time = piezo_jena_settle_time) 
    finez_top = Cpt(EpicsMotor, ':1{Stg:Tomo-Ax:ZFT}Mtr', settle_time = piezo_jena_settle_time) 

#tomo_stage = SRXTomo('XF:05IDD-ES:1{Stg:Tomo-Ax:', name='tomo_stage')
tomo_stage = SRXTomo('XF:05IDD-ES', name='tomo_stage')
relabel_motors(tomo_stage)
