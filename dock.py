d=0
c=0
i=0
n=int(input("Please enter a number:"))
i=n
while i>0: 
    d=i%10 
    if d==0:     
       c=1
       #break  
    i=i//10
if c==1:
    print(n,"is duck number")
else:
    print(n,"not a duck number")