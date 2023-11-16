#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
list1 = [3, 1, 2]   # Create a list
print(list1)
print(list1[2])
print(list1[-1])    
list1[2] = 'hello'    
print(list1)        
list1.append('powenko') 
print(list1)          
x =list1.pop()    
print(list1)
print(x) 
list1.remove('hello' )    
print(list1)
list1 = list1 * 2
print(list1)
list1=list1 + [4,5,6]
print(list1)
list1.extend([7,8])
print(list1)
list1.insert(2,3)
print(list1)
list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.count(1))
print(len(list1))
print( 1 in list1)