# Problem 102: Alphabet pyramid (centered)

n = int(input("Enter number of rows: "))

for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    for j in range(i - 1, -1, -1):
        print(chr(65 + j), end=" ")
    print()
