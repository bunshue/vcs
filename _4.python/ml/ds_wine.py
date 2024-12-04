"""
紅酒資料集

#範例16-1:邏輯斯模型(logistic regression model，羅吉斯):分類，二分法類器
# 題目：預測3種意大利紅酒，將資料集分成train,test，先學習再預測，用3種指標來評估預測績效（決定係數R2，MAE，殘差圖）

#重點1：邏輯斯模型的應用性：
#羅吉斯迴歸現在已經被大量使用，因為它非常有效率，也不需要大量運算資源，所以受到廣泛利用。它很容易解讀，不需要調整輸入特徵，也易於正規化，而且它所提供的輸出結果是經過良好校正的預測機率。
#應用1：衛生保健：例如預測受傷患者的死亡率。預測糖尿病和心臟病等疾病的發病率。
#應用2：政治:可用於預測選舉。這些預測是根據年齡、性別、居住地、社會地位、過往投票模式等變數，產生投票結果預測。
#應用3：產品測試：預測測試中系統或產品的成敗。
#應用4：行銷：可用於預測客戶詢價轉化為銷售的機率、訂閱開始或終止的機率，甚至是客戶對新產品系列的潛在興趣。
#應用5：金融業：可預測客戶未來遲繳的可能性，可以看出某位客戶是否會「違約」或「不違約」
#應用6：電子商務：電子商務公司大量投資於跨媒體廣告和促銷活動，很希望了解哪些活動最有效，以及最可能獲得潛在目標受眾響應的選項。此模型集將客戶分類為「反應者」或「非反應者」，所以此模型稱為「反應傾向模型」。

#重點2：邏輯斯模型的預測數字：
#結果：0～1
#判別：0為否，1為是

#重點3：讀取sklearn的dataset，有2種做法：

#（1）方法1：
data, target = ds.load_wine(return_X_y=True)
import sklearn.model_selection as ms
train_x, test_x, train_y, test_y = ms.train_test_split(data, target, test_size=0.2)

#（2）方法2：
wine = ds.load_wine()
import sklearn.model_selection as ms
train_x, test_x, train_y, test_y = ms.train_test_split(wine.data, wine.target, test_size=0.2)


葡萄酒數據集/紅酒資料庫
Classes          3
Sample per class 59/71/48(共178筆資料)
Samples total    178
Dimensionality    13
Features         real, positive


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

from sklearn import datasets
from sklearn.datasets import load_wine

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("葡萄酒數據集")

data = load_wine()
cc = data.target[[10, 80, 140]]
print(cc)
# array([0, 1, 2])

print("data.data.shape, 數據集資料 形狀")
print(data.data.shape)

print("data.feature_names, 數據集 欄位 的名稱 ")
print(data.feature_names)
print("data.target, target 類的名稱, 分類結果, 就是等級 0 1 2")
print(data.target)
print("data.target_names, target 類的名稱")
print(data.target_names)
print("data.frame")
print(data.frame)
""" many
print("data.DESCR, 數據集的完整描述")
print(data.DESCR)
print("data")
print(data)
"""

# data.feature_names, 數據集 列 的名稱
cc = data.data[:, [0]]  # alcohol
cc = data.data[:, [1]]  # malic_acid
cc = data.data[:, [2]]  # ash
cc = data.data[:, [3]]  # alcalinity_of_ash
cc = data.data[:, [4]]  # magnesium
cc = data.data[:, [5]]  # total_phenols
cc = data.data[:, [6]]  # flavanoids
cc = data.data[:, [7]]  # nonflavanoid_phenols
cc = data.data[:, [8]]  # proanthocyanins
cc = data.data[:, [9]]  # color_intensity
cc = data.data[:, [10]]  # hue
cc = data.data[:, [11]]  # od280/od315_of_diluted_wines
cc = data.data[:, [12]]  # proline

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 支持向量機

from sklearn import svm
from sklearn.model_selection import train_test_split

wine = datasets.load_wine()

X = wine.data
y = wine.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = svm.SVC(gamma=0.001, decision_function_shape="ovo")
clf.fit(X_train, y_train)

dec = clf.decision_function(X_test)
cc = dec.shape[1]  # n_class * (n_class - 1) / 2 =  3*2/2 = 3
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = load_wine()

x3 = data.data[:, [0]]  # alcohol
y3 = data.data[:, [9]]  # color_intensity

plt.subplot(121)
plt.scatter(x3, y3)

plt.subplot(122)
plt.hist(y3, bins=50)

plt.suptitle("wine")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = load_wine()
df_X = pd.DataFrame(data.data, columns=data.feature_names)
print(df_X.head())

df_y = pd.DataFrame(data.target, columns=["kind(target)"])
print(df_y.head())

df = pd.concat([df_X, df_y], axis=1)
print(df.head())

plt.subplot(121)
plt.hist(df.loc[:, "alcohol"])

plt.subplot(122)
plt.boxplot(df.loc[:, "alcohol"])

plt.show()

print(df.corr())
print(df.describe())

print("------------------------------")  # 30個

print("使用 scatter_matrix")
from pandas.plotting import scatter_matrix

_ = scatter_matrix(df, figsize=(15, 15))
plt.show()

_ = scatter_matrix(df.iloc[:, [0, 9, -1]])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ読み込み
data = load_wine()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3
)
model = RandomForestClassifier()
model.fit(X_train, y_train)  # 學習
y_pred = model.predict(X_test)
print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# k-fold 交叉驗證法

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_wine(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

val_score = cross_val_score(forest, dx_train, dy_train, cv=5)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(val_score.mean().round(3))

print(forest.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 產生預測結果報告

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

dx, dy = load_wine(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

forest = RandomForestClassifier()

forest.fit(dx_train, dy_train)

predictions = forest.predict(dx_test)

print(forest.score(dx_train, dy_train).round(3))

print(forest.score(dx_test, dy_test).round(3))

print(classification_report(dy_test, predictions))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
讀入葡萄酒品種分類資料集
資料集 = dataset
"""

