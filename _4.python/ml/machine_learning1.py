"""
使用 scikit-learn(sklearn) 的 函數

預設方法建立資料集

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

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import make_regression
from sklearn.datasets import make_circles
from sklearn.datasets import make_moons

print("------------------------------------------------------------")  # 60個

import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

print("------------------------------------------------------------")  # 60個

import sklearn
from sklearn import datasets, svm, metrics

print(sklearn.__version__)
print(dir(datasets))
print(sklearn)

print("------------------------------------------------------------")  # 60個

print("分類資料集")

X, y = make_classification(
    n_samples=100,
    n_classes=3,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=5,
)
print(X.shape)

# 繪圖
# 樣本點的形狀
markers = ["x", "o", "^"]

# 針對類別各畫一個散佈圖
for k in range(3):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, marker=markers[k], s=50)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("集群資料集")

X, y, centers = make_blobs(
    n_samples=100, centers=3, cluster_std=1, n_features=2, return_centers=True
)
print(X.shape)
print(centers)

# 樣本點的形狀
markers = ["x", "o", "^"]

# 針對類別各畫一個散佈圖
for k in range(3):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, marker=markers[k], s=50)

# 繪製集群中心點
X_0 = []
X_1 = []
for i in range(len(centers)):
    X_0.append(centers[i, 0])
    X_1.append(centers[i, 1])
plt.scatter(X_0, X_1, marker="s", s=200, alpha=0.5)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("迴歸資料集")

X, y, coef = make_regression(
    n_samples=100, n_features=1, noise=20, coef=True, random_state=123
)
print(X.shape)

print(coef)

plt.scatter(X[:, 0], y)
plt.plot([min(X), max(X)], [min(X) * coef, max(X) * coef], "r")
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("非線性的資料集")

X, y = make_moons(n_samples=100, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("圓形分佈的資料集")

X, y = make_circles(n_samples=100, noise=0.05)
print(X.shape)

# 針對類別各畫一個散佈圖
colors = ["red", "blue"]
for k in range(2):
    X_0 = []
    X_1 = []
    for i in range(len(y)):
        if y[i] == k:
            X_0.append(X[i, 0])
            X_1.append(X[i, 1])
            plt.scatter(X_0, X_1, s=50, c=colors[k])
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



"""
sklearn 使用make_regression生成回归样本数据及NumPy拟合

1. 介绍
sklearn的make_regression函数能生成回归样本数据。

2. 函数语法
make_regression(n_samples=100, n_features=100, n_informative=10, n_targets=1, bias=0.0, 
                effective_rank=None, tail_strength=0.5, noise=0.0, shuffle=True, coef=False, random_state=None)

3. 参数说明：
n_samples：样本数
n_features：特征数(自变量个数)
n_informative：参与建模特征数
n_targets：因变量个数
noise：噪音
bias：偏差(截距)
coef：是否输出coef标识
random_state：随机状态若为固定值则每次产生的数据都一样

"""

from sklearn.datasets import make_regression

X, Y = make_regression(
    n_samples=10, n_features=1, n_targets=1, noise=1.5, random_state=1
)


X.shape, Y.shape

import matplotlib.pyplot as plt

plt.scatter(
    X,  # x坐标
    Y,  # y坐标
)
plt.show()


# 5. 用NumPy实现拟合
# Numpy拟合基于最小二乘法

plt.scatter(
    X,  # x坐标
    Y,  # y坐标
)

import numpy as np

# 用一次多项式拟合，相当于线性拟合
z1 = np.polyfit(X.reshape(10), Y, 1)
p1 = np.poly1d(z1)
print(z1)
print(p1)

y = z1[0] * X + z1[1]
plt.plot(X, y, c="red")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
from sklearn.datasets import make_regression
N = 50
X, y = make_regression(n_samples=N, n_features=3)
print(X.shape, y.shape)
print(X)
print(y)

y = y.reshape((-1, 1))
#print(y)

from sklearn.linear_model import LinearRegression

linear_regression = LinearRegression()
linear_regression.fit(X, y)

y_pred_sk = linear_regression.predict(X)
#print(y_pred_sk)

plt.figure(figsize=(9, 4))

plt.plot(y, color="r", linewidth=10)
plt.plot(y_pred_sk, color="g", linewidth=4)

#plt.legend()

plt.show()

print('------------------------------')	#30個


def gd(X, y, theta, l_rate, iterations):
    cost_history = [0] * iterations

    m = X.shape[0]

    for epoch in range(iterations):
        y_hat = X.dot(theta)

        loss = y_hat - y

        gradient = X.T.dot(loss) / m

        theta = theta - l_rate * gradient

        cost = np.dot(loss.T, loss)

        cost_history[epoch] = cost[0, 0]

    return theta, cost_history


def sgd(X, y, theta, l_rate, iterations):
    cost_history = [0] * iterations

    for epoch in range(iterations):
        for i, row in enumerate(X):
            yhat = np.dot(row, theta)

            loss = yhat[0] - y[i]

            theta = theta - l_rate * loss * row.reshape((-1, 1))

            cost_history[epoch] += loss**2

    return theta, cost_history


def predict(X, theta):
    return np.dot(X, theta)


theta = np.random.rand(X.shape[1], 1)

iterations = 100

l_rate = 0.1

theta, cost_history = gd(X, y, theta, l_rate, iterations)

print(theta.T)

# array([[ 1.12259549, 64.22439151, 84.34968956]])

y_predict = predict(X, theta)

y_predict = predict(X, theta)

plt.figure(figsize=(9, 4))

plt.plot(y, color="r")
plt.plot(y, alpha=0.3, linewidth=5)
plt.plot(y_predict, color="g")
plt.plot(y_predict, linewidth=2)

plt.show()

print(linear_regression.coef_)
# array([[48.54597102, 82.31351886,  8.52184984]])

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

print("------------------------------------------------------------")  # 60個
