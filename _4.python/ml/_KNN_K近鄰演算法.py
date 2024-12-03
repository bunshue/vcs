"""
K相鄰

K-近鄰演算法（K Nearest Neighbor）

k是一個用戶定義的常數。
一個沒有類別標籤的向量（查詢或測試點）將被歸類為最接近該點的k個樣本點中最頻繁使用的一類。

簡單來說，我們要找出和新數據附近的K個鄰居（資料），
這些鄰居是哪一類（標籤）的它就是哪一類的啦。

knn演算法，是機器學習中較好理解的一個演算法，是透過找出附近鄰居的分類定義來自己的類別，
並用sklearn輕易的完成這個機器學習的演算法。
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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from common1 import *
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor, KNN）
from sklearn.neighbors import KNeighborsRegressor

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

"""
2019.01.02 更新 ：
由於 sklearn.cross_validation 方法要被棄用了，所以必須改成 sklearn.model_selection。
"""
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# 定義特徵資料：
iris_data = iris.data
iris_label = iris.target

# 可以印出前三筆資料：
cc = iris_data[0:3]
print(cc)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
train_data, test_data, train_label, test_label = train_test_split(
    iris_data, iris_label, test_size=0.2
)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(train_data, train_label)  # 學習訓練.fit

y_pred = knn.predict(test_data)  # 預測.predict
print("預測結果 :\n", y_pred)

print("正確答案")
print(test_label)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("make_blobs 產生測試資料")

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print("make_blobs 產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=9487)

print(dx.shape)
print(dy.shape)
# print(dx)
# print(dy)

plt.subplot(121)
plt.scatter(dx.T[0], dx.T[1], c=dy, cmap="Dark2")
plt.title("dx的分佈狀況, dy是用顏色表示")
plt.grid(True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
dx_std = scaler.fit_transform(dx)  # STD特徵縮放

plt.subplot(122)
plt.scatter(dx_std.T[0], dx_std.T[1], c=dy, cmap="Dark2")
plt.title("經過 StandardScaler")
plt.grid(True)

show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)
# 訓練組8成, 測試組2成

print(dx.shape)
print(dx_train.shape)
print(dx_test.shape)

print(dy.shape)
print(dy_train.shape)
print(dy_test.shape)

knn = KNeighborsClassifier(n_neighbors=5)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(dx_train, dy_train)  # 學習訓練.fit

y_pred = knn.predict(dx_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print(dy_test)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

X, y = make_moons(noise=0.3)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

# 評估
print(accuracy_score(y_pred, y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("K-近鄰演算法（K Nearest Neighbor, KNN）")

X = pd.DataFrame({"耐酸性": [7, 7, 3, 1], "強度": [7, 4, 4, 4]})

y = np.array([0, 0, 1, 1])
k = 3

knn = KNeighborsClassifier(n_neighbors=k)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

# 預測新產品[3,7]的分類 1:好 0:壞
new_tissue = pd.DataFrame(np.array([[3, 7]]), columns=["耐酸性", "強度"])

y_pred = knn.predict(new_tissue)  # 預測.predict
print("預測結果 :\n", y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 60
print("make_blobs 產生", N, "筆資料, 指定3個中心點, 預設2維")
# 生成數據, 3群, 指定中心點
centers = [[-2, 2], [2, 2], [0, 4]]
X, y = make_blobs(n_samples=N, centers=centers, random_state=9487, cluster_std=0.60)

# 畫出數據
c = np.array(centers)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 畫出樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="orange")  # 畫出中心點

show()

k = 5
knn = KNeighborsClassifier(n_neighbors=k)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

# 進行預測
X_sample = [0, 2]
X_sample = np.array(X_sample).reshape(1, -1)

y_pred = knn.predict(X_sample)  # 預測.predict
print("預測結果 :\n", y_pred)

neighbors = knn.kneighbors(X_sample, return_distance=False)

# 畫出示意圖
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="k")  # 中心點
plt.scatter(X_sample[0][0], X_sample[0][1], marker="x", s=100, cmap="cool")  # 待預測的點

for i in neighbors[0]:
    # 預測點與距離最近的 5 個樣本的連線
    plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], "k--", linewidth=0.6)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 生成訓練樣本
N = 40
X = 5 * np.random.rand(N, 1)
y = np.cos(X).ravel()

# 添加一些噪聲
y += 0.2 * np.random.rand(N) - 0.1

k = 5
knn = KNeighborsRegressor(k)
knn.fit(X, y)  # 學習訓練.fit

# 生成足夠密集的點并進行預測
T = np.linspace(0, 5, 500)[:, np.newaxis]

y_pred = knn.predict(T)  # 預測.predict
print("預測結果 :\n", y_pred)

# 評估
print(knn.score(X, y))

# 畫出擬合曲線
plt.scatter(X, y, c="g", label="data", s=100)  # 畫出訓練樣本
plt.plot(T, y_pred, c="k", label="prediction", lw=4)  # 畫出擬合曲線
plt.title("KNeighborsRegressor (k = %i)" % k)
plt.axis("tight")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

iris_X = iris.data
iris_y = iris.target

print(iris_X[:2, :])
print(iris_y)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.2)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = iris.data
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

# 評估
print(knn.score(X_test, y_test))

""" some NG
from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=5, scoring="accuracy")
print(scores)

