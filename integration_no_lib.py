# Numerical Integration Methods
import math

# Function
def f(x):
    return math.cos(x)


# Rectangular Method (Left Endpoint)
def rectangular(a, b, n):
    print("\nRectangular method")
    h = (b - a) / n
    total = 0

    for i in range(n):
        x = a + i * h
        print(f"f({x}) = {f(x)}")
        total += f(x)

    return h * total


# Trapezoidal Rule
def trapezoidal(a, b, n):
    print("\nTrapezoidal method")
    h = (b - a) / n

    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        print(f"f({x}) = {f(x)}")
        total += 2 * f(x)

    return (h / 2) * total


# Simpson's Rule
def simpson(a, b, n):
    print("\nSimpson's method")
    if n % 2 != 0:
        print("n must be even for Simpson's method. Adding 1 to n")
        n+=1

    h = (b - a) / n

    total = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        print(f"f({x}) = {f(x)}")

        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return (h / 3) * total


# Example
a = int(input("Enter the value of a (Lower bound): "))
b = int(input("Enter the value of b (Upper bound): "))
n = int(input("Enter the value of n (Number of intervals): "))

print("Rectangular =", rectangular(a, b, n))
print("Trapezoidal =", trapezoidal(a, b, n))
print("Simpson =", simpson(a, b, n))