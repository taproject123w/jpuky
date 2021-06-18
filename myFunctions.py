#imports 
import sys
sys.path.insert(0, "../")
sys.path.insert(0, "./")
import globalsettings

# functions which are called by function handlers are placed in the MenuFunc_Base class
class MenuFunc_Base:
	def myFunction1():
		if (globalsettings.DEBUGFLAG >= 1):
			print("This is myFunction1")

	def myFunction2():
		if (globalsettings.DEBUGFLAG >= 1):
			print("This is myFunction2")


# dictionary to hold function handlers
#functionHandlersDictionary = { "myFunction1":  [MenuFunc_Base.myFunction1, "My function 1"], "myFunction2": [MenuFunc_Base.myFunction2, "My Function 2"]}
