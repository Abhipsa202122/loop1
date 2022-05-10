i=1
s=0
while i<=100:
    c=0
    j=1
    while j<i:
        if i%j==0:
           c=c+j
        j+=1
    if c==i:
       s+=i
       print(i,"perfect no")
    i+=1
print(s)       