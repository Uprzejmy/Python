def isPrime(number)->bool:
	for x in range(2,number):
		if number % x == 0:
			return False

	else:
		return True

def mersenneNumber(p)->int:
	return 2**p -1


for x in range(1,32):
	y = mersenneNumber(x)
	print(x,": ",y,": ",isPrime(y))