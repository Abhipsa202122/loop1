i=1
#s=0
while i<=100:
    c=0
    j=1
    while j<i:
        if i%j==0:
           c=c+j
        j+=1
    if c==i:
       #l.append(i)
       #s+=i
       #print(l)
       print(i)
    i+=1   

    


   

