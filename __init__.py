print("__init__.py for Bears")
try:
	import MayaUtils
	import RiggingTools
except Exception as e:
	print("...FAILED!",e)
	raise e
print("...imported successfully!")