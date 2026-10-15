# Problem 029: Given 3 sides, check if a valid triangle can be formed

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

# Sum of any two sides must be greater than the third side
if a + b > c and b + c > a and a + c > b:
    print("A valid triangle can be formed")
else:
    print("A valid triangle cannot be formed")
