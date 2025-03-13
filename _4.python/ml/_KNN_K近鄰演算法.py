"""
K-近鄰演算法（K Nearest Neighbor, KNN）
KNeighborsClassifier

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
import sklearn
from common1 import *
from sklearn import datasets
from sklearn import preprocessing  # 極值標準化
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # 交叉驗證 Cross-validation
import sklearn.model_selection as cross_validation

# import sklearn.metrics as metrics

from sklearn.metrics import accuracy_score  # 計算準確率
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import homogeneity_score
from sklearn.metrics import v_measure_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.metrics import ConfusionMatrixDisplay

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier  # K近鄰演算法（K Nearest Neighbor, KNN）
from sklearn.neighbors import KNeighborsRegressor

import sklearn.linear_model
from sklearn import tree
from sklearn import metrics
from matplotlib.colors import ListedColormap


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

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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
scores = cross_val_score(knn, X, y, cv=N, scoring="accuracy")  # 交叉驗證
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

scaler = sklearn.preprocessing.StandardScaler()
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
scores = cross_val_score(knn, X, y, cv=5, scoring="accuracy")  # 交叉驗證
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print("全部分數 :", scores)
print("平均分數 :", scores.mean())

k_scores = []
for k in range(1, 31):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    # loss = -cross_val_score(knn, X, y, cv=10, scoring='mean_squared_error') # for regression
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

Ks = np.arange(1, 15)
accuracies = []
for k in Ks:
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    # 做一次就算準確率
    knn.fit(X, y)  # 學習訓練.fit
    accuracy = knn.score(X, y)  # KNN準確率
    accuracies.append(accuracy)
    """
    # 做10次算準確率
    N = 10
    scores = cross_val_score(knn, X, y, cv=N, scoring="accuracy")  # 交叉驗證
    print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
    accuracies.append(scores.mean())
    """

print("KNN分群數 :", Ks)
print("KNN準確率 :", accuracies)

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
y_pred = knn.predict(X)  # 預測.predict
print(y_pred)
print(y.values)

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
scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(df.drop("Danger", axis=1))
scaled_features = scaler.transform(df.drop("Danger", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

X = df_feat
y = df["Danger"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

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
scaler = sklearn.preprocessing.StandardScaler()
scaler.fit(df.drop("Danger", axis=1))  # 刪除 "Danger" 這一欄的資料
scaled_features = scaler.transform(df.drop("Danger", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

X = df_feat
y = df["Danger"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

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

# 資料分割
X_train, X_test, y_train, y_test = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.2
)

# 上述过程有没有问题？

NEIGHBOARS = 3
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # 默認歐氏距離

knn.fit(X_train, y_train.values.flatten())  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict

print(confusion_matrix(y_test, y_pred, labels=[0, 1]))  # 混淆矩阵
print(classification_report(y_test, y_pred))

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

# 选择k值
for k in range(1, 30, 5):
    NEIGHBOARS = k
    print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
    knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)
    knn.fit(X_train, y_train.values.flatten())  # 學習訓練.fit
    score = knn.score(X_test, y_test)  # KNN準確率
    print("KNN準確率: %.2f" % knn.score(X_test, y_test))

# 交叉验证选择k值
from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold

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

iris = datasets.load_iris()

# 資料清理、資料探索與分析
df = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

print(iris.target_names)

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

# 不須進行特徵工程

# 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print(y_train)

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
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
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Iris

filename = "data/Iris2.csv"
df = pd.read_csv(filename)
df = df.drop("Id", axis=1)
print(df.head())

# 資料處理
# df.info() # 這樣就印出訊息了

df = df.drop_duplicates()  # 刪除重複列
df.reset_index(drop=True)  # 將列索引重新編號
s = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}
df["Species"] = df["Species"].map(s)
df.info()

# 探索性資料分析
print(df.head())

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"]]
df_y = df["Species"]

# 資料分割
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
    # print("KNN準確率: %.2f" % knn.score(X, y))
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

N = 10
s = cross_val_score(knn, df_X, df_y, cv=N, scoring="accuracy")  # 交叉驗證
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

# Titanic

filename = "data/titanic.csv"
df = pd.read_csv(filename)
print(df.head())

# 資料處理
# df.info() # 這樣就印出訊息了

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Embarked"] = df["Embarked"].fillna("S")
df = df.drop("Cabin", axis=1)
print("重複值：", df[df.duplicated()])  # 檢查有無重複值

df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})
print(df.head())

# 重複值： Empty DataFrame

# 探索性資料分析

print(df.head())

# 學習訓練：建立並訓練 KNN 模型

df_X = df[["Sex", "Pclass"]]
df_y = df["Survived"]

# 資料分割
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
    print("k =", k, " KNN準確率:", knn.score(X_test, y_test))  # 用 test data 檢測模型的準確率
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

N = 10
s = cross_val_score(knn, df_X, df_y, cv=N, scoring="accuracy")  # 交叉驗證
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

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 標準化
scaler = sklearn.preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

NEIGHBOARS = 5
print("用 K近鄰演算法 找出最近的", NEIGHBOARS, "個點")
knn = KNeighborsClassifier(n_neighbors=NEIGHBOARS)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

# Predict the target values on the test data
y_pred = knn.predict(X_test)  # 預測.predict

print("計算準確率 :", accuracy_score(y_test, y_pred))
# 計算準確率 : 0.631578947368421

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()
X = iris.data
y = iris.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create instances of the models
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
scaler = sklearn.preprocessing.StandardScaler().fit(X_train)

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

accuracy_knn = knn.score(X_test, y_test)  # KNN準確率
print("KNN準確率: %.2f" % accuracy_knn)

print("計算準確率 :", accuracy_score(y_test, y_pred_lr))

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

# 交叉驗證

N = 4
knn_scores = cross_val_score(knn, X_train, y_train, cv=N)  # 交叉驗證 KNN
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print(knn_scores)

N = 2
lr_scores = cross_val_score(lr, X, y, cv=N)  # 交叉驗證 線性迴歸
print("分成", N, "組, 做 cross_val_score 是驗證用來評分資料準確度的")
print(lr_scores)

# Grid Search

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

# 分類(Classification)

iris = datasets.load_iris()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2
)

knn = KNeighborsClassifier()

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("計算準確率 :", accuracy_score(y_test, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dataset = pd.read_csv("data/Social_Network_Ads.csv")
print(dataset)

# 为了方便理解，这里我们只取Age年龄和EstimatedSalary估计工资作为特征

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 第四步：特征缩放 Feature Scaling
scaler = sklearn.preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# 第五步：使用K-NN对训练集数据进行训练
# Fitting K-NN to the Training set
# 从sklearn的neighbors类中导入KNeighborsClassifier学习器

# 设置好相关的参数 n_neighbors = 5(K值的选择，默认选择5)、
# metric = 'minkowski'(距离度量的选择，这里选择的是闵氏距离(默认参数))、
# p = 2 (距离度量metric的附属参数，只用于闵氏距离和带权重闵氏距离中p值的选择，
# p=1为曼哈顿距离， p=2为欧式距离。默认为2)

classifier = KNeighborsClassifier(n_neighbors=5, metric="minkowski", p=2)

classifier.fit(X_train, y_train)  # 學習訓練.fit

KNeighborsClassifier(
    algorithm="auto",
    leaf_size=30,
    metric="minkowski",
    metric_params=None,
    n_jobs=1,
    n_neighbors=5,
    p=2,
    weights="uniform",
)

# 第六步：对测试集进行预测
# Predicting the Test set results

y_pred = classifier.predict(X_test)
print(y_pred)


# 第七步：生成混淆矩阵
# Making the Confusion Matrix
# 混淆矩阵可以对一个分类器性能进行分析，由此可以计算出许多指标，例如：ROC曲线、正确率等

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

"""
[[64  4]
 [ 3 29]]
    预测值
    0   1
