'''Write a program to enter the numbers till the user enter ZERO and at the end it should display the count of positive and negative numbers entered.

Hide Answer
Ans. '''

ch = 'Y'
sump = 0
sumn = 0
num=1
while (num!=0):
     num = int(input("Enter any number  : "))
     if num > 0 :
       sump = sump + num
     else:
       sumn = sumn + num
print("Sum of all the positive numbers is  : ", sump)
print("Sum of all the negative numbers is  : ", sumn)

'''OUTPUT : 

Enter any number  : 5
Enter any number  : -5
Enter any number  : 3
Enter any number  : -3
Enter any number  : 4
Enter any number  : -4
Enter any number  : 0
Sum of all the positive numbers is  :  12
Sum of all the negative numbers is  :  -12'''

