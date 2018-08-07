import maya.cmds
import MayaAutoControlRig

from Bears import MayaUtils

def MapHierarchyRecursivelyFrom(node, orderedHierarchyDict, level):
    level += 1
    relatives = maya.cmds.listRelatives(node)
    if(node not in orderedHierarchyDict.keys()):
        orderedHierarchyDict[node] = [level, relatives]
    if relatives != [] and relatives is not None:
        for relative in relatives:
            MapHierarchyRecursivelyFrom(relative, orderedHierarchyDict, level)

    
def DoIt():
    controls = ["global_CTRL", "Head_CTRL", "LeftArm_FK_CTRL", "LeftFoot_FK_CTRL", "LeftFoot_IK_CTRL",
                "LeftForeArm_FK_CTRL", "LeftForeArm_IK_CTRL", "LeftHand_FK_CTRL", "LeftHand_IK_CTRL",
                "LeftHandIndex1_CTRL", "LeftHandIndex2_CTRL", "LeftHandIndex3_CTRL", "LeftHandMiddle1_CTRL",
                "LeftHandMiddle2_CTRL", "LeftHandMiddle3_CTRL", "LeftHandPinky1_CTRL", "LeftHandPinky2_CTRL",
                "LeftHandPinky3_CTRL", "LeftHandRing1_CTRL", "LeftHandRing2_CTRL", "LeftHandRing3_CTRL",
                "LeftHandThumb1_CTRL", "LeftHandThumb2_CTRL", "LeftHandThumb3_CTRL", "LeftLeg_FK_CTRL",
                "LeftLeg_IK_CTRL", "LeftShoulder_CTRL", "LeftToeBase_FK_CTRL", "LeftUpLeg_FK_CTRL", "Neck_CTRL",
                "RightArm_FK_CTRL", "RightFoot_FK_CTRL", "RightFoot_IK_CTRL", "RightForeArm_FK_CTRL",
                "RightForeArm_IK_CTRL", "RightHand_FK_CTRL", "RightHand_IK_CTRL", "RightHandIndex1_CTRL",
                "RightHandIndex2_CTRL", "RightHandIndex3_CTRL", "RightHandMiddle1_CTRL", "RightHandMiddle2_CTRL",
                "RightHandMiddle3_CTRL", "RightHandPinky1_CTRL", "RightHandPinky2_CTRL", "RightHandPinky3_CTRL",
                "RightHandRing1_CTRL", "RightHandRing2_CTRL", "RightHandRing3_CTRL", "RightHandThumb1_CTRL",
                "RightHandThumb2_CTRL", "RightHandThumb3_CTRL", "RightLeg_FK_CTRL", "RightLeg_IK_CTRL",
                "RightShoulder_CTRL", "RightToeBase_FK_CTRL", "RightUpLeg_FK_CTRL", "Root_CTRL", "Spine1_CTRL",
                "Spine2_CTRL", "Spine_CTRL"]

    constraintMapping = {u'ORGFBXASC045toeFBXASC046L': [u'Bind_LeftToeBase'], u'ORGFBXASC045upper_armFBXASC046L': [u'Bind_LeftArm'], u'ORGFBXASC045f_ringFBXASC04602FBXASC046R': [u'Bind_RightHandRing2'], u'ORGFBXASC045f_indexFBXASC04602FBXASC046R': [u'Bind_RightHandIndex2'], u'ORGFBXASC045f_pinkyFBXASC04601FBXASC046L': [u'Bind_LeftHandPinky1'], u'ORGFBXASC045hips': [u'Bind_Hips'], u'ORGFBXASC045shinFBXASC046R': [u'Bind_RightLeg'], u'ORGFBXASC045f_pinkyFBXASC04603FBXASC046L': [u'Bind_LeftHandPinky3'], u'ORGFBXASC045f_indexFBXASC04602FBXASC046L': [u'Bind_LeftHandIndex2'], u'ORGFBXASC045f_ringFBXASC04602FBXASC046L': [u'Bind_LeftHandRing2'], u'ORGFBXASC045toeFBXASC046R': [u'Bind_RightToeBase'], u'ORGFBXASC045upper_armFBXASC046R': [u'Bind_RightArm'], u'ORGFBXASC045footFBXASC046L': [u'Bind_LeftFoot'], u'ORGFBXASC045f_pinkyFBXASC04602FBXASC046R': [u'Bind_RightHandPinky2'], u'ORGFBXASC045footFBXASC046R': [u'Bind_RightFoot'], u'ORGFBXASC045f_pinkyFBXASC04603FBXASC046R': [u'Bind_RightHandPinky3'], u'ORGFBXASC045thumbFBXASC04603FBXASC046L': [u'Bind_LeftHandThumb3'], u'ORGFBXASC045f_indexFBXASC04603FBXASC046L': [u'Bind_LeftHandIndex3'], u'ORGFBXASC045f_middleFBXASC04601FBXASC046R': [u'Bind_RightHandMiddle1'], u'ORGFBXASC045f_ringFBXASC04603FBXASC046L': [u'Bind_LeftHandRing3'], u'ORGFBXASC045spine': [u'Bind_Spine'], u'ORGFBXASC045head': [u'Bind_Head'], u'ORGFBXASC045f_middleFBXASC04601FBXASC046L': [u'Bind_LeftHandMiddle1'], u'ORGFBXASC045f_ringFBXASC04603FBXASC046R': [u'Bind_RightHandRing3'], u'ORGFBXASC045f_indexFBXASC04603FBXASC046R': [u'Bind_RightHandIndex3'], u'ATTACHFBXASC045head': [u'Bind_Head'], u'ORGFBXASC045thumbFBXASC04601FBXASC046L': [u'Bind_LeftHandThumb1'], u'ORGFBXASC045f_pinkyFBXASC04602FBXASC046L': [u'Bind_LeftHandPinky2'], u'ORGFBXASC045thighFBXASC046R': [u'Bind_RightUpLeg'], u'ORGFBXASC045neck': [u'Bind_Neck'], u'ORGFBXASC045shoulderFBXASC046L': [u'Bind_LeftShoulder'], u'ORGFBXASC045f_indexFBXASC04601FBXASC046R': [u'Bind_RightHandIndex1'], u'ORGFBXASC045chest': [u'Bind_Spine1'], u'ORGFBXASC045f_ringFBXASC04601FBXASC046R': [u'Bind_RightHandRing1'], u'ORGFBXASC045handFBXASC046R': [u'Bind_RightHand'], u'ORGFBXASC045f_middleFBXASC04603FBXASC046R': [u'Bind_RightHandMiddle3'], u'ORGFBXASC045f_middleFBXASC04603FBXASC046L': [u'Bind_LeftHandMiddle3'], u'ORGFBXASC045forearmFBXASC046R': [u'Bind_RightForeArm'], u'ORGFBXASC045handFBXASC046L': [u'Bind_LeftHand'], u'ORGFBXASC045f_ringFBXASC04601FBXASC046L': [u'Bind_LeftHandRing1'], u'ORGFBXASC045f_indexFBXASC04601FBXASC046L': [u'Bind_LeftHandIndex1'], u'ORGFBXASC045shoulderFBXASC046R': [u'Bind_RightShoulder'], u'ORGFBXASC045thighFBXASC046L': [u'Bind_LeftUpLeg'], u'ORGFBXASC045thumbFBXASC04601FBXASC046R': [u'Bind_RightHandThumb1'], u'ORGFBXASC045thumbFBXASC04603FBXASC046R': [u'Bind_RightHandThumb3'], u'ORGFBXASC045thumbFBXASC04602FBXASC046L': [u'Bind_LeftHandThumb2'], u'ORGFBXASC045forearmFBXASC046L': [u'Bind_LeftForeArm'], u'ORGFBXASC045f_middleFBXASC04602FBXASC046R': [u'Bind_RightHandMiddle2'], u'ORGFBXASC045f_middleFBXASC04602FBXASC046L': [u'Bind_LeftHandMiddle2'], u'ORGFBXASC045thumbFBXASC04602FBXASC046R': [u'Bind_RightHandThumb2'], u'ORGFBXASC045shinFBXASC046L': [u'Bind_LeftLeg'], u'ORGFBXASC045f_pinkyFBXASC04601FBXASC046R': [u'Bind_RightHandPinky1']}

    maya.cmds.currentUnit(l="m")

    root = "root"

    orderedHierarchy = {}
    MapHierarchyRecursivelyFrom(root, orderedHierarchy, -1)
    
    # setScl(root, (1,1,1))
    maya.cmds.select("root", hi=True)
    allJoints = maya.cmds.ls(selection=True)
    
    handJoints = []
    for j in allJoints:
        if "Constraint" in j:
            continue
        SetFloat("visibility", j, 1.0)
        if "palm" in str(j):
            maya.cmds.select(j, hi=True)
            handJoints += (maya.cmds.ls(selection=True))
    
    # set joint sizes
    for j in allJoints:
        if "Constraint" in j:
            continue
        SetFloat("radius", j, 1.0)
    
    for j in handJoints:
        if "Constraint" in j:
            continue
        SetFloat("radius", j, 0.5)
    
    sortedConstraintMapping = []
    for i in range(0,15):
        for joint in orderedHierarchy.keys():
            level = orderedHierarchy[joint][0]
            if(level == i):
                try:
                    sortedConstraintMapping.append([joint, constraintMapping[joint]])
                except:
                    pass
                    #print(joint)
            
