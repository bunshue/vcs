"""
Pandas繪圖 用matplotlib顯示

有以下類型的圖

折線圖df.plot()  # 無參數, 預設就是 line
柱狀圖df.plot(kind='bar')
橫向柱狀圖df.plot(kind='barh')
直方圖df.plot(kind='hist')
核密度(KDE)圖df.plot(kind='kde')
面積圖df.plot(kind='area')
圓餅圖df.plot(kind='pie')
散佈圖df.plot(kind='scatter')
六角形箱體圖df.plot(kind='hexbin')
箱形圖df.plot(kind='box')

print("折線圖")
df.plot(x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

df.plot(x="監測月份", y="PM10", title="監測月份與PM10的關係")

print("柱狀圖")
df.plot(kind="bar", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

print("橫向柱狀圖")
df.plot(kind="barh", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

print("直方圖")
df.plot(kind="hist", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

print("核密度(KDE)圖, 需要 scipy")
df.plot(kind="kde", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

print("面積圖")
df.plot(kind="area", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")

print("圓餅圖")
df.plot(kind="pie", x="監測月份", y="PM25", title="監測月份與PM2.5的關係", autopct="%1.2f%%")

print("散佈圖")
df.plot(kind="scatter", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值

print("六角形箱體圖")
df.plot(kind="hexbin", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值

print("箱形圖")
df.plot(kind="box", x="PM25", y="PM10", title="監測月份與PM2.5的關係")  # X,Y需為數值

df.plot(kind="line", title="線圖", figsize=[10, 5])
df.plot(kind="bar", title="長條圖", figsize=[10, 5])
df.plot(kind="barh", title="橫條圖", figsize=[10, 5])
df.plot(kind="bar", stacked=True, title="堆疊圖", figsize=[10, 5])
df.plot(kind="pie", subplots=True, figsize=[14, 6])

df["1st"].plot(kind="pie", title="Proportion of each area")
df["1st"].plot(kind="pie", colors=["red", "#00FF00", "blue", "yellow"])
df["1st"].plot(kind="pie", fontsize=12)
df["1st"].plot(kind="pie", figsize=(1, 1))
df["1st"].plot(kind="pie", figsize=(4, 4))
df["1st"].plot(kind="pie", autopct="%.2f")
df["1st"].plot(kind="pie", autopct="%.0f%%")

# 掌握分佈局勢的直方圖
df["第1次期中考"].plot(kind="bar")
df["第1次期中考"].plot(kind="hist", bins=10)

# 直方圖 hist
df["第1次平時考"].plot(kind="hist")
df["第1次平時考"].plot(kind="hist", bins=20)
df["第1次平時考"].plot(kind="hist", bins=40)
df["第1次平時考"].plot(kind="hist", color="blue", edgecolor="orange")

"""
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("DataFrame 畫圖")
print("------------------------------------------------------------")  # 60個


def make_data_frame_from_dict():
    datas = {
        "姓名": ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"],
        "國文": [92, 81, 81, 92],
        "英文": [89, 79, 82, 72],
        "數學": [71, 92, 89, 95],
        "社會": [88, 89, 98, 77],
        "自然": [95, 74, 89, 85],
    }
    df = pd.DataFrame(datas)
    return df


df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df.index = index

print("長條圖")
df.plot(kind="bar", title="長條圖", fontsize=12, rot=-15)
show()

print("線圖 為每個欄位畫一條線")
df.plot(title="線圖")  # 無參數, 預設就是 line
show()

print("線圖 只看一欄位")
df["英文"].plot()  # 無參數, 預設就是 line
show()

#df.plot.hist(y="lifespan", rot=45)  # rot表示xstick旋轉的角度

print("線圖 看一些欄位")
df[["英文", "數學"]].plot()  # 無參數, 預設就是 line
show()

# 取出2欄資料並畫出
df2 = df[["英文", "數學"]]
df2.plot()  # 無參數, 預設就是 line
show()

print("線圖 看一些欄位")
print("建立空的df, 再加入資料至df")
df2 = pd.DataFrame()
df2["英文"] = df["英文"]
df2["數學"] = df["數學"]
df2.index = df.index

df2.plot()  # 無參數, 預設就是 line
show()

print("------------------------------------------------------------")  # 60個

print("直方圖")

datas = np.random.randn(1000, 3)

df = pd.DataFrame(datas, columns=["A", "B", "C"])
df["A"] = df["A"] - 3
df["C"] = df["C"] + 3

#df.plot.hist(bins=30, alpha=0.3, title="直方圖") # same
df.plot(kind="hist", bins=30, alpha=0.3, title="直方圖")

