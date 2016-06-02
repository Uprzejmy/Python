def myPrint(s,length=80):
	numberOfSpaces = (length - len(s))//2
	print("-"*(numberOfSpaces-1),s,"-"*(length-len(s)-numberOfSpaces-1))


myPrint("razakakraawdawd",80)