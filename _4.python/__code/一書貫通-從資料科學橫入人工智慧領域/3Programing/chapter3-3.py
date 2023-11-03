# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:39:38 2018

@author: changguozhen
"""

# ## 3.3 Python控制流

# 在Python中通常的情况下程序的执行是从上往下执行的，而某些时候我们为了改变程序的执行顺序，使用控制流语句控制程序执行方式。Python中有三种控制流类型：顺序结构、分支结构、循环结构。

# 另外，Python可以使用分号";"分隔语句，但一般是使用换行来分隔；语句块不用大括号"{}"，而使用缩进（可以使用四个空格）来表示

# ### 3.3.1 顺序结构

# In[ ]:
# 一个物理行包含多个逻辑行
s = '7';num = int(s) 
print (num)
# In[ ]
# 一个逻辑行分为多个物理行
num =1 \
+ 1 
print (num)
# In[ ]
# ### 3.3.2 分支结构：Python中if语句是用来判断选择执行哪个语句块的
"""
if <True or Flase表达式>:
    执行语句块
elif <True or Flase表达式>：
    执行语句块
else：        # 都不满足
    执行语句块
"""    
# elif子句可以有多条，elif和else部分可省略
# In[ ]:

salary = 4
if salary > 5:
    print ("Wow!!!!!!!")
elif salary > 3:
    print ("That's OK.")
elif salary > 2:
    print ("5555555555")
else:
    print ("..........")

# In[ ]
# ### 3.3.3 循环结构

#1) while 循环
"""
while <True or Flase表达式>:
    循环执行语句块
else：          # 不满足条件
    执行语句块
"""
#else部分可以省略
# In[ ]:

a = 1
while a < 10:
    if a <= 5:
        print (a)
    else:
        print ("Hello")
    a = a + 1
else:
    print ("Done")

# In[ ]
# 2)- for 循环
"""
for (条件变量) in (集合)：
    执行语句块
"""   
# “集合”并不单指set，而是“形似”集合的列表、元组、字典、数组都可以进行循环
# 条件变量可以有多个
# In[ ]:
heights = {'Yao':226, 'Sharq':216, 'AI':183}
for i in heights:
    print (i, heights[i])


# *** 练习：使用循环和分支结构输出20以内的奇数
# In[ ]
# ### 3.3.4 break、continue和pass
#break:跳出循环
#continue:跳出当前循环
#pass:占位符，什么也不做
# In[ ]:

for i in range(1, 5):
    if i == 3:
        break
    print (i)


# In[ ]:

for i in range(1, 5):
    if i == 3:
        continue
    print (i)


# In[ ]:

for i in range(1, 5):
    if i == 3:
        pass
    print (i)

# In[ ]
# ### 3.3.5 列表生成式

# 三种形式
# - [<表达式> for (条件变量) in (集合)]
# - [<表达式> for (条件变量) in (集合) if <'True or False'表达式>]
# - [<表达式> if <'True or False'表达式> else <表达式>  for (条件变量) in (集合) ]

# In[ ]:

fruits = ['"Apple', 'Watermelon', '"Banana"']
[x.strip('"') for x in fruits]

# In[ ]:
[x ** 2 for x in range(21) if x%2]
# *练习：使用列表生成式生成一个布尔值列表，每个布尔值对应判断 range(21)中的每个元素是否是奇数。* 提示：if-else语句在for循环语句之前

# In[ ]:
[m + n for m in 'ABC' for n in 'XYZ']
# In[ ]