#ax.set_xlabel("Xlabel")
#ax.set_title("直方圖")

show()

print("------------------------------------------------------------")  # 60個

print("核密度(KDE)圖, 需要 scipy")

N = 500
mu = 85
sigma = 20
datas1 = np.random.normal(mu, sigma, N)

mu = 65
sigma = 20
datas2 = np.random.normal(mu, sigma, N)

df = pd.DataFrame({"x": datas1,"y": datas2})
df.plot.kde()

show()

print("------------------------------------------------------------")  # 60個

print("箱圖")

datas = np.random.randn(10, 4)
columns = ["AAA", "BBB", "CCC", "DDD"]

df = pd.DataFrame(datas, columns=columns)

df.boxplot()

plt.title("箱圖")
show()

print("------------------------------------------------------------")  # 60個

print("箱圖")

df = pd.read_csv("data/iris.csv")

df.boxplot(column="sepal_length", by="target", figsize=(8, 6))

plt.title("箱圖")
show()

print("------------------------------------------------------------")  # 60個


dists = {
    "區名": [
        "中正區",
        "板橋區",
        "桃園區",
        "北屯區",
        "安南區",
        "三民區",
        "大安區",
        "永和區",
        "八德區",
        "前鎮區",
        "鳳山區",
        "信義區",
        "新店區",
    ],
    "人口": [
        159598,
        551452,
        441287,
        275207,
        192327,
        343203,
        309835,
        222531,
        198473,
        189623,
        359125,
        225561,
        302070,
    ],
    "面積": [
        7.6071,
        23.1373,
        34.8046,
        62.7034,
        107.2016,
        19.7866,
        11.3614,
        5.7138,
        33.7111,
        19.1207,
        26.7590,
        11.2077,
        120.2255,
    ],
}

df = pd.DataFrame(dists, columns=["人口", "面積"], index=dists["區名"])
# print(df)

df["面積"] *= 1000
df.plot(xticks=range(len(df.index)), use_index=True, rot=45, figsize=(8, 6))

plt.title("人口 / 面積")
show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/年度銷售金額.csv")
df.index = df["AREA"]
df = df.drop("AREA", axis=1)
print(df)

df["1st"].plot(kind="pie", autopct="%.2f%%")
plt.title("第一季")
show()

df.plot(kind="bar", rot=0)  # 旋轉X軸標籤角度
plt.title("年度 bar圖")
show()

df.plot(kind="barh")
plt.title("年度 barh圖")
show()

print("------------------------------------------------------------")  # 60個

# 折線圖

df = pd.read_csv("data/觀光人數統計.csv")
df.index = df["Month"]  # 自定列索引為Month內容
df = df.drop("Month", axis=1)  # 刪除原本的月份行資料
print(df)

# 折線圖 + 參數
df.plot(linewidth=2, linestyle=":", title="Number of visitors")
show()

# 三月 資料
df_T = df.T
print(df_T.head())

df3 = df_T[3]
df3.plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=["北部", "中部", "南部"],
    columns=[2015, 2016, 2017, 2018, 2019],
)

"""
g1 = df.plot(kind="bar", title="長條圖", figsize=[10, 5])
g2 = df.plot(kind="barh", title="橫條圖", figsize=[10, 5])
g3 = df.plot(kind="bar", stacked=True, title="堆疊圖", figsize=[10, 5])
"""

g4 = df.iloc[0].plot(
    kind="line",
    legend=True,
    xticks=range(2015, 2020),
    title="公司分區年度銷售表",
    figsize=[10, 5],
)
g4 = df.iloc[1].plot(kind="line", legend=True, xticks=range(2015, 2020))
g4 = df.iloc[2].plot(kind="line", legend=True, xticks=range(2015, 2020))
show()

# 派圖
df.plot(kind="pie", subplots=True, figsize=[16, 6])
show()

print("------------------------------------------------------------")  # 60個

# 散佈圖

N = 100
print("建立 N X 2 個 0-100(含) 的整數隨機數")
datas = np.random.randint(0, 100, size=(N, 2))
# print(datas)

columns = ["XXXX", "YYYY"]
df = pd.DataFrame(datas, columns=columns)
# print(df)
print("相關係數矩陣 :", df.corr())

# df.plot(kind="scatter", x="XXXX", y="YYYY")
df.plot(kind="scatter", x="XXXX", y="YYYY", title="Scatter Plot")

# 設定散佈圖X、Y軸的座標值
# df.plot(kind="scatter", x="XXXX", y="YYYY", xlim=(-20, 120), ylim=(-20, 120))

