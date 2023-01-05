import calendar
import datetime

bday = datetime.date(1947, 5, 6)
today = datetime.date.today()

age = int((today - bday).days / 365.2425)

print("\nThe age of Shyam's Grandfather born on {0} as per {1} is {2} years".format(bday, today, age))

print("\nThe calendar of his birth month is : \n" + calendar.month(bday.year, bday.month))
print("\nThe calendar of his birth year is : \n" + calendar.calendar(bday.year))
