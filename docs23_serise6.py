'''Write a program to find the sum of following series :
x + x2/2 + ……….xn/n

Hide Answer
Ans. '''

n = int(input("enter a nth term = "))
x = int(input("Enter value of x : "))
sum = 0
i = 1
while(i<=n):
    sum = sum + 2**i/i
    i = i + 1
print(round(sum,2))

'''OUTPUT :

enter a nth term = 3
Enter value of x : 2
6.67'''