import sklearn.datasets as ds

wine = ds.load_wine()

# 先看資料集的keys:

"""
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

# 看wine資料集的keys：
cc = wine.keys()
print(cc)

print(wine.data.shape)
print(wine.target.shape)

# data(特徵資料)的內容
print(wine.data)


# data(特徵資料（各種變數x1,x2,x3....）)總共幾筆
print(wine.data.shape)

# (178, 13)

# target：wine葡萄酒品種的目標值
print(wine.target)

# target：葡萄酒品種，總共幾筆
print(wine.target.shape)

"""
4.練習4：看看各種影響酒品質的各種因素（欄位名稱）
feature_names：特徵名稱
注意：data特徵資料的13個欄位名稱 = feature_names特徵名稱
注意：data特徵資料的13個欄位數據 = data
"""
cc = wine.feature_names
print(cc)

"""
wine的數據有13種特徵欄位，而每個特徵變數有的意義分別為：
1.alcohol: 酒精濃度
2.malic acid：蘋果酸
3.ash：灰
4.alcalinity of ash：灰的鹼度
5.magnesium：鎂
6.total phenols：總酚
7.flavanoids：黃酮類化合物
8.nonflavanoid phenols：非黃烷類酚類
9.proanthocyanins：原花青素
10.color intensity：色彩強度
11.hue：色調
12.OD280/OD315 of diluted wines：稀釋酒
13.proline：脯氨酸
"""

# 5.練習5：把data資料轉成pandas的dataframe數據格式（變數df_x）

df_x = pd.DataFrame(wine.data, columns=wine.feature_names)

c1 = [
    "酒精濃度",
    "蘋果酸",
    "灰",
    "灰的鹼度",
    "鎂",
    "總酚",
    "黃酮類化合物",
    "非黃烷類酚類",
    "原花青素",
    "色彩強度",
    "色調",
    "稀釋酒",
    "脯氨酸",
]

# 設定英文欄位
import pandas as pd

df_x = pd.DataFrame(wine.data, columns=wine.feature_names)
print(df_x)


# 設定中文欄位
c1 = [
    "酒精濃度",
    "蘋果酸",
    "灰",
    "灰的鹼度",
    "鎂",
    "總酚",
    "黃酮類化合物",
    "非黃烷類酚類",
    "原花青素",
    "色彩強度",
    "色調",
    "稀釋酒",
    "脯氨酸",
]
df_x = pd.DataFrame(wine.data, columns=c1)
print(df_x)


"""
#6.練習6：把target資料轉換成pandas數據dataframe格式（種類df_y）

df_y = pd.DataFrame(boston.target, columns=['種類'])
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

df_y = pd.DataFrame(wine.target, columns=["種類"])
print(df_y)

"""
#7.練習7：建立線性迴歸的模型sklearn model方法：（3步驟）
#1.步驟1：先建立數學模型(邏輯斯模型logistic regression model)

import sklearn.linear_model as lm

model = lm.LinearRegression())

#2.步驟2：讓模型model學習歷史數據

學習指令：model.fit(dataframeX, dataframeY)

3.步驟3：讓模型model進行預測

使用test_x進行預測=pred_y

然後比較實際數值test_y, 與pred_y的差異

指令：model.predict(test_X)

注意：t1,t2必須要是dataframe

t1 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

t2 =[[13.53, 4.10, 2.74, 24.5, 96.0, 2.05, 0.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
winde.target，有三種酒類
值：0：代表Barolo酒
值：1：代表Grignolino酒
值：2：代表Barbera酒
"""

# 1.步驟1：先建立數學模型(邏輯斯模型logistic regression model)
import sklearn.linear_model as lm

model = lm.LogisticRegression()

# 2.步驟2：讓模型model學習歷史數據
model.fit(df_x, df_y)

# 3.步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[6]==>黃酮類化合物==>3.76
print("預測這個紅酒A的酒種：")
t1 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
model.predict(t1)

# 數據差別在[6]==>黃酮類化合物==>0.76
print("預測這個紅酒B的酒種：")
t2 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 0.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
# t1 =[[13.53,   3.10,   2.74,   24.5,   96.0,   2.05,   3.76,   0.56,   1.35,   9.20,   0.61,   1.60,   560.0]]
model.predict(t2)

"""
8.練習8：畫圖，黃酮類化合物 vs 酒種
畫圖的方式有2種
方法（1）使用df.plot(x="欄位", y="欄位", kind="scatter")
方法（2）使用plt.scatter(x=df[欄位], y=df[欄位])
數據點

t1 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

預測：t1-->model.predict(t1)

但是畫圖（黃酮類化合物 vs 酒種)

所以畫點（x = t1[0][6] ==> 黃酮類化合物 ==> 3.76)

但是預測值，還是（y = model.predict(t1))

plt.scatter(t1[0][6], model.predict(t1), label="預測紅酒A",color="red")
"""

plt.scatter(df_x["黃酮類化合物"], df_y, label="實際數據")
plt.scatter(t1[0][6], model.predict(t1), label="預測紅酒A", color="red")
plt.scatter(t2[0][6], model.predict(t2), label="預測紅酒B", color="orange")

plt.legend()
plt.xlabel("黃酮類化合物")
plt.ylabel("酒種")
plt.title("畫圖，黃酮類化合物 vs 酒種")
plt.show()

"""
9.結論(1)：黃酮類化合物，不是影響酒種的關鍵因素
10.練習10：測試，不同『脯氨酸』是否是影響酒種的關鍵因素
步驟3：讓模型model進行預測:model.predict(dataframe())
數據差別在[12]==>脯氨酸==>1560.0

預測這個紅酒C的酒種：

t3 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 1560.0]]
數據差別在[12]==>脯氨酸==>560.0

預測這個紅酒D的酒種：

t4 =[[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]

model.predict(t1)
"""

from pickle import TUPLE3

# (1).步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[12]==>脯氨酸==>1560.0
print("預測這個紅酒C的酒種：")
t3 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 1560.0]]
model.predict(t3)


# (2).步驟3：讓模型model進行預測:model.predict(dataframe())
# 數據差別在[12]==>脯氨酸==>560.0
print("預測這個紅酒D的酒種：")
t4 = [[13.53, 3.10, 2.74, 24.5, 96.0, 2.05, 3.76, 0.56, 1.35, 9.20, 0.61, 1.60, 560.0]]
model.predict(t4)


plt.scatter(df_x["脯氨酸"], df_y, label="實際數據")
plt.scatter(t3[0][12], model.predict(t3), label="預測紅酒C", color="red")
plt.scatter(t4[0][12], model.predict(t4), label="預測紅酒D", color="orange")

plt.legend()
plt.xlabel("脯氨酸")
plt.ylabel("酒種")
plt.title("畫圖，脯氨酸 vs 酒種")
plt.show()

# 11.結論(2)：脯氨酸，是影響酒種的關鍵因素

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

ds = datasets.load_wine()

print("資料集說明")
print(ds.DESCR)

print("資料集的特徵(X)")

df = pd.DataFrame(ds.data, columns=ds.feature_names)
print(df)

print("資料集的目標(Y)")
print(ds.target)

print("目標(Y)的名稱，即標註(Label)")
print(ds.target_names)

print("觀察資料集彙總資訊")

df.info()  # 這樣就已經把資料集彙總資訊印出來

print("描述統計量")
cc = df.describe()
print(cc)

print("另一種載入資料集的方法")

X, y = datasets.load_wine(return_X_y=True)
print(X)
print(y)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_wine

data = load_wine()

X = data.data[:, [0, 9]]

CLUSTERS = 3  # 要分成的群數
clf = KMeans(n_clusters=CLUSTERS)  # K-平均演算法

pred = clf.fit_predict(X)  # 學習訓練 + 預測 .fit_predict

fig, ax = plt.subplots()
ax.scatter(X[pred == 0, 0], X[pred == 0, 1], color="red", marker="s", label="Label1")
ax.scatter(X[pred == 1, 0], X[pred == 1, 1], color="blue", marker="s", label="Label2")
ax.scatter(X[pred == 2, 0], X[pred == 2, 1], color="green", marker="s", label="Label3")
ax.scatter(
    clf.cluster_centers_[:, 0],
    clf.cluster_centers_[:, 1],
    s=200,
    color="yellow",
    marker="*",
    label="center",
)
ax.legend()
plt.title("wine")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
