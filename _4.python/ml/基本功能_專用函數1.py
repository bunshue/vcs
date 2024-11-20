"""
基本功能_專用函數1

使用 scikit-learn(sklearn) 的 函數

預設方法建立資料集

一些簡易的運算

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

from sklearn.datasets import make_regression  # 迴歸資料集
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_classification  # 分類資料集
from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.datasets import make_circles  # 圓形分佈的資料集

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

plt.figure(
    num="sklearn內建資料集集合",
    figsize=(16, 9),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

print("------------------------------")  # 30個
plt.subplot(231)
plt.title("make_regression 迴歸資料集")

X, y, coef = make_regression(
    n_samples=100, n_features=1, noise=20, coef=True, random_state=9487
)
print(X.shape)

print(coef)

plt.scatter(X[:, 0], y)
plt.plot([min(X), max(X)], [min(X) * coef, max(X) * coef], "r")

print("------------------------------")  # 30個
plt.subplot(232)
plt.title("make_blobs 集群資料集")

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

print("------------------------------")  # 30個
plt.subplot(233)
plt.title("make_classification 分類資料集")

print("分類資料集")

X, y = make_classification(
    n_samples=100,
    n_classes=3,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=9487,
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

print("------------------------------")  # 30個
plt.subplot(234)
plt.title("make_moons 非線性的資料集")

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


print("------------------------------")  # 30個
plt.subplot(235)
plt.title("make_circles 圓形分佈的資料集")

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

print("------------------------------")  # 30個
plt.subplot(236)
plt.title("xxx")


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

X, Y = make_regression(
    n_samples=10, n_features=1, n_targets=1, noise=1.5, random_state=9487
)
cc = X.shape, Y.shape
print(cc)


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

print("分類效果評估")
print("FP/FN/TP/TN")

y_pred = [0, 0, 0, 1, 1, 1, 0, 1, 0, 0]  # 預測值
y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]  # 實際值

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_real, y_pred)
tn, fp, fn, tp = cm.ravel()
print("tn", tn, "fp", fp, "fn", fn, "tp", tp)

print("準確率")
from sklearn.metrics import accuracy_score

print(accuracy_score(y_real, y_pred))

print("召回率")
from sklearn.metrics import recall_score

print(recall_score(y_real, y_pred))

print("精度")
from sklearn.metrics import precision_score

print(precision_score(y_real, y_pred))

print("F值")

from sklearn.metrics import f1_score
from sklearn.metrics import fbeta_score

print(f1_score(y_real, y_pred))  # 計算f1
print(fbeta_score(y_real, y_pred, beta=2))  # 計算fn

print("Logloss")
from sklearn.metrics import log_loss

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
print(log_loss(y_real, y_score))

print("ROC曲線和AUC")
from sklearn.metrics import roc_auc_score, roc_curve

print(roc_auc_score(y_real, y_score))  # AUC值

fpr, tpr, thresholds = roc_curve(y_real, y_score)
plt.plot(fpr, tpr)  # 繪圖

# plt.show()

# P-R曲線
from sklearn.metrics import precision_recall_curve

precision, recall, _ = precision_recall_curve(y_real, y_score)
plt.plot(recall, precision)

# plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多指標評分")

from sklearn.metrics import classification_report

y_real = [0, 1, 1, 1, 1, 1, 0, 0, 0, 0]
y_score = [0.9, 0.75, 0.86, 0.47, 0.55, 0.56, 0.74, 0.22, 0.5, 0.26]
y_pred = [round(i) for i in y_score]
print(classification_report(y_real, y_pred))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.svm import SVC

a = np.array([[10, 2.7, 3.6], [-100, 5, -2], [120, 20, 40]], dtype=np.float64)
print(a)
print(preprocessing.scale(a))

X, y = make_classification(
    n_samples=300,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    random_state=22,
    n_clusters_per_class=1,
    scale=100,
)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()

X = preprocessing.scale(X)  # normalization step
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
机器学习笔记：常用数据集之scikit-learn生成分类和聚类数据集

本文介绍分类和聚类数据集的生成，包括以下9个接口函数，其中，

有六个是用于单标签类数据生成：

(1) make_blobs()
(2) make_classification()
(3) make_gaussian_quantiles()
(4) make_hastie_10_2()
(5) make_circles()
(6) make_moons()

一个用于多标签类数据生成:
(7) make_multilabel_classification()

还有两个用于双聚类数据集生成：
(8) make_biclusters
(9) make_checkerboard
"""

