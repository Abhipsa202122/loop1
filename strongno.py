###Strong number-:
num=int(input("enter any number"))
temp=num
sum=0
rem=0
while num>0:
	fact=1
	i=1
	rem=num%10
	while i<=rem:
		fact=fact*i
		i=i+1
	sum=sum+fact
	num=num//10
if sum==temp:
	print(temp,"is a strong number")
else:
	print(temp,"is not a strong number")