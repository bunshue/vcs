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

train_data, test_data, train_label, test_label = train_test_split(
    iris_data, iris_label, test_size=0.2
)

knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(train_data, train_label)

y_pred = knn.predict(test_data)  # 預測.predict

print("預測結果")
print(y_pred)

print("正確答案")
print(test_label)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("make_blobs 產生測試資料")

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

print(dx.shape)
print(dy.shape)
# print(dx)
# print(dy)

plt.subplot(121)
plt.scatter(dx.T[0], dx.T[1], c=dy, cmap="Dark2")
plt.title("dx的分佈狀況, dy是用顏色表示")
plt.grid(True)

# StandardScaler
# 將資料常態分布化，平均值會變為0, 標準差變為1，使離群值影響降低
# MinMaxScaler與StandardScaler類似
dx_std = StandardScaler().fit_transform(dx)

plt.subplot(122)
plt.scatter(dx_std.T[0], dx_std.T[1], c=dy, cmap="Dark2")
plt.title("經過 StandardScaler")
plt.grid(True)

plt.show()

# 分割訓練資料集和測試資料集
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

print(dx.shape)
print(dx_train.shape)
print(dx_test.shape)

print(dy.shape)
print(dy_train.shape)
print(dy_test.shape)

knn = KNeighborsClassifier(n_neighbors=5)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(dx_train, dy_train)  # 學習訓練.fit

y_pred = knn.predict(dx_test)  # 預測.predict
print(y_pred)

print(dy_test)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

knn = KNeighborsClassifier()  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X_train, y_train)  # 學習訓練.fit

y_pred = knn.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))  # 評価

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
print(y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 生成數據
centers = [[-2, 2], [2, 2], [0, 4]]
X, y = make_blobs(n_samples=60, centers=centers, random_state=9487, cluster_std=0.60)

# 畫出數據
c = np.array(centers)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 畫出樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="orange")  # 畫出中心點

plt.show()

k = 5
knn = KNeighborsClassifier(n_neighbors=k)  # K近鄰演算法（K Nearest Neighbor, KNN）

knn.fit(X, y)

# 進行預測
X_sample = [0, 2]
X_sample = np.array(X_sample).reshape(1, -1)

y_pred = knn.predict(X_sample)  # 預測.predict

neighbors = knn.kneighbors(X_sample, return_distance=False)

# 畫出示意圖
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="k")  # 中心點
plt.scatter(X_sample[0][0], X_sample[0][1], marker="x", s=100, cmap="cool")  # 待預測的點

for i in neighbors[0]:
    # 預測點與距離最近的 5 個樣本的連線
    plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], "k--", linewidth=0.6)

plt.show()

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
knn.fit(X, y)

# 生成足夠密集的點并進行預測
T = np.linspace(0, 5, 500)[:, np.newaxis]

y_pred = knn.predict(T)  # 預測.predict
print(knn.score(X, y))

# 畫出擬合曲線
plt.scatter(X, y, c="g", label="data", s=100)  # 畫出訓練樣本
plt.plot(T, y_pred, c="k", label="prediction", lw=4)  # 畫出擬合曲線
plt.title("KNeighborsRegressor (k = %i)" % k)
plt.axis("tight")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target

print(iris_X[:2, :])
print(iris_y)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(iris_X, iris_y, test_size=0.2)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print(knn.predict(X_test))
print(y_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# from __future__ import print_function
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()
X = iris.data
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(knn.score(X_test, y_test))

""" some NG
# this is cross_val_score #
from sklearn.cross_validation import cross_val_score

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=5, scoring="accuracy")
print(scores)

# this is how to use cross_val_score to choose model and configs #
from sklearn.cross_validation import cross_val_score
import matplotlib.pyplot as plt

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
plt.show()
"""
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
