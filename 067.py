# Problem 067: Check if a number is an Armstrong number (generalized for any digits)

n = int(input("Enter a number: "))
original = n
digits = len(str(n))
total = 0

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if total == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")
