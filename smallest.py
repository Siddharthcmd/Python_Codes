#This code will find the smallest number among the three number
num1 = input("enter the first number:")
num2 = input("enter the second number:")
num3 = input("enter the third number:")
print (num1,num2,num3)
if(num1 < num2):
    if(num1 < num3):
        print("smallest number is",num1)
    else:
        print("smallest number is",num3)
elif(num2<num3):
    print("smallest number is",num2)
else:
    print("smallest number is",num3)        
