import random

def addLists(list1,list2):
	return [list1[i]/list2[i] for i in range(0,min(len(list1),len(list2))) if list2[i]!=0]

myList1 = [random.randint(0,10) for i in range(0,10)]
myList2 = [random.randint(0,10) for i in range(0,8)]

print(myList1)
print(myList2)
newList = addLists(myList1,myList2)
print(newList)
