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





#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\02-List2.py

#!/usr/bin/env
__author__ = "Powen Ko, www.powenko.com"
list1 = [1,2,3,4]
print(list1)
list2 = [[1,2],[3,4]]
print(list2)
print(list2[1][1])
list3 = [1, "powen", 3.4]
print(list3)
list4 = ["apple", [8, 4, 6], ['p']]
print(list4)
print(list4[1][1])
list5 = [[1,2], [8, 4, 6], ["apple","banana"]]
print(list5)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\03-List3-Math.py

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

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\04-Slicing.py

list1=[0,1,2,3,4]
print(list1)
print (list1[2])
print (list1[2:4])
print (list1[2:])
print (list1[:2])
print (list1[:])
print (list1[:-1])
try:
  list1[2:4] = [8, 9] # python 3.x
except:
  list1[2] = 8  # python 2.x
  list1[3] = 9

print(list1)



print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\05-Dictionaries1.py

d = {'cat': 'cute',
     'dog': 'love'}
print(d['cat'])        
print('cat' in d)     
d['fish'] = 'wet'
print(d['fish'])        
print(d.get('monkey', 'N/A'))   
print(d.get('fish', 'N/A')) 
del(d['fish'])        
print(d.get('fish', 'N/A'))  



d = {'person': 2, 'cat': 4, 'spider': 8}
for animal in d:
    legs = d[animal]
    print('A %s has %d legs' % (animal, legs))


print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\06-set.py

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A - B)
#print(A + B)
print(A & B)
print(A | B)
print(A.union(B))
print(A.intersection(B))

print(A)
A.discard(2)
print(A)
A.remove(4)
print(A)
A.add(4)
print(A)
A.update([2,3,4])
print(A)

print('------------------------------------------------------------')	#60個

#檔案 : C:\_git\vcs\_4.python\__code\PythonTensorFlow人工智慧機器學習大數據_超炫專案與完全實戰\ch07\07-Tuples1.py

d = {(x, x + 1): x for x in range(10)}  
print(d)
t=(5,6)  
print(t)
print(type(t))  
print(d[t] )
print(d[(1, 2)])  

print('------------------------------------------------------------')	#60個

