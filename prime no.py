#a=[27,60,98,3]
a=int(input("enter no"))
i=1
l=[]
s=0
while i<=a:
    j=1
    c=0
    while j<=i: 
       if i%j==0:
          c+=1
       j+=1
    if c==2:
       l.append(i)
       s=s+i
    i+=1       
print(l)
print(s)
      
'''a=int(input("enter no.")
i=1
c=0
l=[]
while i<=100:
    if a%i==0:
       c+=1
if c==2:  
   print(a,"is prime no")
else:
   print(a,"is not prime no")'''   
           