"""
numpy的使用

numpy: 數值計算的標準套件

DataFrame 測試


1. 基本建立 np.array
   1.1 自填陣列, 串列轉np陣列
   1.2 自動產生陣列

arr1 = np.array([1, 2, 3, 4, 5])

describe(統計資料)

count：数量统计，此列共有多少有效值
unipue：不同的值有多少个
std：标准差
min：最小值
25%：四分之一分位数
50%：二分之一分位数
75%：四分之三分位数
max：最大值
mean：均值

count：非空值的数量
mean：平均值
std：标准差
min：最小值
25%：第一四分位数（Q1）
50%：第二四分位数（中位数，Q2）
75%：第三四分位数（Q3）
max：最大值

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# 可以使用SSL module把證書驗證改成不需要驗證即可，方法如下:
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

print("------------------------------------------------------------")  # 60個

print("目前 Pandas 版本 :")
cc = pd.__version__
print(cc)

print("------------------------------------------------------------")  # 60個

print("建立df, 一維串列 轉 df")

datas = ["鼠", "牛", "虎", "兔", "龍", "蛇"]
df = pd.DataFrame(datas)
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ]
)
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ],
    index=["王小明", "李小美", "陳大同", "林小玉"],
    columns=["國文", "英文", "數學", "自然", "社會"],
)
print(df)

print("------------------------------------------------------------")  # 60個

se1 = pd.Series({"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79})
se2 = pd.Series({"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53})
se3 = pd.Series({"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47})
se4 = pd.Series({"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94})
se5 = pd.Series({"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80})
df = pd.DataFrame({"國文": se1, "英文": se2, "數學": se3, "自然": se4, "社會": se5})
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series 合併")
se1 = pd.Series({"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79})
se2 = pd.Series({"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53})
se3 = pd.Series({"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47})
se4 = pd.Series({"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94})
se5 = pd.Series({"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80})
df = pd.concat([se1, se2, se3, se4, se5], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
df.columns = ["國文", "英文", "數學", "自然", "社會"]
print(df)


# read_html.py
url = "https://www.tiobe.com/tiobe-index/"
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])

# to_csv.py
scores = {
    " 國文": {" 王小明": 65, " 李小美": 90, " 陳大同": 81, " 林小玉": 79},
    " 英文": {" 王小明": 92, " 李小美": 72, " 陳大同": 85, " 林小玉": 53},
    " 數學": {" 王小明": 78, " 李小美": 76, " 陳大同": 91, " 林小玉": 47},
    " 自然": {" 王小明": 83, " 李小美": 93, " 陳大同": 89, " 林小玉": 94},
    " 社會": {" 王小明": 70, " 李小美": 56, " 陳大同": 94, " 林小玉": 80},
}
df = pd.DataFrame(scores)
df.to_csv("tmp_scores3.csv", encoding="utf-8-sig")



print("建立df, 二維串列4X5 轉 df")

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns)
print(df)

"""
print("畫出來")
df.plot(xticks=range(0, 4))
plt.show()
"""

"""df資訊

print('檢視前幾行')
cc = df.head()
print(cc)

print('檢視前2行')
cc = df.head(2)
print(cc)

print('檢視後2行')
cc = df.tail(2)
print(cc)

print('索引index')
cc = df.index
print(cc)

print('欄名columns')
cc = df.columns
print(cc)

print('顯示values')
print(df.values)

print(df.info())

print('df使用記憶體大小')
cc = df.info(memory_usage='deep')
print(cc)

print(df.duplicated())

print("df之大小")
M, N = df.shape
print(df.shape)
print('df之大小', M, 'X',N)

print("顯示df之describe(統計資料)")
print(df.describe())

print(df.count())
print(df.mean())
print(df.std())
print(df.min())
print(df.median())
print(df.max())

