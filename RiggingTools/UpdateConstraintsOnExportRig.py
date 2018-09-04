import maya.cmds

def DoIt():
    controlHierarchyPrefix = "CONTROL_"
    root = "root"

    maya.cmds.select(root, hi=True)
    allChildren = maya.cmds.ls(selection=True)
    
    constraints = [child for child in allChildren if "parentConstraint" in child]

    for const in constraints:
        DeleteParentConstraint(const)
        allChildren.remove(const)

    for child in allChildren:
        controlTwin = controlHierarchyPrefix+child
        if len(maya.cmds.ls(controlTwin)) == 0:
            print("Couldn't find control twin for " + child + " (" + controlTwin + ")")
            continue
        SetupParentConstraint(controlTwin, child, True)

def SetupParentConstraint(parent, child, keepOffset=True):
    print("Creating parent constraint on " + child, parent)
    return maya.cmds.parentConstraint(parent, child, mo=keepOffset)

def DeleteParentConstraint(obj):
    print("Deleting parent constraint on " + obj)
    maya.cmds.delete(obj)
    
if(__name__ == "__main__"):
    DoIt()
    

