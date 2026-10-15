# Problem 072: Convert binary to decimal

binary = input("Enter a binary number: ")
decimal = 0
power = 0

for digit in reversed(binary):
    if digit == "1":
        decimal = decimal + 2 ** power
    power = power + 1

print("Decimal:", decimal)
