from eudplib import *
try:
    InitialWireframe
except NameError:

    def init_wireframe():
        WireFrameDataEditor.WireFrameInit()
        WireFrameDataEditor.ChangeWireframe(10, 1)
        WireFrameDataEditor.ChangeTranframe(10, 1)
        WireFrameDataEditor.ChangeGrpframe(10, 1)
        WireFrameDataEditor.ChangeWireframe(15, 10)
        WireFrameDataEditor.ChangeTranframe(15, 10)
        WireFrameDataEditor.ChangeGrpframe(15, 10)
        WireFrameDataEditor.ChangeWireframe(27, 121)
        WireFrameDataEditor.ChangeTranframe(27, 27)
        WireFrameDataEditor.ChangeGrpframe(27, 121)
        WireFrameDataEditor.ChangeWireframe(32, 0)
        WireFrameDataEditor.ChangeTranframe(32, 0)
        WireFrameDataEditor.ChangeGrpframe(32, 0)
        WireFrameDataEditor.ChangeWireframe(84, 73)
        WireFrameDataEditor.ChangeTranframe(84, 73)
        WireFrameDataEditor.ChangeGrpframe(84, 73)
        WireFrameDataEditor.ChangeWireframe(89, 74)
        WireFrameDataEditor.ChangeTranframe(89, 74)
        WireFrameDataEditor.ChangeGrpframe(89, 74)
        WireFrameDataEditor.ChangeWireframe(90, 91)
        WireFrameDataEditor.ChangeTranframe(90, 91)
        WireFrameDataEditor.ChangeGrpframe(90, 91)
        WireFrameDataEditor.ChangeWireframe(92, 91)
        WireFrameDataEditor.ChangeTranframe(92, 91)
        WireFrameDataEditor.ChangeGrpframe(92, 91)
        WireFrameDataEditor.ChangeWireframe(95, 10)
        WireFrameDataEditor.ChangeTranframe(95, 10)
        WireFrameDataEditor.ChangeGrpframe(95, 10)
        WireFrameDataEditor.ChangeWireframe(99, 16)
        WireFrameDataEditor.ChangeTranframe(99, 16)
        WireFrameDataEditor.ChangeGrpframe(99, 16)
        WireFrameDataEditor.ChangeWireframe(100, 16)
        WireFrameDataEditor.ChangeTranframe(100, 16)
        WireFrameDataEditor.ChangeGrpframe(100, 16)
        WireFrameDataEditor.ChangeWireframe(108, 79)
        WireFrameDataEditor.ChangeGrpframe(108, 79)
        WireFrameDataEditor.ChangeWireframe(117, 76)
        WireFrameDataEditor.ChangeGrpframe(117, 76)
        WireFrameDataEditor.ChangeWireframe(121, 91)
        WireFrameDataEditor.ChangeGrpframe(121, 91)
        WireFrameDataEditor.ChangeWireframe(153, 91)

else:
    InitialWireframe.wirefram(10, 1)
    InitialWireframe.tranwire(10, 1)
    InitialWireframe.grpwire(10, 1)
    InitialWireframe.wirefram(15, 10)
    InitialWireframe.tranwire(15, 10)
    InitialWireframe.grpwire(15, 10)
    InitialWireframe.wirefram(27, 121)
    InitialWireframe.tranwire(27, 27)
    InitialWireframe.grpwire(27, 121)
    InitialWireframe.wirefram(32, 0)
    InitialWireframe.tranwire(32, 0)
    InitialWireframe.grpwire(32, 0)
    InitialWireframe.wirefram(84, 73)
    InitialWireframe.tranwire(84, 73)
    InitialWireframe.grpwire(84, 73)
    InitialWireframe.wirefram(89, 74)
    InitialWireframe.tranwire(89, 74)
    InitialWireframe.grpwire(89, 74)
    InitialWireframe.wirefram(90, 91)
    InitialWireframe.tranwire(90, 91)
    InitialWireframe.grpwire(90, 91)
    InitialWireframe.wirefram(92, 91)
    InitialWireframe.tranwire(92, 91)
    InitialWireframe.grpwire(92, 91)
    InitialWireframe.wirefram(95, 10)
    InitialWireframe.tranwire(95, 10)
    InitialWireframe.grpwire(95, 10)
    InitialWireframe.wirefram(99, 16)
    InitialWireframe.tranwire(99, 16)
    InitialWireframe.grpwire(99, 16)
    InitialWireframe.wirefram(100, 16)
    InitialWireframe.tranwire(100, 16)
    InitialWireframe.grpwire(100, 16)
    InitialWireframe.wirefram(108, 79)
    InitialWireframe.grpwire(108, 79)
    InitialWireframe.wirefram(117, 76)
    InitialWireframe.grpwire(117, 76)
    InitialWireframe.wirefram(121, 91)
    InitialWireframe.grpwire(121, 91)
    InitialWireframe.wirefram(153, 91)


