def lucky_number(number):
    if (sum(int(digits)
            for digits in str(sum(int(digit) for digit in str(number)))) == 9):
        return True
    else:
        return False


# number = input("enter the 4 digit number:")
# result = True
# result = lucky_number(number)
# if (result):
#   print("your number is lucky")
# else:
#   print("your number is not lucky")
