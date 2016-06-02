import random

def enlarge(list1,interval):
	retList = list1.copy()
	for i in range(1,len(retList)//interval):
		retList.insert(i*(interval+1)-1,0)
	list1 [:] = retList

myList1 = [random.randint(-10,10) for i in range(0,10)]
myList2 = [random.randint(-10,10) for i in range(0,8)]

print(myList1)
enlarge(myList1,1)
print(myList1)
