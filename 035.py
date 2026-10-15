# Problem 035: Check if a given character is an alphabet, digit, or special character

ch = input("Enter a character: ")

if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
    print("Alphabet")
elif ch >= '0' and ch <= '9':
    print("Digit")
else:
    print("Special character")
