a=int(input('enter no'))
#a=str(n)
for i in a:
    j=i
    while i>=0:
        a=i%10
        if a==0:
           print("zero")
        elif a==1:
           print("one")
        elif a==2:
           print("two")
        elif a==3:
           print("three")
        elif a==4:
           print("four")
        elif a==5:
           print("five")
        elif a==6:
           print("six")
        elif a==7:
           print("seven")
        elif a==8:
           print("eight")
        elif a==9:
           print("nine")
        i=i//10           
        