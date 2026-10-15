# Problem 104: Hollow diamond inside rectangle

n = int(input("Enter number of rows: "))

# Each row has 2 * n columns. The gap in the middle forms a diamond.
# Upper half
for i in range(n, 0, -1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)

# Lower half
for i in range(2, n + 1):
    print("* " * i + "  " * (n - i) * 2 + "* " * i)