# this is how to use cross_val_score to choose model and configs #
from sklearn.model_selection import cross_val_score

k_range = range(1, 31)
k_scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    ##    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error') # for regression
    scores = cross_val_score(knn, X, y, cv=10, scoring="accuracy")  # for classification
    k_scores.append(scores.mean())

plt.plot(k_range, k_scores)
plt.xlabel("Value of K for KNN")
plt.ylabel("Cross-Validated Accuracy")
show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
機器學習_K-近鄰演算法_空氣盒子
"""

df = pd.read_excel("data/20160101-20190101(Daily)K相鄰.xlsx")
"""
cc = df.head(10)
print(cc)

#資料長度
print(len(df))
print(len(df["PM25"]))

df.info()  # 這樣就已經把資料集彙總資訊印出來

cc = df.describe()
print(cc)
"""
print(df.keys())
print(df.shape)

# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

cc = df.isnull().any()
print(cc)

from sklearn.preprocessing import StandardScaler

# 將Danger中特徵中移除，作為要預測的對象
scaler = StandardScaler()
scaler.fit(df.drop("Danger", axis=1))
scaled_features = scaler.transform(df.drop("Danger", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

X = df_feat
y = df["Danger"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=101
)

# 從k值=1開始測試
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

error_rate = []

for i in range(1, 60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)  # 學習訓練.fit
    pred_i = knn.predict(X_test)  # 預測.predict
    error_rate.append(np.mean(pred_i != y_test))


# 將k=1~60的錯誤率製圖畫出。k=7之後，錯誤率就往上跑，
plt.figure(figsize=(10, 6))
plt.plot(
    range(1, 60),
    error_rate,
    color="blue",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=10,
)
plt.title("Error Rate vs. K Value")
plt.xlabel("K")
plt.ylabel("Error Rate")

show()

print("------------------------------")  # 30個

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("WITH K=1")
print("\n")
print(confusion_matrix(y_test, y_pred))
print("\n")
print(classification_report(y_test, y_pred))

####待回復 ST

knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("WITH K=10")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

cc = df.head(1)
print(cc)

# 0:Safe   對一般人無害
# 1:Danger 對敏感族群有害
classes = {0: "Safe", 1: "Danger"}

# 建立一筆新資料並進行預測
x_new = [[4, 0.3, 25, 10, 15, 22, 2.2, 20, 2.3, 0.3, 2.3, 2, 20, 60]]
y_pred = knn.predict(x_new)  # 預測.predict
print("預測結果 :\n", y_pred)
print(classes[y_pred[0]])

# Danger

classes = {0: "Safe", 1: "Danger"}

x_new = [[1, 0.3, 1, 1, 1, 2, 1, 1, 1, 0.1, 1, 0.5, 30, 50]]
y_pred = knn.predict(x_new)  # 預測.predict
print("預測結果 :\n", y_pred)
print(classes[y_pred[0]])

# Safe
print("評估KNN的準確率")
cc = knn.score(X_test, y_test)  # 是不是應該要用 y_pred??
print(cc)

"""
0.9675010979358806
與前次相比，KNN的準確率 從0.9287356321839081變成0.9675010979358806
前次資料1448筆 本次資料15179筆
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
20190314-空氣盒子數據Scikit-Learn K相鄰演算法實作
"""
df = pd.read_csv("data/200811-201811c.csv")  # 共有 1447 筆資料
cc = df.head(10)
print(cc)

# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上
# 載入標準化比例尺（StandardScaler）套件

from sklearn.preprocessing import StandardScaler

# 將Danger中特徵中移除，作為要預測的對象
scaler = StandardScaler()
scaler.fit(df.drop("Danger", axis=1))  # 刪除 "Danger" 這一欄的資料
scaled_features = scaler.transform(df.drop("Danger", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

X = df_feat
y = df["Danger"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=9487
)

# 從k值=1開始測試
knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

# 使用混淆矩陣
from sklearn.metrics import classification_report, confusion_matrix

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))
print("classification_report")
print(classification_report(y_test, y_pred))

# 利用 For迴圈，選擇K值

error_rate = []

for i in range(1, 60):
    print("選擇K值 :", i)
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)  # 學習訓練.fit
    pred_i = knn.predict(X_test)  # 預測.predict
    error_rate.append(np.mean(pred_i != y_test))

print("錯誤率 :", error_rate)

# 將k=1~60的錯誤率製圖畫出。k=23之後，錯誤率就在5%-6%之間震盪，
plt.figure(figsize=(12, 6))
plt.plot(
    range(1, 60),
    error_rate,
    color="blue",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=10,
)
plt.xlabel("K")
plt.ylabel("Error Rate")
plt.title("Error Rate vs. K Value")

show()

print("選擇 K值 = 7")

knn = KNeighborsClassifier(n_neighbors=7)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))
print("classification_report")
print(classification_report(y_test, y_pred))

# 顯示所有特徵

cc = df.head(1)
print(cc)

# 所有特徵

# 給與一筆數值，進行預測(Danger)

classes = {0: "Safe", 1: "Danger"}

x_new = [[4, 0.3, 25, 15, 22, 2.2, 20, 2.3, 0.3, 2.3, 2, 20, 60]]
y_pred = knn.predict(x_new)  # 預測.predict
print("預測結果 :\n", y_pred)
print(classes[y_pred[0]])

# Danger

# 給與一筆數值，進行預測(Safe)

classes = {0: "Safe", 1: "Danger"}

x_new = [[1, 0.3, 1, 1, 2, 1, 1, 1, 0.1, 1, 0.5, 30, 50]]
y_pred = knn.predict(x_new)  # 預測.predict
print("預測結果 :\n", y_pred)
print("Safe 或 Danger ?")
print(classes[y_pred[0]])

# Safe
print("評估KNN的準確率")
cc = knn.score(X_test, y_test)  # 是不是應該要用 y_pred??
print(cc)
# 0.9287356321839081

####待回復

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.plot([9, 9.2, 9.6, 9.2, 6.7, 7, 7.6], [9.0, 9.2, 9.2, 9.2, 7.1, 7.4, 7.5], "yx")
plt.plot(
    [7.2, 7.3, 7.2, 7.3, 7.2, 7.3, 7.3], [10.3, 10.5, 9.2, 10.2, 9.7, 10.1, 10.1], "g."
)
plt.plot([7], [9], "r^")

circle1 = plt.Circle((7, 9), 1.2, color="#aaaaaa")
plt.gcf().gca().add_artist(circle1)
plt.axis([6, 11, 6, 11])


plt.ylabel("H cm")
plt.xlabel("W cm")
plt.legend(("Orange", "Lemons"), loc="upper right")
show()

print("------------------------------------------------------------")  # 60個

# 02-kNN-Lemon.py

X = [
    [9, 9],
    [9.2, 9.2],
    [9.6, 9.2],
    [9.2, 9.2],
    [6.7, 7.1],
    [7, 7.4],
    [7.6, 7.5],
    [7.2, 10.3],
    [7.3, 10.5],
    [7.2, 9.2],
    [7.3, 10.2],
    [7.2, 9.7],
    [7.3, 10.1],
    [7.3, 10.1],
]
y = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

knn = KNeighborsClassifier(n_neighbors=3)

knn.fit(X, y)  # 學習訓練.fit

print("預測答案＝", knn.predict([[7, 9]]))  # 預測.predict
print("預測樣本距離＝", knn.predict_proba([[7, 9]]))  #      測試數據X的返回概率估計。

print("------------------------------------------------------------")  # 60個

# 03-Iris.py

iris = datasets.load_iris()

print("iris.data.shape=", iris.data.shape)
print("dir(iris)", dir(iris))
print("iris.target.shape=", iris.target.shape)
try:
    print("iris.feature_names=", iris.feature_names)
except:
    print("No iris.feature_names=")

import xlsxwriter

try:
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
except:
    df = pd.DataFrame(
        iris.data,
        columns=[
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )

df["target"] = iris.target

print(df.head())
df.to_csv("tmp_iris.csv", sep="\t")

""" no save
writer = pd.ExcelWriter("tmp_iris.xlsx", engine="xlsxwriter")
df.to_excel(writer, sheet_name="Sheet1")
writer.save()
"""

print("------------------------------------------------------------")  # 60個

# 04-Iris-KNN.py

iris = datasets.load_iris()

iris_X_train, iris_X_test, iris_y_train, iris_y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)

knn = KNeighborsClassifier()

knn.fit(iris_X_train, iris_y_train)  # 學習訓練.fit

print("預測", knn.predict(iris_X_test))  # 預測.predict
print("實際", iris_y_test)

print("準確率: %.2f" % knn.score(iris_X_test, iris_y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from scipy import stats
import sklearn.model_selection as cross_validation

orgData = pd.read_csv("data/date_data.csv")
orgData.describe()

# * 选取自变量

print(orgData.shape)
print(orgData.head())


# 取出後4欄位當訓練資料
# X = orgData.ix[:, :4]
print("取出3欄資料")
X = orgData[["income_rank", "attractive_rank", "assets_rank"]]

# 取出 Dated 欄位 當訓練目標
Y = orgData[["Dated"]]
X.head()

# * 极值标准化

from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)
X_scaled[1:5]

# * 划分训练集和测试集

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8, random_state=123
)  # 划分训练集和测试集


# 上述过程有没有问题？

# * 建模
from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)  # 默认欧氏距离
model.fit(train_data, train_target.values.flatten())
test_est = model.predict(test_data)

import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(test_target, test_est))

model.score(test_data, test_target)

# * 选择k值

for k in range(1, 30):
    k_model = KNeighborsClassifier(n_neighbors=k)
    k_model.fit(train_data, train_target.values.flatten())
    score = k_model.score(test_data, test_target)
    print(k, "\t", score)


# * 交叉验证选择k值

from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold

import sklearn

print(help(sklearn.model_selection.KFold()))

n_samples = len(train_data)
kf = KFold(n_samples)
grid = {"n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9]}
estimator = KNeighborsClassifier()
gridSearchCV = GridSearchCV(estimator, grid, cv=kf)
gridSearchCV.fit(train_data, train_target.values.flatten())
cc = gridSearchCV.cv_results_  # cv_results_ : 具體用法模型不同參數下交叉驗證的結果
print(cc)

mean_test_score = gridSearchCV.cv_results_["mean_test_score"]
std_test_score = gridSearchCV.cv_results_["std_test_score"]
rank_test_score = gridSearchCV.cv_results_["rank_test_score"]

print("mean_test_score : ", mean_test_score)
print("std_test_score : ", std_test_score)
print("rank_test_score : ", rank_test_score)

gridSearchCV.best_params_

best = gridSearchCV.best_estimator_
best.score(test_data, test_target)

# 练习：试一试哪些参数会影响结果

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


# os.chdir(r'D:\Python_book\11KNNNB')
# pd.set_option('display.max_columns', None)