show()

print("------------------------------------------------------------")  # 60個

N = 100
xx = np.random.randint(0, 100, N)
yy = np.random.randint(0, 100, N)
cc = np.random.randint(0, 100, N)
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

df = pd.DataFrame({"XXXX": xx, "YYYY": yy, "COLOR": cc})

# scatter plot 1
# df.plot(kind="scatter", x="XXXX", y="YYYY", title="Scatter Plot")

# scatter plot 2 + 設定點的大小 + 顏色
df.plot.scatter(x="XXXX", y="YYYY", s=50, marker="*", c="COLOR", colormap="viridis")

# plt.title("Scatter Plot") same
show()

print("------------------------------------------------------------")  # 60個

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
name = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

print("建立空的df, 再加入資料至df")
df = pd.DataFrame()
df["name"] = name
df["weight"] = weight
print(df)
print(df["name"])
print(df["weight"])

df.index = df["name"]
df["weight"].plot(kind="line", title="線圖", fontsize=12)
df["weight"].plot(kind="bar", title="長條圖", fontsize=12)

# df["weight"].plot(kind="pie", autopct="%.0f%%", title = '派圖', fontsize = 12)

show()

print("------------------------------------------------------------")  # 60個

# Series的索引會被作為subplot的 X軸，可以使用參數 use_index = False 來禁用該功能
# X軸的刻度可以透過 xticks 和 xlim 選向來調整
# Y軸的刻度可以透過 yticks 和 ylim 選向來調整

N = 10
df = pd.DataFrame(
    np.random.randn(N, 5).cumsum(0),
    # index=np.arange(0, 100, N),
    index=list("ABCDEFGHIJ"),
    columns=["國文", "英文", "數學", "社會", "自然"],
)
print(df)

df.plot(title="DataFrame畫圖")  # 無參數, 預設就是 line
show()

# 柱狀圖
# 設定 kind = 'bar' 或 'barh' 即可繪製柱狀圖
# Series和 DataFrame的 索引會被當作subplot的 X軸(bar)或 Y軸(barh)

df = pd.DataFrame(
    np.random.rand(6, 4),
    index=["one", "two", "three", "four", "five", "six"],
    columns=pd.Index(["A", "B", "C", "D"], name="Genus"),
)
print(df)

# DataFrame的每一 row的值分為一組
# columns 索引的 name屬性 被用來做為 legend的標題
df.plot(kind="bar")

show()

# 設定 stacked = True, 可繪製 堆積柱狀圖
df.plot(kind="barh", stacked=True)
show()

print("------------------------------------------------------------")  # 60個

tips = pd.read_csv("data/tips.csv")
cc = tips[:5]
print(cc)

# 用 crosstab()方法創建一個 交叉表，預設統計 發生的次數(計數)
party_counts = pd.crosstab(tips.day, tips["size"])
print(party_counts)

party_counts.plot(kind="bar")
show()

""" NG
party_counts = party_counts.ix[:, 2:5]
party_counts.plot(kind = 'bar', stacked = True)
show()
"""

print(party_counts)

party_counts = party_counts.div(party_counts.sum(1), axis=0)
print(party_counts)

cc = party_counts.sum(1)
print(cc)

party_counts.plot(kind="bar", stacked=True)
show()

print("------------------------------------------------------------")  # 60個

# 直方圖(histogram)和密度圖

tips = pd.read_csv("data/tips.csv")
cc = tips[:5]
print(cc)

# 用 plot(kind = 'hist') 繪製直方圖
tips.total_bill.plot(kind="hist", bins=50)
plt.title("total_bill")
show()

# 用 hist() 繪製直方圖
tips.total_bill.hist(bins=50)
plt.title("total_bill")
show()

# tip比例 直方圖
tip_ratios = tips.tip / tips.total_bill
tip_ratios.hist(bins=50)
plt.title("tip ratio")
show()

print("------------------------------------------------------------")  # 60個

# 散佈圖(scatter plot)

macro = pd.read_csv("data/macrodata.csv")
cc = macro[:5]
print(cc)

data = macro[["cpi", "m1", "tbilrate", "unemp"]]
cc = data[:5]
print(cc)

# diff(): 以上下元素的差異值填入
trans_data = np.log(data).diff().dropna()
cc = trans_data[:5]
print(cc)

# plt.scatter()可以繪製散佈圖，標示每一個資料row的 兩個columns的數據分布
plt.scatter(trans_data.m1, trans_data.unemp)
plt.title("Changes in log({0}) vs. log({1})".format("m1", "unemp"))
show()

