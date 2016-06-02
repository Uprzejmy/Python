import random

def blur(list):
	retList = [list[0]]
	for i in range(1,len(list)-1):
		retList.append((list[i-1]+list[i]+list[i+1])/3)
	retList.append(list[-1])
	return retList

myList = [random.randint(0,10) for i in range(0,10)]

print(myList)
print(blur(myList))

