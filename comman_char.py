'''
Write a python program to display all the common characters between two strings. Return - 1 
if there are no matching characters.

Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
'''
from collections import OrderedDict


def find_common_characters(msg1, msg2):
    msg1_set = ""  # .join(OrderedDict.fromkeys(msg1))
    msg2_set = ""  # .join(OrderedDict.fromkeys(msg1))
    for i in msg1:
        for j in msg2:
            if (i == j and i != " " and j != " "):
                msg1_set += str(i)
            else:
                msg2_set += str(j)
    return "".join(OrderedDict.fromkeys(msg1_set))


msg1 = "I like Python qrts"
msg2 = "Java is a very popular language qrst "
common_characters = find_common_characters(msg1, msg2)
print(common_characters)
