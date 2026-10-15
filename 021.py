# Problem 021: Ticket Pricing : Calculate ticket price based on the customer's age.

# Pricing rules used:
# Below 5 years  -> Free
# 5 to 12 years  -> Rs. 100
# 13 to 59 years -> Rs. 200
# 60 and above   -> Rs. 150
age = int(input("Enter customer's age: "))

if age < 5:
    price = 0
elif age <= 12:
    price = 100
elif age < 60:
    price = 200
else:
    price = 150

print("Ticket price: Rs.", price)
