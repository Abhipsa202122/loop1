#a=[10,20,[30,40,[50,60,[70,80]]]]
#o/p:[10,20,30,40,50,60,70,80]
# b=[30,40]
# c=[50,60]
# d=[70,80]
# l=b+c+d
# l1=[]
# i=0
# while i<len(l):
#       if i in l1: 
#          l1.append(i)
#       i+=1
# print(l1)      
a=[[10,[25],36]],[11],[12,[13],14]
b=[]
i=0
s=0
while i<(len(a)):
       if type(a[i])==list:
              j=0
              while j<len(a[i]):
                     if type(a[i][j])==list:
                           k=0
                           while k<len(a[i][j]):
                                 if type(a[i][j][k])==list:
                                        l=0
                                        while l<len(a[i][j][k]):
                                               b.append(a[i][j][k][l])
                                               l+=1
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
                                       
                                       
                                        

