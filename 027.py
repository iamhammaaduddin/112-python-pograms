# Problem 027: Calculate electricity bill based on slab rates

# Slab rates used:
# First 100 units      -> Rs. 1.50 per unit
# Next 100 units       -> Rs. 2.50 per unit
# Next 100 units       -> Rs. 4.00 per unit
# Above 300 units      -> Rs. 6.00 per unit
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1.5
elif units <= 200:
    bill = 100 * 1.5 + (units - 100) * 2.5
elif units <= 300:
    bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
else:
    bill = 100 * 1.5 + 100 * 2.5 + 100 * 4 + (units - 300) * 6

print("Electricity bill: Rs.", bill)
