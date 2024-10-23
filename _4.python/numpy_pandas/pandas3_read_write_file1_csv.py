"""
使用pandas讀寫csv檔, 讀成 DataFrame 格式



#匯出DataFrame
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(table, con = engine)

#匯入DataFrame
df.read_csv(filename)
df.read_json(filename)
df.read_html(filename)
df.read_excel(filename)
df.read_sql(query, engine)


匯出匯入DataFrame物件(5)

匯出
df.to_csv(filename)
df.to_json(filename)
df.to_html(filename)
df.to_excel(filename)
df.to_sql(filename)

匯入
pd.read_csv(filename)
pd.read_json(filename)
pd.read_html(filename)
pd.read_excel(filename)
pd.read_sql(filename)






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


print("------------------------------------------------------------")  # 60個
print("簡易讀取csv檔")
print("------------------------------------------------------------")  # 60個

"""
中文名,英文名,體重,全名
鼠,mouse,3,米老鼠
牛,ox,48,班尼牛
虎,tiger,33,跳跳虎
兔,rabbit,8,彼得兔
龍,dragon,38,逗逗龍
    :
豬,pig,42,佩佩豬
"""
filename = "data/animals.csv"
print("讀取csv檔案 :", filename)
df = pd.read_csv(filename)
print(df)
print(df.head())
print(df.info())

print("------------------------------------------------------------")  # 60個

filename = "data/animals_big5.csv"

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告

df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
print(df)

fullname = pd.DataFrame(df["全名"])
print(fullname)

print("------------------------------------------------------------")  # 60個

print("csv檔案 轉 df")
filename = "data/animals.csv"

df = pd.read_csv(filename)
print(df.head(5))

print("------------------------------------------------------------")  # 60個

filename = "data/animals.csv"
DataFrame = pd.read_csv(filename)
print(DataFrame["中文名"])
print()
print(DataFrame[["中文名", "英文名"]])
print()
print(DataFrame[["中文名", "英文名", "體重"]])
print()

DataFrame["中英文"] = DataFrame["中文名"] + DataFrame["英文名"]
print(DataFrame[["中文名", "英文名", "體重", "中英文"]])

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores2.csv"
print("讀取csv檔案 :", filename)
df = pd.read_csv(filename)
print(df)
print("df 之 欄名")
print(df.columns)
print("df 之 索引")
print(df.index)

print("df 之 某欄")
print(df["數學"])

print("------------------------------------------------------------")  # 60個

filename = "http://bit.ly/gradescsv"
print("pd讀取http csv檔案 :", filename)
df = pd.read_csv(filename)
print(df.head())

filename = "tmp_grades.csv"
# df.to_csv(filename)
# df.to_csv(filename, index=False, header=True, columns=["Name", "Sex", "Age"])
# df.to_csv(filename, index=False)
# df.to_csv(filename, index=False, encoding="big5")
df.to_csv(filename, index=False, encoding="utf8")
print("df寫入csv檔案 :", filename)

print("pd讀取http csv檔案 :", filename)
df2 = pd.read_csv(filename)
print(df2.head())

print("比較df是否相同")
cc = df.equals(df2)
print(cc)

print("------------------------------------------------------------")  # 60個

filename = "data/python_ReadWrite_CSV6_score.csv"
print("pd讀取csv檔案 :", filename)
df = pd.read_csv(filename, encoding="UTF-8")
print(df.head())
print("數學平均", np.mean(df["數學"]))
print("數學中位數", np.median(df["數學"]))

print("------------------------------------------------------------")  # 60個

filename = "data/grades.csv"
print("pd讀取csv檔案 :", filename)
df = pd.read_csv(filename)

print("df的前5筆資料")
print(df.head())

print("國文成績")
print(df["國文"])

print("國文成績")
print(df.國文)

cg = df.國文.values
print(type(cg))
print("cg")
print(cg)

print("平均值")
print(cg.mean())
print("標準差")
print(cg.std())

print("平均值")
print(df.國文.mean())
print("標準差")
print(df.國文.std())
print("顯示df統計資料")
print(df.describe())  # 顯示統計資料

# print('係數矩陣 :', df.corr())

# 只算兩科間的相關係數當然也可以。
print(df.國文.corr(df.數學))

df["總級分"] = df[["國文", "英文", "數學", "社會", "自然"]].sum(1)
print(df.head())

df["主科"] = df.數學 * 1.5 + df.英文

print(df.head())

print(df.sort_values(by="總級分", ascending=False).head(20))

print(df.sort_values(by=["主科", "總級分"], ascending=False).head(20))

print("------------------------------------------------------------")  # 60個

filename = "data/ExpensesRecord.csv"
print("pd讀取csv檔案 :", filename)
df = pd.read_csv(filename)
print(df.head(5))
print(df["說明"])
print(df[["說明", "支出金額"]])

df["單價"] = df["支出金額"] / df["數量"]
print(df[["數量", "支出金額", "單價"]])

print("------------------------------------------------------------")  # 60個

filename = "data/qunar_routes.csv"
print("pd讀取csv檔案 :", filename)
df = pd.read_csv(filename)

print(df.路線信息)
print()

print(df.路線信息.str.extract("(\d+)天\d+晚"))

df["天數"] = df.路線信息.str.extract("(\d+)天\d+晚")
print("ttttt2")
df["酒店評分"] = df.酒店信息.str.extract("(\d\.\d)分")
print("ttttt3")
df["酒店等級"] = df.酒店信息.str.extract("\n(.*)")
print("ttttt4")
df["價格"] = df.路線信息.str.extract("(\d+)起/人")
print("ttttt5")
print(df.head())
print(df.info())

print("酒店等級 :", df["酒店等級"])
print("酒店評分 :", df["酒店評分"])
print("價格 :", df["價格"])

class_map = {"其他": 0, "經濟型": 1, "舒適型": 2, "高檔型": 3, "豪華型": 4}
df["酒店等級"] = df["酒店等級"].map(class_map)

print("------------------------------------------------------------")  # 60個

filename = "data/python_ReadWrite_CSV7_onigiri.csv"
print("pd讀取csv檔案 :", filename)
dat = pd.read_csv(filename, encoding="UTF-8")

print(type(dat))
print(dat)

bins = range(0, 200, 10)
for b in bins:
    print(b)

print("計算平均數、變異數、標準差")

print("店長---------")
print("平均:", np.mean(dat["店長"]))
print("變異數:", np.var(dat["店長"]))
print("標準差:", np.std(dat["店長"]))

print("太郎---------")
print("平均:", np.mean(dat["太郎"]))
print("變異數:", np.var(dat["太郎"]))
print("標準差:", np.std(dat["太郎"]))

print("------------------------------------------------------------")  # 60個

print("讀取 .csv 檔 1")
filename = "C:/_git/vcs/_1.data/______test_files1/__RW/_csv/scores.csv"
na = np.genfromtxt(filename, delimiter=",", skip_header=1)
print("資料寬高")
print(na.shape)

print("國文最高分數：", na[:, 1].max())
print("英文最低分數：", na[:, 2].min())
print("數學平均分數：", na[:, 3].mean())
total1 = na[:, 1] + na[:, 2] + na[:, 3]
print(total1)
print("全班最高總分：", total1.max())

total2 = na[:, 1:4].sum(axis=1)
print(total2)
print("全班最高總分：", total2.max())

print("------------------------------------------------------------")  # 60個


def format_data(df):
    # 用missing填充缺失值，並去除首尾空格
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("missing")
            df[column] = df[column].apply(lambda x: x.strip())

    # 清洗數據：將位置只保留省份，面料只保留第一個
    # df["銷量"]=df["銷量"].apply(lambda x: int(x.replace("人付款","")))
    df["位置"] = df["位置"].apply(lambda x: x.split(" ")[0])
    df["面料"] = df["面料"].apply(lambda x: x.split(",")[0])

    return df


filename = "data/dress.csv"
print("pd讀取csv檔案 :", filename)
df = pd.read_csv(filename)
# print(df.head())

# 刪除缺失值個數>100的列
for column in df.columns:
    isnullList = df[column].isnull()
    nullCnt = len(isnullList[isnullList == True])
    if nullCnt > 100:
        del df[column]
#         print("del column:" + column)

# 刪除不重要的特征
del df["貨號"]
del df["年份季節"]
del df["品牌"]
del df["銷量"]

df = format_data(df)
print(df)

print("------------------------------------------------------------")  # 60個

print("用 Groupby 看美國哪裡最容易看到 UFO")
filename = "http://bit.ly/uforeports"
print("pd讀取http csv檔案 :", filename)
df = pd.read_csv(filename)
print(df.head())

df_state = df.groupby("State").count()
print(df_state)

df_state.sort_values(by="Time", ascending=False)
print(df_state)

df_state.sort_values(by="Time", ascending=False, inplace=True)
print(df_state.head(10))

df_state[:10].Time.plot(kind="bar")

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

print("有缺資料之dataframe")

filename = "data/missing_data.csv"

df = pd.read_csv(filename)
print(df)

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
print(df)

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
print(df)

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

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

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

print("------------------------------")  # 30個

fig, axes = plt.subplots(nrows=1, ncols=2)
df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).sum()
df.plot(kind="bar", ax=axes[0])

df = titanic[["Survived", "Died"]].groupby(titanic["Sex"]).mean()
df.plot(kind="bar", ax=axes[1])

plt.show()

print("------------------------------")  # 30個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).sum()
df.plot(kind="bar")

plt.show()

print("------------------------------")  # 30個

df = titanic[["Survived", "Died"]].groupby(titanic["PClass"]).mean()
df.plot(kind="bar")

plt.show()

print("------------------------------")  # 30個

df = titanic.drop("Died", axis=1)
print("係數矩陣 :", df.corr())

plt.show()

print("------------------------------------------------------------")  # 60個

dists = {
    "name": [
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
    "population": [
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
    "city": [
        "台北市",
        "新北市",
        "桃園市",
        "台中市",
        "台南市",
        "高雄市",
        "台北市",
        "新北市",
        "桃園市",
        "高雄市",
        "高雄市",
        "台北市",
        "新北市",
    ],
}
df = pd.DataFrame(dists)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
print(df.head())

df.columns = ["區", "人口", "直轄市"]
print(df.head(4))

print(df.index)

print(df.columns)

print(df.values)

print("資料數= ", len(df))

print("形狀= ", df.shape)

cc = df.info()
print(cc)

for index, row in df.iterrows():
    print(index, row["city"], row["name"], row["population"])

df2 = df.set_index("city")
print(df2.head())

df3 = df2.reset_index()
print(df3.head())

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")

df2 = df.set_index(["city", "name"])
df2.sort_index(ascending=False, inplace=True)
print(df2)

print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/dists.csv", encoding="utf8")
ordinals = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eigth",
    "ninth",
    "tenth",
    "eleventh",
    "twelvth",
    "thirteenth",
]
df.index = ordinals

cc = df["population"].head(3)
print(cc)

cc = df[["city", "name"]].head(3)
print(cc)

cc = df.population.head(3)  # 使用屬性方式
print(cc)

cc = df[0:3]  # 不含 3
print(cc)

print(df["sixth":"eleventh"])  # 含 "eleventh"
cc = df["sixth":"eleventh"]
print(cc)

print("------------------------------")  # 30個

print(df.loc[ordinals[1]])
print(type(df.loc[ordinals[1]]))

print("------------------------------")  # 30個

print(df.loc[:, ["name", "population"]].head(3))
cc = df.loc[:, ["name", "population"]].head(3)
print(cc)

print("------------------------------")  # 30個

print(df.loc["third":"fifth", ["name", "population"]])

print("------------------------------")  # 30個

print(df.loc["third", ["name", "population"]])
cc = df.loc["third":"fifth", ["name", "population"]]
print(cc)

print("------------------------------")  # 30個

# 取得單一純量值
print(df.loc[ordinals[0], "name"])
print(type(df.loc[ordinals[0], "name"]))

print("------------------------------")  # 30個

print(df.loc["first", "population"])
print(type(df.loc["first", "population"]))

print("------------------------------")  # 30個

print(df.iloc[3])  # 第 4 筆

print("------------------------------")  # 30個

print(df.iloc[3:5, 1:3])  # 切割
cc = df.iloc[3:5, 1:3]
print(cc)

print("------------------------------")  # 30個

print(df.iloc[1:3, :])  # 切割列
cc = df.iloc[1:3, :]
print(cc)

print("------------------------------")  # 30個

print(df.iloc[:, 1:3])  # 切割欄
cc = df.iloc[:, 1:3]
print(cc)

print("------------------------------")  # 30個

print(df.iloc[[1, 2, 4], [0, 2]])  # 索引清單
cc = df.iloc[[1, 2, 4], [0, 2]]
print(cc)

print("------------------------------")  # 30個

# 取得單一純量值
print(df.iloc[1, 1])
print(df.iat[1, 1])

print("------------------------------")  # 30個

cc = df[df.population > 350000]
print(cc)

print("------------------------------")  # 30個

print(df[df["city"].isin(["台北市", "高雄市"])])
cc = df[df["city"].isin(["台北市", "高雄市"])]
print(cc)

print("------------------------------")  # 30個

print(df[(df.population > 350000) & (df.population < 500000)])
cc = df[(df.population > 350000) & (df.population < 500000)]
print(cc)

print("------------------------------")  # 30個

print(df[df["city"].str.startswith("台")])
cc = df[df["city"].str.startswith("台")]
print(cc)

print("------------------------------")  # 30個

df2 = df.set_index("population")
print(df2.head())

print("------------------------------")  # 30個

# 排序
df2.sort_index(ascending=False, inplace=True)
print(df2.head())

print("------------------------------")  # 30個

# 排序
df2 = df.sort_values("population", ascending=False)
print(df2.head())

print("------------------------------")  # 30個

# 排序
df.sort_values(["city", "population"], inplace=True)
print(df.head())

print("------------------------------")  # 30個

# 取得與更新單一純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = 160000
print(df.iloc[1, 1])
df.iloc[1, 1] = 560000
print(df.head(2))

print("------------------------------")  # 30個

# 取得與更新單筆記錄
print(df.loc[ordinals[1]])

print("------------------------------")  # 30個

s = ["新莊區", 416640, "新北市"]
df.loc[ordinals[1]] = s
print(df.head(3))

print("------------------------------")  # 30個

# 取得與更新整個欄位
print(df.loc[:, "population"])

print("------------------------------")  # 30個

df.loc[:, "population"] = np.random.randint(34000, 700000, size=len(df))
print(df.head())

df = pd.DataFrame(np.random.randint(5, 1500, size=(2, 3)))
print(df)

print("------------------------------")  # 30個

# 取得與更新整個DataFrame
print(df[df > 800])
cc = df[df > 800]
print(cc)

print("------------------------------")  # 30個

df[df > 800] = df - 100
print(df)

print("------------------------------")  # 30個

# 刪除純量值
print(df.loc[ordinals[0], "population"])
df.loc[ordinals[0], "population"] = None
print(df.iloc[1, 1])
df.iloc[1, 1] = None
print(df.head(3))

print("------------------------------")  # 30個

# 刪除記錄
df2 = df.drop(["second", "fourth"])  # 2,4 筆
print(df2.head())

print("------------------------------")  # 30個

df.drop(df.index[[2, 3]], inplace=True)  # 3,4 筆
print(df.head())

print("------------------------------")  # 30個

# 刪除欄位
df2 = df.drop(["population"], axis=1)
print(df2.head(3))

print("------------------------------------------------------------")  # 60個

# kilo 不可用 append, 但 sugar 可用
data = pd.DataFrame()
a = {"x": 1, "y": 2}
data = data.append(a, ignore_index=True)
print(data)

print("------------------------------")  # 30個

# 新增記錄
df.loc["third-1"] = ["士林區", 288340, "台北市"]
print(df.tail(3))

print("------------------------------")  # 30個

# kilo 不可用 append, 但 sugar 可用
s = pd.Series({"city": "新北市", "name": "中和區", "population": 413291})
df2 = df.append(s, ignore_index=True)
print(df2.tail(3))

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    df.loc[i] = [np.random.randint(-1, 1) for n in range(3)]
print(df)

print("------------------------------")  # 30個

# kilo 不可用 append, 但 sugar 可用
df2 = pd.DataFrame(columns=("qty1", "qty2", "qty3"))
for i in range(5):
    s = pd.Series(
        {
            "qty1": np.random.randint(-1, 1),
            "qty2": np.random.randint(-1, 1),
            "qty3": np.random.randint(-1, 1),
        }
    )
    df2 = df2.append(s, ignore_index=True)
print(df2)

print("------------------------------------------------------------")  # 60個

df["area"] = pd.Series([np.random.randint(6000, 9000) for n in range(len(df))]).values
print(df.head())

print("------------------------------")  # 30個

df.loc[:, "zip"] = np.random.randint(100, 120, size=len(df))
print(df.head())

print("------------------------------------------------------------")  # 60個

columns = ["city", "name", "population"]
# 建立空的DataFrame物件
df_empty = pd.DataFrame(np.nan, index=ordinals, columns=columns)
print(df_empty)

print("------------------------------")  # 30個

# 複製DataFrame物件
df_copy = df.copy()
print(df_copy)

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame(np.random.randint(5, 10, size=(3, 4)), columns=["a", "b", "c", "d"])
df2 = pd.DataFrame(np.random.randint(5, 10, size=(2, 3)), columns=["b", "d", "a"])
print(df1)
print(df2)

df3 = pd.concat([df1, df2])
print(df3)

print("------------------------------")  # 30個

df4 = pd.concat([df1, df2], ignore_index=True)
print(df4)

print("------------------------------------------------------------")  # 60個

df1 = pd.DataFrame({"key": ["a", "b", "b"], "data1": range(3)})
df2 = pd.DataFrame({"key": ["a", "b", "c"], "data2": range(3)})
print(df1)
print(df2)

print("------------------------------")  # 30個

df3 = pd.merge(df1, df2)
print(df3)

print("------------------------------")  # 30個

df4 = pd.merge(df2, df1)
print(df4)

print("------------------------------")  # 30個

df5 = pd.merge(df2, df1, how="left")
print(df5)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {
        "名稱": ["客戶A", "客戶B", "客戶A", "客戶B", "客戶A", "客戶B", "客戶A", "客戶A"],
        "編號": ["訂單1", "訂單1", "訂單2", "訂單3", "訂單2", "訂單2", "訂單1", "訂單3"],
        "數量": np.random.randint(1, 5, size=8),
        "售價": np.random.randint(150, 500, size=8),
    }
)
print(df)
print(df.groupby("名稱").sum())
print(df.groupby(["名稱", "編號"]).sum())

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(
    {
        "分類": ["居家", "居家", "娛樂", "娛樂", "科技", "科技"],
        "商店": ["家樂福", "頂好", "家樂福", "全聯", "頂好", "家樂福"],
        "價格": [11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
        "測試分數": [4, 3, 5, 7, 5, 8],
    }
)
print(df)

# 呼叫 pivot_table() 方法
pivot_products = df.pivot_table(index="分類", columns="商店", values="價格")
print(pivot_products)

print("------------------------------------------------------------")  # 60個

df = pd.DataFrame(np.random.rand(6, 4), columns=list("ABCD"))
print(df)

df2 = df.apply(np.cumsum)
print(df2)

df3 = df.apply(lambda x: x.max() - x.min())
print(df3)

print("------------------------------------------------------------")  # 60個

# df轉csv
print("讀寫CSV文件")

df = pd.DataFrame({"Name": ["Smith", "Lucy"], "Age": ["25", "20"], "Sex": ["男", "女"]})
print(df.info())  # 顯示dataframe相關信息
df.to_csv("tmp.csv", index=False, header=True, columns=["Name", "Sex", "Age"])

df1 = pd.read_csv("tmp.csv")
print(df1.info())
print(df1)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 準備移出

"""
print('資料結構訊息', df.info())
print('資料shape :', df.shape)
print('資料內容\n', df)
print('資料head\n', df.head())
print(type(df))
print(df)
print(df.shape)
"""


""" 看起來以下4種皆不好
print("pd讀取csv檔案00 :", filename)
print('跳過標題與索引')
df = pd.read_csv(filename, header=0, index_col=0)
print(df)

