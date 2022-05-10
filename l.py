# a={2:3,3:5,6:6}
# b=sorted((a))
# dic={}
# i=0
# while i<len(b):
#     #if b[i]==2:
#     d={2:3}
#     dic.update(d)
        
#     i+=1
# print(dic)
l=[[1,2],[2,3][6,7]]
i=0
s=0
while i<len(l):
    j=0
    if type(l[i])==type([]):
       s+=l[i][j]
       j+=1
    i+=1
print(s)        