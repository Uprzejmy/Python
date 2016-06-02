number = int(input("Podaj liczbe do sprawdzenia czy jest pierwsza: "))

for x in range(2,number):
	if number % x == 0:
		print("Liczba ",number," nie jest pierwsza")
		break

else:
	print("Liczba ",number," jest pierwsza")