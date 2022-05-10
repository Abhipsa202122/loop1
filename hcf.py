#Write a program to find the HCF of two numbers entered from the user.

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
rem = 1
if num1 > num2 :
   while rem!=0:
     rem = num1 % num2
     if rem == 0:
         hcf = num2
     else:
         num1 = num2
         num2 = rem
else :
   while rem!=0:
     rem = num2 % num1
     if rem == 0:
         hcf = num1
     else:
         num2 = num1
         num1 = rem
print("HCF of two numbers is  : ", hcf)

'''OUTPUT : 

Enter first number: 2
Enter second number: 8'''
