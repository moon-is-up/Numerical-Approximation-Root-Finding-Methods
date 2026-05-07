import pandas as pd
import math
import time

def f(x):   # the function
    return math.sin(x)

def dfx(x, h=1e-8):  # derivative for Newton
    return (f(x+0.5*h)-f(x-0.5*h))/h

def bisection(a, b, tol=1e-6, max_iter=30):
    start = time.time()
    data = []
    for i in range(1, max_iter+1):
        fa = f(a)
        fb = f(b)
        if fa*fb >= 0:
            print(f"Bisection method fails: No root in the interval [{min(a,b)}, {max(a,b)}]")
            return 0, 0, 0
        c = (a + b) / 2
        fc = f(c)
        data.append([a, fa, b, fb, c, fc, (b-a)/2])
        if abs(fc) < tol or abs((b-a)/2) < tol:
            break
        elif fc*fa < 0:
            b = c
        else:
            a = c
    df = pd.DataFrame(data, columns = ["a", "f(a)", "b", "f(b)", "c", "f(c)", "(b-a)/2"])
    print("\n\nBisection method:")
    print(df)
    end = time.time()
    return c, f(c), end-start


def newtons(x0, tol=1e-6, max_iter=20):
    start = time.time()
    data = []
    for i in range(1, max_iter+1):
        fx = f(x0)
        df = dfx(x0)
        if df == 0:
            print(f"Newton-Raphson method fails: The derivative df({x0}) = 0")
            return 0, 0, 0
        x1 = x0 - fx / df
        fx1 = f(x1)
        data.append([x0, fx, df, x1, fx1, abs(x1-x0)])
        if abs(fx1) < tol or abs(x1-x0) < tol:
            break
        x0 = x1

    df = pd.DataFrame(data, columns = ["x_n", "f(x_n)", "f'(x_n)", "x_n+1", "f(x_n+1)", "|x_n+1 - x_n|"])
    print("\n\nNewton-Raphson method:")
    print(df)
    end = time.time()
    return x1, f(x1), end - start

def secant(x0, x1, tol=1e-6, max_iter=20):
    start = time.time()
    data = []
    for i in range(1, max_iter+1):
        fx0 = f(x0)
        fx1 = f(x1)

        x2 = x1 - fx1 * ((x1 - x0)/(fx1 - fx0))
        fx2 = f(x2)
        data.append([x0, fx0, x1, fx1, x2, fx2, abs(x2-x1)])
        if abs(fx2) < tol or abs(x2-x1) < tol:
            break
        x0 = x1
        x1 = x2
        
    df = pd.DataFrame(data, columns = ["x_n-1", "f(x_n-1)", "x_n", "f(x_n)", "x_n+1", "f(x_n+1)", "|x_n+1 - x_n|"])
    print("\n\nSecant method:")
    print(df)
    end = time.time()
    return x2, f(x2), end - start

a, b = input("Enter the comma-separated interval (i.e. a,b for [a,b]): ").split(',')
a, b = int(a), int(b)
print(f"Newton's method will use {(a+b)/2} as the initial point\n")
root_bis, f_bis, time_bis = bisection(a, b)
root_new, f_new, time_new = newtons((a+b)/2)
root_sec, f_sec, time_sec = secant(a, b)

print("\nRoots:")
print(f"Bisection: x = {root_bis:.12f} f(x) = {f_bis:.12f}")
print(f"Newton:    x = {root_new:.12f} f(x) = {f_new:.12f}")
print(f"Secant:    x = {root_sec:.12f} f(x) = {f_sec:.12f}")

print("\nTime:")
print(f"Bisection: {time_bis:.6f}")
print(f"Newton: {time_new:.6f}")
print(f"Secant: {time_sec:.6f}")