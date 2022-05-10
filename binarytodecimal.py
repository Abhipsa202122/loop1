'''Write a program to convert Decimal to Binary.

Hide Answer
Ans.''' 

num = int(input("Enter a positive number: ")) 
bin = 0 
p = 1 
n = num
while n>0:     
     rem = int(n % 2)     
     bin = bin + rem * p
     p = p*10     
     n = n/2 
print("Binary number of",num,"is",bin)

'''OUTPUT : 

Enter a positive number: 15
Binary number of 15 is 1111'''