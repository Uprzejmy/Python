text = (input("Podaj tekst do tluamczenia: "))
counter = 0

for x in range(0,len(text)):
	if text[x] in ["a","e","i","o","u","y"]:
		text=text[0:x]+"a"+text[x+1:len(text)]
		counter = counter+1

print(text)
print("ilosc samoglosek to: ",counter)