"""

print("------------------------------------------------------------")  # 60個

print("建立df, 二維串列4X5 轉 df, 加上欄名與index")

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]

df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)

print("陳聰明的成績(df.values[1])：")
print(df.values[1])
print("陳聰明的英文成績(df.values[1][2])：")
print(df.values[1][2])

print("------------------------------")  # 30個

print("建立df, 二維串列 轉 df")

datas = np.random.randint(6, 16, (12, 5))  # 整數數字6~12 10X5
columns = ["國文", "英文", "數學", "社會", "自然"]
df = pd.DataFrame(datas, columns=columns)

print("使用預設索引index")
print(df)

print("重新設定索引index")
df.index = range(1, 13)
print(df)

print("重新設定索引index")
# index = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"] # same
index = list("鼠牛虎兔龍蛇馬羊猴雞狗豬")
df.index = index
print(df)

print("------------------------------------------------------------")  # 60個

print("二維串列 轉 df")

print("建立資料 np陣列 常態分布 二維串列 3X4")
datas1 = np.random.randn(3, 4)
datas2 = np.random.randn(3, 4)

print("np陣列 轉 df")
df_a = pd.DataFrame(datas1, columns=list("ABCD"))
df_b = pd.DataFrame(datas2, columns=list("ABCD"))

print("合併兩個 df, axis=0 : 垂直連接")
df = pd.concat([df_a, df_b], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("重新設定索引index")
df.index = range(6)
print(df)

print("------------------------------------------------------------")  # 60個

print("二維串列 轉 df")
# 由list組成list
animals = [
    ["鼠", "mouse", 3, "米老鼠"],
    ["牛", "ox", 48, "班尼牛"],
    ["虎", "tiger", 33, "跳跳虎"],
    ["兔", "rabbit", 8, "彼得兔"],
    ["龍", "dragon", 38, "逗逗龍"],
    ["蛇", "snake", 16, "貪吃蛇"],
    ["馬", "horse", 36, "草泥馬"],
    ["羊", "goat", 29, "喜羊羊"],
    ["猴", "monkey", 22, "山道猴"],
    ["雞", "chicken", 6, "肯德雞"],
    ["狗", "dog", 12, "貴賓狗"],
    ["豬", "pig", 42, "佩佩豬"],
]

indexs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
columns = ["中文名", "英文名", "體重", "全名"]
df = pd.DataFrame(animals, columns=columns, index=indexs)
print(df)

for i in range(12):
    print("index :", i, end="\t")
    print("中文名 :", df.iloc[i, 0], end="\t")
    print("體重 :", df.iloc[i, 2], end="\n")

print("全名(第3欄)")
print(df.iloc[0:12, 3])

print("全名(部分)")
print(df.iloc[[3, 6, 9, 11], 3])

print("排序")
df1 = df.sort_values("體重")
print("依體重排序, 檢視前幾行")
print(df1.head())

print("最重 :", df["體重"].max())
print("最輕 :", df["體重"].min())
print("總重 :", df["體重"].sum())
print("平均 :", df["體重"].mean())

print("------------------------------")  # 30個

print("df.iloc[1, :] ->")
print(df.iloc[1, :])
print("df.iloc[1][1] ->")
print(df.iloc[1][1])

print("------------------------------")  # 30個

print('df.loc["陳聰明"]["數學"] (原始)：' + str(df.loc["陳聰明"]["數學"]))
df.loc["陳聰明"]["數學"] = 91
print('df.loc["陳聰明"]["數學"] (修改)：' + str(df.loc["陳聰明"]["數學"]))
print('df.loc["陳聰明", :] ->')
df.loc["陳聰明", :] = 80
print(df.loc["陳聰明", :])

print("------------------------------")  # 30個

print('df["自然"] ->')
print(df["自然"])
print('df[["國文", "數學", "自然"] ->')
print(df[["國文", "數學", "自然"]])
print("df[df.數學>=80] ->")
print(df[df.數學 >= 80])

print("------------------------------")  # 30個

print('df.loc["陳聰明", :] ->')
print(df.loc["陳聰明", :])
# print(df.loc["陳聰明"])
print('df.loc["陳聰明"]["數學"] ->')
print(df.loc["陳聰明"]["數學"])
print('df.loc[("陳聰明", "熊小娟") ->')
print(df.loc[("陳聰明", "熊小娟"), :])
print('df.loc[:, "數學"] ->')
print(df.loc[:, "數學"])
print('df.loc[("陳聰明", "熊小娟"), ("數學", "自然")] ->')
print(df.loc[("陳聰明", "熊小娟"), ("數學", "自然")])
print('df.loc["陳聰明":"熊小娟", "數學":"社會"] ->')
print(df.loc["陳聰明":"熊小娟", "數學":"社會"])
print('df.loc[:黃美麗, "數學":"社會"] ->')
print(df.loc[:"黃美麗", "數學":"社會"])
print('df.loc["陳聰明":, "數學":"社會"] ->')
print(df.loc["陳聰明":, "數學":"社會"])

print("------------------------------")  # 30個

print("修改索引index")
indexs[0] = "林晶輝"
df.index = indexs

print("修改欄名columns")
columns[3] = "理化"
df.columns = columns

print(df)

print("------------------------------")  # 30個

print("按照數學遞減排序 ->")
df1 = df.sort_values(by="數學", ascending=False)
print(df1)

print("按照列標題遞增排序 ->")
df2 = df.sort_index(axis=0)
print(df2)

print("------------------------------")  # 30個

"""
print("移除陳聰明成績 ->")
df1 = df.drop("陳聰明")
print(df1)
print("移除數學科成績 ->")
df2 = df.drop("數學", axis=1)
print(df2)
print("移除數學科及自然科成績 ->")
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)
print("移除陳聰明到熊小娟成績 ->")
df4 = df.drop(df.index[1:4])
print(df4)
print("移除數學科到自然科成績 ->")
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
"""

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["王小明", "李小美", "陳大同", "林小玉"]
columns = ["國文", "英文", "數學", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

scores = {
    "王小明": {"國文": 65, "英文": 92, "數學": 78, "社會": 83, "自然": 70},
    "李小美": {"國文": 90, "英文": 72, "數學": 76, "社會": 93, "自然": 56},
    "陳大同": {"國文": 81, "英文": 85, "數學": 91, "社會": 89, "自然": 77},
    "林小玉": {"國文": 79, "英文": 53, "數學": 47, "社會": 94, "自然": 80},
}
print(type(scores))
print(scores)
df = pd.DataFrame(scores)
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
df = pd.DataFrame(scores)
print(df)
print(type(scores))
print(scores)
print(df)

print(df["自然"])
print(df[["國文", "數學", "自然"]])
print(df[df["國文"] >= 80])
print(df.values[1])
print(df.values[1][2])
# loc
print(df.loc["林小玉", "社會"])
print(df.loc["王小明", ["國文", "社會"]])
print(df.loc[["王小明", "李小美"], ["數學", "自然"]])
print(df.loc["王小明":"陳大同", "數學":"社會"])
print(df.loc["陳大同", :])
print(df.loc[:"李小美", "數學":"社會"])
print(df.loc["李小美":, "數學":"社會"])
print(df.iloc[3, 4])
# iloc
df.iloc[0, [0, 4]]
df.iloc[[0, 1], [2, 3]]
df.iloc[0:3, 2:5]
df.iloc[2, :]
df.iloc[:2, 2:5]
df.iloc[1:, 2:5]

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
df = pd.DataFrame(scores)
print(df)

# 排序
print(df.sort_values(by="數學", ascending=False))
print(df.sort_index(axis=0))
# 修改
df1 = df.loc["王小明"]["數學"] = 90

print("修改後的資料 :\n", df, "\n")

df2 = df.loc["王小明", :] = 80

print("修改後的資料 :\n", df, "\n")

# 刪除
df.drop("王小明")
df.drop("數學", axis=1)
df.drop(["數學", "自然"], axis=1)
df.drop(df.index[1:4])
df.drop(df.columns[1:4], axis=1)

print("修改後的資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

datas = [["mouse", 3], ["ox", 48], ["tiger", 33], ["rabbit", 8]]
indexs = ["鼠", "牛", "虎", "兔"]
columns = ["英文名", "體重"]

df = pd.DataFrame(datas, columns=columns, index=indexs)
print(df)

print("按照數學遞減排序 ->")
df1 = df.sort_values(by="體重", ascending=False)
print(df1)

print("按照列標題遞增排序 ->")
df2 = df.sort_index(axis=0)
print(df2)

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

datas = {
    "林大明": [65, 92, 78, 83, 70],
    "陳聰明": [90, 72, 76, 93, 56],
    "黃美麗": [81, 85, 91, 89, 77],
    "熊小娟": [79, 53, 47, 94, 80],
}

df = pd.DataFrame(datas)
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

datas = {"姓名": ["Alice", "Bob", "Charlie"], "分數": [78, 65, 90]}
df = pd.DataFrame(datas)
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series 合併")

se1 = pd.Series({"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79})
se2 = pd.Series({"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53})
se3 = pd.Series({"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47})
se4 = pd.Series({"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94})
se5 = pd.Series({"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80})

# 方法一
df = pd.concat([se1, se2, se3, se4, se5], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
df.columns = ["國文", "英文", "數學", "自然", "社會"]
print(df)

# 方法二
df = pd.DataFrame({"國文": se1, "英文": se2, "數學": se3, "自然": se4, "社會": se5})
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series")

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
print("2個Series組成一個df")
df = pd.DataFrame([series1, series2])
print(df)

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}
df = pd.DataFrame(data)
print(df)

order_df = pd.DataFrame(
    [[1000, 2546, 103], [1001, 4352, 101], [1002, 342, 101]],
    columns=["id", "item_id", "customer_id"],
)
print(order_df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series")

# 修改 index 和 column 的名稱 –.index、.column

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)

print("2個Series組成一個df")
df = pd.DataFrame([series1, series2])
print(df)

df.index = [1, 2]
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series")

# 加入新的資料列 – append()

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "time": [1, 4, 5, 6, 3],
}

df = pd.DataFrame(data)

series = pd.Series(["FFF", 2008, 7], index=["fruits", "year", "time"])

# NG
# df = df.append(series, ignore_index=True)
# print(df)

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
data3 = [30, 12, 10, 8, 25, 3]

series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)

print("2個Series組成一個df")
df = pd.DataFrame([series1, series2])

index.append("pineapple")

series3 = pd.Series(data3, index=index)

# NG
# df = df.append(series3, ignore_index=True)
# print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series")

# 加入新的欄位

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "time": [1, 4, 5, 6, 3],
}
df = pd.DataFrame(data)
df["price"] = [150, 120, 100, 300, 150]
print(df)

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
print("2個Series組成一個df")
df = pd.DataFrame([series1, series2])
new_column = pd.Series([15, 7], index=[0, 1])
df["FFF"] = new_column
print(df)

print("------------------------------------------------------------")  # 60個

# 取出 DataFrame 當中的元素 –df.loc[]、df.iloc[]

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "time": [1, 4, 5, 6, 3],
}
df = pd.DataFrame(data)
print(df)

df = df.loc[[1, 2], ["time", "year"]]
print(df)

df = pd.DataFrame()
columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df.loc[range(2, 6), ["CCC", "EEE"]]
print(df)

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    # ["AAA", "BBB", "CCC", "DDD", "EEE"]
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}
df = pd.DataFrame(data)
print(df)

df = df.iloc[[1, 3], [0, 2]]
print(df)

print("------------------------------------------------------------")  # 60個

# 刪除 df 物件的列或行 – drop()

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}

df = pd.DataFrame(data)
print(df)

df_1 = df.drop([0, 1])
print(df_1)

df_2 = df.drop("year", axis=1)
print(df_2)

df = pd.DataFrame()
columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df.drop(np.arange(0, 9, 2))
df = df.drop("DDD", axis=1)
print(df)

print("------------------------------------------------------------")  # 60個

# 將欄位值依大小排序 – sort_values()

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "time": [1, 4, 3, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}
df = pd.DataFrame(data)
print(df)

df = df.sort_values(by="year", ascending=True)
print(df)

df = df.sort_values(by=["time", "year"], ascending=True)
print(df)

print("------------------------------------------------------------")  # 60個

# 從 df 物件篩選出想要的資料

data = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}
df = pd.DataFrame(data)
print(df)
print(df.index % 2 == 0)
print(df[df.index % 2 == 0])

df = pd.DataFrame()
columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df[df["AAA"] >= 5]
df = df[df["EEE"] >= 5]
# df = df.loc[df["AAA"] >= 5][df["EEE"] >= 5]
print(df)

print("------------------------------------------------------------")  # 60個

# 索引、欄位內容「一致」時的串接做法

print("建立df, 使用Series 合併")


def make_random_df(index, columns):
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df


columns = ["AAA", "BBB", "CCC"]
df_data1 = make_random_df(range(1, 5), columns)
df_data2 = make_random_df(range(1, 5), columns)

print(df_data1)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df1)

df2 = pd.concat([df_data1, df_data2], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df2)

print("------------------------------------------------------------")  # 60個

# 索引、欄位內容「不一致」時的串接做法

print("建立df, 使用 合併")

columns1 = ["AAA", "BBB", "CCC"]
columns2 = ["DDD", "EEE", "FFF"]

df_data1 = make_random_df(range(1, 5), columns1)
df_data2 = make_random_df(np.arange(1, 8, 2), columns2)

print(df_data1)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df1)

df2 = pd.concat([df_data1, df_data2], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df2)

print("------------------------------------------------------------")  # 60個

# 於橫向串接時增列上一層的欄位

print("建立df, 使用 合併")

columns = ["AAA", "BBB", "CCC"]
df_data1 = make_random_df(range(1, 5), columns)
df_data2 = make_random_df(range(1, 5), columns)
print(df_data1)
print(df_data2)

df = pd.concat(
    [df_data1, df_data2], axis=1, keys=["X", "Y"]
)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

Y_CCC = df["Y", "CCC"]
print(Y_CCC)

print("------------------------------------------------------------")  # 60個

# 用 merge() 做 DataFrame 的交集合併

data1 = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "EEE"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "amount": [1, 4, 5, 6, 3],
}
df1 = pd.DataFrame(data1)
print("df1 :\n", df1)

data2 = {
    "fruits": ["AAA", "BBB", "CCC", "DDD", "FFF"],
    "year": [2001, 2002, 2001, 2008, 2007],
    "price": [150, 120, 100, 250, 3000],
}
df2 = pd.DataFrame(data2)
print("df2 :\n", df2)

df3 = pd.merge(df1, df2, on="fruits", how="inner")
print("df3 :\n", df3)

# 用 merge() 做 DataFrame 的聯集合併
df3 = pd.merge(df1, df2, on="fruits", how="outer")
print("df3 :\n", df3)

# 透過「具關聯性的欄位」合併多個 DataFrame(一)

order_df = pd.DataFrame(
    [[1000, 2546, 103], [1001, 4352, 101], [1002, 342, 101]],
    columns=["id", "item_id", "customer_id"],
)
print("order_df :\n", order_df)

customer_df = pd.DataFrame(
    [[101, "Tanaka"], [102, "Suzuki"], [103, "Kato"]], columns=["id", "name"]
)
print("customer_df :\n", customer_df)

order_df = pd.merge(
    order_df, customer_df, left_on="customer_id", right_on="id", how="inner"
)
print("-----交集合併-----")
print("order_df :\n", order_df)

print("------------------------------------------------------------")  # 60個

# 透過「具關聯性的欄位」合併多個DataFrame (二)

order_df = pd.DataFrame(
    [[1000, 2546, 103], [1001, 4352, 101], [1002, 342, 101]],
    columns=["id", "item_id", "customer_id"],
)

print("----訂貨紀錄----\n", order_df)

customer_df = pd.DataFrame([["Tanaka"], ["Suzuki"], ["Kato"]], columns=["name"])

customer_df.index = [101, 102, 103]

print("----客戶資訊----\n", customer_df)

order_df = pd.merge(
    order_df, customer_df, left_on="customer_id", right_index=True, how="inner"
)

print("----order_df----\n", order_df)

print("------------------------------------------------------------")  # 60個

# 將 DataFrame 的內容寫入到 CSV 檔

data = {
    "city": [
        "Nagano",
        "Sydney",
        "Salt Lake City",
        "Athens",
        "Torino",
        "Beijing",
        "Vancouver",
        "London",
        "Sochi",
        "Rio de Janeiro",
    ],
    "year": [1998, 2000, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016],
    "season": [
        "winter",
        "summer",
        "winter",
        "summer",
        "winter",
        "summer",
        "winter",
        "summer",
        "winter",
        "summer",
    ],
}
df = pd.DataFrame(data)

print("------------------------------------------------------------")  # 60個

# 處理 DataFrame 中的缺漏值
# 用 dropna() 刪除含有 NaN ( 缺漏值 ) 的列

#   借用 NumPy 的 np.nan 來設定 NaN 值

sample_df = pd.DataFrame(np.random.rand(8, 4))

#   設定亂數種子為 0

#   用 NumPy 隨機產生 8x4 的亂數資料並轉成 DataFrame

sample_df.iloc[1, 0] = np.nan

sample_df.iloc[2, 2] = np.nan

sample_df.iloc[6, 1] = np.nan

sample_df.iloc[5:, 3] = np.nan

#   將部分值改成 NaN

print(sample_df)

#   檢視 DataFrame

sample_df_dropped = sample_df.dropna()

print(sample_df_dropped)

sample_df_dropped_2 = sample_df[[0, 1, 2]].dropna()

print(sample_df_dropped_2)

print("------------------------------------------------------------")  # 60個

# 用 fllna() 填補 NaN 值

sample_df = pd.DataFrame(np.random.rand(8, 4))

sample_df.iloc[1, 0] = np.nan

sample_df.iloc[2, 2] = np.nan

sample_df.iloc[6, 1] = np.nan

sample_df.iloc[5:, 3] = np.nan

sample_df_fill = sample_df.fillna(0)  # 在 NaN 之處填入 0

print(sample_df_fill)

sample_df_fill_2 = sample_df.fillna(method="ffill")

print(sample_df_fill_2)

print(sample_df)

sample_df_fill_3 = sample_df.fillna(sample_df.mean())

print(sample_df_fill_3)

print("------------------------------------------------------------")  # 60個

# duplicated()、drop_duplicated() - 尋找或刪除 DataFrame 內重複的資料

dupli_df = pd.DataFrame(
    {"col1": [1, 1, 2, 3, 4, 4, 5, 5], "col2": ["a", "b", "b", "b", "c", "c", "b", "b"]}
)
print(dupli_df)
print(dupli_df.duplicated())

print("------------------------------------------------------------")  # 60個

# map() - 利用 DataFrame 的既有欄位生成新的欄位

people_data = {
    "ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"],
    "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
    "name": [
        "Hiroshi",
        "Akiko",
        "Yuki",
        "Satoru",
        "Steeve",
        "Mituru",
        "Aoi",
        "Tarou",
        "Suguru",
        "Mitsuo",
    ],
    "city": ["東京", "大阪", "京都", "札幌", "東京", "東京", "大阪", "京都", "札幌", "東京"],
}

people_df = pd.DataFrame(people_data)
print(people_df)

city_map = {"東京": "關東", "札幌": "北海道", "大阪": "關西", "京都": "關西"}

print(people_df["city"].map(city_map))

people_df["region"] = people_df["city"].map(city_map)

print(people_df)

print("------------------------------------------------------------")  # 60個

# 用 cut() 劃分、篩選資料

people_data = {
    "ID": ["100", "101", "102", "103", "104", "106", "108", "110", "111", "113"],
    "name": [
        "Hiroshi",
        "Akiko",
        "Yuki",
        "Satoru",
        "Steeve",
        "Mituru",
        "Aoi",
        "Tarou",
        "Suguru",
        "Mitsuo",
    ],
    "birth_year": [1990, 1989, 1992, 1997, 1982, 1991, 1988, 1990, 1995, 1981],
}

people_df = pd.DataFrame(people_data)
print(people_df)

birth_year_cut = pd.cut(people_df["birth_year"], 4)

print(birth_year_cut)

print(pd.value_counts(birth_year_cut))

birth_year_bins = [1980, 1985, 1990, 1995, 2000]

birth_year_bins_labels = [
    "Born in 81~85",
    "Born in 86~90",
    "Born in 91~95",
    "Born in 96~2000",
]

birth_year_cut = pd.cut(
    people_df["birth_year"], birth_year_bins, labels=birth_year_bins_labels
)

print(pd.value_counts(birth_year_cut))
print(birth_year_cut)

people_df["birth_year_bin"] = birth_year_cut

print(people_df)

print("------------------------------------------------------------")  # 60個

columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

df = pd.DataFrame()
print(df)

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]
print(df)

print("------------------------------------------------------------")  # 60個

# 對 DataFrame 的值做運算

columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

df = pd.DataFrame()
print(df)

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]
print(df)

double_df = df * 2

square_df = df * df

sqrt_df = np.sqrt(df)

print("----double_df----\n", double_df)

print("----square_df----\n", square_df)

print("----sqrt_df----\n", sqrt_df)

print("------------------------------------------------------------")  # 60個

columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

df = pd.DataFrame()
print(df)

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]
print(df)

print("------------------------------------------------------------")  # 60個

# 計算行(列)之間的差 (diff)

columns = ["AAA", "BBB", "CCC", "DDD", "EEE"]

df = pd.DataFrame()
print(df)

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]
print(df)

df_diff = df.diff(-2, axis=0)

print(df_diff)

print("------------------------------------------------------------")  # 60個

# 用 groupy() 做分組統計

prefecture_df = pd.DataFrame(
    [
        ["Tokyo", 2190, 13636, "Kanto"],
        ["Kanagawa", 2415, 9145, "Kanto"],
        ["Osaka", 1904, 8837, "Kinki"],
        ["Kyoto", 4610, 2605, "Kinki"],
        ["Aichi", 5172, 7505, "Chubu"],
    ],
    columns=["Prefecture", "Area", "Population", "Region"],
)
print(prefecture_df)

grouped_region = prefecture_df.groupby("Region")

# NG
# mean_df = grouped_region.mean()
# print(mean_df)

print("------------------------------------------------------------")  # 60個

dates = pd.date_range("20160101", periods=6)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["A", "B", "C", "D"])
print(df["B"])

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)
print(df2.dtypes)

print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))

print("------------------------------------------------------------")  # 60個

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["A", "B", "C", "D"])

print(df["A"], df.A)
print(df[0:3], df["20130102":"20130104"])

# select by label: loc
print(df.loc["20130102"])
print(df.loc[:, ["A", "B"]])
print(df.loc["20130102", ["A", "B"]])

# select by position: iloc
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])

""" no ix
# mixed selection: ix
print(df.ix[:3, ["A", "C"]])
# Boolean indexing
print(df[df.A > 0])
"""
print("------------------------------------------------------------")  # 60個

datas = np.random.randn(6, 4)
columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, columns=columns, index=dates)

df.iloc[2, 2] = 1111
df.loc["2013-01-03", "D"] = 2222
df.A[df.A > 0] = 0
df["F"] = np.nan
df["G"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
print(df)

print("------------------------------------------------------------")  # 60個

datas = np.arange(24).reshape((6, 4))
columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, columns=columns, index=dates)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how="any"))  # how={'any', 'all'}
print(df.fillna(value=0))
print(pd.isnull(df))

print("------------------------------------------------------------")  # 60個

print("建立df 二維串列 常態分佈二維串列 6X4, 設定欄名")

datas = np.random.randn(6, 4)
columns = list("ABCD")
df = pd.DataFrame(datas, columns=columns)
print(df)

print("顯示第0列")
cc = df.iloc[0]
print(cc)

print("顯示A欄")
cc = df.A
print(cc)

print("顯示df之3:5")
print(df[3:5])

print("顯示df之A B D欄")
print(df[["A", "B", "D"]])

print("顯示")
print(df.loc[3, "A"])

print("顯示")
print(df.iloc[3, 0])

print("顯示")
print(df.iloc[2:5, 0:2])

print("顯示")
print(df[df.C > 0])

print("排序 axis=1")
print(df.sort_index(axis=1, ascending=False))

print("依B欄排序")
print(df.sort_values(by="B"))

print("加入TAG")
df["TAG"] = ["cat", "dog", "cat", "cat", "cat", "dog"]
print(df)

print(df.groupby("TAG").sum())

print("------------------------------------------------------------")  # 60個

print("建立df, 使用 合併")

# concatenating
# ignore index
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=["a", "b", "c", "d"])
res = pd.concat(
    [df1, df2, df3], axis=0, ignore_index=True
)  # axis=0 : 垂直連接, axis=1 : 水平連接

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["b", "c", "d", "e"], index=[2, 3, 4])
res = pd.concat([df1, df2], axis=1, join="outer")  # axis=0 : 垂直連接, axis=1 : 水平連接
res = pd.concat([df1, df2], axis=1, join="inner")  # axis=0 : 垂直連接, axis=1 : 水平連接

""" NG
# join_axes
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])  # axis=0 : 垂直連接, axis=1 : 水平連接
"""

# append
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["b", "c", "d", "e"], index=[2, 3, 4])

""" NG append
res = df1.append(df2, ignore_index=True)
res = df1.append([df2, df3])

