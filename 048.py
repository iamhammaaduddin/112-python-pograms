# Problem 048: Count the number of digits in a number

n = abs(int(input("Enter a number: ")))
count = 0

if n == 0:
    count = 1
while n > 0:
    count = count + 1
    n = n // 10

print("Number of digits:", count)
