def listparameters(list):
	print("min: ",min(list))
	print("max: ",max(list))
	sum = 0
	for i in list:
		sum = sum + i
	print("avg: ", sum/len(list))

listparameters([0,1,2,3,4,5,6,7,3,4,2,12,432,2])