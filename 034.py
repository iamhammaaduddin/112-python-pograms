# Problem 034: Find the roots of a quadratic equation (check discriminant: real, equal, imaginary)

import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a == 0:
    print("Not a quadratic equation (a cannot be 0)")
else:
    d = b * b - 4 * a * c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        print("Roots are real and different:", root1, root2)
    elif d == 0:
        root = -b / (2 * a)
        print("Roots are real and equal:", root)
    else:
        real = -b / (2 * a)
        imag = math.sqrt(-d) / (2 * a)
        print("Roots are imaginary:")
        print(real, "+", imag, "i")
        print(real, "-", imag, "i")
