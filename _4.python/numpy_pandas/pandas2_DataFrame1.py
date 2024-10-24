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


"""
1. 建立
2. Info
3. 修改
4. 合併

print("------------------------------------------------------------")  # 60個
print("1. 建立 df 的方法")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("2. df 的 Info 屬性 與 方法")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("3. 建立 df 的方法")
print("------------------------------------------------------------")  # 60個

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


def make_data_frame():
    # print("建立df, 二維串列4X5 轉 df, 加上欄名與index")
    datas = [
        [92, 81, 81, 92],  # 國文
        [89, 79, 82, 72],  # 英文
        [71, 92, 89, 95],  # 數學
        [88, 89, 98, 77],  # 社會
        [95, 74, 89, 85],  # 自然
    ]
    columns = ["國文", "英文", "數學", "社會", "自然"]
    index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
    df = pd.DataFrame(np.array(datas).T, columns=columns, index=index)
    return df


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


print("目前 Pandas 版本 :")
cc = pd.__version__
print(cc)

# many
# pd.show_versions()

print("------------------------------------------------------------")  # 60個
print("1. 建立 df 的方法")
print("------------------------------------------------------------")  # 60個

print("建立df, 一維串列 轉 df")

datas = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df = pd.DataFrame(datas)
print(df)

print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, Series 轉 字典 轉 df")

s1 = pd.Series(["唐三藏", "孫悟空", "豬八戒", "沙悟淨"])
s2 = pd.Series([65, 90, 81, 79])  # 國文成績
s3 = pd.Series([92, 72, 85, 53])  # 英文成績
datas = {"姓名": s1, "國文": s2, "英文": s3}

print("字典 轉 df")
df = pd.DataFrame(datas)
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series 合併4")

index = ["國文", "英文", "數學", "社會", "自然"]

datas1 = [92, 89, 71, 88, 95]  # 唐三藏 的成績
datas2 = [81, 79, 92, 89, 74]  # 孫悟空 的成績
datas3 = [81, 82, 89, 98, 89]  # 豬八戒 的成績
datas4 = [92, 72, 95, 77, 85]  # 沙悟淨 的成績

series1 = pd.Series(datas1, index=index)
series2 = pd.Series(datas2, index=index)
series3 = pd.Series(datas3, index=index)
series4 = pd.Series(datas4, index=index)

print("5個Series組成一個df")
df = pd.DataFrame([series1, series2, series3, series4])
print(df)

index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df.index = index
print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("2. df 的 Info 屬性 與 方法")
print("------------------------------------------------------------")  # 60個

df = make_data_frame()
print(df)

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

print(df.info())

print('顯示values')
print(df.values)
print(df.values[2])
print(df.values[1][2])
print(len(df))

print('df使用記憶體大小')
cc = df.info(memory_usage='deep')
print(cc)

print("df之大小")
M, N = df.shape
print(df.shape)
print('df之大小', M, 'X',N)

print(df.shape)

# 列出各列的列索引標籤、表格內容
print(df.shape[0])
print(df.index.values)

# 列出所有欄索引(欄位名稱)
for col in range(df.shape[1]):
    print(df.columns.values[col], " ", end="")
print()

# 使用loc列出各列的列索引、欄位內容
for row in range(df.shape[0]):
    print(df.index.values[row], " ", end="")
    for col in range(df.shape[1]):
        print(df.loc[df.index.values[row]][df.columns.values[col]], " ", end="")
    print()

print("顯示df之describe(統計資料)")
print(df.describe())

print(df.count())
print(df.mean())
print(df.std())
print(df.min())
print(df.median())
print(df.max())
print(df.sum())

# print('df若有字串(中英文), 不能直接做mean(), 但可做 max() min() sum()')

"""

# 對 DataFrame 的值做運算

print("計算每一科的平均, axis=0, 0直1橫")
print(df.mean(axis=0))

print("所有人成績 乘 2")
double_df = df * 2
print(double_df)

print("所有人成績 平方")
square_df = df * df
print(square_df)

print("所有人成績 開根號 乘 10")
sqrt_df = np.sqrt(df) * 10
print(sqrt_df)

# 計算行(列)之間的差 (diff)

df_diff = df.diff(-2, axis=0)
print(df_diff)

print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("新增欄位 體育")
df["體育"] = [88, 98, 80, 94]
print(df)

print("移除欄位 自然")
df4 = df.drop(["自然"], axis=1)
print(df4)

print("顯示 數學 欄的資料")
cc = df["數學"]
print(cc)

print("對df的某欄做運算")
print("最重 :", df["數學"].max())
print("最輕 :", df["數學"].min())
print("總重 :", df["數學"].sum())
print("平均 :", df["數學"].mean())

print("------------------------------------------------------------")  # 60個

print("刪除 df 的 欄位 或 索引 – drop()")

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("刪除欄位 數學")
# df1 = df.drop("數學", axis=1) # same
df1 = df.drop(["數學"], axis=1)
print(df1)

print("刪除欄位 數學 自然")
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)

print("刪除欄位 1 2, 即刪除 國文 英文")
df5 = df.drop(df.columns[1:3], axis=1)
print(df5)

print("刪除索引 2 3, 即刪除 豬八戒 沙悟淨")
df4 = df.drop(df.index[2:4])
print(df4)

print("刪除索引 0 1, 即刪除 唐三藏 孫悟空")
df5 = df.drop([0, 1])
print(df5)

print("刪除索引 偶數索引")
df6 = df.drop(np.arange(0, 4, 2))
print(df6)

print("找出 社會 < 85 的資料")
print(df[df["社會"] < 85])
print("找出 社會 < 85 的資料 的 索引")
print(df[df["社會"] < 85].index)
print("刪除 社會 < 85 的資料 列")
idx = df[df["社會"] < 85].index
df7 = df.drop(idx)
print(df7)

print("重建df")
df = make_data_frame_from_dict()  # 字典 轉 df

df.set_index("姓名", inplace=True)
print(df)

print("移除索引 index 孫悟空 豬八戒")
df2 = df.drop(["孫悟空", "豬八戒"])
print(df2)

print("移除索引 0 2, 即 唐三藏 豬八戒")
df3 = df.drop(df.index[[0, 2]])
print(df3)

# 不可重建
# print('重建df')
# df = make_data_frame_from_dict()  # 字典 轉 df

print("移除孫悟空成績 ->")
df1 = df.drop("孫悟空")
print(df1)
print("移除數學科成績 ->")
df2 = df.drop("數學", axis=1)
print(df2)
print("移除數學科及自然科成績 ->")
df3 = df.drop(["數學", "自然"], axis=1)
print(df3)
print("移除孫悟空到豬八戒成績 ->")
df4 = df.drop(df.index[1:4])
print(df4)
print("移除數學科到自然科成績 ->")
df5 = df.drop(df.columns[1:4], axis=1)
print(df5)

print("------------------------------")  # 30個

print("重建df")
df = make_data_frame_from_dict()  # 字典 轉 df

print("df反置")
df7 = df.T
print(df7)

# 前 index, 後 column
# index [0, 1, 2, 3] 表示 索引 "唐三藏", "孫悟空", "豬八戒", "沙悟淨"
# column [3, 4, 5] 表示 欄位 "數學" "社會" "自然"
df9 = df.iloc[[0, 1, 2, 3], [3, 4, 5]]
print(df9)

# 取出dataframe其中一欄就是series
print(df["姓名"])
print(df["國文"])

# 自行建立一個pandas series
score = pd.Series([780, 670, 900, 810], name="成績")
print(score)
# 將series加入dataframe導致增加一欄(column)

df["成績"] = score
print(df)

print("從 df 篩選出想要的資料")
cc = df.index % 2 == 0
print(cc)
cc = df[df.index % 2 == 0]
print(cc)

print("------------------------------------------------------------")  # 60個

print("顯示欄資料")
print('df["自然"] ->')
print(df["自然"])
print('df[["英文", "數學", "自然"] ->')
print(df[["英文", "數學", "自然"]])
print("df[df.數學>=80] ->")
print(df[df.數學 >= 80])

print("------------------------------")  # 30個

print("------------------------------")  # 30個


print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("df 轉 字典")
alldata = df.to_dict("split")
print(type(alldata))

# 會有3個list構成: columns, index, data
print("字典")
print(alldata)
print("欄位")
print(alldata["columns"])
print("索引")
print(alldata["index"])
print("資料")
print(alldata["data"])

# 列出所有欄索引標籤(欄位名稱)
for col in range(len(alldata["columns"])):
    print(alldata["columns"][col], " ", end="")
print()

# 列出各列的列索引標籤、欄位內容
for row in range(len(alldata["index"])):
    print(alldata["index"][row], " ", end="")
    for col in range(len(alldata["columns"])):
        print(alldata["data"][row][col], " ", end="")
    print()

print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

datas = {
    "姓名": ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"],
    "國文": [92, 81, 81, 92],
    "英文": [89, 79, 82, 72],
    "數學": [71, 92, 89, 95],
    "社會": [88, 89, 98, 77],
    "自然": [95, 74, 89, 85],
}

datas = {
    "姓名": ["約翰", "瑪莉", "麥可", "大衛"],
    "年齡": [16, 17, 16, 18],
    "性別": ["男", "女", "男", "男"],
    "成績": [78, 67, 90, 81],
}
df = pd.DataFrame(datas)
print(df)

print("建立樞紐分析表 pivot_table")
# aggfunc: mean是求平均, sum是求總和
table = pd.pivot_table(
    data=df, index=["性別"], columns=["年齡"], values=["成績"], aggfunc={"成績": "mean"}
)
print(table)
# 查看欄索引標籤
# 發現是元組tuple型態
print(table.columns.values)
# 查看列索引標籤
print(table.index.values)