s1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
res = df1.append(s1, ignore_index=True)

print(res)
"""
print("------------------------------------------------------------")  # 60個

# merging two df by key/keys. (may be used in database)
# simple example
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
print(left)
print(right)
res = pd.merge(left, right, on="key")
print(res)

# consider two keys
left = pd.DataFrame(
    {
        "key1": ["K0", "K0", "K1", "K2"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)
right = pd.DataFrame(
    {
        "key1": ["K0", "K1", "K1", "K2"],
        "key2": ["K0", "K0", "K0", "K0"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)
print(left)
print(right)
res = pd.merge(left, right, on=["key1", "key2"], how="inner")  # default for how='inner'
# how = ['left', 'right', 'outer', 'inner']
res = pd.merge(left, right, on=["key1", "key2"], how="left")
print(res)

# indicator
df1 = pd.DataFrame({"col1": [0, 1], "col_left": ["a", "b"]})
df2 = pd.DataFrame({"col1": [1, 2, 2], "col_right": [2, 2, 2]})
print(df1)
print(df2)
res = pd.merge(df1, df2, on="col1", how="outer", indicator=True)
# give the indicator a custom name
res = pd.merge(df1, df2, on="col1", how="outer", indicator="indicator_column")

# merged by index
left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)
right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)
print(left)
print(right)
# left_index and right_index
res = pd.merge(left, right, left_index=True, right_index=True, how="outer")
res = pd.merge(left, right, left_index=True, right_index=True, how="inner")

# handle overlapping
boys = pd.DataFrame({"k": ["K0", "K1", "K2"], "age": [1, 2, 3]})
girls = pd.DataFrame({"k": ["K0", "K0", "K3"], "age": [4, 5, 6]})
res = pd.merge(boys, girls, on="k", suffixes=["_boy", "_girl"], how="inner")
print(res)

# join function in pandas is similar with merge. If know merge, you will understand join

print("------------------------------------------------------------")  # 60個

"""
print("畫出來")

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
##data.plot()

# DataFrame
data = pd.DataFrame(
    np.random.randn(1000, 4), index=np.arange(1000), columns=list("ABCD")
)
data = data.cumsum()
# plot methods:
# 'bar', 'hist', 'box', 'kde', 'area', scatter', hexbin', 'pie'
ax = data.plot.scatter(x="A", y="B", color="DarkBlue", label="Class 1")
data.plot.scatter(x="A", y="C", color="LightGreen", label="Class 2", ax=ax)

plt.show()
"""

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 讀取[Chipotle快餐數據]資料集至df
orders = pd.read_table("http://bit.ly/chiporders")
# filename = "data/chipotle.tsv"
# orders = pd.read_csv(filename) # NG

print("檢視前幾行")
cc = orders.head()
print(cc)

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ["user_id", "age", "gender", "occupation", "zip_code"]
users = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=user_cols)

print("檢視前幾行")
cc = users.head()
print(cc)

print("------------------------------------------------------------")  # 60個

# 讀取[UFO報告]資料集至df
# ufo = pd.read_table('http://bit.ly/uforeports', sep=',')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, sep=",")

# read_csv is equivalent to read_table, except it assumes a comma separator
# 讀取[UFO報告]資料集至df
ufo = pd.read_csv("http://bit.ly/uforeports")
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視前幾行")
cc = ufo.head()
print(cc)

# select the 'City' Series using bracket notation
ufo["City"]

# or equivalently, use dot notation
cc = ufo.City
print(cc)

# create a new 'Location' Series (must use bracket notation to define the Series name)
ufo["Location"] = ufo.City + ", " + ufo.State
cc = ufo.head()
print(cc)

print("------------------------------------------------------------")  # 60個

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

print("檢視前幾行")
cc = movies.head()
print(cc)

# example method: calculate summary statistics
cc = movies.describe()  # 方法有()
print(cc)

# example attribute: number of rows and columns
print("movies之大小")
cc = movies.shape  # 屬性無()
print(cc)

# example attribute: data type of each column
cc = movies.dtypes
print(cc)

# use an optional parameter to the describe method to summarize only 'object' columns
cc = movies.describe(include=["object"])
print(cc)

print("------------------------------------------------------------")  # 60個

print("rename pd 之 df")

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢查欄名")
cc = ufo.columns
print(cc)

# Index([u'City', u'Colors Reported', u'Shape Reported', u'State', u'Time'], dtype='object')

# rename two of the columns by using the 'rename' method
ufo.rename(
    columns={"Colors Reported": "Colors_Reported", "Shape Reported": "Shape_Reported"},
    inplace=True,
)
cc = ufo.columns
print(cc)

# Index([u'City', u'Colors_Reported', u'Shape_Reported', u'State', u'Time'], dtype='object')

# Documentation for rename

# replace all of the column names by overwriting the 'columns' attribute
ufo_cols = ["city", "colors reported", "shape reported", "state", "time"]
ufo.columns = ufo_cols

print(ufo.columns)

# replace the column names during the file reading process by using the 'names' parameter
# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', header=0, names=ufo_cols)
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, header=0, names=ufo_cols)

cc = ufo.columns
print(cc)

# Index([u'city', u'colors reported', u'shape reported', u'state', u'time'], dtype='object')

# Documentation for read_csv

# replace all spaces with underscores in the column names by using the 'str.replace' method
ufo.columns = ufo.columns.str.replace(" ", "_")
cc = ufo.columns

print(cc)

print("------------------------------------------------------------")  # 60個

# How do I remove columns from a pandas DataFrame? (video)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視前幾行")
cc = ufo.head()
print(cc)

# remove a single column (axis=1 refers to columns)
ufo.drop("Colors Reported", axis=1, inplace=True)
print("檢視前幾行")
cc = ufo.head()
print(cc)

# remove multiple columns at once
ufo.drop(["City", "State"], axis=1, inplace=True)
print("檢視前幾行")
cc = ufo.head()
print(cc)

# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)
print("檢視前幾行")
cc = ufo.head()
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I sort a pandas DataFrame or a Series? (video)

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

print("檢視前幾行")
cc = movies.head()
print(cc)

# sort the 'title' Series in ascending order (returns a Series)
print("檢視前幾行")
cc = movies.title.sort_values().head()
print(cc)

# sort in descending order instead
print("檢視前幾行")
cc = movies.title.sort_values(ascending=False).head()
print(cc)

# sort the entire DataFrame by the 'title' Series (returns a DataFrame)
print("檢視前幾行")
cc = movies.sort_values("title").head()
print(cc)

# sort in descending order instead
print("檢視前幾行")
cc = movies.sort_values("title", ascending=False).head()
print(cc)

# sort the DataFrame first by 'content_rating', then by 'duration'
print("檢視前幾行")
cc = movies.sort_values(["content_rating", "duration"]).head()
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I filter rows of a pandas DataFrame by column value? (video)

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

print("檢視前幾行")
cc = movies.head()
print(cc)

# examine the number of rows and columns
print("movies之大小")
cc = movies.shape
print(cc)

# create a list in which each element refers to a DataFrame row: True if the row satisfies the condition, False otherwise
booleans = []
for length in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

# confirm that the list has the same length as the DataFrame
cc = len(booleans)
print(cc)

# examine the first five list elements
cc = booleans[0:5]
print(cc)

# convert the list to a Series
is_long = pd.Series(booleans)
print("檢視前幾行")
cc = is_long.head()
print(cc)

# use bracket notation with the boolean Series to tell the DataFrame which rows to display
cc = movies[is_long]
print(cc)

# simplify the steps above: no need to write a for loop to create 'is_long' since pandas will broadcast the comparison
is_long = movies.duration >= 200
cc = movies[is_long]
print(cc)

# or equivalently, write it in one line (no need to create the 'is_long' object)
cc = movies[movies.duration >= 200]
print(cc)

# select the 'genre' Series from the filtered DataFrame
cc = movies[movies.duration >= 200].genre
print(cc)

# or equivalently, use the 'loc' method
cc = movies.loc[movies.duration >= 200, "genre"]
print(cc)

print("------------------------------------------------------------")  # 60個

# 9. How do I apply multiple filter criteria to a pandas DataFrame? (video)

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

print("檢視前幾行")
cc = movies.head()
print(cc)

# filter the DataFrame to only show movies with a 'duration' of at least 200 minutes
cc = movies[movies.duration >= 200]
print(cc)

# CORRECT: use the '&' operator to specify that both conditions are required
cc = movies[(movies.duration >= 200) & (movies.genre == "Drama")]
print(cc)

# 錯誤
# INCORRECT: using the '|' operator would have shown movies that are either long or dramas (or both)
print("檢視前幾行")
cc = movies[(movies.duration >= 200) | (movies.genre == "Drama")].head()
print(cc)

# use the '|' operator to specify that a row can match any of the three criteria
cc = movies[
    (movies.genre == "Crime") | (movies.genre == "Drama") | (movies.genre == "Action")
].head(10)
print(cc)

# or equivalently, use the 'isin' method
cc = movies[movies.genre.isin(["Crime", "Drama", "Action"])].head(10)
print(cc)

print("------------------------------------------------------------")  # 60個

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

cc = ufo.columns
print(cc)

# specify which columns to include by name
# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', usecols=['City', 'State'])
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, usecols=["City", "State"])

print(ufo)

# or equivalently, specify columns by position
# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', usecols=[0, 4])
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, usecols=[0, 4])

cc = ufo.columns
print(cc)

# 只讀一部份
# specify how many rows to read
# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', nrows=3)
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, nrows=3)

print(ufo)

# Series are directly iterable (like a list)
for c in ufo.City:
    print(c)


# various methods are available to iterate through a DataFrame
for index, row in ufo.iterrows():
    print(index, row.City, row.State)

# Question: How do I drop all non-numeric columns from a DataFrame?

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

cc = drinks.dtypes
print(cc)

# only include numeric columns in the DataFrame
cc = drinks.select_dtypes(include=[np.number]).dtypes
print(cc)

# describe all of the numeric columns
cc = drinks.describe()
print(cc)

# pass the string 'all' to describe all columns
cc = drinks.describe(include="all")
print(cc)

# pass a list of data types to only describe certain types
cc = drinks.describe(include=["object", "float64"])
print(cc)

# pass a list even if you only want to describe a single data type
cc = drinks.describe(include=["object"])
print(cc)

print("------------------------------------------------------------")  # 60個

print("使用 axis")

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# drop a column (temporarily)
print("檢視前幾行")
cc = drinks.drop("continent", axis=1).head()
print(cc)

# drop a row (temporarily)
print("檢視前幾行")
cc = drinks.drop(2, axis=0).head()
print(cc)

"""
# calculate the mean of each numeric column
#cc = drinks.mean()  NG
#print(cc)

