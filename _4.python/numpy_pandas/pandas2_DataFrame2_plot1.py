"""
Pandas繪圖 用matplotlib顯示

有以下類型的圖 寫在kind裡面

# plot methods:
# "bar", "hist", "box", "kde", "area", "scatter", "hexbin", "pie"

df.plot()               折線圖, 無參數, 預設就是 line
df.plot(kind="line")    折線圖
df.plot(kind="bar")     柱狀圖
df.plot(kind="barh")    橫條圖
df.plot(kind="hist")    直方圖
df.plot(kind="kde")     核密度(KDE)圖
df.plot(kind="area")    面積圖
df.plot(kind="pie")     派圖
df.plot(kind="scatter") 散佈圖
df.plot(kind="hexbin")  六角形箱體圖
df.plot(kind="box")     箱形圖

print("折線圖")
df.plot(x="監測月份", y="PM25")

print("柱狀圖")
df.plot(kind="bar", x="監測月份", y="PM25")

print("橫條圖")
df.plot(kind="barh", x="監測月份", y="PM25")

print("直方圖")
df.plot(kind="hist", x="監測月份", y="PM25")

print("核密度(KDE)圖, 需要 scipy")
df.plot(kind="kde", x="監測月份", y="PM25")

print("面積圖")
df.plot(kind="area", x="監測月份", y="PM25")

print("派圖")
df.plot(kind="pie", x="監測月份", y="PM25", autopct="%1.2f%%")

print("散佈圖")
df.plot(kind="scatter", x="PM25", y="PM10")  # X,Y需為數值

print("六角形箱體圖")
df.plot(kind="hexbin", x="PM25", y="PM10")  # X,Y需為數值

print("箱形圖")
df.plot(kind="box", x="PM25", y="PM10")  # X,Y需為數值

df.plot(kind="bar", stacked=True)
df.plot(kind="pie", subplots=True)
df.plot(kind="pie", colors=["red", "#00FF00", "blue", "yellow"])
df.plot(kind="pie", autopct="%.2f")
df.plot(kind="pie", autopct="%.0f%%")

# 掌握分佈局勢的直方圖 hist
df.plot(kind="hist")
df.plot(kind="hist", bins=30)
df.plot(kind="hist", color="blue", edgecolor="orange")
"""
print("------------------------------------------------------------")  # 60個

N = 500  # 資料個數
num_bins = 50  # 直方圖顯示時的束數

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

print("df簡易畫圖 + 所有畫圖參數")

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
df = pd.DataFrame(weight, index=animals)
# print(df)

# 簡易畫圖
# df.plot(kind="line")

# 可以寫在一起的參數
df.plot(
    kind="line",
    legend=True,
    title="圖片標題",
    fontsize=18,
    rot=45,
    figsize=[8, 5],
    xlim=(-1, 12),
    ylim=(-10, 60),
)

# rot  # 旋轉X軸標籤角度
# 設定散佈圖X、Y軸的座標值

show()

"""
df.plot(xticks=range(len(df.index)), use_index=True)
# xticks=range(2015, 2020),
"""
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
df.index = index  #  設定df的index

print("線圖 為每個欄位畫一條線")
df.plot(title="線圖 全部欄位")  # 無參數, 預設就是 line
show()

print("線圖 只看一欄位")
df["英文"].plot(title="線圖 只看一欄位")  # 無參數, 預設就是 line
show()

print("長條圖")
df.plot(kind="bar", title="長條圖 全部欄位")
show()

# df.plot.hist(y="age")

print("線圖 看一些欄位")
df[["英文", "數學"]].plot(title="線圖 看一些欄位")  # 無參數, 預設就是 line
show()

# 取出2欄資料並畫出
df2 = df[["英文", "數學"]]
df2.plot(title="線圖 新df一些欄位")  # 無參數, 預設就是 line
show()

print("線圖 看一些欄位")
print("建立空的df, 再加入資料至df")
df2 = pd.DataFrame()
df2["英文"] = df["英文"]
df2["數學"] = df["數學"]
df2.index = df.index  #  設定df的index

df2.plot(title="線圖 新df全部欄位")  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

print("直方圖")

datas = np.random.randn(N, 3)

columns = ["A", "B", "C"]
df = pd.DataFrame(datas, columns=columns)
df["A"] = df["A"] - 2
df["C"] = df["C"] + 2

df.plot(kind="hist", bins=num_bins, alpha=0.3, title="直方圖")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("直方圖")

show()

print("------------------------------------------------------------")  # 60個

print("核密度(KDE)圖, 需要 scipy")

N = 500

mu, sigma = 45, 20
datas1 = np.random.normal(mu, sigma, N)

mu, sigma = 65, 20
datas2 = np.random.normal(mu, sigma, N)

mu, sigma = 85, 20
datas3 = np.random.normal(mu, sigma, N)

df = pd.DataFrame({"A": datas1, "B": datas2, "C": datas3})

# 一般
# df.plot(kind="hist", bins=num_bins, alpha=0.3, title="直方圖")

# 核密度
df.plot.kde(title="核密度")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("箱形圖")

datas = np.random.randn(10, 4)
columns = ["AAA", "BBB", "CCC", "DDD"]
df = pd.DataFrame(datas, columns=columns)

df.boxplot()

plt.title("箱形圖")
show()

print("------------------------------")  # 30個

df = pd.read_csv("data/iris.csv")

df.boxplot(column="sepal_length", by="target", figsize=(8, 6))

