"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import datetime
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

import ssl

ssl._create_default_https_context = ssl._create_stdlib_context

import warnings

warnings.filterwarnings("once")

print("------------------------------------------------------------")  # 60個

import sklearn.metrics as metrics
import statsmodels.api as sm


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
# 日期时间

now = time.strptime("2016-07-20", "%Y-%m-%d")
print(now)

type(now)

cc = time.strftime("%Y-%m-%d", now)
print(cc)

someDay = datetime.date(1999, 2, 10)
anotherDay = datetime.date(1999, 2, 15)
deltaDay = anotherDay - someDay
print(deltaDay.days)

date_formate = "%Y-%m-%d"  # year-month-day
cc = time.strptime("2016-06-22", date_formate)
print(cc)

# 复数complex

cplx = (4 + 2j) * (3 + 0.2j)
print(cplx)


# ## 3.2 Python数据结构
# 列表（list）、元组（tuple）、集合（set）、字典（dict）

# 3.2.1 列表(list)

# 用来存储一连串元素的容器，列表用[]来表示，其中元素的类型可不相同。

students = ["ming", "hua", "li", "juan", "yun", 3]
print(students)

# 插入元素
students.append("han")  # 添加到尾部
students.extend(["long", "wan"])
print(students)

scores = [90, 80, 75, 66]
students.insert(1, scores)  # 添加到指定位置
print(students)

# 删除元素

print(students.pop(1))  # 该函数返回被弹出的元素，不传入参数则删除最后一个元素
print(students)

# 判断元素是否在列表中等

print("wan" in students)
print("han" not in students)

students.count("wan")

students.index("wan")

# 集合

studentsSet = set(students)
print(studentsSet)

studentsSet.add("xu")
print(studentsSet)

studentsSet.remove("xu")
print(studentsSet)

a = set("abcnmaaaaggsng")
print("a=", a)
b = set("cdfm")
print("b=", b)

# 交集
x = a & b
print("x=", x)
# 并集
y = a | b
print("y=", y)
# 差集
z = a - b
print("z=", z)
# 去除重复元素
new = set(a)
print(z)

k = {"name": "weiwei", "home": "guilin"}
print(k["home"])
print(k.keys())
print(k.values())

a = {
    "success": True,
    "reason_code": "200",
    "reason_desc": "获取成功",
    "rules": [
        {
            "rule_id": "1062274",
            "score": 7,
            "conditions": [
                {
                    "address_a_value": "南通市",
                    "address_a": "mobile_address",
                    "address_b": "true_ip_address",
                    "address_b_value": "南京市",
                    "type": "match_address",
                }
            ],
        }
    ],
}
print(a["success"])


# 添加、修改字典里面的项目

k["like"] = "music"
k["name"] = "guangzhou"
print(k)

# 2.2.5 列表、元组、集合、字典的互相转换

tuple(students)
list(k)

zl = zip(("A", "B", "C"), [1, 2, 3, 4])  # zip可以将列表、元组、集合、字典‘缝合’起来
print(zl)
print(type(zl))
print(dict(zl))

heights = {"Yao": 226, "Sharq": 216, "AI": 183}
for i in heights:
    print(i, heights[i])

# for key, value in heights.items():-Python3 不能使用dict.iteritems(),改为dict.items()
for key, value in heights.items():
    print(key, value)


# 匿名函数：高阶函数传入函数时，不需要显式地定义函数，直接传入匿名函数更方便
f = lambda x: x * x
f(4)

df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
cc = df.head(2)
print(cc)

df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
cc = df1.head(5)
print(cc)

df2 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "a", "b"], "data1": range(7)})
cc = pd.crosstab(df2.key, df2.data1)
print(cc)

# ## 3.6 使用pandas读写数据

# pandas可以读取文本文件、json、数据库、Excel等文件
# 使用read_csv方法读取以逗号分隔的文本文件作为DataFrame，其它还有类似read_table, read_excel, read_html, read_sql等等方法

one = pd.read_csv("data/One.csv", sep=",")  # same
one = pd.read_csv("data/One.csv")
cc = one.head()
print(cc)

hsb2 = pd.read_table("data/hsb2.txt")
cc = hsb2.head()
print(cc)

html = pd.read_html(
    "http://www.fdic.gov/bank/individual/failed/banklist.html"
)  # Return a list
print(html)

# xls = pd.read_excel('hsb2.xlsx', sheetname=0) NG
xls = pd.read_excel("data/hsb2.xlsx")
cc = xls.head()
print(cc)

# df存檔  xls.to_csv("tmp_copyofhsb2.csv")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
第4讲 描述性统计分析基础

    数据集描述与属性说明
    ID 客户编号
    Suc_flag 成功入网标识
    ARPU 入网后ARPU
    PromCnt12 12个月内的营销次数
    PromCnt36 36个月内的营销次数
    PromCntMsg12 12个月内发短信的次数
    PromCntMsg36 36个月内发短信的次数
    Class 客户重要性等级(根据前运营商消费情况)
    Age 年龄
    Gender 性别
    HomeOwner 是否拥有住房
    AvgARPU 当地平均ARPU
    AvgHomeValue 当地房屋均价
    AvgIncome 当地人均收入
