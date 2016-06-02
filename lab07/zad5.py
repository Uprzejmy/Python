import time
from sys import stdout

def myPrint(s,length=80):
	numberOfSpaces = (length - len(s))//2
	line = "-"*(numberOfSpaces-1)+s+"-"*(length-len(s)-numberOfSpaces-1)
	#print("-"*(numberOfSpaces-1),s,"-"*(length-len(s)-numberOfSpaces-1))
	for i in range(0,len(line)):
		if line[i] != "-":
			time.sleep(0.1)
		stdout.write('\r'+line[0:i])
	print("")


def credits(*argv1,**argv2):
	for s in argv1:
		myPrint(s)
		time.sleep(1)

	keys = sorted(argv2.keys())
	for key in keys:
		myPrint(key+": "+argv2[key])
		time.sleep(1)


#credits("Program napisy końcowe", "Twórcy:", projkt_graficzny="ŁM", wykonanie="Łm")
print("zle dziala"+'\r')