"""
2. make_classification¶

make_blobs()和make_classification()都用于生成多类别的数据集，
每个类别都是由一个或者多个正态分布簇(normally-distributed cluster)构成。

make_blobs对于各簇的中心和标准偏差提供了更方便的控制选项，
通常用于聚类算法的演示。而make_classification则更加侧重于通过各种手段导入各种“噪声”的影响，
比如说，相关的、冗余的、没有信息量的特征；每个类分成多个正态分布簇；特征空间的线性变换等等。
"""

# make_classification()生成二分类数据集

X, y = make_classification(
    n_samples=1000,
    n_features=5,
    n_redundant=0,
    n_clusters_per_class=1,
    n_informative=1,
    n_classes=2,
    random_state=20,
)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

print(X.shape, y.shape)
plt.show()

"""
3. make_blobs
'blob'的意思可能跟cluster差不多，都是簇、团、块的意思。
以下第一个例子生成了3个blobs，第二个例子生成了4个blobs。
注意，在第3个例子中，显式地制指定了4个blobs的中心各簇的样本数，以及各簇的standard deviation.
"""

# make_blobs: Generate isotropic Gaussian blobs for clustering. Of course, can also be used for classfication problem.

X, y = make_blobs(n_samples=1000, centers=3, n_features=2, random_state=10)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue", 2: "y"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])


plt.show()


X, y = make_blobs(
    n_samples=[100, 300, 250, 400],
    n_features=2,
    centers=[[100, 120], [250, 300], [700, 150], [300, 500]],
    cluster_std=50,
    random_state=111,
)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue", 2: "y", 3: "green"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.show()


""" 
4. make_moons
        make_moons()函数生成一个二分类问题数据集，
        它生成两个半月形对应两个分类。可以通过noise参数来控制噪声量。
        适合于非线性分类算法的演示。
"""

# make_moons: Generate isotropic Gaussian blobs for clustering.
# 经常用于非线性分类示例。

# generate 2d classification dataset
X, y = make_moons(n_samples=1000, shuffle=True, noise=0.1, random_state=10)
# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots()
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.show()

"""
5. make_circles
顾名思义，每个类别的样本构成一个圆形。
"""
# make_circles: generates a binary classification problem with datasets that fall into concentric circles.
# Make a large circle containing a smaller circle in 2d.
# A simple toy dataset to visualize clustering and classification algorithms, suitable for algorithms that can learn complex non-linear manifolds.


# generate 2d classification dataset
X, y = make_circles(
    n_samples=1000, noise=0.05
)  # 'noise' is used to control the amount of noise in the shapes.
# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=X[:, 0], y=X[:, 1], label=y))
colors = {0: "red", 1: "blue"}
fig, ax = plt.subplots(figsize=[6, 6])
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.show()

"""
6. make_gaussian_quantiles
make_gaussian_quantiles()首先生成一个多维正态分布样本集，然后，将这样本集基于分位点(quantiles)分割成多个(n_classes=3 by default)嵌套的多维同心超球，每个超球属于一类，并使得大致各类的样本基本相等。
基于分位点进行分割是什么意思呢？
以一维正态分布为例，大致来说就是这样分割的。假设n_classes = 3，因此对应的两个分割用的分位点就是33%和66%。取样本中位于[0, 33%]分位区间的作为第一类，位于[33%, 66%]分位区间的作为第二类，位于[66%, 100%]分位区间的作为第三类。对于多维数据，是基于对应的𝜒2分布的分位数来进行分类。
"""
from sklearn.datasets import make_gaussian_quantiles

