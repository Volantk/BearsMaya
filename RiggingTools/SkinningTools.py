import maya.cmds

def ExportDeformer(mesh, deformerName):
    return cmds.deformerWeights(mesh+".xml", ex=True, deformer=deformerName)

def ImportDeformer(mesh, deformerName):
    return cmds.deformerWeights(mesh+".xml", im=True, deformer=deformerName)
    
def SaveAndClearWeights(rootBone, mesh, deformerName):
    
    cmds.select(mesh)
    output = ExportDeformer(mesh, deformerName)
    cmds.skinCluster(mesh, e=True, unbind=True)
    
    return output
    
def RestoreWeights(rootBone, mesh, deformerName):
    cmds.skinCluster( rootBone, mesh)
    ImportDeformer(mesh, deformerName)
    
def FixSkinnedMeshScale(rigParent, rootBone, mesh, deformerName="skinCluster1"):
    
    SaveAndClearWeights(rootBone, mesh, deformerName)
    
    cmds.select(rigParent, hi=True)
    cmds.cutKey(cmds.ls(selection=True))
    
    cmds.select(rigParent)
    cmds.makeIdentity(apply=True)

    RestoreWeights(rootBone, mesh, deformerName)
    
def Main():
    sel = cmds.ls(selection=True)
    
    rigParent = "Bass_Daydream_GrabbyHand_RIG"
    mesh = "Bass_Daydream_GrabbyHand_Mesh"
    rootBone = "root"
    deformerName = "skinCluster1"

    FixSkinnedMeshScale(rigParent, rootBone, mesh, deformerName)
    
    cmds.select(sel)
    
Main()

def NameSelectedAfterParent(prefix, suffix):
    for obj in cmds.ls(selection=True):
        parentName = cmds.listRelatives(obj, p=True)[0]
        newName = prefix + parentName + suffix;
        print(newName)
        cmds.rename(obj, newName)
        
#NameSelectedAfterParent("", "_CTRL")