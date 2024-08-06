"""
DataFrame 測試

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

idx = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]

column = ["中文名", "英文名", "體重", "全名"]

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

print(type(animals))
print(type(animals[1]))

df = pd.DataFrame(animals, index=idx, columns=column)

# print(df)

print("df的方法")
print(df.shape)
print(df.columns)
print(df.index)
print(df.head())
print(df.describe())
print(df.info())
print(df.duplicated())

filename = "動物資料0.csv"
df.to_csv(filename)  # 預設為 儲存index行

filename = "動物資料1.csv"
df.to_csv(filename, index=False)  # 不儲存index行

filename = "動物資料2.csv"
df.to_csv(filename, index=True)  # 儲存index行

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
print(df1.head())

print("最重 :", df["體重"].max())
print("最輕 :", df["體重"].min())
print("總重 :", df["體重"].sum())
print("平均 :", df["體重"].mean())

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ]
)
print("原資料 :\n", df, "\n")

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
print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

# 字典轉df
scores = {
    "王小明": {"國文": 65, "英文": 92, "數學": 78, "社會": 83, "自然": 70},
    "李小美": {"國文": 90, "英文": 72, "數學": 76, "社會": 93, "自然": 56},
    "陳大同": {"國文": 81, "英文": 85, "數學": 91, "社會": 89, "自然": 77},
    "林小玉": {"國文": 79, "英文": 53, "數學": 47, "社會": 94, "自然": 80},
}
print(type(scores))
print(scores)
df = pd.DataFrame(scores)
print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

# 字典轉df
scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
print(type(scores))
print(scores)
df = pd.DataFrame(scores)
print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

se1 = pd.Series({"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79})
se2 = pd.Series({"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53})
se3 = pd.Series({"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47})
se4 = pd.Series({"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94})
se5 = pd.Series({"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80})

df = pd.concat([se1, se2, se3, se4, se5], axis=0)
df.columns = ["國文", "英文", "數學", "自然", "社會"]
print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

se1 = pd.Series({"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79})
se2 = pd.Series({"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53})
se3 = pd.Series({"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47})
se4 = pd.Series({"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94})
se5 = pd.Series({"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80})

df = pd.DataFrame({"國文": se1, "英文": se2, "數學": se3, "自然": se4, "社會": se5})
print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

# 字典
scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
df = pd.DataFrame(scores)
print(df["自然"])
print(df[["國文", "數學", "自然"]])
print(df[df["國文"] >= 80])
print(df.values)
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
# head() tail()
df.head(2)
df.tail(2)

print("------------------------------------------------------------")  # 60個

# 字典
scores = {
    "國文": {"王小明": 65, "李小美": 90, "陳大同": 81, "林小玉": 79},
    "英文": {"王小明": 92, "李小美": 72, "陳大同": 85, "林小玉": 53},
    "數學": {"王小明": 78, "李小美": 76, "陳大同": 91, "林小玉": 47},
    "自然": {"王小明": 83, "李小美": 93, "陳大同": 89, "林小玉": 94},
    "社會": {"王小明": 70, "李小美": 56, "陳大同": 94, "林小玉": 80},
}
df = pd.DataFrame(scores)

print("原資料 :\n", df, "\n")

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

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]

df = pd.DataFrame(datas, columns=columns, index=indexs)

print("原資料 :\n", df, "\n")

print("按照數學遞減排序 ->")
df1 = df.sort_values(by="數學", ascending=False)
print(df1)
print()

print("按照列標題遞增排序 ->")
df2 = df.sort_index(axis=0)
print(df2)
print()

print("------------------------------------------------------------")  # 60個

datas = [["mouse", 3], ["ox", 48], ["tiger", 33], ["rabbit", 8]]
indexs = ["鼠", "牛", "虎", "兔"]
columns = ["英文名", "體重"]

df = pd.DataFrame(datas, columns=columns, index=indexs)

print("原資料 :\n", df, "\n")

print("按照數學遞減排序 ->")
df1 = df.sort_values(by="體重", ascending=False)
print(df1)
print()

print("按照列標題遞增排序 ->")
df2 = df.sort_index(axis=0)
print(df2)
print()

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns)
df.plot(xticks=range(0, 4))

plt.show()

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print("最前 2 位學生成績 ->")
print(df.head(2))
print()
print("最後 2 位學生成績 ->")
print(df.tail(2))

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print("df.iloc[1, :] ->")
print(df.iloc[1, :])
print()
print("df.iloc[1][1] ->")
print(df.iloc[1][1])

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print('df.loc["陳聰明", :] ->')
print(df.loc["陳聰明", :])
# print(df.loc["陳聰明"])
print()
print('df.loc["陳聰明"]["數學"] ->')
print(df.loc["陳聰明"]["數學"])
print()
print('df.loc[("陳聰明", "熊小娟") ->')
print(df.loc[("陳聰明", "熊小娟"), :])
print()
print('df.loc[:, "數學"] ->')
print(df.loc[:, "數學"])
print()
print('df.loc[("陳聰明", "熊小娟"), ("數學", "自然")] ->')
print(df.loc[("陳聰明", "熊小娟"), ("數學", "自然")])
print()
print('df.loc["陳聰明":"熊小娟", "數學":"社會"] ->')
print(df.loc["陳聰明":"熊小娟", "數學":"社會"])
print()
print('df.loc[:黃美麗, "數學":"社會"] ->')
print(df.loc[:"黃美麗", "數學":"社會"])
print()
print('df.loc["陳聰明":, "數學":"社會"] ->')
print(df.loc["陳聰明":, "數學":"社會"])

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print('df["自然"] ->')
print(df["自然"])
print()
print('df[["國文", "數學", "自然"] ->')
print(df[["國文", "數學", "自然"]])
print()
print("df[df.數學>=80] ->")
print(df[df.數學 >= 80])

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print("df.values：")
print(df.values)
print("陳聰明的成績(df.values[1])：")
print(df.values[1])
print("陳聰明的英文成績(df.values[1][2])：")
print(df.values[1][2])

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print('df.loc["陳聰明"]["數學"] (原始)：' + str(df.loc["陳聰明"]["數學"]))
df.loc["陳聰明"]["數學"] = 91
print('df.loc["陳聰明"]["數學"] (修改)：' + str(df.loc["陳聰明"]["數學"]))
print()
print('df.loc["陳聰明", :] ->')
df.loc["陳聰明", :] = 80
print(df.loc["陳聰明", :])

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {
        "林大明": [65, 92, 78, 83, 70],
        "陳聰明": [90, 72, 76, 93, 56],
        "黃美麗": [81, 85, 91, 89, 77],
        "熊小娟": [79, 53, 47, 94, 80],
    }
)

print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)

print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
print("移除陳聰明成績 ->")
df1 = df.drop("陳聰明")
print(df1)
print()
print("移除數學科成績 ->")
df2 = df.drop("數學", axis=1)
print(df2)
print()
print("移除數學科及自然科成績 ->")
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)
print()
print("移除陳聰明到熊小娟成績 ->")
df4 = df.drop(df.index[1:4])
print(df4)
print()
print("移除數學科到自然科成績 ->")
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)
print()

print("------------------------------------------------------------")  # 60個

datas = [
    [65, 92, 78, 83, 70],
    [90, 72, 76, 93, 56],
    [81, 85, 91, 89, 77],
    [79, 53, 47, 94, 80],
]
indexs = ["林大明", "陳聰明", "黃美麗", "熊小娟"]
columns = ["國文", "數學", "英文", "自然", "社會"]
df = pd.DataFrame(datas, columns=columns, index=indexs)
indexs[0] = "林晶輝"
df.index = indexs
columns[3] = "理化"
df.columns = columns

print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個

# 字典
fruits = {"蘋果": [4, 3, 1, 0], "香蕉": [0, 4, 6, 2], "橘子": [1, 5, 2, 4]}

print(type(fruits))
print(fruits)

df = pd.DataFrame(fruits)

print("原資料 :\n", df, "\n")

print("前3項")
print(df.head(3))  # 前3項

print("後2項")
print(df.tail(2))  # 後2項

print("------------------------------------------------------------")  # 60個

"""
df.to_csv("fruits.csv",index=False,encoding="utf8")
df.to_json("fruits.json")

