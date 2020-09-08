"""
every value assignment(var=100) is passs by reference in python

"""


def f1(var1):
    var1.append(100)


l2 = [22, 33, 44, 11, 66]

f1(l2)

print(l2)

# how to clone a list ?
# l2=l1[:]
"""
mutable
    list, dict, set


unordered data types: dict, set

immmutable
    int, float, str, tuple"""

# 12341234 11234 12341234ab


def f1():
    return 2


def f2():
    return [1, 2]

# if no brackets ...then it means tuple


def f3():
    return 1, 2


def f4():
    return "123123"


var2 = f3()
print(var2)
print(type(var2))

name, age = f3()
