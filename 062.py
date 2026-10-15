# Problem 062: Compute: 1 − 2 + 3 − 4 + 5 − ... up to N terms

n = int(input("Enter number of terms: "))
total = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        total = total + i
    else:
        total = total - i

print("Sum:", total)
