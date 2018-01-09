from ophyd import EpicsMotor
from ophyd import Device
from ophyd import Component as Cpt
from ophyd import PVPositionerPC
from numpy import int16


class SRXSlitsWB(Device):
    # real synthetic axes
    h_cen = Cpt(EpicsMotor, 'XCtr}Mtr')
    h_gap = Cpt(EpicsMotor, 'XGap}Mtr')
    v_cen = Cpt(EpicsMotor, 'YCtr}Mtr')
    v_gap = Cpt(EpicsMotor, 'YGap}Mtr')
    
    # real motors
    top = Cpt(EpicsMotor, 'T}Mtr')
    bot = Cpt(EpicsMotor, 'B}Mtr')    
    inb = Cpt(EpicsMotor, 'I}Mtr')
    out = Cpt(EpicsMotor, 'O}Mtr')
    
class SRXSlitsPB(Device):
    # real synthetic axes
    h_cen = Cpt(EpicsMotor, 'XCtr}Mtr')
    h_gap = Cpt(EpicsMotor, 'XGap}Mtr')
    
    # real motors
    inb = Cpt(EpicsMotor, 'I}Mtr')
    out = Cpt(EpicsMotor, 'O}Mtr')


# Pseudo motion for slits
#class SRXSlits4SWPM(MagicSetPseudoPositioner):
    # real synthetic axes

#    h_cen = Cpt(FixedPseudoSingle)
#    h_gap = Cpt(FixedPseudoSingle)
#    v_cen = Cpt(FixedPseudoSingle)
#    v_gap = Cpt(FixedPseudoSingle)

    # real motors
#    top = Cpt(EpicsMotor, 'T}Mtr')
#    bot = Cpt(EpicsMotor, 'B}Mtr')
#    inb = Cpt(EpicsMotor, 'I}Mtr')
#    out = Cpt(EpicsMotor, 'O}Mtr')

    # zero positions
#    top_zero = Cpt(PermissiveGetSignal, None, add_prefix=(), value=None)
#    bot_zero = Cpt(PermissiveGetSignal, None, add_prefix=(), value=None)
#    inb_zero = Cpt(PermissiveGetSignal, None, add_prefix=(), value=None)
#    out_zero = Cpt(PermissiveGetSignal, None, add_prefix=(), value=None)

#    def forward(self, p_pos):
#        h_cen, h_gap, v_cen, v_gap = p_pos
        
#        zeros_pos = [getattr(self, k).get() for k in ['top_zero', 'bot_zero',
#                                                      'inb_zero', 'out_zero']]
#        if any([p is None for p in zeros_pos]):
#            raise RuntimeError("You must configure the zero positions")
#        top_zero, bot_zero, inb_zero, out_zero = zeros_pos
#
#        top = (v_cen + top_zero) + (v_gap / 2)
#        bot = (-v_cen + bot_zero) + (v_gap / 2)
        
#        inb = (-h_cen + inb_zero) + (h_gap / 2)
#        out = (h_cen + out_zero) + (h_gap / 2)

#        return self.RealPosition(top=top, bot=bot, inb=inb, out=out)

#    def inverse(self, r_pos):
#        top, bot, inb, out = r_pos

#        zeros_pos = [getattr(self, k).get() for k in ['top_zero', 'bot_zero',
#                                                      'inb_zero', 'out_zero']]
#        if any([p is None for p in zeros_pos]):
#            raise RuntimeError("You must configure the zero positions")
#        top_zero, bot_zero, inb_zero, out_zero = zeros_pos


        # have to flip one sign due to beamline slits coordinate system
#        v_cen = ((top - top_zero) - (bot - bot_zero)) / 2
#        v_gap = ((top - top_zero) + (bot - bot_zero))

#        h_cen = ((out - out_zero) - (inb - inb_zero)) / 2
#        h_gap = ((out - out_zero) + (inb - inb_zero))
        
#        return self.PseudoPosition(v_cen=v_cen, v_gap=v_gap,
#                                   h_cen=h_cen, h_gap=h_gap)

#    def set(self, *args):
#        v = self.PseudoPosition(*args)
#        return super().set(v)

class SRXSlits2(Device):
    inb = Cpt(EpicsMotor, 'I}Mtr')
    out = Cpt(EpicsMotor, 'O}Mtr')

## Pseudo motor for white beam slits
#slt_wb = SRXSlits4SWPM('XF:05IDA-OP:1{Slt:1-Ax:', name='slt_wb')
#slt_wb.top_zero.put(-5.775)
#slt_wb.bot_zero.put(-4.905)
#slt_wb.inb_zero.put(-6.705)
#slt_wb.out_zero.put(-4.345)
slt_wb = SRXSlitsWB('XF:05IDA-OP:1{Slt:1-Ax:', name='slt_wb')

## Pseudo motor for pink beam slits
#slt_pb = SRXSlits2('XF:05IDA-OP:1{Slt:2-Ax:', name='slt_pb')
slt_pb = SRXSlitsPB('XF:05IDA-OP:1{Slt:2-Ax:', name='slt_pb')

#class SRXSSAH(PVPositioner):
#    setpoint = Cpt(EpicsSignal,'X}size')
#    readback = Cpt(EpicsSignalRO, 'X}t2.C')
#    out = Cpt(EpicsMotor,'O}Mtr')
#    inb = Cpt(EpicsMotor,'I}Mtr')
#class SRXSSAV(PVPositioner):
#    setpoint = Cpt(EpicsSignal,'Y}size')
#    readback = Cpt(EpicsSignalRO, 'Y}t2.C')
#    top = Cpt(EpicsMotor,'T}Mtr')
#    bot = Cpt(EpicsMotor,'B}Mtr')

