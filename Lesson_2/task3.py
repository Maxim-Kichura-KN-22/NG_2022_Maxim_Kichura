print(" NNC V1 (Natural Number Chart)")
try:
	num = int(input("Enter a natural number: "))
	if num < 1:
		raise ValueError("ERR01 A Natural number is required.")

	for i in range(num, 0, -1):
		currentNum = i
		for a in range(currentNum, 0, -1):
			print(a, end='')
			if a > 1: print(' ', end='')
		print('')

except ValueError:
	print("ERR02 Invalid number entered.")