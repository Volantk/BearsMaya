import maya


def fix_skinned_mesh_scale(rig_parent, root_bone, mesh, deformer_name):
    original_selection = maya.cmds.ls(selection=True)
    print("fix_skinned_mesh_scale", rig_parent, root_bone, mesh, deformer_name)
    save_and_clear_weights(mesh, deformer_name)

    maya.cmds.select(rig_parent, hi=True)
    maya.cmds.cutKey(maya.cmds.ls(selection=True))

    maya.cmds.select(mesh)
    maya.cmds.cutKey(maya.cmds.ls(selection=True))
    maya.cmds.makeIdentity(apply=True)

    maya.cmds.select(rig_parent)
    maya.cmds.makeIdentity(scale=True, translate=True, apply=True)

    restore_weight(root_bone, mesh, deformer_name)
    maya.cmds.select(original_selection)


def export_deformer(mesh, deformer_name):
    return maya.cmds.deformerWeights(mesh + ".xml", ex=True, deformer=deformer_name)


def import_deformer(mesh, deformer_name):
    deformer_name = maya.cmds.ls("skinCluster*")[0]
    return maya.cmds.deformerWeights(mesh + ".xml", im=True, deformer=deformer_name)


def save_and_clear_weights(mesh, deformer_name):
    maya.cmds.select(mesh)
    output = export_deformer(mesh, deformer_name)
    maya.cmds.skinCluster(mesh, e=True, unbind=True)

    return output


def restore_weight(root_bone, mesh, deformer_name):
    maya.cmds.skinCluster(root_bone, mesh)
    import_deformer(mesh, deformer_name)


def name_selected_after_parent(prefix, suffix):
    for obj in maya.cmds.ls(selection=True):
        parent_name = maya.cmds.listRelatives(obj, p=True)[0]
        new_name = prefix + parent_name + suffix;
        print(new_name)
        maya.cmds.rename(obj, new_name)