trans_data.plot.scatter("m1", "unemp")
show()

# pandas 提供了 scatter_matrix()函數，方便由DataFrame繪製散佈圖
from pandas.plotting import scatter_matrix

# 會自動的產生各個columns之間的 scatter diagram
_ = scatter_matrix(trans_data, color="k", alpha=0.3, figsize=(8, 8))

show()

print("------------------------------------------------------------")  # 60個

# pandas 提供了 scatter_matrix()函數，方便由DataFrame繪製散佈圖
from pandas.plotting import scatter_matrix

df = pd.DataFrame(np.random.rand(6, 4))
print(df)
# 會自動的產生各個columns之間的 scatter diagram
_ = scatter_matrix(df, color="k", alpha=0.3, figsize=(8, 8))

show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330_2019_9.csv")

print("建立空的df, 再加入資料至df")
data = pd.DataFrame()
data["Date"] = pd.to_datetime(df["Date"])
data["Adj Close"] = df["Adj Close"]
data["High"] = df["High"]
data["Low"] = df["Low"]
data = data.set_index("Date")

data.plot(kind="line")

show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/drinks.csv")
print(df)

df.set_index("Type", inplace=True)
df.plot(kind="bar")
df.plot(kind="barh")

show()

print("------------------------------------------------------------")  # 60個

print("pd 之 plot 之 scatter")

N = 1000
datas = np.random.randn(N, 2)

columns = list("AB")
index = np.arange(N)
df = pd.DataFrame(datas, columns=columns, index=index)
# print(df)

ax = df.plot.scatter(x="A", y="B", color="DarkBlue", label="Class 1")
# df.plot.scatter(x="A", y="B", color="LightGreen", label="Class 2", ax=ax)
show()

print("------------------------------------------------------------")  # 60個

N = 1000
N = 100
datas = np.random.randn(N, 4)

# print("建立 3x2 個0-9(含) 的整數隨機數")
# datas = np.random.randint(0, 10, size=(N, 4))
# print(datas)

columns = list("ABCD")
index = np.arange(N)
df = pd.DataFrame(datas, columns=columns, index=index)
# print(df)

# df = df.cumsum()#依欄位, 逐列累加
# print(df)

# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = df.plot.scatter(x="A", y="B", color="DarkBlue", label="Class 1")
# df.plot.scatter(x="A", y="C", color="LightGreen", label="Class 2", ax=ax)

df.plot.scatter(x="A", y="B", color="red", label="Class B", ax=ax)
df.plot.scatter(x="A", y="C", color="green", label="Class C", ax=ax)
df.plot.scatter(x="A", y="D", color="blue", label="Class D", ax=ax)

show()

print("------------------------------------------------------------")  # 60個

print("用plt畫pd資料")

print("只變更要強調的扇形的顏色")

datas = {"name": ["鼠", "牛", "虎", "兔", "龍"], "weight": [3, 48, 33, 8, 38]}
df = pd.DataFrame(datas)
print(df)

"""
# 要強調的扇形的標籤 
point_label = "虎" 
# 重點色 
point_color = "#CC0000"

# 調整特定標籤的顏色
palette = sns.color_palette("binary", len(df)) 
for i in df[df.name == point_label].index.values:
    palette[i] = point_color 

plt.pie(df["weight"], labels=df["name"],
        autopct="%1.1f%%", startangle=90, counterclock=False,
        colors=palette)

show()
"""

print("------------------------------------------------------------")  # 60個

# 1.初始化

pd.set_option("display.max_rows", 1000)  # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000)  # 設定最大能顯示1000columns

# 2.解決plot不能顯示中文問題
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 3.讀取檔案

df = pd.read_excel("data/2017_PM25.xlsx")

# 4.資料操作
# 4.1NaN與重複值處理

df = df.dropna()
df = df.drop_duplicates()

cc = df.head(30)
print(cc)

# 4.2檢視資料類型(有無非數值類型存在)

cc = df.dtypes
print(cc)

# 如果屬性是Object，如何改成數值屬性
# df["屬於Object的欄位"] = pd.to_numeric(df.屬於Object的欄位, errors='coerce')

"""
#相關係數
cc = df.corr()
print(cc)
"""
print("折線圖")

