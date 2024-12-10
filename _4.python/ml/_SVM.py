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

from common1 import *
from sklearn import datasets
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.datasets import make_classification
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score  # 計算準確率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.svm import SVC  # 非線性SVM函數學習機
from sklearn.svm import LinearSVC  # 線性支援向量機 (Linear SVM)

import sklearn.metrics as metrics


def show():
    plt.show()
    pass


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

clf = SVC()  # 非線性SVM函數學習機
# clf = SVC(gamma = 'auto')  # 非線性SVM函數學習機

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

show()

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

clf = SVC()  # 非線性SVM函數學習機
# clf = SVC(gamma = 'auto')  # 非線性SVM函數學習機

clf.fit(x, y)  # 學習訓練.fit

y_pred = clf.predict(x)  # 預測.predict

print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
# print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

# 直接用SVC的方法算正確率
cc = clf.score(x, y)
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing

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
plt.title("原始資料")
show()

X = preprocessing.scale(X)  # normalization step

plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("原始資料經過正規化")
show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = SVC()  # 非線性SVM函數學習機

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)  # 預測.predict

print("真實答案 :", y_test)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y_test)

cc = np.sum(y_pred.reshape(-1, 1) == y_test.reshape(-1, 1))
# print(cc)
cc = cc * 1.0 / len(y_test)
print("正確率 :", cc)

# 直接用SVC的方法算正確率
cc = clf.score(X_test, y_test)
print("正確率 :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# Prepare data
X = iris.data[:, :2]  # We only take the first two features
y = iris.target

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

clf = SVC(kernel="linear")  # 非線性SVM函數學習機, linear模式

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)  # 預測.predict

# 計算正確率
accuracy = accuracy_score(y_test, y_pred)
print("SVM classifier 之 正確率 : {:.2f}".format(accuracy))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 1  # cluster_std, 資料標準差
# print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
# X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

print("使用 make_moons 產生", N, "筆資料")
X, y = make_moons(n_samples=N, noise=0.15)

# print("使用 make_gaussian_quantiles 產生", N, "筆資料")
# X, y = make_gaussian_quantiles(n_features=2, n_classes=2, n_samples=N)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)  # STD特徵縮放

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

print("同樣的資料, 用不同的SVM函數學習機 做")

print("1. 使用 LinearSVC() 線性支援向量機 (Linear SVM)")
linear_clf = LinearSVC()  # 線性支援向量機 (Linear SVM)
linear_clf.fit(X_train, y_train)  # 學習訓練.fit
# predictions = linear_clf.predict(X_test)  # 預測.predict

cc = linear_clf.score(X_train, y_train)
print("正確率 :", cc)
cc = linear_clf.score(X_test, y_test)
print("正確率 :", cc)

print("2. 使用 SVC() 非線性SVM函數學習機")
clf = SVC()  # 非線性SVM函數學習機
clf.fit(X_train, y_train)  # 學習訓練.fit
y_pred = clf.predict(X_test)  # 預測.predict

cc = clf.score(X_train, y_train)
print("正確率 :", cc)
cc = clf.score(X_test, y_test)
print("正確率 :", cc)

# 計算正確率
accuracy = accuracy_score(y_test, y_pred)
print("SVM classifier 之 正確率 : {:.2f}".format(accuracy))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# # 高级分类器：支持向量机( SVM)与凸优化

# 加载数据集

from scipy import stats
import sklearn.model_selection as cross_validation

# In[2]:
orgData = pd.read_csv("data/date_data.csv")
orgData.describe()

# 提取如下字段进行建模

# 取出後4欄位當訓練資料
# X = orgData.ix[:, :4]
print("取出3欄資料")
X = orgData[["income_rank", "attractive_rank", "assets_rank"]]

# 取出 Dated 欄位 當訓練目標
Y = orgData["Dated"]

# 构建训练集和测试集

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X, Y, test_size=0.4, train_size=0.6, random_state=123
)  # 划分训练集和测试集


# 使用svm，建立支持向量机模型

from sklearn import svm

svcModel = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_data, train_target
)

# 初步评估
test_est = svcModel.predict(test_data)
print(metrics.classification_report(test_target, test_est))  # 计算评估指标

# 进行标准化可以提升高斯核svm的表现
from sklearn import preprocessing

scaler = preprocessing.StandardScaler().fit(train_data)
train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

svcModel1 = svm.SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_scaled, train_target
)
test_est1 = svcModel1.predict(test_scaled)
print(metrics.classification_report(test_target, test_est1))  # 计算评估指标

# 选择最优模型

from sklearn.model_selection import ParameterGrid
from sklearn.model_selection import GridSearchCV

kernel = ("linear", "rbf")
gamma = np.arange(0.01, 1, 0.1)
C = np.arange(0.01, 1.0, 0.1)
grid = {"gamma": gamma, "C": C}

