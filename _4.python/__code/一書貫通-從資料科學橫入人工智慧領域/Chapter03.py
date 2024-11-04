print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#日期时间

import time
now = time.strptime('2016-07-20', '%Y-%m-%d')
print (now)

type(now)

cc = time.strftime('%Y-%m-%d', now)
print(cc)

import datetime

someDay = datetime.date(1999,2,10)
anotherDay = datetime.date(1999,2,15)
deltaDay = anotherDay - someDay
print(deltaDay.days)

date_formate = "%Y-%m-%d" # year-month-day
cc = time.strptime('2016-06-22', date_formate)
print(cc)

# 复数complex

cplx = (4 + 2j) * (3 + 0.2j)
print(cplx)


# ## 3.2 Python数据结构
# 列表（list）、元组（tuple）、集合（set）、字典（dict）

# ### 3.2.1 列表(list)

# 用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。

students = ["ming", "hua", "li", "juan", "yun", 3]
print(students)

# 插入元素
students.append('han') # 添加到尾部
students.extend(['long', 'wan'])
print(students)

scores = [90, 80, 75, 66]
students.insert(1, scores) # 添加到指定位置
print(students)

# 删除元素

print(students.pop(1)) # 该函数返回被弹出的元素，不传入参数则删除最后一个元素
print(students)

# 判断元素是否在列表中等

print( 'wan' in students)
print('han' not in students)

students.count('wan')

students.index('wan')

# 集合

studentsSet = set(students)
print(studentsSet)

studentsSet.add('xu')
print(studentsSet)

studentsSet.remove('xu')
print(studentsSet)

a = set("abcnmaaaaggsng")
print('a=', a)
b = set("cdfm")
print('b=', b)

#交集
x = a & b 
print( 'x=', x)
#并集
y = a | b
print('y=', y)
#差集
z = a - b
print( 'z=', z)
#去除重复元素
new = set(a)
print( z)

k = {"name":"weiwei", "home":"guilin"}
print(k["home"])
print( k.keys())
print( k.values())

a={"success":True,"reason_code":"200","reason_desc":"获取成功",
   "rules":[{"rule_id":"1062274","score":7,"conditions":[{"address_a_value":
       "南通市","address_a":"mobile_address","address_b":"true_ip_address","address_b_value":"南京市","type":"match_address"}]}]}
print(a["success"])


# 添加、修改字典里面的项目

# In[ ]:

k["like"] = "music"
k['name'] = 'guangzhou'
print(k)

# ### 2.2.5 列表、元组、集合、字典的互相转换

tuple(students)
list(k)

zl = zip(('A', 'B', 'C'), [1, 2, 3, 4]) # zip可以将列表、元组、集合、字典‘缝合’起来
print(zl)
print(type(zl))
print(dict(zl))

heights = {'Yao':226, 'Sharq':216, 'AI':183}
for i in heights:
    print(i, heights[i])

#for key, value in heights.items():-Python3 不能使用dict.iteritems(),改为dict.items()
for key, value in heights.items():
    print(key, value)


# - 匿名函数：高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
f = lambda x: x * x
f(4)



import pandas as pd

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df.head(2)

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df1.head(5)

df2 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
cc = pd.crosstab(df2.key, df2.data1)
print(cc)

# ## 3.6 使用pandas读写数据

# - pandas可以读取文本文件、json、数据库、Excel等文件
# - 使用read_csv方法读取以逗号分隔的文本文件作为DataFrame，其它还有类似read_table, read_excel, read_html, read_sql等等方法

one = pd.read_csv('data/One.csv',sep=",")  # same
one = pd.read_csv('data/One.csv')
cc = one.head()
print(cc)


hsb2 = pd.read_table('data/hsb2.txt')
cc = hsb2.head()
print(cc)

html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html') # Return a list
print(html)

#xls = pd.read_excel('hsb2.xlsx', sheetname=0) NG
xls = pd.read_excel('data/hsb2.xlsx')
cc = xls.head()
print(cc)

# 写入文件
xls.to_csv('tmp_copyofhsb2.csv')


# 查看一下关键字有哪些，避免关键字做自定义标识符
import keyword
print(keyword.kwlist)


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


