# Problem 030: Build a simple calculator (+, −, ×, ÷) using switch-case

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

# match-case is Python's version of switch-case (Python 3.10+)
match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Cannot divide by zero")
    case _:
        print("Invalid operator")
