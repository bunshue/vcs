"""
使用pandas讀取csv檔, 讀成 DataFrame 格式

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

# 載入資料與定義資料
filename = "data/animals.csv"

df = pd.read_csv(filename)
print(df)
print("--------")
df = pd.read_csv(filename, header=0, index_col=0)
print(df)
print("--------")
df = pd.read_csv(filename, header=0, index_col=1)
print(df)
print("--------")
df = pd.read_csv(filename, header=1, index_col=0)
print(df)
print("--------")
df = pd.read_csv(filename, header=1, index_col=1)
print(df)
print("--------")

"""
print('資料結構訊息', df.info())
print('資料shape :', df.shape)
print('資料內容\n', df)
print('資料head\n', df.head())
print(type(df))
print(df)
print(df.shape)
"""

print("------------------------------------------------------------")  # 60個

print("有缺資料之dataframe")

filename = "data/missing_data.csv"

df = pd.read_csv(filename)

print("原資料\n", df, "\n")
print("資料結構訊息", df.info(), "\n")

df1 = df.dropna()
print("清除NA\n", df1, "\n")

df2 = df.dropna(how="any")
print(df2)
print()

df3 = df.dropna(subset=["B", "C"])
print(df3)
print()

df4 = df.fillna(value=1)
print(df4)
print()

df["B"] = df["B"].fillna(df["B"].mean())
print(df)
print()

print("------------------------------------------------------------")  # 60個

filename = "data/duplicated_data.csv"
df = pd.read_csv(filename)

print("原資料\n", df, "\n")

print(df.duplicated())
print()

print(df.duplicated("B"))
print()

df1 = df.drop_duplicates()
print(df1)
print()

df2 = df.drop_duplicates("B")
print(df2)
print()

df3 = df.drop_duplicates("B", keep=False)
print(df3)
print()

print("------------------------------------------------------------")  # 60個

filename = "data/labelencoder_data.csv"
df = pd.read_csv(filename)

print("原資料\n", df, "\n")

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
df["Gender"] = label_encoder.fit_transform(df["Gender"])
print(df)

print("------------------------------------------------------------")  # 60個

# 載入資料集

# 鐵達尼號資料集是一個CSV檔案：titanic_data.csv，我們可以建立DataFrame物件來載入資料集，如下所示：

"""
資料前處理

在檢視資料集的描述資料後，我們知道目前需要處理的工作，如下所示：

