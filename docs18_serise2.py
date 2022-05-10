#Write a python program  to sum the sequence:
#1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!

#Hide Answer
#Ans. 

n = int(input("enter a nth term = "))
f = 1
s = 1
i=1
while(i<=n):
      f = f * i
      s = s + 1 / f
      i=i+1
print("sum of sequence = ", s)

'''OUTPUT :

enter a nth term = 5
sum of sequence =  2.7166666666666663'''