data, target = make_gaussian_quantiles(n_samples=1500, cov=1.0, n_classes=3)

# scatter plot, dots colored by class value
df = pd.DataFrame(dict(x=data[:, 0], y=data[:, 1], label=target))
colors = {0: "red", 1: "blue", 2: "k"}
fig, ax = plt.subplots(figsize=[6, 6])
grouped = df.groupby("label")
for key, group in grouped:
    group.plot(ax=ax, kind="scatter", x="x", y="y", label=key, color=colors[key])

plt.show()

"""
7. make_hastie_10_2
这个函数是专门用于以下Hastie的机器学习经典教材中例10.2所提及的数据集的生成，用于二分类问题。为一本书中的一个例子专门列了一个函数，确实是很拼。可以看作是make_gaussian_quantiles的一种特例，或者反过来说make_gaussian_quantiles是make_hastie_10_2的推广。
T. Hastie, R. Tibshirani and J. Friedman, “Elements of Statistical Learning Ed. 2”, Springer, 2009.》
该数据集有10个特征，是i.i.d（独立同分布）的标准正态分布，target y定义如下：
y[i] = 1 if np.sum(X[i] ** 2) > 9.34 else -1
"""
from sklearn.datasets import make_hastie_10_2

data, target = make_hastie_10_2(n_samples=1000, random_state=42)

# target[target==-1] = 0  # 原数据集生成的target为[1,-1],这里变换为[1,0]
# target = target.astype('int32') # 变换成整数

df = pd.DataFrame(data)
df["target"] = target

print(df)

"""
这是一个10维的数据，所以不容易以散点图的形式进行图示化。以下通过图示的方式看看各个维度是不是独立同分布（i.i.d）的标准高斯分布。
"""
from scipy.stats import norm

plt.figure(figsize=(20, 6))
for k in range(10):
    df[k].plot(kind="kde", secondary_y=True, label="feature#" + str(k))

x = np.linspace(-8, 8, 1000)
plt.plot(x, norm.pdf(x), "r-", lw=2, alpha=0.6, label="theoretic std norm pdf")

plt.legend()
plt.show()

# 如上图可知，10个特征分量确实基本上都是与标准正态分布吻合的。


"""
8. 多标签数据集生成
多标签数据集用于当存在多各类别，而待分类的数据可能属于其中的一类或者同时属于多个类别，或者甚至不属于任何类别。比如说，当需要识别在一张图像中所包含的交通信号等的类型。一张图片可能不包含信号灯，也可能只包含一个红灯或绿灯或黄灯，也可能同时包含一个红灯和绿灯（如果这张图片覆盖了一个十字路口的两个方向的信号灯的话）。
"""

from sklearn.datasets import make_multilabel_classification as make_ml_clf

x, y = make_ml_clf(n_samples=1000, n_features=10, n_classes=3, random_state=0)
print(x.shape, y.shape)
print(y[:10, :])

"""
可以看出，由于是多分类（本例是3分类）多标签的，所以target(label)采用了one-hot编码的形式，每个数据样本的label中可能有一个或多个1，表示属于1个类别或者多个类别。当然，虽然以上没有显示出来，也存在不属于任何类别的样本，即其label为全零向量。
"""

"""
9. make_biclusters
make_biclusters用于生成具有恒定块对角线结构(constant block diagonal structure)的数组以进行双向聚类。所谓“双向聚类”，是指对变量和实例同时聚类。本数据集可以用于谱协聚类(SpectralCoclustering)算法的示例。
"""

from sklearn.datasets import make_biclusters

data, rows, columns = make_biclusters(
    shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
plt.show()

"""
10. make_checkerboard
make_checkerboard()用于生成一个具有棋盘格结构的数组，以进行双向聚类。
"""
from sklearn.datasets import make_checkerboard

data, rows, columns = make_checkerboard(
    shape=(300, 300), n_clusters=5, noise=5, shuffle=False, random_state=0
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original dataset")
plt.show()

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

X, y = make_regression(n_samples=100, n_features=1, n_targets=1, noise=10)
plt.scatter(X, y)
plt.show()
