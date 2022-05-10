#magic num
n=int(input("enter num"))
a=n
while a>9:
	sum=0
	while a!=0:
		rem=a%10
		sum=sum+rem
		a=int (a//10 )
	a=sum
if sum==1:
	print(n,"magic num")
else:
	print(n,"not magic num")