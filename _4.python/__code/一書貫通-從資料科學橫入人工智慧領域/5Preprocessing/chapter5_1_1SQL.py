
# coding: utf-8

# # 第5章 数据整合和数据清洗

# ## 5.1 SQL语句介绍

# - SQL2数据过滤与排序
# - 选择表中指定列
import pandas as pd
import os 
os.chdir(r"D:\Python_book\5Preprocessing")
sale=pd.read_csv(r"sale.csv",encoding="gbk")

# In[ ]:

import sqlite3 # sqlite3相当于轻量版，更多功能可使用SQLAlchemy

con = sqlite3.connect(':memory:') # 数据库连接
sale.to_sql('sale', con) # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query("select year, market, sale, profit from sale", con) # 也可使用read_sql
newTable.head()


# - 选择表中所有列

# In[ ]:

sqlResult = pd.read_sql_query('select * from sale', con)
sqlResult.head()


# - 删除重复的行

# In[ ]:

pd.read_sql_query("select DISTINCT  year from sale", con)


# - 选择满足条件的行

# In[ ]:

pd.read_sql_query("select * from sale where market in ('东','西') and year=2012", con)


# - 对行进行排序

# In[ ]:

sql = '''select year, market, sale, profit
      from sale
      order by  sale desc'''
pd.read_sql_query(sql, con)


# ## 5.2纵向连接表
# sql操作

# In[ ]:

one = pd.read_csv(r"One.csv")
one.to_sql('One', con, index=False)
one.T


# In[ ]:

two = pd.read_csv(r"Two.csv")
two.to_sql('Two', con, index=False)
two.T


# union 和 union all

# In[ ]:

union = pd.read_sql('select * from one UNION select * from two', con)
union_all = pd.read_sql('select * from one UNION ALL select * from two', con)
union.T


# In[ ]:

union_all.T


# except 和 intersect

# In[ ]:

exceptTable = pd.read_sql('select * from one EXCEPT select * from two', con)
intersectTable = pd.read_sql('select * from one INTERSECT select * from two', con)
exceptTable.T


# In[ ]:

intersectTable.T


# *练习： 多表纵向连接

# DataFrame操作

# In[ ]:

pd.concat([one, two], axis=0, join='outer', ignore_index=True) # 更多参数可查看文档或帮助


# ## 5.3 横向连接表
# sql操作

# In[ ]:

table1 = pd.read_csv(r"Table1.csv")
table1.to_sql('table1', con, index=False)
table1.head()


# In[ ]:

table2 = pd.read_csv(r"Table2.csv")
table2.to_sql('table2', con, index=False)
table2.head()


# 笛卡尔积

# In[ ]:

pd.read_sql("select * from table1, table2", con)


# 内连接（使用inner join或使用where子句）

# In[ ]:

pd.read_sql("select * from table1 as a inner join table2 as b on a.id=b.id", con)
# pd.read_sql("select * from table1 as a, table2 as b where a.id=b.id", con)


# 左连接

# In[ ]:

pd.read_sql("select * from table1 as a left join table2 as b on a.id=b.id", con)


# In[ ]:

