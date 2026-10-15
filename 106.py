# Problem 106: Zigzag pattern

width = int(input("Enter width: "))

for row in range(3):
    for col in range(width):
        if row == 0 and col % 4 == 0:
            print("*", end="")
        elif row == 1 and col % 2 == 1:
            print("*", end="")
        elif row == 2 and col % 4 == 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
