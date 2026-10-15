# Problem 042: Scholarship Eligibility : Determine eligibility based on marks, attendance, and family income.

# Rules used: marks >= 85, attendance >= 75%, family income <= 3,00,000
marks = float(input("Enter marks (%): "))
attendance = float(input("Enter attendance (%): "))
income = float(input("Enter yearly family income: "))

if marks >= 85 and attendance >= 75 and income <= 300000:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")
    if marks < 85:
        print("- Marks are below 85")
    if attendance < 75:
        print("- Attendance is below 75%")
    if income > 300000:
        print("- Family income is above 3,00,000")