"""

# 读取数据
camp = pd.read_csv("data/teleco_camp2.csv")

# 数据预处理
camp.dtypes

camp.describe(include="all")

camp["Suc_flag"] = camp["Suc_flag"].astype("category")
camp["Class"] = camp["Class"].astype("category")

# 3.1 描述性统计与探索型数据分析

# 1.分类变量分析

cc = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
print(cc)

# 2.连续变量分析
# 2.1.数据的集中趋势 ARPU的均值与中位数

fs = camp["ARPU"]  # 可以使用camp.ARPU
type(fs)

print("mean = %6.4f" % fs.mean())  # 求fs的均值
print("median = %6.4f" % fs.median())  # 求fs的中位数
print("quantiles\n", fs.quantile([0.25, 0.5, 0.75]))  # 求a的上下四分位数与中位数

fs.plot(kind="hist")
show()

# 2.2.数据的离散程度

# print ('mad = %6.4f' %fs.mad())      # 求平均绝对偏差 mad = np.abs(fs - fs.mean()).mean()
print("range = %6.4f" % (fs.max(skipna=True) - fs.min(skipna=True)))  # 求极差
print("var = %6.4f" % fs.var())  # 求方差
print("std = %6.4f" % fs.std())  # 求标准差

# 2.3.数据的偏度与峰度- ARPU:右偏

plt.hist(fs.dropna(), bins=15)
show()

print("skewness = %6.4f" % fs.skew(skipna=True))
print("kurtosis = %6.4f" % fs.kurt(skipna=True))
"""
#2.4.分布- 正态分布模拟函数

from scipy import stats

x = map(lambda x: x / 10., range(-40, 41))
norm = stats.norm.pdf(x, loc=0, scale=1) # 随机正态分布概率密度(均值为0，标准差为1)
plt.plot(x, norm)
show()

points = map(lambda x: x / 10.0, range(-40, 41))
plt.plot(points, stats.norm.cdf(points,loc=0, scale=1)) # 正态分布函数
show()

#卡方分布模拟

x = range(1, 31)
chi = stats.chi2.pdf(x, df=3, loc=0, scale=1) #生成自由度为3的卡方分布概率密度
plt.plot(x, chi)
show()

#t分布模拟

