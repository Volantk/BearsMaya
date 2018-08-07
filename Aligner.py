def AlignPositionRotation():
    selection = cmds.ls(selection=True)
    
    if(len(selection) <= 1):
       print("Must select at least 2 objects")
       return
       
    destinationObj = selection[0]
    toBeAlignedObj = selection[1:]
    
    pos = cmds.xform(destinationObj, q=True, t=True)
    rot = cmds.xform(destinationObj, q=True, ro=True)
       
    cmds.xform(toBeAlignedObj, ws=True, t=pos, ro=rot)
    
AlignPositionRotation()