# or equivalently, specify the axis explicitly
drinks.mean(axis=0)

# calculate the mean of each row
print('檢視前幾行')
cc = drinks.mean(axis=1).head()
print(cc)


# 'index' is an alias for axis 0
drinks.mean(axis='index')


# 'columns' is an alias for axis 1
print('檢視前幾行')
cc = drinks.mean(axis='columns').head()
print(cc)
"""

print("------------------------------------------------------------")  # 60個

# How do I use string methods in pandas? (video)

# 讀取[Chipotle快餐數據]資料集至df
orders = pd.read_table("http://bit.ly/chiporders")
# filename = "data/chipotle.tsv"
# orders = pd.read_csv(filename) # NG

print("檢視前幾行")
cc = orders.head()
print(cc)

# string methods for pandas Series are accessed via 'str'
print("檢視前幾行")
cc = orders.item_name.str.upper().head()
print(cc)

# string method 'contains' checks for a substring and returns a boolean Series
print("檢視前幾行")
cc = orders.item_name.str.contains("Chicken").head()
print(cc)

# use the boolean Series to filter the DataFrame
print("檢視前幾行")
cc = orders[orders.item_name.str.contains("Chicken")].head()
print(cc)

# string methods can be chained together
print("檢視前幾行")
cc = orders.choice_description.str.replace("[", "").str.replace("]", "").head()
print(cc)

# many pandas string methods support regular expressions (regex)
print("檢視前幾行")
cc = orders.choice_description.str.replace("[\[\]]", "").head()
print(cc)

print("------------------------------------------------------------")  # 60個

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# examine the data type of each Series
print("檢視資料型態")
cc = drinks.dtypes
print(cc)

# change the data type of an existing Series
drinks["beer_servings"] = drinks.beer_servings.astype(float)
cc = drinks.dtypes
print(cc)

# alternatively, change the data type of a Series while reading in a file
drinks = pd.read_csv("http://bit.ly/drinksbycountry", dtype={"beer_servings": float})
cc = drinks.dtypes
print(cc)

# 讀取[Chipotle快餐數據]資料集至df
orders = pd.read_table("http://bit.ly/chiporders")
# filename = "data/chipotle.tsv"
# orders = pd.read_csv(filename) # NG

print("檢視前幾行")
cc = orders.head()
print(cc)

# examine the data type of each Series
cc = orders.dtypes
print(cc)

# convert a string to a number in order to do math
cc = orders.item_price.str.replace("$", "").astype(float).mean()
print(cc)

# string method 'contains' checks for a substring and returns a boolean Series
print("檢視前幾行")
cc = orders.item_name.str.contains("Chicken").head()
print(cc)

# convert a boolean Series to an integer (False = 0, True = 1)
print("檢視前幾行")
cc = orders.item_name.str.contains("Chicken").astype(int).head()
print(cc)

print("------------------------------------------------------------")  # 60個

# When should I use a "groupby" in pandas? (video)

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

"""
# calculate the mean beer servings across the entire dataset
drinks.beer_servings.mean()

# calculate the mean beer servings just for countries in Africa
drinks[drinks.continent=='Africa'].beer_servings.mean()

# calculate the mean beer servings for each continent
drinks.groupby('continent').beer_servings.mean()

# other aggregation functions (such as 'max') can also be used with groupby
drinks.groupby('continent').beer_servings.max()

# multiple aggregation functions can be applied simultaneously
drinks.groupby('continent').beer_servings.agg(['count', 'mean', 'min', 'max'])

# specifying a column to which the aggregation function should be applied is not required
drinks.groupby('continent').mean()

# side-by-side bar plot of the DataFrame directly above
drinks.groupby('continent').mean().plot(kind='bar')