x = np.arange(-4, 4, 0.1)
student_t = stats.t.pdf(x, df=5, loc=0, scale=1)#生成自由度为5的t分布的概率密度值
norm = stats.norm.pdf(x, loc=0, scale=1)
plt.plot(x, student_t, 'b-')
plt.plot(x, norm, 'r--')
show()
"""
# 3.2 apply\map\groupby及其它相关

data = pd.DataFrame(data={"a": range(1, 11), "b": np.random.randn(10)})
data.T

data.apply(np.mean)  # 等价于data.mean()，是其完整形式

data.apply(lambda x: x.astype("str")).dtypes  # DataFrame没有astype方法，只有Series有

(data["a"] - data["a"].mean()) / data["a"].std()

data["a"].map(
    lambda x: (x - data["a"].mean()) / data["a"].std()
)  # 等价于(data['a']- data['a'].mean()) / data['a'].std()

data["a"].map(lambda x: int(str(x), base=16))  # 不支持“广播”时，可以使用map进行函数映射

# 分组-应用/聚合

key = [1, 2] * 5
print(key)

group1, group2 = data.groupby(key)  # 使用groupby可按照‘key’进行分组，‘key’需与待分组数据有同样长度
print(group1)
print(group2)

data.groupby(key).aggregate(np.mean)
# 聚合函数在各分组中进行聚合，是data.groupby(key).mean()的完整形式，可传入函数或字符串(sum/mean/median/std/var等)，也可传入列表

data.groupby(key).agg({"a": "sum", "b": "count"})  # agg可以在多列上使用不同的聚合函数

data.groupby(key).transform(np.mean)  # 转换函数可在各分组内进行运算，将结果广播到原数据中

data.groupby(key).apply(np.mean)  # apply是一般化的‘分组-应用/聚合’函数，更灵活地实现aggregate或transform的功能

# *练习：对camp数据集，按照客户级别汇总ARPU

camp["ARPU"].groupby(camp["Class"]).apply(lambda x: x.describe())

camp[["PromCnt12", "PromCnt36"]].groupby(camp["Suc_flag"]).mean()

# crosstab 和pivot_table

pd.crosstab(camp.Suc_flag, camp.Class)

camp.pivot_table(
    ["PromCnt12", "PromCnt36"], index="Suc_flag", columns="Class", aggfunc=np.mean
)  # index、columns、aggfunc参数均可传入列表

# 3.3绘图

# 散点图

camp.plot(x="AvgARPU", y="ARPU", kind="scatter")  # 散点图
plt.text(60, 1100, "ARPU VS AvgARPU")  # 加标签
show()

# 柱图/条形图、折线图

data.b.plot(kind="bar")  # 柱图
show()

data.b.plot(kind="line")  # 折线图
show()

# 直方图

camp[["PromCnt12", "PromCnt36"]].plot(stacked=False, kind="hist", alpha=0.3, bins=20)
camp[["PromCnt12", "PromCnt36"]].hist(alpha=0.8, bins=20, figsize=(10, 2))

# 饼图

gb = camp["Suc_flag"].groupby(camp["Suc_flag"]).count()
gb.plot(
    kind="pie",
    labels=["Yes", "No"],
    colors=["r", "g"],
    autopct="%.2f",
    fontsize=20,
    figsize=(6, 6),
)
show()

# 箱线图

camp[["PromCnt12", "Suc_flag"]].boxplot(by="Suc_flag")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def stack2dim(raw, i, j, rotation=0, location="upper right"):
    """
    此函数是为了画两个维度标准化的堆积柱状图
    raw为pandas的DataFrame数据框
    i、j为两个分类变量的变量名称，要求带引号，比如"school"
    rotation：水平标签旋转角度，默认水平方向，如标签过长，可设置一定角度，比如设置rotation = 40
    location：分类标签的位置，如果被主体图形挡住，可更改为'upper left'
    """
    data_raw = pd.crosstab(raw[i], raw[j])
    data = data_raw.div(data_raw.sum(1), axis=0)  # 交叉表转换成比率，为得到标准化堆积柱状图

    # 计算x坐标，及bar宽度
    createVar = locals()
    x = [0]  # 每个bar的中心x轴坐标
    width = []  # bar的宽度
    k = 0
    for n in range(len(data)):
        # 根据频数计算每一列bar的宽度
        createVar["width" + str(n)] = list(data_raw.sum(axis=1))[n] / sum(
            data_raw.sum(axis=1)
        )
        width.append(createVar["width" + str(n)])
        if n == 0:
            continue
        else:
            k += (
                createVar["width" + str(n - 1)] / 2
                + createVar["width" + str(n)] / 2
                + 0.05
            )
            x.append(k)

    # 以下是通过频率交叉表矩阵生成一串对应堆积图每一块位置数据的数组，再把数组转化为矩阵
    y_mat = []
    n = 0
    y_level = len(data.columns)
    for p in range(data.shape[0]):
        for q in range(data.shape[1]):
            n += 1
            y_mat.append(data.iloc[p, q])
            if n == data.shape[0] * data.shape[1]:
                break
            elif n % y_level != 0:
                y_mat.extend([0] * (len(data) - 1))
            elif n % y_level == 0:
                y_mat.extend([0] * len(data))

    y_mat = np.array(y_mat).reshape(-1, len(data))
    y_mat = pd.DataFrame(y_mat)  # bar图中的y变量矩阵，每一行是一个y变量

    # 通过x，y_mat中的每一行y，依次绘制每一块堆积图中的每一块图

    from matplotlib import cm

    cm_subsection = [level for level in range(y_level)]
    colors = [cm.Pastel1(color) for color in cm_subsection]

    bottom = [0] * y_mat.shape[1]
    createVar = locals()
    for row in range(len(y_mat)):
        createVar["a" + str(row)] = y_mat.iloc[row, :]
        color = colors[row % y_level]

        if row % y_level == 0:
            bottom = bottom = [0] * y_mat.shape[1]
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    width=width[math.floor(row / y_level)],
                    color=color,
                )
        else:
            if math.floor(row / y_level) == 0:
                label = data.columns.name + ": " + str(data.columns[row])
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    label=label,
                    color=color,
                )
            else:
                plt.bar(
                    x,
                    createVar["a" + str(row)],
                    bottom=bottom,
                    width=width[math.floor(row / y_level)],
                    color=color,
                )

        bottom += createVar["a" + str(row)]

    plt.title(j + " vs " + i)
    group_labels = [str(name) for name in data.index]
    plt.xticks(x, group_labels, rotation=rotation)
    plt.ylabel(j)
    plt.legend(shadow=True, loc=location)
    show()


# # 一、使用sndHsPr

import matplotlib

# get_ipython().magic('matplotlib inline')

snd = pd.read_csv("data/sndHsPr.csv")

snd["all_pr2"] = snd[["price", "AREA"]].apply(lambda x: x[0] * x[1], axis=1)
cc = snd.head()
print(cc)

# 1、把dist變量重新編碼為中文，比如chaoyang改為朝陽區。1）先作頻次統計，然后繪制柱形圖圖展現每個區樣本的數量；

# 把dist變量重新編碼為中文，比如chaoyang改為朝陽區。

district = {
    "fengtai": "豐臺區",
    "haidian": "海淀區",
    "chaoyang": "朝陽區",
    "dongcheng": "東城區",
    "xicheng": "西城區",
    "shijingshan": "石景山區",
}
snd["district"] = snd.dist.map(district)
# snd_new = snd.drop('dist',axis = 1)
cc = snd.head()
print(cc)

# 4.1 描述性統計與探索型數據分析
# 1單因子頻數:描述名義變量的分布

# snd.dist.value_counts()
snd.district.value_counts()
# type(snd.district.value_counts())
# snd.district.value_counts()/snd.district.count()

snd.district.value_counts().plot(kind="bar")
# snd.district.value_counts().plot(kind = 'pie')

# 2 單變量描述:描述連續變量的分布

snd.price.mean()

snd.price.median()

snd.price.std()

snd.price.skew()

snd.price.agg(["mean", "median", "sum", "std", "skew"])

snd.price.quantile([0.01, 0.5, 0.99])

snd.price.hist(bins=40)

# 4.2 描述統計方法大全
# 1.1表分析

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch

pd.crosstab(snd.dist, snd.subway).plot(kind="bar")

# pd.crosstab(snd.district,snd.school).plot(kind = 'bar')
t1 = pd.crosstab(snd.district, snd.school)
t1.plot(kind="bar", stacked=True)
type(t1)

sub_sch = pd.crosstab(snd.district, snd.school)
sub_sch["sum1"] = sub_sch.sum(1)
cc = sub_sch.head()
print(cc)

sub_sch = sub_sch.div(sub_sch.sum1, axis=0)
sub_sch

sub_sch[[0, 1]].plot(kind="bar", stacked=True)

# stack2dim(snd, i="district", j="school")

# from pyecharts import Map

# from echarts-china-cities-pypkg import *
"""
官網給的解釋如下：
自從 0.3.2 開始，為了縮減項目本身的體積以及維持 pyecharts 項目的輕量化運行，pyecharts 將不再自帶地圖 js 文件。如用戶需要用到地圖圖表，可自行安裝對應的地圖文件包。下面介紹如何安裝。
全球國家地圖: echarts-countries-pypkg (1.9MB): 世界地圖和 213 個國家，包括中國地圖
中國省級地圖: echarts-china-provinces-pypkg (730KB)：23 個省，5 個自治區
中國市級地圖: echarts-china-cities-pypkg (3.8MB)：370 個中國城市:https://github.com/echarts-maps/echarts-china-cities-js
pip install echarts-countries-pypkg
pip install echarts-china-provinces-pypkg
pip install echarts-china-cities-pypkg
別注明，中國地圖在 echarts-countries-pypkg 里。
"""
snd_price = list(
    zip(
        snd.price.groupby(snd.district).mean().index,
        snd.price.groupby(snd.district).mean().values,
    )
)

min_ = snd.price.groupby(snd.dist).mean().min()
max_ = snd.price.groupby(snd.dist).mean().max()

# ![北京房價](北京各區房價.png)

# 1.2 分類匯總
snd.price.groupby(snd.district).mean().plot(kind="bar")
show()

snd.price.groupby(snd.district).mean().sort_values(ascending=True).plot(kind="barh")
show()

sns.boxplot(x="district", y="price", data=snd)
show()

# 1.3 匯總表

snd.pivot_table(values="price", index="district", columns="school", aggfunc=np.mean)
show()

snd.pivot_table(
    values="price", index="district", columns="school", aggfunc=np.mean
).plot(kind="bar")
show()

# 1.4、兩個連續變量---使用area和price做散點圖，分析area是否影響單位面積房價

snd.plot.scatter(x="AREA", y="price")
show()

# 1.5 雙軸圖 需要導入GDP數據

# 按年度匯總GDP，并計算GDP增長率。繪制雙軸圖。GDP為柱子，GDP增長率為線。

gdp = pd.read_csv("data/gdp_gdpcr.csv", encoding="gbk")
cc = gdp.head()
print(cc)

x = list(gdp.year)
GDP = list(gdp.GDP)
GDPCR = list(gdp.GDPCR)
fig = plt.figure()

ax1 = fig.add_subplot(111)
ax1.bar(x, GDP)
ax1.set_ylabel("GDP")
ax1.set_title("GDP of China(2000-2017)")
ax1.set_xlim(2000, 2018)

ax2 = ax1.twinx()
ax2.plot(x, GDPCR, "r")
ax2.set_ylabel("Increase Ratio")
ax2.set_xlabel("Year")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''

print("------------------------------------------------------------")  # 60個
import sqlite3
print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# SQL语句介绍

sale = pd.read_csv("data/sale.csv", encoding="gbk")
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

one = pd.read_csv("data/One.csv")
one.to_sql("One", con, index=False)
print(one.T)

two = pd.read_csv("data/Two.csv")
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

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", con, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("data/Table2.csv")
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
# Pandas
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗
# pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# 数据整合

# 5.1.1 行列操作

# 1. 单列

sample = pd.DataFrame(np.random.randn(4, 5), columns=["a", "b", "c", "d", "e"])
sample

sample["a"]

sample.loc[:, "a"]

sample[["a"]]

# 2. 选择多行和多列
sample.iloc[0:2, 0:2]

# 3. 创建、删除列
sample["new_col1"] = sample["a"] - sample["b"]
sample

sample_new = sample.assign(
    new_col2=sample["a"] - sample["b"], new_col3=sample["a"] + sample["b"]
)
sample_new

sample.drop("a", axis=1)

# 条件查询

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 65, 67],
        "group": [1, 1, 1, 2, 1, 2],
    }
)
sample

# 单条件

# sample.score > 70
sample[sample.score > 70]

# 多条件

sample[(sample.score > 70) & (sample.group == 1)]


# 3. 使用query

# sample.query('score > 90')
sample.query("(group ==2) |(group == 1)")

# 4. 其他

# NG
# sample[sample["score"].between(70, 80, inclusive=True)]

sample[sample["name"].isin(["Bob", "Lindy"])]

sample[sample["name"].str.contains("[M]+")]

# 横向连接

df1 = pd.DataFrame({"id": [1, 2, 3], "col1": ["a", "b", "c"]})
df2 = pd.DataFrame({"id": [4, 3], "col2": ["d", "e"]})

# 1. 内连接

df1.merge(df2, how="inner", left_on="id", right_on="id")

# 2. 外连接

df1.merge(df2, how="left", on="id")

# 3. 行索引连接

df1 = pd.DataFrame({"id1": [1, 2, 3], "col1": ["a", "b", "c"]}, index=[1, 2, 3])
df2 = pd.DataFrame({"id2": [1, 2, 3], "col2": ["aa", "bb", "cc"]}, index=[1, 3, 2])

pd.concat([df1, df2], axis=1)
# df1.join(df2)

# 纵向合并

df1 = pd.DataFrame(
    {"id": [1, 1, 1, 2, 3, 4, 6], "col": ["a", "a", "b", "c", "v", "e", "q"]}
)
df2 = pd.DataFrame({"id": [1, 2, 3, 3, 5], "col": ["x", "y", "z", "v", "w"]})

pd.concat([df1, df2], ignore_index=True, axis=0)

pd.concat([df1, df2], ignore_index=True).drop_duplicates()

df3 = df1.rename(columns={"col": "new_col"})

pd.concat([df1, df3], ignore_index=True).drop_duplicates()

# 排序

# 1. 排序

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [98, 78, 87, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)

sample

sample.sort_values("score", ascending=False, na_position="last")

sample.sort_values(["group", "score"])

# 分组汇总

sample = pd.read_csv("data/sample.csv", encoding="gbk")
cc = sample.head()
print(cc)

sample.groupby("class")[["math"]].max()

sample.groupby(["grade", "class"])[["math"]].mean()

# NG sample.groupby(["grade"])["math", "chinese"].mean()

sample.groupby("class")["math"].agg(["mean", "min", "max"])

# NG df = sample.groupby(["grade", "class"])["math", "chinese"].agg(["min", "max"])
# df

# 拆分、堆叠列

table = pd.DataFrame(
    {
        "cust_id": [10001, 10001, 10002, 10002, 10003],
        "type": ["Normal", "Special_offer", "Normal", "Special_offer", "Special_offer"],
        "Monetary": [3608, 420, 1894, 3503, 4567],
    }
)

pd.pivot_table(table, index="cust_id", columns="type", values="Monetary")

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

pd.melt(
    table1,
    id_vars="cust_id",
    value_vars=["Normal", "Special_offer"],
    value_name="Monetary",
    var_name="TYPE",
)

# 赋值与条件赋值

# 1. 赋值

sample = pd.DataFrame(
    {
        "name": ["Bob", "Lindy", "Mark", "Miki", "Sully", "Rose"],
        "score": [99, 78, 999, 77, 77, np.nan],
        "group": [1, 1, 1, 2, 1, 2],
    }
)

sample.score.replace(999, np.nan)

sample.replace({"score": {999: np.nan}, "name": {"Bob": np.nan}})

# 2. 条件赋值


def transform(row):
    if row["group"] == 1:
        return "class1"
    elif row["group"] == 2:
        return "class2"


sample.apply(transform, axis=1)

sample.assign(class_n=sample.apply(transform, axis=1))

sample = sample.copy()
sample.loc[sample.group == 1, "class_n"] = "class1"
sample.loc[sample.group == 2, "class_n"] = "class2"

print("------------------------------------------------------------")  # 60個
# SQL
print("------------------------------------------------------------")  # 60個

# # 第5章 数据整合和数据清洗

# ## 5.1 SQL语句介绍

# SQL2数据过滤与排序
# 选择表中指定列

sale = pd.read_csv("data/sale.csv", encoding="gbk")

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

pd.read_sql_query("select * from sale where market in ('东','西') and year=2012", con)

# 对行进行排序

sql = """select year, market, sale, profit
      from sale
      order by  sale desc"""
pd.read_sql_query(sql, con)

# ## 5.2纵向连接表
# sql操作

one = pd.read_csv("data/One.csv")
one.to_sql("One", con, index=False)
one.T

two = pd.read_csv("data/Two.csv")
two.to_sql("Two", con, index=False)
two.T

# union 和 union all

union = pd.read_sql("select * from one UNION select * from two", con)
union_all = pd.read_sql("select * from one UNION ALL select * from two", con)
union.T

union_all.T

# except 和 intersect

exceptTable = pd.read_sql("select * from one EXCEPT select * from two", con)
intersectTable = pd.read_sql("select * from one INTERSECT select * from two", con)
exceptTable.T

intersectTable.T

# *练习： 多表纵向连接

# DataFrame操作

pd.concat([one, two], axis=0, join="outer", ignore_index=True)  # 更多参数可查看文档或帮助

# ## 5.3 横向连接表
# sql操作

table1 = pd.read_csv("data/Table1.csv")
table1.to_sql("table1", con, index=False)
cc = table1.head()
print(cc)

table2 = pd.read_csv("data/Table2.csv")
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

print("------------------------------------------------------------")  # 60個
# cleaning
print("------------------------------------------------------------")  # 60個

# 数据整合和数据清洗

# 数据清洗

# 发现数据问题类型

camp = pd.read_csv("data/teleco_camp_orig.csv")
cc = camp.head()
print(cc)

# 脏数据或数据不正确

plt.hist(camp["AvgIncome"], bins=20, density=True)  # 查看分布情况
camp["AvgIncome"].describe(include="all")
show()

plt.hist(camp["AvgHomeValue"], bins=20, density=True)  # 查看分布情况
camp["AvgHomeValue"].describe(include="all")
show()

# 这里的0值应该是缺失值
camp["AvgIncome"] = camp["AvgIncome"].replace({0: np.NaN})
# 像这种外部获取的数据要比较小心，经常出现意义不清晰或这错误值。AvgHomeValue也有这种情况
plt.hist(
    camp["AvgIncome"],
    bins=20,
    density=True,
    range=(camp.AvgIncome.min(), camp.AvgIncome.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域

camp["AvgIncome"].describe(include="all")

camp["AvgHomeValue"] = camp["AvgHomeValue"].replace({0: np.NaN})

plt.hist(
    camp["AvgHomeValue"],
    bins=20,
    density=True,
    range=(camp.AvgHomeValue.min(), camp.AvgHomeValue.max()),
)  # 由于数据中存在缺失值,需要指定绘图的值域

camp["AvgHomeValue"].describe(include="all")

# 数据不一致-
# 这个问题需要详细的结合描述统计进行变量说明核对

# 数据重复

camp["dup"] = camp.duplicated()  # 生成重复标识变量
cc = camp.dup.head()
print(cc)

# 本数据没有重复记录，此处只是示例
camp_dup = camp[camp["dup"] == True]  # 把有重复的数据保存出来，以备核查
camp_nodup = camp[camp["dup"] == False]  # 注意与camp.drop_duplicates()的区别
cc = camp_nodup.head()
print(cc)

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

# 其他有缺失变量请自行填补，找到一个有缺失的分类变量，使用众数进行填补
# 多重插补：sklearn.preprocessing.Imputer仅可用于填补均值、中位数、众数，多重插补可考虑使用Orange、impute、Theano等包
# 多重插补的处理有两个要点：1、被解释变量有缺失值的观测不能填补，只能删除；2、只对放入模型的解释变量进行插补。

# 噪声值处理
# 盖帽法


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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3、對age按照5歲間隔分段，命名為age_group，用loss_flag對age_group作logit圖。

auto = pd.read_csv("data/auto_ins.csv", encoding="gbk")

auto.Loss = auto.Loss.map(lambda x: 1 if x > 0 else 0)

bins = [21, 26, 31, 36, 41, 46, 51, 56, 61, 67]
labels = [1, 2, 3, 4, 5, 6, 7, 8, 9]
auto["age_group"] = pd.cut(auto.Age, bins, labels=labels, right=False)

log_tab = pd.crosstab(auto.age_group, auto.Loss)
log_tab

log_tab[["p0", "p1"]] = log_tab[[0, 1]].apply(lambda x: x / sum(x))
log_tab["log"] = log_tab[["p1", "p0"]].apply(lambda x: np.log(x[0] / x[-1]), axis=1)
log_tab

log_tab.log.plot()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

# GBDT_ROC_KS_PR

from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.metrics as metrics

print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
model_data.head()

target = model_data["BROADBAND"]
orgData1 = model_data.ix[:, 1:-2]  # 所有 .ix[ 改成 .loc[



def metrics_roc(ts_real_Y, tr_real_Y, ts_pred_prob, tr_pred_prob):
    fpr_test, tpr_test, th_test = metrics.roc_curve(ts_real_Y, ts_pred_prob)
    fpr_train, tpr_train, th_train = metrics.roc_curve(tr_real_Y, tr_pred_prob)
    plt.figure(figsize=[3, 3])
    plt.plot(fpr_test, tpr_test, "b--")
    plt.plot(fpr_train, tpr_train, "r-")
    plt.title("ROC curve::Test is Blue")
    print("Test AUC = %.4f" % metrics.auc(fpr_test, tpr_test))
    print("Train AUC = %.4f" % metrics.auc(fpr_train, tpr_train))
    plt.show()


def metrics_pr(ts_real_Y, tr_real_Y, ts_pred_prob, tr_pred_prob):
    precision_test, recall_test, th_test = metrics.precision_recall_curve(
        ts_real_Y, ts_pred_prob
    )
    precision_train, recall_train, th_train = metrics.precision_recall_curve(
        tr_real_Y, tr_pred_prob
    )
    plt.figure(figsize=[3, 3])
    plt.plot(recall_test, precision_test, "b--")
    plt.plot(recall_train, precision_train, "r-")
    plt.title("precision-Recall curve:Test is Blue")
    print("Test AP = %.4f" % metrics.average_precision_score(ts_real_Y, ts_pred_prob))
    print("Train AP = %.4f" % metrics.average_precision_score(tr_real_Y, tr_pred_prob))
    plt.show()


# https://pypi.org/project/scikit-plot/0.3.4/
import scikitplot as skplt  # pip install scikit-plot


def plot_result(Y, pred, pred_proba):
    # 输出混淆矩阵
    skplt.metrics.plot_confusion_matrix(Y, pred)
    plt.show()
    # 输出roc曲线
    skplt.metrics.plot_roc_curve(Y, pred_proba, curves=("each_class"))
    plt.show()
    # 输出pr曲线
    skplt.metrics.plot_precision_recall_curve(Y, pred_proba, curves=("each_class"))
    plt.show()
    # 输出ks曲线
    skplt.metrics.plot_ks_statistic(Y, pred_proba)
    plt.show()


train_data, test_data, train_target, test_target = train_test_split(
    orgData1, target, test_size=0.2
)

# 决策树算法
param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = tree.DecisionTreeClassifier()
clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(train_data, train_target)

# 使用scikitplot
test_est = clfcv.predict(test_data)
# train_est = clfcv.predict(train_data)
y_predicted_probas = clfcv.predict_proba(test_data)
plot_result(test_target, test_est, y_predicted_probas)

# 使用sklearn.metrics
tr_pred_prob = clfcv.predict_proba(train_data)[:, 1]
ts_pred_prob = clfcv.predict_proba(test_data)[:, 1]
metrics_roc(test_target, train_target, ts_pred_prob, tr_pred_prob)

metrics_pr(test_target, train_target, ts_pred_prob, tr_pred_prob)

# GBDT
gbc = ensemble.GradientBoostingClassifier(
    learning_rate=0.1, max_depth=2, min_samples_split=20, n_estimators=100
)
gbc.fit(train_data, train_target)
# 使用scikitplot
test_est = gbc.predict(test_data)
y_predicted_probas = gbc.predict_proba(test_data)
plot_result(test_target, test_est, y_predicted_probas)

# 使用sklearn.metrics
tr_pred_prob = gbc.predict_proba(train_data)[:, 1]
ts_pred_prob = gbc.predict_proba(test_data)[:, 1]
metrics_roc(test_target, train_target, ts_pred_prob, tr_pred_prob)

metrics_pr(test_target, train_target, ts_pred_prob, tr_pred_prob)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
model_data.head()

target = model_data["BROADBAND"]
orgData1 = model_data.ix[:, 1:-2]  # 所有 .ix[ 改成 .loc[

from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import auc

from sklearn.utils.multiclass import unique_labels
import itertools


def plot_confusion_matrix(
    y_true,
    y_pred,
    cmap="Blues",
    title="Confusion Matrix",
    title_fontsize="large",
    text_fontsize="medium",
):
    """
    args:
        y_true: target values in test
        y_pred: prediction values
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    classes = unique_labels(y_true, y_pred)

    fig, ax = plt.subplots(1, 1, figsize=None)
    cm = confusion_matrix(y_true, y_pred)

    ax.set_title(title, fontsize=title_fontsize)
    # Display an image on the axes
    image = ax.imshow(cm, interpolation="nearest", cmap=plt.cm.get_cmap(cmap))
    plt.colorbar(mappable=image)
    x_tick_marks = np.arange(len(classes))
    y_tick_marks = np.arange(len(classes))
    # Set the x ticks with list of ticks
    ax.set_xticks(x_tick_marks)
    # Set the x-tick labels with list of string labels
    ax.set_xticklabels(classes, fontsize=text_fontsize)
    ax.set_yticks(y_tick_marks)
    ax.set_yticklabels(classes, fontsize=text_fontsize)

    thresh = cm.max() / 2.0
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if cm[i, j] != 0:
            ax.text(
                j,
                i,
                cm[i, j],
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=text_fontsize,
                color="white" if cm[i, j] > thresh else "black",
            )

    ax.set_ylabel("True label", fontsize=text_fontsize)
    ax.set_xlabel("Predicted label", fontsize=text_fontsize)
    return ax


