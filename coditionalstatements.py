
age = 18

if age > 18:
    print("Eligible to vote")
elif age == 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")


## WAP to check if a number entered by the user is odd or even

num = float(input("Enter the number :"))

if  num % 2 == 0 :
    print("Given number is even")
else :
    print("Given number is odd")

### WAP to find the greatest of 3 numbers entered by the user

num1 = (float(input("Enter the number")))
num2 = (float(input("Enter the number")))
num3 = (float(input("Enter the number")))

if num1 > num2  and num1 > num3:
    print("The greatest number is :", num1)
elif num2 > num3:
    print("The greatest number is :", num2)
else : 
    print("The greatest number is :", num3)

## WAP to check if a number is multiple of 7 or not.

num1 = (float(input("Enter the number")))

if (num1 % 7 == 0) :
    print("The number is a multiple of 7")
else :
    print("The number is not a multiple of 7")