plt.title("箱形圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 字典
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

columns = ["人口", "面積"]
index = dists["區名"]
df = pd.DataFrame(dists, columns=columns, index=index)
# print(df)

df["面積"] *= 1000
df.plot(xticks=range(len(df.index)), use_index=True, figsize=(8, 6))

plt.title("人口 / 面積")
show()

print("------------------------------------------------------------")  # 60個

print("派圖 長條圖 橫條圖")
"""
年度銷售金額.csv
AREA,1st,2nd,3rd,4th
East,4522,2120,1200,3800
West,3101,1846,2022,1900
South,2111,2897,3200,2139
North,4213,987,500,1568
"""

df = pd.read_csv("data/年度銷售金額.csv")
print(df)

df.index = df["AREA"]  #  設定df的index
print(df)

df = df.drop("AREA", axis=1)  # 刪除 AREA 欄，直欄 axis=1 ??
print(df)

df["1st"].plot(kind="pie", autopct="%.2f%%")
plt.title("派圖 第一季")
show()

df.plot(kind="bar")
plt.title("長條圖 年度")
show()

df.plot(kind="barh")
plt.title("橫條圖 年度")
show()

print("------------------------------------------------------------")  # 60個

print("折線圖")
"""
觀光人數統計.csv
Month, Green Island, Guguan, National Museum
1,     5872,         151397, 40988
2,     10210,        151951, 82165
3,     13213,        127943, 50683
4,     42587,        147752, 83679
5,     39920,        108086, 66842
6,     43395,        112835, 72504
7,     62794,        121329, 115817
8,     51393,        103038, 116285
9,     26671,        134118, 67488
10,    21745,        129351, 66921
11,    11525,        144019, 50670
12,    10294,        205617, 64738
"""

df = pd.read_csv("data/觀光人數統計.csv")
print(df)

df.index = df["Month"]  #  設定df的index  # 自定列索引為Month內容
df = df.drop("Month", axis=1)  # 刪除原本的月份行資料
print(df)

# 折線圖 + 參數
df.plot(linewidth=2, linestyle=":", title="觀光客人數")
show()

# 三月 資料
df_T = df.T
print(df_T.head())

df3 = df_T[3]
df3.plot(title="觀光客人數 三月")  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

print("折線圖 派圖")

columns = [2015, 2016, 2017, 2018, 2019]
index = ["北部", "中部", "南部"]
df = pd.DataFrame(
    [[250, 320, 300, 312, 280], [280, 300, 280, 290, 310], [220, 280, 250, 305, 250]],
    index=index,
    columns=columns,
)
print("df 全部資料")
print(df)
print("df.iloc[0] 第0列資料 北部")
print(df.iloc[0])
print("df.iloc[1] 第1列資料 中部")
print(df.iloc[1])
print("df.iloc[2] 第2列資料 南部")
print(df.iloc[2])

df.plot(kind="bar", title="長條圖")
show()

df.plot(kind="barh", title="橫條圖")
show()

df.plot(kind="bar", stacked=True, title="堆疊圖")
show()

print("------------------------------")  # 30個

# df.iloc[0] 第0列資料 北部
g4 = df.iloc[0].plot(kind="line", legend=True, xticks=range(2015, 2020))
# df.iloc[0] 第1列資料 中部
g4 = df.iloc[1].plot(kind="line", legend=True, xticks=range(2015, 2020))
# df.iloc[0] 第2列資料 南部
g4 = df.iloc[2].plot(kind="line", legend=True, xticks=range(2015, 2020))
plt.title("公司分區年度銷售表")

show()

print("------------------------------")  # 30個

# 派圖
df.plot(kind="pie", subplots=True, title="派圖", figsize=[12, 4])
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("散佈圖")

N = 100
print("建立 NX2 個 0-100(含) 的整數隨機數")
datas = np.random.randint(0, 100, size=(N, 2))
columns = ["XXXX", "YYYY"]
df = pd.DataFrame(datas, columns=columns)
# print(df)

print("相關係數矩陣 :\n", df.corr(), sep="")

# df.plot(kind="scatter", x="XXXX", y="YYYY")
df.plot(
    kind="scatter", x="XXXX", y="YYYY", s=50, marker="*", c="red", colormap="viridis"
)

plt.xlim(-20, 120)  # X軸範圍
plt.ylim(-20, 120)  # Y軸範圍
plt.title("散佈圖")
show()

print("------------------------------")  # 30個

print("散佈圖")

N = 100
xx = np.random.randint(0, 100, N)
yy = np.random.randint(0, 100, N)
cc = np.random.randint(0, 100, N)

df = pd.DataFrame({"XXXX": xx, "YYYY": yy, "COLOR": cc})

df.plot(
    kind="scatter", x="XXXX", y="YYYY", s=50, marker="*", c="COLOR", colormap="viridis"
)

plt.title("散佈圖")
show()

print("------------------------------")  # 30個

N = 1000
datas = np.random.randn(N, 2)

columns = list("XY")
index = np.arange(N)
df = pd.DataFrame(datas, columns=columns, index=index)
# print(df)

df.plot(kind="scatter", x="X", y="Y", color="DarkBlue", label="散佈圖")
show()

print("------------------------------------------------------------")  # 60個

N = 100
datas = np.random.randn(N, 4)

# print("建立 3x2 個0-9(含) 的整數隨機數")
# datas = np.random.randint(0, 10, size=(N, 4))
# print(datas)

columns = list("ABCD")
index = np.arange(N)
df = pd.DataFrame(datas, columns=columns, index=index)
# print(df)

print("多個scatter畫在一起")

ax = df.plot(kind="scatter", x="A", y="B", color="r", label="A級品")
df.plot(kind="scatter", x="A", y="C", color="g", label="B級品", ax=ax)
df.plot(kind="scatter", x="A", y="D", color="b", label="C級品", ax=ax)

show()

print("------------------------------------------------------------")  # 60個
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

df.index = df["name"]  #  設定df的index

df["weight"].plot(kind="line", title="線圖")
df["weight"].plot(kind="bar", title="長條圖")

# df["weight"].plot(kind="pie", autopct="%.0f%%", title = "派圖")

show()

print("------------------------------------------------------------")  # 60個

print("只變更要強調的扇形的顏色")

datas = {"name": ["鼠", "牛", "虎", "兔", "龍"], "weight": [3, 48, 33, 8, 38]}
df = pd.DataFrame(datas)
print(df)

# 要強調的扇形的標籤
point_label = "虎"
# 重點色
point_color = "#FF0000"

# 調整特定標籤的顏色
palette = sns.color_palette("binary", len(df))
for i in df[df.name == point_label].index.values:
    palette[i] = point_color

# df["weight"].plot(kind="pie", autopct="%.0f%%", title = "派圖")

df["weight"].plot(
    kind="pie",
    labels=df["name"],
    autopct="%1.1f%%",
    startangle=90,
    counterclock=False,
    colors=palette,
)

show()

print("------------------------------------------------------------")  # 60個

N = 1000
datas = np.random.randn(N, 4)
datas[0, :] = 0

columns = list("ABCD")
df = pd.DataFrame(datas, columns=columns)
df = df.cumsum()
df.plot()  # 無參數, 預設就是 line

plt.title("線圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Series的索引會被作為subplot的 X軸，可以使用參數 use_index = False 來禁用該功能
# X軸的刻度可以透過 xticks 來調整
# Y軸的刻度可以透過 yticks 來調整

N = 6
columns = pd.Index(["國文", "英文", "數學", "社會"], name="科目")
index = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Frog"]
df = pd.DataFrame(
    np.random.randn(N, 4).cumsum(0),
    index=index,
    columns=columns,
)
print(df)

df.plot()  # 無參數, 預設就是 line

plt.title("折線圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 柱狀圖
# 設定 kind = "bar" 或 "barh" 即可繪製柱狀圖
# Series和 DataFrame的 索引會被當作subplot的 X軸(bar)或 Y軸(barh)

N = 6
columns = pd.Index(["國文", "英文", "數學", "社會"], name="科目")
index = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Frog"]
df = pd.DataFrame(
    np.random.rand(N, 4),
    index=index,
    columns=columns,
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
print("------------------------------------------------------------")  # 60個

print("長條圖")
"""
tips.csv
total_bill,tip,sex,smoker,day,time,size
16.99,1.01,Female,No,Sun,Dinner,2
10.34,1.66,Male,No,Sun,Dinner,3
21.01,3.5,Male,No,Sun,Dinner,3
23.68,3.31,Male,No,Sun,Dinner,2
24.59,3.61,Female,No,Sun,Dinner,4
25.29,4.71,Male,No,Sun,Dinner,4
"""

tips = pd.read_csv("data/tips.csv")

# 用 crosstab()方法創建一個 交叉表，預設統計 發生的次數(計數)
party_counts = pd.crosstab(tips.day, tips["size"])
print(party_counts)
party_counts.plot(kind="bar")
show()

party_counts = party_counts.iloc[:, 2:5]
print(party_counts)
party_counts.plot(kind="bar", stacked=True)
show()

party_counts = party_counts.div(party_counts.sum(1), axis=0)
print(party_counts)

cc = party_counts.sum(1)
print(cc)

party_counts.plot(kind="bar", stacked=True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("直方圖(histogram)和密度圖")

"""
tips.csv
total_bill,tip,sex,smoker,day,time,size
16.99,1.01,Female,No,Sun,Dinner,2
10.34,1.66,Male,No,Sun,Dinner,3
21.01,3.5,Male,No,Sun,Dinner,3
23.68,3.31,Male,No,Sun,Dinner,2
24.59,3.61,Female,No,Sun,Dinner,4
25.29,4.71,Male,No,Sun,Dinner,4
"""

tips = pd.read_csv("data/tips.csv")

# 用 plot(kind="hist") 繪製直方圖
tips.total_bill.plot(kind="hist", bins=50)
plt.title("total_bill 直方圖")
show()

# tip比例 直方圖
tip_ratios = tips.tip / tips.total_bill
tip_ratios.plot(kind="hist", bins=50)
plt.title("tip比例 直方圖")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("散佈圖")

"""
macrodata.csv
year,quarter,realgdp,realcons,realinv,realgovt,realdpi,cpi,m1,tbilrate,unemp,pop,infl,realint
1959.0,1.0,2710.349,1707.4,286.898,470.045,1886.9,28.98,139.7,2.82,5.8,177.146,0.0,0.0
1959.0,2.0,2778.801,1733.7,310.859,481.301,1919.7,29.15,141.7,3.08,5.1,177.83,2.34,0.74
1959.0,3.0,2775.488,1751.8,289.226,491.26,1916.4,29.35,140.5,3.82,5.3,178.657,2.74,1.09
1959.0,4.0,2785.204,1753.7,299.356,484.052,1931.3,29.37,140.0,4.33,5.6,179.386,0.27,4.06
1960.0,1.0,2847.699,1770.5,331.722,462.199,1955.5,29.54,139.6,3.5,5.2,180.007,2.31,1.19
1960.0,2.0,2834.39,1792.9,298.152,460.4,1966.1,29.55,140.2,2.68,5.2,180.671,0.14,2.55
"""

macro = pd.read_csv("data/macrodata.csv")
cc = macro[:5]
print(cc)

data = macro[["cpi", "m1", "tbilrate", "unemp"]]
cc = data[:5]
print(cc)

# diff(): 以上下元素的差異值填入
df = np.log(data).diff().dropna()

df.plot(kind="scatter", x="m1", y="unemp")
plt.title("Changes in log({0}) vs. log({1})".format("m1", "unemp"))

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
print("------------------------------------------------------------")  # 60個

df = pd.read_excel("data/2017_PM25.xlsx")

# 資料操作, NaN與重複值處理

df = df.dropna()
df = df.drop_duplicates()

cc = df.head(30)
print(cc)

print("檢視資料類型(有無非數值類型存在)")
cc = df.dtypes
print(cc)

# 如果屬性是Object，如何改成數值屬性
# df["屬於Object的欄位"] = pd.to_numeric(df.屬於Object的欄位, errors="coerce")

# print("相關係數矩陣 :\n", df.corr(), sep="")

print("折線圖")

df.plot(x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

df.plot(x="監測月份", y="PM10", title="監測月份與PM10的關係")
show()

print("柱狀圖")
df.plot(kind="bar", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("橫條圖")
df.plot(kind="barh", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("直方圖")
df.plot(kind="hist", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

"""
print("核密度(KDE)圖")
df.plot(kind="kde",x="監測月份", y="PM25",title="監測月份與PM2.5的關係")
show()
"""

print("面積圖")
df.plot(kind="area", x="監測月份", y="PM25", title="監測月份與PM2.5的關係")
show()

print("派圖")
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

sns.histplot(df["PM25"].dropna(), kde=False, bins=30)
plt.title("用直方圖看PM25分佈")
show()

df["Nox"].hist(bins=30)
plt.title("用直方圖看Nox的分佈")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

tips = sns.load_dataset("tips")

g = sns.FacetGrid(data=tips, col="time", row="smoker")  # 分成2X2
g.map(plt.scatter, "total_bill", "tip")
show()

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

tips = sns.load_dataset("tips")
cc = tips.head()
print(cc)

sns.histplot(tips["total_bill"])
show()

sns.histplot(tips["total_bill"], kde=False, bins=30)
show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="scatter")
show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="hex")
show()

sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
show()

sns.pairplot(tips)
show()

sns.pairplot(tips, hue="sex", palette="coolwarm")
show()

sns.kdeplot(tips["total_bill"])
show()

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
show()

sns.swarmplot(x="day", y="total_bill", data=tips, color="black")
show()

# catplot兩變量關係圖
sns.catplot(x="day", y="total_bill", data=tips, kind="bar")

print(tips.shape)
print(tips)

tips2 = pd.concat([tips["total_bill"], tips["tip"]], axis=1)

print(tips2.shape)
print(tips2)

correlation = tips2.corr()
print("相關係數矩陣 :\n", correlation, sep="")

sns.heatmap(correlation, annot=True, cmap="coolwarm")
show()

""" NG
fp=flights.pivot_table(index="month",columns="year",values="passengers")

sns.heatmap(fp,cmap="magma",linecolor="white",linewidths=1)

show()

sns.clustermap(fp,cmap="coolwarm",standard_scale=1)

sns.lmplot(x="total_bill",y="tip",data=tips,hue="sex",markers=["o","v"],scatter_kws={"s":100})

sns.lmplot(x="total_bill",y="tip",data=tips,col="sex",row="time",aspect=1,size=4)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = sns.load_dataset("iris")
cc = iris.head()
print(cc)

cc = iris["species"].unique()
print(cc)

g = sns.PairGrid(iris)  # 分成4X4

g.map_diag(sns.histplot)  # 對角線

g.map_upper(plt.scatter)  # 右上三角形

g.map_lower(sns.kdeplot)  # 左下三角形

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(15, 5))

# because of mixed types we specify dtype to prevent any errors
csv_filename = "D:/_git/vcs/_big_files/311-service-requests.csv"
complaints = pd.read_csv(csv_filename, dtype="unicode")

print(complaints)
complaints["Complaint Type"]

complaints["Complaint Type"].value_counts()

complaint_counts = complaints["Complaint Type"].value_counts()
complaint_counts[:10]

complaint_counts[:10].plot(kind="bar")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(15, 5))

# because of mixed types we specify dtype to prevent any errors
csv_filename = "D:/_git/vcs/_big_files/311-service-requests.csv"
complaints = pd.read_csv(csv_filename, dtype="unicode")

is_noise = complaints["Complaint Type"] == "Noise - Street/Sidewalk"
noise_complaints = complaints[is_noise]
noise_complaints["Borough"].value_counts()

noise_complaint_counts = noise_complaints["Borough"].value_counts()
complaint_counts = complaints["Borough"].value_counts()

noise_complaint_counts / complaint_counts

noise_complaint_counts / complaint_counts.astype(float)

(noise_complaint_counts / complaint_counts.astype(float)).plot(kind="bar")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
weather_sample.csv
年月,東京-平均氣溫(℃),東京-降雨量合計(mm),東京-日照時間(時間),大阪-平均氣溫(℃),大阪-降雨量合計(mm),大阪-日照時間(時間),那霸-平均氣溫(℃),那霸-降雨量合計(mm),那霸-日照時間(時間),函館-平均氣溫(℃),函館-降雨量合計(mm),函館-日照時間(時間)
2015/1/1,5.8,92.5,182,6.1,93,123.3,16.6,22,90.7,-0.9,43,108.2
2015/2/1,5.7,62,166.9,6.9,25.5,136.8,16.8,47,114.1,0.1,52.5,129.4
2015/3/1,10.3,94,194.2,10.2,174.5,175.4,19,95.5,126.5,4.3,100,160
2015/4/1,14.5,129,149.5,15.9,107,152.1,22.2,100,118.9,8.3,133.5,227.5
2015/5/1,21.1,88,240.6,21.5,104,249.3,24.9,197.5,144.2,13.2,74.5,251.4
2015/6/1,22.1,195.5,137.3,22.9,196,144.1,28.7,38,221.7,16.6,93,169.9
"""
print("日本各都市平均氣溫全年資料")

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"])
# print(df)

df.plot(kind="line", x="年月", y="東京-平均氣溫(℃)", title="東京", figsize=[6, 4])
show()

df.plot(kind="line", x="年月", y="大阪-平均氣溫(℃)", title="大阪", figsize=[6, 4])
show()

print("------------------------------")  # 30個

filename = "data/weather_sample.csv"
df = pd.read_csv(filename, header=0, parse_dates=["年月"], index_col=0)

df_average = df[["東京-平均氣溫(℃)", "大阪-平均氣溫(℃)", "那霸-平均氣溫(℃)", "函館-平均氣溫(℃)"]]
print(df_average)

df_average.plot(kind="line")

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

ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette="pastel")

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

ax = sns.lineplot(data=tmp_stack, x="年月", y="value", hue="category", palette=palette)

plt.xticks(rotation=30)
ax.legend(loc="lower left", bbox_to_anchor=(1, 0))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
bikes.csv 310筆資料
Date;Berri 1;Brébeuf (données non disponibles);Côte-Sainte-Catherine;Maisonneuve 1;Maisonneuve 2;du Parc;Pierre-Dupuy;Rachel1;St-Urbain (données non disponibles)
01/01/2012;35;;0;38;51;26;10;16;
02/01/2012;83;;1;68;153;53;6;43;
03/01/2012;135;;2;104;248;89;3;58;
04/01/2012;144;;1;116;318;111;8;61;
05/01/2012;197;;2;124;330;97;13;95;
06/01/2012;146;;0;98;244;86;4;75;
"""
print("bikes ST")

df = pd.read_csv("data/bikes.csv", encoding="ISO-8859-1")
print(df.head())

df = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)

df["Berri 1"].plot(figsize=(8, 6))  # 無參數, 預設就是 line
plt.title("只畫出一欄")
show()

df.plot(figsize=(8, 6))
plt.title("畫出全部資料")
show()

print("------------------------------")  # 30個

print("讀取csv檔, 其他參數")
bikes = pd.read_csv(
    "data/bikes.csv",
    sep=";",
    encoding="latin1",
    parse_dates=["Date"],
    dayfirst=True,
    index_col="Date",
)
print(df.head())

bikes["Berri 1"].plot(figsize=(8, 6))  # 無參數, 預設就是 line
plt.title("只畫出一欄")
show()

# Add the weekday column
berri_bikes = bikes[["Berri 1"]].copy()

berri_bikes[:5]

berri_bikes.index  #  設定df的index

berri_bikes.index.day

berri_bikes.index.weekday

berri_bikes.loc[:, "weekday"] = berri_bikes.index.weekday

# 將週間的騎乘數加起來
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

plt.title("柱狀圖")
show()

print("bikes SP")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("2012蒙特婁氣象資料 ST")

"""
# Here's an URL template you can use to get data in Montreal.
url_template = "http://climate.weather.gc.ca/climateData/bulkdata_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"

# To get the data for March 2013, we need to format it with month=3, year=2012.
# url = url_template.format(month=3, year=2012)
# df_mar_2012 = pd.read_csv(url, skiprows=15, index_col="Date/Time", parse_dates=True, encoding="latin1", header=True)

weather_2012.csv 2012蒙特婁氣象資料 8784筆資料 8欄
Date/Time,Temp (C),Dew Point Temp (C),Rel Hum (%),Wind Spd (km/h),Visibility (km),Stn Press (kPa),Weather
2012-01-01 00:00:00,-1.8,-3.9,86,4,8.0,101.24,Fog
2012-01-01 01:00:00,-1.8,-3.7,87,4,8.0,101.24,Fog
2012-01-01 02:00:00,-1.8,-3.4,89,7,4.0,101.26,"Freezing Drizzle,Fog"
2012-01-01 03:00:00,-1.5,-3.2,88,6,4.0,101.27,"Freezing Drizzle,Fog"
2012-01-01 04:00:00,-1.5,-3.3,88,7,4.8,101.23,Fog
2012-01-01 05:00:00,-1.4,-3.3,87,9,6.4,101.27,Fog
2012-01-01 06:00:00,-1.5,-3.1,89,7,6.4,101.29,Fog
"""

plt.figure(figsize=(8, 4))

filename = "data/weather_2012.csv"
df_2012 = pd.read_csv(filename, index_col="Date/Time")

df_2012["Temp (C)"].plot()

show()

print("------------------------------")  # 30個

filename = "data/weather_2012.csv"
df_mar_2012 = pd.read_csv(filename)

plt.figure(figsize=(8, 4))
df_mar_2012["Temp (C)"].plot()  # 沒有指明X軸刻度
show()

df_mar_2012 = df_mar_2012.dropna(axis=1, how="any")
print(df_mar_2012[:5])

print("------------------------------")  # 30個

# Plotting the temperature by hour of day

temperatures = df_mar_2012[["Temp (C)"]].copy()
print(temperatures.head)

print(df_mar_2012.index)

temperatures.loc[:, "Hour"] = df_mar_2012.index
temperatures.groupby("Hour").aggregate(np.median).plot()  # 無參數, 預設就是 line

show()

print("------------------------------------------------------------")  # 60個

# 讀取csv檔
# "\xb0" for that degree character °

filename = "data/weather_2012.csv"
weather_2012 = pd.read_csv(
    filename, skiprows=0, index_col="Date/Time", parse_dates=True
)
weather_2012 = weather_2012.dropna(axis=1)
weather_2012.columns = [col.replace("\xb0", "") for col in weather_2012.columns]
print(weather_2012)
print(weather_2012.shape)

print("------------------------------------------------------------")  # 60個

plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 3)
plt.rcParams["font.family"] = "sans-serif"

filename = "data/weather_2012.csv"
weather_2012 = pd.read_csv(filename, parse_dates=True, index_col="Date/Time")
print(weather_2012[:5])

weather_description = weather_2012["Weather"]
is_snowing = weather_description.str.contains("Snow")

print(is_snowing[:5])

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

print("2012蒙特婁氣象資料 SP")
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("子圖 ST")
print("------------------------------------------------------------")  # 60個

weight = [3, 48, 33, 8, 38]
age = [10, 20, 30, 25, 15]
index = ["鼠", "牛", "虎", "兔", "龍"]
df = pd.DataFrame({"體重": weight, "年齡": age}, index=index)
print(df)

print("2X1 bar圖")
axes = df.plot.bar(subplots=True, sharex=False, figsize=(8, 6))

axes[0].legend(loc=0)
axes[1].legend(loc=0)

plt.subplots_adjust(hspace=1, wspace=0.5)  # 調整各個ax間的距離
plt.suptitle("畫 2X1 圖")

show()

print("2X1 bar圖")
fig, axes = plt.subplots(2, 1, sharey=False, figsize=(8, 6))
df.plot.bar(ax=axes[0], y="體重")
df.plot.bar(ax=axes[1], y=["體重", "年齡"])
plt.subplots_adjust(wspace=0.1)
plt.suptitle("畫 2X1 圖")

show()

print("------------------------------------------------------------")  # 60個

# 2X1
fig, axes = plt.subplots(2, 1, figsize=(10, 8))
df = pd.DataFrame(np.random.randint(1, 7, 6000), columns=["one"])
df["two"] = df["one"] + np.random.randint(1, 7, 6000)

# 畫在第0圖
df.plot.hist(ax=axes[0], bins=12, alpha=0.5)

# 畫在第1圖
df.plot.hist(ax=axes[1], bins=12, alpha=0.5)

axes[0].set_title("第0圖")
axes[1].set_title("第1圖")
axes[0].set_xlabel("xlabel")
axes[1].set_xlabel("xlabel")
axes[0].set_ylabel("ylabel")
axes[1].set_ylabel("ylabel")

# axes[1].legend(loc=2)

show()

print("------------------------------------------------------------")  # 60個

print("建立df, 一維串列 轉 df")

weight = [3, 48, 33, 8, 38, 16, 36, 29, 22, 6, 12, 42]
animals = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
df = pd.DataFrame(weight, index=animals)
# print(df)

# 畫 2X1 圖
fig, axes = plt.subplots(2, 1)

# 畫在第0圖
df.plot(ax=axes[0], kind="line")

# 畫在第1圖
df.plot(ax=axes[1], kind="line")

plt.suptitle("畫 2X1 圖")
show()

# 畫 2X2 圖
fig, axes = plt.subplots(2, 2)

# 畫在第0,0圖
df.plot(ax=axes[0, 0], kind="line")

# 畫在第0,1圖
df.plot(ax=axes[0, 1], kind="line")

# 畫在第1,0圖
df.plot(ax=axes[1, 0], kind="line")

# 畫在第1,1圖
df.plot(ax=axes[1, 1], kind="line")

plt.suptitle("畫 2X2 圖")
show()

# 畫 2X1 圖
fig, axes = plt.subplots(2, 1, figsize=(8, 5), sharey=False)

# 畫在第0圖
df.plot(ax=axes[0], kind="line")

# 畫在第1圖
df.plot(ax=axes[1], kind="line")

plt.suptitle("畫 2X1 圖")
plt.subplots_adjust(wspace=0.1)
show()

print("------------------------------------------------------------")  # 60個

# 畫 2X1 圖

data = np.random.randn(1000, 4)

columns = ["a", "b", "c", "d"]
index = np.arange(1000)
df = pd.DataFrame(data=data, index=index, columns=columns)

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(10, 8))

# 畫在第0圖 1欄資料
df.plot(ax=axes[0], y=["a"], kind="line", title="ax1")

# 畫在第1圖 3欄資料
df.plot(ax=axes[1], y=["b", "c", "d"], kind="line", title="ax2")

axes[0].set_xlabel("X")
axes[0].set_ylabel("Y")
axes[1].set_xlabel("X")
axes[1].set_ylabel("Y")

plt.suptitle("畫 2X1 圖")
show()

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(14, 5))

# 畫在第0圖 1欄資料
df.plot(y=["a"], kind="line", ax=axes[0], legend=False)

# 畫在第1圖 3欄資料
df.plot(y=["b", "c", "d"], kind="line", ax=axes[1])

axes[0].set_title("第0圖")
axes[1].set_title("第1圖")
axes[0].set_xlabel("xlabel")
axes[1].set_xlabel("xlabel")
axes[0].set_ylabel("ylabel")
axes[1].set_ylabel("ylabel")

plt.subplots_adjust(hspace=0.5, wspace=0.1)  # 調整各個圖的間距

show()

print("------------------------------------------------------------")  # 60個
print("子圖 SP")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# 完整的
# 疫情數據分析

print("疫情數據分析")

# 讀入疫情數據, 做簡單的分析
df0 = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
)

# 在 pandas 最常用的指令, 大概就是用 head 看看 Data Frame 長什麼樣子。
print("看看資料的前5筆a")
print(df0.head())

# 我們把一些不用的欄位刪掉。
df0 = df0.drop(columns=["Province/State", "Lat", "Long"])

# 再欣賞一下, 看 Data Frame 是不是又清爽一些？
print("看看資料的前5筆b, 少了3個欄位")
print(df0.head())

# 為了方便說明, 我們只選擇幾個國家來分析。
df = df0.loc[
    df0["Country/Region"].isin(
        ["Taiwan*", "Japan", "Korea, South", "Germany", "Singapore"]
    )
]
print("選幾個國家來分析")
print(df)

print("df 這個 Data Frame 改以國家為 index")
df = df.set_index("Country/Region")

print("行列互換")
df = df.T
print(df.head())

print("改成每日新增案例, 而不是累計案例")
df = df.diff()
print(df.head())

print("去掉第一天")
df = df.drop(["1/22/20"])
print(df.head())

print("把 index 的日期改為「真的」日期")
df.index = pd.to_datetime(df.index)
print(df.head())

# 我們來依人口調整, 較能比較。最後我們希望得到的是「每 10 萬人中, 有多少人染疫」
population = np.array([84284340, 125753381, 51351596, 5936285, 23897291]) / 100000
dfm = df / population
print("每10萬人中,有多少人染疫")
print(dfm.tail())

# 畫個最近 2 個月的圖試試看
dfm[-60:].plot()
plt.title("最近2個月的圖")
plt.show()

print("看各國疫情最高峰的數目大概是多少, 這樣也知道台灣的狀況應該算如何")
print(dfm.max(axis=0))

# 注意前面我們發現, 我們的數據有些問題。可能有些日子疫情沒有更新, 所以新增是 0, 結果加到下一天去。
# 在實際的工作中, 我們會花很多時間去調校, 做「資料清理」。
# 現在我們準備看看各國疫情高峰期, 走勢大概是怎麼樣的。

de = dfm["Germany"]
jp = dfm["Japan"]
kr = dfm["Korea, South"]
sg = dfm["Singapore"]
tw = dfm["Taiwan*"]

# 試以德國為例, 我們看看最高峰前後兩個月的樣子。
n = de.argmax()
period = de[n - 60 : n + 60]
ma = period.rolling(window=7).mean()[6:]
period[6:].plot()
ma.plot()
plt.title("德國的情況")
plt.show()

# 把剛剛的想法寫成一個函式, 簡簡單單就應用到不同國家。


def peak_period(country):
    n = country.argmax()
    period = country[n - 60 : n + 60]
    ma = period.rolling(window=7).mean()[6:]
    period[6:].plot()
    ma.plot()


# 日本的情況
peak_period(jp)
plt.title("日本的情況")
plt.show()

# 韓國的情況
peak_period(kr)
plt.title("韓國的情況")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# titanic 畫圖


"""
数据分析

基于Pandas和Numpy两种工具，分析给定数据集包含的特征。主要包括数据探索、数据清洗等，其目的在于保持数据的“整洁”，为后续应用机器学习模型做准备。

整个数据分析流程如下：

1、加载数据：可以直接从网站下载，也可以使用numpy或者Pandas、python等本地加载

2、观察和理解数据：数据集大小，数据集的饱和度，数据集中各个属性的含义、数值分布，正负标签比例等。

3、数据清洗
1.加载数据

案例，我们分析一个登船者的生存概率。
"""

data = sns.load_dataset("titanic")  # 从网站直接下载。
# 或者直接通过函数加载。
# data = pd.read_csv("./titanic.csv")  # 加载后的文件是一个dataframe 格式的文件。


##观察和理解数据
print(data.shape)  # 观察数据规模

# (891, 15)

cc = data.describe()  # 数据分布描述
print(cc)

cc = data.head(5)  # 前五条数据记录
print(cc)

cc = data.columns  # 列出所有字段
print(cc)

"""
# 学习相关知识，了解每个字段的含义。
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object')
"""

# 观察正负标签的比例

# data["survived"].sum()  # 总数
cc = data["survived"].sum() / data.shape[0]  # 生存者的比例是38.38%，比例稍微偏低，但可以接受。最好正负标签平衡。
print(cc)

# 或者使用
cc = data["survived"].mean()
print(cc)

# 观察数据的饱和度.
cc = data.isna().sum() / data.shape[0]
print(cc)
"""
# 可以看出deck（舱面）和Age缺少较为严重,分别是70%和19.8%。

survived       0.000000
pclass         0.000000
sex            0.000000
age            0.198653
sibsp          0.000000
parch          0.000000
fare           0.000000
embarked       0.002245
class          0.000000
who            0.000000
adult_male     0.000000
deck           0.772166
embark_town    0.002245
alive          0.000000
alone          0.000000
dtype: float64
"""

# 观察标签的均衡性
# 观察survived的均衡性
data["survived"].value_counts().plot(kind="bar")
show()

print("------------------------------")  # 30個

# 观察性别分布
data["sex"].value_counts().plot(kind="pie")  # 饼状图
show()

print("------------------------------")  # 30個

# 观察登船港口的分布
data.columns
data["embarked"].value_counts().plot(kind="bar")  # 类别数据作图

show()

print("------------------------------")  # 30個

# 观察年龄分布
data["age"].plot(kind="hist")  # 数值型数据不用统计，直接做图

show()

print("------------------------------")  # 30個

# 热力图分析

# 热力图是观察数据相关性的利器
# 使用sns做热力图，观察变量间的相关性
""" NG 做 corr() 要純數字
sns.heatmap(data.corr(),linewidths=.5)

show()
"""
print("------------------------------")  # 30個

# 1.2 数据的清洗

# 对数据进行删除、补充或者修改，洗掉“杂质”。

# 填充和删除数据
# 获取缺失值情况
print(data.columns)

"""
Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object')
"""

cc = data.isna().sum()  # 查看缺省值
print(cc)
"""
survived         0
pclass           0
sex              0
age            177
sibsp            0
parch            0
fare             0
embarked         2
class            0
who              0
adult_male       0
deck           688
embark_town      2
alive            0
alone            0
dtype: int64
"""
# age、deck and embark_town
# NG data['deck'].fillna('missing',inplace=True) # 用字符“missing”填充
print(data["deck"])

print(data["age"])

# 使用平均年龄来填充年龄中的 nan 值
data["age"].fillna(data["age"].mean(), inplace=True)

print(data["age"])
print(data["age"].isna().sum())

# 删除数据。这个步骤只能运行一次，否则系统会报错。
# 从表示相关性的热力图可以发现，pclass和adult_male与survied相关性非常差，所以删除他们
# data = data.drop(columns=["pclass","adult_male"])
# print(data.columns,data.shape)

# 上述删除操作只能运行一次。当第一次运行时，指定的columns被删除。第二次运行时会出现找不到属性的报错。
# 为了程序运行流畅，也可以做如下改写。
print("删除操作之前-----\n", data.columns, data.shape)
if "pclass" in data.columns:
    data = data.drop(columns=["pclass"])
    print(data.columns, data.shape)
else:
    print("pclass 属性已经被删除")
if "adult_male" in data.columns:
    data = data.drop(columns=["adult_male"])
    print(data.columns, data.shape)
else:
    print("adult_male属性已经被删除")
if "alive" in data.columns:
    data = data.drop(columns=["alive"])
    print(data.columns, data.shape)
else:
    print("alive属性已经被删除")

# 删除之后，再一次做热力图
# 使用sns做热力图，观察变量间的相关性
""" NG 做 corr() 要純數字
sns.heatmap(data.corr(),linewidths=.5)
show()
"""

"""
删除操作之前-----
 Index(['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'fare',
       'embarked', 'class', 'who', 'adult_male', 'deck', 'embark_town',
       'alive', 'alone'],
      dtype='object') (891, 15)
Index(['survived', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class',
       'who', 'adult_male', 'deck', 'embark_town', 'alive', 'alone'],
      dtype='object') (891, 14)
Index(['survived', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class',
       'who', 'deck', 'embark_town', 'alive', 'alone'],
      dtype='object') (891, 13)
Index(['survived', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'class',
       'who', 'deck', 'embark_town', 'alone'],
      dtype='object') (891, 12)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('測試滾動均值')

N = 100
x = np.linspace(0, 2 * np.pi, N)
y = np.sin(x)

y = np.random.randn(N)

df = pd.DataFrame({"Y": y})
# print(df)
# df.plot()

df.plot()
#print(df)

ma = df.rolling(window=10).mean()
ma.plot()
#print(ma)

plt.title("測試滾動均值")
plt.show()

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
ax.legend(loc=2)  # legend的位置可以用loc調整

from matplotlib import style

style.use("fivethirtyeight")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

plt.title("體重")

columns = ["體重"]
index = dists["姓名"]
df2 = pd.DataFrame(dists, columns=columns, index=index)

columns = ["體重"]
index = dists["姓名"]
df = pd.DataFrame(dists, columns=columns, index=index)

df.plot(xticks=range(len(df.index)), use_index=True)
df.plot(xticks=range(len(df.index)), use_index=True, rot=90)

columns = ["第一欄", "第二欄", "第三欄"]
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=columns)

# 使用 df.corr() 先做出各變數間的關係係數，再用heatmap作圖
correlation = df.corr()
print("相關係數矩陣 :\n", correlation, sep="")
sns.heatmap(correlation)
plt.title("關係係數")
show()

# 用 histplot() 看PM2.5主要集中的區間
sns.histplot(df["PM25"])
plt.title("PM25濃度統計")
show()

print("------------------------------------------------------------")  # 60個

# Make the graphs a bit prettier, and bigger
plt.style.use("ggplot")
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["figure.figsize"] = (15, 5)
plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["figure.figsize"] = (8, 3)
plt.rcParams["font.family"] = "sans-serif"

print("------------------------------------------------------------")  # 60個

# 1.初始化

# 2.解決plot不能顯示中文問題
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
mpl.rcParams["axes.unicode_minus"] = False

print("------------------------------------------------------------")  # 60個

# df = df.cumsum()#依欄位, 逐列累加
# print(df)

print("------------------------------------------------------------")  # 60個

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x)

print("------------------------------------------------------------")  # 60個

# fail
# df_mar_2012 = df_mar_2012.drop(["Year", "Month", "Day", "Time", "Data Quality"], axis=1)
# print(df_mar_2012[:5])
# weather_data = weather_data.drop(["Year", "Day", "Month", "Time", "Data Quality"], axis=1)

print("------------------------------")  # 30個

weather_2012 = pd.concat(data_by_month)




