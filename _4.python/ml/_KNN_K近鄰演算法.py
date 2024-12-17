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

import joblib
from common1 import *
from sklearn import datasets
from sklearn import preprocessing  # 極值標準化
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score  # 計算準確率
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor, KNN）
from sklearn.neighbors import KNeighborsRegressor


def show():
    plt.show()
    pass


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

print("make_moons 未指定個數, 就是100個")
X, y = make_moons(noise=0.3)

print("自己建立資料")
X = np.array(
    [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [1, 0],
        [1, 1],
        [1, 2],
        [1, 3],
        [1, 4],
        [2, 0],
        [2, 1],
        [2, 2],
        [2, 3],
        [2, 4],
        [3, 0],
        [3, 1],
        [3, 2],
        [3, 3],
        [3, 4],
        [4, 0],
        [4, 1],
        [4, 2],
        [4, 3],
        [4, 4],
    ]
)
y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3]

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
# knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）
knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）
# 無參數就是n_neighbors=5

N = 5
scores = cross_val_score(knn, X, y, cv=N, scoring="accuracy")
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print("全部分數 :", scores)
print("平均分數 :", scores.mean())

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果 :\n", y_pred)

print("計算準確率 :", accuracy_score(y_pred, y))

print("正確答案 :\n", y)

print("KNN準確率: %.2f" % knn.score(X, y))

"""
#測試y與y_pred
plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100)
plt.title('原始資料')
plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=y_pred, s=100)
plt.title('預測結果')
show()
"""

# 預測
x = [2.5, 2.5]
xx = np.array(x).reshape(1, -1)

y_pred = knn.predict(xx)  # 預測.predict
print("預測結果 :", y_pred)

y_pred = knn.predict([x])  # 預測.predict
print("預測答案 :", y_pred)
print("預測樣本距離 :", knn.predict_proba([x]))  # 測試數據X的返回概率估計

neighbors = knn.kneighbors(xx, return_distance=False)
print("找到的", NEIGHBOARS, "個點 :", neighbors)

# 原始資料
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")
# plt.scatter(X[:, 0], X[:, 1], c=y, s=100)

# 畫出預測點 紅星
plt.scatter(x[0], x[1], marker="*", s=200, c="r", alpha=0.8, cmap="cool")  # 待預測的點

print("劃出預測點與距離最近的", NEIGHBOARS, "個樣本的連線")
for i in neighbors[0]:
    print("第", i, "點 (", X[i][0], ",", X[i][1], ")")
    plt.plot([X[i][0], x[0]], [X[i][1], x[1]], "r--", linewidth=1.2)
plt.title("KNN預測")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

scaler = StandardScaler()
X_std = scaler.fit_transform(X)  # STD特徵縮放, 標準化

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="bwr")
# plt.scatter(X.T[0], X.T[1], c=y, cmap="Dark2")
plt.grid(True)
plt.title("原始資料")

plt.subplot(122)
plt.scatter(X_std[:, 0], X_std[:, 1], c=y, cmap="bwr")
# plt.scatter(X_std.T[0], X_std.T[1], c=y, cmap="Dark2")
plt.grid(True)
plt.title("特徵縮放 StandardScaler\n平均值0 標準差1")
show()

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果 :\n", y_pred)

print("正確答案 :\n", y)

print("KNN準確率: %.2f" % knn.score(X, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
X = iris.data
y = iris.target

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果 :\n", y_pred)

print("KNN準確率: %.2f" % knn.score(X, y))

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

N = 5
scores = cross_val_score(knn, X, y, cv=5, scoring="accuracy")
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print("全部分數 :", scores)
print("平均分數 :", scores.mean())

# this is how to use cross_val_score to choose model and configs #
from sklearn.model_selection import cross_val_score

k_scores = []
for k in range(1, 31):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    ##    loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error') # for regression
    N = 10
    scores = cross_val_score(knn, X, y, cv=N, scoring="accuracy")  # for classification
    print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
    k_scores.append(scores.mean())
    print("取得 :", scores.mean())

plt.plot(range(1, 31), k_scores)
plt.xlabel("Value of K for KNN")
plt.ylabel("Cross-Validated Accuracy")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

Ks = np.arange(1, round(0.2 * len(X) + 1))
accuracies = []
for k in Ks:
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    knn.fit(X, y)  # 學習訓練.fit
    accuracy = knn.score(X, y)  # KNN準確率
    accuracies.append(accuracy)

plt.plot(Ks, accuracies)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

NEIGHBOARS = 3
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X, y)  # 學習訓練.fit

print("KNN準確率: %.2f" % knn.score(X, y))
print("---------------------------")
y_pred = knn.predict(X)  # 預測.predict
print(y_pred)
print("---------------------------")
print(y.values)
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import cross_val_score

iris = datasets.load_iris()

X = pd.DataFrame(iris.data, columns=iris.feature_names)
X.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
target = pd.DataFrame(iris.target, columns=["target"])
y = target["target"]

Ks = np.arange(1, round(0.2 * len(X) + 1))
accuracies = []
for k in Ks:
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    N = 10
    scores = cross_val_score(knn, X, y, cv=N, scoring="accuracy")
    print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
    accuracies.append(scores.mean())

plt.plot(Ks, accuracies)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立模型, 儲存模型, 使用模型")

iris = datasets.load_iris()
X = iris.data
y = iris.target

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X, y)  # 學習訓練.fit

