# Problem 073: Read numbers until user enters −1, print the count and average

count = 0
total = 0

num = int(input("Enter a number (-1 to stop): "))
while num != -1:
    count = count + 1
    total = total + num
    num = int(input("Enter a number (-1 to stop): "))

if count > 0:
    print("Count:", count)
    print("Average:", total / count)
else:
    print("No numbers were entered")
