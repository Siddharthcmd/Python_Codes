# PF-Exer-41
import math


# This verification is based on string match.

def sum_all(function, data):
    summ = 0
    for i in data:
        if function(i):
            summ += i
    return summ
list_of_nos = [25, 26, 27, 28, 29, 30, 147, 187]

greater = lambda x: x > 10

divide = lambda x: x % 10 == 0

range_of_values = lambda x: 25 <= x <= 50

# Use the below given print statements to display the output
# Also, do not modify them for verification to work
print(sum_all(greater, list_of_nos))
print(sum_all(divide, list_of_nos))
print(sum_all(range_of_values, list_of_nos))
