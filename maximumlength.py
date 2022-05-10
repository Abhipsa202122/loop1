l=[1,3,5,8]
i=0
m=0
c=0
while i<len(l):
    if l[i]>m:
        m=l[i]
        c+=1
    i+=1
print(c,m)    