def plot_roc_curve(
    y_true, y_probas, title="ROC Curves", title_fontsize="large", text_fontsize="medium"
):
    """
    args:
        y_true: target values in test
        y_probas: prediction probabilities
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    """
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    fig, ax = plt.subplots(1, 1, figsize=None)
    ax.set_title(title, fontsize=title_fontsize)

    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    for i in range(len(classes)):
        print("{0}: {1}".format(i, classes[i]))
        # pos_label: label considered as positive
        fpr[i], tpr[i], _ = roc_curve(y_true, probas[:, i], pos_label=classes[i])
        # compute the area under the curve
        roc_auc[i] = auc(fpr[i], tpr[i])
        ax.plot(
            fpr[i],
            tpr[i],
            lw=2,
            label="ROC curve of class {0} (area = {1:0.2f})"
            "".format(classes[i], roc_auc[i]),
        )
    ax.plot([0, 1], [0, 1], "k--", lw=2)
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel("False Positive Rate", fontsize=text_fontsize)
    ax.set_ylabel("True Positive Rate", fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc="lower right", fontsize=text_fontsize)
    return ax


def plot_pr_curve(
    y_true,
    y_probas,
    title="Precision-Recall Curves",
    title_fontsize="large",
    text_fontsize="medium",
):
    """
    args:
        y_true: target values in test
        y_probas: prediction probabilities
    return:
        ax: matplotlib.axes._subplots.AxesSubplot
    """
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    fig, ax = plt.subplots(1, 1, figsize=None)
    ax.set_title(title, fontsize=title_fontsize)

    precision_dict = dict()
    recall_dict = dict()

    for i in range(len(classes)):
        precision_dict[i], recall_dict[i], _ = precision_recall_curve(
            y_true, probas[:, i], pos_label=classes[i]
        )
        ax.plot(
            recall_dict[i],
            precision_dict[i],
            lw=2,
            label="Precision-recall curve of class {0} ".format(classes[i]),
        )
    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])
    ax.set_xlabel("Recall", fontsize=text_fontsize)
    ax.set_ylabel("Precision", fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc="best", fontsize=text_fontsize)
    return ax


