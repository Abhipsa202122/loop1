'''Write a program to find the sum of following series:
1 + 2 + 6 + 24 + 120 . . . . . n terms

Hide Answer
Ans. '''

n = int(input("Enter number of terms  : "))
s = 0
pr = 1
i = 1
while(i<=n) :
    pr = i * pr
    print(pr, end = " + ")
    s = s + pr
    i = i + 1
print(" = ", s)

'''OUTPUT : 

Enter number of terms  : 5
1 + 2 + 6 + 24 + 120 +  =  153'''
