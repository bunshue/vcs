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

import sqlite3


print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# SQL语句介绍

sale = pd.read_csv("sale.csv", encoding="gbk")
cc = sale.head()
print(cc)

# SQL数据过滤与排序
# 选择表中指定列

con = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", con)  # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query(
    "select year, market, sale, profit from sale", con
)  # 也可使用read_sql
cc = newTable.head()
print(cc)

# 选择表中所有列

sqlResult = pd.read_sql_query("select * from sale", con)
cc = sqlResult.head()
print(cc)

# 删除重复的行

pd.read_sql_query("select DISTINCT  year from sale", con)

# 选择满足条件的行

pd.read_sql_query("select * from sale where year=2012 and market='东'", con)

# 对行进行排序

sql = """select year, market, sale, profit
      from sale
      order by year"""
pd.read_sql_query(sql, con)


# 4.2纵向连接表

# sql操作

one = pd.read_csv("One.csv")
one.to_sql("One", con, index=False)
print(one.T)

two = pd.read_csv("Two.csv")
two.to_sql("Two", con, index=False)
print(two.T)

# union 和 union all

union = pd.read_sql("select * from one UNION select * from two", con)
union_all = pd.read_sql("select * from one UNION ALL select * from two", con)
print(union.T)

print(union_all.T)

# except 和 intersect

exceptTable = pd.read_sql("select * from one EXCEPT select * from two", con)
intersectTable = pd.read_sql("select * from one INTERSECT select * from two", con)
print(exceptTable.T)

print(intersectTable.T)

# *练习： 多表纵向连接

# DataFrame操作

cc = pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助
print(cc)

# 4.3 横向连接表

# sql操作

