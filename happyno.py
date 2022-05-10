n=int(input("enter a number"))
i=n
result=0
sum=0
while n>0:
	if n%10==0:
		sum=sum+i
		result=result+sum**2
		print( result)	
	n=n//10
if n==result:
	print("happy no.")
else:
	print("unhappy no.")