import math

for x in range(-10,11):
	print(format(x/10, "#8.2f")+" "+format(math.sin(x/10), "#08.6f"))
