# Problem 052: Happy Number: Repeatedly replace a number with the sum of the squares of its digits. Determine whether it eventually reaches 1.

def sum_of_squares(num):
    total = 0
    while num > 0:
        digit = num % 10
        total = total + digit * digit
        num = num // 10
    return total


n = int(input("Enter a number: "))
seen = []

# Keep replacing the number; stop at 1 or if a number repeats (loop)
while n != 1 and n not in seen:
    seen.append(n)
    n = sum_of_squares(n)

if n == 1:
    print("Happy number")
else:
    print("Not a happy number")
