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

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

"""
2019.01.02 更新 ：
由於 sklearn.cross_validation 方法要被棄用了，所以必須改成 sklearn.model_selection。
"""

iris = datasets.load_iris()

#定義特徵資料：
iris_data = iris.data
iris_label = iris.target

#可以印出前三筆資料：

cc = iris_data[0:3]
print(cc)

train_data , test_data , train_label , test_label = train_test_split(iris_data,iris_label,test_size=0.2)

knn = KNeighborsClassifier() #使用KNeighbors分類法

knn.fit(train_data,train_label)

y_pred = knn.predict(test_data)

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
#print(dx)
#print(dy)

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

# k 最近鄰演算法 (KNN)
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(dx_train, dy_train)  # 學習訓練.fit

predictions = knn.predict(dx_test)  # 預測.predict

print(dy_test)
print(predictions)
print(knn.score(dx_train, dy_train))
print(knn.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# データ生成
X, y = make_moons(noise=0.3)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = KNeighborsClassifier()

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))  # 評価

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
