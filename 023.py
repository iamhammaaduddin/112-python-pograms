# Problem 023: Time Greeting : Given an hour, print Morning, Afternoon, Evening, or Night.

hour = int(input("Enter hour (0-23): "))

if hour >= 5 and hour <= 11:
    print("Morning")
elif hour >= 12 and hour <= 16:
    print("Afternoon")
elif hour >= 17 and hour <= 20:
    print("Evening")
elif hour >= 0 and hour <= 23:
    print("Night")
else:
    print("Invalid hour")
