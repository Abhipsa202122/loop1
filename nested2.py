a=[1,2,[3,4,[5,6]]]
#o/p:[1,2,3,4,5,6]         
b=[]
i=0

while i<(len(a)):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==list:
                       k+=1
                    else:
                        b.append(a[i][j][k])
                    k+=1
            else:
                b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i+=1
print(b)
#print(s)
                                       
                                       
                                        


                                       
                                       
                                        

