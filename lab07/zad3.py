import math

def myPrint(fx,xp=-1,xk=1,interval=10):
	for x in range(xp*10,xk*10,((xk*10 - xp*10)//interval)):
		print("x: ",x/10," fx: ",fx(x/10))


myPrint(lambda x:math.sin(x))
myPrint(lambda x:x**2)