import random

def cleanList(list1):
	del list1[::3]
	list1[:] = [el for el in list1 if el>=0]

myList1 = [random.randint(-10,10) for i in range(0,10)]
myList2 = [random.randint(-10,10) for i in range(0,8)]

print(myList1)
cleanList(myList1)
print(myList1)