#    print(sortedConstraintMapping)

    controlRigExists = False
    try:
        # SETUP POSITIONS
        for i in range(len(sortedConstraintMapping)):
            toJoint = sortedConstraintMapping[i][0]
            fromJoint = str(sortedConstraintMapping[i][1]).replace("[u'","").replace("']","")
            fromJoint = fromJoint.replace("Bind_", "mixamorig:")

            op = GetJointPosition(toJoint)

            SetJointPosition(fromJoint, op)
    except:
        controlRigExists = True

        maya.cmds.select("root", hi=True)

    if not controlRigExists:
        MayaAutoControlRig.UI.Main_UI.MIXAMO_AutoControlRig_UI()
        return

    # IF RIG EXISTS:

    # SETUP CONSTRAINTS
    for i in range(len(sortedConstraintMapping)):
        blenderJoint = sortedConstraintMapping[i][0]
        rigJoint = str(sortedConstraintMapping[i][1]).replace("[u'","").replace("']","")

        constraint = GetParentConstraint(blenderJoint)

        if constraint is None:
            constraint = SetupParentConstraint(rigJoint, blenderJoint)
        else:
            print("Found existing constraint on " + PrettyFBXName(blenderJoint))
            
    for control in controls:
        controlName = control.lower()
        #fingers
        if "index" in controlName or "middle" in controlName or "thumb" in controlName or "ring" in controlName or "pinky" in controlName:
            print(controlName + " is finger")
            maya.cmds.hilite(control)
            maya.cmds.select(control + "Shape.cv[0:2]", control + "Shape.cv[4:7]", r=True)
            maya.cmds.select(control + ".cv[0:2]", control + ".cv[4:7]", add=True)