print("將 模型存檔 使用 joblib")
joblib.dump(knn, "tmp_my_model_iris.joblib")

print("------------------------------")  # 60個

print("讀取模型, 預測")
iris = datasets.load_iris()
X = iris.data
y = iris.target

print("讀取模型")
knnmodel = joblib.load("tmp_my_model_iris.joblib")

print("KNN準確率: %.2f" % knnmodel.score(X, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
X = iris.data
y = iris.target

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X, y)  # 學習訓練.fit

y_pred = knn.predict(X)  # 預測.predict
print("預測結果：{}".format(y_pred))
print("KNN準確率: %.2f" % knn.score(X, y))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習_K-近鄰演算法_空氣盒子

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
    X, y, test_size=0.30
)  # 訓練組8成, 測試組2成

# 從k值=1開始測試
NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

error_rate = []

for i in range(1, 60):
    NEIGHBOARS = i
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    knn.fit(X_train, y_train)  # 學習訓練.fit
    y_pred = knn.predict(X_test)  # 預測.predict
    error_rate.append(np.mean(y_pred != y_test))


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

NEIGHBOARS = 10
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

print("WITH K=10")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

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
    X, y, test_size=0.30
)  # 訓練組8成, 測試組2成

# 從k值=1開始測試
NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict
print("預測結果 :\n", y_pred)

# 使用混淆矩陣
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
    y_pred = knn.predict(X_test)  # 預測.predict
    error_rate.append(np.mean(y_pred != y_test))

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
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)
X_scaled[1:5]

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8
)  # 訓練組8成, 測試組2成

# 上述过程有没有问题？

NEIGHBOARS = 3
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # 默認歐氏距離

knn.fit(X_train, y_train.values.flatten())  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict

import sklearn.metrics as metrics

print(metrics.confusion_matrix(y_test, y_pred, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(y_test, y_pred))

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

# * 选择k值
for k in range(1, 30, 5):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    knn.fit(X_train, y_train.values.flatten())  # 學習訓練.fit
    score = knn.score(X_test, y_test)  # KNN準確率
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

print("以下 久")
gridSearchCV.fit(X_train, y_train.values.flatten())  # 學習訓練.fit

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
best.score(X_test, y_test)  # GridSearchCV準確率

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

# 06_05_knn_iris

# 鳶尾花(Iris)品種的辨識

ds = datasets.load_iris()

# 2. 資料清理、資料探索與分析
df = pd.DataFrame(ds.data, columns=ds.feature_names)
y = ds.target

print(ds.target_names)

# 箱型圖
sns.boxplot(data=df)
show()

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# y 各類別資料筆數統計
sns.countplot(x=y)
show()

# 以Pandas函數統計各類別資料筆數
cc = pd.Series(y).value_counts()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print(y_train)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)

knn.fit(X_train_std, y_train)  # 學習訓練.fit

print("計算準確率")
y_pred = knn.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 90.00%

print("最近鄰的距離與索引值")
cc = knn.kneighbors(X_test[0:1])
print(cc)

print("設定距離為加權值")
NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS, weights="distance")

knn.fit(X_train_std, y_train)  # 學習訓練.fit

print("計算準確率")
y_pred = knn.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.67%

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 機器學習前準備─以Iris為例

# 1. 資料取得

filename = "data/Iris2.csv"

df = pd.read_csv(filename)

df = df.drop("Id", axis=1)

print(df.head())

# 2. 資料處理

# df.info() # 這樣就印出訊息了

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

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
df_y = df["Species"]

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的正確率計算-------")

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    NEIGHBOARS = i
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(
        n_neighbors=NEIGHBOARS
    )  # K近鄰演算法（K Nearest Neighbor, KNN）
    knn.fit(X_train, y_train)  # 學習訓練.fit
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))  # KNN準確率

NEIGHBOARS = 8
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

# 加廣知識：視覺化圖表來顯示準確率

df_knn = pd.DataFrame()
df_knn["s"] = s
df_knn.index = [3, 4, 5, 6, 7, 8, 9, 10]
df_knn.plot(grid=True)

show()

