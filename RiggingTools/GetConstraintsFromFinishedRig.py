import maya.cmds

def DoIt():
    root = "root"

    maya.cmds.select("root", hi=True)
    allChildren = maya.cmds.ls(selection=True)
    
    constraints = [child for child in allChildren if "parentConstraint" in child]
    
    parentConstraintMapping = {}
   # print(maya.cmds.listAttr(constraints[0],iu=True))
    for const in constraints:
        jointName = const.replace("_parentConstraint1","")
        
        bindBoneConstraints = [connection for connection in maya.cmds.listConnections(const) if "bind" in connection.lower()]
        validConstraints = list(set(bindBoneConstraints))
        if(validConstraints != []):
            parentConstraintMapping[jointName] = validConstraints
            
    print(parentConstraintMapping)

    #connections1 = maya.cmds.listConnections(constraints[6])
    #print(connections1)
    #c = connections1[11]
    #print(c)
    #print("bind" in c.lower())
    #print(type(c))

    
    
    
def CreateLocatorIfNone(locatorName):
    if(maya.cmds.ls(locatorName) == []):
        maya.cmds.spaceLocator(p=(0,0,0),name=locatorName)
    return locatorName
    
def AlignMixamoJointsToExistingJoints(jointA, jointB):
    print("oopooopo")
    
def Get(attr, transform):
    return maya.cmds.getAttr(str("%s."+attr) % transform)
    
def SetVector(attr, transform, value):
    return maya.cmds.setAttr(str("%s."+attr) % transform, type="float3", *value)    

def SetFloat(attr, transform, value):
    return maya.cmds.setAttr(str("%s."+attr) % transform, value)    
    
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
    
if(__name__ == "__main__"):
    DoIt()
    

