"""



"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import time
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

# 6-1 探索性資料分析──以Titanic(鐵達尼號)之生還預測為例
# 資料科學 0. 問個感興趣的問題

# 資料科學 1. 資料取得
# 資料科學1.1 自建資料或下載資料後上傳到雲端硬碟

# train.csv行資料說明.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/titanic.csv"
df = pd.read_csv(filename)

print(df)

# 資料科學2. 資料處理
# 資料科學2.1 由列資料了解資料集

print(df.head())

# 資料科學2.2 了解行資料的標題與資料型別 ( 整數、浮點數、字串等)
# Step 01

print(df.info())

# Step 02

print(df.describe())

# 資料科學2.3 資料清理
# 缺失值的補值或刪除
# Step 01

print(df.isnull())

# Step 02

print(df.isnull().sum())

print(df.isnull().count())

print(df.isnull().sum() / df.isnull().count() * 100)

# Step 03

df[df["Age"].isnull() == True]

# Step 04

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

# Step 05

df[df["Embarked"].isnull()]

# Step 06

df["Embarked"].value_counts()

# Step 07

df["Embarked"] = df["Embarked"].fillna("S")

df.loc[[61, 829], :]  # 顯示列索引61,829的資料

# Step 08

print(df.info())

df = df.drop("Cabin", axis=1)

print(df.info())

# 刪除重複值或異常值
df[df.duplicated()]

# 資料轉換
print(df.head())

s = {"female": 0, "male": 1}
df["Sex"] = df["Sex"].map(s)
e = {"S": 0, "C": 1, "Q": 2}
df["Embarked"] = df["Embarked"].map(e)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)

print(df.head())

# 資料科學3.2 資料視覺化
# 1.全體乘客生還、死亡的比例

print(df["Survived"].value_counts())

df["Survived"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------------------------------------")  # 60個

# 2.男性、女性乘客的比例

print(df["Sex"].value_counts())

df["Sex"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------------------------------------")  # 60個

# 3.搭1等艙、2等艙、3等艙的乘客比例

print(df["Pclass"].value_counts())

df["Pclass"].value_counts().plot(kind="pie", autopct="%1.2f%%")
plt.show()

print("------------------------------------------------------------")  # 60個

# 4.進一步探討性別與生還的關係

# 女、男乘客的人數

print(df.groupby(["Sex"])["PassengerId"].count())

# 不同性別的生還和死亡人數

print(df.groupby(["Sex", "Survived"])["PassengerId"].count())

df.groupby(["Sex", "Survived"])["PassengerId"].count().plot(kind="bar", rot=1)
plt.show()

print("------------------------------------------------------------")  # 60個

# 不同性別生還人數/不同性別人數

ss = (
    df.groupby(["Sex", "Survived"])["PassengerId"].count()
    / df.groupby(["Sex"])["PassengerId"].count()
    * 100
)
print(ss)

ss.plot(kind="bar", color=["r", "g"], rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

# 5.進一步探討艙等與生還的關係

# 三種艙等的生還和死亡人數

print(df.groupby(["Pclass", "Survived"])["PassengerId"].count())

df.groupby(["Pclass", "Survived"])["PassengerId"].count().plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

# 不同艙等生還人數/不同艙等人數

ps = (
    df.groupby(["Pclass", "Survived"])["PassengerId"].count()
    / df.groupby(["Pclass"])["PassengerId"].count()
    * 100
)
print(ps)

ps.plot(kind="bar", rot=0)
plt.show()

print("------------------------------------------------------------")  # 60個

# 6-2 探索性資料分析──以 Iris 的花種分類為例
# 資料科學0. 感興趣的問題

# 資料科學1. 資料取得
# 資料科學1.1 自建資料或從網路下載資料後上傳到雲端硬碟

# Iris.jpg
# 資料科學1.2 讀取Google雲端硬碟中的csv檔
# 資料科學1.3 將行列結構的資料建立為Pandas的資料框

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
print(df)

df = df.drop("Id", axis=1)
print(df.head())

# 資料科學2. 資料處理
# 資料科學2.1 由列資料了解資料集

print(df.head())

# 資料科學2.2 了解行資料的標題與資料型別(整數、浮點數、字串等)

print(df.info())

# 資料科學2.3 資料清理

# 缺失值的補值或刪除

print(df.info())

# 刪除重複值或異常值

print(df[df.duplicated()])

df = df.drop_duplicates()

print(df[df.duplicated()])

df.reset_index(drop=True)  # 將列索引重新編號

# 資料轉換

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
print(df.head())

# 資料科學3. 探索性資料分析
# 資料科學3.1 觀察資料的分佈(統計)
print(df.head())

# 資料科學3.2 資料視覺化
# Step 01

c = {0: "r", 1: "g", 2: "b"}
df["colors"] = df["Species"].map(c)
print(df)

# Step 02
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (圖)-不同欄位和「類別(Species)」所繪製的散佈圖
# (a)花萼長度
df.plot(kind="scatter", x="SepalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (b)花萼寬度
df.plot(kind="scatter", x="SepalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (c)花瓣長度
df.plot(kind="scatter", x="PetalLengthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (d)花瓣寬度
df.plot(kind="scatter", x="PetalWidthCm", y="Species", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (圖)-2個欄位組合所繪製的散佈圖
# (a)花萼長度 vs. 花萼寬度
df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (b)花瓣長度 vs. 花瓣寬度
df.plot(kind="scatter", x="PetalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (c)花萼長度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (d)花瓣長度 vs. 花萼寬度
df.plot(kind="scatter", x="PetalLengthCm", y="SepalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (e)花萼長度 vs. 花瓣長度
df.plot(kind="scatter", x="SepalLengthCm", y="PetalLengthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個

# (f)花萼寬度 vs. 花瓣寬度
df.plot(kind="scatter", x="SepalWidthCm", y="PetalWidthCm", c=df["colors"])
plt.show()

print("------------------------------------------------------------")  # 60個


# 氣溫
t = [17, 17, 17, 22, 19, 21, 17, 17, 22, 24, 21, 21, 21, 17, 25, 21, 20, 19, 19, 22]

# 飲料銷售量
q = [
    386,
    360,
    383,
    146,
    300,
    254,
    403,
    381,
    269,
    99,
    171,
    204,
    213,
    279,
    97,
    262,
    262,
    225,
    240,
    226,
]

df = pd.DataFrame()

df["T"] = t  # 行資料：氣溫

df["Q"] = q  # 行資料：銷售量

print(df.head())

df.plot(kind="scatter", x="T", y="Q")
plt.show()

df_X = df[["T"]]  # 雙層的中括號(特徵值)，設定成資料框
df_y = df["Q"]  # 單層的中括號(標籤)，設定成序列
print(df_X.head())

print(df_y.head())

print("------------------------------------------------------------")  # 60個

# 8-2 機器學習實作

# 8-2-1 提出具體的假設
# 8-2-2 找出機器學習模型
# 挑選模型：匯入線性迴歸模型

from sklearn.linear_model import LinearRegression

# 學習訓練：建立並訓練線性迴歸模型

lm = LinearRegression()  # 建立新模型 lm
lm.fit(df_X, df_y)  # 訓練模型

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None, normalize=False)

# 測試評估
# 決定模型：取出線性迴歸模型的 m、b 參數

print("線性迴歸的模型為 y = f(x) = mx +b")
print("m 為 ", lm.coef_)
print("b 為 ", lm.intercept_)

# 線性迴歸的模型為 y = f(x) = mx +b
# m 為  [-33.19704219]
# b 為  920.2809917355372

# 進行預測

temp = [[23]]  # 輸入特徵值(氣溫)
p = lm.predict(temp)  # 輸出標籤(預測的銷售量)
print(p)

# [156.74902131]

temp = [[23], [18], [36]]
p = lm.predict(temp)
print(p)

# [ 156.74902131  322.73423227 -274.81252719]


print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Iris為例

# 1. 資料取得

filename = "data/Iris2.csv"

df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

df.info()

df = df.drop_duplicates()  # 刪除重複列
df.reset_index(drop=True)  # 將列索引重新編號
s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
df.info()

# 3. 探索性資料分析
print(df.head())
"""
#4. 機器學習做資料分析
9-2 機器學習實作──以Iris為例
9-2-1 提出具體的假設
9-2-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
df_y = df["Species"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)  # 建立新模型 knn

