# Problem 055: Find factorial of N

n = int(input("Enter N: "))
fact = 1

for i in range(1, n + 1):
    fact = fact * i

print("Factorial of", n, "is", fact)
