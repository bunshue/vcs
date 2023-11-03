# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 16:41:15 2018

@author: changguozhen
"""

# ## 3.6 pandas读写结构化数据

# 模块是可以实现一项或多项功能的程序块，Python本身就内置了很多非常有用的模块，只要安装完毕，这些模块就可以立刻使用

# In[ ]:
# 可以通过安装第三方包来增加系统功能，也可以自己编写模块。引入模块有多种方式

# In[ ]:

import pandas as pd

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df.head(2)


# In[ ]:

from pandas import DataFrame

df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})
df1.head(5)


# In[5]
# ## 3.6 使用pandas读写数据

# - pandas可以读取文本文件、json、数据库、Excel等文件
# - 使用read_csv方法读取以逗号分隔的文本文件作为DataFrame，其它还有类似read_table, read_excel, read_html, read_sql等等方法

# In[5]:

import pandas as pd
one = pd.read_csv(r'D:\Python_book\3Programing\One.csv',sep=",")
one.head()
# In[ ]:
#设置工作目录
import os
os.chdir(r'D:\Python_book\3Programing')
hsb2 = pd.read_table('hsb2.txt')
hsb2.head()


# In[ ]:
#html = pd.read_html('http://www.fdic.gov/bank/individual/failed/banklist.html') # Return a list
#html
# In[ ]:
xls = pd.read_excel('hsb2.xlsx', sheetname=0)
xls.head()
# In[ ]
# 写入文件
xls.to_csv('copyofhsb2.csv')
# In[ ]