knn.fit(X_train, y_train)  # 用 training data 去訓練模型

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的正確率計算-------")

print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 用 training data 去訓練模型
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 8
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

# 加廣知識：視覺化圖表來顯示準確率

df_knn = pd.DataFrame()
df_knn["s"] = s
df_knn.index = [3, 4, 5, 6, 7, 8, 9, 10]
df_knn.plot(grid=True)

plt.show()

print("分類的預測結果：")
pred = knn.predict(X_test)  # 產生Test data預測結果
print(pred)

print(y_test.values)  # 觀察Test data真實數據

# 加廣知識：利用values屬性做橫式顯示

print(y_test)

print(y_test.values)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 1.0

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

# 加深知識：交叉驗證概念

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("交叉驗證每次的準確率：", s)
print("交叉驗證得到的平均準確率：", s.mean())

# 決定模型
# 進行分類預測

new = [[6.6, 3.1, 5.2, 2.4]]
v = knn.predict(new)
if v == 0:
    s = "Iris-Setosa"
elif v == 1:
    s = "Iris-Versicolour"
elif v == 2:
    s = "Iris-Virginica"
else:
    s = "錯誤"
print("預測結果為：", s)

# 預測結果為： 錯誤

print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Titanic為例

# 1. 資料取得

filename = "data/titanic.csv"
df = pd.read_csv(filename)
print(df.head())

