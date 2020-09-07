def string_palindrom(string):
    if (string == string[::-1]):
        return True
    else:
        return False


string = input("enter the string:")
result = string_palindrom(string)
if result:
    print("string is a palindrom")
else:
    print("string is not a palindrom")
