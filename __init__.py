print("__init__.py for BearsMaya")
try:
	import maya
	print(maya)
	import MayaUtils
	print(MayaUtils)
	import RiggingTools
	print(RiggingTools)
except Exception as e:
	print("...FAILED!",e)
	raise e
print("...imported successfully!")