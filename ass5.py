# This program will check weather the number is palindrom or not

number = input("Enter the number you want to check:")
temp=number
reverse=0
while(number!=0):
    remainder=number%10
    number=number/10
    reverse=reverse*10+remainder
if(temp==reverse):
    print("number is a palindrom")
else:
    print("number is not a palindrom")  
