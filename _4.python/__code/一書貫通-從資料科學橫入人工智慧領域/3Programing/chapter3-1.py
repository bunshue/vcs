
# coding: utf-8

# # 第3讲 Python语言基础

# ## 3.1 Python数据类型
############################################################################################################
# ### 3.1.1 字符串

# 在Python中用引号引起来的字符集称之为字符串，比如：'hello'、"my Python"、"2+3"等都是字符串
# Python中字符串中使用的引号可以是单引号、双引号跟三引号

# In[ ]:
print ('hello world!')
# In[ ]:
c = 'It is a "dog"!'
print (c)
# In[ ]:
c1= "It's a dog!"
print (c1)
# In[ ]:
c2 = """hello
world
!"""
print (c2)
# In[ ]:
# - 转义字符'\'

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
# 原样输出引号内字符串可以使用在引号前加r
#转义字符	描述
#\\	反斜杠符号
#\'	单引号
#\"	双引号
#\a	响铃
#\b	退格(Backspace)
#\e	转义
#\000	空
#\n	换行
#\v	纵向制表符
#\t	横向制表符
#\r	回车
#\f	换页
#\oyy	八进制数，yy代表的字符，例如：\o12代表换行
#\xyy	十六进制数，yy代表的字符，例如：\x0a代表换行
print ('It\'s a dog!')
print ("hello world!\nhello Python!")
print ('\\\t\\')
# In[ ]:
print (r'\\\t\\')
# In[]
import pandas as pd
one1=pd.read_csv("D:\Python_book\3Programing\One.csv")
one1.head()
# In[ ]
one2=pd.read_csv("D:\\Python_book\\3Programing\\One.csv")
one2.head()
# In[ ]
one3=pd.read_csv(r"D:\Python_book\3Programing\One.csv")
one3.head()
# In[ ]:
# - 子字符串及运算
s = 'Python'
print( 'Py' in s)

# In[ ]:
# 取子字符串有两种方法，使用[]索引或者切片运算法[:]，这两个方法使用面非常广
print (s[2])

# In[ ]:
print (s[1:4])
# In[ ]:
# - 字符串连接 
word1 = '"hello"'
word2 = '"world"'
sentence = word1.strip('"') + ' ' + word2.strip('"') + '!'
print(sentence)
# In[ ]:
# - 字符串格式化输出
print( 'The first word is %s, and the second word is %s' %(word1, word2))

# In[ ]
############################################################################################################
# ### 3.1.2 整数与浮点数
# Python可以处理任意大小的整数，当然包括负整数，在程序中的表示方法和数学上的写法一模一样
i = 7
print(i)
# In[ ]:
7 + 3
# In[ ]:
7 - 3
# In[ ]:
7 * 3
# In[ ]:
7 ** 3
# In[ ]:
7 / 3#Python3之后，整数除法和浮点数除法已经没有差异
# In[ ]:
7 % 3
# 浮点数
# In[ ]:
7.0 / 3
# In[ ]:
3.14 * 10 ** 2
# In[ ]:
# 更多运算
import math

print (math.log(math.e)) # 更多运算可查阅文档
# In[ ]
############################################################################################################
# ### 3.1.3 布尔值
True and False
# In[ ]:
True or False
# In[ ]:
not True
# In[ ]:
True + False
# In[ ]:
18 >= 6 * 3 and 'py' in 'Python'

# In[ ]
############################################################################################################
# ### 3.1.4 日期时间
import time

now = time.strptime('2016-07-20', '%Y-%m-%d')
print (now)
# In[ ]:
type(now)
# In[ ]:
import datetime

someDay = datetime.date(1999,2,10)
anotherDay = datetime.date(1999,2,15)
deltaDay = anotherDay - someDay
deltaDay.days
# In[ ]
############################################################################################################
# ### 3.1.5空值none

# In[ ]:
print( None)

# In[ ]
############################################################################################################
# ### 3.1.6查看变量类型和类型转换
type(None)
# In[ ]:
type(s)
# In[ ]
############################################################################################################
# 类型转换
str(10086)
# In[ ]:
float(10086)
# In[ ]
int('10086')

# In[ ]
############################################################################################################
# ### 3.1.7表达式
#1）算数运算符
print(9//2)
print(9.0//2.0)
# In[ ]
#2）赋值运算符
a=3;c=1
c+=a
print(c)
#https://www.zhihu.com/question/20114936
# In[ ]
#3）比较运算符
a=3;b=1
print(a == b)
# In[ ]
#4）逻辑运算符
a=True;b=False
print(a and b)
# In[ ]
#5）成员运算符
str="你好北京";s="你"
#print("你在\"你好北京\"吗?",s in str)
print("%s在%s吗?"%(s, str),s in str)
# In[ ]











