# a="I am Abhipsa live in Navgurukul"
# d=dict()
# b=a.split()
# j=0
# while j<len(b):
#     d[b[j]]=len(b[j])
#     i=0
#     c=0
#     while i<len(a):
#         if a[i]==" ":
#             c=c+1
#         i=i+1
#     j=j+1
# d["space"]=c
# print(d)
# name=input('Enter name: ')
# position=input('What position in the list would you like to change: ')
# position=int(position)
# if -1 < position < 10:
#     name[position] = name
# else:
#     print('Invalid position entered')
# n=["abhi"]
# c=0
# i=0
# while i<len(n):
#     c+=1
#     print(c)
#     i+=1

# x = int(input("Enter a number: "))
# i = 1
# s=" "
# l=[]
# l1=[]
# while i<=10:
#     if i%2==0:
#         s=i
#         # l.append(i)
#         # print(s)
#     # elif i%2!=0:
#         # l1.append(i) 
#         # print(i)    
#     i = i + 1
# print(s)
# def f(str1,str2):  
#  # Convert string into lists  
#    list1 = list(str1)  
#    list2 = list(str2)  
#         # Sort the list value  
#    list1.sort()  
#    list2.sort()  
      
#    position = 0  
#    matches = True  
      
#    while position < len(str1) and matches:  
#       if list1[position]==list2[position]:  
#          position = position + 1  
#       else:  
#          matches = False  
      
#       return matches
# print(f('python','ythonp')) 
# n = int(input("num "))
# m = int(input("limit "))
# for i in range(1, m+1):
#     sum1 = 0
#     sum2 = 0
#     if i % n == 0:
#         sum1 += i
#     else:
#         sum2 += i
# print(f"{sum1} and {sum2}")
# print(abs(sum2-sum1))

# def f(r, unit, arr):
#   n = len(arr)
#   #We calculate the total amount of food that the rats can consume
#   sum = r * unit
#   sum_arr = 0
#   #We calculate the total amount in the households
#   for i in arr:
#     sum_arr = sum_arr + i
#   if len(arr) == 0:
#     return -1
#   elif sum > sum_arr:
#     return 0
#   #Where 1 represents that the household has surplus food for the rats 
#   elif sum < sum_arr:
#     return 1
# f()    


#task(7,2,[2, 8, 3, 5, 7, 4, 1, 2])
n = int(input("enter"))
arr = map(int,input().split())
print(arr)
#wordscorehackrank
 def is_vowel(letter):
        return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            #++score
            score=2
    return score   


   