实0 64  4   
际1 3   29
值
预测集中的0总共有68个，1总共有32个。
在这个混淆矩阵中，实际有68个0，但K-NN预测出有67(64+3)个0，其中有3个实际上是1。
同时K-NN预测出有33(4+29)个1，其中4个实际上是0。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 共同函數

# numpy and matplotlib will be used a lot during the lecture
# if you are familiar with these libraries you may skip this part
# if not - extended comments were added to make it easier to understand

# used later to apply different colors in for loops
mpl_colors = ("r", "b", "g", "c", "m", "y", "k", "w")

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")


def generate_random_points(size=10, low=0, high=1):
    """Generate a set of random 2D points
    size -- number of points to generate
    low  -- min value
    high -- max value
    """
    # random_sample([size]) returns random numbers with shape defined by size
    # e.g.
    # >>> np.random.random_sample((2, 3))
    #
    # array([[ 0.44013807,  0.77358569,  0.64338619],
    #        [ 0.54363868,  0.31855232,  0.16791031]])
    #
    return (high - low) * np.random.random_sample((size, 2)) + low


def init_plot(x_range=None, y_range=None, x_label="$x_1$", y_label="$x_2$"):
    """Set axes limits and labels

    x_range -- [min x, max x]
    y_range -- [min y, max y]
    x_label -- string
    y_label -- string
    """

    # subplots returns figure and axes
    # (in general you may want many axes on one figure)
    # we do not need fig here
    # but we will apply changes (including adding points) to axes
    _, ax = plt.subplots(dpi=70)

    # set grid style and color
    ax.grid(c="0.70", linestyle=":")

    # set axes limits (x_range and y_range is a list with two elements)
    ax.set_xlim(x_range)
    ax.set_ylim(y_range)

    # set axes labels
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    # return axes so we can continue modyfing them later
    return ax


def plot_random_points(style=None, color=None):
    """Generate and plot two (separated) sets of random points

    style -- latter group points style (default as first)
    color -- latter group color (default as first)
    """

    # create a plot with x and y ranges from 0 to 2.5
    ax = init_plot([0, 2.5], [0, 2.5])

    # add two different sets of random points
    # first set = 5 points from [0.5, 1.0]x[0.5, 1.0]
    # second set = 5 points from [1.5, 2.0]x[1.5, 2.0]
    # generate_random_points return a numpy array in the format like
    # [[x1, y1], [x2, y2], ..., [xn, yn]]
    # pyplot.plt take separately arrays with X and Y, like
    # plot([x1, x2, x3], [y1, y2, y3])
    # thus, we transpose numpy array to the format
    # [[x1, x2, ..., xn], [y1, y2, ..., yn]]
    # and unpack it with *
    ax.plot(*generate_random_points(5, 0.5, 1.0).T, "ro")
    ax.plot(*generate_random_points(5, 1.5, 2.0).T, style or "ro")

    return ax


