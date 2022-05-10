'''Write a program to convert Binary to Decimal.

Hide Answer
Ans.''' 

bin = input("Enter a binary number: ")
dec=0
p=0
for i in reversed(bin):
     dec = dec + int(i)*pow(2,p)
     p=p+1
print("Decimal number of binary",bin," number is : ",dec)

'''OUTPUT :

Enter a binary number: 1111
Decimal number of binary 1111 number is : 15'''