# 2. 資料處理
df.info()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna("S")
df = df.drop("Cabin", axis=1)
print("重複值：", df[df.duplicated()])  # 檢查有無重複值

df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print(df.head())

# 重複值： Empty DataFrame

# 3. 探索性資料分析

print(df.head())

"""
4. 機器學習做資料分析
9-4 機器學習實作─以Titanic為例
9-4-1 提出具體的假設
9-4-2 找出機器學習模型
挑選模型：匯入 KNN 模型
"""

from sklearn.neighbors import KNeighborsClassifier

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["Sex", "Pclass"]]
df_y = df["Survived"]

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

k = 1
knn = KNeighborsClassifier(n_neighbors=k)

knn.fit(X_train, y_train)

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的準確率計算-------")
print("準確率:", knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    k = i
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)  # 用 training data 去訓練模型
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))

k = 4
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)

print("分類的預測結果：")
pred = knn.predict(X_test)
print(pred)  # 觀察預測結果

print("真實數據：")
print(y_test.values)  # 觀察真實數據(Test data)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

# 0.7541899441340782

from sklearn.metrics import confusion_matrix

confusion_matrix(y_test, pred)

from sklearn.model_selection import cross_val_score

s = cross_val_score(knn, df_X, df_y, scoring="accuracy", cv=10)
print("準確率：", s)
print("平均準確率：", s.mean())
print("最高：", s.max())
print("最差：", s.min())

# 決定模型
# 進行分類預測

print("-----------(1)電影中兩位主角的生還推測-------------")

Rose = [[0, 1]]  # 女性 頭等艙 蘿絲（Rose DeWitt Bukater）
Jack = [[1, 3]]  # 男性 三等艙 傑克（Jack Dawson）
v = knn.predict(Rose)
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Rose能生還嗎 ? ", s)  # Rose為女性,及坐頭等艙

v = knn.predict(Jack)
if v == 1:
    s = "生還"
else:
    s = "死亡"

print("Jack能生還嗎 ? ", s)  # Jack為男性,及坐三等艙

