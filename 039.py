# Problem 039: Given hours worked and rate, compute salary with overtime (>40 hrs at 1.5× rate)

hours = float(input("Enter hours worked: "))
rate = float(input("Enter rate per hour: "))

if hours <= 40:
    salary = hours * rate
else:
    overtime = hours - 40
    salary = 40 * rate + overtime * rate * 1.5

print("Salary:", salary)
