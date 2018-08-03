def Get(attr, transform):
    return cmds.getAttr(str("%s."+attr) % transform)
    
# NOT WORKING
def Set(attr, transform, value):
    return cmds.setAttr(str("%s."+attr) % transform, type="float3", *value)    
    