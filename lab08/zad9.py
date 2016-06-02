def countVowels(s):
	counter=0
	for c in s:
		if c in ["a","e","i","o","u","y"]:
			counter = counter+1

	return counter


def cleanList(myList):
	return [s for s in myList if countVowels(s)%2==0]

print(cleanList(["robot", "mech", "metal gear", "android"]))