def onPluginStart():
    try:
        init_wireframe()
    except NameError:
        pass
    DoActions([ # 스테이터스인포메이션
        SetMemory(0x5194E8, SetTo, 4344192),
        SetMemory(0x5194EC, SetTo, 4353872),
        SetMemory(0x5197DC, SetTo, 4343040),
        SetMemory(0x5197E0, SetTo, 4349664),
        SetMemory(0x5198B4, SetTo, 4344192),
        SetMemory(0x5198B8, SetTo, 4353872),
        SetMemory(0x519920, SetTo, 4344192),
        SetMemory(0x519924, SetTo, 4353872),
        SetMemory(0x51992C, SetTo, 4343040),
        SetMemory(0x519930, SetTo, 4349664),
        SetMemory(0x519950, SetTo, 4343040),
        SetMemory(0x519954, SetTo, 4349664),
        SetMemory(0x519AD0, SetTo, 4343040),
        SetMemory(0x519B10, SetTo, 4356240),
    ])
    # 버튼셋
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,130,1,96,142,66,0,176,52,66,0,5,0,5,0,88,5,10,6])
    btnptr0 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,130,1,96,142,66,0,176,52,66,0,5,0,5,0,88,5,10,6])
    btnptr1 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,130,1,96,142,66,0,176,52,66,0,5,0,5,0,87,5,10,6])
    btnptr10 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,130,1,96,142,66,0,176,52,66,0,5,0,5,0,88,5,10,6])
    btnptr16 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,51,0,96,142,66,0,176,52,66,0,28,0,28,0,55,4,36,4,2,0,16,0,96,142,66,0,176,52,66,0,27,0,27,0,54,4,34,4,4,0,50,0,96,142,66,0,176,52,66,0,29,0,29,0,56,4,37,4,5,0,1,0,96,142,66,0,176,52,66,0,22,0,22,0,53,4,35,4,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,10,6,9,0,236,0,208,130,66,0,240,154,69,0,0,0,228,0,177,2,10,6])
    btnptr26 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,31,1,80,148,66,0,16,51,66,0,17,0,17,0,107,5,245,1,1,0,33,1,80,148,66,0,16,51,66,0,8,0,8,0,119,5,245,1,2,0,0,1,80,148,66,0,16,51,66,0,21,0,21,0,108,5,245,1,2,0,34,1,80,148,66,0,16,51,66,0,9,0,9,0,120,5,245,1,4,0,219,0,80,148,66,0,16,51,66,0,22,0,22,0,111,5,245,1,4,0,50,1,80,148,66,0,16,51,66,0,10,0,10,0,121,5,245,1,5,0,129,0,80,148,66,0,16,51,66,0,23,0,23,0,110,5,245,1,5,0,32,1,80,148,66,0,16,51,66,0,11,0,11,0,122,5,245,1,6,0,128,0,80,148,66,0,16,51,66,0,43,0,43,0,109,5,245,1,7,0,33,1,80,148,66,0,16,51,66,0,14,0,14,0,123,5,91,5,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,10,6,9,0,236,0,208,130,66,0,240,154,69,0,0,0,228,0,177,2,10,6])
    btnptr50 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,53,1,96,142,66,0,176,52,66,0,64,0,64,0,70,5,10,6,2,0,53,1,96,142,66,0,176,52,66,0,65,0,65,0,71,5,10,6,3,0,53,1,96,142,66,0,176,52,66,0,66,0,66,0,72,5,10,6,4,0,53,1,96,142,66,0,176,52,66,0,67,0,67,0,73,5,10,6,5,0,53,1,96,142,66,0,176,52,66,0,61,0,61,0,74,5,10,6,8,0,121,1,96,142,66,0,176,52,66,0,83,0,83,0,75,5,10,6,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,10,6,9,0,236,0,208,130,66,0,240,154,69,0,0,0,228,0,177,2,10,6])
    btnptr51 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr72 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,208,130,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,208,130,66,0,240,51,66,0,0,0,0,0,153,2,0,0,4,0,254,0,208,130,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,208,130,66,0,112,51,66,0,0,0,0,0,156,2,0,0])
    btnptr96 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,130,1,96,142,66,0,176,52,66,0,5,0,5,0,88,5,10,6])
    btnptr99 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1,9,0,88,5,96,142,66,0,176,52,66,0,5,0,5,0,87,5,10,6])
    btnptr100 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,250,0,224,148,66,0,112,63,66,0,4,0,4,0,81,1,0,0,2,0,132,1,96,142,66,0,176,52,66,0,11,0,11,0,217,5,10,6,3,0,130,1,96,142,66,0,176,52,66,0,3,0,3,0,132,5,10,6,4,0,16,1,96,142,66,0,240,154,69,0,50,0,50,0,66,5,106,5,5,0,21,1,96,142,66,0,176,52,66,0,12,0,12,0,133,5,10,6,6,0,54,1,80,148,66,0,16,51,66,0,20,0,20,0,83,5,245,1,7,0,214,0,96,142,66,0,240,154,69,0,51,0,51,0,69,5,216,5,8,0,32,1,80,148,66,0,16,51,66,0,18,0,18,0,84,5,245,1,9,0,36,1,80,148,66,0,16,51,66,0,19,0,19,0,81,5,248,1])
    btnptr107 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,0,0,96,142,66,0,176,52,66,0,82,0,82,0,74,2,0,0,2,0,1,0,96,142,66,0,176,52,66,0,8,0,8,0,38,4,0,0,3,0,118,1,96,142,66,0,176,52,66,0,19,0,19,0,39,4,14,5,4,0,34,0,96,142,66,0,176,52,66,0,34,0,34,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,9,0,9,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,88,0,88,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,80,0,80,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,21,0,21,0,10,5,14,5,5,0,17,1,96,142,66,0,240,154,69,0,26,0,26,0,89,5,106,5,6,0,30,1,32,149,66,0,160,68,66,0,0,0,0,0,160,2,0,0,7,0,32,1,80,148,66,0,16,51,66,0,7,0,7,0,207,1,248,1,7,0,237,0,96,142,66,0,176,52,66,0,74,0,74,0,78,1,10,6,8,0,54,1,80,148,66,0,16,51,66,0,15,0,15,0,215,1,248,1,9,0,236,0,48,133,66,0,144,52,66,0,0,0,254,0,181,2,0,0,9,0,236,0,32,137,66,0,208,50,66,0,0,0,0,0,182,2,0,0,9,0,36,1,80,148,66,0,16,51,66,0,0,0,0,0,200,1,245,1])
    btnptr111 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,32,149,66,0,160,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,96,142,66,0,176,52,66,0,77,0,77,0,153,2,10,6,3,0,230,0,96,142,66,0,176,52,66,0,78,0,78,0,154,2,10,6,4,0,34,0,96,142,66,0,176,52,66,0,34,0,34,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,9,0,9,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,88,0,88,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,80,0,80,0,10,5,14,5,4,0,34,0,96,142,66,0,176,52,66,0,21,0,21,0,10,5,14,5,5,0,255,0,96,142,66,0,176,52,66,0,15,0,15,0,156,2,10,6,6,0,118,1,96,142,66,0,176,52,66,0,19,0,19,0,39,4,14,5,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr113 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,56,1,96,142,66,0,176,52,66,0,68,0,68,0,80,5,10,6,2,0,56,1,96,142,66,0,176,52,66,0,84,0,84,0,76,5,10,6,3,0,56,1,96,142,66,0,176,52,66,0,69,0,69,0,77,5,10,6,4,0,56,1,96,142,66,0,176,52,66,0,70,0,70,0,78,5,10,6,5,0,56,1,96,142,66,0,176,52,66,0,60,0,60,0,79,5,10,6,7,0,133,1,96,142,66,0,176,52,66,0,63,0,63,0,68,5,10,6,8,0,132,1,96,142,66,0,176,52,66,0,62,0,62,0,67,5,10,6])
    btnptr115 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr244 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr246 = Db(bytebuffer)
    bytebuffer = bytearray([1,0,228,0,160,141,66,0,64,68,66,0,0,0,0,0,152,2,0,0,2,0,229,0,64,141,66,0,240,51,66,0,0,0,0,0,153,2,0,0,3,0,230,0,48,143,66,0,128,67,66,0,0,0,0,0,154,2,0,0,4,0,254,0,160,141,66,0,64,65,66,0,0,0,0,0,155,2,0,0,5,0,255,0,160,141,66,0,112,51,66,0,0,0,0,0,156,2,0,0,7,0,237,0,224,148,66,0,208,52,66,0,0,0,0,0,78,1,90,1])
    btnptr247 = Db(bytebuffer)
    DoActions([
        SetMemory(0x5187EC, SetTo, btnptr16),
        SetMemory(0x5187E8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5187F8, SetTo, btnptr16),
        SetMemory(0x5187F4, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518864, SetTo, btnptr10),
        SetMemory(0x518860, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188A0, SetTo, btnptr10),
        SetMemory(0x51889C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x5188AC, SetTo, btnptr16),
        SetMemory(0x5188A8, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518924, SetTo, btnptr26),
        SetMemory(0x518920, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518930, SetTo, 0),
        SetMemory(0x51892C, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518A44, SetTo, btnptr50),
        SetMemory(0x518A40, SetTo, 12),
    ])
    DoActions([
        SetMemory(0x518A50, SetTo, btnptr51),
        SetMemory(0x518A4C, SetTo, 8),
    ])
    DoActions([
        SetMemory(0x518B4C, SetTo, btnptr72),
        SetMemory(0x518B48, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x518BDC, SetTo, 0),
        SetMemory(0x518BD8, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C18, SetTo, 5332432),
        SetMemory(0x518C14, SetTo, 5),
    ])
    DoActions([
        SetMemory(0x518C24, SetTo, 0),
        SetMemory(0x518C20, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C3C, SetTo, 0),
        SetMemory(0x518C38, SetTo, 0),
    ])
    DoActions([
        SetMemory(0x518C60, SetTo, btnptr10),
        SetMemory(0x518C5C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C6C, SetTo, btnptr96),
        SetMemory(0x518C68, SetTo, 4),
    ])
    DoActions([
        SetMemory(0x518C90, SetTo, btnptr16),
        SetMemory(0x518C8C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518C9C, SetTo, btnptr16),
        SetMemory(0x518C98, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x518CF0, SetTo, btnptr107),
        SetMemory(0x518CEC, SetTo, 9),
    ])
    DoActions([
        SetMemory(0x518D20, SetTo, btnptr111),
        SetMemory(0x518D1C, SetTo, 16),
    ])
    DoActions([
        SetMemory(0x518D38, SetTo, btnptr113),
        SetMemory(0x518D34, SetTo, 11),
    ])
    DoActions([
        SetMemory(0x518D50, SetTo, btnptr115),
        SetMemory(0x518D4C, SetTo, 7),
    ])
    DoActions([
        SetMemory(0x51935C, SetTo, btnptr244),
        SetMemory(0x519358, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x519374, SetTo, btnptr246),
        SetMemory(0x519370, SetTo, 6),
    ])
    DoActions([
        SetMemory(0x519380, SetTo, btnptr247),
        SetMemory(0x51937C, SetTo, 6),
    ])
    with open('../temp/RequireData', 'rb') as file:
        inputData = file.read()
        inputData_db = Db(inputData)
        inputDwordN = (len(inputData) + 3) // 4

    addrEPD = EPD(0x514178)
    f_repmovsd_epd(addrEPD, EPD(inputData_db), inputDwordN)


