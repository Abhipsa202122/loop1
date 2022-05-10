# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     my_array = list(arr)
#     print(max([x for x in my_array if x != max(my_array)]))
# #l=[2,3,6,6,5]
#m1=0
#m2=0
#i=0
#while i<len(l):
#    if l[i]>m1:
#        m2=m1
#        m1=l[i]
#     elif l[i]>m2:
#        if m1!=l[i]:
#           m2=l[i]
#     i+=1
#print("max",m2)    
        
    
    #l=[2,3,6,6,5]
#     m1=0
#     m2=0
#     i=0
#     while i<len(l):
#        if l[i]>m1:
#           m2=m1
#           m1=l[i]
#        elif l[i]>m2:
#           if m1!=l[i]:
#              m2=l[i]
#        i+=1
#     print("max",m2)
# def is_leap(year):
#     leap = False
#     if year%400==0:
#         leap=True
#     elif year%4==0 and year%100!=0:
#         leap=True
    
#     # Write your logic here
    
#     return leap        
        
# def solve(s):
#     str=''
#     if s.isalnum():
#         a=s.split(" ")
#         print(a)
#         for i in a:
#             str+=i.capitalize()
#     print(str)
# solve("abc")        
# import math
# import os
# import random
# import re
# import sys
 
# # Complete the solve function below.
# def solve(s):
#     for i in s.split():
#         s = s.replace(i,i.capitalize())
#     return s



# n = int(input('enter the number:'))
# student_marks = {}
# for i in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input('enter the name:')
# l= list(student_marks[query_name])
# no = len(l)
# print(no)
# s = sum(l)
# print(s)
# ss = s/no
# print(ss)
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
    query_name = input()
    marks=student_marks[query_name]
    #print(marks)
print(format(sum(marks)/3,"2f"))


