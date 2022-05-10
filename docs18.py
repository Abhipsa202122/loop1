'''n=int(input("Enter no")) 
bin=0 
p=1
i=0 
while n!=0:     
     r=(n % 10)     
     bin=bin+r*p(2,i)
     #p=p*10     
     n=n/10
     i+=0 
print("Binary no is",bin)'''
'''bin=int(input("enter no"))
dec=0
#i=0
p=0
for i in reversed(bin):
    dec=dec+int(i)*pow(2,p)
    #u=int(u/10)
    p+=1'''
bin=int(input("enter no"))
d=0
s=0
i=1
while i<=len(bin):
     s+bin[i]*2**i
     i+=1
print("decimal",s)        
