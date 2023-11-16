#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
list1 = [1,2,3,4]
print(list1)
print(list1*2)

i=0
for x in list1:
	list1[i]=list1[i]*2
	i=i+1
print(list1)
"""
for x in list1
   return x*2
"""
list1 = [1,2,3,4]
list1=[x*2 for x in list1]
print(list1)

list1 = [1,2,3,4]
list1=[x*2 for x in list1 if x % 2==0]
print(list1)

list1 = [1,2,3,4]
list1=[x for x in list1 if x>=3]
print(list1)

list1 = [59,60,70,80]
list1=[x**2 for x in list1 if x<60]
print(list1)


list1 = [20,30,50,80]
list1=[x for x in list1 if (x>=30 and x<=50)]
print(list1)   # 30,50
