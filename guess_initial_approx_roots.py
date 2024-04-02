"""
if f(x) is a continuous function and f(a)*f(b) < 0 then a root lies in (a,b) if a<b or vice-versa
"""

def f(x: float) -> float:
    return (2**x - x - 3)

xmin: float = float(input("Enter xmin: "))
xmax: float = float(input("Enter xmax: "))
dx: float = float(input("Enter step size: "))

x: float = xmin

print("The tabulated function points are: ")
while x<=xmax:
    y = f(x)
    print(f"x: {x}, f(x): {y}")
    x = x+dx
