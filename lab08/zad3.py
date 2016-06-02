import random

def copyList(list):
	return [el for el in list]

myList = [random.randint(0,10) for i in range(0,10)]

print(myList)
newList = copyList(myList)
myList[0] = 120
print(myList)
print(newList)