def plot_an_example(style=None, color=None, label="Class"):
    """Plot an example of supervised or unsupervised learning"""
    ax = plot_random_points(style, color)

    # circle areas related to each set of points
    # pyplot.Circle((x, y), r); (x, y) - the center of a circle; r - radius
    ax.add_artist(plt.Circle((0.75, 0.75), 0.5, fill=0, color="r", lw=2))
    ax.add_artist(plt.Circle((1.75, 1.75), 0.5, fill=0, color=color or "r", lw=2))

    # put group labels
    # pyplot.text just put arbitrary text in given coordinates
    ax.text(0.65, 1.4, label + " I", fontdict={"color": "r"})
    ax.text(1.65, 1.1, label + " II", fontdict={"color": color or "r"})


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# introduction_to_machine_learning_00_intro

# Supervised learning
plot_an_example(style="bs", color="b")
show()

# Unsupervised learning
plot_an_example(label="Cluster")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# introduction_to_machine_learning_01_knn

# k-Nearest Neighbors

"""
Our first ML problem
    Two classes: red circles and blue squares (training samples)
    Where does the green triangle (test sample) belong?
"""
X1 = generate_random_points(20, 0, 1)
X2 = generate_random_points(20, 1, 2)

new_point = generate_random_points(1, 0, 2)

plot = init_plot([0, 2], [0, 2])  # [0, 2] x [0, 2]

plot.plot(*X1.T, "ro", *X2.T, "bs", *new_point.T, "g^")
show()

# Nearest Neighbor


class NearestNeighbor:
    """Nearest Neighbor Classifier"""

    def __init__(self, distance=0):
        """Set distance definition: 0 - L1, 1 - L2"""
        if distance == 0:
            self.distance = np.abs  # absolute value
        elif distance == 1:
            self.distance = np.square  # square root
        else:
            raise Exception("Distance not defined.")

    def train(self, x, y):
        """Train the classifier (here simply save training data)

        x -- feature vectors (N x D)
        y -- labels (N x 1)
        """
        self.x_train = x
        self.y_train = y

    def predict(self, x):
        """Predict and return labels for each feature vector from x

        x -- feature vectors (N x D)
        """
        predictions = []  # placeholder for N labels

        # loop over all test samples
        for x_test in x:
            # array of distances between current test and all training samples
            distances = np.sum(self.distance(self.x_train - x_test), axis=1)

            # get the closest one
            min_index = np.argmin(distances)

            # add corresponding label
            predictions.append(self.y_train[min_index])

        return predictions


# let's create an array with 5x2 shape
a = np.random.random_sample((5, 2))

# and another array with 1x2 shape
b = np.array([[1.0, 1.0]])

print(a, b, sep="\n\n")

# subtract arguments (element-wise)
# note, that at least one dimension must be the same
print(a - b)

# numpy.abs calculates absolute value (element-wise)
print(np.abs(a - b))

# sum all elements
np.sum(np.abs(a - b))

# sum elements over a given axis
np.sum(np.abs(a - b), axis=0)

np.sum(np.abs(a - b), axis=1)

# Analysis


class Analysis:
    """Apply NearestNeighbor to generated (uniformly) test samples."""

    def __init__(self, *x, distance):
        """Generate labels and initilize classifier

        x -- feature vectors arrays
        distance -- 0 for L1, 1 for L2
        """
        # get number of classes
        self.nof_classes = len(x)

        # create lables array
        # np.ones creates an array of given shape filled with 1 of given type
        # we apply consecutive integer numbers as class labels
        # ravel return flatten array
        y = [i * np.ones(_x.shape[0], dtype=np.int) for i, _x in enumerate(x)]
        y = np.array(y).ravel()

        # save training samples to plot them later
        self.x_train = x

        # merge feature vector arrays for NearestNeighbor
        x = np.concatenate(x, axis=0)

        # train classifier
        self.nn = NearestNeighbor(distance)
        self.nn.train(x, y)

    def prepare_test_samples(self, low=0, high=2, step=0.01):
        """Generate a grid with test points (from low to high with step)"""
        # remember range
        self.range = [low, high]

        # start with grid of points from [low, high] x [low, high]
        grid = np.mgrid[low : high + step : step, low : high + step : step]

        # convert to an array of 2D points
        self.x_test = np.vstack([grid[0].ravel(), grid[1].ravel()]).T

    def analyse(self):
        """Run classifier on test samples and split them according to labels."""

        # find labels for test samples
        self.y_test = self.nn.predict(self.x_test)

        self.classified = []  # [class I test points, class II test ...]

        # loop over available labels
        for label in range(self.nof_classes):
            # if i-th label == current label -> add test[i]
            class_i = np.array(
                [self.x_test[i] for i, l in enumerate(self.y_test) if l == label]
            )
            self.classified.append(class_i)

    def plot(self, t=""):
        """Visualize the result of classification"""
        plot = init_plot(self.range, self.range)
        plot.set_title(t)
        plot.grid(False)

        # plot training samples
        for i, x in enumerate(self.x_train):
            plot.plot(*x.T, mpl_colors[i] + "o")

        # plot test samples
        for i, x in enumerate(self.classified):
            plot.plot(*x.T, mpl_colors[i] + ",")


