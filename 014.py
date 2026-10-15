# Problem 014: Check if the Kth bit of a number is set or not

n = int(input("Enter a number: "))
k = int(input("Enter K (bit position, starting from 0): "))

if (n >> k) & 1:
    print("The", k, "th bit is SET")
else:
    print("The", k, "th bit is NOT set")