table1 = pd.read_csv("Table1.csv")
table1.to_sql("table1", con, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("Table2.csv")
table2.to_sql("table2", con, index=False)
cc = table2.head()
print(cc)

# 笛卡尔积

pd.read_sql("select * from table1, table2", con)

# 内连接（使用inner join或使用where子句）

pd.read_sql("select * from table1 as a inner join table2 as b on a.id=b.id", con)
# pd.read_sql("select * from table1 as a, table2 as b where a.id=b.id", con)

# 左连接

pd.read_sql("select * from table1 as a left join table2 as b on a.id=b.id", con)

# DataFrame操作

pd.merge(table1, table2, on="id", how="left")  # 参数设置可查看帮助

# 按索引连接

table1.join(table2, how="outer", lsuffix="t1", rsuffix="t2")  # 参数设置可查看帮助

# 4.4 数据清洗

# 发现数据问题类型

camp = pd.read_csv("teleco_camp_orig.csv")
cc = camp.head()
print(cc)

# 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20)
# Try this: accepts['purch_price'].plot(kind='hist')
# And this: sns.histplot(accepts['purch_price'], kde=True, fit=stats.norm)
# should scipy.stats first
plt.show()

# 这里的0值应该是缺失值
camp["AvgIncome"] = camp["AvgIncome"].replace({0: np.NaN})
# 像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
camp["AvgHomeValue"] = camp["AvgHomeValue"].replace({0: np.NaN})
camp["Age"] = camp["Age"].replace({0: np.NaN})
cc = camp.head(8)
print(cc)

cc = camp["AvgIncome"].describe(include="all")
print(cc)

# 数据不一致- 这个问题需要详细的结合描述统计进行变量说明核对

# 数据重复

cc = camp["dup"] = camp.duplicated()  # 生成重复标识变量
print(cc)

cc = camp.dup.head()
print(cc)

# 本数据没有重复记录，此处只是示例
camp_dup = camp[camp["dup"] == True]  # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp["dup"] == False]  # 注意与camp.drop_duplicates()的区别
cc = camp_nodup.head()
print(cc)

cc = camp["dup1"] = camp["ID"].duplicated()  # 按照主键进行重复记录标识
print(cc)

# accepts['fico_score'].duplicated() # 没有实际意义

# 缺失值处理

cc = camp.describe()
print(cc)
# 如果count数量少于样本量，说明存在缺失
# 缺失最多的两个变量是Age和AvgIncome,缺失了大概20%。

vmean = camp["Age"].mean(axis=0, skipna=True)
camp["Age_empflag"] = camp["Age"].isnull()
camp["Age"] = camp["Age"].fillna(vmean)
camp["Age"].describe()

vmean = camp["AvgHomeValue"].mean(axis=0, skipna=True)
camp["AvgHomeValue_empflag"] = camp["AvgHomeValue"].isnull()
camp["AvgHomeValue"] = camp["AvgHomeValue"].fillna(vmean)
camp["AvgHomeValue"].describe()

vmean = camp["AvgIncome"].mean(axis=0, skipna=True)
camp["AvgIncome_empflag"] = camp["AvgIncome"].isnull()
camp["AvgIncome"] = camp["AvgIncome"].fillna(vmean)
camp["AvgIncome"].describe()

"""
其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

噪声值处理

盖帽法
"""


def blk(floor, root):  # 'blk' will return a function
    def f(x):
        if x < floor:
            x = floor
        elif x > root:
            x = root
        return x

    return f


q1 = camp["Age"].quantile(0.01)  # 计算百分位数
q99 = camp["Age"].quantile(0.99)
blk_tot = blk(floor=q1, root=q99)  # 'blk_tot' is a function
camp["Age"] = camp["Age"].map(blk_tot)
cc = camp["Age"].describe()
print(cc)

# 分箱（等深，等宽）
# 分箱法——等宽分箱

camp["Age_group1"] = pd.qcut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group1.head()
print(cc)

# 分箱法——等深分箱

camp["Age_group2"] = pd.cut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
cc = camp.Age_group2.head()
print(cc)

camp.to_csv("tmp_tele_camp_ok.csv")

print("------------------------------------------------------------")  # 60個
# Pandas
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# ### 5.1.1 行列操作

# #### 1. 单列

sample = pd.DataFrame(np.random.randn(4, 5), columns=["a", "b", "c", "d", "e"])
sample

sample["a"]

sample.ix[:, "a"]

sample[["a"]]

# #### 2. 选择多行和多列

sample.ix[0:2, 0:2]

# #### 3. 创建、删除列

sample["new_col1"] = sample["a"] - sample["b"]
sample


# In[16]:

sample_new = sample.assign(
    new_col2=sample["a"] - sample["b"], new_col3=sample["a"] + sample["b"]
)
sample_new


# In[24]:

sample.drop("a", axis=1)


# ### 5.1.2 条件查询

# In[25]:

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 65, 67],
        "group": [1, 1, 1, 2, 1, 2],
    }
)
sample


# #### 1. 单条件

# In[30]:

# sample.score > 70
sample[sample.score > 70]


# #### 2. 多条件

# In[32]:

sample[(sample.score > 70) & (sample.group == 1)]


# #### 3. 使用query

# In[33]:

# sample.query('score > 90')
sample.query("(group ==2) |(group == 1)")


# #### 4. 其他

# In[34]:

sample[sample["score"].between(70, 80, inclusive=True)]


# In[35]:

sample[sample["name"].isin(["Bob", "Lindy"])]


# In[36]:

sample[sample["name"].str.contains("[M]+")]


# ### 5.1.3 横向连接

# In[37]:

df1 = pd.DataFrame({"id": [1, 2, 3], "col1": ["a", "b", "c"]})
df2 = pd.DataFrame({"id": [4, 3], "col2": ["d", "e"]})


# #### 1. 内连接

# In[38]:

df1.merge(df2, how="inner", left_on="id", right_on="id")


# #### 2. 外连接

# In[40]:

df1.merge(df2, how="left", on="id")


# #### 3. 行索引连接

# In[41]:

df1 = pd.DataFrame({"id1": [1, 2, 3], "col1": ["a", "b", "c"]}, index=[1, 2, 3])
df2 = pd.DataFrame({"id2": [1, 2, 3], "col2": ["aa", "bb", "cc"]}, index=[1, 3, 2])


# In[42]:

pd.concat([df1, df2], axis=1)
# df1.join(df2)


# ### 5.1.4 纵向合并

# In[43]:

