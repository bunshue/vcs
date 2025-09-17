"""
sqlite + pandas


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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # return
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


print("------------------------------------------------------------")  # 60個

import csv
import shutil
import datetime
import sqlite3


def show_data_base_contents(db_filename, table_name):
    conn = sqlite3.connect(db_filename)  # 建立資料庫連線
    # SELECT * : 取得所有資料
    sqlstr = "SELECT * FROM {};".format(table_name)  # same
    sqlstr = "SELECT * FROM %s" % table_name
    cursor = conn.execute(sqlstr)
    # 使用fetchall()
    # print("用fetchall()讀取 全部資料 預設排序(依第1項升冪排序)")
    rows = cursor.fetchall()  # 讀取全部資料成元組串列
    length = len(rows)
    print("共有", length, "筆資料")
    for i in range(length):
        print("第" + str(i + 1) + "筆資料 : ", rows[i])
        if i > 50:
            break
    """
    # 不使用fetchall()
    i = 0
    for row in cursor:  # 不是用fetchall()讀取全部資料
        print("第" + str(i + 1) + "筆資料 : ", row)
        i += 1
        if i > 10:
            break
    """
    conn.close()  # 關閉資料庫連線


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料庫 轉 df")

db_filename_animals = "data/animals_old.sqlite"

print("讀取資料庫")
table_name = "animals"
show_data_base_contents(db_filename_animals, table_name)

conn = sqlite3.connect(db_filename_animals)  # 建立資料庫連線
cursor = conn.cursor()  # 建立 cursor 物件

# 查詢資料
cursor = conn.execute("SELECT * FROM animals")
rows = cursor.fetchall()  # 讀取全部資料成元組串列
print(rows)

# cursor.description 包含 欄位資訊
print("cursor.description")
print(cursor.description)

print("資料庫轉df")  # 用資料庫的資料建立 DataFrame
df = pd.DataFrame(rows, columns=[f[0] for f in cursor.description])
print("df")
print(df)

print("讀取資料轉df, 讀取全部資料")
df = pd.read_sql("SELECT * FROM animals", conn)
print("df")
print(df)

conn.commit()  # 更新
conn.close()  # 關閉資料庫連線

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("csv 轉 sqlite")

csv_filename = "D:/_git/vcs/_4.python/write_read_file/_3.csv/data/animals.csv"
db_filename = (
    "tmp_db06_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + "_csv.sqlite"
)

df = pd.read_csv(csv_filename)
df.columns = df.columns.str.strip()

conn = sqlite3.connect(db_filename)  # 建立資料庫連線
df.to_sql("animals", conn, if_exists="replace")
# df.to_sql("animals", conn)
conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料轉df")

conn = sqlite3.connect(db_filename)  # 建立資料庫連線

print("讀取資料轉df 1, 讀取3筆資料")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn)
print(df)

print("讀取資料轉df 2, 讀取3筆資料, 依體重排序(預設升冪)")
df = pd.read_sql("SELECT * FROM animals ORDER BY 體重 LIMIT 3", conn)
print(df)

print("讀取資料轉df 3, 讀取3筆資料")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn, index_col="index")
print(df)

print("讀取資料轉df 4")
df = pd.read_sql("SELECT * FROM animals LIMIT 3", conn, index_col=["index", "英文名"])
print(df)

print("讀取資料轉df 5")
df = pd.read_sql_query("SELECT * FROM animals;", conn)
print(df.head())

print("讀取資料轉df 6")
df = pd.read_sql_query("SELECT * FROM animals WHERE 體重>25;", conn)
print(df)

print("讀取資料轉df 7")
df = pd.read_sql_query('SELECT * FROM animals WHERE 中文名="跳跳虎";', conn)
print(df)

conn.close()  # 關閉資料庫連線

print("------------------------------")  # 30個

print("讀取資料庫")
table_name = "animals"
show_data_base_contents(db_filename, table_name)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# SQL语句介绍

sale = pd.read_csv("data/sale.csv", encoding="gbk")
cc = sale.head()
print(cc)

# SQL数据过滤与排序
# 选择表中指定列

conn = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", conn)  # 将DataFrame注册成可用sql查询的表

newTable = pd.read_sql_query(
    "SELECT year, market, sale, profit FROM sale", conn
)  # 也可使用read_sql
cc = newTable.head()
print(cc)

# 选择表中所有列

sqlResult = pd.read_sql_query("SELECT * FROM sale", conn)
cc = sqlResult.head()
print(cc)

# 删除重复的行

pd.read_sql_query("SELECT DISTINCT  year FROM sale", conn)

# 选择满足条件的行

pd.read_sql_query("SELECT * FROM sale WHERE year=2012 and market='东'", conn)

# 对行进行排序

sql = """SELECT year, market, sale, profit
      FROM sale
      order by year"""
pd.read_sql_query(sql, conn)


# 4.2纵向连接表

# sql操作

one = pd.read_csv("data/One.csv")
one.to_sql("One", conn, index=False)
print(one.T)

two = pd.read_csv("data/Two.csv")
two.to_sql("Two", conn, index=False)
print(two.T)

# union 和 union all

union = pd.read_sql("SELECT * FROM one UNION SELECT * FROM two", conn)
union_all = pd.read_sql("SELECT * FROM one UNION ALL SELECT * FROM two", conn)
print(union.T)

print(union_all.T)

# except 和 intersect

exceptTable = pd.read_sql("SELECT * FROM one EXCEPT SELECT * FROM two", conn)
intersectTable = pd.read_sql("SELECT * FROM one INTERSECT SELECT * FROM two", conn)
print(exceptTable.T)

print(intersectTable.T)

# *练习： 多表纵向连接

# DataFrame操作

cc = pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助
print(cc)

# 4.3 横向连接表

# sql操作

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", conn, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("data/Table2.csv")
table2.to_sql("table2", conn, index=False)
cc = table2.head()
print(cc)

# 笛卡尔积

pd.read_sql("SELECT * FROM table1, table2", conn)

# 内连接（使用inner join或使用where子句）

pd.read_sql("SELECT * FROM table1 as a inner join table2 as b on a.id=b.id", conn)
# pd.read_sql("SELECT * FROM table1 as a, table2 as b WHERE a.id=b.id", conn)

# 左连接

pd.read_sql("SELECT * FROM table1 as a left join table2 as b on a.id=b.id", conn)

# DataFrame操作

pd.merge(table1, table2, on="id", how="left")  # 参数设置可查看帮助

# 按索引连接

table1.join(table2, how="outer", lsuffix="t1", rsuffix="t2")  # 参数设置可查看帮助

# 4.4 数据清洗

# 发现数据问题类型

camp = pd.read_csv("data/teleco_camp_orig.csv")
cc = camp.head()
print(cc)

# 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20)
# Try this: accepts['purch_price'].plot(kind='hist')
# And this: sns.histplot(accepts['purch_price'], kde=True, fit=stats.norm)
# should scipy.stats first
show()

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

# df存檔 camp.to_csv("tmp_tele_camp_ok.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗

# ## 5.1 SQL语句介绍

# SQL2数据过滤与排序
# 选择表中指定列

sale = pd.read_csv("data/sale.csv", encoding="gbk")

conn = sqlite3.connect(":memory:")  # 数据库连接
sale.to_sql("sale", conn)  # 将DataFrame注册成可用sql查询的表
newTable = pd.read_sql_query(
    "SELECT year, market, sale, profit FROM sale", conn
)  # 也可使用read_sql
cc = newTable.head()
print(cc)

# 选择表中所有列

sqlResult = pd.read_sql_query("SELECT * FROM sale", conn)
cc = sqlResult.head()
print(cc)

# 删除重复的行

pd.read_sql_query("SELECT DISTINCT  year FROM sale", conn)

# 选择满足条件的行

pd.read_sql_query("SELECT * FROM sale WHERE market in ('东','西') and year=2012", conn)

# 对行进行排序

sql = """SELECT year, market, sale, profit
      FROM sale
      order by  sale desc"""
pd.read_sql_query(sql, conn)

# ## 5.2纵向连接表
# sql操作

one = pd.read_csv("data/One.csv")
one.to_sql("One", conn, index=False)
one.T

two = pd.read_csv("data/Two.csv")
two.to_sql("Two", conn, index=False)
two.T

# union 和 union all

union = pd.read_sql("SELECT * FROM one UNION SELECT * FROM two", conn)
union_all = pd.read_sql("SELECT * FROM one UNION ALL SELECT * FROM two", conn)
union.T

union_all.T

# except 和 intersect

exceptTable = pd.read_sql("SELECT * FROM one EXCEPT SELECT * FROM two", conn)
intersectTable = pd.read_sql("SELECT * FROM one INTERSECT SELECT * FROM two", conn)
exceptTable.T

intersectTable.T

# *练习： 多表纵向连接

# DataFrame操作

pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助

# ## 5.3 横向连接表
# sql操作

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", conn, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("data/Table2.csv")
table2.to_sql("table2", conn, index=False)
cc = table2.head()
print(cc)

# 笛卡尔积

pd.read_sql("SELECT * FROM table1, table2", conn)

# 内连接（使用inner join或使用where子句）

pd.read_sql("SELECT * FROM table1 as a inner join table2 as b on a.id=b.id", conn)
# pd.read_sql("SELECT * FROM table1 as a, table2 as b WHERE a.id=b.id", conn)

# 左连接

pd.read_sql("SELECT * FROM table1 as a left join table2 as b on a.id=b.id", conn)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("done")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
