# Problem 001: Read two numbers and print their sum, difference, product, quotient, and remainder

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
if b != 0:
    print("Quotient:", a / b)
    print("Remainder:", a % b)
else:
    print("Cannot divide by zero")