print("分類的預測結果：")
y_pred = knn.predict(X_test)  # 預測.predict
print(y_pred)

print(y_test.values)  # 觀察Test data真實數據

# 加廣知識：利用values屬性做橫式顯示

print(y_test)

print(y_test.values)

print("計算準確率 :", accuracy_score(y_test, y_pred))
# 1.0

print("混淆矩陣 :", confusion_matrix(y_test, y_pred))

# 加深知識：交叉驗證概念
from sklearn.model_selection import cross_val_score

N = 10
s = cross_val_score(knn, df_X, df_y, cv=N, scoring="accuracy")
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print("交叉驗證每次的準確率：", s)
print("交叉驗證得到的平均準確率：", s.mean())

# 決定模型
# 進行分類預測

new = [[6.6, 3.1, 5.2, 2.4]]
v = knn.predict(new)  # 預測.predict
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

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["Sex", "Pclass"]]
df_y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size=0.2)

NEIGHBOARS = 1
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

# 測試評估

print("----KNN模式訓練後，取test data 進行分類的準確率計算-------")
print("KNN準確率: %.2f" % knn.score(X_test, y_test))

s = []
for i in range(3, 11):
    NEIGHBOARS = i
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(
        n_neighbors=NEIGHBOARS
    )  # K近鄰演算法（K Nearest Neighbor, KNN）
    knn.fit(X_train, y_train)  # 學習訓練.fit
    print("k =", k, " 準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
    s.append(knn.score(X_test, y_test))  # KNN準確率


NEIGHBOARS = 4
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

print("分類的預測結果：")
y_pred = knn.predict(X_test)  # 預測.predict
print(y_pred)  # 觀察預測結果

print("真實數據：")
print(y_test.values)  # 觀察真實數據(Test data)

print("計算準確率 :", accuracy_score(y_test, y_pred))
# 0.7541899441340782

print("混淆矩陣 :", confusion_matrix(y_test, y_pred))

from sklearn.model_selection import cross_val_score

N = 10
s = cross_val_score(knn, df_X, df_y, cv=N, scoring="accuracy")
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print("準確率：", s)
print("平均準確率：", s.mean())
print("最高：", s.max())
print("最差：", s.min())

# 決定模型
# 進行分類預測

print("-----------(1)電影中兩位主角的生還推測-------------")

Rose = [[0, 1]]  # 女性 頭等艙 蘿絲（Rose DeWitt Bukater）
Jack = [[1, 3]]  # 男性 三等艙 傑克（Jack Dawson）
v = knn.predict(Rose)  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Rose能生還嗎 ? ", s)  # Rose為女性,及坐頭等艙

v = knn.predict(Jack)  # 預測.predict
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
v = knn.predict(Mrs)  # 預測.predict
if v == 1:
    s = "生還"
else:
    s = "死亡"
print("Mrs. Straus能生還嗎 ? ", s)  # Ida為女性,及坐頭等艙，可優先搭乘救生艇存活

v = knn.predict(Mr)  # Isidor的生存率有多高呢？  # 預測.predict
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
v = knn.predict(Brown)  # Mrs. Brown呢？  # 預測.predict
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
v = knn.predict(you)  # 預測.predict
if v == 1:
    print("預測為:幸運生還")
else:
    print("預測為:無法生還")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = iris.data[:, :2]
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 標準化
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

# Predict the target values on the test data
y_pred = knn.predict(X_test)  # 預測.predict

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)

# Accuracy: 0.631578947368421

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# Split the dataset into features (X) and target (y)
X, y = iris.data, iris.target

# Print the lengths of X and y
print("Size of X:", X.shape)  #  (150, 4)
print("Size of y:", y.shape)  #  (150, )

# Split the data into training and test sets with test_size=0.2 (20% for test set)
X, y = iris.data, iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Print the sizes of the arrays
print("Size of X_train:", X_train.shape)
print("Size of X_test: ", X_test.shape)
print("Size of y_train:", y_train.shape)
print("Size of y_test: ", y_test.shape)

print("------------------------------------------------------------")  # 60個

# Create instances of the models

# Import necessary classes from sklearn libraries
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# Create instances of supervised learning models
# Logistic Regression classifier (max_iter=1000)
lr = LogisticRegression(max_iter=1000)

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

# Support Vector Machine classifier
svc = SVC()

# Create instances of unsupervised learning models
# k-Means clustering with 3 clusters and 10 initialization attempts
k_means = KMeans(n_clusters=3, n_init=10)

# Principal Component Analysis with 2 components
pca = PCA(n_components=2)

print("------------------------------")  # 30個

# Model Fitting

# Fit models to the data
lr.fit(X_train, y_train)  # 學習訓練.fit
knn.fit(X_train, y_train)  # 學習訓練.fit
svc.fit(X_train, y_train)  # 學習訓練.fit
k_means.fit(X_train)  # 學習訓練.fit
pca.fit_transform(X_train)

