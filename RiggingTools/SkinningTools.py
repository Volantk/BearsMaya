import maya

def ExportDeformer(mesh, deformerName):
    return maya.cmds.deformerWeights(mesh+".xml", ex=True, deformer=deformerName)

def ImportDeformer(mesh, deformerName):
    return maya.cmds.deformerWeights(mesh+".xml", im=True, deformer=deformerName)
    
def SaveAndClearWeights(rootBone, mesh, deformerName):
    
    maya.cmds.select(mesh)
    output = ExportDeformer(mesh, deformerName)
    maya.cmds.skinCluster(mesh, e=True, unbind=True)
    
    return output
    
def RestoreWeights(rootBone, mesh, deformerName):
    maya.cmds.skinCluster( rootBone, mesh)
    ImportDeformer(mesh, deformerName)
    
def FixSkinnedMeshScale(rigParent, rootBone, mesh, deformerName):
    
    SaveAndClearWeights(rootBone, mesh, deformerName)
    
    maya.cmds.select(rigParent, hi=True)
    maya.cmds.cutKey(maya.cmds.ls(selection=True))
    
    maya.cmds.select(mesh)
    maya.cmds.cutKey(maya.cmds.ls(selection=True))
    maya.cmds.makeIdentity(apply=True)
    
    maya.cmds.select(rigParent)
    maya.cmds.makeIdentity(apply=True)

    RestoreWeights(rootBone, mesh, deformerName)
    
def Main():
    sel = maya.cmds.ls(selection=True)
    
    rigParent = "Bass_rig"
    mesh = "Bass"
    rootBone = "root"
    deformerName = "skinCluster1"

    FixSkinnedMeshScale(rigParent, rootBone, mesh, deformerName)
    
    maya.cmds.select(sel)
    
Main()

def NameSelectedAfterParent(prefix, suffix):
    for obj in maya.cmds.ls(selection=True):
        parentName = maya.cmds.listRelatives(obj, p=True)[0]
        newName = prefix + parentName + suffix;
        print(newName)
        maya.cmds.rename(obj, newName)
        
#NameSelectedAfterParent("", "_CTRL")