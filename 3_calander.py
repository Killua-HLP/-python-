import calendar

try:
    year = int(input("Enter the Year: "))
    if year <= 0:
        print("Invalid Year!")
    else:
        month = int(input("Enter the Month: "))
        if not 1 <= month <= 12:
            print("Invalid Month!")
        else:
            cal = calendar.month(year, month)
            print(cal)
except ValueError:
    print("Please enter numbers only.")

