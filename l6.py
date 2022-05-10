# name=input("enter")
# for i in name:
#     print(name[i],(ord(i)))
# a=int(input("enter"))
# print(str(chr(a)))
i=1
a=int(input("enter 2nd number: "))
l=[]
while i<=10:
	#print(i,"*",j,"=",i*j)
    #l.append((i,"*",a,"=",i*a))
    #b=[a[i],a[i]+1]
    l.append((a[i],"*",i,"=",i*a[i]))
    i+=1
print(l)    