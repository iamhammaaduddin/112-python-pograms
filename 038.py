# Problem 038: Check if a 3-digit number is an Armstrong number (e.g., 153)

n = int(input("Enter a 3-digit number: "))

if n < 100 or n > 999:
    print("Please enter a 3-digit number")
else:
    original = n
    d1 = n % 10
    d2 = (n // 10) % 10
    d3 = n // 100
    total = d1 ** 3 + d2 ** 3 + d3 ** 3
    if total == original:
        print(original, "is an Armstrong number")
    else:
        print(original, "is not an Armstrong number")