def plot_ks_curve(
    y_true, y_probas, title="KS Curve", title_fontsize="large", text_fontsize="medium"
):
    y_true = np.array(y_true)
    probas = np.array(y_probas)

    classes = np.unique(y_true)

    thresholds, pct1, pct2, ks_value, max_distance_at = ks_curve(
        y_true, probas[:, 1].ravel()
    )

    fig, ax = plt.subplots(1, 1, figsize=None)

    ax.set_title(title, fontsize=title_fontsize)

    ax.plot(thresholds, pct1, lw=3, label="Class {}".format(classes[0]))
    ax.plot(thresholds, pct2, lw=3, label="Class {}".format(classes[1]))
    # get the index of max_distance_at
    idx = np.where(thresholds == max_distance_at)[0][0]
    # Add a vertical line across the axes
    ax.axvline(
        max_distance_at,
        *sorted([pct1[idx], pct2[idx]]),
        label="KS Statistic: {:.3f} at {:.3f}".format(ks_value, max_distance_at),
        linestyle=":",
        lw=3,
        color="black"
    )

    ax.set_xlim([0.0, 1.0])
    ax.set_ylim([0.0, 1.0])

    ax.set_xlabel("Threshold", fontsize=text_fontsize)
    ax.set_ylabel("Percentage below threshold", fontsize=text_fontsize)
    ax.tick_params(labelsize=text_fontsize)
    ax.legend(loc="lower right", fontsize=text_fontsize)

    return ax