class SRXSSAHG(PVPositionerPC):
    setpoint = Cpt(EpicsSignal,'X}size')
    readback = Cpt(EpicsSignalRO, 'X}t2.C')
class SRXSSAHC(PVPositionerPC):
    setpoint = Cpt(EpicsSignal,'X}center')
    readback = Cpt(EpicsSignalRO, 'X}t2.D')
class SRXSSAVG(PVPositionerPC):
    setpoint = Cpt(EpicsSignal,'Y}size')
    readback = Cpt(EpicsSignalRO, 'Y}t2.C')
class SRXSSAVC(PVPositionerPC):
    setpoint = Cpt(EpicsSignal,'Y}center')
    readback = Cpt(EpicsSignalRO, 'Y}t2.D')

class SRXSSACalc(Device):
    h_cen = SRXSSAHC('XF:05IDB-OP:1{Slt:SSA-Ax:')
    h_gap = SRXSSAHG('XF:05IDB-OP:1{Slt:SSA-Ax:')
    v_cen = SRXSSAVC('XF:05IDB-OP:1{Slt:SSA-Ax:')
    v_gap = SRXSSAVG('XF:05IDB-OP:1{Slt:SSA-Ax:')
    
slt_ssa = SRXSSACalc('XF:05IDB-OP:1{Slt:SSA-Ax:',name='slt_ssa')
# Pseudo motor for secondary source slits
#slt_ssa = SRXSlits4SWPM('XF:05IDB-OP:1{Slt:SSA-Ax:', name='slt_ssa')

#values to use when ssa offset in css/epics are set to zeros
#slt_ssa.top_zero.put(0.2396)
#slt_ssa.bot_zero.put(-2.2046)
#slt_ssa.inb_zero.put(-0.4895)
#slt_ssa.out_zero.put(1.3610)

#values to use when ssa offset in css/epics are defined
#slt_ssa.top_zero.put(0.0)
#slt_ssa.bot_zero.put(0.0)
#slt_ssa.inb_zero.put(0.0)
#slt_ssa.out_zero.put(0.0)



# HFM Mirror
class SRXHFM(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    pitch = Cpt(EpicsMotor, 'P}Mtr')
    bend = Cpt(EpicsMotor, 'Bend}Mtr')

hfm = SRXHFM('XF:05IDA-OP:1{Mir:1-Ax:', name='hfm')

class SRXM2(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')
    pitch = Cpt(EpicsMotor, 'P}Mtr')
    roll = Cpt(EpicsMotor, 'R}Mtr')
    yaw = Cpt(EpicsMotor, 'Yaw}Mtr')
m2 = SRXM2('XF:05IDD-OP:1{Mir:2-Ax:')

class SRXM3(Device):
    x = Cpt(EpicsMotor, 'X}Mtr')
    pitch = Cpt(EpicsMotor, 'P}Mtr')
m3 = SRXM2('XF:05IDD-OP:1{Mir:3-Ax:')


# HDCM
class SRXDCM(Device):
    bragg = Cpt(EpicsMotor, 'P}Mtr')
    c1_roll = Cpt(EpicsMotor, 'R1}Mtr')
    c2_x = Cpt(EpicsMotor, 'X2}Mtr')
    c2_pitch = Cpt(EpicsMotor, 'P2}Mtr')
    c2_pitch_kill = Cpt(EpicsSignal, 'P2}Cmd:Kill-Cmd')
    x = Cpt(EpicsMotor, 'X}Mtr')
    y = Cpt(EpicsMotor, 'Y}Mtr')

    temp_pitch = Cpt(EpicsSignalRO, 'P}T-I')

dcm = SRXDCM('XF:05IDA-OP:1{Mono:HDCM-Ax:' , name='dcm')



# BPMs
class SRXBPM(Device):
    y = Cpt(EpicsMotor, 'YFoil}Mtr')
    diode_x = Cpt(EpicsMotor, 'XDiode}Mtr')
    diode_y = Cpt(EpicsMotor, 'YDiode}Mtr')


bpm1_pos = SRXBPM('XF:05IDA-BI:1{BPM:1-Ax:', name='bpm1_pos')
bpm2_pos = SRXBPM('XF:05IDB-BI:1{BPM:2-Ax:', name='bpm2_pos')


#fast shutter
class SRXSOFTINP(Device):
    pulse = Cpt(EpicsSignal,'')
    #these need to be put complete!!
    def high_cmd(self):
        self.pulse.put(1)
    def low_cmd(self):
        self.pulse.put(0)
    def toggle_cmd(self):
        if self.pulse.get() == 0:
            self.pulse.put(1)
        else:
            self.pulse.put(0)
shut_fast = SRXSOFTINP('XF:05IDD-ES:1{Sclr:1}UserLED',name='shut_fast')

class SRXFASTSHUT(SRXSOFTINP):
    pulse = Cpt(EpicsSignal,':SOFT_IN:B1')
    iobit = Cpt(EpicsSignalRO,':SYS_STAT1LO')
    def status(self):
        self.low_cmd()
        shutopen = bool(int16(self.iobit.get()) & int16(2))
        if shutopen is True:
            return 'Open'
        else:
            return 'Closed'
    def high_cmd(self):
        self.pulse.put(1)
    def low_cmd(self):
        self.pulse.put(0)
    def open_cmd(self):
        print(self.status())
        if self.status() is 'Closed':
            print(self.status())
        #    self.low_cmd()
            self.high_cmd()
    def close_cmd(self):
        print(self.status())
        if self.status() is 'Open':
            print(self.status())
         #   self.low_cmd()
            self.high_cmd()

#shut_fast = SRXFASTSHUT('XF:05IDD-ES:1{Dev:Zebra1}',name='shut_fast')