"""
print("------------------------------------------------------------")  # 60個

# How do I explore a pandas Series? (video)

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

print("檢視前幾行")
cc = movies.head()
print(cc)

# examine the data type of each Series
cc = movies.dtypes
print(cc)

# count the non-null values, unique values, and frequency of the most common value
cc = movies.genre.describe()
print(cc)

# count how many times each value in the Series occurs
cc = movies.genre.value_counts()
print(cc)

# display percentages instead of raw counts
cc = movies.genre.value_counts(normalize=True)
print(cc)

# 'value_counts' (like many pandas methods) outputs a Series
cc = type(movies.genre.value_counts())
print(cc)

# thus, you can add another Series method on the end
print("檢視前幾行")
cc = movies.genre.value_counts().head()
print(cc)

# display the unique values in the Series
cc = movies.genre.unique()
print(cc)

# count the number of unique values in the Series
cc = movies.genre.nunique()
print(cc)

# compute a cross-tabulation of two Series
cc = pd.crosstab(movies.genre, movies.content_rating)
print(cc)

# calculate various summary statistics
cc = movies.duration.describe()
print(cc)

# many statistics are implemented as Series methods
cc = movies.duration.mean()
print(cc)

# 'value_counts' is primarily useful for categorical data, not numerical data
print("檢視前幾行")
cc = movies.duration.value_counts().head()
print(cc)

# histogram of the 'duration' Series (shows the distribution of a numerical variable)
movies.duration.plot(kind="hist")

plt.show()

# bar plot of the 'value_counts' for the 'genre' Series
movies.genre.value_counts().plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

# How do I handle missing values in pandas? (video)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視後幾行")
cc = ufo.tail()
print(cc)

print("找出缺少資料的項目")
# 'isnull' returns a DataFrame of booleans (True if missing, False if not missing)
print("檢視後幾行")
cc = ufo.isnull().tail()
print(cc)

print("找出缺少資料的項目")
# 'nonnull' returns the opposite of 'isnull' (True if not missing, False if missing)
print("檢視後幾行")
cc = ufo.notnull().tail()
print(cc)

# count the number of missing values in each Series
cc = ufo.isnull().sum()
print(cc)

# use the 'isnull' Series method to filter the DataFrame rows
print("檢視前幾行")
cc = ufo[ufo.City.isnull()].head()
print(cc)

# examine the number of rows and columns
print("ufo之大小")
cc = ufo.shape
print(cc)

# if 'any' values are missing in a row, then drop that row
print("ufo之大小")
ufo.dropna(how="any").shape

# 'inplace' parameter for 'dropna' is False by default, thus rows were only dropped temporarily
print("ufo之大小")
cc = ufo.shape
print(cc)

# if 'all' values are missing in a row, then drop that row (none are dropped in this case)
print("ufo之大小")
cc = ufo.dropna(how="all").shape
print(cc)

# if 'any' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
print("ufo之大小")
cc = ufo.dropna(subset=["City", "Shape Reported"], how="any").shape
print(cc)

# if 'all' values are missing in a row (considering only 'City' and 'Shape Reported'), then drop that row
print("ufo之大小")
cc = ufo.dropna(subset=["City", "Shape Reported"], how="all").shape
print(cc)

# 'value_counts' does not include missing values by default
print("檢視前幾行")
cc = ufo["Shape Reported"].value_counts().head()
print(cc)

# explicitly include missing values
print("檢視前幾行")
cc = ufo["Shape Reported"].value_counts(dropna=False).head()
print(cc)

# fill in missing values with a specified value
ufo["Shape Reported"].fillna(value="VARIOUS", inplace=True)

# confirm that the missing values were filled in
print("檢視前幾行")
cc = ufo["Shape Reported"].value_counts().head()
print(cc)

print("------------------------------------------------------------")  # 60個

# pandas index

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# every DataFrame has an index (sometimes called the "row labels")
cc = drinks.index
print(cc)

# column names are also stored in a special "index" object
cc = drinks.columns
print(cc)

# neither the index nor the columns are included in the shape
print("drinks之大小")
cc = drinks.shape
print(cc)

# index and columns both default to integers if you don't define them
print("檢視前幾行")
cc = pd.read_table("http://bit.ly/movieusers", header=None, sep="|").head()
print(cc)

# identification: index remains with each row when filtering the DataFrame
cc = drinks[drinks.continent == "South America"]
print(cc)

# selection: select a portion of the DataFrame using the index
cc = drinks.loc[23, "beer_servings"]
print(cc)

# set an existing column as the index
drinks.set_index("country", inplace=True)
print("檢視前幾行")
cc = drinks.head()
print(cc)

# 'country' is now the index
drinks.index

# 'country' is no longer a column
drinks.columns

# 'country' data is no longer part of the DataFrame contents
print("drinks之大小")
cc = drinks.shape
print(cc)

# country name can now be used for selection
cc = drinks.loc["Brazil", "beer_servings"]
print(cc)

# index name is optional
drinks.index.name = None
print("檢視前幾行")
cc = drinks.head()
print(cc)

# restore the index name, and move the index back to a column
drinks.index.name = "country"
drinks.reset_index(inplace=True)
print("檢視前幾行")
cc = drinks.head()
print(cc)

# many DataFrame methods output a DataFrame
cc = drinks.describe()
print(cc)

# you can interact with any DataFrame using its index and columns
cc = drinks.describe().loc["25%", "beer_servings"]
print(cc)

print("------------------------------------------------------------")  # 60個

# pandas index

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# every DataFrame has an index
cc = drinks.index
print(cc)
# RangeIndex(start=0, stop=193, step=1)

# every Series also has an index (which carries over from the DataFrame)
print("檢視前幾行")
cc = drinks.continent.head()
print(cc)

# set 'country' as the index
drinks.set_index("country", inplace=True)

# Series index is on the left, values are on the right
print("檢視前幾行")
cc = drinks.continent.head()
print(cc)

# another example of a Series (output from the 'value_counts' method)
cc = drinks.continent.value_counts()
print(cc)

# access the Series index
cc = drinks.continent.value_counts().index
print(cc)

# access the Series values
cc = drinks.continent.value_counts().values
print(cc)

# elements in a Series can be selected by index (using bracket notation)
cc = drinks.continent.value_counts()["Africa"]
print(cc)

# any Series can be sorted by its values
cc = drinks.continent.value_counts().sort_values()
print(cc)

# any Series can also be sorted by its index
cc = drinks.continent.value_counts().sort_index()
print(cc)

# 'beer_servings' Series contains the average annual beer servings per person
print("檢視前幾行")
cc = drinks.beer_servings.head()
print(cc)

# create a Series containing the population of two countries
people = pd.Series([3000000, 85000], index=["Albania", "Andorra"], name="population")
people

# calculate the total annual beer servings for each country
print("檢視前幾行")
cc = (drinks.beer_servings * people).head()
print(cc)

# concatenate the 'drinks' DataFrame with the 'population' Series (aligns by the index)
print("檢視前幾行")
cc = pd.concat([drinks, people], axis=1).head()  # axis=0 : 垂直連接, axis=1 : 水平連接
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I select multiple rows and columns from a pandas DataFrame? (video)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視前3行")
cc = ufo.head(3)
print(cc)

# row 0, all columns
ufo.loc[0, :]

# rows 0 and 1 and 2, all columns
ufo.loc[[0, 1, 2], :]

# rows 0 through 2 (inclusive), all columns
ufo.loc[0:2, :]

# this implies "all columns", but explicitly stating "all columns" is better
ufo.loc[0:2]

# rows 0 through 2 (inclusive), column 'City'
ufo.loc[0:2, "City"]

# rows 0 through 2 (inclusive), columns 'City' and 'State'
ufo.loc[0:2, ["City", "State"]]

# accomplish the same thing using double brackets - but using 'loc' is preferred since it's more explicit
print("檢視前3行")
cc = ufo[["City", "State"]].head(3)
print(cc)

# rows 0 through 2 (inclusive), columns 'City' through 'State' (inclusive)
ufo.loc[0:2, "City":"State"]

# accomplish the same thing using 'head' and 'drop'
print("檢視前3行")
cc = ufo.head(3).drop("Time", axis=1)
print(cc)

# rows in which the 'City' is 'Oakland', column 'State'
cc = ufo.loc[ufo.City == "Oakland", "State"]
print(cc)

# accomplish the same thing using "chained indexing" - but using 'loc' is preferred since chained indexing can cause problems
cc = ufo[ufo.City == "Oakland"].State
print(cc)

# rows in positions 0 and 1, columns in positions 0 and 3
cc = ufo.iloc[[0, 1], [0, 3]]
print(cc)

# rows in positions 0 through 2 (exclusive), columns in positions 0 through 4 (exclusive)
cc = ufo.iloc[0:2, 0:4]
print(cc)

# rows in positions 0 through 2 (exclusive), all columns
cc = ufo.iloc[0:2, :]
print(cc)

# accomplish the same thing - but using 'iloc' is preferred since it's more explicit
cc = ufo[0:2]
print(cc)

# read a dataset of alcohol consumption into a DataFrame and set 'country' as the index
drinks = pd.read_csv("http://bit.ly/drinksbycountry", index_col="country")
print("檢視前幾行")
cc = drinks.head()
print(cc)

print("------------------------------------------------------------")  # 60個

# "inplace"

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視前幾行")
cc = ufo.head()
print(cc)

print("ufo之大小")
cc = ufo.shape
print(cc)

# remove the 'City' column (doesn't affect the DataFrame since inplace=False)
print("檢視前幾行")
cc = ufo.drop("City", axis=1).head()
print(cc)

# confirm that the 'City' column was not actually removed
print("檢視前幾行")
cc = ufo.head()
print(cc)

# remove the 'City' column (does affect the DataFrame since inplace=True)
cc = ufo.drop("City", axis=1, inplace=True)
print(cc)

# confirm that the 'City' column was actually removed
print("檢視前幾行")
cc = ufo.head()
print(cc)

# drop a row if any value is missing from that row (doesn't affect the DataFrame since inplace=False)
print("ufo之大小")
cc = ufo.dropna(how="any").shape
print(cc)
# (2490, 4)

# confirm that no rows were actually removed
print("ufo之大小")
cc = ufo.shape
print(cc)
# (18241, 4)

# use an assignment statement instead of the 'inplace' parameter
ufo = ufo.set_index("Time")
print("檢視後幾行")
cc = ufo.tail()
print(cc)

# fill missing values using "backward fill" strategy (doesn't affect the DataFrame since inplace=False)
print("檢視後幾行")
cc = ufo.fillna(method="bfill").tail()
print(cc)

# compare with "forward fill" strategy (doesn't affect the DataFrame since inplace=False)
print("檢視後幾行")
cc = ufo.fillna(method="ffill").tail()
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I make my pandas DataFrame smaller and faster? (video)

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# exact memory usage is unknown because object columns are references elsewhere
cc = drinks.info()
print(cc)

# force pandas to calculate the true memory usage
cc = drinks.info(memory_usage="deep")
print(cc)

# calculate the memory usage for each Series (in bytes)
cc = drinks.memory_usage(deep=True)
print(cc)

# use the 'category' data type (new in pandas 0.15) to store the 'continent' strings as integers
drinks["continent"] = drinks.continent.astype("category")
print(drinks.dtypes)

# 'continent' Series appears to be unchanged
print("檢視前幾行")
cc = drinks.continent.head()
print(cc)

# strings are now encoded (0 means 'Africa', 1 means 'Asia', 2 means 'Europe', etc.)
print("檢視前幾行")
cc = drinks.continent.cat.codes.head()
print(cc)

# memory usage has been drastically reduced
cc = drinks.memory_usage(deep=True)
print(cc)

# repeat this process for the 'country' Series
drinks["country"] = drinks.country.astype("category")
cc = drinks.memory_usage(deep=True)
print(cc)

# memory usage increased because we created 193 categories
cc = drinks.country.cat.categories
print(cc)

print("建立df, 字典轉df")
# create a small DataFrame from a dictionary
df = pd.DataFrame(
    {"ID": [100, 101, 102, 103], "quality": ["good", "very good", "good", "excellent"]}
)
print(df)

# sort the DataFrame by the 'quality' Series (alphabetical order)
cc = df.sort_values("quality")
print(cc)

# sort the DataFrame by the 'quality' Series (logical order)
cc = df.sort_values("quality")
print(cc)

# comparison operators work with ordered categories
cc = df.loc[df.quality > "good", :]
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I use pandas with scikit-learn to create Kaggle submissions? (video)

# 讀取[Kaggle's Titanic competition]資料集至df
# train = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
train = pd.read_csv(filename)

print("檢視前幾行")
cc = train.head()
print(cc)

# create a feature matrix 'X' by selecting two DataFrame columns
feature_cols = ["Pclass", "Parch"]
X = train.loc[:, feature_cols]
print("X之大小")
cc = X.shape
print(cc)

# create a response vector 'y' by selecting a Series
y = train.Survived
print("y之大小")
cc = y.shape
print(cc)

# fit a classification model to the training data
from sklearn.linear_model import LogisticRegression

logreg = LogisticRegression()
logreg.fit(X, y)

# read the testing dataset from Kaggle's Titanic competition into a DataFrame
test = pd.read_csv("http://bit.ly/kaggletest")
print("檢視前幾行")
cc = test.head()
print(cc)

# create a feature matrix from the testing data that matches the training data
X_new = test.loc[:, feature_cols]
print("X_new之大小")
cc = X_new.shape
print(cc)

# use the fitted model to make predictions for the testing set observations
new_pred_class = logreg.predict(X_new)

# create a DataFrame of passenger IDs and testing set predictions
print("檢視前幾行")
cc = pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).head()
print(cc)

# ensure that PassengerID is the first column by setting it as the index
print("檢視前幾行")
cc = (
    pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class})
    .set_index("PassengerId")
    .head()
)
print(cc)

print("df轉csv")
pd.DataFrame({"PassengerId": test.PassengerId, "Survived": new_pred_class}).set_index(
    "PassengerId"
).to_csv("tmp_sub.csv")

print("df轉pickle")
train.to_pickle("tmp_train.pkl")

print("pickle轉df")
print("檢視前幾行")
cc = pd.read_pickle("tmp_train.pkl").head()
print(cc)

print("------------------------------------------------------------")  # 60個

# How do I work with dates and times in pandas? (video)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports')
filename = "data/ufo.csv"
ufo = pd.read_csv(filename)

print("檢視前幾行")
cc = ufo.head()
print(cc)

# 'Time' is currently stored as a string
print(ufo.dtypes)

# hour could be accessed using string slicing, but this approach breaks too easily
print("檢視前幾行")
cc = ufo.Time.str.slice(-5, -3).astype(int).head()
print(cc)

# convert 'Time' to datetime format
ufo["Time"] = pd.to_datetime(ufo.Time)
print("檢視前幾行")
cc = ufo.head()
print(cc)

print(ufo.dtypes)

# convenient Series attributes are now available
print("檢視前幾行")
cc = ufo.Time.dt.hour.head()
print(cc)

""" NG
print('檢視前幾行')
cc = ufo.Time.dt.weekday_name.head()
print(cc)
"""
print("檢視前幾行")
cc = ufo.Time.dt.dayofyear.head()
print(cc)

# convert a single string to datetime format (outputs a timestamp object)
ts = pd.to_datetime("1/1/1999")
print(ts)

# compare a datetime Series with a timestamp
print("檢視前幾行")
cc = ufo.loc[ufo.Time >= ts, :].head()
print(cc)

# perform mathematical operations with timestamps (outputs a timedelta object)
cc = ufo.Time.max() - ufo.Time.min()
print(cc)

# Timedelta('25781 days 01:59:00')

# timedelta objects also have attributes you can access
cc = (ufo.Time.max() - ufo.Time.min()).days
print(cc)
# 25781L

# count the number of UFO reports per year
ufo["Year"] = ufo.Time.dt.year
print("檢視前幾行")
cc = ufo.Year.value_counts().sort_index().head()
print(cc)

# plot the number of UFO reports per year (line plot is the default)
ufo.Year.value_counts().sort_index().plot()

# plt.show()

print("------------------------------------------------------------")  # 60個

# How do I create a pandas DataFrame from another object? (video)

# create a DataFrame from a dictionary (keys become column names, values become data)
print("建立df, 字典轉df")
df = pd.DataFrame({"id": [100, 101, 102], "color": ["red", "blue", "red"]})
print(df)

# optionally specify the order of columns and define the index
print("建立df, 字典轉df")
df = pd.DataFrame(
    {"id": [100, 101, 102], "color": ["red", "blue", "red"]},
    columns=["id", "color"],
    index=["a", "b", "c"],
)
print(df)

# create a DataFrame from a list of lists (each inner list becomes a row)
pd.DataFrame([[100, "red"], [101, "blue"], [102, "red"]], columns=["id", "color"])

# create a NumPy array (with shape 4 by 2) and fill it with random numbers between 0 and 1
arr = np.random.rand(4, 2)
print(arr)

# create a DataFrame from the NumPy array
pd.DataFrame(arr, columns=["one", "two"])

# create a DataFrame of student IDs (100 through 109) and test scores (random integers between 60 and 100)
pd.DataFrame(
    {"student": np.arange(100, 110, 1), "test": np.random.randint(60, 101, 10)}
)

# 'set_index' can be chained with the DataFrame constructor to select an index
pd.DataFrame(
    {"student": np.arange(100, 110, 1), "test": np.random.randint(60, 101, 10)}
).set_index("student")

# create a new Series using the Series constructor
s = pd.Series(["round", "square"], index=["c", "b"], name="shape")
print(s)

# concatenate the DataFrame and the Series (use axis=1 to concatenate columns)
pd.concat([df, s], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("------------------------------------------------------------")  # 60個

# merge DataFrames

print("電影資料")
movie_cols = ["movie_id", "title"]
movies = pd.read_table(
    "data/u.item", sep="|", header=None, names=movie_cols, usecols=[0, 1]
)
print("檢視前幾行")
cc = movies.head()
print(cc)

print("movies之大小")
cc = movies.shape
print(cc)

cc = movies.movie_id.nunique()
print(cc)

# Ratings

rating_cols = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("data/u.data", sep="\t", header=None, names=rating_cols)
print("檢視前幾行")
cc = ratings.head()
print(cc)

print("ratings之大小")
cc = ratings.shape
print(cc)

cc = ratings.movie_id.nunique()
print(cc)

print("檢視前幾行")
cc = ratings.loc[ratings.movie_id == 1, :].head()
print(cc)

# Merging Movies and Ratings

cc = movies.columns
print(cc)

# Index(['movie_id', 'title'], dtype='object')

cc = ratings.columns
print(cc)

# Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')

movie_ratings = pd.merge(movies, ratings)
cc = movie_ratings.columns
print(cc)

# Index(['movie_id', 'title', 'user_id', 'rating', 'timestamp'], dtype='object')

print("檢視前幾行")
cc = movie_ratings.head()
print(cc)

print("movie_ratings之大小")
cc = movie_ratings.shape
print(cc)

print("movie之大小")
print(movies.shape)
print("ratings之大小")
print(ratings.shape)
print("movie_ratings之大小")
print(movie_ratings.shape)

print("3個df都不一樣大")

movies.columns = ["m_id", "title"]
cc = movies.columns
print(cc)

# Index(['m_id', 'title'], dtype='object')

cc = ratings.columns
print(cc)

# Index(['user_id', 'movie_id', 'rating', 'timestamp'], dtype='object')

print("檢視前幾行")
cc = pd.merge(movies, ratings, left_on="m_id", right_on="movie_id").head()
print(cc)

# What if you want to join on one index?

movies = movies.set_index("m_id")
print("檢視前幾行")
cc = movies.head()
print(cc)

print("檢視前幾行")
cc = pd.merge(movies, ratings, left_index=True, right_on="movie_id").head()
print(cc)


# What if you want to join on two indexes?

ratings = ratings.set_index("movie_id")
print("檢視前幾行")
cc = ratings.head()
print(cc)

print("檢視前幾行")
cc = pd.merge(movies, ratings, left_index=True, right_index=True).head()
print(cc)

print("------------------------------------------------------------")  # 60個

# Four Types of Joins

A = pd.DataFrame({"color": ["green", "yellow", "red"], "num": [1, 2, 3]})

B = pd.DataFrame({"color": ["green", "yellow", "pink"], "size": ["S", "M", "L"]})

print("Inner join")
# Only include observations found in both A and B:
cc = pd.merge(A, B, how="inner")
print(cc)

print("Outer join")
# Include observations found in either A or B:
cc = pd.merge(A, B, how="outer")
print(cc)

print("Left join")
# Include all observations found in A:
cc = pd.merge(A, B, how="left")
print(cc)

print("Right join")
# Include all observations found in B:
cc = pd.merge(A, B, how="right")
print(cc)

print("------------------------------------------------------------")  # 60個

print("Create a datetime column from a DataFrame")

# create an example DataFrame
df = pd.DataFrame(
    [[12, 25, 2017, 10], [1, 15, 2018, 11]], columns=["month", "day", "year", "hour"]
)
print(df)

# new: create a datetime column from the entire DataFrame
print(pd.to_datetime(df))

# new: create a datetime column from a subset of columns
print(pd.to_datetime(df[["month", "day", "year"]]))

print(df)

print("------------------------------------------------------------")  # 60個

print("Create a category column during file reading")

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
print(cc)

# data types are automatically detected
cc = drinks.dtypes
print(cc)

# old way to create a category (after file reading)
drinks["continent"] = drinks.continent.astype("category")
cc = drinks.dtypes
print(cc)

# new way to create a category (during file reading)
drinks = pd.read_csv("http://bit.ly/drinksbycountry", dtype={"continent": "category"})
cc = drinks.dtypes
print(cc)

print("------------------------------------------------------------")  # 60個

print("Convert the data type of multiple columns at once")

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

cc = drinks.dtypes
print(cc)

# old way to convert data types (one at a time)
drinks["beer_servings"] = drinks.beer_servings.astype("float")
drinks["spirit_servings"] = drinks.spirit_servings.astype("float")
cc = drinks.dtypes
print(cc)

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

drinks = drinks.astype({"beer_servings": "float", "spirit_servings": "float"})
cc = drinks.dtypes
print(cc)

print("------------------------------------------------------------")  # 60個

print("Apply multiple aggregations on a Series or DataFrame")

# example of a single aggregation function after a groupby
cc = drinks.groupby("continent").beer_servings.mean()
print(cc)

# multiple aggregation functions can be applied simultaneously
cc = drinks.groupby("continent").beer_servings.agg(["mean", "min", "max"])
print(cc)

# new: apply the same aggregations to a Series
cc = drinks.beer_servings.agg(["mean", "min", "max"])
print(cc)

""" NG
# new: apply the same aggregations to a DataFrame
cc = drinks.agg(['mean', 'min', 'max'])
print(cc)
"""

print("------------------------------------------------------------")  # 60個

# Load example datasets

drinks = pd.read_csv("http://bit.ly/drinksbycountry")
movies = pd.read_csv("http://bit.ly/imdbratings")
orders = pd.read_csv("http://bit.ly/chiporders", sep="\t")
orders["item_price"] = orders.item_price.str.replace("$", "").astype("float")

# 讀取[部分股市資料]資料集至df
# stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
filename = "data/stocks.csv"
stocks = pd.read_csv(filename, parse_dates=["Date"])

# 讀取[Kaggle's Titanic competition]資料集至df
# titanic = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
titanic = pd.read_csv(filename)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, parse_dates=["Time"])

cc = pd.__version__
print(cc)

cc = pd.show_versions()
print(cc)

# 2. Create an example DataFrame
print("建立df")
df = pd.DataFrame({"col one": [100, 200], "col two": [300, 400]})
print(df)

cc = pd.DataFrame(np.random.rand(4, 8))
print(cc)

cc = pd.DataFrame(np.random.rand(4, 8), columns=list("abcdefgh"))
print(cc)

# 3. Rename columns

# 承上 df
print(df)

df = df.rename({"col one": "col_one", "col two": "col_two"}, axis="columns")
print(df)

cc = df.columns = ["col_one", "col_two"]
print(cc)

# replace

cc = df.columns = df.columns.str.replace(" ", "_")
print(cc)

print(df)

cc = df.add_prefix("X_")
print(cc)

cc = df.add_suffix("_Y")
print(cc)

# 4. Reverse row order

# the drinks DataFrame:

print("檢視前幾行")
cc = drinks.head()
print(cc)

print("檢視前幾行")
cc = drinks.loc[::-1].head()
print(cc)

print("檢視前幾行")
cc = drinks.loc[::-1].reset_index(drop=True).head()
print(cc)

# 5. Reverse column order

print("檢視前幾行")
cc = drinks.loc[:, ::-1].head()
print(cc)

# 6. Select columns by data type

# the drinks DataFrame:

cc = drinks.dtypes
print(cc)

print("檢視前幾行")
cc = drinks.select_dtypes(include="number").head()
print(cc)

print("檢視前幾行")
cc = drinks.select_dtypes(include="object").head()
print(cc)

print("檢視前幾行")
cc = drinks.select_dtypes(include=["number", "object", "category", "datetime"]).head()
print(cc)

print("檢視前幾行")
cc = drinks.select_dtypes(exclude="number").head()
print(cc)

# 7. Convert strings to numbers
print("建立df")
df = pd.DataFrame(
    {
        "col_one": ["1.1", "2.2", "3.3"],
        "col_two": ["4.4", "5.5", "6.6"],
        "col_three": ["7.7", "8.8", "-"],
    }
)
print(df)

print(df.dtypes)

cc = df.astype({"col_one": "float", "col_two": "float"}).dtypes
print(cc)

cc = pd.to_numeric(df.col_three, errors="coerce")
print(cc)

cc = pd.to_numeric(df.col_three, errors="coerce").fillna(0)
print(cc)

df = df.apply(pd.to_numeric, errors="coerce").fillna(0)
print(df)

print(df.dtypes)

# 8. Reduce DataFrame size

cc = drinks.info(memory_usage="deep")
print(cc)

cols = ["beer_servings", "continent"]
small_drinks = pd.read_csv("http://bit.ly/drinksbycountry", usecols=cols)
small_drinks.info(memory_usage="deep")

dtypes = {"continent": "category"}
smaller_drinks = pd.read_csv(
    "http://bit.ly/drinksbycountry", usecols=cols, dtype=dtypes
)
smaller_drinks.info(memory_usage="deep")

# 9. Build a DataFrame from multiple files (row-wise)

cc = pd.read_csv("data/stocks1.csv")
print(cc)

# Here's the second day:

cc = pd.read_csv("data/stocks2.csv")
print(cc)

# And here's the third day:

cc = pd.read_csv("data/stocks3.csv")
print(cc)

from glob import glob

stock_files = sorted(glob("data/stocks*.csv"))
print(stock_files)

# ['data/stocks1.csv', 'data/stocks2.csv', 'data/stocks3.csv']

cc = pd.concat(
    (pd.read_csv(file) for file in stock_files)
)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(cc)

# Unfortunately, there are now duplicate values in the index. To avoid that, we can tell the concat() function to ignore the index and instead use the default integer index:

cc = pd.concat(
    (pd.read_csv(file) for file in stock_files), ignore_index=True
)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(cc)

# 10. Build a DataFrame from multiple files (column-wise)

print("檢視前幾行")
cc = pd.read_csv("data/drinks1.csv").head()
print(cc)

print("檢視前幾行")
cc = pd.read_csv("data/drinks2.csv").head()
print(cc)

drink_files = sorted(glob("data/drinks*.csv"))

print("檢視前幾行")
cc = pd.concat(
    (pd.read_csv(file) for file in drink_files), axis="columns"
).head()  # axis=0 : 垂直連接, axis=1 : 水平連接
print(cc)
""" skip
#11. Create a DataFrame from the clipboard
print("建立df 將剪貼簿的資料轉成df")
df = pd.read_clipboard()
print(df)