# L1 test

l1 = Analysis(X1, X2, distance=0)
l1.prepare_test_samples()
l1.analyse()
l1.plot()

# L2 Test

l2 = Analysis(X1, X2, distance=1)
l2.prepare_test_samples()
l2.analyse()
l2.plot()


# Multiclass classification


def generate4(n=50):
    """Generate 4 sets of random points."""

    # points from [0, 1] x [0, 1]
    X1 = generate_random_points(n, 0, 1)
    # points from [1, 2] x [1, 2]
    X2 = generate_random_points(n, 1, 2)
    # points from [0, 1] x [1, 2]
    X3 = np.array([[x, y + 1] for x, y in generate_random_points(n, 0, 1)])
    # points from [1, 2] x [0, 1]
    X4 = np.array([[x, y - 1] for x, y in generate_random_points(n, 1, 2)])

    return X1, X2, X3, X4


# loop over no. of training samples
for n in (5, 10, 50, 100):
    # generate 4 sets of random points (each one with n samples)
    # unpack them when passing to Analysis
    c4 = Analysis(*generate4(n), distance=1)
    c4.prepare_test_samples()
    c4.analyse()
    c4.plot("No. of samples = {}".format(n))
    show()

# Message 01: size matters!

# Noise

# generate 4 classes of 2D points
X1, X2, X3, X4 = generate4()

# add some noise by applying gaussian to every point coordinates
noise = lambda x, y: [np.random.normal(x, 0.1), np.random.normal(y, 0.1)]

X1 = np.array([noise(x, y) for x, y in X1])
X2 = np.array([noise(x, y) for x, y in X2])
X3 = np.array([noise(x, y) for x, y in X3])
X4 = np.array([noise(x, y) for x, y in X4])

# perform analysis
c4 = Analysis(X1, X2, X3, X4, distance=1)
c4.prepare_test_samples()
c4.analyse()
c4.plot()
show()

# Overfitting

# Message 02: avoid overfitting!
# Accuracy

accuracy = 0

# loop over (sample, reconstructed label)
for sample, label in zip(c4.x_test, c4.y_test):
    # determine true label
    if sample[0] < 1 and sample[1] < 1:
        true_label = 0
    elif sample[0] > 1 and sample[1] > 1:
        true_label = 1
    elif sample[0] < 1 and sample[1] > 1:
        true_label = 2
    else:
        true_label = 3

    if true_label == label:
        accuracy += 1

accuracy /= len(c4.x_test)

print(accuracy)

print("------------------------------------------------------------")  # 60個

# Message 03: keep some data for testing!
print("k-Nearest Neighbors")


class kNearestNeighbors(NearestNeighbor):
    """k-Nearest Neighbor Classifier"""

    def __init__(self, k=1, distance=0):
        """Set distance definition: 0 - L1, 1 - L2"""
        super().__init__(distance)
        self.k = k

    def predict(self, x):
        """Predict and return labels for each feature vector from x

        x -- feature vectors (N x D)
        """
        predictions = []  # placeholder for N labels

        # no. of classes = max label (labels starts from 0)
        nof_classes = np.amax(self.y_train) + 1

        # loop over all test samples
        for x_test in x:
            # array of distances between current test and all training samples
            distances = np.sum(self.distance(self.x_train - x_test), axis=1)

            # placeholder for labels votes
            votes = np.zeros(nof_classes, dtype=np.int)

            # find k closet neighbors and vote
            # argsort returns the indices that would sort an array
            # so indices of nearest neighbors
            # we take self.k first
            for neighbor_id in np.argsort(distances)[: self.k]:
                # this is a label corresponding to one of the closest neighbor
                neighbor_label = self.y_train[neighbor_id]
                # which updates votes array
                votes[neighbor_label] += 1

            # predicted label is the one with most votes
            predictions.append(np.argmax(votes))

        return predictions


print("kAnalysis")


class kAnalysis(Analysis):
    """Apply kNearestNeighbor to generated (uniformly) test samples."""

    def __init__(self, *x, k=1, distance=1):
        """Generate labels and initilize classifier

        x -- feature vectors arrays
        k -- number of nearest neighbors
        distance -- 0 for L1, 1 for L2
        """
        # get number of classes
        self.nof_classes = len(x)

        # create lables array
        y = [i * np.ones(_x.shape[0], dtype=np.int) for i, _x in enumerate(x)]
        y = np.array(y).ravel()

        # save training samples to plot them later
        self.x_train = x

        # merge feature vector arrays for NearestNeighbor
        x = np.concatenate(x, axis=0)

        # train classifier (knn this time)
        self.nn = kNearestNeighbors(k, distance)
        self.nn.train(x, y)


print("Sanity check")

# apply kNN with k=1 on the same set of training samples
knn = kAnalysis(X1, X2, X3, X4, k=1, distance=1)
knn.prepare_test_samples()
knn.analyse()
knn.plot()
show()

