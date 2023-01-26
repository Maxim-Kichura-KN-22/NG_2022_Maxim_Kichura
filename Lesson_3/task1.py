print("Bayan Kalkulator 3-rd Lection")
import sys

def add (firstNum, secondNum): return firstNum + secondNum
def substract(firstNum, secondNum): return firstNum - secondNum
def multiply(firstNum, secondNum): return firstNum * secondNum
def divide(firstNum, secondNum):
	if secondNum == 0:
		print("Division by zero.")
		sys.exit(2)
	else:
		return firstNum / secondNum
def square(num): return num**2

def isNatural(num): return False if num < 1 or not num.is_integer() else True
def isEven(num): return True if (num % 2) == 0 else False
def isNegative(num): return True if num < 0 else False

def root(num, degree):
	if not isNatural(degree):
		print("Can't extract a root with non-natural degree.")
		sys.exit(3)
	elif isEven(degree) and isNegative(num):
		print("Can't extract a root of a negative number with an even degree.")
		sys.exit(4)
	else:
		if num < 0:
			return -abs(num ** (1 / degree))
		else:
			return num ** (1 / degree)

try:
	firstNum = float(input("Enter the first number: "))
	secondNum = float(input("Enter the second number: "))
except ValueError:
	print("ERR01 Invalid numbers entered.")
	sys.exit(1)

print(
'''
Valid operations:
Addition: +
Subtraction: - 
Multiplication: * or 1
Division: / or 2
Root: root or 3
Square: square or 4 ''', end="\n\n"
)

operation = input("Enter operation: ")

if operation == "+":
	print(add(firstNum, secondNum))
elif operation == "-" : 
	print(substract(firstNum, secondNum))
elif operation == "*" or operation == "1":
	print(multiply(firstNum, secondNum))
elif operation == "/" or operation == "2": 
	print(divide(firstNum, secondNum))
elif operation == "root" or operation == "3": 
	print(root(firstNum, secondNum))
elif operation == "square" or operation == "4":
	print("First number square: " + str(square(firstNum)) + "\n Second number square: " + str(square(secondNum)))
else:
	print("ERR02 Invalid operation.")
	sys.exit(5)