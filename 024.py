# Problem 024: Login Validator : Check whether a username and password combination is valid.

# Stored (correct) login details
correct_username = "admin"
correct_password = "1234"

username = input("Enter username: ")
password = input("Enter password: ")

if username == correct_username and password == correct_password:
    print("Login successful")
else:
    print("Invalid username or password")
