print ("NumLetter Sorter V1")
occurrence = {}
row = input("Enter a row: ")

for element in row:
	if element in occurrence: occurrence[element] = occurrence[element] + 1
	else: occurrence[element] = 1

print("Sorted by letter: " + str(dict(sorted(occurrence.items()))))
print("Sorted by number: " + str(dict(sorted(occurrence.items(), key=lambda item: item[1], reverse=True))))
print("here is your result Enjoy our sorting : )")