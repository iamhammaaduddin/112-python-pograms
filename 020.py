# Problem 020: Check if a character is a vowel or consonant

ch = input("Enter a letter: ").lower()

if ch >= 'a' and ch <= 'z':
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
