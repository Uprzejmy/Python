import time

def myPrint(s,length=80):
	numberOfSpaces = (length - len(s))//2
	print("-"*(numberOfSpaces-1),s,"-"*(length-len(s)-numberOfSpaces-1))


def credits(*argv1,**argv2):
	for s in argv1:
		myPrint(s)
		time.sleep(1)

	keys = sorted(argv2.keys())
	for key in keys:
		myPrint(key+": "+argv2[key])
		time.sleep(1)


credits("Program napisy końcowe", "Twórcy:", projkt_graficzny="ŁM", wykonanie="Łm")