# 真實的伊西多和伊達·斯特勞斯（Isidor and Ida Straus）夫婦 (You stay, I stay)
# http://www.epochtimes.com/b5/17/12/6/n9931745.htm
# Isidor 美國梅西百貨創辦人之一

print("-----(2)真實的伊西多和伊達·斯特勞斯夫婦的生還推測-------")
Mrs = [[0, 1]]  # 女性 頭等艙 Straus, Mrs. Isidor (Rosalie Ida Blun)
Mr = [[1, 1]]  # 男性 頭等艙 Straus, Mr. Isidor
v = knn.predict(Mrs)
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Straus能生還嗎 ? ", s)  # Ida為女性,及坐頭等艙，可優先搭乘救生艇存活

v = knn.predict(Mr)  # Isidor的生存率有多高呢？
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mr. Straus能生還嗎 ? ", s)

# 真實的 Mrs. Brown
# https://hokkfabrica.com/her-story-margaret-brown-from-titanic/
#

print("-----------(3)真實的Mrs. Brown的生還推測-------------")

# 女性 頭等艙 Brown, Mrs. James Joseph (Margaret Tobin) 故事中的暴發戶 對Jack很友善
Brown = [[0, 1]]
v = knn.predict(Brown)  # Mrs. Brown呢？
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Brown能生還嗎 ? ", s)

print("-------------- (5)若你也搭上了鐵達尼號呢？ ----------------")

# s=input('您的性別（0：女，1：男），請輸入代碼？ ')
s = 1
# c=input('搭乘的船艙艙等（1：S艙，2：C艙，3：Q艙），請輸入代碼？ ')
c = 3
you = [[int(s), int(c)]]
v = knn.predict(you)
if v == 1:
    print("預測為:幸運生還")
else:
    print("預測為:無法生還")

print("------------------------------------------------------------")  # 60個

# 10-1 機器學習前準備
# 1. 資料取得

filename = "data/Iris2.csv"
df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

print(df.info())

df = df.drop_duplicates()  # 刪除重複列

df.reset_index(drop=True)  # 將列索引重新編號

s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}

df["Species"] = df["Species"].map(s)

print(df.info())

# 3. 探索性資料分析
print(df.head())

# 4. 機器學習做資料分析
# 10-2 機器學習實作
# 挑選模型：匯入 K- 平均法模型

from sklearn.cluster import KMeans

# 學習訓練：建立並訓練 K-平均法模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
k = 1
km = KMeans(n_clusters=k)
km.fit(df_X)

# 測試評估

print("分群準確性:", km.inertia_)

# 分群準確性: 663.895238095238

s = []
for k in range(1, 15):
    km = KMeans(n_clusters=k)
    km.fit(df_X)
    s.append(km.inertia_)

print(s)

# [663.895238095238, 151.77145833333336, 77.91989035087718, 56.64237065018315, 45.816421929824564, 38.380978808131445, 34.1150969785575, 29.771330051212402, 27.730401211361738, 25.771261585636587, 24.236889472455648, 22.68941452991453, 21.258278047116285, 19.7686452991453]

# 看視覺化圖表決定參數K值
df_kmeans = pd.DataFrame()
df_kmeans["inertia_"] = s
df_kmeans.index = list(range(1, 15))
df_kmeans.plot(grid=True)
plt.show()

k = 3
km = KMeans(n_clusters=k)
km.fit(df_X)

print("分群的預測結果：")
pred = km.fit_predict(df_X)
print(pred)

# 決定模型
# 進行分群預測

df1 = df_X.copy()
df1["pred"] = pred

c = {0: "r", 1: "g", 2: "b"}

df1["colors"] = df1["pred"].map(c)
df1.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm", c=df1["colors"])

plt.show()

# 給一朵鳶尾花的4個特徵值：「花萼長度 6.6公分、花萼寬度 3.1公分、花瓣長度 5.2公分、花寬度 2.4公分」

new = [[6.6, 3.1, 5.2, 2.4]]

v = km.predict(new)

print("預測結果為：", v)

# 預測結果為： [0]

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("作業完成")
