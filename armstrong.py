l=[24,21,10,11,5,9]
#p=int(input("enter power"))
m=0
i=0
for i in l:
    j=i
    while 0<i:
        r=i%10
        m=r**len(str(i))**2
        i=i//10
        #i+=1
          #print(s)
if m==j:
    print(m,"armstrong no")
else:
    print(m,"not")        