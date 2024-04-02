"""
We start with two intial approximations a and b, such that f(a)*f(b)<0, i.e. the root lies between 
a and b. Then for every iteration mid is calculated as (a+b)/2, then:
1. f(mid) = 0, then stop and mid is root.
2. f(a)*f(mid)<0 then for next iteration b=mid, bisecting the interval
3. f(b)*f(mid)<0 then for next iteration a=mid, bisecting the interval again

If tolerance |a-b|<e, then number of steps: 
n = {log(a-b) - log(e)}/log(2)

Pros: Only 1 fn evaluation per iter, Cons: Needs large no. of steps. So if fn evaluation is easy, 
this is a very good choice.
"""

def f(x: float) -> float:
    return (x**3 -4*x - 9)

a: float = 0.0
b: float = 0.0
mid: float = 0.0

while True:
    a = float(input("Enter starting of search interval: "))
    b = float(input("Enter ending of search interval: "))

    if f(a) * f(b) > 0:
        print("Intial approximations not suitable, retry!")

    else:
        break

e: float = float(input("Enter tolerance: "))

while abs(a-b) > e:
    mid = (a+b)/2
    if f(a) * f(mid) < 0:
        b = mid
    else:
        a = mid

print(f"Approximate root is: {mid}")