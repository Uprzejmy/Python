import math

def nextSum(x, y):
    return (y, x+y);

def fibonacci(n):
	t = (0,1)
	for x in range(1,n):
		t = nextSum(t[0],t[1])
	print(t[1])

number = int(input("Podaj ktory wyraz ciagu fib chcesz poznac: "))
fibonacci(number)
