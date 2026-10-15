# Problem 010: Check if a character is uppercase, lowercase, digit, or special character

ch = input("Enter a single character: ")

if ch >= 'A' and ch <= 'Z':
    print("Uppercase letter")
elif ch >= 'a' and ch <= 'z':
    print("Lowercase letter")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")
