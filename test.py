import pandas as pd
import math
import time

def f(x):   # the function
    return math.cos(x)

def dfx(x, h=1e-8):  # derivative for Newton
    return (f(x+0.5*h)-f(x-0.5*h))/h

def bisection(a, b, tol=1e-6, max_iter=30):
    start = time.time()
    data = []
    for i in range(1, max_iter+1):
        fa = f(a)
        fb = f(b)

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


root_bis, f_bis, time_bis = bisection(1, 2)
root_new, f_new, time_new = newtons(1.5)
root_sec, f_sec, time_sec = secant(1, 2)

print("\nRoots:")
print(f"Bisection: x = {root_bis:.10f} f(x) = {f_bis:.10f}")
print(f"Newton:    x = {root_new:.10f} f(x) = {f_new:.10f}")
print(f"Secant:    x = {root_bis:.10f} f(x) = {f_bis:.10f}")

print("\nTime:")
print(f"Bisection: {time_bis:.6f}")
print(f"Newton: {time_new:.6f}")
print(f"Secant: {time_sec:.6f}")