def printClass(myDict):
	for name,marks in myDict.items():
		print(name)

def printClassWithMarks(myDict):
	for name,marks in myDict.items():
		print(name,": ",marks)


printClass({"Jan": [2,3,4],"Piotr": [1,3,5],"Paweł": [2,5,4,2],"Michał": [1,1,1,1,1]})

printClassWithMarks({"Jan": [2,3,4],"Piotr": [1,3,5],"Paweł": [2,5,4,2],"Michał": [1,1,1,1,1]})