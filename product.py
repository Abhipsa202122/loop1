#product:    
a=int(input("enter no"))
r=0
p=1
while a!=0:
    r=a%10
    p=p*r
    a=a//10
print("product of digit=",p)    