import maya.cmds as mayac

def Get(attr, transform):
    return mayac.getAttr(str("%s."+attr) % transform)
    
def SetVector(attr, transform, value):
    return mayac.setAttr(str("%s."+attr) % transform, type="float3", *value)    

def SetFloat(attr, transform, value):
    return mayac.setAttr(str("%s."+attr) % transform, value, type="float")    
    