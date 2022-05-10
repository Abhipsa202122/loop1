'''Write a program to add first n terms of the following series using a for loop:
1/1! + 1/2! + 1/3! + …….. + 1/n!'''
num = int(input("Enter any number  : "))
sum = 0
fact = 1
i = 1
while(i < num):
      fact= fact*i
      sum= sum + i/fact
      i = i + 1
print("Sum is       :    ",round(sum, 2))


'''OUTPUT : 

Enter any number  : 3
Sum is       :     2.0'''
print(1/10+1/9+1/8+1/7+1/6+1/5+1/4+1/3+1/2+1/1)
