# Problem 037: Given coordinates (x, y), determine which quadrant the point lies in

x = float(input("Enter x: "))
y = float(input("Enter y: "))

if x > 0 and y > 0:
    print("First quadrant")
elif x < 0 and y > 0:
    print("Second quadrant")
elif x < 0 and y < 0:
    print("Third quadrant")
elif x > 0 and y < 0:
    print("Fourth quadrant")
elif x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On the Y-axis")
else:
    print("On the X-axis")
