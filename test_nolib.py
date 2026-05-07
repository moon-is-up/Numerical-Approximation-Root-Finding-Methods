import math
import time

def f(x):
    return math.cos(x)

def df(x, h=1e-8):
    # fwd approx.
    # return (f(x+h)-f(x))/h
    # bwd approx.
    # return (f(x)-f(x-h))/h
    # cntr approx.
    return (f(x+0.5*h)-f(x-0.5*h))/h

def bisection(a, b, tol=1e-6, max_iter=20):
    start = time.time()
    print("\nBisection Method Table:\n")

    print(f"{'n':<3} {'a_n':<12} {'b_n':<12} {'p_n':<12} {'f(p_n)':<12} {'(b-a)/n':<12}")
    print("-"*65)

    for n in range(1, max_iter + 1):
        if f(a)*f(b) >= 0:
            print(f"Bisection method fails: No root in the interval [{min(a,b)}, {max(a,b)}]")
            return 0, 0, 0
        p = (a + b) / 2
        fp = f(p)

        print(f"{n:<3} {a:<12.6f} {b:<12.6f} {p:<12.6f} {fp:<12.6f} {(b-a)/n:<12.6f}")

        if abs(fp) < tol:
            break

        if f(a) * fp < 0:
            b = p
        else:
            a = p
    end = time.time()
    return p, fp, end-start

def newton(x0, tol=1e-6, max_iter=20):
    start = time.time()
    print("\nNewton Method Table:\n")

    print(f"{'n':<3} {'x_n':<12} {'f(x_n)':<12} {'f\'(x_n)':<12} {'x_n+1':<12}")
    print("-"*60)

    for n in range(1, max_iter + 1):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            print(f"Newton-Raphson method fails: The derivative df({x0}) = 0")
            return 0, 0, 0
        x1 = x0 - fx / dfx

        print(f"{n:<3} {x0:<12.6f} {fx:<12.6f} {dfx:<12.6f} {x1:<12.6f}")

        if abs(x1 - x0) < tol:
            break

        x0 = x1
    end = time.time()
    return x1, f(x1), end-start

def secant(x0, x1, tol=1e-6, max_iter=20):
    start = time.time()
    print("\nSecant Method Table:\n")

    print(f"{'n':<3} {'x_n-1':<12} {'x_n':<12} {'f(x_n-1)':<12} {'f(x_n)':<12} {'x_n+1':<12}")
    print("-"*75)

    for n in range(1, max_iter + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)

        print(f"{n:<3} {x0:<12.6f} {x1:<12.6f} {fx0:<12.6f} {fx1:<12.6f} {x2:<12.6f}")

        if abs(x2 - x1) < tol:
            break

        x0 = x1
        x1 = x2
    end = time.time()
    return x2, f(x2), end-start


a, b = input("Enter the comma-separated interval (i.e. a,b for [a,b]): ").split(',')
a, b = int(a), int(b)
print(f"Newton's method will use {(a+b)/2} as the initial point\n")
root_bis, f_bis, time_bis = bisection(a, b)
root_new, f_new, time_new = newton((a+b)/2)
root_sec, f_sec, time_sec = secant(a, b)

print("\nRoots:")
print(f"Bisection: x = {root_bis:.12f} f(x) = {f_bis:.12f}")
print(f"Newton:    x = {root_new:.12f} f(x) = {f_new:.12f}")
print(f"Secant:    x = {root_sec:.12f} f(x) = {f_sec:.12f}")

print("\nTime:")
print(f"Bisection: {time_bis:.6f}")
print(f"Newton: {time_new:.6f}")
print(f"Secant: {time_sec:.6f}")