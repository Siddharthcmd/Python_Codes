def leap_year(year):
    return [index for index in range(year, year + 60) if(index % 4 == 0 or index % 400 == 0 and index % 100 == 0)]

# program logic
# if year % 100 == 0:
#    if year % 400 == 0:
#        return True
# elif year % 4 == 0:
#    return True
# return False


print(leap_year(2100))
