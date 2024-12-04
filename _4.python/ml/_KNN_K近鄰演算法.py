"""
K-近鄰演算法（K Nearest Neighbor, KNN）

k是一個用戶定義的常數。
一個沒有類別標籤的向量（查詢或測試點）將被歸類為最接近該點的k個樣本點中最頻繁使用的一類。

簡單來說，我們要找出和新數據附近的K個鄰居（資料）
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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("make_blobs 產生測試資料")

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print("make_blobs 產生", N, "筆資料 2維 2群")
X, y = make_blobs(n_samples=N, n_features=2, centers=2, random_state=9487)

print(X.shape)
print(y.shape)
# print(X)
# print(y)

plt.subplot(121)
plt.scatter(X.T[0], X.T[1], c=y, cmap="Dark2")
plt.title("dx的分佈狀況, dy是用顏色表示")
plt.grid(True)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
dx_std = scaler.fit_transform(X)  # STD特徵縮放

plt.subplot(122)
plt.scatter(dx_std.T[0], dx_std.T[1], c=y, cmap="Dark2")
plt.title("經過 StandardScaler")
plt.grid(True)

show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(dx_std, y, test_size=0.2)
# 訓練組8成, 測試組2成

print(X.shape)
print(X_train.shape)
print(X_test.shape)

print(y.shape)
print(y_train.shape)
print(y_test.shape)

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print(y_test)

print("KNN準確率: %.2f" % knn.score(X_train, y_train))
print("KNN準確率: %.2f" % knn.score(X_test, y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.metrics import accuracy_score

X, y = make_moons(noise=0.3)
print("make_moons 未指定個數, 就是100個")
print(X.shape)
print(y.shape)
print(X)
print(y)

plt.scatter(X[:, 0], X[:, 1], s=50, c=y)
plt.show()

# NEIGHBOARS = 5
# print('用 K近鄰演算法 找出最近的', NEIGHBOARS, "個點")
# 無參數
knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果 :\n", y_pred)

print("評估")
print(accuracy_score(y_pred, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


""" TBD
print('最簡易 K近鄰演算法（K Nearest Neighbor, KNN）')

print('任意隨機資料')
X = np.random.rand(50, 2)

# 畫出來
plt.scatter(X[:, 0], X[:, 1], s=50)
show()




sys.exit()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = np.array(
    [
        [9, 9],
        [9.2, 9.2],
        [9.6, 9.2],
        [8.7, 8.0],
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
)
y = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

# 進行預測
X_sample = [8.1, 9.2]
X_sample = np.array(X_sample).reshape(1, -1)

y_pred = knn.predict(X_sample)  # 預測.predict
print("預測結果 :\n", y_pred)

print("預測答案＝", knn.predict([[8.1, 9.2]]))  # 預測.predict
print("預測樣本距離＝", knn.predict_proba([[8.1, 9.2]]))  #      測試數據X的返回概率估計。

neighbors = knn.kneighbors(X_sample, return_distance=False)
print(len(neighbors))
print(neighbors)

# plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
# plt.scatter(c[:, 0], c[:, 1], marker="*", s=200, c="r", alpha=0.8)  # 畫出中心點

plt.scatter(X_sample[0][0], X_sample[0][1], marker="x", s=100, cmap="cool")  # 待預測的點

print("劃出預測點與距離最近的", NEIGHBOARS, "個樣本的連線")
for i in neighbors[0]:
    print("(", X[i][0], ",", X[i][1], ")")
    plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], "r--", linewidth=0.6)
plt.title("KNN預測")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
# print(iris.feature_names)

X = iris.data
y = iris.target

# NEIGHBOARS = 3
# print('用 K近鄰演算法 找出最近的', NEIGHBOARS, "個點")
# 無參數
knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果 :\n", y_pred)

print("正確答案")
print(y)

