#Write a program to find the sum of the following series(accept values of x and n from user)
#1 + x/1! + x2/2! + ……….xn/n!

#Hide Answer
#Ans. 

def fac(n):
    f = 1
    for i in range(1,n+1):
       f = f * i
    return(f)
sum = 1
n = int(input("Enter value of n : "))
x = int(input("Enter value of x : "))
i = 1
while(i < n):
    sum = sum + x**i/fac(i)
    i = i + 1
print(sum)

'''OUTPUT : 

Enter value of n : 5
Enter value of x : 3
16.375 '''