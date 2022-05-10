'''Write a program to find the sum of following series
1 + 8 + 27 …………n terms

Hide Answer
Ans.''' 

n = int(input("Enter number of terms : "))
s = 0
i = 1
while(i <= n):
   s = s + i ** 3
   i = i + 1
print(s)


'''OUTPUT:

Enter number of terms  : 4
100'''