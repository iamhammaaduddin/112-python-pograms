# Problem 084: Diamond shape

n = int(input("Enter number of rows: "))

# Upper half (pyramid)
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower half (inverted pyramid, skipping the middle row)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
