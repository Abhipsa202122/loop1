''' Write a program to print the following series till n terms.
1 4 9 16 25 _ _ _ _ _ n terms.

Hide Answer
Ans. '''

n = int(input("Enter value of n : "))
i = 1
while(i <= n):
    print(i**2, end = " , ")
    i = i + 1

'''OUTPUT : 

Enter value of n : 5
1 , 4 , 9 , 16 , 25 ,'''