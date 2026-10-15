# Problem 064: Compute: 1! + 2! + 3! + ... + N!

n = int(input("Enter N: "))
total = 0
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    total = total + fact

print("1! + 2! + ... + N! =", total)