df.plot(x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

df.plot(x="監測月份", y="PM10", title="監測月份與PM10的關係")
show()

print("柱狀圖")
df.plot(kind="bar", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("橫向柱狀圖")
df.plot(kind="barh", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("直方圖")
df.plot(kind="hist", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

"""
print("核密度(KDE)圖")
df.plot(kind='kde',x='監測月份', y='PM25',title='監測月份與PM2.5的關係')
show()
"""

print("面積圖")
df.plot(kind="area", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("圓餅圖")
df.plot(kind="pie", x="監測月份", y="PM25", title="監測月份與PM2.5的關係", autopct="%1.2f%%")
show()

print("散佈圖")
df.plot(kind="scatter", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值
show()

print("六角形箱體圖")
df.plot(kind="hexbin", x="PM25", y="PM10", title="PM2.5與PM10的關係")  # X,Y需為數值
show()

print("箱形圖")
df.plot(kind="box", x="PM25", y="PM10", title="監測月份與PM2.5的關係")  # X,Y需為數值
show()

print("------------------------------")  # 30個

plt.title("用直方圖看PM25分佈")

sns.histplot(df["PM25"].dropna(), kde=False, bins=30)

show()

print("------------------------------")  # 30個

plt.title("用直方圖看Nox的分佈")

df["Nox"].hist(bins=30)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

tips = sns.load_dataset("tips")
cc = tips.head()
print(cc)

sns.histplot(tips["total_bill"])
show()

sns.histplot(tips["total_bill"], kde=False, bins=30)
show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")

sns.pairplot(tips)

sns.pairplot(tips, hue="sex", palette="coolwarm")

sns.kdeplot(tips["total_bill"])
sns.rugplot(tips["tip"])
show()


sns.barplot(x="sex", y="total_bill", data=tips, estimator=np.std)
show()

sns.countplot(x="sex", data=tips)
show()

sns.boxplot(x="day", y="total_bill", data=tips, hue="smoker")
show()

sns.violinplot(x="day", y="total_bill", data=tips, hue="sex", split=True)
show()

sns.stripplot(x="day", y="total_bill", data=tips, jitter=True, hue="sex", dodge=True)
show()

sns.violinplot(x="day", y="total_bill", data=tips)
sns.swarmplot(x="day", y="total_bill", data=tips, color="black")

show()

# catplot兩變量關係圖
sns.catplot(x="day", y="total_bill", data=tips, kind="bar")

tc = tips.corr()

sns.heatmap(tc, annot=True, cmap="coolwarm")

show()


""" NG
fp=flights.pivot_table(index='month',columns='year',values='passengers')

sns.heatmap(fp,cmap='magma',linecolor='white',linewidths=1)

show()

sns.clustermap(fp,cmap='coolwarm',standard_scale=1)

sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex',markers=['o','v'],scatter_kws={'s':100})

sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',aspect=1,size=4)
"""
iris = sns.load_dataset("iris")
cc = iris.head()
print(cc)

cc = iris["species"].unique()
print(cc)

# array(['setosa', 'versicolor', 'virginica'], dtype=object)

g = sns.PairGrid(iris)
g.map_diag(sns.distplot)
g.map_upper(plt.scatter)
g.map_lower(sns.kdeplot)

g = sns.FacetGrid(data=tips, col="time", row="smoker")

g.map(plt.scatter, "total_bill", "tip")

sns.set_style("ticks")
sns.countplot(x="sex", data=tips)

show()

sns.despine(left=True, bottom=True)

sns.countplot(x="sex", data=tips)

show()

sns.set_context("paper")
sns.countplot(x="sex", data=tips)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("日本各都市平均氣溫全年資料")

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"])
# print(df)

df.plot(kind="line", x="年月", y="東京-平均氣溫(℃)", title="東京", figsize=[10, 5])
df.plot(kind="line", x="年月", y="大阪-平均氣溫(℃)", title="大阪", figsize=[10, 5])

show()

print("------------------------------")  # 30個

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"], index_col=0)
df_average = df[["東京-平均氣溫(℃)", "大阪-平均氣溫(℃)", "那霸-平均氣溫(℃)", "函館-平均氣溫(℃)"]]
print(df_average)

# 在單一圖表繪製多張折線圖的範例

df_average.plot(kind="line")

# 適度調整標籤與圖例
plt.xticks(rotation=30)
plt.legend()

show()

print("------------------------------")  # 30個

# 將多張折線圖的折線設定為同一種類的範例

tmp_stack = (
    df_average.stack()
    .rename_axis(["年月", "category"])
    .reset_index()
    .rename(columns={0: "value"})
)
print(tmp_stack)

# 繪製折線圖
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette="pastel")

# 適度調整標籤與圖例
plt.xticks(rotation=30)
plt.legend()

show()

print("------------------------------")  # 30個

# 強調特定折線圖的範例
# sns.set(style="white", font="meiryo")
tmp_stack = (
    df_average.stack()
    .rename_axis(["年月", "category"])
    .reset_index()
    .rename(columns={0: "value"})
)
print(tmp_stack)

# 計算分類數量
num_category = len(tmp_stack["category"].unique())
# 設定顏色
point_color = "#CC0000"

# 要變更的分類的編號
point_number = 2

# 建立原始的調色盤
palette = sns.color_palette("gray_r", num_category)

# 變更調色盤的部分顏色
palette[point_number] = point_color

# 繪製折線圖
ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette=palette)

# 適度調整標籤與圖例
plt.xticks(rotation=30)
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("bikes ST")

broken_df = pd.read_csv("data/bikes.csv", encoding="ISO-8859-1")

# Look at the first 3 rows
print(broken_df[:3])

print("------------------------------------------------------------")  # 60個

fixed_df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
print(fixed_df[:3])

print(fixed_df["Berri 1"])

fixed_df["Berri 1"].plot()  # 無參數, 預設就是 line

show()


fixed_df.plot(figsize=(15, 10))

show()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
df["Berri 1"].plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

# Make the graphs a bit prettier, and bigger
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option("display.width", 5000)
pd.set_option("display.max_columns", 60)


bikes = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
bikes["Berri 1"].plot()  # 無參數, 預設就是 line
show()

berri_bikes = bikes[["Berri 1"]].copy()

berri_bikes[:5]

berri_bikes.index

berri_bikes.index.day

berri_bikes.index.weekday

berri_bikes.loc[:, "weekday"] = berri_bikes.index.weekday
berri_bikes[:5]

weekday_counts = berri_bikes.groupby("weekday").aggregate(sum)
weekday_counts

weekday_counts.index = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
weekday_counts

weekday_counts.plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

bikes = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
# Add the weekday column
berri_bikes = bikes[["Berri 1"]].copy()
berri_bikes.loc[:, "weekday"] = berri_bikes.index.weekday

# Add up the number of cyclists by weekday, and plot!
weekday_counts = berri_bikes.groupby("weekday").aggregate(sum)
weekday_counts.index = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
weekday_counts.plot(kind="bar")

show()

print("bikes SP")

print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (8, 3)
plt.rcParams["font.family"] = "sans-serif"

# Canada's weather data for 2012, and saved it to a CSV.
# Here's the temperature every hour for 2012!

df_2012 = pd.read_csv("data/weather_2012.csv", index_col="Date/Time")
df_2012["Temp (C)"].plot(figsize=(8, 4), rot=-10)

show()

print("------------------------------------------------------------")  # 60個

# Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

# To get the data for March 2013, we need to format it with month=3, year=2012.
# url = url_template.format(month=3, year=2012)
# df_mar_2012 = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, encoding='latin1', header=True)

# because the url is broken, we use our saved dataframe for now
df_mar_2012 = pd.read_csv("data/weather_2012.csv")

print(df_mar_2012)

df_mar_2012["Temp (C)"].plot(figsize=(15, 5))
show()

# '\xb0' for that degree character °
""" fail
df_mar_2012.columns = [
    u'Year', u'Month', u'Day', u'Time', u'Data Quality', u'Temp (C)', 
    u'Temp Flag', u'Dew Point Temp (C)', u'Dew Point Temp Flag', 
    u'Rel Hum (%)', u'Rel Hum Flag', u'Wind Dir (10s deg)', u'Wind Dir Flag', 
    u'Wind Spd (km/h)', u'Wind Spd Flag', u'Visibility (km)', u'Visibility Flag',
    u'Stn Press (kPa)', u'Stn Press Flag', u'Hmdx', u'Hmdx Flag', u'Wind Chill', 
    u'Wind Chill Flag', u'Weather']
"""

df_mar_2012 = df_mar_2012.dropna(axis=1, how="any")
print(df_mar_2012[:5])

print("------------------------------------------------------------")  # 60個

# fail
# df_mar_2012 = df_mar_2012.drop(['Year', 'Month', 'Day', 'Time', 'Data Quality'], axis=1)
# print(df_mar_2012[:5])

print("------------------------------------------------------------")  # 60個


# Plotting the temperature by hour of day

"""fail
temperatures = df_mar_2012[[u'Temp (C)']].copy()
print(temperatures.head)
temperatures.loc[:,'Hour'] = df_mar_2012.index.hour
temperatures.groupby('Hour').aggregate(np.median).plot()  # 無參數, 預設就是 line

show()
"""

print("------------------------------------------------------------")  # 60個

""" fail in reading csv data
#5.3 Getting the whole year of data

def download_weather_month(year, month):
    if month == 1:
        year += 1
    url = 'weather_2012.csv'
    weather_data = pd.read_csv(url, skiprows=15, index_col='Date/Time', parse_dates=True, header=True)
    weather_data = weather_data.dropna(axis=1)
    weather_data.columns = [col.replace('\xb0', '') for col in weather_data.columns]
    weather_data = weather_data.drop(['Year', 'Day', 'Month', 'Time', 'Data Quality'], axis=1)
    return weather_data


cc = download_weather_month(2012, 1)[:5]
print(cc)

data_by_month = [download_weather_month(2012, i) for i in range(1, 13)]

weather_2012 = pd.concat(data_by_month)
print(weather_2012)

#save to csv file
weather_2012.to_csv('tmp_weather_2012.csv')
"""
print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 3)
plt.rcParams["font.family"] = "sans-serif"

weather_2012 = pd.read_csv(
    "data/weather_2012.csv", parse_dates=True, index_col="Date/Time"
)
print(weather_2012[:5])

weather_description = weather_2012["Weather"]
is_snowing = weather_description.str.contains("Snow")

# Not super useful
print(is_snowing[:5])

# More useful!
is_snowing = is_snowing.astype(float)
is_snowing.plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

# Use resampling to find the snowiest month

# If we wanted the median temperature each month, we could use the resample() method like this:

weather_2012["Temp (C)"].resample("M").apply(np.median).plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float)[:10])

print("------------------------------------------------------------")  # 60個

print(is_snowing.astype(float).resample("M").apply(np.mean))

is_snowing.astype(float).resample("M").apply(np.mean).plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個

# Plotting temperature and snowiness stats together

temperature = weather_2012["Temp (C)"].resample("M").apply(np.median)
is_snowing = weather_2012["Weather"].str.contains("Snow")
snowiness = is_snowing.astype(float).resample("M").apply(np.mean)

# Name the columns
temperature.name = "Temperature"
snowiness.name = "Snowiness"

# We'll use concat again to combine the two statistics into a single dataframe.
stats = pd.concat([temperature, snowiness], axis=1)
print(stats)

stats.plot(kind="bar")
show()

# Uh, that didn't work so well because the scale was wrong. We can do better by plotting them on two separate graphs:

stats.plot(kind="bar", subplots=True, figsize=(15, 10))
show()

print("------------------------------------------------------------")  # 60個

# Make the graphs a bit prettier, and bigger
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"

# This is necessary to show lots of columns in pandas 0.12.
# Not necessary in pandas 0.13.
pd.set_option("display.width", 5000)
pd.set_option("display.max_columns", 60)

print("------------------------------------------------------------")  # 60個

"""
# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)

plt.rcParams['figure.figsize'] = (15, 5)

# because of mixed types we specify dtype to prevent any errors
csv_filename = 'C:/_git/vcs/_big_files/311-service-requests.csv'
complaints = pd.read_csv(csv_filename, dtype='unicode')

print(complaints)
complaints['Complaint Type']

complaints['Complaint Type'].value_counts()

complaint_counts = complaints['Complaint Type'].value_counts()
complaint_counts[:10]

complaint_counts[:10].plot(kind='bar')
show()

print('------------------------------------------------------------')	#60個

# Make the graphs a bit prettier, and bigger
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (15, 5)

# This is necessary to show lots of columns in pandas 0.12. 
# Not necessary in pandas 0.13.
pd.set_option('display.width', 5000) 
pd.set_option('display.max_columns', 60)


# because of mixed types we specify dtype to prevent any errors
csv_filename = 'C:/_git/vcs/_big_files/311-service-requests.csv'
complaints = pd.read_csv(csv_filename, dtype='unicode')

is_noise = complaints['Complaint Type'] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints['Borough'].value_counts()

noise_complaint_counts = noise_complaints['Borough'].value_counts()
complaint_counts = complaints['Borough'].value_counts()

noise_complaint_counts / complaint_counts

noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind='bar')

show()
"""

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

print("------------------------------------------------------------")  # 60個


"""
print("畫出來")
df.plot(xticks=range(0, 4))
show()
"""

ax = df.plot.bar(rot=-45)  # rot表示xstick旋轉的角度
ax.legend(loc=2)  # legend的位置可以用loc調整

from matplotlib import style

style.use("fivethirtyeight")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# subplot

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ["snail", "pig", "elephant", "rabbit", "giraffe", "coyote", "horse"]
df = pd.DataFrame({"speed": speed, "lifespan": lifespan}, index=index)

print("2 X 1 bar圖")
axes = df.plot.bar(rot=-45, subplots=True, sharex=False)
axes[1].legend(loc=1)

plt.subplots_adjust(hspace=1, wspace=0.5)  # 調整各個ax間的距離
plt.suptitle("2 X 1 bar圖")

show()

print("1 X 2 bar圖")
fig, axs = plt.subplots(1, 2, sharey=False, figsize=(15, 4))
df.plot.bar(ax=axs[0], y="speed", rot=-45)
df.plot.bar(ax=axs[1], y=["speed", "lifespan"], rot=45)
plt.subplots_adjust(wspace=0.1)
plt.suptitle("1 X 2 bar圖")

show()

# 2 X 1
fig, ax = plt.subplots(2, 1, figsize=(10, 8))
df = pd.DataFrame(np.random.randint(1, 7, 6000), columns=["one"])
df["two"] = df["one"] + np.random.randint(1, 7, 6000)
df.plot.hist(ax=ax[0], bins=12, alpha=0.5)
# ax.set_title("Hist. plot")
# ax.set_xlabel("Xlabel")

show()

print("------------------------------------------------------------")  # 60個

print("建立df, 一維串列 轉 df")

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
df = pd.DataFrame(weight, index=animals)
print(df)

# 只畫一圖
df.plot(kind="line")
show()

# 畫 2X1 圖
fig, axes = plt.subplots(2, 1)
df.plot(ax=axes[0], kind="line")
df.plot(ax=axes[1], kind="line")
show()

# 畫 2X2 圖
fig, axes = plt.subplots(2, 2)
df.plot(ax=axes[0, 0], kind="line")
df.plot(ax=axes[0, 1], kind="line")
df.plot(ax=axes[1, 0], kind="line")
df.plot(ax=axes[1, 1], kind="line")
show()

# 畫 1X2 圖
fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=False)

