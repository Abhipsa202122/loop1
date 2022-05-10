s=0
i=1
while i<=100:
    a=1
    f=0
    while a<=i:
        if i%a==0:
           f+=1
        a+=1
    if f==2:
       s=s+i
       print(i,"is prime no") 
       #print(s)
    i+=1
#print(i,"is prime no")
print(s)            