print("k-Test")

# training size = 50
# let's check a few values between 1 and 50
for k in (1, 5, 10, 50):
    knn = kAnalysis(X1, X2, X3, X4, k=k, distance=1)
    knn.prepare_test_samples()
    knn.analyse()
    knn.plot("k = {}".format(k))
    show()

print("------------------------------------------------------------")  # 60個

# Hyperparameters

# Over-, under-fitting example

# generate random data from x^2 function (with some noise)
data = np.array(
    [[x, np.random.normal(x**2, 0.1)] for x in 2 * np.random.random(10) - 1]
)

plot = init_plot([-1, 1], [-1, 1])
plot.plot(*data.T, "o")
show()

# loop over degrees of polynomial
# data is x^2, so let's try degrees 1, 2, 10
for n in (1, 2, 10):
    # polyfit returns an array with polynomial coefficients
    # poly1d is a polynomial class
    f = np.poly1d(np.polyfit(*data.T, n))

    # returns an array with 100 uniformly distributed numbers from -1 to 1
    x = np.linspace(-1, 1, 100)

    plot = init_plot([-1, 1], [-1, 1])
    plot.set_title("n = {}".format(n))
    plot.plot(*data.T, "o", x, f(x))
    show()

"""
For n = 1 we clearly underfit the data as we do not have enough parameters to describe the complexity of the problem

For n = 2 we have appropriate capacity (as we actually generated data form

    function)

    For n = 10 we overfit the data - training samples are described perfectly, but we clearly lost the generalization ability

Message 04: right choice of hyperparameters is crucial!
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Validation dataset

# Iris dataset

# columns names - can be used to access columns later
columns = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"]

# iris.data is a csv file
src = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"

# load the file with pandas.read_csv
# it will name columns as defined in columns list
# so one can access a column through index or name
iris_data = pd.read_csv(src, header=None, names=columns)

iris_data.head()  # print a few first entries


# Visualize dataset

# to extract rows with class column == class_name
extract = lambda class_name: iris_data.loc[iris_data["Class"] == class_name]

# axes settings - part = Sepal or Petal; x = Length, y = Width
set_ax = lambda part: {"x": part + " Length", "y": part + " Width", "kind": "scatter"}

# add iris type / sepal or petal / color to existing axis
plot = lambda class_name, part, color, axis: extract(class_name).plot(
    **set_ax(part), color=color, label=class_name, ax=axis
)

# plot all Iris types (sepal or petal) on existing axis
plot_all = lambda part, axis: [
    plot(iris, part, mpl_colors[i], axis)
    for i, iris in enumerate(set(iris_data["Class"]))
]

# with pyplot.subplots we can create many plots on one figure
# here we create 2 plots - 1 row and 2 columns
# thus, subplots returns figure, axes of 1st plot, axes for 2nd plot
_, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 4))

# using messy lambda we can plot all Iris types at once
# Petal data on 1st plots and Sepal data on 2nd plot
plot_all("Petal", ax1)
plot_all("Sepal", ax2)

# tight_layout adjust subplots params so they fit into figure ares
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# Prepare feature vectors and labels

# every Iris has 4 features (forming our 4D feature vectors)
# pandaoc.DataFrame.iloc allows us access data through indices
# we create an array with feature vectors by taking all rows for first 4 columns
X = iris_data.iloc[:, :4]

# it is still pandoc.DataFrame object - pretty handy
X.head()

# create numpy array (matrix) for further processing
X = np.array(X)

# print a few first entries
print(X[:5])

# as mentioned before, we can access DataFrame object through column labels
Y = np.array(iris_data["Class"])

# print a few first entries
print(Y[:5])

# Prepare test dataset

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train, X_valid, Y_train, Y_valid = train_test_split(X_train, Y_train, test_size=0.2)

# check how many sample we have
print(X_train.shape[0], X_valid.shape[0], X_test.shape[0])

# kNN from scikit-learn

# create knn classifier with k = 48
knn = KNeighborsClassifier(n_neighbors=48)

# train the model
knn.fit(X_train, Y_train)

# predict labels for test samples
Y_pred = knn.predict(X_valid)

# Accuracy

# use bold if true != predicted
for true, pred in zip(Y_valid, Y_pred):
    if pred == true:
        print("{}\t -> {}".format(true, pred))
    else:
        print("\033[1m{}\t -> {}\033[0m".format(true, pred))

# Y_valid == Y_pred -> array of True/False (if two elements are equal or not)
# (Y_valid == Y_pred).sum() -> number of Trues
# Y_valid.shape[0] -> number of validation samples
accuracy = (Y_valid == Y_pred).sum() / Y_valid.shape[0]
print(accuracy)

print("計算準確率 :", accuracy_score(Y_valid, Y_pred))

# k-dependence of the accuracy

scores = []  # placeholder for accuracy

max_k = 85  # maximum number of voters

# loop over different values of k
for k in range(1, max_k):
    # create knn classifier with k = k
    knn = KNeighborsClassifier(n_neighbors=k)

    # train the model
    knn.fit(X_train, Y_train)

    # predict labels for test samples
    Y_pred = knn.predict(X_valid)

    # add accuracy to score table
    scores.append(accuracy_score(Y_valid, Y_pred))

# Now, we can plot accuracy as a function of k


def k_accuracy_plot(max_k=85):
    """Just plot settings"""
    plt.grid(True)
    plt.xlabel("k")
    plt.ylabel("Accuracy")
    plt.xlim([0, max_k + 5])
    plt.ylim([0, 1])
    plt.xticks(range(0, max_k + 5, 5))

    return plt


k_accuracy_plot().plot(range(1, max_k), scores)
show()

# And check the accuracy measured on the test samples

knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)

print("計算準確率 :", accuracy_score(Y_test, Y_pred))
# 0.9666666666666667

print("------------------------------------------------------------")  # 60個

# Cross-validation

# this time we do not create dedicated validation set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

avg_scores = []  # average score for different k

nof_folds = 10

# loop over different values of k
for k in range(1, max_k):
    # create knn classifier with k = k
    knn = KNeighborsClassifier(n_neighbors=k)

    # cross-validate knn on our training sample with nof_folds
    scores = cross_val_score(knn, X_train, Y_train, cv=nof_folds, scoring="accuracy")

    # add avg accuracy to score table
    avg_scores.append(scores.mean())

k_accuracy_plot().plot(range(1, max_k), avg_scores)
show()

print("------------------------------------------------------------")  # 60個

# Data normalization

# original data - both in cm
print(X[:5])

# make a copy of X
Xmm = X.copy()

# and multiply last two columns by 0.1
Xmm[:, 2:] *= 0.1

# and we have our fake Iris data with petal length/width in mm
print(Xmm[:5])


def get_accuracy(X, Y, k=10):
    """Make training and test datasets and process through kNN"""

    # prepare training / test samples
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # create a kNN with k = k
    knn = KNeighborsClassifier(n_neighbors=k)

    # get prediction for original dataset
    knn.fit(X_train, Y_train)
    Y_pred = knn.predict(X_test)

    return accuracy_score(Y_test, Y_pred)


cm = get_accuracy(X, Y)
mm = get_accuracy(Xmm, Y)

print("Accuracy:\n\tboth in cm: {}\n\tpetal in mm: {}".format(cm, mm))

# Message 05: be aware of data normalization!

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MNIST
"""
    THE MNIST DATABASE of handwritten digits
    The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
    It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.
    To make it simpler (and faster) let's use digits toy dataset which comes with scikit-learn src
    Each datapoint is a 8x8 image of a digit.
    About 180 samples per class (digit)
    Total number of samples 1797
