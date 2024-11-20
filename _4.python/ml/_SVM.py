"""
機器學習 SVM

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數
f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk), 我們想知道這
f(x)=y

其中的 y 就是某一個類別。

這種學函數的方法, 又可以分為:

1. supervised learning
2. unsupervised learning

1. supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。
2. unsupervised learning 我們不知道答案, 卻要電腦自己去學!

最基本的方式, 一個是 SVM, 一個是 K-Means。

# Supervised Learning SVM

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

from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個

from sklearn.svm import SVC
from sklearn.svm import LinearSVC  # 線性支援向量機 (Linear SVM)

print("------------------------------------------------------------")  # 60個

plt.figure(
    num="SVM 支援向量機",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# SVM 支援向量機
# 簡單的分類, 用 SVM 來做分類
# 假設我們有6個點, 有2個類別
# 支持向量機, 大家都用英文縮寫 SVM 稱呼。是一個用曲線把資料分隔的辦法。
# 在高維度的時候自然就是曲面 (超曲面) 分隔資料的方法。
# 打開一個 SVM 的函數學習機 (SVC 是 SVM 裏面負責做分類的)

# 原始資料x
x = np.array([[5, 0], [5, -5], [0, -5], [0, 5], [-5, 5], [-5, 0]])
# 目標y
y = np.array([1, 1, 1, 2, 2, 2])

print("x全部")
print(x)
print("x全部")
print(x[:])
print("x之x座標")
print(x[:, 0])
print("x之y座標")
print(x[:, 1])

plt.subplot(231)
plt.scatter(x[:, 0], x[:, 1], c=y, s=100, cmap="Paired")  # c = y 就是指定顏色, 不同類別不同色
xmin, xmax, ymin, ymax = -8, 8, -8, 8
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
plt.title("原始資料, 6個點, 2個類別")

clf = SVC()  # SVM 函數學習機
# clf = SVC(gamma = 'auto')  # SVM 函數學習機

clf.fit(x, y)  # 學習訓練.fit

y_pred = clf.predict(x)  # 預測.predict

print("原始 x 資料 :", x)
print("原始 y 資料 :", y, "\t=> 目標")
print("用原始 x 資料預測的結果 :", y_pred)

print("預測結果")
xx, yy = -0.8, -1
print(clf.predict([[xx, yy]]))  # 預測.predict

xx = yy = np.arange(-7, 7, 0.2)
X, Y = np.meshgrid(xx, yy)
P = np.c_[X.ravel(), Y.ravel()]
z = clf.predict(P)  # 預測.predict
Z = z.reshape(X.shape)

print("------------------------------")  # 30個

print("顯示結果 1")

plt.subplot(232)
plt.contourf(X, Y, Z, alpha=0.3, cmap="Paired")
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="Paired")
plt.title("預測的結果1")

print("------------------------------")  # 30個

print("顯示結果 2")
x1, x2 = np.meshgrid(np.arange(-7, 7, 0.2), np.arange(-7, 7, 0.2))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)  # 預測.predict

z = Z.reshape(x1.shape)

plt.subplot(233)
plt.contourf(x1, x2, z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=100, c=y)
plt.title("預測的結果2")

print("------------------------------")  # 30個

print("顯示結果 3")

gd = np.array([[i, j] for i in np.arange(-7, 7, 0.2) for j in np.arange(-7, 7, 0.2)])

gdc = clf.predict(gd)  # 預測.predict

plt.subplot(234)
# plt.scatter(gd[:, 0], gd[:, 1], s = 100, c = gdc)
plt.scatter(gd[:, 0], gd[:, 1], s=100, c=2 - gdc)
plt.scatter(x[:, 0], x[:, 1], s=100, c=y)  # 依據y給定顏色
plt.scatter(xx, yy, c="r", s=100)
plt.title("預測的結果3")

print("------------------------------")  # 30個

print("顯示結果 4")

x1, x2 = np.meshgrid(np.arange(-7, 7, 0.2), np.arange(-7, 7, 0.2))
X = np.c_[x1.ravel(), x2.ravel()]
c = clf.predict(X)  # 預測.predict

plt.subplot(235)
plt.scatter(X[:, 0], X[:, 1], s=10, c=c)
plt.title("預測的結果4")

print("------------------------------")  # 30個

print("顯示結果 5")

x = np.linspace(-7, 7, 30)
y = np.linspace(-7, 7, 30)
X, Y = np.meshgrid(x, y)

# ravel 拉平法
X = X.ravel()
Y = Y.ravel()
plt.scatter(X, Y)

# zip 高級組合法

xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
list(zip(xx, yy))

Z = clf.predict(list(zip(X, Y)))  # 預測.predict

plt.subplot(236)
plt.scatter(X, Y, s=50, c=Z)
plt.title("預測的結果5")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.figure(
    num="SVM 支援向量機",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 生個「像樣點」的假數據
# 用 sklearn 生一些「像真的一樣」的數據
# 用 make_classification 製造分類數據

from sklearn.datasets import make_classification

# n_features 是指 x 的參數要幾個, n_classes 是你要分成幾類
x, y = make_classification(
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    n_classes=3,
    random_state=9487,
)
plt.subplot(231)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("用 make_classification 造數據, 3群")
plt.grid()

"""
print(len(x))
print(len(y))
print(x)
print(y)
"""

clf = SVC()  # SVM 函數學習機
# clf = SVC(gamma = 'auto')  # SVM 函數學習機

clf.fit(x, y)  # 學習訓練.fit

y_pred = clf.predict(x)  # 預測.predict

print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

# 看看SVM, 把訓練資料學得怎麼樣
plt.subplot(232)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y_pred)
plt.grid()

# 如果沒錯的會用一個顏色, 錯了就用其他顏色表示
plt.subplot(233)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y_pred - y)
plt.title("畫出預測差異")
plt.grid()

# 方法一 點圖
gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 4, 0.4)])

gdc = clf.predict(gd)  # 預測.predict
plt.subplot(234)
plt.scatter(gd[:, 0], gd[:, 1], s=100, c=gdc)
plt.title("點圖")
plt.grid()

# 方法二 等高線圖
x1, x2 = np.meshgrid(np.arange(-4, 4, 0.02), np.arange(-3, 4, 0.02))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)  # 預測.predict

z = Z.reshape(x1.shape)

plt.subplot(235)
plt.contourf(x1, x2, z, alpha=0.3)
plt.scatter(x[:, 0], x[:, 1], s=100, c=y)
plt.title("等高線圖")
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.metrics import accuracy_score

# Load dataset
iris = datasets.load_iris()

# Prepare data
X = iris.data[:, :2]  # We only take the first two features
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# Create SVM classifier object
svm = SVC(kernel="linear")  # SVM 函數學習機

# Train SVM classifier
svm.fit(X_train, y_train)  # 學習訓練.fit

# Predict target values for test data
y_pred = svm.predict(X_test)  # 預測.predict

# Evaluate accuracy of SVM classifier
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy of SVM classifier: {:.2f}".format(accuracy))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_gaussian_quantiles
from sklearn.metrics import accuracy_score

X, y = make_gaussian_quantiles(n_features=2, n_classes=2, n_samples=300)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

model = SVC()  # SVM 函數學習機

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性支援向量機 (Linear SVM)

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
dx_std = scaler.fit_transform(dx)  # STD特徵縮放

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)
# 訓練組8成, 測試組2成

linear_svm = LinearSVC()  # SVM 函數學習機

linear_svm.fit(dx_train, dy_train)  # 學習訓練.fit

predictions = linear_svm.predict(dx_test)  # 預測.predict

print(linear_svm.score(dx_train, dy_train))
print(linear_svm.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 非線性 SVM

from sklearn.datasets import make_moons

dx, dy = make_moons(n_samples=500, noise=0.15)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
xx = scaler.fit_transform(dx)  # STD特徵縮放

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, dy_train, dy_test = train_test_split(xx, dy, test_size=0.2)
# 訓練組8成, 測試組2成

linear_svm = LinearSVC()  # SVM 函數學習機

linear_svm.fit(dx_train, dy_train)  # 學習訓練.fit

predictions = linear_svm.predict(dx_test)  # 預測.predict

svm = SVC()  # SVM 函數學習機

svm.fit(dx_train, dy_train)  # 學習訓練.fit

predictions = svm.predict(dx_test)  # 預測.predict

print(linear_svm.score(dx_train, dy_train))

print(linear_svm.score(dx_test, dy_test))

print(svm.score(dx_train, dy_train))

print(svm.score(dx_test, dy_test))

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


print("------------------------------------------------------------")  # 60個

"""
xmin, xmax, ymin, ymax = -8, 8, -8, 8
#plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
"""