PassengerId欄位是否是流水號，如果是，我們可以將此欄位改為索引欄位。
Sex欄位需要處理分類資料轉換成數值的0和1（1是女；0是男）。
PClass欄位需要處理分類資料轉換成數值的1、2和3（1是1st；2是2nd；3是3rd）。
Age欄位有很多遺漏值，我們準備使用Age欄位的平均值來補值。
"""
filename = "data/titanic_data.csv"
titanic = pd.read_csv(filename)

print("資料shape")
print(titanic.shape)
print()

print("資料")
print(titanic)
print()

print("資料.head()")
print(titanic.head())
print()

print("size")
print(np.unique(titanic["PassengerId"].values).size)
print()

titanic.set_index(["PassengerId"], inplace=True)
print(titanic.head())
print()

titanic["SexCode"] = np.where(titanic["Sex"] == "female", 1, 0)
print(titanic.head())
print()

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()
titanic["PClass"] = label_encoder.fit_transform(titanic["PClass"])
print(titanic.head())

print("isnull().sum()")
print(titanic.isnull().sum())

print("age.isnull()")
print(sum(titanic["Age"].isnull()))

avg_age = titanic["Age"].mean()
print("average age =", avg_age)

titanic["Age"].fillna(avg_age, inplace=True)
print(sum(titanic["Age"].isnull()))

print("1111")
print(titanic["Sex"].groupby(titanic["Sex"]).size())

print("2222")
print(titanic.groupby("Sex")["Age"].mean())

print("------------------------------------------------------------")  # 60個

# 探索性資料分析

print("3333")
titanic["Died"] = np.where(titanic["Survived"] == 0, 1, 0)
print(titanic.head())

titanic["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 0]
df["Age"].plot(kind="hist", bins=15)
df = titanic[titanic.Survived == 1]
df["Age"].plot(kind="hist", bins=15)

plt.show()

print("------------------------------------------------------------")  # 60個

fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])

df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])

plt.show()

print("------------------------------------------------------------")  # 60個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

plt.show()

print("------------------------------------------------------------")  # 60個

df = titanic.drop("Died", axis=1)
print("係數矩陣 :", df.corr())

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "data/iris_sample.csv"

iris = pd.read_csv(filename)
"""
共有五個欄位：
1. 花萼長度(Sepal Length)：計算單位是公分。
2. 花萼寬度(Sepal Width)：計算單位是公分。
3. 花瓣長度(Petal Length) ：計算單位是公分。
4. 花瓣寬度(Petal Width)：計算單位是公分。
5. 類別(Class)：可分為Setosa，Versicolor和Virginica三個品種。
"""

print("資料")
print(iris)

print("資料shape")
print(iris.shape)

print("資料.type")
print(type(iris))

print("資料.head()")
print(iris.head())

print("size")
print(np.unique(iris["花萼長度"].values).size)
print()

cccc = np.where(iris["類別"] == "versicolor", 1, 0)
print("抓出versicolor :", cccc)
print()

color = ["r", "y", "b"]
species = ["Setosa", "Versicolour", "Virginica"]
Setosa = []
Versicolour = []
Virginica = []

print(type(iris))
print(len(iris))
print(iris.shape)

# sepal_length,sepal_width,petal_length,petal_width,species
print(iris["花萼長度"])

print(len(iris["花萼長度"]))

print(iris["花萼長度"][0])

# 不同种类保存为不同的列表
for i in range(len(iris)):
    if iris["類別"][i] == "setosa":
        Setosa.append(1)
        Versicolour.append(0)
        Virginica.append(0)
    elif iris["類別"][i] == "versicolor":
        Setosa.append(0)
        Versicolour.append(1)
        Virginica.append(0)
    elif iris["類別"][i] == "virginica":
        Setosa.append(0)
        Versicolour.append(0)
        Virginica.append(1)

print("Setosa :", Setosa)
print("Versicolour :", Versicolour)
print("Virginica :", Virginica)

print("------------------------------------------------------------")  # 60個

dists = {"name": ["中正區", "板橋區", "桃園區", "北屯區", 
                   "安南區", "三民區", "大安區", "永和區", 
                   "八德區", "前鎮區", "鳳山區", 
                   "信義區", "新店區"],
         "population": [159598, 551452, 441287, 275207,
                        192327, 343203, 309835, 222531,
                        198473, 189623, 359125, 
                        225561, 302070],
         "city": ["台北市", "新北市", "桃園市", "台中市",
                  "台南市", "高雄市", "台北市", "新北市",
                  "桃園市", "高雄市", "高雄市",
                  "台北市", "新北市"]}
df = pd.DataFrame(dists) 

df.to_csv("tmp_dists2.csv", index=False, encoding="utf8")
df.to_json("tmp_dists.json")

print("------------------------------------------------------------")  # 60個

# 匯入CSV格式的檔案
df = pd.read_csv("tmp_dists2.csv", encoding="utf8")
print(df)
df.to_html("tmp8-2-2a-01.html")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print(df.head())
df.head().to_html("tmp8-2-3-01.html")

print("------------------------------")  # 30個

print(df.head(3))
df.head(3).to_html("tmp8-2-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print(df.tail())
df.tail().to_html("tmp8-2-3a-01.html")

print("------------------------------")  # 30個

print(df.tail(3)) 
df.tail(3).to_html("tmp8-2-3a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.head(4)) 
df.head(4).to_html("tmp8-2-3b.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df.columns = ["區", "人口", "直轄市"]
print(df.index)

print("------------------------------")  # 30個

print(df.columns)

print("------------------------------")  # 30個

print(df.values)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

print("資料數= ", len(df))

print("------------------------------")  # 30個

print("形狀= ", df.shape)

print("------------------------------")  # 30個

df.info()

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

for index, row in df.iterrows() :
    print(index, row["city"], row["name"], row["population"])

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df2 = df.set_index("city")
print(df2.head())
df2.head().to_html("tmp8-2-5-01.html")

print("------------------------------")  # 30個

df3 = df2.reset_index()
print(df3.head())
df3.head().to_html("tmp8-2-5-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df2 = df.set_index(["city", "name"])
df2.sort_index(ascending=False, inplace=True)
print(df2)
df2.to_html("tmp8-2-5a.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df["population"].head(3))

print("------------------------------")  # 30個

print(df[["city","name"]].head(3))
df[["city","name"]].head(3).to_html("tmp8-3-1.html")

print("------------------------------")  # 30個

print(df.population.head(3))   # 使用屬性方式

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[0:3])                # 不含 3
df[0:3].to_html("tmp8-3-1a-01.html")

print("------------------------------")  # 30個

print(df["sixth":"eleventh"]) # 含 "eleventh"
df["sixth":"eleventh"].to_html("tmp8-3-1a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))

print("------------------------------")  # 30個

print(df.loc[:,["name","population"]].head(3))
df.loc[:,["name","population"]].head(3).to_html("tmp8-3-1b-01.html")

print("------------------------------")  # 30個

print(df.loc["third":"fifth", ["name","population"]])

print("------------------------------")  # 30個

print(df.loc["third", ["name","population"]])
df.loc["third":"fifth", ["name","population"]].to_html("tmp8-3-1b-02.html")

print("------------------------------")  # 30個

# 取得單一純量值
print(df.loc[ordinals[0], "name"])
print(type(df.loc[ordinals[0],"name"]))

print("------------------------------")  # 30個

print(df.loc["first", "population"])
print(type(df.loc["first", "population"]))

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.iloc[3])          # 第 4 筆

print("------------------------------")  # 30個

print(df.iloc[3:5, 1:3])   # 切割
df.iloc[3:5, 1:3].to_html("tmp8-3-1c-01.html")

print("------------------------------")  # 30個

print(df.iloc[1:3, :])     # 切割列
df.iloc[1:3, :].to_html("tmp8-3-1c-02.html")

print("------------------------------")  # 30個

print(df.iloc[:, 1:3])     # 切割欄
df.iloc[:, 1:3].to_html("tmp8-3-1c-03.html")

print("------------------------------")  # 30個

print(df.iloc[[1,2,4], [0,2]])   # 索引清單
df.iloc[[1,2,4], [0,2]].to_html("tmp8-3-1c-04.html")

print("------------------------------")  # 30個

# 取得單一純量值
print(df.iloc[1,1])
print(df.iat[1,1])

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[df.population > 350000])
df[df.population > 350000].to_html("tmp8-3-2-01.html")

print("------------------------------")  # 30個

print(df[df["city"].isin(["台北市","高雄市"])])
df[df["city"].isin(["台北市","高雄市"])].to_html("tmp8-3-2-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df[(df.population > 350000) & (df.population < 500000)])
df[(df.population > 350000) & (df.population < 500000)].to_html("tmp8-3-2a-01.html")

print("------------------------------")  # 30個

print(df[df["city"].str.startswith("台")])
df[df["city"].str.startswith("台")].to_html("tmp8-3-2a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df2 = df.set_index("population")
print(df2.head())
df2.head().to_html("tmp8-3-3-01.html")

print("------------------------------")  # 30個

df2.sort_index(ascending=False, inplace=True)
print(df2.head())
df2.head().to_html("tmp8-3-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())
df.head().to_html("tmp8-3-3a-01.html")

print("------------------------------")  # 30個

df2 = df.sort_values("population", ascending=False)
print(df2.head())
df2.head().to_html("tmp8-3-3a-02.html")

print("------------------------------")  # 30個

df.sort_values(["city","population"], inplace=True)
print(df.head())
df.head().to_html("tmp8-3-3a-03.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(2))

print("------------------------------")  # 30個

# 取得與更新單一純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = 160000
print(df.iloc[1,1])
df.iloc[1,1] = 560000
print(df.head(2))
df.head(2).to_html("tmp8-4-1.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))

print("------------------------------")  # 30個

# 取得與更新單筆記錄
print(df.loc[ordinals[1]])

print("------------------------------")  # 30個

s = ["新莊區", 416640, "新北市"] 
df.loc[ordinals[1]] = s
print(df.head(3))
df.head(3).to_html("tmp8-4-1a.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df)

print("------------------------------")  # 30個

# 取得與更新整個欄位
print(df.loc[:, "population"])

print("------------------------------")  # 30個

df.loc[:, "population"] = np.random.randint(34000, 700000, size=len(df))
print(df.head())
df.head().to_html("tmp8-4-1b.html")

df = pd.DataFrame(np.random.randint(5, 1500, size=(2,3)))
print(df)
df.to_html("tmp8-4-1c-01.html")

print("------------------------------")  # 30個

# 取得與更新整個DataFrame
print(df[df > 800])
df[df > 800].to_html("tmp8-4-1c-02.html")

print("------------------------------")  # 30個

df[df > 800] = df - 100
print(df)
df.to_html("tmp8-4-1c-03.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))

print("------------------------------")  # 30個

# 刪除純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = None
print(df.iloc[1,1])
df.iloc[1,1] = None
print(df.head(3))
df.head(3).to_html("tmp8-4-2.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head())

print("------------------------------")  # 30個

# 刪除記錄
df2 = df.drop(["second", "fourth"])    # 2,4 筆
print(df2.head())
df2.head().to_html("tmp8-4-2a-01.html")

print("------------------------------")  # 30個

df.drop(df.index[[2,3]], inplace=True) # 3,4 筆
print(df.head())
df.head().to_html("tmp8-4-2a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.head(3))

print("------------------------------")  # 30個

# 刪除欄位
df2 = df.drop(["population"], axis=1)
print(df2.head(3))
df2.head(3).to_html("tmp8-4-2b.html")

print("------------------------------------------------------------")  # 60個


# kilo 不可用 append, 但 sugar 可用
data = pd.DataFrame()
a = {"x":1,"y":2}
data = data.append(a,ignore_index=True)
print(data)

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

print(df.tail(3))

print("------------------------------")  # 30個

# 新增記錄
df.loc["third-1"] = ["士林區", 288340, "台北市"]
print(df.tail(3))
df.tail(3).to_html("tmp8-4-3-01.html")

print("------------------------------")  # 30個

# kilo 不可用 append, 但 sugar 可用
s = pd.Series({"city":"新北市","name":"中和區","population":413291})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))
df2.tail(3).to_html("tmp8-4-3-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    df.loc[i] = [np.random.randint(-1,1) for n in range(3)]
print(df)
df.to_html("tmp8-4-3a-01.html")

print("------------------------------")  # 30個

# kilo 不可用 append, 但 sugar 可用
df2 = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    s = pd.Series({"qty1":np.random.randint(-1,1),"qty2":np.random.randint(-1,1),"qty3":np.random.randint(-1,1)})
    df2 = df2.append(s, ignore_index=True)
print(df2)
df.to_html("tmp8-4-3a-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

df["area"] = pd.Series([np.random.randint(6000,9000) for n in range(len(df))]).values 
print(df.head())
df.head().to_html("tmp8-4-3b-01.html")

print("------------------------------")  # 30個

df.loc[:,"zip"] = np.random.randint(100, 120, size=len(df))
print(df.head())
df.head().to_html("tmp8-4-3b-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals =["first", "second", "third", "fourth", "fifth",
           "sixth", "seventh", "eigth", "ninth", "tenth",
           "eleventh", "twelvth", "thirteenth"]  
df.index = ordinals

columns =["city","name", "population"]
# 建立空的DataFrame物件
df_empty = pd.DataFrame(np.nan, index=ordinals, columns=columns)
print(df_empty)

print("------------------------------")  # 30個

# 複製DataFrame物件
df_copy = df.copy()
print(df_copy)

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame(np.random.randint(5,10,size=(3,4)),columns=["a","b","c","d"])  
df2 = pd.DataFrame(np.random.randint(5,10,size=(2,3)),columns=["b","d","a"])  
print(df1)
df1.to_html("tmp8-4-4a-01.html")

print("------------------------------")  # 30個

print(df2)
df2.to_html("tmp8-4-4a-02.html")

print("------------------------------")  # 30個

df3 = pd.concat([df1,df2])  
print(df3)
df3.to_html("tmp8-4-4a-03.html")

print("------------------------------")  # 30個

df4 = pd.concat([df1,df2], ignore_index=True)
print(df4) 
df4.to_html("tmp8-4-4a-04.html") 

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame({"key":["a","b","b"],"data1":range(3)})  
df2 = pd.DataFrame({"key":["a","b","c"],"data2":range(3)})  
print(df1)
df1.to_html("tmp8-4-4b-01.html")

print("------------------------------")  # 30個

print(df2)
df2.to_html("tmp8-4-4b-02.html")

print("------------------------------")  # 30個

df3 = pd.merge(df1, df2)
print(df3)
df3.to_html("tmp8-4-4b-03.html")

print("------------------------------")  # 30個

df4 = pd.merge(df2, df1)
print(df4)
df4.to_html("tmp8-4-4b-04.html")

print("------------------------------")  # 30個

df5 = pd.merge(df2, df1, how='left')
print(df5)
df5.to_html("tmp8-4-4b-05.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame({"名稱" : ["客戶A", "客戶B", "客戶A", "客戶B",
                             "客戶A", "客戶B", "客戶A", "客戶A"],
                   "編號" : ["訂單1", "訂單1", "訂單2", "訂單3",
                             "訂單2", "訂單2", "訂單1", "訂單3"],
                   "數量" : np.random.randint(1,5,size=8),
                   "售價" : np.random.randint(150,500,size=8)})

print(df)
df.to_html("tmp8-5-1-01.html")

print("------------------------------")  # 30個

print(df.groupby("名稱").sum())
df.groupby("名稱").sum().to_html("tmp8-5-1-02.html")

print("------------------------------")  # 30個

print(df.groupby(["名稱","編號"]).sum())
df.groupby(["名稱","編號"]).sum().to_html("tmp8-5-1-03.html")

print("------------------------------------------------------------")  # 60個

products = pd.DataFrame({
        "分類": ["居家", "居家", "娛樂", "娛樂", "科技", "科技"],
        "商店": ["家樂福", "頂好", "家樂福", "全聯", "頂好","家樂福"],
        "價格":[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
        "測試分數": [4, 3, 5, 7, 5, 8]})
print(products)
products.to_html("tmp8-5-2-01.html")

print("------------------------------")  # 30個

# 呼叫 pivot_table() 方法
pivot_products = products.pivot_table(index='分類',columns='商店',values='價格')
print(pivot_products)
pivot_products.to_html("tmp8-5-2-02.html")

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(np.random.rand(6,4), columns=list("ABCD"))
print(df)
df.to_html("tmp8-5-3-01.html")

print("------------------------------")  # 30個

df2 = df.apply(np.cumsum)
print(df2)
df2.to_html("tmp8-5-3-02.html")

print("------------------------------")  # 30個

df3 = df.apply(lambda x: x.max() - x.min())
print(df3)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




