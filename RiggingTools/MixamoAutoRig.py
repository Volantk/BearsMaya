import maya
import MayaAutoControlRig
from BearsMaya import MayaUtils
from BearsMaya.RiggingTools import SkinningTools


def MapHierarchyRecursivelyFrom(node, orderedHierarchyDict, level):
    level += 1
    relatives = maya.cmds.listRelatives(node)
    if node not in orderedHierarchyDict.keys():
        orderedHierarchyDict[node] = [level, relatives]
    if relatives != [] and relatives is not None:
        for relative in relatives:
            MapHierarchyRecursivelyFrom(relative, orderedHierarchyDict, level)
    return orderedHierarchyDict


def DoIt():
    export_bone_key = "$EXPORTPREFIX$"
    bind_bone_key = "$BINDPREFIX$"
    ctrl_suffix_key = "$CTRLNAME$"

    controls = ["global_$CTRLNAME$", "Head_$CTRLNAME$", "LeftArm_FK_$CTRLNAME$", "LeftFoot_FK_$CTRLNAME$",
                "LeftFoot_IK_$CTRLNAME$", "LeftForeArm_FK_$CTRLNAME$", "LeftForeArm_IK_$CTRLNAME$",
                "LeftHand_FK_$CTRLNAME$", "LeftHand_IK_$CTRLNAME$", "LeftHandIndex1_$CTRLNAME$",
                "LeftHandIndex2_$CTRLNAME$", "LeftHandIndex3_$CTRLNAME$", "LeftHandMiddle1_$CTRLNAME$",
                "LeftHandMiddle2_$CTRLNAME$", "LeftHandMiddle3_$CTRLNAME$", "LeftHandPinky1_$CTRLNAME$",
                "LeftHandPinky2_$CTRLNAME$", "LeftHandPinky3_$CTRLNAME$", "LeftHandRing1_$CTRLNAME$",
                "LeftHandRing2_$CTRLNAME$", "LeftHandRing3_$CTRLNAME$", "LeftHandThumb1_$CTRLNAME$",
                "LeftHandThumb2_$CTRLNAME$", "LeftHandThumb3_$CTRLNAME$", "LeftLeg_FK_$CTRLNAME$",
                "LeftLeg_IK_$CTRLNAME$", "LeftShoulder_$CTRLNAME$", "LeftToeBase_FK_$CTRLNAME$",
                "LeftUpLeg_FK_$CTRLNAME$", "Neck_$CTRLNAME$", "RightArm_FK_$CTRLNAME$", "RightFoot_FK_$CTRLNAME$",
                "RightFoot_IK_$CTRLNAME$", "RightForeArm_FK_$CTRLNAME$", "RightForeArm_IK_$CTRLNAME$",
                "RightHand_FK_$CTRLNAME$", "RightHand_IK_$CTRLNAME$", "RightHandIndex1_$CTRLNAME$",
                "RightHandIndex2_$CTRLNAME$", "RightHandIndex3_$CTRLNAME$", "RightHandMiddle1_$CTRLNAME$",
                "RightHandMiddle2_$CTRLNAME$", "RightHandMiddle3_$CTRLNAME$", "RightHandPinky1_$CTRLNAME$",
                "RightHandPinky2_$CTRLNAME$", "RightHandPinky3_$CTRLNAME$", "RightHandRing1_$CTRLNAME$",
                "RightHandRing2_$CTRLNAME$", "RightHandRing3_$CTRLNAME$", "RightHandThumb1_$CTRLNAME$",
                "RightHandThumb2_$CTRLNAME$", "RightHandThumb3_$CTRLNAME$", "RightLeg_FK_$CTRLNAME$",
                "RightLeg_IK_$CTRLNAME$", "RightShoulder_$CTRLNAME$", "RightToeBase_FK_$CTRLNAME$",
                "RightUpLeg_FK_$CTRLNAME$", "Root_$CTRLNAME$", "Spine1_$CTRLNAME$", "Spine2_$CTRLNAME$",
                "Spine_$CTRLNAME$"]
    constraintMapping = {u'$EXPORTPREFIX$FBXASC045toeFBXASC046L': [u'$BINDPREFIX$LeftToeBase'],
                         u'$EXPORTPREFIX$FBXASC045upper_armFBXASC046L': [u'$BINDPREFIX$LeftArm'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandRing2'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandIndex2'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandPinky1'],
                         u'$EXPORTPREFIX$FBXASC045hips': [u'$BINDPREFIX$Hips'],
                         u'$EXPORTPREFIX$FBXASC045shinFBXASC046R': [u'$BINDPREFIX$RightLeg'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandPinky3'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandIndex2'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandRing2'],
                         u'$EXPORTPREFIX$FBXASC045toeFBXASC046R': [u'$BINDPREFIX$RightToeBase'],
                         u'$EXPORTPREFIX$FBXASC045upper_armFBXASC046R': [u'$BINDPREFIX$RightArm'],
                         u'$EXPORTPREFIX$FBXASC045footFBXASC046L': [u'$BINDPREFIX$LeftFoot'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandPinky2'],
                         u'$EXPORTPREFIX$FBXASC045footFBXASC046R': [u'$BINDPREFIX$RightFoot'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandPinky3'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandThumb3'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandIndex3'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandMiddle1'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandRing3'],
                         u'$EXPORTPREFIX$FBXASC045spine': [u'$BINDPREFIX$Spine'],
                         u'$EXPORTPREFIX$FBXASC045head': [u'$BINDPREFIX$Head'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle1'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandRing3'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandIndex3'],
                         u'ATTACHFBXASC045head': [u'$BINDPREFIX$Head'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandThumb1'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandPinky2'],
                         u'$EXPORTPREFIX$FBXASC045thighFBXASC046R': [u'$BINDPREFIX$RightUpLeg'],
                         u'$EXPORTPREFIX$FBXASC045neck': [u'$BINDPREFIX$Neck'],
                         u'$EXPORTPREFIX$FBXASC045shoulderFBXASC046L': [u'$BINDPREFIX$LeftShoulder'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandIndex1'],
                         u'$EXPORTPREFIX$FBXASC045chest': [u'$BINDPREFIX$Spine1', u'$BINDPREFIX$Spine2'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandRing1'],
                         u'$EXPORTPREFIX$FBXASC045handFBXASC046R': [u'$BINDPREFIX$RightHand'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandMiddle3'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04603FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle3'],
                         u'$EXPORTPREFIX$FBXASC045forearmFBXASC046R': [u'$BINDPREFIX$RightForeArm'],
                         u'$EXPORTPREFIX$FBXASC045handFBXASC046L': [u'$BINDPREFIX$LeftHand'],
                         u'$EXPORTPREFIX$FBXASC045f_ringFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandRing1'],
                         u'$EXPORTPREFIX$FBXASC045f_indexFBXASC04601FBXASC046L': [u'$BINDPREFIX$LeftHandIndex1'],
                         u'$EXPORTPREFIX$FBXASC045shoulderFBXASC046R': [u'$BINDPREFIX$RightShoulder'],
                         u'$EXPORTPREFIX$FBXASC045thighFBXASC046L': [u'$BINDPREFIX$LeftUpLeg'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandThumb1'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04603FBXASC046R': [u'$BINDPREFIX$RightHandThumb3'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandThumb2'],
                         u'$EXPORTPREFIX$FBXASC045forearmFBXASC046L': [u'$BINDPREFIX$LeftForeArm'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandMiddle2'],
                         u'$EXPORTPREFIX$FBXASC045f_middleFBXASC04602FBXASC046L': [u'$BINDPREFIX$LeftHandMiddle2'],
                         u'$EXPORTPREFIX$FBXASC045thumbFBXASC04602FBXASC046R': [u'$BINDPREFIX$RightHandThumb2'],
                         u'$EXPORTPREFIX$FBXASC045shinFBXASC046L': [u'$BINDPREFIX$LeftLeg'],
                         u'$EXPORTPREFIX$FBXASC045f_pinkyFBXASC04601FBXASC046R': [u'$BINDPREFIX$RightHandPinky1']}

    control_name = "CTRL"
    export_bone_prefix = "ORG"
    bind_bone_prefix = "Bind_"

    # SETUP NAMES
    for i in range(0, len(controls)):
        controls[i] = controls[i].replace(ctrl_suffix_key, control_name)

    for key in constraintMapping:
        new_key = key.replace(export_bone_key, export_bone_prefix)
        constraintMapping[new_key] = constraintMapping.pop(key)

    for key in constraintMapping:
        for i in range(len(constraintMapping[key])):
            constraintMapping[key][i] = constraintMapping[key][i].replace(bind_bone_key, bind_bone_prefix)

    maya.cmds.currentUnit(l="m")

    root = "root"

    maya.cmds.select("root", hi=True)

    if (len(maya.cmds.ls("mixamorig")) > 0):  # Fix mesh scale
        rigParent = maya.cmds.listRelatives(root, parent=True)[0]
        mesh = "Bass"
        deformerName = "skinCluster1"

        SkinningTools.FixSkinnedMeshScale(rigParent, root, mesh, deformerName)

    all_joints = [j for j in maya.cmds.ls(selection=True) if "Constraint" not in j]

    hand_joints = []
    for j in all_joints:
        SetFloat("visibility", j, 1.0)
        SetFloat("radius", j, 1.0)
        if "hand" in str(j):
            maya.cmds.select(j, hi=True)
            hand_joints += (maya.cmds.ls(selection=True))
            SetFloat("radius", j, 0.5)

    for j in hand_joints:
        SetFloat("radius", j, 0.5)

    ordered_hierarchy = {}
    ordered_hierarchy = MapHierarchyRecursivelyFrom(root, ordered_hierarchy, -1)

    print("hierarchy", ordered_hierarchy)

    sorted_constraint_mapping = []
    for i in range(0, 15):
        for joint in ordered_hierarchy.keys():
            level = ordered_hierarchy[joint][0]
            if level == i:
                if joint in constraintMapping:
                    sorted_constraint_mapping.append([joint, constraintMapping[joint]])

    print("sorted_constraint_mapping", sorted_constraint_mapping)

    control_rig_exists = False
    try:
        print("yes")
        # SETUP POSITIONS
        for i in range(len(sorted_constraint_mapping)):
            to_joint = sorted_constraint_mapping[i][0]

            for fj in sorted_constraint_mapping[i][1]:
                print("fj", fj)
                # from_joint = fj.replace("[u'","").replace("']","")
                from_joint = fj.replace(bind_bone_prefix, "mixamorig:")
                print(from_joint, to_joint)
                op = GetJointPosition(to_joint)
                SetJointPosition(from_joint, op)
    except:
        control_rig_exists = True

        maya.cmds.select("root", hi=True)

    print(control_rig_exists)

    if not control_rig_exists:
        # IF RIG DOESN'T EXIST, SHOW UI FOR MAKING IT!
        MayaAutoControlRig.UI.Main_UI.MIXAMO_AutoControlRig_UI()
        return

    # SETUP CONSTRAINTS
    for i in range(len(sorted_constraint_mapping)):
        blender_joint = sorted_constraint_mapping[i][0]
        for rigJoint in sorted_constraint_mapping[i][1]:

            # rigJoint = str()

            constraint = GetParentConstraint(blender_joint)

            if constraint is None:
                constraint = SetupParentConstraint(rigJoint, blender_joint)
            #    print("constrained " + rigJoint + " " + blender_joint)
            # else:
            #    print("Found existing constraint on " + PrettyFBXName(blender_joint))

    simple_handles_to_fix = ["index", "middle", "thumb", "ring", "pinky", "neck", "leftfoot_fk", "rightfoot_fk",
                             "lefttoebase_fk", "righttoebase_fk", "leg_fk"]
    controls_to_hide = ["spine2"]

    circle_controls_to_scale_up = ["spine1", "root", "spine_"]

    shoulders = ["shoulder"]

    for control in controls:
        c = control.lower()

        # fingers or similar controls
        for h in simple_handles_to_fix:
            if h in c:
                select_and_scale_with_cluster_uniform([control + ".cv[0:2]", control + ".cv[4:7]"], 100)
                break

        for h in controls_to_hide:
            if h in c:
                maya.cmds.setAttr(control + ".dispGeometry", False)
                break

        for h in circle_controls_to_scale_up:
            if h in c:
                select_and_scale_with_cluster_uniform(control + ".cv[0:7]", 100)
                break

        for h in shoulders:
            if h in c:
                break
                maya.cmds.select(all=True, d=True)
                maya.cmds.select(control + ".cv[0:7]")

                rot = maya.cmds.xform(control, q=True, ws=True, ro=True)
                clst = maya.cmds.cluster()
                handle = clst[1]
                SetRot(handle, rot)
                
                #print("before", clst)
                
                print("cluster", maya.cmds.cluster(clst[0], q=True, g=True))
                print("cluster", maya.cmds.cluster(clst[0], q=True, gi=True))
                print("cluster", maya.cmds.cluster(clst[0], q=True, dt=True))
                maya.cmds.cluster(clst[0], e=True, name=clst[0] )

                #print("after", clst)

                # hide cluster
                #maya.cmds.setAttr(handle + ".visibility", False)

                pos = maya.cmds.xform(handle, q=True, ws=True, rp=True)

                maya.cmds.scale(1, 1, 1, r=True, pivot=pos) 

                # select_and_scale_with_cluster(control + ".cv[0:7]", [1, 1, 0.01], [100, 100, 100])
                break

    # CREATE HIP CONTROL IN THE RIGHT PLACE
    root_ctrl = [ctrl for ctrl in controls if "Root_" in ctrl]
    if len(root_ctrl) > 0:
        root_ctrl = root_ctrl[0]
        duplicated_hip_ctrl_hierarchy = maya.cmds.duplicate(root_ctrl, parentOnly=False, name="Hip_CTRL",
                                                            renameChildren=True)
        hip_ctrl = duplicated_hip_ctrl_hierarchy[0]

        duplicated_hip_ctrl_hierarchy.remove(hip_ctrl)

        maya.cmds.delete(duplicated_hip_ctrl_hierarchy)

        leg_bone_left = bind_bone_prefix + "LeftUpLeg"
        leg_bone_right = bind_bone_prefix + "RightUpLeg"

        left_pos = GetLoc(leg_bone_left)
        right_pos = GetLoc(leg_bone_right)
        avg = [left_pos[0] + right_pos[0] * 0.5, left_pos[1] + right_pos[1] * 0.5, left_pos[2] + right_pos[2] * 0.5]

        for i in range(len(left_pos)):
            avg[i] = (left_pos[i] + right_pos[i]) * 0.5

        SetLoc(hip_ctrl, avg)

        maya.cmds.parent(root_ctrl, hip_ctrl)

    # setup layers

    # createDisplayLayer -name "layer1" -number 1 -empty;

    # editDisplayLayerMembers -noRecurse layer1 `ls -selection`;


def select_and_scale_with_cluster_uniform(objects, scale):
    try:
        maya.cmds.select(objects, r=True)
        return CreateClusterFromSelectionAndScale([scale, scale, scale])
    except:
        print("could not find objects: " + objects)
        pass


def select_and_scale_with_cluster(objects, scale, scale2=None):
    try:
        maya.cmds.select(objects, r=True)
        return CreateClusterFromSelectionAndScale([scale[0], scale[1], scale[2]], scale2)
    except:
        print("could not find objects: " + objects)
        pass


def CreateClusterFromSelectionAndScale(scale=[100, 100, 100], scale2=None):
    clst = maya.cmds.cluster()
    handle = clst[1]

    # hide cluster
    maya.cmds.setAttr(handle + ".visibility", False)

    pos = maya.cmds.xform(handle, q=True, ws=True, rp=True)

    maya.cmds.scale(scale[0], scale[1], scale[2], r=True, pivot=pos)

    if (scale2 is not None):
        maya.cmds.scale(scale2[0], scale2[1], scale2[2], r=True, pivot=pos)

    return clst


def SetupParentConstraint(parent, child, keepOffset=True):
    # print("Creating parent constraint on " + child, parent)
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
    prettyName = uglyName.replace("FBXASC045", "-").replace("FBXASC046", ".")
    return prettyName


def CreateLocatorIfNone(locatorName):
    if maya.cmds.ls(locatorName) == []:
        maya.cmds.spaceLocator(p=(0, 0, 0), name=locatorName)
    return locatorName


def AlignMixamoJointsToExistingJoints(jointA, jointB):
    print("oopooopo")


def Get(attr, transform):
    return maya.cmds.getAttr(str("%s." + attr) % transform)


def SetVector(attr, transform, value):
    return maya.cmds.setAttr(str("%s." + attr) % transform, type="float3", *value)


def SetFloat(attr, transform, value):
    return maya.cmds.setAttr(str("%s." + attr) % transform, value)


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


if __name__ == "__main__":
    DoIt()
