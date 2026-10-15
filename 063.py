# Problem 063: Find x^n (power) without using built-in pow function

x = float(input("Enter base (x): "))
n = int(input("Enter power (n): "))
result = 1

for i in range(abs(n)):
    result = result * x

if n < 0:
    result = 1 / result

print(x, "^", n, "=", result)
