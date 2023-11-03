# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:40:22 2018

@author: changguozhen
"""

# ## 3.4 Python函数

# 函数是用来封装特定功能的实体，可对不同类型和结构的数据进行操作，达到预定目标

# ### 3.4.1 调用函数

# - Python内置了很多有用的函数，我们可以直接调用，进行数据分析时多数情况下是通过调用定义好的函数来操作数据的

# In[ ]:

str1 = "as"
int1 = -9
print (len(str1))
print (abs(int1))

# In[ ]
# ### 3.4.2 定义函数

# 当系统自带函数不足以完成指定的功能时，需要用户自定义函数来完成。
"""
def 函数名()：
    函数内容
    函数内容
    <return 返回值>
"""
# In[ ]:

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
    
my_abs(-9)


# 多个返回值的情况

# In[ ]:

def test(i, j):
    k = i * j
    return i, j, k

a , b , c = test(4, 5)
print (a, b , c)
type(test(4, 5))

# In[ ]
# ### 3.4.3 高阶函数

# - 把另一个函数作为参数传入一个函数，这样的函数称为高阶函数

# 函数本身也可以赋值给变量，函数与其它对象具有同等地位

# In[ ]:
abs(-9)
myFunction = abs
myFunction(-9)


# - 参数传入函数

# In[ ]:

def add(x, y, f):
    return f(x) + f(y)

add(7, -5, myFunction)


# - 常用高阶函数

# map/reduce: 
#map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回；
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

# In[ ]:

myList = [-1, 2, -3, 4, -5, 6, 7]
map(abs, myList)
for i in map(abs, myList):
    print(i)

# In[ ]
# filter： filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
def is_odd(x):
    return x % 3  # 0被判断为False，其它被判断为True

filter(is_odd, myList)
# In[ ]
# sorted: 实现对序列排序，默认情况下对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1

# 默认排序：数字大小或字母序（针对字符串）
sorted(myList)

# In[ ]
# ### 3.4.4 匿名函数：
#高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便

# In[ ]:
f = lambda x: x * x
f(4)

# 等同于：
# In[ ]:
def f(x):
    return x * x
# In[ ]:
for i in map(lambda x: x * x, myList):
    print(i)
# In[ ]