clf_search = GridSearchCV(estimator=svcModel1, param_grid=grid, cv=4)
clf_search.fit(train_scaled, train_target)

best_model = clf_search.best_estimator_
test_est2 = best_model.predict(test_scaled)
print(metrics.classification_report(test_target, test_est2))  # 计算评估指标

best_model

# 画出在svm模型中，两个变量的关系图，可以用于提升感性认识，但一般不能推广到大于两维的情况

train_x = train_scaled[:, 1:3]
train_y = train_target.values
h = 1.0  # step size in the mesh
C = 1.0  # SVM regularization parameter
svc = svm.SVC(kernel="linear", C=C).fit(train_x, train_y)
rbf_svc = svm.SVC(kernel="rbf", gamma=0.5, C=1).fit(train_x, train_y)
poly_svc = svm.SVC(kernel="poly", degree=3, C=C).fit(train_x, train_y)
lin_svc = svm.LinearSVC(C=C).fit(train_x, train_y)

# create a mesh to plot in
x_min, x_max = train_x[:, 0].min() - 1, train_x[:, 0].max() + 1
y_min, y_max = train_x[:, 1].min() - 1, train_x[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# title for the plots
titles = [
    "SVC with linear kernel",
    "LinearSVC (linear kernel)",
    "SVC with RBF kernel",
    "SVC with polynomial (degree 3) kernel",
]
plt.figure(figsize=(8, 8))
for i, clf in enumerate((svc, lin_svc, rbf_svc, poly_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.7)

    # Plot also the training points
    plt.scatter(train_x[:, 0], train_x[:, 1], c=train_y, cmap=plt.cm.coolwarm)
    plt.xlabel("Attractive")
    plt.ylabel("Assets")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("用SVM做分類, 有監督學習")

iris = datasets.load_iris()

X = iris.data
Y = iris.target

X_SVM = X[:, :2]  # 取出前兩欄

clf = SVC()

clf.fit(X_SVM, Y)  # 學習訓練.fit

y_predict = clf.predict(X_SVM)

plt.scatter(X_SVM[:, 0], X_SVM[:, 1], c=y_predict)

show()

# 再去做預測

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500
GROUPS = 3
X, y = make_blobs(n_samples=N, centers=GROUPS, n_features=2)

from sklearn.model_selection import cross_val_score  # Cross Validation

print("使用 SVC")
# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
clf = SVC()
# clf = SVC(gamma = 'scale')

scores = cross_val_score(clf, X, y, cv=5)
print("看一下五次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)

d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
svm_model = LinearSVC()

# 建立訓練數據模型
svm_model.fit(dx_train, label_train)  # 學習訓練.fit

# 對測試數據做預測
pred = svm_model.predict(dx_test)

# 輸出測試數據的 label
print(label_test)

# 輸出預測數據的 label
print(pred)

# 輸出準確性
print(f"訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {svm_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data, label = make_moons(n_samples=200, noise=0.2, random_state=9487)

d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm_model = LinearSVC()

svm_model.fit(dx_train, label_train)  # 學習訓練.fit

pred = svm_model.predict(dx_test)

# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")
print("=" * 50)

# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm = SVC()
svm.fit(dx_train, label_train)
pred = svm.predict(dx_test)

# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {svm.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {svm.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def plot_hyperplane(clf, X, y, h=0.02, draw_sv=True, title="hyperplan"):
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap="hot", alpha=0.5)

    markers = ["o", "s", "^"]
    colors = ["b", "r", "c"]
    labels = np.unique(y)
    for label in labels:
        plt.scatter(
            X[y == label][:, 0],
            X[y == label][:, 1],
            c=colors[label],
            marker=markers[label],
        )
    if draw_sv:
        sv = clf.support_vectors_
        plt.scatter(sv[:, 0], sv[:, 1], c="y", marker="x")


X, y = make_blobs(n_samples=100, centers=2, random_state=9487, cluster_std=0.3)
clf = sklearn.svm.SVC(C=1.0, kernel="linear")
clf.fit(X, y)

plt.figure(figsize=(12, 4))
plot_hyperplane(clf, X, y, h=0.01, title="Maximum Margin Hyperplan")

show()

print("------------------------------")  # 30個

X, y = make_blobs(n_samples=100, centers=3, random_state=9487, cluster_std=0.8)
clf_linear = sklearn.svm.SVC(C=1.0, kernel="linear")
clf_poly = sklearn.svm.SVC(C=1.0, kernel="poly", degree=3)
clf_rbf = sklearn.svm.SVC(C=1.0, kernel="rbf", gamma=0.5)
clf_rbf2 = sklearn.svm.SVC(C=1.0, kernel="rbf", gamma=0.1)

plt.figure(figsize=(10, 10))

clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = [
    "Linear Kernel",
    "Polynomial Kernel with Degree=3",
    "Gaussian Kernel with $\gamma=0.5$",
    "Gaussian Kernel with $\gamma=0.1$",
]
for clf, i in zip(clfs, range(len(clfs))):
    clf.fit(X, y)
    plt.subplot(2, 2, i + 1)
    plot_hyperplane(clf, X, y, title=titles[i])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# データ生成
centers = [(-1, -0.125), (0.5, 0.5)]

N = 50
print("產生", N, "筆資料 2維 2群")
X, y = make_blobs(n_samples=N, n_features=2, centers=centers, cluster_std=0.3)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LinearSVC()

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("SVM")

# 支持向量机 (SVM)

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 第四步：特征量化  # Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.fit_transform(X_test)  # STD特徵縮放

# 第五步：适配SVM到训练集合
# Fitting SVM to the Training set

classifier = SVC(kernel="linear", random_state=0)

classifier.fit(X_train, y_train)  # 學習訓練.fit

SVC(
    C=1.0,
    cache_size=200,
    class_weight=None,
    coef0=0.0,
    decision_function_shape="ovr",
    degree=3,
    gamma="auto",
    kernel="linear",
    max_iter=-1,
    probability=False,
    random_state=0,
    shrinking=True,
    tol=0.001,
    verbose=False,
)

# 第六步：预测测试集合结果
# Predicting the Test set results
y_pred = classifier.predict(X_test)

# 第七步：创建混淆矩阵
# Making the Confusion Matrix

cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

# 第八步：训练集合结果可视化
# Visualising the Training set results
from matplotlib.colors import ListedColormap

X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("SVM (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()
show()


# 第九步：测试集合结果可视化

from matplotlib.colors import ListedColormap

X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)
plt.contourf(
    X1,
    X2,
    classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
    alpha=0.75,
    cmap=ListedColormap(("red", "green")),
)
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(
        X_set[y_set == j, 0],
        X_set[y_set == j, 1],
        c=ListedColormap(("red", "green"))(i),
        label=j,
    )
plt.title("SVM (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_01_self_training

# 自我訓練(Self-training)測試

from sklearn.semi_supervised import SelfTrainingClassifier

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 設定 30% 資料為沒有標註(-1)

rng = np.random.RandomState(0)
y_rand = rng.rand(y_train.shape[0])
y_30 = np.copy(y_train)
y_30[y_rand < 0.3] = -1
cc = np.count_nonzero(y_30 == -1)
print(cc)

y_30_index = np.where(y_30 == -1)[0]
print(y_30_index)

print(type(y_30_index))

# 模型訓練

base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
clf = SelfTrainingClassifier(base_classifier).fit(X_train, y_30)  # 學習訓練.fit

# 繪製決策邊界

# 建立 mesh grid
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 每個標籤不同顏色(RGB)
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# 繪製等高線
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.axis("off")

# 繪製實際點
colors = [color_map[y] for y in y_30]
plt.scatter(X_train[:, 0], X_train[:, 1], c=colors, edgecolors="black")

show()

# SVM 模型評估
base_classifier.fit(X_train, y_30)  # 學習訓練.fit
cc = base_classifier.score(X_test, y_test)
print(cc)
# 0.6666666666666666

# Self-training 模型評估
cc = clf.score(X_test, y_test)
print(cc)
# 0.7666666666666667

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 完整資料進行模型評估

rng = np.random.RandomState(42)
X, y = datasets.load_iris(return_X_y=True)
random_unlabeled_points = rng.rand(y.shape[0]) < 0.3
y[random_unlabeled_points] = -1

svc = SVC(probability=True, gamma="auto")

self_training_model = SelfTrainingClassifier(svc)

self_training_model.fit(X, y)  # 學習訓練.fit

"""
SelfTrainingClassifier(base_estimator=SVC(gamma='auto', probability=True))
"""

svc.fit(X[y >= 0], y[y >= 0])  # 學習訓練.fit
cc = svc.score(X, y)
print(cc)

# 0.66

X, y = datasets.load_iris(return_X_y=True)
cc = self_training_model.score(X, y)
print(cc)

# 0.9733333333333334

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 繪製混淆矩陣

from sklearn import svm

# 載入資料
ds = datasets.load_iris()
X, y = ds.data, ds.target

# 分割資料
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = svm.SVC(kernel="linear", C=0.01)

clf.fit(X_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test)

# 設定顯示小數點位數
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
titles_options = [("正常的混淆矩陣", None), ("正規化混淆矩陣", "true")]

f, axes = plt.subplots(1, 2, figsize=(14, 5), sharey="row")
for i, (title, normalize) in enumerate(titles_options):
    cm = ConfusionMatrixDisplay.from_predictions(
        y_test,
        y_pred,
        ax=axes[i],
        cmap=plt.cm.Blues,
        display_labels=ds.target_names,
        normalize=normalize,
    )
    #     cm.plot(ax=axes[i])
    cm.ax_.set_title(title, fontsize=16)

show()

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
# os.chdir(r'D:\Python_book\12SVM')
# pd.set_option('display.max_columns', None)