print("型態:", df.dtypes)

#Amazingly, pandas has even identified the first column as the index:
print(df.index)
#Index(['Alice', 'Bob', 'Charlie'], dtype='object')
"""
# 12. Split a DataFrame into two random subsets

cc = len(movies)
print(cc)

# We can use the sample() method to randomly select 75% of the rows and assign them to the "movies_1" DataFrame:

movies_1 = movies.sample(frac=0.75, random_state=1234)

# Then we can use the drop() method to drop all rows that are in "movies_1" and assign the remaining rows to "movies_2":

movies_2 = movies.drop(movies_1.index)

# You can see that the total number of rows is correct:

cc = len(movies_1) + len(movies_2)
print(cc)

# And you can see from the index that every movie is in either "movies_1":

cc = movies_1.index.sort_values()
print(cc)

cc = movies_2.index.sort_values()

# Keep in mind that this approach will not work if your index values are not unique.


# 13. Filter a DataFrame by multiple categories

# the movies DataFrame:

print("檢視前幾行")
cc = movies.head()
print(cc)

# One of the columns is genre:
cc = movies.genre.unique()
print(cc)

print("檢視前幾行")
cc = movies[
    (movies.genre == "Action") | (movies.genre == "Drama") | (movies.genre == "Western")
].head()
print(cc)

print("檢視前幾行")
cc = movies[movies.genre.isin(["Action", "Drama", "Western"])].head()
print(cc)

# And if you want to reverse this filter, so that you are excluding (rather than including) those three genres, you can put a tilde in front of the condition:

print("檢視前幾行")
cc = movies[~movies.genre.isin(["Action", "Drama", "Western"])].head()
print(cc)

# 14. Filter a DataFrame by largest categories

counts = movies.genre.value_counts()
print(counts)

cc = counts.nlargest(3)
print(cc)

# And all we actually need from this Series is the index:
cc = counts.nlargest(3).index
print(cc)

# Finally, we can pass the index object to isin(), and it will be treated like a list of genres:

print("檢視前幾行")
cc = movies[movies.genre.isin(counts.nlargest(3).index)].head()
print(cc)

# 15. Handle missing values

# Let's look at a dataset of UFO sightings:

print("檢視前幾行")
cc = ufo.head()
print(cc)

cc = ufo.isna().sum()
print(cc)

cc = ufo.isna().mean()
print(cc)

print("檢視前幾行")
cc = ufo.dropna(axis="columns").head()
print(cc)

print("檢視前幾行")
cc = ufo.dropna(thresh=len(ufo) * 0.9, axis="columns").head()
print(cc)

# len(ufo) returns the total number of rows, and then we multiply that by 0.9 to tell pandas to only keep columns in which at least 90% of the values are not missing.

# 16. Split a string into multiple columns
print("建立df")
df = pd.DataFrame(
    {
        "name": ["John Arthur Doe", "Jane Ann Smith"],
        "location": ["Los Angeles, CA", "Washington, DC"],
    }
)
print(df)

cc = df.name.str.split(" ", expand=True)
print(cc)

df[["first", "middle", "last"]] = df.name.str.split(" ", expand=True)
print(df)

cc = df.location.str.split(", ", expand=True)
print(cc)

df["city"] = df.location.str.split(", ", expand=True)[0]
print(df)

# 17. Expand a Series of lists into a DataFrame

# Let's create another example DataFrame:
print("建立df")
df = pd.DataFrame(
    {"col_one": ["a", "b", "c"], "col_two": [[10, 40], [20, 50], [30, 60]]}
)
print(df)

df_new = df.col_two.apply(pd.Series)
print(df_new)

cc = pd.concat([df, df_new], axis="columns")  # axis=0 : 垂直連接, axis=1 : 水平連接
print(cc)

# 18. Aggregate by multiple functions

# Let's look at a DataFrame of orders from the Chipotle restaurant chain:

print("檢視前10行")
cc = orders.head(10)
print(cc)

cc = orders[orders.order_id == 1].item_price.sum()
print(cc)

print("檢視前幾行")
cc = orders.groupby("order_id").item_price.sum().head()
print(cc)

print("檢視前幾行")
cc = orders.groupby("order_id").item_price.agg(["sum", "count"]).head()
print(cc)

# 19. Combine the output of an aggregation with a DataFrame

print("檢視前10行")
cc = orders.head(10)
print(cc)

print("檢視前幾行")
cc = orders.groupby("order_id").item_price.sum().head()
print(cc)

# In other words, the output of the sum() function:

cc = len(orders.groupby("order_id").item_price.sum())
print(cc)

cc = len(orders.item_price)
print(cc)

total_price = orders.groupby("order_id").item_price.transform("sum")
cc = len(total_price)
print(cc)

orders["total_price"] = total_price
print("檢視前10行")
cc = orders.head(10)
print(cc)

orders["percent_of_total"] = orders.item_price / orders.total_price
print("檢視前10行")
cc = orders.head(10)
print(cc)

# 20. Select a slice of rows and columns

# Let's take a look at another dataset:

# 讀取[Kaggle's Titanic competition]資料集至df
# titanic = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
titanic = pd.read_csv(filename)

print("檢視前幾行")
cc = titanic.head()
print(cc)

cc = titanic.describe()
print(cc)

cc = titanic.describe().loc["min":"max"]
print(cc)

cc = titanic.describe().loc["min":"max", "Pclass":"Parch"]
print(cc)

# 21. Reshape a MultiIndexed Series

cc = titanic.Survived.mean()
print(cc)

# 0.3838383838383838

cc = titanic.groupby("Sex").Survived.mean()
print(cc)

cc = titanic.groupby(["Sex", "Pclass"]).Survived.mean()
print(cc)

cc = titanic.groupby(["Sex", "Pclass"]).Survived.mean().unstack()
print(cc)

# 22. Create a pivot table

cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="mean"
)
print(cc)

cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="mean", margins=True
)
print(cc)

cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="count", margins=True
)
print(cc)

# 23. Convert continuous data into categorical data

print("檢視前10行")
cc = titanic.Age.head(10)
print(cc)

print("檢視前10行")
pd.cut(
    titanic.Age, bins=[0, 18, 25, 99], labels=["child", "young adult", "adult"]
).head(10)
print(cc)

# 24. Change display options

print("修改顯示模式")
print("檢視前幾行")
cc = titanic.head()
print(cc)

pd.set_option("display.float_format", "{:.2f}".format)

print("檢視前幾行")
cc = titanic.head()
print(cc)

# You can also reset any option back to its default:
print("恢復預設顯示模式")
pd.reset_option("display.float_format")

# 25. Style a DataFrame

# 讀取[部分股市資料]資料集至df
# stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
filename = "data/stocks.csv"
stocks = pd.read_csv(filename, parse_dates=["Date"])

print(stocks)

format_dict = {"Date": "{:%m/%d/%y}", "Close": "${:.2f}", "Volume": "{:,}"}

cc = stocks.style.format(format_dict)
print(cc)

"""
(stocks.style.format(format_dict)
 .hide_index()
 .highlight_min('Close', color='red')
 .highlight_max('Close', color='lightgreen')
)