print("KNN準確率: %.2f" % knn.score(X, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
# print(iris.feature_names)

X = iris.data
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

from sklearn.model_selection import cross_val_score

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
scores = cross_val_score(knn, X, y, cv=5, scoring="accuracy")
print(scores)

# this is how to use cross_val_score to choose model and configs #
from sklearn.model_selection import cross_val_score

k_scores = []
for k in range(1, 31):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    ##    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error') # for regression
    scores = cross_val_score(knn, X, y, cv=10, scoring="accuracy")  # for classification
    k_scores.append(scores.mean())
    print("取得 :", scores.mean())

plt.plot(range(1, 31), k_scores)
plt.xlabel("Value of K for KNN")
plt.ylabel("Cross-Validated Accuracy")

show()

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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=9487
)  # 訓練組8成, 測試組2成

# 從k值=1開始測試
NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

from sklearn.metrics import classification_report, confusion_matrix

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

error_rate = []

for i in range(1, 60):
    NEIGHBOARS = i
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
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

NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("WITH K=1")
print("\n")
print(confusion_matrix(y_test, y_pred))
print("\n")
print(classification_report(y_test, y_pred))

####待回復 ST

NEIGHBOARS = 10
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

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

print("KNN準確率: %.2f" % knn.score(X_test, y_test))  # 是不是應該要用 y_pred??

"""
0.9675010979358806
與前次相比，KNN的準確率 從0.9287356321839081變成0.9675010979358806
前次資料1448筆 本次資料15179筆
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 20190314-空氣盒子數據Scikit-Learn K相鄰演算法實作

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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.30, random_state=9487
)  # 訓練組8成, 測試組2成

# 從k值=1開始測試
NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

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
    NEIGHBOARS = i
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
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

NEIGHBOARS = 7
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

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

print("KNN準確率: %.2f" % knn.score(X_test, y_test))  # 是不是應該要用 y_pred??

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

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8, random_state=9487
)  # 訓練組8成, 測試組2成

# 上述过程有没有问题？

# * 建模
from sklearn.neighbors import KNeighborsClassifier

NEIGHBOARS = 3
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # 默認歐氏距離

knn.fit(X_train, y_train.values.flatten())

test_est = knn.predict(X_test)

import sklearn.metrics as metrics

print(metrics.confusion_matrix(y_test, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(y_test, test_est))

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

# * 选择k值

for k in range(1, 30):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    knn.fit(X_train, y_train.values.flatten())
    score = knn.score(X_test, y_test)
    print("KNN準確率: %.2f" % knn.score(X_test, y_test))


# * 交叉验证选择k值

from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold

import sklearn

print(help(sklearn.model_selection.KFold()))

n_samples = len(X_train)
kf = KFold(n_samples)
grid = {"n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9]}
estimator = KNeighborsClassifier()
gridSearchCV = GridSearchCV(estimator, grid, cv=kf)
gridSearchCV.fit(X_train, y_train.values.flatten())
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
best.score(X_test, y_test)

# 练习：试一试哪些参数会影响结果

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("KNeighborsRegressor")

# 生成訓練樣本
N = 40
X = 5 * np.random.rand(N, 1)
y = np.cos(X).ravel()

# 添加一些噪聲
y += 0.2 * np.random.rand(N) - 0.1

NEIGHBOARS = 5
print("用 KNeighborsRegressor 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsRegressor(NEIGHBOARS)

knn.fit(X, y)  # 學習訓練.fit

# 生成足夠密集的點并進行預測
T = np.linspace(0, 5, 500)[:, np.newaxis]

y_pred = knn.predict(T)  # 預測.predict
print("預測結果 :\n", y_pred)

print("KNN準確率: %.2f" % knn.score(X, y))

# 畫出擬合曲線
plt.scatter(X, y, c="g", label="data", s=100)  # 畫出訓練樣本
plt.plot(T, y_pred, c="k", label="prediction", lw=4)  # 畫出擬合曲線
plt.title("KNeighborsRegressor (NEIGHBOARS = %i)" % NEIGHBOARS)
plt.axis("tight")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


# os.chdir(r'D:\Python_book\11KNNNB')
# pd.set_option('display.max_columns', None)


print("------------------------------------------------------------")  # 60個
