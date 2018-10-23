import maya.cmds
import MayaAutoControlRig

from BearsMaya import MayaUtils

def MapHierarchyRecursivelyFrom(node, orderedHierarchyDict, level):
    level += 1
    relatives = maya.cmds.listRelatives(node)
    if(node not in orderedHierarchyDict.keys()):
        orderedHierarchyDict[node] = [level, relatives]
    if relatives != [] and relatives is not None:
        for relative in relatives:
            MapHierarchyRecursivelyFrom(relative, orderedHierarchyDict, level)
    return orderedHierarchyDict
       
def DoIt():
    exportBoneKey = "$EXPORTPREFIX$"
    bindBoneKey = "$BINDPREFIX$"
    ctrlSuffixKey = "$CTRLNAME$"

    controls = ["global_$CTRLNAME$", "Head_$CTRLNAME$", "LeftArm_FK_$CTRLNAME$", "LeftFoot_FK_$CTRLNAME$", "LeftFoot_IK_$CTRLNAME$", "LeftForeArm_FK_$CTRLNAME$", "LeftForeArm_IK_$CTRLNAME$", "LeftHand_FK_$CTRLNAME$", "LeftHand_IK_$CTRLNAME$", "LeftHandIndex1_$CTRLNAME$", "LeftHandIndex2_$CTRLNAME$", "LeftHandIndex3_$CTRLNAME$", "LeftHandMiddle1_$CTRLNAME$", "LeftHandMiddle2_$CTRLNAME$", "LeftHandMiddle3_$CTRLNAME$", "LeftHandPinky1_$CTRLNAME$", "LeftHandPinky2_$CTRLNAME$", "LeftHandPinky3_$CTRLNAME$", "LeftHandRing1_$CTRLNAME$", "LeftHandRing2_$CTRLNAME$", "LeftHandRing3_$CTRLNAME$", "LeftHandThumb1_$CTRLNAME$", "LeftHandThumb2_$CTRLNAME$", "LeftHandThumb3_$CTRLNAME$", "LeftLeg_FK_$CTRLNAME$", "LeftLeg_IK_$CTRLNAME$", "LeftShoulder_$CTRLNAME$", "LeftToeBase_FK_$CTRLNAME$", "LeftUpLeg_FK_$CTRLNAME$", "Neck_$CTRLNAME$", "RightArm_FK_$CTRLNAME$", "RightFoot_FK_$CTRLNAME$", "RightFoot_IK_$CTRLNAME$", "RightForeArm_FK_$CTRLNAME$", "RightForeArm_IK_$CTRLNAME$", "RightHand_FK_$CTRLNAME$", "RightHand_IK_$CTRLNAME$", "RightHandIndex1_$CTRLNAME$", "RightHandIndex2_$CTRLNAME$", "RightHandIndex3_$CTRLNAME$", "RightHandMiddle1_$CTRLNAME$", "RightHandMiddle2_$CTRLNAME$", "RightHandMiddle3_$CTRLNAME$", "RightHandPinky1_$CTRLNAME$", "RightHandPinky2_$CTRLNAME$", "RightHandPinky3_$CTRLNAME$", "RightHandRing1_$CTRLNAME$", "RightHandRing2_$CTRLNAME$", "RightHandRing3_$CTRLNAME$", "RightHandThumb1_$CTRLNAME$", "RightHandThumb2_$CTRLNAME$", "RightHandThumb3_$CTRLNAME$", "RightLeg_FK_$CTRLNAME$", "RightLeg_IK_$CTRLNAME$", "RightShoulder_$CTRLNAME$", "RightToeBase_FK_$CTRLNAME$", "RightUpLeg_FK_$CTRLNAME$", "Root_$CTRLNAME$", "Spine1_$CTRLNAME$", "Spine2_$CTRLNAME$", "Spine_$CTRLNAME$"]
    constraintMapping = {u'$EXPORTPREFIX$FBXASC045toeFBXASC046L': [u'$BINDPREFIX$LeftToeBase'], u'$EXPORTPREFIX$FBXASC045upper_armFBXASC046L': [u'$BINDPREFIX$LeftArm'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandRing2'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandIndex2'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandPinky1'], u'$EXPORTPREFIX$FBXASC045hips': [u'$BINDPREFIX$Hips'], u'$EXPORTPREFIX$FBXASC045shinFBXASC046R': [u'$BINDPREFIX$RightLeg'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandPinky3'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandIndex2'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandRing2'], u'$EXPORTPREFIX$FBXASC045toeFBXASC046R': [u'$BINDPREFIX$RightToeBase'], u'$EXPORTPREFIX$FBXASC045upper_armFBXASC046R': [u'$BINDPREFIX$RightArm'], u'$EXPORTPREFIX$FBXASC045footFBXASC046L': [u'$BINDPREFIX$LeftFoot'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandPinky2'], u'$EXPORTPREFIX$FBXASC045footFBXASC046R': [u'$BINDPREFIX$RightFoot'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandPinky3'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandThumb3'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandIndex3'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandMiddle1'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandRing3'], u'$EXPORTPREFIX$FBXASC045spine': [u'$BINDPREFIX$Spine'], u'$EXPORTPREFIX$FBXASC045head': [u'$BINDPREFIX$Head'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle1'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandRing3'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandIndex3'], u'ATTACHFBXASC045head': [u'$BINDPREFIX$Head'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandThumb1'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandPinky2'], u'$EXPORTPREFIX$FBXASC045thighFBXASC046R': [u'$BINDPREFIX$RightUpLeg'], u'$EXPORTPREFIX$FBXASC045neck': [u'$BINDPREFIX$Neck'], u'$EXPORTPREFIX$FBXASC045shoulderFBXASC046L': [u'$BINDPREFIX$LeftShoulder'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandIndex1'], u'$EXPORTPREFIX$FBXASC045chest': [u'$BINDPREFIX$Spine1', u'$BINDPREFIX$Spine2'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandRing1'], u'$EXPORTPREFIX$FBXASC045handFBXASC046R': [u'$BINDPREFIX$RightHand'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandMiddle3'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle3'], u'$EXPORTPREFIX$FBXASC045forearmFBXASC046R': [u'$BINDPREFIX$RightForeArm'], u'$EXPORTPREFIX$FBXASC045handFBXASC046L': [u'$BINDPREFIX$LeftHand'], u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandRing1'], u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandIndex1'], u'$EXPORTPREFIX$FBXASC045shoulderFBXASC046R': [u'$BINDPREFIX$RightShoulder'], u'$EXPORTPREFIX$FBXASC045thighFBXASC046L': [u'$BINDPREFIX$LeftUpLeg'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandThumb1'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandThumb3'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandThumb2'], u'$EXPORTPREFIX$FBXASC045forearmFBXASC046L': [u'$BINDPREFIX$LeftForeArm'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandMiddle2'], u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle2'], u'$EXPORTPREFIX$FBXASC045thumbFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandThumb2'], u'$EXPORTPREFIX$FBXASC045shinFBXASC046L': [u'$BINDPREFIX$LeftLeg'], u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandPinky1']}

    controlName = "CTRL"
    exportBonePrefix = "ORG"
    bindBonePrefix = "Bind_"
    
    # SETUP NAMES
    for i in range(0,len(controls)):
        controls[i] = controls[i].replace(ctrlSuffixKey, controlName)
    
    for key in constraintMapping:
        newKey = key.replace(exportBoneKey, exportBonePrefix)
        constraintMapping[newKey] = constraintMapping.pop(key)
    
    for key in constraintMapping:
        constraintMapping[key][0] = constraintMapping[key][0].replace(bindBoneKey, bindBonePrefix)


    maya.cmds.currentUnit(l="m")

    root = "root"
    
    maya.cmds.select("root", hi=True)
    allJoints = [j for j in maya.cmds.ls(selection=True) if "Constraint" not in j]
    
    handJoints = []
    for j in allJoints:
        SetFloat("visibility", j, 1.0)
        SetFloat("radius", j, 1.0)
        if "hand" in str(j):
            maya.cmds.select(j, hi=True)
            handJoints += (maya.cmds.ls(selection=True))
            SetFloat("radius", j, 0.5)
    
    for j in handJoints:
        SetFloat("radius", j, 0.5)
        

    orderedHierarchy = {}
    orderedHierarchy = MapHierarchyRecursivelyFrom(root, orderedHierarchy, -1)
    
    print("hierarchy", orderedHierarchy)
    
    sortedConstraintMapping = []
    for i in range(0,15):
        for joint in orderedHierarchy.keys():
            level = orderedHierarchy[joint][0]
            if(level == i):
                if(joint in constraintMapping):
                    sortedConstraintMapping.append([joint, constraintMapping[joint]])
                    
    print("sortedConstraintMapping", sortedConstraintMapping)

    controlRigExists = False
    try:
        print("yes")
        # SETUP POSITIONS
        for i in range(len(sortedConstraintMapping)):
            toJoint = sortedConstraintMapping[i][0]
            fromJoint = str(sortedConstraintMapping[i][1]).replace("[u'","").replace("']","")
            fromJoint = fromJoint.replace(bindBonePrefix, "mixamorig:")
            print(fromJoint, toJoint)

            op = GetJointPosition(toJoint)

            SetJointPosition(fromJoint, op)
    except:
        controlRigExists = True

        maya.cmds.select("root", hi=True)
        
    print(controlRigExists)

    if not controlRigExists:
        # IF RIG DOESN'T EXIST, SHOW UI FOR MAKING IT!
        MayaAutoControlRig.UI.Main_UI.MIXAMO_AutoControlRig_UI()
        return

    # SETUP CONSTRAINTS
    for i in range(len(sortedConstraintMapping)):
        blenderJoint = sortedConstraintMapping[i][0]
        rigJoint = str(sortedConstraintMapping[i][1]).replace("[u'","").replace("']","")

        constraint = GetParentConstraint(blenderJoint)

        if constraint is None:
            constraint = SetupParentConstraint(rigJoint, blenderJoint)
            print("constrained " + rigJoint + " " + blenderJoint)
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
            
           # maya.cmds.delete(clst[1])
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
    

