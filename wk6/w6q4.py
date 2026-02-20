month = int(input("Enter month (1-12): "))
if month >= 1 and month <= 12:
    year = int(input("Enter year: "))
    if year >= 0:
        m = [1, 3, 5, 7, 8, 10, 12]
        if month in m:
            print("31 days")

        elif month == 2:
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                print("29 days")
            else:
                print("28 days")
        else:
            print("30 days")
    else:
        ("Not a valid year")
else:
    print("Not a valid month")
