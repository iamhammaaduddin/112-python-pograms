# Problem 074: Find the sum of a series: x − x³/3! + x⁵/5! − x⁷/7! ... (sin series)

x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0
sign = 1

for i in range(n):
    power = 2 * i + 1
    fact = 1
    for j in range(1, power + 1):
        fact = fact * j
    total = total + sign * (x ** power) / fact
    sign = -sign

print("Sum of the series:", total)
