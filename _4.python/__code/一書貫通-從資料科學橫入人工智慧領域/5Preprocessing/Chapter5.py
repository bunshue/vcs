"""


"""


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

#第四讲 数据整合和数据清洗

#4.1 SQL语句介绍

sale = pd.read_csv('sale.csv', encoding='gbk')
cc = sale.head()
print(cc)

#SQL2数据过滤与排序
#选择表中指定列

import sqlite3 # sqlite3相当于轻量版，更多功能可使用SQLAlchemy

con = sqlite3.connect(':memory:') # 数据库连接
sale.to_sql('sale', con) # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query("select year, market, sale, profit from sale", con) # 也可使用read_sql
cc = newTable.head()
print(cc)

#选择表中所有列

sqlResult = pd.read_sql_query('select * from sale', con)
cc = sqlResult.head()
print(cc)

#删除重复的行

pd.read_sql_query("select DISTINCT  year from sale", con)

#选择满足条件的行

pd.read_sql_query("select * from sale where year=2012 and market='东'", con)

#对行进行排序

sql = '''select year, market, sale, profit
      from sale
      order by year'''
pd.read_sql_query(sql, con)


#4.2纵向连接表

#sql操作

one = pd.read_csv("One.csv")
one.to_sql('One', con, index=False)
print(one.T)

two = pd.read_csv("Two.csv")
two.to_sql('Two', con, index=False)
print(two.T)

#union 和 union all

union = pd.read_sql('select * from one UNION select * from two', con)
union_all = pd.read_sql('select * from one UNION ALL select * from two', con)
print(union.T)

print(union_all.T)

#except 和 intersect

exceptTable = pd.read_sql('select * from one EXCEPT select * from two', con)
intersectTable = pd.read_sql('select * from one INTERSECT select * from two', con)
print(exceptTable.T)

print(intersectTable.T)

#*练习： 多表纵向连接

#DataFrame操作

cc = pd.concat([one, two], axis=0, join='outer', ignore_index=True) # 更多参数可查看文档或帮助
print(cc)

#4.3 横向连接表

#sql操作

table1 = pd.read_csv('Table1.csv')
table1.to_sql('table1', con, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv('Table2.csv')
table2.to_sql('table2', con, index=False)
cc = table2.head()
print(cc)

#笛卡尔积

pd.read_sql("select * from table1, table2", con)

#内连接（使用inner join或使用where子句）

pd.read_sql("select * from table1 as a inner join table2 as b on a.id=b.id", con)
# pd.read_sql("select * from table1 as a, table2 as b where a.id=b.id", con)

#左连接

pd.read_sql("select * from table1 as a left join table2 as b on a.id=b.id", con)

#DataFrame操作

pd.merge(table1, table2, on='id', how='left') # 参数设置可查看帮助

#按索引连接

table1.join(table2, how='outer', lsuffix='t1', rsuffix='t2') # 参数设置可查看帮助

#4.4 数据清洗

#发现数据问题类型

camp = pd.read_csv('teleco_camp_orig.csv')
cc = camp.head()
print(cc)

#脏数据或数据不正确

plt.hist(camp['AvgIncome'], bins=20)
# Try this: accepts['purch_price'].plot(kind='hist')
# And this: sns.distplot(accepts['purch_price'], kde=True, fit=stats.norm)
# should scipy.stats first
plt.show()

#这里的0值应该是缺失值
camp['AvgIncome']=camp['AvgIncome'].replace({0: np.NaN})
#像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
camp['AvgHomeValue']=camp['AvgHomeValue'].replace({0: np.NaN})
camp['Age']=camp['Age'].replace({0: np.NaN})
cc = camp.head(8)
print(cc)

cc = camp['AvgIncome'].describe(include='all')
print(cc)

#数据不一致- 这个问题需要详细的结合描述统计进行变量说明核对

#数据重复

cc = camp['dup'] = camp.duplicated() # 生成重复标识变量
print(cc)

cc = camp.dup.head()
print(cc)

#本数据没有重复记录，此处只是示例
camp_dup = camp[camp['dup'] == True] # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp['dup'] == False] # 注意与camp.drop_duplicates()的区别
cc = camp_nodup.head()
print(cc)

cc = camp['dup1'] = camp['ID'].duplicated() # 按照主键进行重复记录标识
print(cc)

# accepts['fico_score'].duplicated() # 没有实际意义

#缺失值处理

cc = camp.describe()
print(cc)
#如果count数量少于样本量，说明存在缺失
#缺失最多的两个变量是Age和AvgIncome,缺失了大概20%。

vmean = camp['Age'].mean(axis=0, skipna=True)
camp['Age_empflag'] = camp['Age'].isnull()
camp['Age']= camp['Age'].fillna(vmean)
camp['Age'].describe()

vmean = camp['AvgHomeValue'].mean(axis=0, skipna=True)
camp['AvgHomeValue_empflag'] = camp['AvgHomeValue'].isnull()
camp['AvgHomeValue']= camp['AvgHomeValue'].fillna(vmean)
camp['AvgHomeValue'].describe()

vmean = camp['AvgIncome'].mean(axis=0, skipna=True)
camp['AvgIncome_empflag'] = camp['AvgIncome'].isnull()
camp['AvgIncome']= camp['AvgIncome'].fillna(vmean)
camp['AvgIncome'].describe()

"""
其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

噪声值处理

盖帽法
"""

def blk(floor, root): # 'blk' will return a function
    def f(x):       
        if x < floor:
            x = floor
        elif x > root:
            x = root
        return x
    return f

q1 = camp['Age'].quantile(0.01) # 计算百分位数
q99 = camp['Age'].quantile(0.99)
blk_tot = blk(floor=q1, root=q99) # 'blk_tot' is a function
camp['Age']= camp['Age'].map(blk_tot)
cc = camp['Age'].describe()
print(cc)

#分箱（等深，等宽）
#分箱法——等宽分箱

camp['Age_group1'] = pd.qcut( camp['Age'], 4) # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group1.head()
print(cc)

#分箱法——等深分箱

camp['Age_group2'] = pd.cut( camp['Age'], 4) # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group2.head()
print(cc)

camp.to_csv('tmp_tele_camp_ok.csv')


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

