year = int(input("Podaj rok: "))

if year%400 == 0:
	print("rok ", year, " jest przestepny")
elif year%100 == 0:
	print("rok ", year, " nie jest przestepny")
elif year%4 == 0:
	print("rok ", year, " jest przestepny")
else:
	print("rok ", year, " nie jest przestepny")