print("建立樞紐分析表 pivot_table")
# aggfunc: mean是求平均, sum是求總和
table = pd.pivot_table(data=df, index=["性別"], values=["成績"], aggfunc={"成績": "sum"})
print(table)
# 查看欄索引標籤
print(table.columns.values)
# 查看列索引標籤
print(table.index.values)

print("------------------------------------------------------------")  # 60個

print("建立空的df, 再加入資料至df")

df = pd.DataFrame()

df["國文"] = [92, 81, 81, 92]
df["英文"] = [89, 79, 82, 72]
df["數學"] = [71, 92, 89, 95]
df["社會"] = [88, 89, 98, 77]
df["自然"] = [95, 74, 89, 85]
df.index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
print(df)

print("國文 > 75 者")
df1 = df[df["國文"] >= 75]
print(df1)

print("英文 > 75 者")
df2 = df[df["英文"] >= 75]
print(df2)

print("------------------------------------------------------------")  # 60個

print("建立空的df, 再加入資料至df")

df = pd.DataFrame()

df["國文"] = [92, 81, 81, 92]
df["英文"] = [89, 79, 82, 72]
df["數學"] = [71, 92, 89, 95]
df["社會"] = [88, 89, 98, 77]
df["自然"] = [95, 74, 89, 85]
# df.index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"] 不能設定文字
print(df)


print("------------------------------------------------------------")  # 60個

print("建立df, 使用Series 合併1")

se1 = pd.Series({"唐三藏": 65, "孫悟空": 90, "豬八戒": 81, "沙悟淨": 79})  # 國文成績
se2 = pd.Series({"唐三藏": 92, "孫悟空": 72, "豬八戒": 85, "沙悟淨": 53})  # 英文成績
se3 = pd.Series({"唐三藏": 78, "孫悟空": 76, "豬八戒": 91, "沙悟淨": 47})  # 數學成績
se4 = pd.Series({"唐三藏": 70, "孫悟空": 56, "豬八戒": 94, "沙悟淨": 80})  # 社會成績
se5 = pd.Series({"唐三藏": 83, "孫悟空": 93, "豬八戒": 89, "沙悟淨": 94})  # 自然成績

# 方法一
df = pd.concat([se1, se2, se3, se4, se5], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
df.columns = ["國文", "英文", "數學", "社會", "自然"]
print(df)

# 方法二
df = pd.DataFrame({"國文": se1, "英文": se2, "數學": se3, "社會": se4, "自然": se5})
print(df)

print("------------------------------------------------------------")  # 60個

url = "https://www.tiobe.com/tiobe-index/"
tables = pd.read_html(url, header=0, keep_default_na=False)
print(tables[0])

print("------------------------------------------------------------")  # 60個

print("建立df, 二維串列 轉 df")

datas = [
    [92, 81, 81, 92],  # 國文
    [89, 79, 82, 72],  # 英文
    [71, 92, 89, 95],  # 數學
    [88, 89, 98, 77],  # 社會
    [95, 74, 89, 85],  # 自然
]

columns = ["國文", "英文", "數學", "社會", "自然"]
df = pd.DataFrame(np.array(datas).T, columns=columns)

print("使用預設索引index 從0開始數")
print(df)

print("重新設定索引index 從1開始數")
df.index = range(1, 5)
print(df)

print("重新設定索引index")
index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df.index = index
print(df)

print("------------------------------------------------------------")  # 60個

df = make_data_frame()
print(df)

print("二維串列 轉 df")

print("建立資料 二維串列 3X4")

datas1 = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
]

datas2 = [
    [7, 7, 7, 7],
    [8, 8, 8, 8],
    [9, 9, 9, 9],
]

print("np陣列 轉 df")

columns = list("ABCD")
df_a = pd.DataFrame(datas1, columns=columns)
df_b = pd.DataFrame(datas2, columns=columns)

print("合併兩個 df, axis=0 : 垂直連接")
df = pd.concat([df_a, df_b], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("重新設定索引index")
df.index = range(6)
print(df)

print("------------------------------------------------------------")  # 60個

datas1 = {
    "順序": [1, 2, 3, 4],
    "中文名": ["鼠", "牛", "虎", "兔"],
    "英文名": ["mouse", "ox", "tiger", "rabbit"],
    "體重": [3, 48, 33, 8],
    "代表": ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"],
}
print("字典轉DataFrame")
df1 = pd.DataFrame(datas1)
print("df1:\n", df1)

datas2 = {
    "順序": [5, 6, 7, 8],
    "中文名": ["龍", "蛇", "馬", "羊"],
    "英文名": ["dragon", "snake", "horse", "goat"],
    "體重": [38, 16, 36, 29],
    "代表": ["逗逗龍", "貪吃蛇", "草泥馬", "喜羊羊"],
}
print("字典轉DataFrame")
df2 = pd.DataFrame(datas2)
print("df2:\n", df2)

print("合併兩個DataFrame")
df3 = pd.concat([df1, df2])
print("df3:\n", df3)

# 設定陣列的第一欄
df3.set_index("順序", inplace=True)

# 排序, 升冪排序
df3.sort_values(by=["順序"])
print("df3:\n", df3)

print("------------------------------------------------------------")  # 60個

print("二維串列 轉 df")

print("建立df, 二維串列 轉 df")

datas = [
    [92, 81, 81, 92],  # 國文
    [89, 79, 82, 72],  # 英文
    [71, 92, 89, 95],  # 數學
    [88, 89, 98, 77],  # 社會
    [95, 74, 89, 85],  # 自然
]

columns = ["國文", "英文", "數學", "社會", "自然"]
index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df = pd.DataFrame(np.array(datas).T, columns=columns, index=index)
print(df)

for i in range(4):
    print("index :", i, end="\t")
    print("中文名 :", df.iloc[i, 0], end="\t")
    print("數學 :", df.iloc[i, 2], end="\n")

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

datas = {
    "國文": {"唐三藏": 65, "孫悟空": 90, "豬八戒": 81, "沙悟淨": 79},
    "英文": {"唐三藏": 92, "孫悟空": 72, "豬八戒": 85, "沙悟淨": 53},
    "數學": {"唐三藏": 78, "孫悟空": 76, "豬八戒": 91, "沙悟淨": 47},
    "社會": {"唐三藏": 70, "孫悟空": 56, "豬八戒": 94, "沙悟淨": 80},
    "自然": {"唐三藏": 83, "孫悟空": 93, "豬八戒": 89, "沙悟淨": 94},
}
df = pd.DataFrame(datas)
print(df)

print("欄位 自然 的資料")
print(df["自然"])
print("欄位 國文 數學 自然 的資料")
print(df[["國文", "數學", "自然"]])
print("欄位 國文 >= 80 的資料")
print(df[df["國文"] >= 80])

print("索引 1 的資料(孫悟空)")
print(df.values[1])
print("索引 1 欄位 2 的資料(孫悟空 數學)")
print(df.values[1][2])

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

datas = {
    "國文": {"唐三藏": 65, "孫悟空": 90, "豬八戒": 81, "沙悟淨": 79},
    "英文": {"唐三藏": 92, "孫悟空": 72, "豬八戒": 85, "沙悟淨": 53},
    "數學": {"唐三藏": 78, "孫悟空": 76, "豬八戒": 91, "沙悟淨": 47},
    "社會": {"唐三藏": 70, "孫悟空": 56, "豬八戒": 94, "沙悟淨": 80},
    "自然": {"唐三藏": 83, "孫悟空": 93, "豬八戒": 89, "沙悟淨": 94},
}
df = pd.DataFrame(datas)
print(df)

print("修改 孫悟空 的 所有成績為 為 100")
df.loc["孫悟空", :] = 100

print("新df")
print(df)

print("------------------------------------------------------------")  # 60個

# 索引、欄位內容「一致」時的串接做法

print("建立df, 使用Series 合併7")

columns = ["國文", "英文", "數學"]
df_data1 = pd.DataFrame()
for column in columns:
    df_data1[column] = np.random.choice(range(1, 101), 4)
df_data1.index = range(1, 5)
print(df_data1)

df_data2 = pd.DataFrame()
for column in columns:
    df_data2[column] = np.random.choice(range(1, 101), 4)
df_data2.index = range(1, 5)
print(df_data2)

df1 = pd.concat([df_data1, df_data2], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df1)

df2 = pd.concat([df_data1, df_data2], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df2)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用 合併")


def make_data_frame():
    # print("建立df, 二維串列4X5 轉 df, 加上欄名與index")
    datas = [
        [92, 81, 81, 92],  # 國文
        [89, 79, 82, 72],  # 英文
        [71, 92, 89, 95],  # 數學
        [88, 89, 98, 77],  # 社會
        [95, 74, 89, 85],  # 自然
    ]
    columns = ["國文", "英文", "數學", "社會", "自然"]
    index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
    df = pd.DataFrame(np.array(datas).T, columns=columns, index=index)
    return df


df1 = make_data_frame()
print(df1)

df2 = make_data_frame()
print(df2)

print("pd.concat() 合併, axis = 1 水平連接")
df = pd.concat([df1, df2], axis=1, keys=["X", "Y"])  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 使用 合併")
print("索引、欄位內容「不一致」時的串接做法")

print("製作df1, df2, 索引欄位不一致")
columns1 = ["國文", "英文", "數學"]
columns2 = ["物理", "化學", "生物"]

df1 = pd.DataFrame()
for column in columns1:
    df1[column] = np.random.choice(range(1, 101), 4)
df1.index = range(1, 5)
print(df1)

df2 = pd.DataFrame()
for column in columns2:
    df2[column] = np.random.choice(range(1, 101), 4)
df2.index = np.arange(1, 8, 2)
print(df2)

print("pd.concat() 合併, axis = 0 垂直連接")
df = pd.concat([df1, df2], axis=0)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("pd.concat() 合併, axis = 1 水平連接")
df = pd.concat([df1, df2], axis=1)  # axis=0 : 垂直連接, axis=1 : 水平連接
print(df)

print("------------------------------------------------------------")  # 60個

# 用 merge() 做 DataFrame 的交集合併

datas1 = {
    "姓名": ["唐三藏", "孫悟空", "豬八戒", "沙悟淨", "白龍馬"],
    "國文": [65, 90, 81, 79, 88],
    "英文": [92, 72, 85, 53, 69],
}
df1 = pd.DataFrame(datas1)
print(df1)

datas2 = {
    "姓名": ["唐三藏", "孫悟空", "豬八戒", "沙悟淨", "紅孩兒"],
    "國文": [65, 90, 81, 79, 92],
    "數學": [78, 76, 91, 47, 88],
}
df2 = pd.DataFrame(datas2)
print(df2)

print("pd.merge(), 使用 inner, 取交集")
df = pd.merge(df1, df2, on="姓名", how="inner")
print(df)

print("pd.merge(), 使用 outer, 取聯集")
df = pd.merge(df1, df2, on="姓名", how="outer")
print(df3)

print("------------------------------------------------------------")  # 60個

datas = {
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
}

print("字典轉 df")
df2 = pd.DataFrame(datas)
print(df2)

print("------------------------------------------------------------")  # 60個

datas = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
    [5, 5, 5, 5],
    [6, 6, 6, 6],
]

columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, index=dates, columns=columns)

print(df["A"], df.A)
print(df[0:3], df["20130102":"20130104"])

# select by label: loc
print(df.loc["20130102"])
print(df.loc[:, ["A", "B"]])
print(df.loc["20130102", ["A", "B"]])

""" no ix
# mixed selection: ix
print(df.ix[:3, ["A", "C"]])
# Boolean indexing
print(df[df.A > 0])
"""
print("------------------------------------------------------------")  # 60個

datas = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
    [5, 5, 5, 5],
    [6, 6, 6, 6],
]

columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, columns=columns, index=dates)
print(df)

print(df.A)

df.iloc[2, 2] = 1111
df.loc["2013-01-03", "D"] = 2222
df["F"] = np.nan
df["G"] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range("20130101", periods=6))
print(df)

print("------------------------------------------------------------")  # 60個

print("建立df, 二維串列4X5 轉 df, 加上欄名與index")

datas = [
    [92, 81, 81, 92],  # 國文
    [89, 79, 82, 72],  # 英文
    [71, 92, 89, 95],  # 數學
    [88, 89, 98, 77],  # 社會
    [95, 74, 89, 85],  # 自然
]
columns = ["國文", "英文", "數學", "社會", "自然"]
index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df = pd.DataFrame(np.array(datas).T, columns=columns, index=index)
print(df)

print("顯示 國文 欄")
cc = df.國文
print(cc)

print("顯示df之1:3")
print(df[3:5])

print("顯示df之 國文 英文 社會 欄")
print(df[["國文", "英文", "社會"]])

print("顯示")
print(df[df.數學 > 80])

print("加入TAG")
df["TAG"] = ["AAA", "BBB", "AAA", "BBB"]
print(df)

print(df.groupby("TAG").sum())

print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("data2/titanic_data.csv")
# 顯示資料集的形狀
print(titanic.shape)

# 顯示前5筆
print(titanic.head())

# 顯示統計摘要資訊
print(titanic.describe())

# 顯示資料集資訊
print(titanic.info())

print("---檢查PassengerId欄位是否是唯一值---")
print(np.unique(titanic["PassengerId"].values).size)

print("---指定DataFrame物件的索引欄位---")
titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())

print("---新增SexCode欄位---")
titanic["SexCode"] = np.where(titanic["Sex"] == "female", 1, 0)
print(titanic.head())

print("---PCass欄位轉換成數值資料---")
class_mapping = {"1st": 1, "2nd": 2, "3rd": 3}
titanic["PClass"] = titanic["PClass"].map(class_mapping)
print(titanic.head())

print("---檢查Age欄位的遺漏值有多少---")
print(titanic.isnull().sum())
print(sum(titanic["Age"].isnull()))

print("---補值成平均值---")
VALUE = titanic["Age"].mean()
titanic["Age"].fillna(value=VALUE, inplace=True)  # 將指定欄位內空資料填入指定數值
print(sum(titanic["Age"].isnull()))

print("---顯示性別人數和計算平均年齡---")
print("性別人數:")
print(titanic["Sex"].groupby(titanic["Sex"]).size())
print(titanic.groupby("Sex")["Age"].mean())

print("---處理姓名欄位---")

import re

patt = re.compile(r"\,\s(\S+\s)")
titles = []
for index, row in titanic.iterrows():
    m = re.search(patt, row["Name"])
    if m is None:
        title = "Mrs" if row["SexCode"] == 1 else "Mr"
    else:
        title = m.group(0)
        title = re.sub(r",", "", title).strip()
        if title[0] != "M":
            title = "Mrs" if row["SexCode"] == 1 else "Mr"
        else:
            if title[0] == "M" and title[1] == "a":
                title = "Mrs" if row["SexCode"] == 1 else "Mr"
    titles.append(title)
titanic["Title"] = titles

print("Title類別:")
print(np.unique(titles).shape[0], np.unique(titles))

print("---修正類別錯誤顯示Titel人數---")
titanic["Title"] = titanic["Title"].replace("Mlle", "Miss")
titanic["Title"] = titanic["Title"].replace("Ms", "Miss")
titanic.to_csv("tmp_titanic_pre.csv", encoding="utf8")
print("Title人數:")
print(titanic["Title"].groupby(titanic["Title"]).size())
print("---顯示平均生存率---")
""" NG
print("平均生存率:")
print(titanic[["Title","Survived"]].groupby(titanic["Title"]).mean())
"""
print("------------------------------------------------------------")  # 60個

titanic = pd.read_csv("data2/titanic_pre.csv")
titanic["Died"] = np.where(titanic["Survived"] == 0, 1, 0)
print(titanic.head())

print("------------------------------")  # 30個

# 繪出直方圖的年齡分佈, 生存或死亡
titanic["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 0]
df["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 1]
df["Age"].plot(kind="hist", bins=15)

# 分類顯示Title欄位的生存和死亡數
fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived", "Died"]].groupby(titanic["Title"]).sum()
df.plot(kind="bar", ax=axes[0])
df = titanic[["Survived", "Died"]].groupby(titanic["Title"]).mean()
df.plot(kind="bar", ax=axes[1])

# 分類顯示Sex欄位的生存和死亡數
fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])
df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])

# 分類顯示PClass欄位的生存和死亡數
df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")
df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

# 計算相關係數
df = titanic.drop("PassengerId", axis=1)
df = df.drop("Died", axis=1)
df = df.drop("Title", axis=1)
# print(df.corr()) NG
df.to_csv("tmp_titanic_train.csv", encoding="utf8")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 新竹市氣象資料1992_2020

columns = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]
index = [
    "歷史最高溫",
    "平均高溫",
    "日均氣溫",
    "平均低溫",
    "歷史最低溫",
    "平均降雨量",
    "平均降雨天數",
    "平均相對濕度",
    "月均日照時數",
]

datas = [
    [30.3, 30.6, 33.8, 34.1, 35.5, 37.4, 38.0, 39.4, 38.8, 37.9, 34.4, 31.1],
    [19.1, 19.4, 21.6, 25.6, 28.9, 31.5, 33.2, 32.8, 31.2, 28.0, 25.1, 21.1],
    [15.7, 16.0, 18.0, 21.9, 25.2, 27.9, 29.3, 28.9, 27.3, 24.4, 21.5, 17.7],
    [13.1, 13.4, 15.2, 18.9, 22.2, 24.9, 26.0, 25.8, 24.4, 21.8, 18.8, 15.1],
    [-0.1, 3.5, 3.4, 4.9, 11.7, 14.7, 20.2, 18.9, 14.7, 9.5, 6.6, 4.0],
    [75.7, 123.0, 159.8, 161.9, 249, 252.0, 120.2, 197.1, 174.5, 53.6, 51.1, 57.7],
    [9.8, 11.3, 13.5, 12.7, 12, 10.6, 7.9, 10.7, 8.9, 5.5, 6.8, 8.0],
    [78.3, 80.4, 79.6, 78.4, 78.1, 77, 74.3, 75.9, 74.5, 73.8, 75.5, 76.3],
    [106.7, 91, 101, 111.6, 145.4, 185, 240.6, 209.7, 193.5, 190, 144.8, 126.1],
]

data_year = [39.4, 26.5, 22.8, 20.0, -0.1, 1675.6, 117.7, 76.8, 1845.4]

df = pd.DataFrame(datas, columns=columns, index=index)
print(df)

# 資料運算要做橫向運算, df先轉成直向
df2 = df.T
print("全年")
print("歷史最高溫 :", df2["歷史最高溫"].max())
print("平均高溫 :", df2["平均高溫"].mean())
print("日均氣溫 :", df2["日均氣溫"].mean())
print("平均低溫 :", df2["平均低溫"].mean())
print("歷史最低溫 :", df2["歷史最低溫"].min())
print("平均降雨量 :", df2["平均降雨量"].sum())
print("平均降雨天數 :", df2["平均降雨天數"].sum())
print("平均相對濕度 :", df2["平均相對濕度"].mean())
print("月均日照時數 :", df2["月均日照時數"].sum())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

datas = np.arange(24).reshape((6, 4))
columns = ["A", "B", "C", "D"]
dates = pd.date_range("20130101", periods=6)

df = pd.DataFrame(datas, columns=columns, index=dates)

df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df.dropna(axis=0, how="any"))  # how={'any', 'all'}

VALUE = 0
print(df.fillna(value=VALUE))  # 將df內空資料填入指定數值

print("空資料 :")
print(pd.isnull(df))

print("------------------------------------------------------------")  # 60個

# 處理 DataFrame 中的缺漏值
# 用 dropna() 刪除含有 NaN ( 缺漏值 ) 的列

