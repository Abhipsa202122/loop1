n = int(input("Enter any number"))
print("Factors are : ")
i = 1
while(i <= n):
   if n % i==0:
     print(i)
   u=i  
   if u%2==0:
      print("even",u)
   #else:
   #   print("odd",i)  
   i = i + 1
#print("even",u)