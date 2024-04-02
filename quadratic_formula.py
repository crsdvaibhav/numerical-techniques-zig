import math

print("Input A,B and C according to: Ax^2 + Bx + C\n")
a: float = float(input("Enter A: "))
b: float = float(input("Enter B: "))
c: float = float(input("Enter C: "))

d: float = b**2 - 4*a*c

if d>=0:
    x1: float = (-b + math.sqrt(d))/ (2*a)
    x2: float = (-b - math.sqrt(d))/ (2*a)
    print(f"The roots are: {x1} and {x2}\n")
else:
    x: float = (-b)/(2*a)
    y: float = math.sqrt(abs(d)) / (2*a)
    print(f"The roots are: {x} (+/-) {y}i\n")