df1 = pd.DataFrame(
    {"id": [1, 1, 1, 2, 3, 4, 6], "col": ["a", "a", "b", "c", "v", "e", "q"]}
)
df2 = pd.DataFrame({"id": [1, 2, 3, 3, 5], "col": ["x", "y", "z", "v", "w"]})


# In[44]:

pd.concat([df1, df2], ignore_index=True, axis=0)


# In[45]:

pd.concat([df1, df2], ignore_index=True).drop_duplicates()


# In[46]:

df3 = df1.rename(columns={"col": "new_col"})


# In[47]:

pd.concat([df1, df3], ignore_index=True).drop_duplicates()


# ### 5.1.5 排序

# #### 1. 排序

# In[50]:

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)


# In[51]:

sample


# In[52]:

sample.sort_values("score", ascending=False, na_position="last")


# In[53]:

sample.sort_values(["group", "score"])


# ### 5.1.6 分组汇总

# In[8]:

sample = pd.read_csv(r"D:\Python_book\5Preprocessing\sample.csv", encoding="gbk")
sample.head()


# In[9]:

sample.groupby("class")[["math"]].max()


# In[10]:

sample.groupby(["grade", "class"])[["math"]].mean()


# In[11]:

sample.groupby(["grade"])["math", "chinese"].mean()


# In[12]:

sample.groupby("class")["math"].agg(["mean", "min", "max"])


# In[14]:

df = sample.groupby(["grade", "class"])["math", "chinese"].agg(["min", "max"])
df


# ### 5.1.7 拆分、堆叠列

# In[19]:

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)


# In[24]:

pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")


# In[25]:

pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc="sum",
)


# In[27]:

table1 = pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc=np.sum,
).reset_index()
table1


# In[28]:

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)


# ### 5.1.8 赋值与条件赋值

# #### 1. 赋值

# In[29]:

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [99, 78, 999, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)


# In[30]:

sample.score.replace(999, np.nan)


# In[32]:

sample.replace({"score": {999: np.nan}, "name": {"Bob": np.nan}})


# #### 2. 条件赋值

# In[33]:


def transform(row):
    if row["group"] == 1:
        return "class1"
    elif row["group"] == 2:
        return "class2"


sample.apply(transform, axis=1)


# In[34]:

sample.assign(class_n=sample.apply(transform, axis=1))


# In[35]:

sample = sample.copy()
sample.loc[sample.group == 1, "class_n"] = "class1"
sample.loc[sample.group == 2, "class_n"] = "class2"


# In[ ]:


print("------------------------------------------------------------")  # 60個
# SQL
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗

# ## 5.1 SQL语句介绍

# - SQL2数据过滤与排序
# - 选择表中指定列

sale = pd.read_csv(r"sale.csv", encoding="gbk")

# In[ ]:

con = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", con)  # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query(
    "select year, market, sale, profit from sale", con
)  # 也可使用read_sql
newTable.head()


# - 选择表中所有列

# In[ ]:

sqlResult = pd.read_sql_query("select * from sale", con)
sqlResult.head()


# - 删除重复的行

# In[ ]:

pd.read_sql_query("select DISTINCT  year from sale", con)


# - 选择满足条件的行

# In[ ]:

pd.read_sql_query("select * from sale where market in ('东','西') and year=2012", con)


# - 对行进行排序

# In[ ]:

sql = """select year, market, sale, profit
      from sale
      order by  sale desc"""
pd.read_sql_query(sql, con)


# ## 5.2纵向连接表
# sql操作

# In[ ]:

one = pd.read_csv(r"One.csv")
one.to_sql("One", con, index=False)
one.T


# In[ ]:

two = pd.read_csv(r"Two.csv")
two.to_sql("Two", con, index=False)
two.T


# union 和 union all

# In[ ]:

union = pd.read_sql("select * from one UNION select * from two", con)
union_all = pd.read_sql("select * from one UNION ALL select * from two", con)
union.T


# In[ ]:

union_all.T


# except 和 intersect

# In[ ]:

exceptTable = pd.read_sql("select * from one EXCEPT select * from two", con)
intersectTable = pd.read_sql("select * from one INTERSECT select * from two", con)
exceptTable.T


# In[ ]:

intersectTable.T


# *练习： 多表纵向连接

# DataFrame操作

# In[ ]:

pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助


# ## 5.3 横向连接表
# sql操作

# In[ ]:

table1 = pd.read_csv(r"Table1.csv")
table1.to_sql("table1", con, index=False)
table1.head()


# In[ ]:

table2 = pd.read_csv(r"Table2.csv")
table2.to_sql("table2", con, index=False)
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


print("------------------------------------------------------------")  # 60個
# cleaning
print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# 数据清洗

# 发现数据问题类型

camp = pd.read_csv("teleco_camp_orig.csv")
camp.head()

# - 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20, normed=True)  # 查看分布情况  # normed 改成 density
camp["AvgIncome"].describe(include="all")

plt.hist(camp["AvgHomeValue"], bins=20, normed=True)  # 查看分布情况  # normed 改成 density
camp["AvgHomeValue"].describe(include="all")

# 这里的0值应该是缺失值
camp["AvgIncome"] = camp["AvgIncome"].replace({0: np.NaN})
# 像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
plt.hist(
    camp["AvgIncome"],
    bins=20,
    normed=True,
    range=(camp.AvgIncome.min(), camp.AvgIncome.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域
camp["AvgIncome"].describe(include="all")

camp["AvgHomeValue"] = camp["AvgHomeValue"].replace({0: np.NaN})
plt.hist(
    camp["AvgHomeValue"],
    bins=20,
    normed=True,
    range=(camp.AvgHomeValue.min(), camp.AvgHomeValue.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域
camp["AvgHomeValue"].describe(include="all")

# - 数据不一致-
# 这个问题需要详细的结合描述统计进行变量说明核对

# - 数据重复

camp["dup"] = camp.duplicated()  # 生成重复标识变量
camp.dup.head()

# 本数据没有重复记录，此处只是示例
camp_dup = camp[camp["dup"] == True]  # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp["dup"] == False]  # 注意与camp.drop_duplicates()的区别
camp_nodup.head()

camp["dup1"] = camp["ID"].duplicated()  # 按照主键进行重复记录标识
# accepts['fico_score'].duplicated() # 没有实际意义

# * 缺失值处理

camp.describe()
# 如果count数量少于样本量，说明存在缺失
# 缺失最多的两个变量是Age和AvgIncome,缺失了大概20%。

vmean = camp["Age"].mean(axis=0, skipna=True)
camp["Age_empflag"] = camp["Age"].isnull()
camp["Age"] = camp["Age"].fillna(vmean)
camp["Age"].describe()

vmean = camp["AvgHomeValue"].mean(axis=0, skipna=True)
camp["AvgHomeValue_empflag"] = camp["AvgHomeValue"].isnull()
camp["AvgHomeValue"] = camp["AvgHomeValue"].fillna(vmean)
camp["AvgHomeValue"].describe()

vmean = camp["AvgIncome"].mean(axis=0, skipna=True)
camp["AvgIncome_empflag"] = camp["AvgIncome"].isnull()
camp["AvgIncome"] = camp["AvgIncome"].fillna(vmean)
camp["AvgIncome"].describe()

# - 其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
# - 多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
# - 多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

# * 噪声值处理
# - 盖帽法


def blk(floor, root):  # 'blk' will return a function
    def f(x):
        if x < floor:
            x = floor
        elif x > root:
            x = root
        return x

    return f


q1 = camp["Age"].quantile(0.01)  # 计算百分位数
q99 = camp["Age"].quantile(0.99)
blk_tot = blk(floor=q1, root=q99)  # 'blk_tot' is a function
camp["Age"] = camp["Age"].map(blk_tot)
camp["Age"].describe()

# - 分箱（等深，等宽）
# - 分箱法——等宽分箱

camp["Age_group1"] = pd.qcut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
camp.Age_group1.head()

# - 分箱法——等深分箱

camp["Age_group2"] = pd.cut(camp["Age"], 4)  # 这里以age_oldest_tr字段等宽分为4段
camp.Age_group2.head()

camp.to_csv("tele_camp_ok.csv")


print("------------------------------------------------------------")  # 60個
# reshape
print("------------------------------------------------------------")  # 60個


# coding: utf-8

# # 第5章 数据整合和数据清洗
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# ### 5.1.1 行列操作

# #### 1. 单列

# ### 拆分、堆叠列

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)


table

result = pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")

pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc="sum",
)

table1 = pd.pivot_table(
    table,
    index="cust_id",
    columns="type",
    values="Monetary",
    fill_value=0,
    aggfunc=np.sum,
).reset_index()
table1


# In[28]:

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)

# # 第5章3 RFM
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ### 1. 导入数据

trad_flow = pd.read_csv(
    r"D:\Python_Training\script_Python\5Preprocessing\RFM_TRAD_FLOW.csv", encoding="gbk"
)
trad_flow.head(10)

# ### 2.计算 RFM

# In[6]:

M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()


# In[7]:

M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")


# In[8]:

F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()
F.head()


# In[9]:

F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")
F_trans.head()


# In[10]:

R = trad_flow.groupby(["cumid", "type"])[["time"]].max()
R.head()


# In[11]:

# R_trans=pd.pivot_table(R,index='cumid',columns='type',values='time')
# R_trans.head()


# ### 3.衡量客户对打折商品的偏好

# In[12]:

M_trans["Special_offer"] = M_trans["Special_offer"].fillna(0)


# In[13]:

M_trans["spe_ratio"] = M_trans["Special_offer"] / (
    M_trans["Special_offer"] + M_trans["Normal"]
)
M_rank = M_trans.sort_values("spe_ratio", ascending=False, na_position="last").head()


# In[16]:

M_rank["spe_ratio_group"] = pd.qcut(M_rank["spe_ratio"], 4)  # 这里以age_oldest_tr字段等宽分为4段
M_rank.head()


# In[ ]:


print("------------------------------------------------------------")  # 60個
# sampling
print("------------------------------------------------------------")  # 60個


# coding: utf-8

# In[147]:


def get_sample(df, sampling="simple_random", k=1, stratified_col=None):
    """
    对输入的 dataframe 进行抽样的函数

    参数:
        - df: 输入的数据框 pandas.dataframe 对象

        - sampling:抽样方法 str
            可选值有 ["simple_random", "stratified", "systematic"]
            按顺序分别为: 简单随机抽样、分层抽样、系统抽样

        - k: 抽样个数或抽样比例 int or float
            (int, 则必须大于0; float, 则必须在区间(0,1)中)
            如果 0 < k < 1 , 则 k 表示抽样对于总体的比例
            如果 k >= 1 , 则 k 表示抽样的个数；当为分层抽样时，代表每层的样本量

        - stratified_col: 需要分层的列名的列表 list
            只有在分层抽样时才生效

    返回值:
        pandas.dataframe 对象, 抽样结果
    """
    from functools import reduce

    len_df = len(df)
    if k <= 0:
        raise AssertionError("k不能为负数")
    elif k >= 1:
        assert isinstance(k, int), "选择抽样个数时, k必须为正整数"
        sample_by_n = True
        if sampling is "stratified":
            alln = (
                k * df.groupby(by=stratified_col)[stratified_col[0]].count().count()
            )  # 有问题的
            # alln=k*df[stratified_col].value_counts().count()
            if alln >= len_df:
                raise AssertionError("请确认k乘以层数不能超过总样本量")
    else:
        sample_by_n = False
        if sampling in ("simple_random", "systematic"):
            k = math.ceil(len_df * k)

    # print(k)

    if sampling is "simple_random":
        print("使用简单随机抽样")
        idx = random.sample(range(len_df), k)
        res_df = df.iloc[idx, :].copy()
        return res_df

    elif sampling is "systematic":
        print("使用系统抽样")
        step = len_df // k + 1  # step=len_df//k-1
        start = 0  # start=0
        idx = range(len_df)[start::step]  # idx=range(len_df+1)[start::step]
        res_df = df.iloc[idx, :].copy()
        # print("k=%d,step=%d,idx=%d"%(k,step,len(idx)))
        return res_df

    elif sampling is "stratified":
        assert stratified_col is not None, "请传入包含需要分层的列名的列表"
        assert all(np.in1d(stratified_col, df.columns)), "请检查输入的列名"

        grouped = df.groupby(by=stratified_col)[stratified_col[0]].count()
        if sample_by_n == True:
            group_k = grouped.map(lambda x: k)
        else:
            group_k = grouped.map(lambda x: math.ceil(x * k))

        res_df = pd.DataFrame(columns=df.columns)
        for df_idx in group_k.index:
            df1 = df
            if len(stratified_col) == 1:
                df1 = df1[df1[stratified_col[0]] == df_idx]
            else:
                for i in range(len(df_idx)):
                    df1 = df1[df1[stratified_col[i]] == df_idx[i]]
            idx = random.sample(range(len(df1)), group_k[df_idx])
            group_df = df1.iloc[idx, :].copy()
            res_df = res_df.append(group_df)
        return res_df

    else:
        raise AssertionError("sampling is illegal")


clients = pd.read_csv(r"D:\Python_book\5Preprocessing\clients.csv", encoding="gbk")
# clients["district_id_c"]=clients["district_id"].map(lambda x:"id"+str(x))
# %%
# 在每个地区分别用简单随机抽样、分层抽样、系统抽样，三种方式抽取样本

# %%1简单随机抽样
# %%简单随机抽样-按数量取
srn = get_sample(clients, sampling="simple_random", k=22, stratified_col=None)
# %%简单随机抽样-按百分比取
srp = get_sample(clients, sampling="simple_random", k=0.1, stratified_col=None)

# %%2分层抽样
# %%分层抽样-按每层数量取
strn = get_sample(clients, sampling="stratified", k=2, stratified_col=["district_id"])
# %%分层抽样-按每层百分比取
strp = get_sample(clients, sampling="stratified", k=0.1, stratified_col=["district_id"])

# %%3系统抽样
# %%系统抽样-按数量取
sysn = get_sample(clients, sampling="systematic", k=4, stratified_col=None)
# %%系统抽样-按百分比取
sysp = get_sample(clients, sampling="systematic", k=0.1, stratified_col=None)
# %%


# %%


print("------------------------------------------------------------")  # 60個
# RFM2
print("------------------------------------------------------------")  # 60個

# # 第5章3 RFM
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

trad_flow = pd.read_csv("RFM_TRAD_FLOW.csv", encoding="gbk")
trad_flow.head()

# ### 2.计算 RFM

# 先将非标准字符串时间格式化为时间数组，再转换为时间戳便于计算
trad_flow["time"] = trad_flow["time"].map(
    lambda x: time.mktime(time.strptime(x, "%d%b%y:%H:%M:%S"))
)

# 查找每个购物ID每个销售类型下的最近时间
R = trad_flow.groupby(["cumid", "type"])[["time"]].max()

# 转化为透视表
R_trans = pd.pivot_table(R, index="cumid", columns="type", values="time")

# 用最久远的购物时间替换缺失值
R_trans[["Special_offer", "returned_goods"]] = R_trans[
    ["Special_offer", "returned_goods"]
].apply(lambda x: x.replace(np.nan, min(x)), axis=0)
R_trans["R_max"] = R_trans[["Normal", "Presented", "Special_offer"]].apply(
    lambda x: max(x), axis=1
)

R_trans.head()


# In[3]:

# 对购物频率按照购物ID和购物类型进行汇总统计
F = trad_flow.groupby(["cumid", "type"])[["transID"]].count()

# 转化为透视表
F_trans = pd.pivot_table(F, index="cumid", columns="type", values="transID")

# 用0填补缺失值
F_trans[["Special_offer", "returned_goods"]] = F_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 将退货的频数转化为负数
F_trans["returned_goods"] = F_trans["returned_goods"].map(lambda x: -x)

# 求每个购物ID的购物总次数
F_trans["F_total"] = F_trans.apply(lambda x: sum(x), axis=1)

F_trans.head()


# In[4]:

# 对购物金额按照购物ID和购物类型进行汇总统计
M = trad_flow.groupby(["cumid", "type"])[["amount"]].sum()

# 转化为透视表
M_trans = pd.pivot_table(M, index="cumid", columns="type", values="amount")

# 用0填补缺失值
M_trans[["Special_offer", "returned_goods"]] = M_trans[
    ["Special_offer", "returned_goods"]
].fillna(0)

# 求每个购物ID的购物总金额
M_trans["M_total"] = M_trans.apply(lambda x: sum(x), axis=1)

M_trans.head()


# In[5]:

# 合并表
RFM = pd.concat([R_trans["R_max"], F_trans["F_total"], M_trans["M_total"]], axis=1)
# RFM三个维度等宽分箱打分
RFM["R_score"] = pd.cut(RFM.R_max, 3, labels=[1, 2, 3], precision=2)
RFM["F_score"] = pd.cut(RFM.F_total, 3, labels=[1, 2, 3], precision=2)
RFM["M_score"] = pd.cut(RFM.M_total, 3, labels=[1, 2, 3], precision=2)


# RFM各三类，总共有27种组合，为方便营销简化分类为8种
def score_label(a, b, c):
    """
    a: 'R_score'
    b: 'F_score'
    c: 'M_score'
    """
    if a == 3 and b == 3 and c == 3:
        return "重要价值客户"
    elif a == 3 and (b in [1, 2]) and c == 3:
        return "重要发展客户"
    elif (a in [1, 2]) and b == 3 and c == 3:
        return "重要保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and c == 3:
        return "重要挽留客户"
    elif a == 3 and b == 3 and (c in [1, 2]):
        return "一般价值客户"
    elif a == 3 and (b in [1, 2]) and (c in [1, 2]):
        return "一般发展客户"
    elif (a in [1, 2]) and b == 3 and (c in [1, 2]):
        return "一般保持客户"
    elif (a in [1, 2]) and (b in [1, 2]) and (c in [1, 2]):
        return "一般挽留客户"


# 为每个购物ID贴标签
RFM["Label"] = RFM[["R_score", "F_score", "M_score"]].apply(
    lambda x: score_label(x[0], x[1], x[2]), axis=1
)

RFM.head()


# - '重要价值客户'：消费额度高，购物频率高，最近购物时间也较近——该类客户是重要且忠实的大客户，要细心维护。
#
#
# - '重要发展客户'：消费额度高，购物频率不高，最近购物时间较近——该类客户只是购物频率不高，有巨大的挖掘潜力，可根据该客户以往购物信息，进行个性                                                              化推荐，并发放购物优惠券刺激消费，增加客户粘性。
#
#
# - '重要保持客户'：消费额度高，购物频率高，但最近购物时间较远——该类客户最近一次购物时间较久远，可能是快要流失的重要客户，可以让客户沟通了解其                                                              是不是哪项环节不够人性化体验不好，导致购物频率过低。
#
#
# - '重要挽留客户'：消费额度高，购物频率不高，最近购物时间也较远——该类客户可能是已经流失的重要客户，如果还能联系上，可跟进了解其流失原因，对有                                                              相似客户特征的群体进行预警，针对性改进。
#
#
# - '一般价值客户'：消费额度不高，购物频率高，最近购物时间也较近——该类客户对我们的产品感兴趣，很活跃，但购物金额过低，可能是价格敏感性客户，可                                                              对其组合金融产品增加其购买力。
#
#
# - '一般发展客户'：消费额度不高，购物频率不高，最近购物时间较近——该类客户可能是我们的新晋客户，对我们的服务和产品进行试探性体验，可多留意此类                                                              客户，进行邮件短信关怀及时发送优惠信息。
#
#
# - '一般保持客户'：消费额度不高，购物频率高，最近购物时间较远——该类客户可能是快要流失的一般客户，可进行一般性低成本营销。
#
#
# - '一般挽留客户'：消费额度不高，购物频率不高，最近购物时间也较远——该类客户不是我们的目标客户，经费有限可忽略此类客户。


# In[ ]:


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


# coding: utf-8
