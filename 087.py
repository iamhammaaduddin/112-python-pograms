# Problem 087: Sandglass / Hourglass

n = int(input("Enter number of rows: "))

# Upper half (inverted pyramid)
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Lower half (pyramid, skipping the middle row)
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
