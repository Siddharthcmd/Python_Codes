'''
Write a python program that displays a message as follows for a given number:

If it is a multiple of three, display "Zip"
If it is a multiple of five, display "Zap".
If it is a multiple of both three and five, display "Zoom".
If it does not satisfy any of the above given conditions, display "Invalid".

'''

num = input("enter the number: ")
if(num % 3 == 0 and num % 5 == 0):
    print("zoom")
elif(num % 3 == 0):
    print("zip")
elif (num % 5 == 0):
    print("zap")
else:
    print("invalid entry")
