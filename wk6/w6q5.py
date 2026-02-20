month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month == 2:
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(29)
    else:
        print(28)
elif 1 <= month <= 12:
    print(days[month - 1])
else:
    print("Invalid month")
