'''Write a program to enter the numbers till the user wants and at the end it should display the sum of all the numbers entered.

Hide Answer'''
#Ans. 

ch = 'Y'
sum = 0
while ch.upper() == 'Y':
     num = int(input("Enter any number  : "))
     sum = sum + num
     ch=input("Do you wish to continue(Y,N)?: ")    
print("Sum of all the numbers is  : ", sum)

'''OUTPUT : 

Enter any number  : 1
Do you wish to continue(Y,N)?: y
Enter any number  : 2
Do you wish to continue(Y,N)?: y
Enter any number  : 3
Do you wish to continue(Y,N)?: n
Sum of all the numbers is  :  6'''

