# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:38:38 2018

@author: changguozhen
"""

# ## 3.2 Python数据结构

# 列表（list）、元组（tuple）、集合（set）、字典（dict）

# ### 3.2.1 列表(list)

# 用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。

# In[ ]

students = ["ming", "hua", "li", "juan", "yun", 3]
print (students)

# In[ ]
# 1）列表索引和切片

# 正序的时候索引从0开始，含左不含右；倒序的时候引从1开始
print(students)#打印出students列表
print(len(students))#利用len（）方法查询列表的长度
print ('[4]=', students[4])# 根据索引 查询 列表中的数据，索引是从0 开始的
print ('[-4]=', students[-4])#提取倒数第4个元素 
print ('[0:4]=', students[0:4])# 切片 从索引0 到 3提取list的元素
print( '[4:]=', students[4:])#切片  从索引4到最后的元素全部提取 
print ('[::2]=', students[::2])#切片 步长为2 
print ('[0:4:2]=', students[0:4:2])# 从索引0 到 3提取list的元素，切片 步长为2
print ('[-5:-1:]=', students[-5:-1:])# 从倒数第5到倒数第1提取list的元素，切片 步长为1
print ('[-2::-1]=', students[-2::-1])# 从倒数第5到倒数第1提取list的元素，切片 步长为1，倒叙

# In[ ]
# 2）修改列表
students = ["ming", "hua", "li", "juan", "yun", 3]
print (students)

students[3] = "小月"
print (students[3])

students[5]="小楠"
print (students[5])

students[5]=19978
print (students[5])

# In[ ]
# 3）插入元素
"""
append方法每次只能在末尾填入一个元素；
extend方法用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
insert方法可在指定的位置插入一个元素；
"""
# In[ ]:
students = ["ming", "hua", "li", "juan", "yun", 3]
print (students)

students.append('han') # 添加到尾部
students.extend(['long', 'wan'])
print (students)
# In[ ]:
students = ["ming", "hua", "li", "juan", "yun", 3]
print (students)
scores = [90, 80, 75, 66]
students.insert(1, scores) # 添加到指定位置
print (students)

# In[ ]
# 4）删除元素
"""
pop方法在不指定参数时默认删除末尾元素，也可以指定删除某个位置的元素；
remove方法删除指定的元素值；
clear方法清空列表元素；
del函数删除列表对象；
"""
# In[ ]:
students = ["ming", "hua", "li", "juan", "yun", 3]
print (students)

print (students.pop(1)) # 该函数返回被弹出的元素，不传入参数则删除最后一个元素
print (students)
students.remove("li")
print(students)
students.clear()
print(students)

# In[ ]
# 5）判断元素是否在列表中等
students = ["ming", "hua", "li", "juan", "yun", "hua",3]
print (students)

print( 'wan' in students)
print ('han' not in students)


# In[ ]:
# 6）列表常用方法
"""
copy方法复制一个物理对象，而非视图对象；
count方法计数；
index方法返回索引位置；
reverse方法实现元素颠倒；
sort方法排序，默认升序排序；
"""
students1 = ["ming", "hua", "li", "juan", "yun"]
students2=students1#students2共享students1的内存地址
students2[0]="New"
print(students1)
print(students2)
# In[ ]
students1 = ["ming", "hua", "li", "juan", "yun"]
students2=students1.copy()#students2复制students1的内容，不共享内存地址
students2[0]="New"
print(students1)
print(students2)
# In[ ]
students1.count("hua")
# In[ ]
students1.index("hua")# 只返回第一次出现的索引
# In[ ]
students1.reverse()
print(students1)
# In[ ]
L1=['f','g','a','a','b','c','d','e']
L1.sort()
print(L1)


# In[ ]:
# 7）range函数生成整数列表对象，含左不含右
for i in range(10):
    print(i)
# In[ ]
for i in range(-5, 5):
    print(i)
# In[ ]
for i in range(-10, 10, 2):
    print(i)
# In[ ]
for i in range(16, 10, -1):
    print(i)
# In[ ]

# ### 3.2.2 元组(tuple)

# 元组类似列表，元组里面的元素也是进行索引计算。列表里面的元素的值可以修改，而元组里面的元素的值不能修改，只能读取。元组的符号是()。

# In[ ]:

studentsTuple = ("ming", "jun", "qiang", "wu")
studentsTuple
# In[ ]:
try:
    studentsTuple[1] = 'fu'
except TypeError:
    print ('TypeError')

# In[ ]:
'ming' in studentsTuple
# In[ ]:
studentsTuple[0:4]
# In[ ]:
studentsTuple.count('ming')
# In[ ]:
studentsTuple.index('jun')
# In[ ]:
len(studentsTuple)


# In[ ]
# ### 3.2.3 集合(set)

# Python中集合主要有两个功能，一个功能是进行集合操作，另一个功能是消除重复元素。 集合的格式是：set()，其中()内可以是列表、字典或字符串，因为字符串是以列表的形式存储的

# In[ ]:
students = ["ming", "hua", "li", "juan", "yun", "hua"]
studentsSet = set(students)
print (studentsSet)
# In[ ]:
studentsSet.add('xu')
print (studentsSet)
# In[ ]:
studentsSet.remove('xu')
print (studentsSet)
# In[ ]
a = set("aabc")
print ('a=', a)
b = set("cdfm")
print ('b=', b)
# In[ ]
#交集
x = a & b 
print( 'x=', x)
# In[ ]
#并集
y = a | b
print ('y=', y)
# In[ ]
#差集
z = a - b
print( 'z=', z)

# In[ ]
# ### 3.2.4字典(dict)

# Python中的字典dict也叫做关联数组，用大括号{}括起来，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度，其中key不能重复。

# In[ ]:
k = {"name":"weiwei", "home":"guilin"}
print (k["home"])
# In[ ]:
print( k.keys())
print( k.values())
# In[ ]:

a={"success":True,"reason_code":"200","reason_desc":"获取成功",
   "rules":[{"rule_id":"1062274","score":7,"conditions":[{"address_a_value":
       "南通市","address_a":"mobile_address","address_b":"true_ip_address","address_b_value":"南京市","type":"match_address"}]}]}
print(a["success"])

# 添加、修改字典里面的项目

# In[ ]:
k = {"name":"weiwei", "home":"guilin"}
k["like"] = "music"
k['name'] = 'guangzhou'

# In[ ]:
print (k)
# 判断key是否存在
#要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
print ('name' in k)
#通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print (k.get('name'))

# In[ ]
# 删除key-value元素
k.pop('like')
print (k)


# ### 3.2.5 列表、元组、集合、字典的互相转换

# In[ ]:
students = ["ming", "hua", "li", "juan", "yun", "hua"]
tuple(students)

# In[ ]
#直接使用list，是将字典中的key转换为列表
k = {"name":"weiwei", "home":"guilin"}
list(k)
# In[ ]
#字典中的key转换为列表
key_value = list(k.keys())
print('字典中的key转换为列表：', key_value) 
#字典中的value转换为列表
value_list = list(k.values())
print('字典中的value转换为列表：', value_list)
# In[ ]
# zip可以将列表、元组、集合、字典‘缝合’起来
zl = zip(('A', 'B', 'C'), [1, 2, 3, 4]) 
print (zl)
print (dict(zl))

#%%
# *练习：小明的语文成绩是80分，数学成绩是70分，小红两门课的成绩则分别是90分和95分，尝试生成一个嵌套字典，可用于方便的查找分数

