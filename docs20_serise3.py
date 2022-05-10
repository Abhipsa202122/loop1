'''Write a program to print the following series till n terms.
2 , 22 , 222 , 2222 _ _ _ _ _ n terms

Hide Answer
Ans. '''

n = int(input("Enter value of n  : "))
st = '2'
i = 0
while(i<n):
    print(st, end=" , ")
    st =st + '2'
    i = i + 1