def ks_curve(y_true, y_probas):
    y_true, y_probas = np.asarray(y_true), np.asarray(y_probas)
    idx = y_true == 0  # if target value is 0 then true else false
    data1 = np.sort(y_probas[idx])  # predicition probabilities which target value is 0
    data2 = np.sort(
        y_probas[np.logical_not(idx)]
    )  # predicition probabilities which target value is 1

    ctr1, ctr2 = 0, 0
    thresholds, pct1, pct2 = [], [], []
    while ctr1 < len(data1) or ctr2 < len(data2):
        # Check if data1 has no more elements
        if ctr1 >= len(data1):
            current = data2[ctr2]
            while ctr2 < len(data2) and current == data2[ctr2]:
                ctr2 += 1

        # Check if data2 has no more elements
        elif ctr2 >= len(data2):
            current = data1[ctr1]
            while ctr1 < len(data1) and current == data1[ctr1]:
                ctr1 += 1

        else:
            if data1[ctr1] > data2[ctr2]:
                current = data2[ctr2]
                while ctr2 < len(data2) and current == data2[ctr2]:
                    ctr2 += 1

            elif data1[ctr1] < data2[ctr2]:
                current = data1[ctr1]
                while ctr1 < len(data1) and current == data1[ctr1]:
                    ctr1 += 1

            else:
                current = data2[ctr2]
                while ctr2 < len(data2) and current == data2[ctr2]:
                    ctr2 += 1
                while ctr1 < len(data1) and current == data1[ctr1]:
                    ctr1 += 1

        thresholds.append(current)
        pct1.append(ctr1)
        pct2.append(ctr2)

    thresholds = np.asarray(thresholds)
    pct1 = np.asarray(pct1) / float(len(data1))  # fpr
    pct2 = np.asarray(pct2) / float(len(data2))  # tpr

    if thresholds[0] != 0:
        thresholds = np.insert(thresholds, 0, [0.0])
        pct1 = np.insert(pct1, 0, [0.0])
        pct2 = np.insert(pct2, 0, [0.0])
    if thresholds[-1] != 1:
        thresholds = np.append(thresholds, [1.0])
        pct1 = np.append(pct1, [1.0])
        pct2 = np.append(pct2, [1.0])

    differences = pct1 - pct2
    # np.argmax: Returns the indices of the maximum values along an axis
    ks_value, max_distance_at = np.max(differences), thresholds[np.argmax(differences)]

    return thresholds, pct1, pct2, ks_value, max_distance_at