# Print the instances and models
print("lr:", lr)
print("knn:", knn)
print("svc:", svc)
print("k_means:", k_means)
print("pca:", pca)

print("------------------------------")  # 30個

# Prediction

# Predict using different supervised estimators
y_pred_svc = svc.predict(X_test)
y_pred_lr = lr.predict(X_test)
y_pred_knn_proba = knn.predict_proba(X_test)

# Predict labels using KMeans in clustering algorithms
y_pred_kmeans = k_means.predict(X_test)

# Print the results
print("Supervised Estimators:")
print("SVC predictions:", y_pred_svc)
print("Logistic Regression predictions:", y_pred_lr)
print("KNeighborsClassifier probabilities:\n", y_pred_knn_proba[:5], "\n     ...")

print("\nUnsupervised Estimators:")
print("KMeans predictions:", y_pred_kmeans)

print("------------------------------")  # 30個

# Preprocessing The Data
# Standardization

# Create an instance of the StandardScaler and fit it to training data
scaler = StandardScaler().fit(X_train)

# Transform the training and test data using the scaler
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)

# Print the variables
print("\nStandardized X_train:\n", standardized_X[:5], "\n     ...")
print("\nStandardized X_test:\n", standardized_X_test[:5], "\n     ...")

# Normalization

from sklearn.preprocessing import Normalizer

scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)

# Print the variables
print("\nNormalized X_train:\n", normalized_X[:5], "\n     ...")
print("\nNormalized X_test:\n", normalized_X_test[:5], "\n     ...")

print("------------------------------------------------------------")  # 60個

# Classification Metrics

# Accuracy Score
accuracy_knn = knn.score(X_test, y_test)  # KNN準確率
print("Accuracy Score (knn):", knn.score(X_test, y_test))

accuracy_y_pred = accuracy_score(y_test, y_pred_lr)
print("Accuracy Score (y_pred):", accuracy_y_pred)

# Classification Report
classification_rep_y_pred = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred):\n", classification_rep_y_pred)

classification_rep_y_pred_lr = classification_report(y_test, y_pred_lr)
print("Classification Report (y_pred_lr):\n", classification_rep_y_pred_lr)

# Confusion Matrix
conf_matrix_y_pred_lr = confusion_matrix(y_test, y_pred_lr)
print("Confusion Matrix (y_pred_lr):\n", conf_matrix_y_pred_lr)

print("------------------------------------------------------------")  # 60個

# Regression Metrics

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# True values (ground truth)
y_true = [3, -0.5, 2]

# Predicted values
y_pred = [2.8, -0.3, 1.8]

# Calculate Mean Absolute Error
mae = mean_absolute_error(y_true, y_pred)
print("Mean Absolute Error:", mae)

# Calculate Mean Squared Error
mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)

# Calculate R² Score
r2 = r2_score(y_true, y_pred)
print("R² Score:", r2)

print("------------------------------------------------------------")  # 60個

# Clustering Metrics

from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import homogeneity_score
from sklearn.metrics import v_measure_score

# Adjusted Rand Index
adjusted_rand_index = adjusted_rand_score(y_test, y_pred_kmeans)
print("Adjusted Rand Index:", adjusted_rand_index)

# Homogeneity Score
homogeneity = homogeneity_score(y_test, y_pred_kmeans)
print("Homogeneity Score:", homogeneity)

# V-Measure Score
v_measure = v_measure_score(y_test, y_pred_kmeans)
print("V-Measure Score:", v_measure)

print("------------------------------------------------------------")  # 60個

# Cross-Validation

# Import necessary library
from sklearn.model_selection import cross_val_score

# Cross-validation with KNN estimator
N = 4
knn_scores = cross_val_score(knn, X_train, y_train, cv=N)
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print(knn_scores)

# Cross-validation with Linear Regression estimator
N = 2
lr_scores = cross_val_score(lr, X, y, cv=N)
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print(lr_scores)

# Grid Search

# Import necessary library
from sklearn.model_selection import GridSearchCV

# Define parameter grid
params = {"n_neighbors": np.arange(1, 3), "weights": ["uniform", "distance"]}

# Create GridSearchCV object
grid = GridSearchCV(estimator=knn, param_grid=params)

# Fit the grid to the data
grid.fit(X_train, y_train)

# Print the best parameters found
print("Best parameters:", grid.best_params_)

# Print the best cross-validation score
print("Best cross-validation score:", grid.best_score_)

# Print the accuracy on the test set using the best parameters
best_knn = grid.best_estimator_
test_accuracy = best_knn.score(X_test, y_test)  # GridSearchCV準確率
print("Test set accuracy:", test_accuracy)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
