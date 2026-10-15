# Problem 068: Find the largest and smallest digit in a number

n = abs(int(input("Enter a number: ")))
largest = 0
smallest = 9

if n == 0:
    smallest = 0

while n > 0:
    digit = n % 10
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    n = n // 10

print("Largest digit:", largest)
print("Smallest digit:", smallest)