(stocks.style.format(format_dict)
 .hide_index()
 .background_gradient(subset='Volume', cmap='Blues')
)

(stocks.style.format(format_dict)
 .hide_index()
 .bar('Volume', color='lightblue', align='zero')
 .set_caption('Stock Prices from October 2016')
)
"""

""" NG
import pandas_profiling
pandas_profiling.ProfileReport(titanic)
"""

print("------------------------------------------------------------")  # 60個

drinks = pd.read_csv("http://bit.ly/drinksbycountry")

# 讀取[部分股市資料]資料集至df
# stocks = pd.read_csv('http://bit.ly/smallstocks', parse_dates=['Date'])
filename = "data/stocks.csv"
stocks = pd.read_csv(filename, parse_dates=["Date"])

# 讀取[Kaggle's Titanic competition]資料集至df
# titanic = pd.read_csv('http://bit.ly/kaggletrain')
filename = "data/titanic_train.csv"
titanic = pd.read_csv(filename)

# 讀取[UFO報告]資料集至df
# ufo = pd.read_csv('http://bit.ly/uforeports', parse_dates=['Time'])
filename = "data/ufo.csv"
ufo = pd.read_csv(filename, parse_dates=["Time"])

# 1. Check for equality

df = pd.DataFrame({"a": [1, 2, np.nan], "b": [1, 2, np.nan]})
print(df)

cc = df.a == df.b
print(cc)


cc = np.nan == np.nan
print(cc)

cc = df.a.equals(df.b)
print(cc)

df_new = df.copy()
cc = df_new.equals(df)
print(cc)

# 2. Check for equality (alternative)

df = pd.DataFrame({"c": [1, 2, 3], "d": [1.0, 2.0, 3.0], "e": [1.0, 2.0, 3.000005]})
print(df)

cc = df.c.equals(df.d)
print(cc)

pd.testing.assert_series_equal(df.c, df.d, check_names=False, check_dtype=False)

pd.testing.assert_series_equal(df.d, df.e, check_names=False, check_exact=False)

df_new = df.copy()
pd.testing.assert_frame_equal(df, df_new)

# 3. Use NumPy without importing NumPy

cc = pd.DataFrame(np.random.rand(2, 4))
print(cc)

df.loc[0, "e"] = np.nan
print(df)

# 4. Calculate memory usage

# Here's a DataFrame of UFO sightings:

cc = ufo.head()
print(cc)

# You can calculate the memory used by the entire DataFrame:
print("df使用記憶體大小")
cc = ufo.info(memory_usage="deep")
print(cc)

print()
# You can also calculate memory used by each column (in bytes):

cc = ufo.memory_usage(deep=True)
print(cc)

print()

# 5. Count the number of words in a column

cc = ufo["Colors Reported"].value_counts()
print(cc)

cc = (ufo["Colors Reported"].str.count(" ") + 1).value_counts()
print(cc)

# 6. Convert one set of values to another

cc = titanic.Sex.head()

titanic["Sex_num"] = titanic.Sex.map({"male": 0, "female": 1})
cc = titanic.Sex_num.head()
print(cc)

cc = titanic.Embarked.head(10)
print(cc)

titanic["Embarked_num"] = titanic.Embarked.factorize()[0]
cc = titanic.Embarked_num.head(10)
print(cc)

cc = titanic.Embarked.factorize()[1]
print(cc)


cc = titanic.SibSp.head(10)
print(cc)

titanic["SibSp_binary"] = (titanic.SibSp > 0).astype("int")
cc = titanic.SibSp_binary.head(10)
print(cc)


# 7. Convert continuous data into categorical data (alternative)

cc = pd.cut(
    titanic.Age, bins=[0, 18, 25, 99], labels=["child", "young adult", "adult"]
).head(10)
print(cc)

cca = pd.qcut(titanic.Age, q=3).head(10)
print(cc)

cc = pd.qcut(titanic.Age, q=3).value_counts()
print(cc)

# 8. Create a cross-tabulation

cc = titanic.Sex.value_counts()
print(cc)

cc = pd.crosstab(titanic.Sex, titanic.Pclass)
print(cc)

cca = pd.crosstab(titanic.Sex, titanic.Pclass, margins=True)
print(cc)

cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="count", margins=True
)
print(cc)

# 9. Create a datetime column from multiple columns

df = pd.DataFrame(
    [[12, 25, 2019, "christmas"], [11, 28, 2019, "thanksgiving"]],
    columns=["month", "day", "year", "holiday"],
)
print(df)

df["date"] = pd.to_datetime(df[["month", "day", "year"]])
print(df)

print(df.dtypes)

# 10. Resample a datetime column

print(stocks)

cc = stocks.resample("D", on="Date").Close.mean()
print(cc)

ufo = ufo.set_index("Time")
cc = ufo.head()
print(cc)

cc = ufo.resample("Y").State.count().tail()
print(cc)

cc = ufo.resample("M").State.count().tail()
print(cc)

# 11. Read and write from compressed files

# df存檔
ufo.to_csv("tmp_ufo.csv")
# 存檔 並壓縮
ufo.to_csv("tmp_ufo.csv.zip")
ufo.to_csv("tmp_ufo.csv.gz")
ufo.to_csv("tmp_ufo.csv.bz2")
ufo.to_csv("tmp_ufo.csv.xz")

# 直接讀取壓縮檔
ufo_new = pd.read_csv("tmp_ufo.csv.gz", index_col="Time", parse_dates=["Time"])
cc = ufo_new.head()
print(cc)

print("比較df是否相同")
cc = ufo_new.equals(ufo)
print(cc)

# 12. Fill missing values using interpolation

df = pd.DataFrame({"a": [100, 120, 130, np.nan, 140], "b": [9, 9, np.nan, 7.5, 6.5]})
df.index = pd.to_datetime(["2019-01", "2019-02", "2019-03", "2019-04", "2019-05"])
print(df)

cc = df.interpolate()
print(cc)

# 13. Check for duplicate merge keys
print("合併df")
left = pd.DataFrame({"color": ["green", "yellow", "red"], "num": [1, 2, 3]})
print(left)

right = pd.DataFrame(
    {"color": ["green", "yellow", "pink", "green"], "size": ["S", "M", "L", "XL"]}
)
print(right)

pd.merge(left, right, how="inner", validate="one_to_many")
print(pd)

# NG
# pd.merge(left, right, how='inner', validate='many_to_one')

# 15. Create an example DataFrame (alternative)

cc = pd.DataFrame({"col one": [100, 200], "col two": [300, 400]})
print(cc)

cc = pd.DataFrame(np.random.rand(4, 8), columns=list("abcdefgh"))
print(cc)

# makeMissingDataframe() is similar, except that some of the values are missing:

# makeTimeDataFrame() is similar, except it creates a DatetimeIndex:

# 17. Use query to avoid intermediate variables

print(stocks)

cc = stocks[stocks.Symbol == "AAPL"]
print(cc)

cc = stocks.query("Symbol == 'AAPL'")
print(cc)

cc = stocks.groupby("Symbol").mean()
print(cc)

temp = stocks.groupby("Symbol").mean()
cc = temp[temp.Close < 100]
print(cc)

# But query() works even better in this situation, since you can avoid creating an intermediate object:

cc = stocks.groupby("Symbol").mean().query("Close < 100")
print(cc)

# 18. Reshape a DataFrame from wide format to long format

distances = pd.DataFrame(
    [["12345", 100, 200, 300], ["34567", 400, 500, 600], ["67890", 700, 800, 900]],
    columns=["zip", "factory", "warehouse", "retail"],
)
print(distances)

users = pd.DataFrame(
    [[1, "12345", "factory"], [2, "34567", "warehouse"]],
    columns=["user_id", "zip", "location_type"],
)
print(users)

distances_long = distances.melt(
    id_vars="zip", var_name="location_type", value_name="distance"
)
print(distances_long)

cc = pd.merge(users, distances_long)
print(cc)


# 19. Reverse row order (alternative)

print(drinks.head())

print(drinks.loc[::-1].head())

cc = drinks.reindex(reversed(drinks.index)).head()
print(cc)

stocks = stocks.set_index("Date")
print(stocks)


# Since the index above is not unique, this will result in an error:
# stocks.reindex(reversed(stocks.index))

# 20. Reverse column order (alternative)

cc = drinks.loc[:, ::-1].head()
print(cc)

cc = drinks[reversed(drinks.columns)].head()
print(cc)

stocks = stocks.rename({"Symbol": "XYZ", "Volume": "XYZ"}, axis="columns")
print(stocks)

cc = stocks[reversed(stocks.columns)]
print(cc)

# 21. Split a string into multiple columns (alternative)

df = pd.DataFrame(
    {
        "name": ["John Arthur Doe", "Jane Ann Smith"],
        "location": ["Los Angeles, CA", "Washington, DC"],
    }
)
print(df)

df[["first", "middle", "last"]] = df.name.str.split(" ", expand=True)
print(df)

df["first"], df["middle"], df["last"] = zip(*df.name.str.split(" "))
print(df)

cc = df.name.str.split(" ")
print(cc)

cc = list(zip(*df.name.str.split(" ")))
print(cc)

df["first"], df["middle"], df["last"] = zip(*df.name.str.split(" "))
print(df)

print("------------------------------------------------------------")  # 60個

stocks = pd.read_csv("data/stocks.csv")
print(stocks)

print(stocks.index)

cc = stocks.groupby("Symbol").Close.mean()
print(cc)

# Series with MultiIndex

ser = stocks.groupby(["Symbol", "Date"]).Close.mean()
print(ser)

print(ser.index)

print(ser.unstack())

df = stocks.pivot_table(values="Close", index="Symbol", columns="Date")
print(df)

# Selection from Series with MultiIndex

print(ser)

cc = ser.loc["AAPL"]
print(cc)

cc = ser.loc["AAPL", "2016-10-03"]
print(cc)

cc = ser.loc[:, "2016-10-03"]
print(cc)

print(df)

cc = df.loc["AAPL"]
print(cc)

cc = df.loc["AAPL", "2016-10-03"]
print(cc)

cc = df.loc[:, "2016-10-03"]
print(cc)

# DataFrame with MultiIndex

stocks.set_index(["Symbol", "Date"], inplace=True)
print(stocks)

print(stocks.index)

stocks.sort_index(inplace=True)
print(stocks)

# Selection from DataFrame with MultiIndex

cc = stocks.loc["AAPL"]
print(cc)

cc = stocks.loc[("AAPL", "2016-10-03"), :]
print(cc)

cc = stocks.loc[("AAPL", "2016-10-03"), "Close"]
print(cc)

cc = stocks.loc[["AAPL", "MSFT"], :]
print(cc)

cc = stocks.loc[(["AAPL", "MSFT"], "2016-10-03"), :]
print(cc)

cc = stocks.loc[(["AAPL", "MSFT"], "2016-10-03"), "Close"]
print(cc)

cc = stocks.loc[("AAPL", ["2016-10-03", "2016-10-04"]), "Close"]
print(cc)

cc = stocks.loc[(slice(None), ["2016-10-03", "2016-10-04"]), :]
print(cc)

# Merging DataFrames with MultiIndexes

close = pd.read_csv(
    "data/stocks.csv", usecols=[0, 1, 3], index_col=["Symbol", "Date"]
).sort_index()
print(close)

volume = pd.read_csv(
    "data/stocks.csv", usecols=[0, 2, 3], index_col=["Symbol", "Date"]
).sort_index()
print(volume)

both = pd.merge(close, volume, left_index=True, right_index=True)
print(both)

cc = both.reset_index()
print(cc)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# dfclean1.py
# 讀取資料
df = pd.read_csv("_new/customer.csv")
# 空值的處理
print("各個欄位有空值的狀況:")
print(df.isnull().sum())
print("有空值的記錄筆數:", df.isnull().any(axis=1).sum())
print("有空值的欄位數:", df.isnull().any(axis=0).sum())
print("age欄有空值的記錄:")
print(df[df["age"].isnull()])


# dfclean2.py
# 讀取資料
df = pd.read_csv("_new/customer.csv")
# 將age的空值填入0
df_sample = df.copy()
df_sample["age"] = df_sample["age"].fillna(value=0)
print(df_sample.head())

# 將age的空值填入平均值
df_sample = df.copy()
df_sample["age"] = df_sample["age"].fillna(value=df_sample["age"].mean())
print(df_sample.head())

# 以前一個值往下填ffill或後一個值往上填bfill
df_sample["gender"] = df_sample["gender"].fillna(method="ffill")
df_sample["area"] = df_sample["area"].fillna(method="ffill")
print(df_sample.head())

# 刪除不完整的資料
print(df.dropna())


# dfclean3.py
# 讀取資料
df = pd.read_csv("_new/customer.csv")
# 資料基本清理
df_sample = df.copy()
df_sample["age"] = df_sample["age"].fillna(value=df_sample["age"].mean())
df_sample["gender"] = df_sample["gender"].fillna(method="ffill")
df_sample["area"] = df_sample["area"].fillna(method="ffill")

# 去除重覆記錄
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
print(df_sample.head())

# 去除欄位中的空白
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
print(df_sample.head())

# 轉換值的格式
df_sample["age"] = df_sample["age"].astype("int32")
print(df_sample.head())

# dffilter.py
# 讀取資料
df = pd.read_csv("_new/customer.csv")
# 資料基本清理
df_sample = df.copy()
df_sample["age"] = df_sample["age"].fillna(value=df_sample["age"].mean())
df_sample["gender"] = df_sample["gender"].fillna(method="ffill")
df_sample["area"] = df_sample["area"].fillna(method="ffill")
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
df_sample["age"] = df_sample["age"].astype("int32")

# 篩選女性的資料
print(df_sample[(df_sample["gender"] == "Female")])

# 篩選男性且大於50歲的資料
print(df_sample[(df_sample["gender"] == "Male") & (df_sample["age"] > 50)])

# 篩選住在新北市三重區或基隆市中正區的資料
print(df_sample[(df_sample["area"] == "新北市三重區") | (df_sample["area"] == "基隆市中正區")])

# dfgroupby.py
# 讀取資料
df = pd.read_csv("_new/customer.csv")
# 資料基本清理
df_sample = df.copy()
df_sample["age"] = df_sample["age"].fillna(value=df_sample["age"].mean())
df_sample["gender"] = df_sample["gender"].fillna(method="ffill")
df_sample["area"] = df_sample["area"].fillna(method="ffill")
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
df_sample["age"] = df_sample["age"].astype("int32")

# 客戶中男女生的平均年齡
print(df_sample.groupby("gender")["age"].mean())
print("-" * 30)

# 客戶中住各區的人數
print(df_sample.groupby("area")["id"].count())
print("-" * 30)

# 客戶中男女生的平均年齡、最年長及最年輕的年齡
print(df_sample.groupby("gender")["age"].agg(["mean", "max", "min"]))

print("cccccc")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

s1 = pd.Series(["Bike", "Bus", "Car", "Truck"])
s2 = pd.Series([3, 4, 6, 2])
s3 = pd.Series([2, 4, 4, 6])
data = {"種類": s1, "數量": s2, "輪數": s3}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
print(type(df))
print(df)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
print(df)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
labels = ["A", "B", "E", "D"]
df.columns = ["Types", "Count", "Wheels"]
labels[2] = "C"
df.index = labels
print(df)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
df.set_index("種類", inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)

s = pd.Series({"種類": "Bicycle", "數量": 5, "輪數": 2})
"""NG
df2 = df.append(s, ignore_index = True)
print(df2.tail())
"""
df["載客數"] = [1, 20, 4, 2]
print(df)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
df.set_index("種類", inplace=True)
print(df)
df2 = df.drop(["Bus", "Truck"])
print(df2)
df3 = df.drop(df.index[[0, 2]])
print(df3)
df4 = df.drop(["輪數"], axis=1)
print(df4)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
print(df.head(2))
print(df.tail(3))

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
print(df.index)
print(df.columns)
print(df.values)

print(df.values[2])
print(df.values[1][2])

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}

print("字典 轉 DataFrame")
df = pd.DataFrame(data)
print(len(df))
print(df.shape)

print("------------------------------------------------------------")  # 60個

data = {"種類": ["Bike", "Bus", "Car", "Truck"], "數量": [3, 4, 6, 2], "輪數": [2, 4, 4, 6]}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data)

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
print(df["種類"])

print(df[["數量", "輪數"]].head(3))

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
print(df[0:2])

print(df["A":"C"])

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
print(df.loc["A", "數量"])
print(df.loc[["C", "D"], ["數量", "輪數"]])

print(df.loc[:, ["數量", "輪數"]])
print(df.loc["B":"C", "種類":"數量"])

print(df.iloc[3])
print(df.iloc[2:4, 1:3])

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
df["輪數"] = df["輪數"].astype("int64")
print(df[df.輪數 > 3])

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
print(type(data))

print("字典 轉 DataFrame")
df = pd.DataFrame(data, index=["A", "B", "C", "D"])
df2 = df.sort_values("數量", ascending=False)
print(df2)

print("------------------------------------------------------------")  # 60個

dates_d = pd.date_range("20170109", periods=5, freq="D")
print(dates_d)
df = pd.read_csv("_new/2330.TW.csv")
df["Date"] = dates_d
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330.TW.csv")
print(df["Volume"].pct_change())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330.TW.csv")
print(df["Close"].unique())
print(df["Close"].nunique())
print(df["Close"].value_counts())

print("------------------------------------------------------------")  # 60個

print("建立df, 使用 合併")
df1 = pd.DataFrame({"Name": ["A", "B"], "Value": [11, 12]})
df2 = pd.DataFrame({"Name": ["C"], "Value": [23]})
df3 = pd.concat([df1, df2], ignore_index=True)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df3)

print("建立df, 使用 合併")
df4 = pd.DataFrame({"Name": ["A", "B"], "Value": [11, 12]})
df5 = pd.DataFrame({"Size": ["XL", "L"]})
df6 = pd.concat([df4, df5], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df6)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/batchSales.csv")
print(df)
df2 = df.groupby("BatchNo").mean()
print(df2)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/titanic_test.csv")
print(df.head())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/titanic_test.csv")
print(df["Age"].isnull().sum())
df2 = df.dropna(subset=["Age"])
print(len(df2))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/titanic_test.csv")
df["Age"] = df["Age"].fillna(value=20)
print(df["Age"].isnull().sum())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/titanic_test.csv")
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].isnull().sum())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/sales.csv")
df1 = df.drop_duplicates("Country")
print(df1)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/shoes.csv")
print(df)
size_mapping = {"XXL": 5, "XL": 4, "L": 3, "M": 2, "S": 1, "XS": 0}

df["Size"] = df["Size"].map(size_mapping)
print(df)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/2330_2019_9.csv")
data = pd.DataFrame()
data["Date"] = pd.to_datetime(df["Date"])
data["Adj Close"] = df["Adj Close"]
data["High"] = df["High"]
data["Low"] = df["Low"]
data = data.set_index("Date")

data.plot(kind="line")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/drinks.csv")
print(df)
df.set_index("Type", inplace=True)
df.plot(kind="bar")
df.plot(kind="barh")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("_new/NBA_players_salary_stats_2018.csv")
df.plot(kind="scatter", x="PTS", y="salary", title="Scatter Plot of NBA Salary and PTS")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

cc = pd.merge(df1, df2, how="left", indicator=True).query("_merge == 'left_only'")
print(cc)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# read / write csv

# Writing to a SQLite database

weather_df = pd.read_csv("data/weather_2012.csv")
con = sqlite3.connect("tmp_test_db.sqlite")
con.execute("DROP TABLE IF EXISTS weather_2012")
weather_df.to_sql("weather_2012", con)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

con = sqlite3.connect("tmp_test_db.sqlite")
df = pd.read_sql("SELECT * from weather_2012 ORDER BY Weather LIMIT 3", con)
print(df)

print("------------------------------------------------------------")  # 60個

data = pd.read_csv("_new/scores2.csv", header=0, index_col=0)
print(data)
print(type(data))

print("------------------------------------------------------------")  # 60個

import sqlite3

con = sqlite3.connect("data/weather_2012.sqlite")
df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con)
print(df)

print("------------------------------")  # 30個

df = pd.read_sql("SELECT * from weather_2012 LIMIT 3", con, index_col="id")
print(df)

print("------------------------------")  # 30個

df = pd.read_sql(
    "SELECT * from weather_2012 LIMIT 3", con, index_col=["id", "date_time"]
)
print(df)

print("------------------------------")  # 30個

# 讓我們來看一個更實際的示例，我們有一個包含按年數量銷售的數據集。

fruits = pd.DataFrame(
    [["FFF", 40], ["AAA", 90], ["CCC", 130]],
    columns=["Product", "ContainerSales"],
)
print(fruits)

# 在數據集中，缺少年份列。我們嘗試使用numpy添加它。

fruits["year"] = np.repeat(2020, fruits.shape[0])
print(fruits)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" no file
# 載入外部檔案並做資料整理
# 使用 Pandas 讀取 CSV 檔

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
url = "iris.data"
df = pd.read_csv(url, header=None)
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
print(df)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("Pandas資料讀取與顯示")

url = "xxxx"  # 網頁上有csv的地方
df = pd.read_csv(
    "https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001"
)

print("資料排序")

# df1 = df[['醫事機構名稱','電話','地址','備註']]
# 把幾個欄位的資料抓出來

# 排序
df1.sort_values(["地址", "電話"], ascending=[True, False])

print("資料篩選")
mask = df1["地址"].str.startswith("苗栗縣")
cc = df1[mask]
print(cc)

print("新增欄位(columns)")
df1.insert(1, "縣市", df1["地址"].str.slice(0, 3, 1))
df1.insert(2, "地區", df1["地址"].str.slice(3, 6, 1))

print(df1)

print("資料統計")

df2 = df1[["醫事機構名稱", "縣市"]].groupby("縣市").count()
df2.columns = ["總計"]
df2.sort_values("總計", ascending=False)

print("口罩何處尋 健保藥局查詢程式")

# df = pd.read_csv('https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001')

df1 = df[["醫事機構名稱", "電話", "地址", "備註"]]

"""
keyword = input('請輸入查詢縣市：')

if keyword != '':
    mask = df1['地址'].str.startswith(keyword.replace('台', '臺'))
    if len(df1[mask]) > 0:
        display(df1[mask])
    else:
        print('請輸入正確資料！')
else:
    print('請重新輸入查詢縣市資料')
"""


"""

1. 建立df
2. 各種df資訊
3. 

"""


cc = df.describe()  # 方法有()
print(cc)

cc = df.shape  # 屬性無()
print(cc)


# 14. Transpose a wide DataFrame

df = pd.DataFrame(np.random.rand(200, 25), columns=list("ABCDEFGHIJKLMNOPQRSTUVWXY"))

cc = df.head()
print(cc)

cc = df.head().T
print(cc)

cc = df.describe().T
print(cc)



plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 也可設mingliu或DFKai-SB

