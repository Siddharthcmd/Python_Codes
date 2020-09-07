'''
Write a Python function to find all the Strong numbers in a given list of numbers.
Write another function to find and return the factorial of a number. Use it to solve the problem.

Example:
A number is considered to be a Strong number if sum of the factorial of its digits is equal to the number itself.
145 is a Strong number as 1! + 4! + 5! = 145.

Sample Input	Expected Output
num_list = [145, 375, 0, 100, 2][145, 2]
'''


def factorial(number):

    return 1 if (int(number) == 0 or int(number) == 1) else int(number) * factorial(int(number) - 1)


def find_strong_numbers(num_list):
    str_num_list = []
    for num in num_list:
        sum = 0
        for digit in str(num):
            sum += factorial(digit)
        if sum == num:
            str_num_list.append(num)
    return str_num_list


num_list = [145, 0, 0, 1, 375, 100, 2, 10]
factorial(4)
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)