"""

from sklearn.datasets import load_digits

digits = load_digits()
print(digits.data.shape)

"""
(1797, 64)
    digits.images is a numpy array with 1797 numpy arrays 8x8 (feature vectors) representing digits
    digits.target is a numpy array with 1797 integer numbers (class labels)
    the code below allow us to visualize a random digits from the dataset
"""
# set grayscale
plt.gray()

# get some random index from 0 to dataset size
random_index = np.random.randint(1796)


# draw random digit
plt.matshow(digits.images[random_index])

# and print the matrix
plt.text(
    8, 5, digits.images[random_index], fontdict={"family": "monospace", "size": 16}
)

# and the label
plt.text(
    10,
    1,
    "This is: {}".format(digits.target[random_index]),
    fontdict={"family": "monospace", "size": 16},
)
show()

# Distance between images
"""
  TEST      TRAIN    PIXEL-WISE
| 4 2 0     2 5 8 |   |2 3 8|
| 5 3 9  -  2 8 1 | = |3 5 8|  ->  38
| 0 2 3     1 4 9 |   |1 2 6|
"""
# Prepare data

# the original shape of an image
print(digits.images.shape)

# (1797, 8, 8)

# numpy.reshape is handy here
print(digits.images.reshape((1797, -1)).shape)

# (1797, 64)

print(digits.images.reshape((1797, 64)).shape)

# (1797, 64)

print(digits.images.reshape((-1, 64)).shape)

# (1797, 64)

data_train, data_test, label_train, label_test = train_test_split(
    digits.images.reshape((1797, -1)), digits.target, test_size=0.2
)

# Cross-validation

avg_scores = []  # average score for different k

max_k = 50
nof_folds = 10

# loop over different values of k
for k in range(1, max_k):
    # create knn classifier with k = k
    knn = KNeighborsClassifier(n_neighbors=k)

    # cross-validate knn on our training sample with nof_folds
    scores = cross_val_score(
        knn, data_train, label_train, cv=nof_folds, scoring="accuracy"
    )

    # add avg accuracy to score table
    avg_scores.append(scores.mean())

plt.grid(True)
plt.xlabel("k")
plt.ylabel("Accuracy")
plt.xlim([0, max_k])
plt.ylim([0, 1])
plt.xticks(range(0, max_k, 5))

plt.plot(range(1, max_k), avg_scores)
show()

# Final test

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(data_train, label_train)
prediction = knn.predict(data_test)

print("計算準確率 :", accuracy_score(label_test, prediction))
# 0.9888888888888889

for i, (true, predict) in enumerate(zip(label_test, prediction)):
    if true != predict:
        digit = data_test[i].reshape((8, 8))  # reshape again to 8x8
        plt.matshow(digit)  # for matshow
        plt.title("{} predicted as {}".format(true, predict))
show()

print("------------------------------------------------------------")  # 60個

# Regression with kNN

# Genearate some fake data

data_size = 50

# generate and sort *data_size* numbers from 0 to 4pi
x_train = 4 * np.pi * np.sort(np.random.rand(data_size, 1), axis=0)

# let's fit to sine
y_train = np.sin(x_train).ravel()

# add some noise to the data
y_train = np.array([np.random.normal(y, 0.05) for y in y_train])

plt.plot(x_train, y_train, "ro")
show()

# Make a fit

# Comment on numpy.newaxis

# let's create a 1D numpy array
D1 = np.array([1, 2, 3, 4])

print(D1)

# [1 2 3 4]

# we can easily add another dimension using numpy.newaxis
D2 = D1[:, np.newaxis]

print(D2)

# And back to the task

from sklearn.neighbors import KNeighborsRegressor

# first we need test sample
x_test = np.linspace(0, 4 * np.pi, 100)[:, np.newaxis]

for i, k in enumerate((1, 5, 10, 20)):
    # weights=distance - weight using distances
    knn = KNeighborsRegressor(k, weights="distance")

    # calculate y_test for all points in x_test
    y_test = knn.fit(x_train, y_train).predict(x_test)

    plt.subplot(2, 2, i + 1)

    plt.title("k = {}".format(k))

    plt.plot(x_train, y_train, "ro", x_test, y_test, "g")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import math
from itertools import combinations


def Distance(x, y, p=2):
    if len(x) == len(y) and len(x) > 1:
        sum = 0
        for i in range(len(x)):
            sum += math.pow(abs(x[i] - y[i]), p)
        return math.pow(sum, 1 / p)
    else:
        return 0


# 二维空间的三个点坐标
x1 = [1, 1]
x2 = [5, 1]
x3 = [4, 4]

for i in range(1, 5):
    r = {"p={} x1=[1,1],x2={}".format(i, x2): Distance(x1, x2, p=i)}
    print(min(zip(r.keys(), r.values())))

for i in range(1, 5):
    r = {"p={} x1=[1,1],x3={}".format(i, c): Distance(x1, c, p=i) for c in [x3]}
    print(min(zip(r.keys(), r.values())))

# 对iris花瓣数据分类 python实现

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from collections import Counter

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["label"] = iris.target
# 构建数据列名
df.columns = ["sepal length", "sepal width", "petal length", "petal width", "label"]

# 展示部分数据(展示10条记录)，截取部分记录 df[start:end]
cc = df[0:10]
print(cc)


# 以花萼长度和宽度构架二维数据并展示
plt.scatter(df[:50]["sepal length"], df[:50]["sepal width"], label="0")
plt.scatter(df[50:100]["sepal length"], df[50:100]["sepal width"], label="1")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
show()

# 2.定义KNN


class KNN:
    def __init__(self, X_train, y_train, n_neighbors=3, p=2):
        """
        parameter: n_neighbors 临近点个数
        parameter: p 距离度量
        """
        self.n = n_neighbors
        self.p = p
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X):
        # 取出n个点
        knn_list = []
        for i in range(self.n):
            dist = np.linalg.norm(X - self.X_train[i], ord=self.p)
            knn_list.append((dist, self.y_train[i]))

        for i in range(self.n, len(self.X_train)):
            max_index = knn_list.index(max(knn_list, key=lambda x: x[0]))
            dist = np.linalg.norm(X - self.X_train[i], ord=self.p)
            if knn_list[max_index][0] > dist:
                knn_list[max_index] = (dist, self.y_train[i])

        # 统计
        knn = [k[-1] for k in knn_list]
        count_pairs = Counter(knn)
        max_count = sorted(count_pairs, key=lambda x: x)[-1]
        return max_count

    def score(self, X_test, y_test):
        # 投票得分
        right_count = 0
        n = 10
        for X, y in zip(X_test, y_test):
            label = self.predict(X)
            if label == y:
                right_count += 1
        return right_count / len(X_test)


# 构建训练数据和测试数据

data = np.array(df.iloc[:100, [0, 1, -1]])
X, y = data[:, :-1], data[:, -1]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 4.训练

knn = KNN(X_train, y_train)

# 5.测试

# 给定测试数据，计算其分类正确性

print("KNN準確率: %.2f" % knn.score(X_test, y_test))

# 1.0

# 6.预测

# 构建测试点 预测其类别
point = [7.0, 4.0]
print("测试点类别: {}".format(knn.predict(point)))

plt.scatter(df[:50]["sepal length"], df[:50]["sepal width"], label="0")
plt.scatter(df[50:100]["sepal length"], df[50:100]["sepal width"], label="1")
plt.plot(point[0], point[1], "g*", label="point")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.legend()
show()

# 测试点类别: 1.0

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# k近邻算法的实现: kd树

# kd树代码实现

# 定义kd树，设计kd树的数据结构


# 构建结点对象
class KdNode(object):
    def __init__(self, dom_elt, dim=0, left=None, right=None):
        self.dom_elt = dom_elt  # k维向量节点(k维空间中的一个样本点)
        self.dim = dim  # 整数（进行分割维度的序号）
        self.left = left  # 该结点分割超平面左子空间构成的kd-tree
        self.right = right  # 该结点分割超平面右子空间构成的kd-tree


class KdTree(object):
    def __init__(self, data):
        k = len(data[0])  # 数据维度

        # 按第dim维划分数据集exset创建KdNode
        def _CreateNode(dim, data_set):
            if not data_set:  # 数据集为空
                return None

            # 按要进行分割的那一维数据排序
            data_set.sort(key=lambda x: x[dim])
            split_pos = len(data_set) // 2
            median = data_set[split_pos]  # 中位数分割点
            split_next = (dim + 1) % k  # cycle coordinates

            # 递归的创建kd树
            return KdNode(
                median,
                dim,
                _CreateNode(split_next, data_set[:split_pos]),  # 创建左子树
                _CreateNode(split_next, data_set[split_pos + 1 :]),
            )  # 创建右子树

        self.root = _CreateNode(0, data)  # 从第0维分量开始构建kd树,返回根节点


# kdTree的前序遍历
def preorder(root):
    print(root.dom_elt)
    if root.left:  # 节点不为空
        preorder(root.left)
    if root.right:
        preorder(root.right)


data = [[2, 3], [5, 4], [9, 6], [4, 7], [8, 1], [7, 2]]
kd = KdTree(data)
cc = preorder(kd.root)
print(cc)

from collections import namedtuple
from operator import itemgetter
from pprint import pformat


class Node(namedtuple("Node", "location left_child right_child")):
    def __repr__(self):
        return pformat(tuple(self))


def kdtree(point_list, depth=0):
    if not point_list:
        return None

    k = len(point_list[0])  # 假定所有点的尺寸相同
    # 根据深度选择轴
    axis = depth % k

    # 根据轴对点的列表进行排序，并选择中间值作为轴元素
    point_list.sort(key=itemgetter(axis))
    median = len(point_list) // 2

    # 创建结点并构建子树
    return Node(
        location=point_list[median],
        left_child=kdtree(point_list[:median], depth + 1),
        right_child=kdtree(point_list[median + 1 :], depth + 1),
    )


def main():
    """构建kd树-案例"""
    point_list = [(7, 2), (5, 4), (9, 6), (4, 7), (8, 1), (2, 3)]
    tree = kdtree(point_list)
    print(tree)


if __name__ == "__main__":
    main()

# scikit-learn中的 k-d-tree案例

# scikit-learn是一个机器学习类库，里面实现了KDTree。

# 下面例子，构建一个二维空间的kd树，然后对其作k近邻搜索以及指定半径的搜索。

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Circle
from sklearn.neighbors import KDTree

np.random.seed(0)

# 随机产生150个二维数据
points = np.random.random((150, 2))
tree = KDTree(points)
point = points[0]
# k近邻发搜索
dists, indices = tree.query([point], k=4)

# q指定半径搜索
indices = tree.query_radius([point], r=0.2)

fig = plt.figure()
ax = fig.add_subplot(111, aspect="equal")
ax.add_patch(Circle(point, 0.2, color="g", fill=False))
X, Y = [p[0] for p in points], [p[1] for p in points]
plt.scatter(X, Y)
plt.scatter([point[0]], [point[1]], c="r")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# K-nearest neighbor Classification

df = pd.read_csv("data/Classified Data", index_col=0)
cc = df.head()
print(cc)

cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# Check the spread of the features

l = list(df.columns)
l[0 : len(l) - 2]

for i in range(len(l) - 1):
    sns.boxplot(x="TARGET CLASS", y=l[i], data=df)
    plt.figure()

show()

# Scale the features using sklearn.preprocessing package

# Instantiate a scaler standardizing estimator

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

scaler.fit(df.drop("TARGET CLASS", axis=1))
scaled_features = scaler.transform(df.drop("TARGET CLASS", axis=1))

df_feat = pd.DataFrame(scaled_features, columns=df.columns[:-1])
cc = df_feat.head()
print(cc)

# Train/Test split, model fit and prediction

from sklearn.model_selection import train_test_split

X = df_feat
y = df["TARGET CLASS"]
X_train, X_test, y_train, y_test = train_test_split(
    scaled_features, df["TARGET CLASS"], test_size=0.50, random_state=101
)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

pred = knn.predict(X_test)

# Evaluation of classification quality

from sklearn.metrics import classification_report, confusion_matrix

conf_mat = confusion_matrix(y_test, pred)
print(conf_mat)

print(classification_report(y_test, pred))

print("Misclassification error rate:", round(np.mean(pred != y_test), 3))

# Misclassification error rate: 0.082

# Choosing 'k' by elbow method

error_rate = []

# Will take some time
for i in range(1, 60):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error_rate.append(np.mean(pred_i != y_test))

plt.figure(figsize=(10, 6))
plt.plot(
    range(1, 60),
    error_rate,
    color="blue",
    linestyle="dashed",
    marker="o",
    markerfacecolor="red",
    markersize=8,
)
plt.title("Error Rate vs. K Value", fontsize=20)
plt.xlabel("K", fontsize=15)
plt.ylabel("Error (misclassification) Rate", fontsize=15)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個
