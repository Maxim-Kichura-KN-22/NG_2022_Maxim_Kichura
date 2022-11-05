import math

print("enter the coefficients for the equation")
print('ax^2 + bx + c = 0')
a = float(input("a = "))
b = float(input("b = "))
c = int(input("c = "))

D = b**2 - 4 * a * c
print(D)

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(x1,x2)
elif D==0:
    x = -b / (2 * a)
    print(x)
else:
    print("no roots here mate")