#Write a program to find the sum of the digits of a number accepted from the user.
a=int(input("enter no"))
s=0
while a>0:
    s=s+a%10
    a=a//10
print("sum of digit=",s)
#product:    
a=int(input("enter no"))
p=1
while a>0:
    p=p*a%10
    a=a//10
print("product of digit=",p)    