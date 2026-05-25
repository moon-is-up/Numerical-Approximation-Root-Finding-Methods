import math
import pandas as pd

def f(x):
    return math.cos(math.log(x**2 + 1)) * math.exp(-x**2)

def trapezoidal(a,b,n):
    print("\nTrapezoidal Method")
    data = []
    total = 0
    h = (b-a)/n
    for i in range(n+1):
        x = a + i*h
        if i == 0 or i == n:
            w = 1
        else:
            w == 2
        data.append([x, f(x), w])
        total += w*f(x)
    df = pd.DataFrame(data, columns=["x","f(x)","w"])
    print(df)
    return (h/2)  * total

def simpson(a,b,n):
    print("\nSimpson's Method")
    data = []
    total = 0
    if n%2 != 0:
        print("\nn must be even for Simpson's method. Adding 1 to n!")
        n += 1
    h = (b-a)/n
    for i in range(n+1):
        x = a + i*h
        if i == 0 or i == n:
            w = 1
        elif i % 2 == 0:
            w = 2
        else:
            w = 4
        data.append([x, f(x), w])
        total += w*f(x)
    df = pd.DataFrame(data, columns=["x","f(x)","w"])
    print(df)
    return (h/3) * total

a = int(input("Enter value of a (Lower bound): "))
b = int(input("Enter value of b (Upper bound): "))
n = int(input("Enter value of n (Number of intervals): "))
simp = simpson(a,b,n)
trap = trapezoidal(a,b,n)

print(f"Trapezoidal = {trap}")
print(f"Simpson's = {simp}")