##
## Author:	Owen Cocjin
## Version:	1.4.2
## Date:	2021.04.14
## Description:	Example menuentries file
## Notes:
##    - Added recurse examples
## Updates:
##    - Added nested recursed entries
##    - Commented out nested recursed entries (they would throw an error otherwise)
##    - Adding recurses for testing
from progmenu import EntryFlag, EntryArg, EntryKeyArg
#Menu Entry functions
def noargFunc():
	'''Takes no arguments'''
	print("NOARG: This takes no args!")
	return True

def argFunc(x):
	'''Normally you use this mode to get an arg from the user.
	This is ignored if no arg passed'''
	print(f"ARG: You gave me: {x}!")
	return x

def kwargFunc(x='Bad'):
	'''Like mode 1, but has a value if no arg given.
	If not called, uses default value (passed in EntryKeyArg)!'''
	print(f"KWARG: What I have is: {x}!")
	return x

def strictFunc():
	'''This flag MUST be called if PARSER is strict'''
	print("STRICT: You have to call me!")
	return True

def strictArgFunc(x):
	'''This takes an arg and is strict'''
	print(f"STRICTARG: You've given me {x}!")
	return x

def recurseFunc(x, y):
	'''This reads arguments from other flags!'''
	print(f"RECURSE: Arg is '{x}' and noarg is '{y}'!")
	return x, y

def argcurseFunc(arg, rec):
	'''This takes an arg AND recurse'''
	print(f"ARGCURSE: Your arg is '{arg}' and the recurse is '{rec}'")
	return arg

#Menu Entries
EntryArg("argcurse", ['z', "argcurse"], argcurseFunc, recurse=["recurse"])
EntryFlag("noarg", ['n', "noarg"], noargFunc, default='Nothing')
EntryArg("arg", ['a', "arg"], argFunc)
EntryKeyArg("kwarg", ['k', "kwarg"], kwargFunc, default="default", recurse=["recurse"])
EntryFlag("strictflag", ['s', "strict"], strictFunc, strict=True)
EntryArg("strictarg", ['r', "sarg", "strictarg"], strictArgFunc, strict=False)
EntryFlag("recurse", ['c', "recurse"], recurseFunc, recurse=["arg", "noarg"])
#Uncomment these to test invalid recurses
#EntryFlag("nested", ['d'], lambda _:True, recurse=["looped"])
#EntryFlag("looped", ['l'], lambda _:True, recurse=["toodeep"])
#EntryFlag("toodeep", ['t'], lambda _:True, recurse=["nested"])
