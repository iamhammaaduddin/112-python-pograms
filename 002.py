# Problem 002: Calculate the area of a circle given radius (A = πr²)

import math

r = float(input("Enter radius: "))
area = math.pi * r * r
print("Area of circle:", round(area, 2))