print("pd讀取csv檔案01 :", filename)
df = pd.read_csv(filename, header=0, index_col=1)
print(df)

print("pd讀取csv檔案10 :", filename)
df = pd.read_csv(filename, header=1, index_col=0)
print(df)

print("pd讀取csv檔案11 :", filename)
df = pd.read_csv(filename, header=1, index_col=1)
print(df)
"""

filename = "tmp_ExpensesRecord.csv"
df.to_csv(filename)
print("df寫入csv檔案 :", filename)


filename = "tmp_score2.csv"
df.to_csv(filename, encoding="utf-8-sig")
print("df寫入csv檔案 :", filename)

filename = "tmp_score1.csv"
df.to_csv(filename, encoding="utf-8-sig")
print("df寫入csv檔案 :", filename)

df.to_csv("tmp_dists2.csv", index=False, encoding="utf8")
df.to_json("tmp_dists.json")

print("df 轉 csv檔案")
filename = "tmp_write_read_csv07.csv"
df.to_csv(filename)

filename = "tmp_district.csv"
df3.to_csv(filename, encoding="big5", index=False)
print("df寫入csv檔案 :", filename)

print("------------------------------------------------------------")  # 60個

# 匯入CSV格式的檔案
df = pd.read_csv("tmp_dists2.csv", encoding="utf8")
print(df)

print("pd讀取csv檔案 :", filename)
print("跳過索引")
df = pd.read_csv(filename, encoding="utf-8-sig", index_col=0)
print(df)

print("------------------------------------------------------------")  # 60個

data = {
    "種類": ["Bike", "Bus", "Car", "Truck"],
    "數量": [3, 4, 6, 2],
    "輪數": ["2", "4", "4", "6"],
}
df = pd.DataFrame(data, index=["A", "B", "C", "D"])

filename = "tmp_vehicles.csv"
df.to_csv(filename, index=False, encoding="big5")
print("df寫入csv檔案 :", filename)

filename = "tmp_vehicles.csv"
print("pd讀取csv檔案 :", filename)
df1 = pd.read_csv(filename, encoding="big5")
print(df1)

print("------------------------------------------------------------")  # 60個

# NYC 311 service request dataset
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, dtype="unicode")

cc = requests["Incident Zip"].unique()
print(cc)

print("------------------------------------------------------------")  # 60個

# Fixing the nan values and string/float confusion

na_values = ["NO CLUE", "N/A", "0"]
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, na_values=na_values, dtype={"Incident Zip": str})

cc = requests["Incident Zip"].unique()
print(cc)

# What's up with the dashes?

rows_with_dashes = requests["Incident Zip"].str.contains("-").fillna(False)
cc = len(requests[rows_with_dashes])
print(cc)

print(requests[rows_with_dashes])

# But then my friend Dave pointed out that 9-digit zip codes are normal.
# Let's look at all the zip codes with more than 5 digits, make sure they're okay, and then truncate them.
long_zip_codes = requests["Incident Zip"].str.len() > 5
cc = requests["Incident Zip"][long_zip_codes].unique()
print(cc)

requests["Incident Zip"] = requests["Incident Zip"].str.slice(0, 5)

# Earlier I thought 00083 was a broken zip code, but turns out Central Park's zip code 00083!
# Shows what I know. I'm still concerned about the 00000 zip codes, though: let's look at that.
cc = requests[requests["Incident Zip"] == "00000"]
print(cc)

zero_zips = requests["Incident Zip"] == "00000"
requests.loc[zero_zips, "Incident Zip"] = np.nan

# fail
# unique_zips = requests['Incident Zip'].unique()
# unique_zips.sort()
# cc = unique_zips
# print(cc)
zips = requests["Incident Zip"]
# Let's say the zips starting with '0' and '1' are okay, for now. (this isn't actually true -- 13221 is in Syracuse, and why?)
is_close = zips.str.startswith("0") | zips.str.startswith("1")
# There are a bunch of NaNs, but we're not interested in them right now, so we'll say they're False
is_far = ~(is_close) & zips.notnull()

cc = zips[is_far]
print(cc)

cc = requests[is_far][["Incident Zip", "Descriptor", "City"]].sort_values(
    "Incident Zip"
)
print(cc)

cc = requests["City"].str.upper().value_counts()
print(cc)

print("------------------------------------------------------------")  # 60個

# Putting it together

na_values = ["NO CLUE", "N/A", "0"]
csv_filename = "C:/_git/vcs/_big_files/311-service-requests.csv"
print("pd讀取csv檔案 :", csv_filename)
requests = pd.read_csv(csv_filename, na_values=na_values, dtype={"Incident Zip": str})


def fix_zip_codes(zips):
    # Truncate everything to length 5
    zips = zips.str.slice(0, 5)
    # Set 00000 zip codes to nan
    zero_zips = zips == "00000"
    zips[zero_zips] = np.nan
    return zips


requests["Incident Zip"] = fix_zip_codes(requests["Incident Zip"])

cc = requests["Incident Zip"].unique()
print(cc)

print("------------------------------------------------------------")  # 60個

# Parsing Unix timestamps

# Read it, and remove the last row
popcon = pd.read_csv(
    "data/popularity-contest",
    sep=" ",
)[:-1]
popcon.columns = ["atime", "ctime", "package-name", "mru-program", "tag"]

print(popcon[:5])

popcon["atime"] = popcon["atime"].astype(int)
popcon["ctime"] = popcon["ctime"].astype(int)

popcon["atime"] = pd.to_datetime(popcon["atime"], unit="s")
popcon["ctime"] = pd.to_datetime(popcon["ctime"], unit="s")

print(popcon["atime"].dtype)

print(popcon[:5])

print("------------------------------------------------------------")  # 60個

popcon = popcon[popcon["atime"] > "1970-01-01"]

# 不包含lib的
nonlibraries = popcon[~popcon["package-name"].str.contains("lib")]

cc = nonlibraries.sort_values("ctime", ascending=False)[:10]
print(cc)

print("------------------------------------------------------------")  # 60個

# use_pivot_sum

filename = "data\ordersList.csv"
print("pd讀取csv檔案 :", filename)
print("跳過標題")
df = pd.read_csv(filename, encoding="utf-8", header=0)

print(
    df.pivot_table(
        index="品名",
        columns="客戶名稱",
        values="金額",
        fill_value=0,
        margins=True,
        aggfunc="sum",
    )
)

print(
    df.pivot_table(index="品名", columns="客戶名稱", values="金額", fill_value=0, margins=True)
)

print("------------------------------------------------------------")  # 60個

print("df 轉 檔案")

data = {
    "中文名": ["鼠", "牛", "虎", "兔"],
    "英文名": ["mouse", "ox", "tiger", "rabbit"],
    "體重": [3, 48, 33, 8],
    "全名": ["米老鼠", "班尼牛", "跳跳虎", "彼得兔"],
}
df = pd.DataFrame(data, index=["1", "2", "3", "4"])

df.to_csv("tmp_write_read_csv06.csv", index=False, encoding="big5")

print("檔案 轉 df")
df = pd.read_csv("tmp_write_read_csv06.csv", encoding="big5")
print(df)

print("------------------------------------------------------------")  # 60個

cities = pd.read_csv("data/california_cities.csv")

print(cities.head())

# extracting the data we ar interested in
latitude, longitude = cities["latd"], cities["longd"]
population, area = cities["population_total"], cities["area_total_km2"]

# to scatter the points, using size and color but without label

import seaborn

seaborn.set()
plt.scatter(
    longitude,
    latitude,
    label=None,
    c=np.log10(population),
    cmap="viridis",
    s=area,
    linewidth=0,
    alpha=0.5,
)
# plt.axis(aspect='equal') NG
plt.xlabel("Longitude")
plt.ylabel("Longitude")
plt.colorbar(label="log$_{10}$(population)")
plt.clim(3, 7)
# now we will craete a legend, we will plot empty lists with the desired size and label
for area in [100, 300, 500]:
    plt.scatter([], [], c="k", alpha=0.3, s=area, label=str(area) + "km$^2$")
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="City Areas")
plt.title("Area and Population of California Cities")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


"""

filename = "tmp_動物資料0.csv"
df.to_csv(filename)  # 預設為 儲存index行

filename = "tmp_動物資料1.csv"
df.to_csv(filename, index=False)  # 不儲存index行

filename = "tmp_動物資料2.csv"
df.to_csv(filename, index=True)  # 儲存index行

df.to_csv("tmp_datas11.csv",index=False,encoding="utf8")

df2 = pd.read_csv("tmp_datas11.csv", encoding="utf8")


print("df存成csv檔")
df.to_csv("tmp_olympics.csv")


print("csv檔案轉df")
df = pd.read_csv("data/student.csv")
print(df)




"""
