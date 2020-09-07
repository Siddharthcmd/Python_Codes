# Write a Python program to find the sum of digits of a given number. E.g. Sum of number 123 will be 6
def find_sum_of_digits(number):

    return sum(int(digit) for digit in str(number))


num = input("enter the number:")
sum_of_digits = find_sum_of_digits(num)
print("Sum of digits:", sum_of_digits)