#            print(maya.cmds.ls(selection=True))

            clst = maya.cmds.cluster()
            print(clst)
            pos = maya.cmds.xform(clst[1], q=True, ws=True, rp=True)
            maya.cmds.scale(100, 100, 100, r=True, pivot=pos)
            
            maya.cmds.delete(clst[1])
        elif "shoulder" in controlName:
            print(controlName + " is shoulder")
        elif "fk" in controlName:
            print(controlName + " is FK control")
        else:
            print(controlName + " needs definition")
        

    # scale components

    # setup layers
    
    #createDisplayLayer -name "layer1" -number 1 -empty;
    
    #editDisplayLayerMembers -noRecurse layer1 `ls -selection`;

def SetupParentConstraint(parent, child, keepOffset=True):
    print("Creating parent constraint on " + child, parent)
    return maya.cmds.parentConstraint(parent, child, mo=keepOffset)

def GetParentConstraint(obj):
    return maya.cmds.parentConstraint(obj, q=True)

def GetJointPosition(joint):
    return maya.cmds.joint(joint, q=True, position=True)
def GetJointRotation(joint):
    return maya.cmds.joint(joint, q=True, rotation=True)
def GetJointScale(joint):
    return maya.cmds.joint(joint, q=True, scale=True)

def SetJointPosition(joint, value):
    return maya.cmds.joint(joint, e=True, position=value)
def SetJointRotation(joint, value):
    return maya.cmds.joint(joint, e=True, rotation=value)
def SetJointScale(joint, value):
    return maya.cmds.joint(joint, e=True, scale=value)

def PrettyFBXName(uglyName):
    prettyName = uglyName.replace("FBXASC045","-").replace("FBXASC046", ".")
    return prettyName
    
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
    return SetVector("rotate", transform, value)
def SetLoc(transform, value):
    return SetVector("translate", transform, value)
def SetScl(transform, value):
    return SetVector("scale", transform, value)
    
if(__name__ == "__main__"):
    DoIt()
    