def print_classification_report(y_true, y_pred):
    """
    args:
        y_true: target values in test
        y_probas: prediction values
    """
    print(metrics.classification_report(y_true, y_pred))


train_data, test_data, train_target, test_target = train_test_split(
    orgData1, target, test_size=0.2
)

# 决策树算法
param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = tree.DecisionTreeClassifier()
clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(train_data, train_target)

# 使用scikitplot
test_est = clfcv.predict(test_data)
# train_est = clfcv.predict(train_data)
y_predicted_probas = clfcv.predict_proba(test_data)
print("decision tree accuracy:")
print(metrics.classification_report(test_target, test_est))
print("decision tree AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)

# GBDT
param_grid = {
    "loss": ["deviance", "exponential"],
    "learning_rate": [0.1, 0.3, 0.5, 0.7, 1],
    "n_estimators": [10, 15, 20, 30],  # 决策树个数-GBDT特有参数
    "max_depth": [1, 2, 3],  # 单棵树最大深度-GBDT特有参数
    "min_samples_split": [2, 4, 8, 12, 16, 20],
}

gbc = ensemble.GradientBoostingClassifier()
gbccv = GridSearchCV(estimator=gbc, param_grid=param_grid, scoring="roc_auc", cv=4)
gbccv.fit(train_data, train_target)
test_est = gbccv.predict(test_data)
y_predicted_probas = gbccv.predict_proba(test_data)
print("gradient boosting accuracy:")
print(metrics.classification_report(test_target, test_est))
print("gradient boosting AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

gbccv.best_params_

plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)

# Adaboost算法
param_grid = {
    #'base_estimator':['DecisionTreeClassifier'],
    "learning_rate": [0.1, 0.3, 0.5, 0.7, 1]
}
abc = ensemble.AdaBoostClassifier(n_estimators=100, algorithm="SAMME")
abccv = GridSearchCV(estimator=abc, param_grid=param_grid, scoring="roc_auc", cv=4)
abccv.fit(train_data, train_target)
test_est = abccv.predict(test_data)
y_predicted_probas = abccv.predict_proba(test_data)
print("abc classifier accuracy:")
print(metrics.classification_report(test_target, test_est))
print("abc classifier AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

abccv.best_params_

plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)

# 随机森林
param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [7, 8, 10, 12],
    "n_estimators": [11, 13, 15],  # 决策树个数-随机森林特有参数
    "max_features": [0.2, 0.3, 0.4, 0.5],  # 每棵决策树使用的变量占比-随机森林特有参数
    "min_samples_split": [4, 8, 12, 16],
}

rfc = ensemble.RandomForestClassifier()
rfccv = GridSearchCV(estimator=rfc, param_grid=param_grid, scoring="roc_auc", cv=4)
rfccv.fit(train_data, train_target)
test_est = rfccv.predict(test_data)
y_predicted_probas = rfccv.predict_proba(test_data)
print("random forest accuracy:")
print(metrics.classification_report(test_target, test_est))
print("random forest AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, y_predicted_probas[:, 1])
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

rfccv.best_params_

plot_confusion_matrix(test_target, test_est)
plot_roc_curve(test_target, y_predicted_probas)
plot_pr_curve(test_target, y_predicted_probas)
plot_ks_curve(test_target, y_predicted_probas)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 查看一下关键字有哪些，避免关键字做自定义标识符
import keyword

print(keyword.kwlist)


# .ix改 .loc


# normed 改成 density

# In[19]:


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

