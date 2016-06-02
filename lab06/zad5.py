
i=0
while i < 2:

	day = (input("Podaj dzień tygodnia: "))

	if day == "Monday":
		print("Poniedzialek jest slaby")
	elif day == "Tuesday":
		print("Wtorek jest lepszy")
	elif day == "Wednesday":
		print("Sroda jest super")
	elif day == "Thursday":
		print("Czwartek jest sredni")
	elif day == "Friday":
		print("Piatek jest w porzadku")
	elif day == "Saturday":
		print("Sobota jest swietna")
	elif day == "Sunday":
		print("Niedziela jest najlepsza!")
	else:
		i = i+1
		if i < 2:
			print("Jestes gupi?... Sprobuj jeszcze raz")

else:
	print("Jednak jestes gupi...")