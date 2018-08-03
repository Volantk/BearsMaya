# from maya import cmds
from maya import cmds
from Bears import MayaUtils

def DoIt():
    SetupScene()
    root = "root"
    x = MayaUtils.Get("rotate", root)

    # setScl(root, (1,1,1))
    # cmds.select("root", hi=True)

def SetupScene():
    # Set working units to Meters
    cmds.currentUnit(l="m")
    
def AlignMixamoJointsToExistingJoints(jointA, jointB):
    print("oopooopo")

def GetRot(transform):
    return Get("rotate", transform)[0]
def GetLoc(transform):
    return Get("translate", transform)[0]
def GetScl(transform):
    return Get("scale", transform)[0]
    
def SetRot(transform, value):
    return Set("rotate", transform, value)
def SetLoc(transform, value):
    return Set("translate", transform, value)
def SetScl(transform, value):
    return Set("scale", transform, value)