df2 = pd.read_csv("fruits.csv", encoding="utf8")
df2 = pd.read_json("fruits.json")
print(df2)

for index, row in df.iterrows() :
    print(index, row["蘋果"], row["香蕉"],
          row["橘子"])

"""

print("------------------------------------------------------------")  # 60個

sales = [11.22, 23.50, 12.99, 15.95, 25.75, 11.55]

df = pd.DataFrame(sales)  # 串列 轉 DataFrame

print(df.describe())
print(df.count())
print(df.median())
print(df.mean())
print(df.min())
print(df.max())
print(df.std())

print("------------------------------------------------------------")  # 60個

print("DataFrame格式的範例")

df = pd.DataFrame({"姓名": ["Alice", "Bob", "Charlie"], "分數": [78, 65, 90]})

print("原資料 :\n", df, "\n")

print("------------------------------------------------------------")  # 60個


# 建立 Series 物件

index = ["鼠", "牛", "虎", "兔", "龍"]
data = [1, 4, 5, 6, 3]
series = pd.Series(data, index=index)

print(series)
print(series.shape)

data = [1, 4, 5, 6, 3]
series = pd.Series(data)

print(series)

fruits = {"orange": 2, "banana": 3}
print(pd.Series(fruits))

print("------------------------------------------------------------")  # 60個

# 取出 Series 當中的元素

fruits = {"banana": 3, "orange": 4, "grape": 1, "peach": 5}

series = pd.Series(fruits)

print(series[0:2])

print(series[["orange", "peach"]])

print("------------------------------------------------------------")  # 60個

# 單取出「索引值」或者「內容值」-.index、.values

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

series_index = series.index

series_values = series.values

print(series_index)

print(series_values)

print("------------------------------------------------------------")  # 60個

# 新增 Series 物件的元素 – append()

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

pineapple = pd.Series([12], index=["pineapple"])

# pineapple = pd.Series( {"pineapple":12})

series = series.append(pineapple)

print(series)

print("------------------------------------------------------------")  # 60個

# 刪除 Series 物件的元素 – drop()

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

series = series.drop("兔")

print(series)

print("------------------------------------------------------------")  # 60個

# 從 Series 物件篩選出想要的元素

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

conditions = [True, True, False, False, False]

print(series[conditions])

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series[series >= 5])

series = series[series >= 5][series < 10]

print(series)

print("------------------------------------------------------------")  # 60個

# 將 Series 的元素排序 – sort_index()、sort_values()

index = ["鼠", "牛", "虎", "兔", "龍"]

data = [10, 5, 8, 12, 3]

series = pd.Series(data, index=index)

print(series)

items1 = series.sort_index()

items2 = series.sort_values()

print(items1)

print()

print(items2)

print("------------------------------------------------------------")  # 60個

# 建立 DataFrame 物件 – pd.DataFrame()

index = ["鼠", "牛", "虎", "兔", "龍"]

data1 = [10, 5, 8, 12, 3]

data2 = [30, 25, 12, 10, 8]

series1 = pd.Series(data1, index=index)

series2 = pd.Series(data2, index=index)

df = pd.DataFrame([series1, series2])

print(df)

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
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

# 修改 index 和 column 的名稱 –.index、.column

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)
df = pd.DataFrame([series1, series2])
df.index = [1, 2]
print(df)

print("------------------------------------------------------------")  # 60個

# 加入新的資料列 – append()

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "time": [1, 4, 5, 6, 3],
}

df = pd.DataFrame(data)

series = pd.Series(["mango", 2008, 7], index=["fruits", "year", "time"])

df = df.append(series, ignore_index=True)

print(df)

index = ["鼠", "牛", "虎", "兔", "龍"]
data1 = [10, 5, 8, 12, 3]
data2 = [30, 25, 12, 10, 8]
data3 = [30, 12, 10, 8, 25, 3]

series1 = pd.Series(data1, index=index)
series2 = pd.Series(data2, index=index)

df = pd.DataFrame([series1, series2])

index.append("pineapple")

series3 = pd.Series(data3, index=index)

df = df.append(series3, ignore_index=True)

print(df)

print("------------------------------------------------------------")  # 60個

# 加入新的欄位

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
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
df = pd.DataFrame([series1, series2])
new_column = pd.Series([15, 7], index=[0, 1])
df["mango"] = new_column
print(df)

print("------------------------------------------------------------")  # 60個

# 取出 DataFrame 當中的元素 –df.loc[]、df.iloc[]

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "time": [1, 4, 5, 6, 3],
}
df = pd.DataFrame(data)
print(df)

df = df.loc[[1, 2], ["time", "year"]]
print(df)

np.random.seed(0)
df = pd.DataFrame()
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df.loc[range(2, 6), ["banana", "kiwifruit"]]
print(df)

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
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
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}

df = pd.DataFrame(data)
print(df)

df_1 = df.drop([0, 1])
print(df_1)

df_2 = df.drop("year", axis=1)
print(df_2)

np.random.seed(0)
df = pd.DataFrame()
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df.drop(np.arange(0, 9, 2))
df = df.drop("strawberry", axis=1)
print(df)

print("------------------------------------------------------------")  # 60個

# 將欄位值依大小排序 – sort_values()

data = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
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
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "time": [1, 4, 5, 6, 3],
    "year": [2001, 2002, 2001, 2008, 2006],
}
df = pd.DataFrame(data)
print(df)
print(df.index % 2 == 0)
print(df[df.index % 2 == 0])

np.random.seed(0)
df = pd.DataFrame()
columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]
for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)
print(df)

df = df[df["apple"] >= 5]
df = df[df["kiwifruit"] >= 5]
# df = df.loc[df["apple"] >= 5][df["kiwifruit"] >= 5]
print(df)

print("------------------------------------------------------------")  # 60個

# 索引、欄位內容「一致」時的串接做法


def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df


columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)

print(df_data1)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis=0)
print(df1)

df2 = pd.concat([df_data1, df_data2], axis=1)
print(df2)

print("------------------------------------------------------------")  # 60個

# 索引、欄位內容「不一致」時的串接做法


def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df


columns1 = ["apple", "orange", "banana"]
columns2 = ["orange", "kiwifruit", "banana"]

df_data1 = make_random_df(range(1, 5), columns1, 0)
df_data2 = make_random_df(np.arange(1, 8, 2), columns2, 1)

print(df_data1)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis=0)
print(df1)

df2 = pd.concat([df_data1, df_data2], axis=1)
print(df2)

print("------------------------------------------------------------")  # 60個

# 於橫向串接時增列上一層的欄位


def make_random_df(index, columns, seed):
    np.random.seed(seed)
    df = pd.DataFrame()
    for column in columns:
        df[column] = np.random.choice(range(1, 101), len(index))
    df.index = index
    return df


columns = ["apple", "orange", "banana"]
df_data1 = make_random_df(range(1, 5), columns, 0)
df_data2 = make_random_df(range(1, 5), columns, 1)
print(df_data1)
print(df_data2)

df = pd.concat([df_data1, df_data2], axis=1, keys=["X", "Y"])
print(df)

Y_banana = df["Y", "banana"]
print(Y_banana)

print("------------------------------------------------------------")  # 60個

# 用 merge() 做 DataFrame 的交集合併

data1 = {
    "fruits": ["apple", "orange", "banana", "strawberry", "kiwifruit"],
    "year": [2001, 2002, 2001, 2008, 2006],
    "amount": [1, 4, 5, 6, 3],
}
df1 = pd.DataFrame(data1)
print("df1 :\n", df1)

data2 = {
    "fruits": ["apple", "orange", "banana", "strawberry", "mango"],
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


print("------------------------------------------------------------")  # 60個

from numpy import nan

print("------------------------------------------------------------")  # 60個

# 載入外部檔案並做資料整理
# 使用 Pandas 讀取 CSV 檔

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
url = "iris.data"
df = pd.read_csv(url, header=None)
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "class"]
print(df)

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

print("df存成csv檔")
df.to_csv("olympics.csv")

print("------------------------------------------------------------")  # 60個

# 處理 DataFrame 中的缺漏值
# 用 dropna() 刪除含有 NaN ( 缺漏值 ) 的列

#   借用 NumPy 的 nan 來設定 NaN 值
np.random.seed(0)

sample_df = pd.DataFrame(np.random.rand(8, 4))

#   設定亂數種子為 0

#   用 NumPy 隨機產生 8x4 的亂數資料並轉成 DataFrame

sample_df.iloc[1, 0] = nan

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

#   將部分值改成 NaN

print(sample_df)

#   檢視 DataFrame

sample_df_dropped = sample_df.dropna()

print(sample_df_dropped)

sample_df_dropped_2 = sample_df[[0, 1, 2]].dropna()

print(sample_df_dropped_2)

print("------------------------------------------------------------")  # 60個

# 用 fllna() 填補 NaN 值

np.random.seed(0)

sample_df = pd.DataFrame(np.random.rand(8, 4))

sample_df.iloc[1, 0] = nan

sample_df.iloc[2, 2] = nan

sample_df.iloc[6, 1] = nan

sample_df.iloc[5:, 3] = nan

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

# 取頭尾列 - head()、tail()

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

df = pd.DataFrame()

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]

print(df)

df_head = df.head(3)

df_tail = df.tail()

print("----前 3 列----\n", df_head)

print("----倒數 5 列----\n", df_tail)

print("------------------------------------------------------------")  # 60個

# 對 DataFrame 的值做運算

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

df = pd.DataFrame()

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

# 快速取得 DataFrame 各種統計數據

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

df = pd.DataFrame()

for column in columns:
    df[column] = np.random.choice(range(1, 11), 10)

df.index = [i for i in range(1, 11)]

print(df)

print(df.describe())

print("------------------------------------------------------------")  # 60個

# 計算行(列)之間的差 (diff)

np.random.seed(0)

columns = ["apple", "orange", "banana", "strawberry", "kiwifruit"]

df = pd.DataFrame()

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

mean_df = grouped_region.mean()
print(mean_df)

print("------------------------------------------------------------")  # 60個


from __future__ import print_function
import pandas as pd
import numpy as np

s = pd.Series([1, 3, 6, np.nan, 4, 1])  # similar with 1D numpy
print(s)
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

print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by="B"))

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd
import numpy as np

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

# mixed selection: ix
print(df.ix[:3, ["A", "C"]])
# Boolean indexing
print(df[df.A > 0])

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=["A", "B", "C", "D"])

df.iloc[2, 2] = 1111
df.loc["2013-01-03", "D"] = 2222
df.A[df.A > 0] = 0
df["F"] = np.nan
df["G"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
print(df)

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(
    np.arange(24).reshape((6, 4)), index=dates, columns=["A", "B", "C", "D"]
)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how="any"))  # how={'any', 'all'}
print(df.fillna(value=0))
print(pd.isnull(df))

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd

# read from
data = pd.read_csv("data/student.csv")
print(data)

# save to
data.to_pickle("tmp_student.pickle")

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd
import numpy as np

# concatenating
# ignore index
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df3 = pd.DataFrame(np.ones((3, 4)) * 2, columns=["a", "b", "c", "d"])
res = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

# join, ('inner', 'outer')
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"], index=[1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["b", "c", "d", "e"], index=[2, 3, 4])
res = pd.concat([df1, df2], axis=1, join="outer")
res = pd.concat([df1, df2], axis=1, join="inner")

# join_axes
res = pd.concat([df1, df2], axis=1, join_axes=[df1.index])

# append
df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["b", "c", "d", "e"], index=[2, 3, 4])
res = df1.append(df2, ignore_index=True)
res = df1.append([df2, df3])

s1 = pd.Series([1, 2, 3, 4], index=["a", "b", "c", "d"])
res = df1.append(s1, ignore_index=True)

print(res)

print("------------------------------------------------------------")  # 60個

from __future__ import print_function
import pandas as pd

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

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

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

print("------------------------------------------------------------")  # 60個