def beforeTriggerExec():
    DoActions([
        SetMemory(0x660A70 + 0, SetTo, 393217),
        SetMemory(0x660A70 + 4, SetTo, 1179661),
        SetMemory(0x660A70 + 8, SetTo, 1507328),
        SetMemory(0x660A70 + 12, SetTo, 1572864),
        SetMemory(0x660A70 + 16, SetTo, 2228253),
        SetMemory(0x660A70 + 20, SetTo, 2752512),
        SetMemory(0x660A70 + 24, SetTo, 47),
        SetMemory(0x660A70 + 28, SetTo, 3735604),
        SetMemory(0x660A70 + 32, SetTo, 0),
        SetMemory(0x660A70 + 36, SetTo, 4063232),
        SetMemory(0x660A70 + 40, SetTo, 4915270),
        SetMemory(0x660A70 + 44, SetTo, 83),
        SetMemory(0x660A70 + 48, SetTo, 0),
        SetMemory(0x660A70 + 52, SetTo, 5898329),
        SetMemory(0x660A70 + 56, SetTo, 6684768),
        SetMemory(0x660A70 + 60, SetTo, 0),
        SetMemory(0x660A70 + 64, SetTo, 108),
        SetMemory(0x660A70 + 68, SetTo, 113),
        SetMemory(0x660A70 + 72, SetTo, 7929856),
        SetMemory(0x660A70 + 76, SetTo, 8454269),
        SetMemory(0x660A70 + 80, SetTo, 8716288),
        SetMemory(0x660A70 + 84, SetTo, 9109640),
        SetMemory(0x660A70 + 88, SetTo, 9830546),
        SetMemory(0x660A70 + 92, SetTo, 10354842),
        SetMemory(0x660A70 + 96, SetTo, 0),
        SetMemory(0x660A70 + 100, SetTo, 11141285),
        SetMemory(0x660A70 + 104, SetTo, 0),
        SetMemory(0x660A70 + 108, SetTo, 0),
        SetMemory(0x660A70 + 112, SetTo, 0),
        SetMemory(0x660A70 + 116, SetTo, 175),
        SetMemory(0x660A70 + 120, SetTo, 12320952),
        SetMemory(0x660A70 + 124, SetTo, 193),
        SetMemory(0x660A70 + 128, SetTo, 13304006),
        SetMemory(0x660A70 + 132, SetTo, 13959376),
        SetMemory(0x660A70 + 136, SetTo, 14286848),
        SetMemory(0x660A70 + 140, SetTo, 14680285),
        SetMemory(0x660A70 + 144, SetTo, 15270116),
        SetMemory(0x660A70 + 148, SetTo, 240),
        SetMemory(0x660A70 + 152, SetTo, 16056320),
        SetMemory(0x660A70 + 156, SetTo, 250),
        SetMemory(0x660A70 + 160, SetTo, 255),
        SetMemory(0x660A70 + 164, SetTo, 17563911),
        SetMemory(0x660A70 + 168, SetTo, 273),
        SetMemory(0x660A70 + 172, SetTo, 0),
        SetMemory(0x660A70 + 176, SetTo, 18678037),
        SetMemory(0x660A70 + 180, SetTo, 0),
        SetMemory(0x660A70 + 184, SetTo, 0),
        SetMemory(0x660A70 + 188, SetTo, 18743296),
        SetMemory(0x660A70 + 192, SetTo, 0),
        SetMemory(0x660A70 + 196, SetTo, 0),
        SetMemory(0x660A70 + 200, SetTo, 0),
        SetMemory(0x660A70 + 204, SetTo, 18808832),
        SetMemory(0x660A70 + 208, SetTo, 0),
        SetMemory(0x660A70 + 212, SetTo, 19464485),
        SetMemory(0x660A70 + 216, SetTo, 20250927),
        SetMemory(0x660A70 + 220, SetTo, 20775225),
        SetMemory(0x660A70 + 224, SetTo, 21430594),
        SetMemory(0x660A70 + 228, SetTo, 22085964),
        SetMemory(0x660A70 + 232, SetTo, 342),
        SetMemory(0x660A70 + 236, SetTo, 347),
        SetMemory(0x660A70 + 240, SetTo, 352),
        SetMemory(0x660A70 + 244, SetTo, 23724389),
        SetMemory(0x660A70 + 248, SetTo, 24379759),
        SetMemory(0x660A70 + 252, SetTo, 0),
        SetMemory(0x660A70 + 256, SetTo, 0),
        SetMemory(0x660A70 + 260, SetTo, 24707072),
        SetMemory(0x660A70 + 264, SetTo, 25297277),
        SetMemory(0x660A70 + 268, SetTo, 25952647),
        SetMemory(0x660A70 + 272, SetTo, 26608017),
        SetMemory(0x660A70 + 276, SetTo, 27459995),
        SetMemory(0x660A70 + 280, SetTo, 28508590),
        SetMemory(0x660A70 + 284, SetTo, 29753787),
        SetMemory(0x660A70 + 288, SetTo, 458),
        SetMemory(0x660A70 + 292, SetTo, 462),
        SetMemory(0x660A70 + 296, SetTo, 30539776),
        SetMemory(0x660A70 + 300, SetTo, 0),
        SetMemory(0x660A70 + 304, SetTo, 0),
        SetMemory(0x660A70 + 308, SetTo, 30933461),
        SetMemory(0x660A70 + 312, SetTo, 31392220),
        SetMemory(0x660A70 + 316, SetTo, 31588352),
        SetMemory(0x660A70 + 320, SetTo, 486),
        SetMemory(0x660A70 + 324, SetTo, 32375274),
        SetMemory(0x660A70 + 328, SetTo, 32899570),
        SetMemory(0x660A70 + 332, SetTo, 33423866),
        SetMemory(0x660A70 + 336, SetTo, 33685504),
        SetMemory(0x660A70 + 340, SetTo, 34275846),
        SetMemory(0x660A70 + 344, SetTo, 527),
        SetMemory(0x660A70 + 348, SetTo, 0),
        SetMemory(0x660A70 + 352, SetTo, 0),
        SetMemory(0x660A70 + 356, SetTo, 0),
        SetMemory(0x660A70 + 360, SetTo, 0),
        SetMemory(0x660A70 + 364, SetTo, 0),
        SetMemory(0x660A70 + 368, SetTo, 0),
        SetMemory(0x660A70 + 372, SetTo, 0),
        SetMemory(0x660A70 + 376, SetTo, 0),
        SetMemory(0x660A70 + 380, SetTo, 0),
        SetMemory(0x660A70 + 384, SetTo, 0),
        SetMemory(0x660A70 + 388, SetTo, 0),
        SetMemory(0x660A70 + 392, SetTo, 0),
        SetMemory(0x660A70 + 396, SetTo, 0),
        SetMemory(0x660A70 + 400, SetTo, 0),
        SetMemory(0x660A70 + 404, SetTo, 0),
        SetMemory(0x660A70 + 408, SetTo, 34799616),
        SetMemory(0x660A70 + 412, SetTo, 34931220),
        SetMemory(0x660A70 + 416, SetTo, 534),
        SetMemory(0x660A70 + 420, SetTo, 0),
        SetMemory(0x660A70 + 424, SetTo, 0),
        SetMemory(0x660A70 + 428, SetTo, 0),
        SetMemory(0x660A70 + 432, SetTo, 0),
        SetMemory(0x660A70 + 436, SetTo, 0),
        SetMemory(0x660A70 + 440, SetTo, 0),
        SetMemory(0x660A70 + 444, SetTo, 0),
        SetMemory(0x660A70 + 448, SetTo, 0),
        SetMemory(0x660A70 + 452, SetTo, 0),
        SetMemory(0x6558C0 + 0, SetTo, 393217),
        SetMemory(0x6558C0 + 4, SetTo, 1966098),
        SetMemory(0x6558C0 + 8, SetTo, 3997740),
        SetMemory(0x6558C0 + 12, SetTo, 5439560),
        SetMemory(0x6558C0 + 16, SetTo, 6094936),
        SetMemory(0x6558C0 + 20, SetTo, 6750306),
        SetMemory(0x6558C0 + 24, SetTo, 8192108),
        SetMemory(0x6558C0 + 28, SetTo, 9306248),
        SetMemory(0x6558C0 + 32, SetTo, 9961619),
        SetMemory(0x6558C0 + 36, SetTo, 10616989),
        SetMemory(0x6558C0 + 40, SetTo, 11272359),
        SetMemory(0x6558C0 + 44, SetTo, 11927729),
        SetMemory(0x6558C0 + 48, SetTo, 12714171),
        SetMemory(0x6558C0 + 52, SetTo, 13631689),
        SetMemory(0x6558C0 + 56, SetTo, 14221524),
        SetMemory(0x6558C0 + 60, SetTo, 14745821),
        SetMemory(0x6558C0 + 64, SetTo, 15270117),
        SetMemory(0x6558C0 + 68, SetTo, 15794413),
        SetMemory(0x6558C0 + 72, SetTo, 16318709),
        SetMemory(0x6558C0 + 76, SetTo, 16843005),
        SetMemory(0x6558C0 + 80, SetTo, 17367301),
        SetMemory(0x6558C0 + 84, SetTo, 17891597),
        SetMemory(0x6558C0 + 88, SetTo, 278),
        SetMemory(0x6558C0 + 92, SetTo, 18481152),
        SetMemory(0x6558C0 + 96, SetTo, 18808832),
        SetMemory(0x6558C0 + 100, SetTo, 19136512),
        SetMemory(0x6558C0 + 104, SetTo, 19857706),
        SetMemory(0x6558C0 + 108, SetTo, 308),
        SetMemory(0x6558C0 + 112, SetTo, 0),
        SetMemory(0x6558C0 + 116, SetTo, 0),
        SetMemory(0x656198 + 0, SetTo, 393217),
        SetMemory(0x656198 + 4, SetTo, 1048587),
        SetMemory(0x656198 + 8, SetTo, 1376256),
        SetMemory(0x656198 + 12, SetTo, 1703936),
        SetMemory(0x656198 + 16, SetTo, 2359327),
        SetMemory(0x656198 + 20, SetTo, 3014697),
        SetMemory(0x656198 + 24, SetTo, 3670016),
        SetMemory(0x656198 + 28, SetTo, 3932160),
        SetMemory(0x656198 + 32, SetTo, 4456512),
        SetMemory(0x656198 + 36, SetTo, 4980808),
        SetMemory(0x656198 + 40, SetTo, 5505104),
        SetMemory(0x656198 + 44, SetTo, 88),
        SetMemory(0x656198 + 48, SetTo, 6422620),
        SetMemory(0x656198 + 52, SetTo, 6750208),
        SetMemory(0x656198 + 56, SetTo, 7077888),
        SetMemory(0x656198 + 60, SetTo, 7798897),
        SetMemory(0x656198 + 64, SetTo, 124),
        SetMemory(0x656198 + 68, SetTo, 0),
        SetMemory(0x656198 + 72, SetTo, 0),
        SetMemory(0x656198 + 76, SetTo, 0),
        SetMemory(0x656198 + 80, SetTo, 0),
        SetMemory(0x656198 + 84, SetTo, 0),
        SetMemory(0x6562F8 + 0, SetTo, 131073),
        SetMemory(0x6562F8 + 4, SetTo, 1900564),
        SetMemory(0x6562F8 + 8, SetTo, 2752551),
        SetMemory(0x6562F8 + 12, SetTo, 4128825),
        SetMemory(0x6562F8 + 16, SetTo, 5701704),
        SetMemory(0x6562F8 + 20, SetTo, 6291456),
        SetMemory(0x6562F8 + 24, SetTo, 8650878),
        SetMemory(0x6562F8 + 28, SetTo, 9699469),
        SetMemory(0x6562F8 + 32, SetTo, 11403422),
        SetMemory(0x6562F8 + 36, SetTo, 12648635),
        SetMemory(0x6562F8 + 40, SetTo, 14024909),
        SetMemory(0x6562F8 + 44, SetTo, 15204575),
        SetMemory(0x6562F8 + 48, SetTo, 15663339),
        SetMemory(0x6562F8 + 52, SetTo, 16252928),
        SetMemory(0x6562F8 + 56, SetTo, 16777468),
        SetMemory(0x6562F8 + 60, SetTo, 17236227),
        SetMemory(0x6562F8 + 64, SetTo, 267),
        SetMemory(0x6562F8 + 68, SetTo, 272),
        SetMemory(0x6562F8 + 72, SetTo, 0),
        SetMemory(0x6562F8 + 76, SetTo, 0),
        SetMemory(0x6562F8 + 80, SetTo, 0),
        SetMemory(0x6562F8 + 84, SetTo, 0),
        SetMemory(0x665580 + 0, SetTo, 327682),
        SetMemory(0x665580 + 4, SetTo, 786440),
        SetMemory(0x665580 + 8, SetTo, 1310736),
        SetMemory(0x665580 + 12, SetTo, 1835032),
        SetMemory(0x665580 + 16, SetTo, 2621476),
        SetMemory(0x665580 + 20, SetTo, 3145772),
        SetMemory(0x665580 + 24, SetTo, 3670068),
        SetMemory(0x665580 + 28, SetTo, 4194364),
        SetMemory(0x665580 + 32, SetTo, 0),
        SetMemory(0x665580 + 36, SetTo, 5308484),
        SetMemory(0x665580 + 40, SetTo, 7405677),
        SetMemory(0x665580 + 44, SetTo, 7929973),
        SetMemory(0x665580 + 48, SetTo, 8126464),
        SetMemory(0x665580 + 52, SetTo, 8650880),
        SetMemory(0x665580 + 56, SetTo, 9568395),
        SetMemory(0x665580 + 60, SetTo, 10289305),
        SetMemory(0x665580 + 64, SetTo, 10813601),
        SetMemory(0x665580 + 68, SetTo, 11337897),
        SetMemory(0x665580 + 72, SetTo, 177),
        SetMemory(0x665580 + 76, SetTo, 11730944),
        SetMemory(0x665580 + 80, SetTo, 12124342),
        SetMemory(0x665580 + 84, SetTo, 0),
        SetMemory(0x665580 + 88, SetTo, 0),
        SetMemory(0x665580 + 92, SetTo, 192),
        SetMemory(0x665580 + 96, SetTo, 12910592),
        SetMemory(0x665580 + 100, SetTo, 13697225),
        SetMemory(0x665580 + 104, SetTo, 15139039),
        SetMemory(0x665580 + 108, SetTo, 16187631),
        SetMemory(0x665580 + 112, SetTo, 17629445),
        SetMemory(0x665580 + 116, SetTo, 18678037),
        SetMemory(0x665580 + 120, SetTo, 19726629),
        SetMemory(0x665580 + 124, SetTo, 309),
        SetMemory(0x665580 + 128, SetTo, 21102909),
        SetMemory(0x665580 + 132, SetTo, 21364736),
        SetMemory(0x665580 + 136, SetTo, 21626880),
        SetMemory(0x665580 + 140, SetTo, 22085965),
        SetMemory(0x665580 + 144, SetTo, 341),
        SetMemory(0x665580 + 148, SetTo, 345),
        SetMemory(0x665580 + 152, SetTo, 22806528),
        SetMemory(0x665580 + 156, SetTo, 23789921),
        SetMemory(0x665580 + 160, SetTo, 24183150),
        SetMemory(0x665580 + 164, SetTo, 372),
        SetMemory(0x665580 + 168, SetTo, 24772983),
        SetMemory(0x665580 + 172, SetTo, 381),
        SetMemory(0x665580 + 176, SetTo, 0),
        SetMemory(0x665580 + 180, SetTo, 384),
        SetMemory(0x665580 + 184, SetTo, 25559427),
        SetMemory(0x665580 + 188, SetTo, 26149260),
        SetMemory(0x665580 + 192, SetTo, 26411008),
        SetMemory(0x665580 + 196, SetTo, 0),
        SetMemory(0x665580 + 200, SetTo, 26804630),
        SetMemory(0x665580 + 204, SetTo, 27787686),
        SetMemory(0x665580 + 208, SetTo, 431),
        SetMemory(0x665580 + 212, SetTo, 28508160),
        SetMemory(0x665580 + 216, SetTo, 439),
        SetMemory(0x665580 + 220, SetTo, 29229056),
        SetMemory(0x665580 + 224, SetTo, 449),
        SetMemory(0x665580 + 228, SetTo, 0),
        SetMemory(0x665580 + 232, SetTo, 0),
        SetMemory(0x665580 + 236, SetTo, 0),
        SetMemory(0x665580 + 240, SetTo, 0),
        SetMemory(0x665580 + 244, SetTo, 29622272),
        SetMemory(0x665580 + 248, SetTo, 29884416),
        SetMemory(0x665580 + 252, SetTo, 30409164),
        SetMemory(0x665580 + 256, SetTo, 30933460),
        SetMemory(0x665580 + 260, SetTo, 31719900),
        SetMemory(0x665580 + 264, SetTo, 32178176),
        SetMemory(0x665580 + 268, SetTo, 32702958),
        SetMemory(0x665580 + 272, SetTo, 504),
        SetMemory(0x665580 + 276, SetTo, 0),
        SetMemory(0x665580 + 280, SetTo, 512),
        SetMemory(0x665580 + 284, SetTo, 0),
        SetMemory(0x665580 + 288, SetTo, 0),
        SetMemory(0x665580 + 292, SetTo, 0),
        SetMemory(0x665580 + 296, SetTo, 0),
        SetMemory(0x665580 + 300, SetTo, 0),
        SetMemory(0x665580 + 304, SetTo, 516),
        SetMemory(0x665580 + 308, SetTo, 34078720),
        SetMemory(0x665580 + 312, SetTo, 34734080),
        SetMemory(0x665580 + 316, SetTo, 0),
        SetMemory(0x665580 + 320, SetTo, 0),
        SetMemory(0x665580 + 324, SetTo, 0),
        SetMemory(0x665580 + 328, SetTo, 34996224),
        SetMemory(0x665580 + 332, SetTo, 36569626),
        SetMemory(0x665580 + 336, SetTo, 38470206),
        SetMemory(0x665580 + 340, SetTo, 40567384),
        SetMemory(0x665580 + 344, SetTo, 0),
        SetMemory(0x665580 + 348, SetTo, 41811968),
        SetMemory(0x665580 + 352, SetTo, 42336898),
        SetMemory(0x665580 + 356, SetTo, 650),
        SetMemory(0x665580 + 360, SetTo, 0),
        SetMemory(0x665580 + 364, SetTo, 654),
        SetMemory(0x665580 + 368, SetTo, 0),
        SetMemory(0x665580 + 372, SetTo, 0),
    ])
    