#   借用 NumPy 的 np.nan 來設定 NaN 值
df = pd.DataFrame(np.random.rand(8, 4))

#   設定亂數種子為 0
#   用 NumPy 隨機產生 8x4 的亂數資料並轉成 DataFrame

df.iloc[1, 0] = np.nan
df.iloc[2, 2] = np.nan
df.iloc[6, 1] = np.nan
df.iloc[5:, 3] = np.nan

#   將部分值改成 NaN
print(df)

#   檢視 DataFrame
df_dropped = df.dropna()
print(df_dropped)
df_dropped_2 = df[[0, 1, 2]].dropna()
print(df_dropped_2)

print("------------------------------------------------------------")  # 60個

# 讀取資料
df = pd.read_csv("_new/customer.csv")
print(df)

print("空值的處理")

print("各欄位有 空資料 的個數 :")
print(df.isnull().sum())

print("有空值的記錄筆數:", df.isnull().any(axis=1).sum())
print("有空值的欄位數:", df.isnull().any(axis=0).sum())
print("age欄有空值的記錄:")
df2 = df[df["age"].isnull()]
print(df2)

print("------------------------------")  # 30個

print("將age的空值填入0")
df_sample = df.copy()
VALUE = 0
df_sample["age"] = df_sample["age"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
print(df_sample.head())

print("將age的空值填入平均值")
df_sample = df.copy()
VALUE = df_sample["age"].mean()
df_sample["age"] = df_sample["age"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
print(df_sample.head())

df_sample["gender"] = df_sample["gender"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample["area"] = df_sample["area"].ffill()  # ffill()拿前一個值往下填, 承上
print(df_sample.head())

print("刪除不完整的資料")
df3 = df.dropna()
print(df3)

print("------------------------------")  # 30個

print("資料基本清理")
df_sample = df.copy()
VALUE = df_sample["age"].mean()
df_sample["age"] = df_sample["age"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
df_sample["gender"] = df_sample["gender"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample["area"] = df_sample["area"].ffill()  # ffill()拿前一個值往下填, 承上

print("去除重覆記錄")
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
print(df_sample.head())

print("去除欄位中的空白")
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
print(df_sample.head())

print("轉換值的格式")
df_sample["age"] = df_sample["age"].astype("int32")
print(df_sample.head())

print("------------------------------")  # 30個

print("資料基本清理")
df_sample = df.copy()
VALUE = value = df_sample["age"].mean()
df_sample["age"] = df_sample["age"].fillna(VALUE)  # 將指定欄位內空資料填入指定數值
df_sample["gender"] = df_sample["gender"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample["area"] = df_sample["area"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
df_sample["age"] = df_sample["age"].astype("int32")

print("篩選女性的資料")
cc = df_sample[(df_sample["gender"] == "Female")]
print(cc)

print("篩選男性且大於50歲的資料")
cc = df_sample[(df_sample["gender"] == "Male") & (df_sample["age"] > 50)]
print(cc)

print("篩選住在新北市三重區或基隆市中正區的資料")
cc = df_sample[(df_sample["area"] == "新北市三重區") | (df_sample["area"] == "基隆市中正區")]
print(cc)

print("------------------------------")  # 30個

print("資料基本清理")
df_sample = df.copy()
VALUE = value = df_sample["age"].mean()
df_sample["age"] = df_sample["age"].fillna(VALUE)  # 將指定欄位內空資料填入指定數值
df_sample["gender"] = df_sample["gender"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample["area"] = df_sample["area"].ffill()  # ffill()拿前一個值往下填, 承上
df_sample.drop_duplicates(subset="id", keep="first", inplace=True)
df_sample["job"] = df_sample["job"].str.strip()
df_sample["job"] = df_sample["job"].str.replace(" ", "")
df_sample["age"] = df_sample["age"].astype("int32")

print("客戶中男女生的平均年齡")
cc = df_sample.groupby("gender")["age"].mean()
print(cc)

print("------------------------------")  # 30個

print("客戶中住各區的人數")
cc = df_sample.groupby("area")["id"].count()
print(cc)

print("------------------------------")  # 30個

print("客戶中男女生的平均年齡、最年長及最年輕的年齡")
cc = df_sample.groupby("gender")["age"].agg(["mean", "max", "min"])
print(cc)

print("------------------------------------------------------------")  # 60個

print("字典 轉 df")

datas = {
    "國文": [92, 81, 81, 92],
    "英文": [89, 79, 82, 72],
    "數學": [71, 92, 89, 95],
    "社會": [88, 89, 98, 77],
    "自然": [95, 74, 89, 85],
}

index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df = pd.DataFrame(datas, index=index)
print(df)

print(df["國文"])

print(df[["英文", "數學"]])

print(df[0:2])

print(df["唐三藏":"豬八戒"])

print(df.loc["唐三藏", "英文"])

print(df.loc[["豬八戒", "沙悟淨"], ["英文", "數學"]])

print(df.loc[:, ["英文", "數學"]])

print(df.loc["孫悟空":"豬八戒", "國文":"英文"])

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

df = pd.read_csv("data/titanic20.csv")

print("取出某欄位的資料方法1")
cc = df["Sex"].head()
print(cc)

print("取出某欄位的資料方法2, 英文字串可以直接當變數用")
cc = df.Sex.head()
print(cc)

print("對 空資料之處理")

df = pd.read_csv("data/titanic20.csv")

# print("檢視前幾行\n", df.head())

print("原df之個數")
print(len(df))
print("欄位 Age 為 空資料 之個數")
print(df["Age"].isnull().sum())

print("將原df之 Age為空資料 之列 刪除, 新建df")
df2 = df.dropna(subset=["Age"])
print("新df之個數")
print(len(df2))

print("------------------------------")  # 30個

df = pd.read_csv("data/titanic20.csv")

print("將原df之 Age為空資料 之列 填入20")
VALUE = 20
df["Age"] = df["Age"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值

print("欄位 Age 為 空資料 之個數")
print(df["Age"].isnull().sum())

# print("檢視前幾行\n", df.head())

print("------------------------------")  # 30個

df = pd.read_csv("data/titanic20.csv")

print("將原df之 Age為空資料 之列 填入 Age 之平均")
VALUE = df["Age"].mean()
df["Age"] = df["Age"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值

print("欄位 Age 為 空資料 之個數")
print(df["Age"].isnull().sum())

# print("檢視前幾行\n", df.head())

print("------------------------------------------------------------")  # 60個

print("pd.concat() 默認情況下是縱向連接兩個DataFrame")

columns = list("ABCD")
datas1 = np.ones((3, 4)) * 1
datas2 = np.ones((3, 4)) * 2
datas3 = np.ones((3, 4)) * 3
df1 = pd.DataFrame(datas1, columns=columns)
df2 = pd.DataFrame(datas2, columns=columns)
df3 = pd.DataFrame(datas3, columns=columns)
print("3個 df")
print(df1)
print(df2)
print(df3)

print("使用 concat(), 直向連接, 索引錯誤")
res = pd.concat([df1, df2, df3])
print(res)

print("使用 concat(), 直向連接, 重排索引index")
print("ignore_index = True可以忽略合併時舊的index，改採用自動生成的index")
res = pd.concat([df1, df2, df3], ignore_index=True)
print(res)

print("------------------------------------------------------------")  # 60個

print("pd.concat() 合併資料可以使用 join，outer 是聯集(預設)、inner 是交集(如果資料不存在時，NaN)")

datas1 = np.ones((3, 4)) * 1
datas2 = np.ones((3, 4)) * 2
df1 = pd.DataFrame(datas1, columns=["A", "B", "C", "D"], index=[1, 2, 3])
df2 = pd.DataFrame(datas2, columns=["B", "C", "D", "E"], index=[2, 3, 4])
print("2個 df")
print(df1)
print(df2)

print("使用 concat 時，預設的 join 模式是 'outer'，會直接把沒有的資料用 NaN 取代")
res = pd.concat([df1, df2])  # 執行結果相等
print(res)
res = pd.concat([df1, df2], join="outer")  # 執行結果相等
print(res)

print("使用 concat 的 join ='inner'，會直接把沒有的資料刪除")
res = pd.concat([df1, df2], join="inner", ignore_index=True)
print(res)

print("------------------------------------------------------------")  # 60個

print("Merge() : merge()的默認操作是水平連接兩個DataFrame")

datas1 = {"key": ["K0", "K1", "K2"], "A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}
datas2 = {
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}
df1 = pd.DataFrame(datas1)
df2 = pd.DataFrame(datas2)
print("df1")
print(df1)
print("df2")
print(df2)

print("基於 key 把 df1 與 df2 合併")
result = pd.merge(df1, df2, on="key")
print(result)

print("------------------------------")  # 30個

print("merge 多個 key")

datas1 = {
    "k1": ["K0", "K0", "K1", "K2"],
    "k2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
}

datas2 = {
    "k1": ["K0", "K1", "K1", "K2"],
    "k2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}

df1 = pd.DataFrame(datas1)
df2 = pd.DataFrame(datas2)

print("df1")
print(df1)
print("df2")
print(df2)
print("pd.merge 1")
res = pd.merge(df1, df2, on=["k1", "k2"])  # 執行結果一樣
print(res)

print("pd.merge 2")
res = pd.merge(df1, df2, on=["k1", "k2"], how="inner")  # 執行結果一樣
print(res)

print("------------------------------")  # 30個

print("outer right left 模式")

print("outer 模式")
res = pd.merge(df1, df2, on=["k1", "k2"], how="outer")
print(res)

print("right 模式，保留右半部")
res = pd.merge(df1, df2, on=["k1", "k2"], how="right")
print(res)

print("left 模式，保留左半部")
res = pd.merge(df1, df2, on=["k1", "k2"], how="left")
print(res)

print("------------------------------")  # 30個

print("merge合併時，處理相同欄位的衝突，以suffixes區分")

datas1 = {"name": ["小黑", "小白", "小藍", "小綠"], "number": [23, 32, 31, 8]}
datas2 = {"name": ["小黑", "小白", "小藍", "小綠"], "number": ["台灣", "日本", "荷蘭", "菲律賓"]}

df1 = pd.DataFrame(datas1)
df2 = pd.DataFrame(datas2)

print("2個 df")
print(df1)
print(df2)

print("pd.merge")
df = pd.merge(df1, df2, on="name", suffixes=["_代號", "_國家"])
print(df)

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

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=["b", "c", "d", "e"], index=[2, 3, 4])

print("------------------------------------------------------------")  # 60個

print("使用 pd.merge(), by key/keys")

datas1 = {
    "key": ["K0", "K1", "K2", "K3"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
}

datas2 = {
    "key": ["K0", "K1", "K2", "K3"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}

df1 = pd.DataFrame(datas1)
df2 = pd.DataFrame(datas2)
print(df1)
print(df2)
res = pd.merge(df1, df2, on="key")
print(res)

# consider two keys
datas1 = {
    "key1": ["K0", "K0", "K1", "K2"],
    "key2": ["K0", "K1", "K0", "K1"],
    "A": ["A0", "A1", "A2", "A3"],
    "B": ["B0", "B1", "B2", "B3"],
}

datas2 = {
    "key1": ["K0", "K1", "K1", "K2"],
    "key2": ["K0", "K0", "K0", "K0"],
    "C": ["C0", "C1", "C2", "C3"],
    "D": ["D0", "D1", "D2", "D3"],
}

df1 = pd.DataFrame(datas1)
df2 = pd.DataFrame(datas2)
print(df1)
print(df2)
res = pd.merge(df1, df2, on=["key1", "key2"], how="inner")  # default for how='inner'
# how = ['left', 'right', 'outer', 'inner']
res = pd.merge(df1, df2, on=["key1", "key2"], how="left")
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
datas1 = {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}
datas2 = {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}

df1 = pd.DataFrame(datas1, index=["K0", "K1", "K2"])
df2 = pd.DataFrame(datas2, index=["K0", "K2", "K3"])
print(df1)
print(df2)
# left_index and right_index
res = pd.merge(df1, df2, left_index=True, right_index=True, how="outer")
res = pd.merge(df1, df2, left_index=True, right_index=True, how="inner")

# handle overlapping
datas1 = {"k": ["K0", "K1", "K2"], "age": [1, 2, 3]}

datas2 = {"k": ["K0", "K0", "K3"], "age": [4, 5, 6]}

boys = pd.DataFrame(datas1)
girls = pd.DataFrame(datas2)
res = pd.merge(boys, girls, on="k", suffixes=["_boy", "_girl"], how="inner")
print(res)

# join function in pandas is similar with merge. If know merge, you will understand join

print("------------------------------------------------------------")  # 60個

# 讀取[Chipotle快餐數據]資料集至df
orders = pd.read_table("http://bit.ly/chiporders")
# filename = "data/chipotle.tsv"
# orders = pd.read_csv(filename) # NG

print("檢視前幾行\n", orders.head())

# read a dataset of movie reviewers (modifying the default parameter values for read_table)
user_cols = ["user_id", "age", "gender", "occupation", "zip_code"]
users = pd.read_table("http://bit.ly/movieusers", sep="|", header=None, names=user_cols)

print("檢視前幾行\n", users.head())

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

# print("檢視前幾行\n", ufo.head())

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

# print("檢視前幾行\n", movies.head())

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

# print("檢視前幾行\n", ufo.head())

# remove a single column (axis=1 refers to columns)
ufo.drop("Colors Reported", axis=1, inplace=True)

# print("檢視前幾行\n", ufo.head())

# remove multiple columns at once
ufo.drop(["City", "State"], axis=1, inplace=True)

# print("檢視前幾行\n", ufo.head())

# remove multiple rows at once (axis=0 refers to rows)
ufo.drop([0, 1], axis=0, inplace=True)

# print("檢視前幾行\n", ufo.head())

print("------------------------------------------------------------")  # 60個

# How do I sort a pandas DataFrame or a Series? (video)

# 讀取[電影IMDb]資料集至df
# movies = pd.read_csv('http://bit.ly/imdbratings')
filename = "data/imdb_1000.csv"
movies = pd.read_csv(filename)

# print("檢視前幾行\n", movies.head())

# sort the 'title' Series in ascending order (returns a Series)
print("將 欄位 title 讀出並排序 升冪")
print("檢視前幾行")
cc = movies.title.sort_values().head()
print(cc)

# sort in descending order instead
print("將 欄位 title 讀出並排序 降冪")
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

# print("檢視前幾行\n", movies.head())

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

# print("檢視前幾行\n", drinks.head())

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

# print("檢視前幾行\n", orders.head())

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

# print("檢視前幾行\n", drinks.head())

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

# print("檢視前幾行\n", orders.head())

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
plt.show()
"""
print("------------------------------------------------------------")  # 60個
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
print("ufo 之 空資料 的個數")
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
VALUE = "VARIOUS"
ufo["Shape Reported"] = ufo["Shape Reported"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值

# confirm that the missing values were filled in
print("檢視前幾行")
cc = ufo["Shape Reported"].value_counts().head()
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pandas index

# 讀取[各國酒類消費量]資料集至df
# drinks = pd.read_csv('http://bit.ly/drinksbycountry')
filename = "data/drinks.csv"
drinks = pd.read_csv(filename)

print("檢視前幾行")
cc = drinks.head()
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
print(people)

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
cc = ufo.ffill().tail()  # ffill()拿前一個值往下填, 承上
print(cc)

# compare with "forward fill" strategy (doesn't affect the DataFrame since inplace=False)
print("檢視後幾行")
cc = ufo.ffill().tail()  # ffill()拿前一個值往下填, 承上
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

plt.show()

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

cc = movies.movie_id.nunique()
print(cc)

# Ratings

rating_cols = ["user_id", "movie_id", "rating", "timestamp"]
ratings = pd.read_table("data/u.data", sep="\t", header=None, names=rating_cols)
print("檢視前幾行")
cc = ratings.head()
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

VALUE = 0
cc = pd.to_numeric(df.col_three, errors="coerce").fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
print(cc)

VALUE = 0
df = df.apply(pd.to_numeric, errors="coerce").fillna(vlaue=VALUE)  # 將指定欄位內空資料填入指定數值
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

print("建立樞紐分析表 pivot_table")
cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="mean"
)
print(cc)

print("建立樞紐分析表 pivot_table")
cc = titanic.pivot_table(
    index="Sex", columns="Pclass", values="Survived", aggfunc="mean", margins=True
)
print(cc)

print("建立樞紐分析表 pivot_table")
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
print(cc)

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

print("建立樞紐分析表 pivot_table")
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

cc = ufo.resample("YE").State.count().tail()
print(cc)

cc = ufo.resample("ME").State.count().tail()
print(cc)

# 11. Read and write from compressed files

# df存檔
ufo.to_csv("tmp_ufo.csv")

# df存檔 並壓縮
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
df1 = pd.DataFrame({"color": ["green", "yellow", "red"], "num": [1, 2, 3]})
print(df1)

df2 = pd.DataFrame(
    {"color": ["green", "yellow", "pink", "green"], "size": ["S", "M", "L", "XL"]}
)
print(df2)

pd.merge(df1, df2, how="inner", validate="one_to_many")
print(pd)

# NG
# pd.merge(df1, df2, how='inner', validate='many_to_one')

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

print("建立樞紐分析表 pivot_table")
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
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

"""
cc = pd.merge(df1, df2, how="left", indicator=True).query("_merge == 'left_only'")
print(cc)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
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
"""
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

dates = pd.date_range("20130101", periods=6)
print(dates)

print("------------------------------------------------------------")  # 60個

""" no file
print("Pandas資料讀取與顯示")

url = "xxxx"  # 網頁上有csv的地方
df = pd.read_csv(
    "https://data.nhi.gov.tw/DataSets/DataSetResource.ashx?rId=A21030000I-D21005-001"
)

print("資料排序")

# df1 = df[['醫事機構名稱','電話','地址','備註']]
# 把幾個欄位的資料抓出來

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

columns = list("ABCDEFGHIJKLMNOPQRSTUVWXY")
df = pd.DataFrame(np.random.rand(200, 25), columns=columns)
print(df)

print("------------------------------")  # 30個
print("------------------------------")  # 30個

df = pd.read_csv("_new/scores2.csv", header=0, index_col=0)
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 取出 DataFrame 當中的元素 –df.loc[]

df[column] = np.random.choice(range(1, 101), 4)
df[column] = np.random.choice(range(1, 11), 10)
df[column] = np.random.choice(range(1, 11), 10)


datas = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨", "白龍馬", "牛魔王", "紅孩兒", "蜘蛛精", "白骨精"]


print("增加一列  TBD")
s = pd.Series({"姓名": "白龍馬", "國文": 84, "英文": 91, "數學": 82, "社會": 95, "自然": 92})


datas = np.random.randint(6, 16, (4, 5))  # 整數數字6~12 10X5


print("------------------------------------------------------------")  # 60個

print("交集合併")
order_df = pd.merge(order_df, customer_df, left_on="數學", right_on="國文", how="inner")

order_df = pd.merge(order_df, customer_df, left_on="數學", right_index=True, how="inner")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("測試完成部分")  # 60個
print("------------------------------------------------------------")  # 60個

print("df寫讀檔案")

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

df.to_csv("tmp_df_aaaa.csv", encoding="utf-8-sig")

# 11. Read and write from compressed files

# df存檔
df.to_csv("tmp_df.csv")
# df存檔 並壓縮
df.to_csv("tmp_df.csv.zip")
df.to_csv("tmp_df.csv.gz")
df.to_csv("tmp_df.csv.bz2")
df.to_csv("tmp_df.csv.xz")

# 直接讀取壓縮檔
# df_new = pd.read_csv("tmp_df.csv.gz", index_col="Time", parse_dates=["Time"])
df_new = pd.read_csv("tmp_df.csv.gz")
cc = df_new.head()
print(cc)

print("比較df是否相同")
cc = df_new.equals(df)
print(cc)

print("------------------------------------------------------------")  # 60個
print("重複資料處理")
print("------------------------------------------------------------")  # 60個

datas = [
    ["2019/10/22", "Tom", "USA", 32434],
    ["2019/10/22", "Joe", "China", 16543],
    ["2019/10/22", "Jack", "Canada", 1564],
    ["2019/10/22", "Joe", "China", 16543],
    ["2019/10/22", "Mary", "Japan", 5000],
    ["2019/10/22", "Tom", "USA", 32434],
    ["2019/10/23", "Jinie", "Brazil", 5243],
    ["2019/10/23", "Jane", "USA", 5000],
    ["2019/10/23", "John", "Canada", 2346],
    ["2019/10/23", "Joe", "Brazil", 6643],
    ["2019/10/23", "Jack", "Japan", 6465],
    ["2019/10/23", "Jinie", "Brazil", 5243],
]
columns = ["Date", "Sales Rep", "Country", "Amount"]
df = pd.DataFrame(datas, columns=columns)
print(df)


print("去重函數 drop_duplicates, 依據欄位 Country")
print("欄位 Country 有一樣的, 即刪除")
df1 = df.drop_duplicates("Country")
print("df1")
print(df1)

print("去重函數 drop_duplicates, 依據欄位 Country, keep=last")
print("欄位 Country 有一樣的, 保留後者")
df2 = df.drop_duplicates("Country", keep="last")
print(df2)

print("去重函數 drop_duplicates, 依據欄位 Country, keep=False")
print("欄位 Country 有一樣的, 皆刪除")
df3 = df.drop_duplicates("Country", keep=False)
print(df3)

print("------------------------------------------------------------")  # 60個

datas = [
    [0.7, 0.3, 0.8, 0.9],
    [0.8, 0.6, 0.4, 0.8],
    [0.7, 0.3, 0.8, 0.9],
    [0.8, 0.3, 0.5, 0.2],
    [0.9, 0.3, 0.7, 0.3],
    [0.7, 0.3, 0.8, 0.9],
]
columns = ["A", "B", "C", "D"]
df = pd.DataFrame(datas, columns=columns)
print(df)

print("檢查df內是否有重複資料, 整列都重複的")
print(df.duplicated())

print("去重函數 drop_duplicates, 整列都重複的, 刪除之")
df1 = df.drop_duplicates()
print(df1)

print("檢查df內是否有重複資料, 依據欄位 B")
print(df.duplicated("B"))

print("去重函數 drop_duplicates, 依據欄位 B")
print("欄位 B 有一樣的, 即刪除")
df1 = df.drop_duplicates("B")
print(df1)

print("去重函數 drop_duplicates, 依據欄位 B, keep=last")
print("欄位 B 有一樣的, 保留後者")
df2 = df.drop_duplicates("B", keep="last")
print(df2)

print("去重函數 drop_duplicates, 依據欄位 B, keep=False")
print("欄位 B 有一樣的, 皆刪除")
df3 = df.drop_duplicates("B", keep=False)
print(df3)

print("------------------------------------------------------------")  # 60個

print("有重複資料之df")

datas = [
    [92, 81, 92, 81, 92, 81],  # 國文
    [89, 79, 89, 82, 72, 82],  # 英文
    [71, 92, 71, 89, 95, 89],  # 數學
    [88, 89, 88, 98, 77, 98],  # 社會
    [95, 74, 95, 89, 85, 89],  # 自然
]
columns = ["國文", "英文", "數學", "社會", "自然"]
index = ["唐三藏", "孫悟空", "唐三藏", "豬八戒", "沙悟淨", "豬八戒"]
df = pd.DataFrame(np.array(datas).T, columns=columns, index=index)
print(df)

print("檢查df內是否有重複資料")
print(df.duplicated())

print("去重後的df")
print(df)

print("去重後的df")
print(df)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("字典 轉 df")

datas = {
    "國文": [92, 81, 81, 92],
    "英文": [89, 79, 82, 72],
    "數學": [71, 92, 89, 95],
    "社會": [88, 89, 98, 77],
    "自然": ["95", "74", "89", "85"],  # 字串
}

index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df = pd.DataFrame(datas, index=index)
print(df)

print("將字串轉成數字")
df["自然"] = df["自然"].astype("int64")
print(df)

print("------------------------------------------------------------")  # 60個

print("字典 轉 df")

datas = {
    "國文": [92, 81, 81, 92],
    "英文": [89, 79, 82, 72],
    "數學": [71, 92, 89, 95],
}
df = pd.DataFrame(datas)
print(df)

index = ["唐三藏", "孫悟空", "牛魔王", "沙悟淨"]
df.columns = ["國文", "英文", "數學"]
index[2] = "豬八戒"  # 修改 索引
df.index = index
print(df)

print("------------------------------------------------------------")  # 60個

print("修改 索引")
df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("重新設定索引index")
index = ["唐三藏", "孫悟空", "豬八戒", "沙悟淨"]
df.index = index
print(df)

print("重新設定索引index")
index = ["Tang", "Monkey", "Pig", "Sand"]
df.index = index
print(df)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("過濾資料與排序")
print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("將 df 的 數學 成績讀出並排序")
cc = df.數學.sort_values()
print(cc)

print("印出 數學 > 90 的資料")
df1 = df[df.數學 > 90]
print(df1)

print("依照 數學 排序 降冪")
df2 = df.sort_values("數學", ascending=False)
print(df2)

print("依照 數學 排序 升冪")
df3 = df.sort_values("數學", ascending=True)
print(df3)

print("依照 數學 排序 預設為 升冪")
df4 = df.sort_values("數學")
print(df4)

print("依照 國文/英文 排序 升冪/降冪")
df5 = df.sort_values(["國文", "英文"], ascending=[True, False])
print(df5)

print("排序, 依 數學 欄, 預設為上升")
print(df.sort_values(by="數學"))  # 預設上升
print(df.sort_values(by="數學", ascending=True))  # 上升
print(df.sort_values(by="數學", ascending=False))  # 下降
df = df.sort_values(by=["國文", "英文"], ascending=True)
print(df)

print("排序 axis=1, 依column欄名排序, 橫向, 下降")
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(axis=0))

print("------------------------------------------------------------")  # 60個

df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("------------------------------------------------------------")  # 60個

""" data2/test3.csv
性別,尺寸,價格
male,XL,800
female,M,400
not specified,XXL,300
male,L,500
female,S,700
female,XS,850
"""

print("df內容的資料對應")

df = pd.read_csv("data2/test3.csv")
print(df)

size_mapping = {"XXL": 666, "XL": 555, "L": 444, "M": 333, "S": 222, "XS": 111}
df["尺寸"] = df["尺寸"].map(size_mapping)
print(df)

print("------------------------------------------------------------")  # 60個

print("測試 cumsum()")
df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

df = df.cumsum()  # 依欄位, 逐列累加
print(df)

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

print("簡單df操作")

df = make_data_frame()
print(df)

print("孫悟空的成績(df.values[1])：")
print(df.values[1])
print("孫悟空的英文成績(df.values[1][2])：")
print(df.values[1][2])

print("------------------------------------------------------------")  # 60個

print("空資料的處理 填值 fillna 填補 NaN 值")

df = pd.DataFrame(np.random.rand(8, 4))
print(df)
#       R  C
df.iloc[1, 0] = np.nan
df.iloc[2, 2] = np.nan
df.iloc[6, 1] = np.nan
df.iloc[5:, 3] = np.nan
print(df)

print("------------------------------")  # 30個

VALUE = 0
df_fill = df.fillna(value=VALUE)  # 將df內空資料填入指定數值
print(df_fill)

print("------------------------------")  # 30個

df_fill_2 = df.ffill()  # ffill()拿前一個值往下填, 承上
print(df_fill_2)

print("------------------------------")  # 30個

df_fill_3 = df.bfill()  # bfill()拿下一個值往上填, 承下
print(df_fill_3)

print("------------------------------------------------------------")  # 60個


print("刪除 df 的 欄位 或 索引 – drop() + 缺失資料處理")

""" data/data_with_NaN.csv
     A    B    C    D
0  0.5  0.9  0.4  NaN
1  0.8  0.6  NaN  NaN
2  0.7  0.3  0.8  0.9
3  0.8  0.3  NaN  0.2
4  0.9  NaN  0.7  0.3
5  0.2  0.7  0.6  NaN
"""
df = pd.read_csv("data/data_with_NaN.csv")

# df 轉 html
# df.to_html("test_csv2html.html")

print("df 原始資料")
print(df)

# 刪除所有 NaN 的記錄
df1 = df.dropna()
print("df1 有任何NaN的列 刪除")
print(df1)

df2 = df.dropna(how="any")
print("df2 有任何NaN的列 刪除")
print(df2)

df3 = df.dropna(how="all")
print("df3 全部都NaN的列 刪除")
print(df3)

df4 = df.dropna(subset=["B", "C"])
print("df4 B C 欄有NaN的列 刪除")
print(df4)

df5 = pd.isnull(df)
print("df5 建立布林遮罩")
print(df5)

print("空資料 :")
print(pd.isnull(df))

VALUE = 1
df6 = df.fillna(value=VALUE)  # 將df內空資料填入指定數值
print(df6)

print("df 欄位B 的 缺失資料 補值 補上原先欄位B 的 平均數")
VALUE = df["B"].mean()
df["B"] = df["B"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
print(df)

print("df 欄位C 的 缺失資料 補值 補上原先欄位C 的 中位數")
VALUE = df["C"].median()
df["C"] = df["C"].fillna(value=VALUE)  # 將指定欄位內空資料填入指定數值
print(df)

print("------------------------------------------------------------")  # 60個

print("測試 iloc(R, C)")
df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

print("顯示第0列, 即索引0, 唐三藏的成績")
cc = df.iloc[0]
print(cc)

print("用iloc取得每一個欄位的資料")
#             R  C
print(df.iloc[1, 0])
print(df.iloc[2, 3])
print(df.iloc[2:, 3])
print(df.iloc[2:5, 0:2])

cc = df.iloc[0, [0, 4]]
print(cc)
cc = df.iloc[[0, 1], [2, 3]]
print(cc)
cc = df.iloc[0:3, 2:5]
print(cc)
cc = df.iloc[2, :]
print(cc)
cc = df.iloc[:2, 2:5]
print(cc)
cc = df.iloc[1:, 2:5]
print(cc)
cc = df.iloc[[1, 2, 3], [0, 2]]
print(cc)

print("社會(第3欄)")
print(df.iloc[0:12, 3])

print("社會(部分)")
print(df.iloc[[0, 1, 3], 3])

print("df.iloc[1, :] ->")
print(df.iloc[1, :])

"""
#       R  C
df.iloc[1, 0] = np.nan
df.iloc[2, 2] = np.nan
df.iloc[6, 1] = np.nan
df.iloc[5:, 3] = np.nan
print(df)
"""

print("------------------------------------------------------------")  # 60個

print("測試 loc(R, C)")
df = make_data_frame_from_dict()  # 字典 轉 df
print(df)

# 比較loc(彈性較大)和iloc顯示表格內容
# loc使用行索引標籤(column index label)和列索引標籤(row index label)
cc = df.loc[1]["姓名"]
print(cc)

df8 = df.loc[[1, 2], ["國文", "英文"]]
print(df8)

print("數學成績")
print(df.loc[:, "數學"])

print('df.loc["孫悟空":"豬八戒", "數學":"社會"] ->')
print(df.loc["孫悟空":"豬八戒", "數學":"社會"])
print('df.loc[:沙悟淨, "數學":"社會"] ->')
print(df.loc[:"沙悟淨", "數學":"社會"])
print('df.loc["孫悟空":, "數學":"社會"] ->')
print(df.loc["孫悟空":, "數學":"社會"])

print("國文 > 75 且 英文 > 75 者")
df3 = df.loc[df["國文"] >= 75][df["英文"] >= 75]
print(df3)

print("看 索引 1~3, 數學 社會 成績")
df4 = df.loc[range(1, 4), ["數學", "社會"]]
print(df4)

print("顯示")
# print(df.loc[3, 0])

print("------------------------------------------------------------")  # 60個

print("建立df, 字典 轉 df")

datas = {
    "國文": {"唐三藏": 65, "孫悟空": 90, "豬八戒": 81, "沙悟淨": 79},
    "英文": {"唐三藏": 92, "孫悟空": 72, "豬八戒": 85, "沙悟淨": 53},
    "數學": {"唐三藏": 78, "孫悟空": 76, "豬八戒": 91, "沙悟淨": 47},
    "社會": {"唐三藏": 70, "孫悟空": 56, "豬八戒": 94, "沙悟淨": 80},
    "自然": {"唐三藏": 83, "孫悟空": 93, "豬八戒": 89, "沙悟淨": 94},
}
df = pd.DataFrame(datas)
print(df)

print("欄位 自然 的資料")
print(df["自然"])
print("欄位 國文 數學 自然 的資料")
print(df[["國文", "數學", "自然"]])
print("欄位 國文 >= 80 的資料")
print(df[df["國文"] >= 80])

print("索引 1 的資料(孫悟空)")
print(df.values[1])
print("索引 1 欄位 2 的資料(孫悟空 數學)")
print(df.values[1][2])

print("看 孫悟空 數學 的資料")
print(df.loc["孫悟空", "數學"])

print("看 唐三藏 國文 社會 的資料")
print(df.loc["唐三藏", ["國文", "社會"]])

print("看 唐三藏 和 豬八戒 國文 和 社會 的資料")
print(df.loc[["唐三藏", "豬八戒"], ["國文", "社會"]])

print("看 唐三藏 到 豬八戒 國文 到 數學 的資料")
print(df.loc["唐三藏":"豬八戒", "國文":"數學"])

print("看 豬八戒 的 所有 資料")
print(df.loc["豬八戒", :])

print("看 從頭 到 豬八戒 的 數學 到 社會 的資料")
print(df.loc[:"豬八戒", "數學":"社會"])

print("看 豬八戒 到 末尾 的 數學 到 社會 的資料")
print(df.loc["豬八戒":, "數學":"社會"])

print("------------------------------------------------------------")  # 60個


"""
color="DarkBlue"
color="LightGreen"

"""


"""

import pandas as pd
df = pd.read_csv('Iris.csv')
print(df.head())
print('將Id整欄刪除')
df = df.drop('Id', axis = 1)

print(df.head())





"""


"""

pandas主要之資料型態:
1. Series	一維資料結構
2. DataFrame	二維資料結構



pandas 可以說像是 Python 中的 Excel

不只 CSV 檔, 很多資料檔案, 像 Excel 檔都很容易在 pandas 完成。使用法是這樣:

df2 = pd.read_excel('filename.xls', 'sheetname')
其中 sheetname 那裡要放工作表的名稱, 如果是中文的最好改成英文。

Pandas 有兩個基本資料結構:
1. DataFrame: 可以想成一個表格。
2. Series: 表格的某一列、某一行, 基本上就是我們以前的 list 或 array

一個 DataFrame, 我們有 index (列的名稱), columns (行的名稱)。
series 大概就是一個 list, 一個 array。其實更精準的說, 其實是一個有 "index" 的 array。


"""


"""

use_pivot 看encoding
import pandas as pd
df = pd.read_csv("..\data\ordersList.csv",encoding="utf-8",header = 0)
print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True, aggfunc="sum"))

print(df.pivot_table(index="品名",columns="客戶名稱", values="金額", fill_value=0, margins=True ))

"""


# df = pd.DataFrame(np.random.randn(3,3), columns=list("甲乙丙"))
# print(df)

# df = pd.DataFrame(np.random.randn(5, 3), index=list(range(1,6)), columns=list("ABC"))

#                    A  B  C  D  E
df = pd.DataFrame(
    [
        [65, 92, 78, 83, 70],
        [90, 72, 76, 93, 56],
        [81, 85, 91, 89, 77],
        [79, 53, 47, 94, 80],
    ],
    index=list(range(1, 5)),
    columns=list("ABCDE"),
)

print("原資料 :\n", df)

print("常用統計數據")
print(df.describe())

print("相關係數")
print(df.corr())

print("df轉csv")
df.to_csv("tmp_df_data1.csv")

print("data_frame 畫點圖")

x = df.A.values
y = df.B.values

"""
loc 的用法
df.loc[列的範圍, 行的範圍]

df.loc[2:3, "B":"C"]


列或行只要一個
df.loc[2, "B"]

df.loc[2, "B"]=-1
"""

print("------------------------------------------------------------")  # 60個

mu = 170
sigma = 10
N = 500
datas = np.random.normal(mu, sigma, N)
df = pd.DataFrame(datas)

print("------------------------------------------------------------")  # 60個

columns = ["姓名", "班級"]
data = [
    ["林大和", "一年甲班"],
    ["張小明", "一年乙班"],
    ["林美麗", "一年乙班"],
    ["鄭中林", "二年甲班"],
    ["林品朋", "二年甲班"],
    ["陳明朋", "二年乙班"],
]
df = pd.DataFrame(data, columns=columns)
# print(df)

df1 = df[df["班級"] == "二年甲班"]
# print(df1)
df2 = df[df["姓名"].str.contains("林")]
# print(df2)
df3 = df[(df["姓名"].str.contains("林")) & (df["班級"].str.contains("一年"))]
print(df3)

print("------------------------------------------------------------")  # 60個

# 索引
df = pd.DataFrame({"a": [1, 3], "b": [2, 4]}, index=["line1", "line2"])
print(df.index)  # 顯示行索引
print(df.columns)  # 顯示列索引

print("------------------------------------------------------------")  # 60個

from datetime import datetime

# Pandas日期時間處理
# 時間點TimeStamp

t = pd.to_datetime("2019-03-01 00:00:00")  # 從字符串轉換
print(type(t), t)
t = pd.to_datetime(datetime.now())  # 從datetime格式轉換
print(type(t), t)

# 時間間隔
t1 = pd.to_datetime("2019-03-01 00:00:00")
t2 = pd.to_datetime(datetime.now())
delta = t2 - t1  # 通過TimeStamp相減獲取
print(type(delta), delta, delta.days, delta.seconds)

delta = pd.Timedelta(days=27)  # 構造時間間隔爲27天
print(t2 + delta)

# 時間段Period
t = pd.to_datetime(datetime.now())
p = pd.Period(t, freq="H")
print(p, p.start_time, p.end_time)  # 顯示時間段起止時間

# 批量轉換
arr = ["2019-03-01", "2019-03-02", "2019-03-03"]
df = pd.DataFrame({"d": arr})
df["d"] = pd.to_datetime(df["d"])
print(df)

print("------------------------------------------------------------")  # 60個

# 時間序列操作
# 時間日期類型索引
df.index = pd.to_datetime(df["d"])  # 本例中使用了上例中構造的df[‘d’]
print(df.index)

df = pd.DataFrame()
df["date"] = pd.date_range(start="2017-12-30", end="2019-01-05", freq="d")  # 創建時間數據
df["val"] = df["date"].apply(lambda x: x.weekday())  # 計算該日是星期幾
df.set_index("date", inplace=True)  # 設置時間索引
print(df.head(3))  # 顯示前三條

# 時間段類型索引
df_period = df.to_period(freq="M")  # 按月創建時間段
print(type(df_period.index))  # 查看類型
print(len(df_period))  # 查看記錄個數，與原記錄個數一致
print(df_period.head(3))

print(df_period.index[0].start_time, df_period.index[0].end_time)
print(df_period.index[1].start_time, df_period.index[1].end_time)
print(df.index.is_unique, df_period.index.is_unique)

df_dt = df_period.to_timestamp()
print(df_dt.head(3))
print(type(df_dt.index))

print("------------------------------------------------------------")  # 60個
""" no df
# 篩選和切分
print(df['2019'])  # 篩選2019全年數據
print(df['2019-01'])  #  篩選2019年一月全月數據
print(df['2018':'2019'].head()) # 篩選2018年初到2019年底的所有數據
print(df['2018-12-31':].head()) # 篩選2018-12-31及之後的數據

# 重採樣
tmp = df.resample('w').sum() # 使用疊加方式按周重採樣
print(tmp.head(3))

tmp = df.resample('M').ohlc() # 使用用ohlc方式按月降採樣
print(tmp.head(3))

tmp = df.resample('M').sum().to_period('M') # 按月降採樣，同時將時間變爲時間段
print(tmp.head(3))

df1 = pd.DataFrame({'val':[8,7,6]})
df1.index = pd.to_datetime(['2019-03-01','2019-03-15','2019-03-31']) # 僅含三條數據
df2 = df1.resample('D').interpolate() # 用插值方式升採樣
print(len(df2))
print(df2.head(3))

df3 = df1.asfreq('D')
print(df3.head(3))

# 偏移
df['prev'] = df['val'].shift() # 取前一條數據的val值作爲當前記錄中prev字段的值
print(df.head(3))

# 計算滑動窗口
df['sw'] = df['val'].rolling(window=3).mean() # 計算窗口中數據的均值
print(df.head(3))

df['emw_3'] = df['val'].ewm(span=3).mean()
df['emw_7'] = df['val'].ewm(span=7).mean()
df['rolling'] = df['val'].rolling(7).mean()
"""
print("------------------------------------------------------------")  # 60個

# 時區轉換

import pytz

print("時區個數 :", len(pytz.common_timezones))
print("前3個 :", pytz.common_timezones[:3])

import datetime

t = datetime.datetime.now()
print(t)

utc_dt = pytz.utc.localize(t)
print(utc_dt)

from pytz import timezone

tz = timezone("Asia/Shanghai")  # 將時區設爲上海
print(utc_dt.astimezone(tz))  # 轉換時區

df = pd.DataFrame()
df["date"] = pd.date_range(start="2018-12-31", end="2019-01-01", freq="d")
df.set_index("date", inplace=True)  # 設置時間索引
print(df.index)

df.index = df.index.tz_localize("UTC")
print(df.index.values, df.index)

df.index = df.index.tz_convert("Asia/Shanghai")
print(df.index.values)
print(df.index)

print("------------------------------------------------------------")  # 60個

# 數據重排
# 數據錶轉置
df = pd.DataFrame({"a": [1, 2], "b": [3, 4]}, index=["l1", "l2"])
print(df)
print(df.T)

# 行轉列和列轉行
df1 = df.stack()  # 列轉行
print(df1)

print(df1.unstack())  # 將內層行索引轉爲列索引
print(df1.unstack(level=0))  # 將外層行索引轉爲列索引

# 透視轉換
df = pd.DataFrame(
    {
        "時間": ["期中", "期末", "期中", "期末"],
        "學科": ["語文", "語文", "數學", "數學"],
        "分數": [89, 75, 90, 95],
    }
)
df1 = df.pivot(index="時間", columns="學科", values="分數")
print(df, df1)

print("------------------------------------------------------------")  # 60個

print("基本類型轉換")

dic = {
    "string": ["dog", "snake", "cat", "dog", "monkey", "elephant"],
    "integer": [2000, 2000, 2001, 2002, 2003, np.nan],
    "float": [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
    "dtime": [
        "2018-01-01",
        "2018/01/02",
        "2018-01-03",
        "2018-01-04",
        "2018-01-05",
        np.nan,
    ],
    "mix": [1, 1, 0, "+", 0, 1],
    "classify": ["A", "B", "A", "B", "A", "A"],
}
data = pd.DataFrame(dic)
print(data.dtypes)
""" NG
data['dtime'] = pd.to_datetime(data['dtime'], infer_datetime_format=True)
data['mix']=pd.to_numeric(data['mix'],errors='coerce')
data['classify']=pd.Categorical(data['classify'])
data['float']=data['float'].astype(np.float32)
print(data.dtypes)
"""
print("------------------------------------------------------------")  # 60個

print("缺失值處理")

dic = {
    "state": ["Ohio", "Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
    "year": [2000, 2000, 2001, 2002, 2003, 3456],
    "score": [1.5, 1.5, 1.7, np.nan, np.nan, 8.3],
    "desc": [np.nan, np.nan, np.nan, np.nan, np.nan, 3],
    "val1": [1, 1, 0, "+", 0, 1],
}
data = pd.DataFrame(dic)

print(data["desc"].nunique())  # 不同取值個數
print(data["desc"].unique())  # 不同取值列表
print(data["year"].value_counts())  # 不同取值出現次數

print(data["desc"].isnull())  # 是否缺失
print(data["desc"].isnull().any())  # 是否含有任意缺失
print(data["desc"].isnull().all())  # 是否全部缺失
print(data["desc"].isnull().sum(), len(data))  # 空值個數與記錄個數
print(data.dropna(axis=1, how="all"))
print(data["score"].fillna(data["score"].mean()))
print(data["score"].fillna(method="ffill", limit=1))

print(data.interpolate(mdthod="polynomial", order=2))  # 二次多項式插值
print(data.interpolate(mdthod="spline", order=3))  # 三次樣條插值

print("異常值處理")

print(data.query("year<2050"))
print(data[data["year"] < 2050])

data["val1"] = data["val1"].apply(lambda x: 1 if x == "+" else x)

print("去重處理")

print(data.drop_duplicates(keep="last"))
print(data.drop_duplicates(keep="last", subset="year"))

print("------------------------------------------------------------")  # 60個

print("merge方法")

df1 = pd.DataFrame({"id": [1, 2, 3], "val1": [2, 4, 6]})
df2 = pd.DataFrame({"id": [3, 2, 2], "val2": [9, 6, 5]})
print(pd.merge(df1, df2, how="left"))

print("------------------------------------------------------------")  # 60個

print("concat方法")

df1 = pd.DataFrame({"id": [1, 2, 3], "val1": [2, 4, 6]})
df2 = pd.DataFrame({"id": [3, 2, 2], "val2": [9, 6, 5]})
print(pd.concat([df1, df2]))
print(pd.concat([df1, df2], axis=1))

print("------------------------------------------------------------")  # 60個

print("數值型特徵")

dic = {"height": [1.6, 1.7, 1.8], "weight": [60, 70, 90]}
data = pd.DataFrame(dic)
data["bmi"] = data["weight"] / (data["height"] ** 2)
print(data)
data["overweight"] = data["bmi"] > 25
print(data)
data["overweight"] = data["overweight"].map({True: "Yes", False: "No"})
print(data)

print("------------------------------------------------------------")  # 60個

print("類型特徵")

dic = {"string": ["第一組", "第二組", "第二組"]}
data = pd.DataFrame(dic)
print(pd.factorize(data.string))  # 轉換成數值型編碼

data["num"] = pd.factorize(data["string"])[0]
df = pd.get_dummies(data["string"], prefix="組別")  # 轉換成onehot類型編碼
new_data = pd.concat([data, df], axis=1)
print(new_data)

print("------------------------------------------------------------")  # 60個

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=0, high=2, size=num_throws)
    probability_of_throws = throws.sum() / num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲": results})

df.plot(color="b")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個

results = []
for num_throws in range(1, 10001):
    throws = np.random.randint(low=1, high=7, size=num_throws)
    mask = throws == 1
    probability_of_throws = len(throws[mask]) / num_throws
    results.append(probability_of_throws)

df = pd.DataFrame({"投擲": results})

df.plot(color="r")
plt.title("大數法則(Law of Large Numbers)")
plt.xlabel("投擲次數")
plt.ylabel("平均機率")
plt.show()

print("------------------------------------------------------------")  # 60個


dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=1)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=10)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

dice = [1, 2, 3, 4, 5, 6]
sample_means = []
for x in range(100):
    sample = np.random.choice(a=dice, size=100)
    sample_means.append(sample.mean())

df = pd.DataFrame(sample_means)
df.plot(kind="density")
plt.show()

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"] * 352) + (["男"] * 315) + (["女"] * 217) + (["女"] * 331))
voter_favorite = np.array(
    (["喜歡"] * 352) + (["不喜歡"] * 315) + (["喜歡"] * 217) + (["不喜歡"] * 331)
)
voters = pd.DataFrame({"gender": voter_gender, "favorite": voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)

print("------------------------------------------------------------")  # 60個

voter_gender = np.array((["男"] * 352) + (["男"] * 315) + (["女"] * 217) + (["女"] * 331))
voter_favorite = np.array(
    (["喜歡"] * 352) + (["不喜歡"] * 315) + (["喜歡"] * 217) + (["不喜歡"] * 331)
)
voters = pd.DataFrame({"gender": voter_gender, "favorite": voter_favorite})
voter_tab = pd.crosstab(voters.gender, voters.favorite, margins=True)
voter_tab.columns = ["喜歡", "不喜歡", "小計"]
voter_tab.index = ["男", "女", "小計"]
observed = voter_tab.iloc[0:3, 0:3]
print(observed)
print("---------------------------")
expected = np.outer(voter_tab["小計"][0:2], voter_tab.loc["小計"][0:2]) / 1215
expected = pd.DataFrame(expected)
expected.columns = ["喜歡", "不喜歡"]
expected.index = ["男", "女"]
print(expected)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
