# Problem 090: Floyd's triangle

n = int(input("Enter number of rows: "))

# Floyd's triangle (numbers are aligned in columns)
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(str(num).rjust(3), end=" ")
        num = num + 1
    print()
