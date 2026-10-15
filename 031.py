# Problem 031: Read month number (1–12) and print number of days in that month

month = int(input("Enter month number (1-12): "))

match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print("31 days")
    case 4 | 6 | 9 | 11:
        print("30 days")
    case 2:
        print("28 days (29 in a leap year)")
    case _:
        print("Invalid month number")
