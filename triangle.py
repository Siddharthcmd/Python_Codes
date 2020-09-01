# Write a python function to check whether three given numbers can form the sides of a triangle.


def form_triangle(num1, num2, num3):
    # Do not change the messages provided below
    success = "Triangle can be formed"
    failure = "Triangle can't be formed"
    if (num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1):
        return success
    else:
        return failure


# Provide different values for the variables, num1, num2, num3 and test your program
num1 = 3
num2 = 3
num3 = 3
x = num1 ** 3
print(x)
print(form_triangle(num1, num2, num3))
