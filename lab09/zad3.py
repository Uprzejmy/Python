import random

def blur(list1,wages):
	retList = [(list1[i-1]*wages[i-1]+list1[i]*wages[i]+list1[i+1]*wages[i+1])/(wages[i-1]+wages[i]+wages[i+1]) for i in range(1,len(list1)-1)]
	retList.insert(0,list1[0])
	retList.append(list1[-1])
	return retList

myList1 = [random.randint(0,10) for i in range(0,10)]
myList2 = [random.randint(0,10) for i in range(0,10)]

print(myList1)
print(myList2)
print(blur(myList1,myList2))

