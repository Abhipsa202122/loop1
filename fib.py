'''n=int(input("enter no"))
a=0
b=1
c=0
while c<=n:
    print(c)
    a=b
    b=c
    c=a+b
    #r=b
    #while r<=c:
        #j=1
        #while j<=r:
        #print(r,end="")
    #print( )
    #r+=1  '''  
'''r=1
while r<=5:
	c=1
	while c<=r:
		print(c,end=' ')
		c+=1
	print( )
	r+=1 '''              
'''from collections import defaultdict
def len():
    a=input("enter a sentence")
    d=defaultdict(set)
    for i in a.split():
        d[len(i)].add(i)
    return {key:list(value) for key,value in d.item()}
print(len())'''
a="my name"
d=dict()
b=a.split()
j=0
while j<len(b):
    d[b[j]]=len(b[j])
    i=0
    c=0
    while i<len(a):
        if a[i]==" ":
            c=c+1
        i=i+1
    j=j+1
d["space"]=c
print(d)
