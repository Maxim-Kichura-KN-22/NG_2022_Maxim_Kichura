print("Factorials to God of Factorials")
try:
	num = int(input("Enter a natural number: "))
	if num < 1:
		raise ValueError("ERR01 A natural number is required.")

	fal = 1

	for a in range(2, num + 1):
		fal = fal * a

	print(str(num) + " factorial is " + str(fal))
except ValueError:
	print("ERR02 INVALID number detected.")