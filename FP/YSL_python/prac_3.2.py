def leap(year):
    if year % 400 == 0 and year % 100 == 0:
        return True

    elif year % 4 == 0 and year % 100 != 0:
        return True

    else:
        return False


yr = int(input("Enter the year : "))

frst = int(input("Enter the number for first day of specific year : "))

while frst < 1 or frst > 7:
    print("Invalid Input!")
    frst = int(input("Please enter the valid number for first day of specific year between 1 and 7 : "))

dys = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

mnths = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30, "July": 31,
         "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

if leap(yr):
    mnths["February"] = 29
