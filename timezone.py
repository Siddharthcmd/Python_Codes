import time
import datetime

# To get current GM time
print("Current GM time:", time.gmtime())
# This returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

# To get current local time
print("Current local time:", time.localtime())
# This also returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

# To extract today's date in a specified string format
print("Today's date using time module", time.strftime("%d/%m/%Y"))

# Python additionally allows use of  datetime module
# Prints today's date
print("Today's date using datetime module:", datetime.date.today())

# To extract today's date in a specified string format
print("Today's date (dd/mm/yyyy) using datetime module:",
      datetime.date.today().strftime("%d/%m/%Y"))


# To convert a date in string format to datetime value
print("Today's date (dd/mm/yyyy):",
      datetime.datetime.strptime("17/04/2016", "%d/%m/%Y"))