df.plot(ax=axes[0], kind="line")
df.plot(ax=axes[1], kind="line", rot=45)

axes[1].set_xlabel("XXXX")
axes[1].set_ylabel("YYYY")
# axes[1].legend(loc=2)

plt.suptitle("畫 1X2 圖")
plt.subplots_adjust(wspace=0.1)
show()

# 畫 2X1 圖

data = np.random.randn(1000, 4)

df = pd.DataFrame(data=data, index=np.arange(1000), columns=["a", "b", "c", "d"])

# 畫 2X1 圖

fig, axs = plt.subplots(2, 1, sharex=True)
df.plot(ax=axs[0], y=["a"], kind="line", title="ax1")
df.plot(ax=axs[1], y=["b", "c", "d"], kind="line", title="ax2", figsize=(10, 8))

axs[0].set_ylabel("ylabel")
axs[1].set_ylabel("ylabel")
axs[1].set_xlabel("Xlabel")
fig.suptitle("This is a somewhat long figure title", fontsize=16)
show()

fig, axs = plt.subplots(1, 2, sharey=True)
df.plot(y=["a"], kind="line", ax=axs[0], legend=False)
df.plot(y=["b", "c", "d"], kind="line", ax=axs[1], figsize=(20, 5))
# 設定title
axs[0].set_title("ax1")
axs[1].set_title("ax2")
# 設定label
axs[0].set_xlabel("xlabel")
axs[1].set_xlabel("xlabel")
axs[0].set_xlabel("ylabel")
# 調整各個圖的間距
plt.subplots_adjust(hspace=0.5, wspace=0.1)

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

plt.title("體重")
plt.title("加刻度+旋轉")

df2 = pd.DataFrame(dists, columns=["體重"], index=dists["姓名"])
df = pd.DataFrame(dists, columns=["體重"], index=dists["姓名"])

df.plot(xticks=range(len(df.index)), use_index=True)
df.plot(xticks=range(len(df.index)), use_index=True, rot=90)


df = pd.DataFrame(
    np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["第一欄", "第二欄", "第三欄"]
)

# 使用 df.corr() 先做出各變數間的關係係數，再用heatmap作圖
sns.heatmap(df.corr())
plt.title("關係係數")
show()


# 用 histplot() 看PM2.5主要集中的區間
sns.histplot(df["PM25"])
plt.title("PM25濃度統計")
show()

print("------------------------------")  # 30個

# 使用 df.corr() 先做出各變數間的關係係數，再用heatmap作圖
sns.heatmap(df.corr())
plt.title("關係係數")
show()
