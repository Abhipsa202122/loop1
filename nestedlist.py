a=[[10,[25],36]],[11],[12,[13],14]
i=0
l=[]
while i<(len(a)):
    if type(a[i])==list:
       j=0
       while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==list:
                        m=0
                        while m<len(a[i][j][k]):
                            if type(a[i][j][k][m])==list:
                               m+=1
                            else:
                                l.append(a[i][j][k][m])   
                            m+=1
                    else:
                        l.append(a[i][j][k])
                    k+=1
            else:
                l.append(a[i][j])
            j+=1
    else:
        l.append(a[i])
    i+=1
print(l)
                           