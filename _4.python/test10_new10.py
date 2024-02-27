import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

list1 = [1, 2, 3, 4, 5, 6, 7]
# 找最小、最大元素
print(min(list1), max(list1))
# 串列長度、串列加總
print(len(list1), sum(list1))

s0 = slice(0, 2)                 # 切片物件：定義切片範圍
s1 = slice(1, -1, 2)
print(list1[s0], list1[s1])      # list1直接帶入切片範圍
# 結果：([1, 2], [2, 4, 6])

print("------------------------------------------------------------")  # 60個

fset = frozenset(['a', 'b', 'c'])
print(fset)           # frozenset({'a', 'b', 'c'})

#fset.remove('a')      # 不能修改，AttributeError
# frozenset根本沒有remove()可用！

print("------------------------------------------------------------")  # 60個

keys = ('name', 'age', 'job')
values = ('Amy', 25, 'writer')
dic1 = dict(zip(keys, values))      # zip真好用！
print(dic1)
# {'name': 'Amy', 'age': 25, 'job': 'writer'}


print("------------------------------------------------------------")  # 60個

names = ['Amy', 'Bob', 'Cathy']
scores = [70, 92, 85]
list1 = list(enumerate(zip(names, scores)))
# [(0, ('Amy', 70)), (1, ('Bob', 92)), (2, ('Cathy', 85))]
for item in list1:
    print(item[0], item[1][0], item[1][1])


print(list(zip(('a', 'b', 'c'), (30, 41, 52))))
# [('a', 30), ('b', 41), ('c', 52)]


print(list(enumerate(['a', 'b', 'c'])))  
# [(0, 'a'), (1, 'b'), (2, 'c')]
    
print("------------------------------------------------------------")  # 60個

list1 = [30, 45, 1024, 2500, 699, 126]

# 過濾出小於1000元的消費
list2 = [num for num in list1 if num<1000]
sum1 = sum(list2)        # 用sum做消費加總
avg1 = sum1/len(list2)   # 用len取消費筆數

print(sum1)
print(avg1)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
