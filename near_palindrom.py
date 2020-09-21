# PF-Assgn-46

def nearest_palindrome(number):
    while(number > 0):
        if(str(number) == (str(number))[::-1]):
            return number
        number += 1


number = 12331
print(nearest_palindrome(number))
