"""
SVM 支持向量机
用SVM做分類, 有監督學習

Support Vector Machine
    Support vector machine (SVM) is a binary linear classifier
    There are tricks to make SVM able to solve non-linear problems
    There are extensions which allows using SVM to multiclass classification or regression
    SVM is a supervised learning algorithm
    There are extensions which allows using SVM for (unsupervised) clustering

Linear SVM
    Lets consider a training dataset of N samples ( x → 1 , y 1 ) , ⋯ , ( x → N , y N )
    x → i is D -dimensional vector representing features
    y i is a class label, for convenience
    Missing or unrecognized delimiter for \left
    $y_i = \left{-1, 1\right}$
    At this point we assume that classes are linearly separable
    For visualization purpose lets use D = 2
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
import sklearn.linear_model
import sklearn.metrics as metrics
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons  # 非線性的資料集
from sklearn.datasets import make_classification  # 分類資料集
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score  # 計算準確率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.svm import SVC  # 非線性SVM函數學習機
from sklearn.svm import LinearSVC  # 線性支援向量機 (Linear SVM)
from sklearn import metrics
from sklearn import tree
from sklearn import svm
from matplotlib.colors import ListedColormap


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def plot_gallery(images, titles, h, w, n_row=3, n_col=4):
    """Helper function to plot a gallery of portraits"""
    plt.figure(figsize=(1.8 * n_col, 2.4 * n_row))
    plt.subplots_adjust(bottom=0, left=0.01, right=0.99, top=0.90, hspace=0.35)
    for i in range(n_row * n_col):
        plt.subplot(n_row, n_col, i + 1)
        plt.imshow(images[i].reshape((h, w)), cmap=plt.cm.gray)
        plt.title(titles[i], size=12)
        plt.xticks(())
        plt.yticks(())


def title(y_pred, y_test, target_names, i):
    pred_name = target_names[y_pred[i]].rsplit(" ", 1)[-1]
    true_name = target_names[y_test[i]].rsplit(" ", 1)[-1]
    # return "predicted: %s\ntrue:      %s" % (pred_name, true_name)
    return f"predicted: {pred_name}\ntrue:         {true_name}"


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
plt.contourf(X, Y, Z, alpha=0.3, cmap="Paired")  # contourf 等高線面積圖
plt.scatter(x[:, 0], x[:, 1], c=y, cmap="Paired")
plt.title("預測的結果1")

print("------------------------------")  # 30個

print("顯示結果 2")
x1, x2 = np.meshgrid(np.arange(-7, 7, 0.2), np.arange(-7, 7, 0.2))
X = np.c_[x1.ravel(), x2.ravel()]
Z = clf.predict(X)  # 預測.predict

z = Z.reshape(x1.shape)

plt.subplot(233)
plt.contourf(x1, x2, z, alpha=0.3)  # contourf 等高線面積圖
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

print("分類資料集")

N = 100  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
# n_classes 是你要分成幾類
print("make_classification,", N, "個樣本,", M, "個特徵")

x, y = make_classification(
    n_samples=N,
    n_features=2,
    n_redundant=0,
    n_informative=2,
    n_clusters_per_class=1,
    n_classes=3,
    random_state=9487,
)
"""
print(len(x))
print(len(y))
print(x.shape)
print(y.shape)
"""
plt.subplot(231)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("用 make_classification 造數據, 3群")
plt.grid()

clf = SVC()  # 非線性SVM函數學習機
# clf = SVC(gamma = 'auto')  # 非線性SVM函數學習機

clf.fit(x, y)  # 學習訓練.fit

y_pred = clf.predict(x)  # 預測.predict
"""
print("真實答案 :", y)
print("預測結果 :", y_pred)
print("預測差值 :", y_pred - y)
"""
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
plt.contourf(x1, x2, z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(x[:, 0], x[:, 1], s=100, c=y)
plt.title("等高線圖")
plt.grid()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("分類資料集")

N = 300  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
# n_classes 是你要分成幾類
print("make_classification,", N, "個樣本,", M, "個特徵")

X, y = make_classification(
    n_samples=N,
    n_features=M,
    n_redundant=0,
    n_informative=2,
    random_state=22,
    n_clusters_per_class=1,
    scale=100,
)

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("原始資料")

X = preprocessing.scale(X)  # normalization step

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("原始資料經過正規化")

show()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = SVC()  # 非線性SVM函數學習機

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)  # 預測.predict

# 直接用SVC的方法算正確率
cc = clf.score(X_test, y_test)
print("正確率 :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

centers = [(-1, -0.125), (0.5, 0.5)]

N = 50  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 6  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(n_samples=N, n_features=M, centers=centers, cluster_std=STD)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearSVC()  # 線性支援向量機 (Linear SVM)

model.fit(X_train, y_train)  # 學習訓練.fit

y_pred = model.predict(X_test)  # 預測.predict

print(accuracy_score(y_pred, y_test))  # 評価

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
data, label = make_blobs(n_samples=N, n_features=M, centers=GROUPS, random_state=9487)

d_sta = preprocessing.StandardScaler().fit_transform(data)  # 標準化

# 資料分割
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2
)

# 建立分類模型
svm_model = LinearSVC()  # 線性支援向量機 (Linear SVM)

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

d_sta = preprocessing.StandardScaler().fit_transform(data)  # 標準化

# 資料分割
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2
)

# 線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
svm_model = LinearSVC()  # 線性支援向量機 (Linear SVM)

svm_model.fit(dx_train, label_train)  # 學習訓練.fit

pred = svm_model.predict(dx_test)

# 輸出線性SVM準確性
print(f"線性訓練資料的準確性 = {svm_model.score(dx_train, label_train)}")
print(f"線性測試資料的準確性 = {svm_model.score(dx_test, label_test)}")

# 非線性SVM 建立分類模型, 建立訓練數據模型, 對測試數據做預測
clf = SVC()
clf.fit(dx_train, label_train)
pred = clf.predict(dx_test)

# 輸出非線性SVM準確性
print(f"非線性訓練資料的準確性 = {clf.score(dx_train, label_train)}")
print(f"非線性測試資料的準確性 = {clf.score(dx_test, label_test)}")

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

scaler = preprocessing.StandardScaler()
X = scaler.fit_transform(X)  # STD特徵縮放

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

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
    X, Y, test_size=0.2, train_size=0.2
)

# 使用svm，建立支持向量机模型
svcModel = SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
    train_data, train_target
)

# 初步评估
test_est = svcModel.predict(test_data)
print(metrics.classification_report(test_target, test_est))  # 计算评估指标

# 进行标准化可以提升高斯核svm的表现
scaler = preprocessing.StandardScaler().fit(train_data)
train_scaled = scaler.transform(train_data)
test_scaled = scaler.transform(test_data)

svcModel1 = SVC(kernel="rbf", gamma=0.5, C=0.5, probability=True).fit(
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

svc = SVC(kernel="linear", C=C).fit(train_x, train_y)  # 非線性SVM函數學習機, linear模式

rbf_svc = SVC(kernel="rbf", gamma=0.5, C=1).fit(train_x, train_y)
poly_svc = SVC(kernel="poly", degree=3, C=C).fit(train_x, train_y)
lin_svc = LinearSVC(C=C).fit(train_x, train_y)  # 線性支援向量機 (Linear SVM)

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
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.7)  # contourf 等高線面積圖

    # Plot also the training points
    plt.scatter(train_x[:, 0], train_x[:, 1], c=train_y, cmap=plt.cm.coolwarm)
    plt.xlabel("Attractive")
    plt.ylabel("Assets")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = iris.data
Y = iris.target

X_SVM = X[:, :2]  # 取出前兩欄

clf = SVC()

clf.fit(X_SVM, Y)  # 學習訓練.fit

y_predict = clf.predict(X_SVM)

plt.scatter(X_SVM[:, 0], X_SVM[:, 1], c=y_predict)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

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

# SelectFromModel

from sklearn.feature_selection import SelectFromModel

X, y = datasets.load_iris(return_X_y=True)
print("X.shape :", X.shape)

# SelectFromModel特徵選取

svc = SVC(kernel="linear", C=1)  # 非線性SVM函數學習機, linear模式

clf = SelectFromModel(estimator=svc, threshold="mean")

X_new = clf.fit_transform(X, y)
print("X_new.shape :", X_new.shape)

print("特徵是否被選取")
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

print("選擇2個特徵")
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
# ((120, 2), (30, 2), (120,), (30,))

print("特徵縮放")
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 7. 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(y_pred)

print("計算準確率")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.67%

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

print("使用全部特徵1")

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("查看陣列維度")
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
# (120, 4) (30, 4) (120,) (30,)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = sklearn.linear_model.LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

print("模型計分")
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 93.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 順序特徵選取(Sequential Feature Selection)

from sklearn.feature_selection import SequentialFeatureSelector

X, y = datasets.load_iris(return_X_y=True)
print("X.shape :", X.shape)

# SFS 特徵選取
svc = SVC(kernel="linear", C=1)  # 非線性SVM函數學習機, linear模式

clf = SequentialFeatureSelector(estimator=svc, n_features_to_select=2)
X_new = clf.fit_transform(X, y)

print("X_new.shape :", X_new.shape)

# 特徵是否被選取
cc = clf.get_support()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
X_train.shape, X_test.shape, y_train.shape, y_test.shape

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = sklearn.linear_model.LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 7. 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 86.67%

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

print("使用全部特徵2")

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf = sklearn.linear_model.LogisticRegression()

clf.fit(X_train_std, y_train)  # 學習訓練.fit

# 模型計分
y_pred = clf.predict(X_test_std)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

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
    plt.contourf(xx, yy, Z, cmap="hot", alpha=0.5)  # contourf 等高線面積圖

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


N = 100  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, centers=GROUPS, cluster_std=STD, random_state=9487)

clf = SVC(C=1.0, kernel="linear")

clf.fit(X, y)

plt.figure(figsize=(12, 4))
plot_hyperplane(clf, X, y, h=0.01, title="Maximum Margin Hyperplan")

show()

print("------------------------------")  # 30個

N = 100  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
STD = 0.8  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, centers=GROUPS, cluster_std=STD, random_state=9487)

clf_linear = SVC(C=1.0, kernel="linear")
clf_poly = SVC(C=1.0, kernel="poly", degree=3)
clf_rbf = SVC(C=1.0, kernel="rbf", gamma=0.5)
clf_rbf2 = SVC(C=1.0, kernel="rbf", gamma=0.1)

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

dataset = pd.read_csv("data/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 第四步：特征量化  # Feature Scaling
scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.fit_transform(X_test)  # STD特徵縮放

# 第五步：适配SVM到训练集合
# Fitting SVM to the Training set

classifier = SVC(kernel="linear", random_state=9487)  # 非線性SVM函數學習機, linear模式

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
)  # contourf 等高線面積圖
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
)  # contourf 等高線面積圖
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

# 自我訓練(Self-training)測試

from sklearn.semi_supervised import SelfTrainingClassifier

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
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)  # contourf 等高線面積圖
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

print("4維線性SVC")

iris = datasets.load_iris()

X = iris.data
y = iris.target

clf = SVC(kernel="linear")  # 非線性SVM函數學習機, linear模式

clf.fit(X, y)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict

# 計算正確率
accuracy = accuracy_score(y, y_pred)
print("SVM classifier 之 正確率 : {:.2f}".format(accuracy))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 繪製混淆矩陣
iris = datasets.load_iris()

X = iris.data
y = iris.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y)

# 模型訓練
clf = SVC(kernel="linear", C=0.01)  # 非線性SVM函數學習機, linear模式

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
        display_labels=iris.target_names,
        normalize=normalize,
    )
    #     cm.plot(ax=axes[i])
    cm.ax_.set_title(title, fontsize=16)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 07_01_svm_from_scratch
# 自行開發支援向量機分類器，並進行鳶尾花(Iris)品種的辨識

# SVM 演算法


class SVM:
    def __init__(self, learning_rate=1e-3, lambda_param=1e-2, n_iters=1000):
        self.lr = learning_rate
        self.lambda_param = lambda_param
        self.n_iters = n_iters
        self.w = None
        self.b = None

    # 初始化權重、偏差
    def _init_weights_bias(self, X):
        n_features = X.shape[1]
        self.w = np.zeros(n_features)
        self.b = 0

    # 類別代碼：-1, 1
    def _get_cls_map(self, y):
        return np.where(y <= 0, -1, 1)

    # 限制條件：y(wx + b) >= 1
    def _satisfy_constraint(self, x, idx):
        linear_model = np.dot(x, self.w) + self.b
        return self.cls_map[idx] * linear_model >= 1

    # 反向傳導
    def _get_gradients(self, constrain, x, idx):
        if constrain:
            dw = self.lambda_param * self.w
            db = 0
            return dw, db

        dw = self.lambda_param * self.w - np.dot(self.cls_map[idx], x)
        db = -self.cls_map[idx]
        return dw, db

    # 更新權重、偏差
    def _update_weights_bias(self, dw, db):
        self.w -= self.lr * dw
        self.b -= self.lr * db

    # 訓練
    def fit(self, X, y):
        self._init_weights_bias(X)
        self.cls_map = self._get_cls_map(y)

        for _ in range(self.n_iters):
            for idx, x in enumerate(X):
                constrain = self._satisfy_constraint(x, idx)
                dw, db = self._get_gradients(constrain, x, idx)
                self._update_weights_bias(dw, db)

    # 預測
    def predict(self, X):
        estimate = np.dot(X, self.w) + self.b
        prediction = np.sign(estimate)
        return np.where(prediction == -1, 0, 1)


X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 選擇演算法

clf = SVM(learning_rate=1e-2, lambda_param=1e-3, n_iters=5000)

# 模型訓練
SVC
clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 73.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 以Scikit-learn SVM進行鳶尾花(Iris)品種的辨識

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = SVC(probability=True)

clf.fit(X_train_std, y_train)

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_std)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 100.00%

cc = clf.support_vectors_
print(cc)

cc = clf.support_
print(cc)

cc = clf.predict_proba(X_test)
print(cc)

cc = clf.predict_log_proba(X_test)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
SVM優點：
    切出來的線很漂亮，擁有最大margin的特性
    可以很容易透過更換Kernel，做出非線性的線（非線性的決策邊界）
SVM缺點：
    效能較不佳，由於時間複雜度為O(n²)當有超過一萬筆資料時，運算速度會慢上許多
"""

iris = datasets.load_iris()

x = pd.DataFrame(iris["data"], columns=iris["feature_names"])
print("target_names: " + str(iris["target_names"]))
y = pd.DataFrame(iris["target"], columns=["target"])
iris_data = pd.concat([x, y], axis=1)
iris_data = iris_data[["sepal length (cm)", "petal length (cm)", "target"]]
iris_data = iris_data[iris_data["target"].isin([0, 1])]
cc = iris_data.head(3)
print(cc)

# 將資料分為Train以及Test並將特徵標準化

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    iris_data[["sepal length (cm)", "petal length (cm)"]],
    iris_data[["target"]],
    test_size=0.2,
    random_state=0,
)

sc = preprocessing.StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 載入SVM中的SVC，並將kernel設為線性（SVM的Kernel可以換成非線性），並將Probability設為True

clf = SVC(kernel="linear", probability=True)  # 非線性SVM函數學習機, linear模式

clf.fit(X_train_std, y_train["target"].values)

""" Out
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape=None, degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=True, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

SVC是SVM用C++語言實作的版本，背後是libsvm

"""

cc = clf.predict(X_test_std)
print(cc)

cc = y_test["target"].values
print(cc)

error = 0
for i, v in enumerate(clf.predict(X_test_std)):
    if v != y_test["target"].values[i]:
        error += 1
print(error)

cc = clf.predict_proba(X_test_std)
print(cc)


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)  # contourf 等高線面積圖
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.6,
            c=cmap(idx),
            edgecolor="black",
            marker=markers[idx],
            label=cl,
        )

    # highlight test samples
    if test_idx:
        # plot all samples
        if not versiontuple(np.__version__) >= versiontuple("1.9.0"):
            X_test, y_test = X[list(test_idx), :], y[list(test_idx)]
            warnings.warn("Please update to NumPy 1.9.0 or newer")
        else:
            X_test, y_test = X[test_idx, :], y[test_idx]

        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            c="",
            alpha=1.0,
            edgecolor="black",
            linewidths=1,
            marker="o",
            s=55,
            label="test set",
        )


plot_decision_regions(X_train_std, y_train["target"].values, classifier=clf)
plt.xlabel("sepal length [standardized]")
plt.ylabel("petal width [standardized]")
plt.legend(loc="upper left")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_03_svm _sample_weight

# 不平衡的資料集利用sample_weight矯正

# 生成隨機資料

# 20筆資料，前10筆+1
X = np.r_[np.random.randn(10, 2) + [1, 1], np.random.randn(10, 2)]
# y 前10筆為1，後10筆為-1
y = [1] * 10 + [-1] * 10
print(X)
print(y)

# 指定不同權重

# 初始權重為隨機亂數
modified_weight = abs(np.random.randn(len(X)))

# 後5筆權重乘以 5
modified_weight[15:] *= 5
# 第10筆權重乘以 15
modified_weight[9] *= 15
print(modified_weight)

# 無加權的模型訓練

clf_no_weights = SVC(gamma=1)
clf_no_weights.fit(X, y)

"""
SVC(gamma=1)
"""

# 加權的模型訓練

clf_weights = SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=modified_weight)

"""
SVC(gamma=1)
"""

# 決策邊界函數


def plot_decision_function(classifier, sample_weight, axis, title):
    # plot the decision function
    xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))

    Z = classifier.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    # plot the line, the points, and the nearest vectors to the plane
    axis.contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)  # contourf 等高線面積圖
    axis.scatter(
        X[:, 0],
        X[:, 1],
        c=y,
        s=100 * sample_weight,
        alpha=0.9,
        cmap=plt.cm.bone,
        edgecolors="black",
    )

    axis.axis("off")
    axis.set_title(title)


# 繪圖比較兩個模型

# plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['axes.unicode_minus'] = False

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 權重全部為 1
constant_weight = np.ones(len(X))
plot_decision_function(clf_no_weights, constant_weight, axes[0], "無加權的模型")

# 權重全部為 1
plot_decision_function(clf_weights, modified_weight, axes[1], "加權的模型")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_04_svm_kernels

# 非線性分割SVM測試

# 生成隨機資料
# 16筆資料，分兩類
X = np.c_[
    (0.4, -0.7),
    (-1.5, -1),
    (-1.4, -0.9),
    (-1.3, -1.2),
    (-1.1, -0.2),
    (-1.2, -0.4),
    (-0.5, 1.2),
    (-1.5, 2.1),
    (1, 1),
    (1.3, 0.8),
    (1.2, 0.5),
    (0.2, -2),
    (0.5, -2.4),
    (0.2, -2.3),
    (0, -2.7),
    (1.3, 2.1),
].T
Y = [0] * 8 + [1] * 8

print(X)
print(Y)

# 繪圖比較三種 kernels 模型

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
for fignum, kernel in enumerate(["linear", "poly", "rbf"]):
    clf = SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)

    plt.subplot(1, 3, fignum + 1)
    plt.scatter(
        clf.support_vectors_[:, 0],
        clf.support_vectors_[:, 1],
        s=80,
        facecolors="none",
        zorder=10,
        edgecolors="r",
    )
    colors = np.array(["yellow", "lightgreen"])
    plt.scatter(X[:, 0], X[:, 1], c=colors[Y], zorder=10, cmap=plt.cm.Paired)

    x_min, x_max, y_min, y_max = -3, 3, -3, 3
    XX, YY = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
    Z = clf.decision_function(np.c_[XX.ravel(), YY.ravel()])
    Z = Z.reshape(XX.shape)
    plt.pcolormesh(XX, YY, Z > 0, cmap=plt.cm.Paired)
    plt.contour(
        XX,
        YY,
        Z,
        colors=["k", "k", "k"],
        linestyles=["--", "-", "--"],
        levels=[-0.5, 0, 0.5],
    )

    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition

# SVM人臉辨識

from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)
n_samples, h, w = lfw_people.images.shape

X = lfw_people.data
n_features = X.shape[1]
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print(f"n_samples: {n_samples}")
print(f"n_features: {n_features}")
print(f"n_classes: {n_classes}")

"""
Total dataset size:
n_samples: 1288
n_features: 1850
n_classes: 7
"""

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 使用 PCA 萃取 150 個特徵
n_components = 150

t0 = time.time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)

X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print(f"轉換耗時: {(time.time() - t0):.3f}s")

# 轉換耗時: 0.183s

# 模型訓練
clf = SVC(kernel="rbf", class_weight="balanced")
clf.fit(X_train_pca, y_train)

"""
SVC(class_weight='balanced')
"""

# 模型評分

# 計算準確率
y_pred = clf.predict(X_test_pca)
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 分類報告

y_pred = clf.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))

# 混淆矩陣圖

ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation=30
)
show()

# 結合圖像與預測結果驗證

prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w, n_row=6, n_col=4)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 07_06_svm_faces recognition_org

# Faces recognition example using eigenfaces and SVMs

# The dataset used in this example is a preprocessed excerpt of the "Labeled Faces in the Wild", aka LFW_:

# http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

from sklearn.model_selection import RandomizedSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from scipy.stats import loguniform

# Download the data, if not already on disk and load it as numpy arrays

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape

# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]

# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]

print("Total dataset size:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled dataset): unsupervised feature extraction / dimensionality reduction
n_components = 150

print(
    "Extracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0])
)
t0 = time.time()
pca = PCA(n_components=n_components, svd_solver="randomized", whiten=True).fit(X_train)
print("done in %0.3fs" % (time.time() - t0))

eigenfaces = pca.components_.reshape((n_components, h, w))

print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time.time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time.time() - t0))

# Train a SVM classification model

print("Fitting the classifier to the training set")
t0 = time.time()
param_grid = {
    "C": loguniform(1e3, 1e5),
    "gamma": loguniform(1e-4, 1e-1),
}
clf = RandomizedSearchCV(
    SVC(kernel="rbf", class_weight="balanced"), param_grid, n_iter=10
)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time.time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)

# Quantitative evaluation of the model quality on the test set

print("Predicting people's names on the test set")
t0 = time.time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time.time() - t0))

print(classification_report(y_test, y_pred, target_names=target_names))
ConfusionMatrixDisplay.from_estimator(
    clf, X_test_pca, y_test, display_labels=target_names, xticks_rotation="vertical"
)
plt.tight_layout()
show()

# Predicting people's names on the test set

prediction_titles = [
    title(y_pred, y_test, target_names, i) for i in range(y_pred.shape[0])
]

plot_gallery(X_test, prediction_titles, h, w)

# plot the gallery of the most significative eigenfaces

eigenface_titles = ["eigenface %d" % i for i in range(eigenfaces.shape[0])]
plot_gallery(eigenfaces, eigenface_titles, h, w)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

"""
print("另存新檔");
filename = 'tmp_aaaa.csv'
np.savetxt(filename, iris.data, delimiter=',')
print("寫入完成")
"""

# :2 是 前兩個 => 花萼
# 2: 是 第2個(含)以後 => 花瓣

# 準備 inputs 和 outputs
x = iris.data
y = iris.target  # 資料集目標

# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 只選兩個 features 原因之一是好畫 :)

plt.scatter(X[:, 0], X[:, 1], c="pink", s=150)
plt.scatter(X[:, 0], X[:, 1], s=50, c=Y, alpha=0.6)
plt.title("花瓣 原始資料")
show()

# 試著用我們學過的方式, 看能不能做出一個分類器函數, 來把鳶尾花正確分類!

# 準備 inputs 和 outputs
x = iris.data
y = iris.target  # 資料集目標

# 為了表示我們很神 (事實上只是好畫圖), 我們只用兩個 features (花瓣長度、寬度)。
# X = x[:, :2]   #初~2 花萼
X = x[:, 2:]  # 2~末 花瓣
Y = y

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# 看一下整筆數據的分佈。
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("花瓣 原始資料")
show()

# 看訓練結果
plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
plt.title("花瓣 訓練資料")
show()

# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。

clf = SVC()

clf.fit(x_train, y_train)

y_predict = clf.predict(x_test)

print("看看我們模型預測和真實狀況差多少?")
print(y_predict - y_test)

# 看看有沒有不準的?
y_predict = clf.predict(x_test)

# 這時因為如果答對了, 我們和正確答案相減就是 0。學得不錯就會大部份是 0, 錯的不是 0 畫出來就會不同色。我們來試試看。
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)
plt.title("看差值")
show()

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)
plt.title("看最後預測結果")
show()

# 現在我們做的是讓平面上密密麻麻的點都去看它會是哪種鳶尾花的數據。

x1, y1 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))

# 記得 x1, y1 是什麼樣子的, 我們要拉平之後 (x1_ravel(), y1_ravel()),
# 再用 np.c_ 合成一點一點的, 才可以送進去預測。

Z = clf.predict(np.c_[x1.ravel(), y1.ravel()])

# 好奇的話可以看看我們到底送了多少點進去?

print(len(x1.ravel()))

# 52500

# 等一下我們要用 contourf 做填充型的等高線,
# 每一點的「高度」就是我們的 SVC 學習機判斷鳶尾花的亞種。
# 但用 contourf 輸入的格點是前面 meshgrid 後的 x1, y1,
# 而高度 Z 也是要用同樣的型式。

Z = Z.reshape(x1.shape)

# 於是我們終於可以畫圖了...

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_test)
plt.contourf(x1, y1, Z, alpha=0.3)  # contourf 等高線面積圖
show()

# 這是測試資料, 之前我們已經知道我們全對!
# 不如就來看看所有鳶尾花資料我們 SVC 的表現。

plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.contourf(x1, y1, Z, alpha=0.3)  # contourf 等高線面積圖
show()

# 在測試資料中是全對!! 我們畫圖來看看整體表現如何?
# 畫出結果
x0 = np.linspace(0, 7.5, 500)
y0 = np.linspace(0, 2.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=Y)

show()

x0 = np.linspace(3, 8, 500)
y0 = np.linspace(1.5, 4.5, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # contourf 等高線面積圖

plt.scatter(X[:, 0], X[:, 1], c=Y)
show()

# 畫出結果
x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=Y)
show()

x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
xx = [1, 2, 3, 4]
yy = [5, 6, 7, 8]
np.c_[xx, yy]
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, cmap=plt.cm.coolwarm, alpha=0.8)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=Y)
plt.title("更炫的畫圖法")
show()

"""
X, Y = np.meshgrid(np.arange(4, 8, 0.02), np.arange(2, 4.5, 0.02))
x_data = np.c_[X.ravel(), Y.ravel()]
data_pred = clf.predict(x_data)
Z = data_pred.reshape(X.shape)
plt.contourf(X, Y, Z, alpha = 0.3)  # contourf 等高線面積圖
plt.scatter(x[:, 0], x[:, 1], c = y)
show()
"""

# 畫出結果
x1, x2 = np.meshgrid(np.arange(0, 7, 0.02), np.arange(0, 3, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
Z = Z.reshape(x1.shape)
plt.contourf(x1, x2, Z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=Y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# 資料內容 iris.data
# 鳶尾花 (Iris) 的數據, 有三類的鳶尾花我們想用 SVM 做分類。
# 答案 iris.target

x = iris.data[:, :2]
y = iris.target  # 資料集目標

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)
plt.title("原圖")
show()

clf = SVC()

clf.fit(x, y)
clf.predict(x)
clf.predict(x) - y
gd = np.array([[i, j] for i in np.arange(4, 8, 0.2) for j in np.arange(1.8, 4.5, 0.2)])
gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
plt.title("SVM結果")

show()

# 呈現學習成果
# 學出來的用比較透明的顏色, 真實資料用 100% 不透明。

gd = np.array([[i, j] for i in np.arange(4, 8, 0.1) for j in np.arange(1.8, 4.5, 0.1)])
gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc, alpha=0.4)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.title("SVM結果2")

show()

print("------------------------------------------------------------")  # 60個

# PCA 可以救鳶尾花嗎？
from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)
# 我們來看原來的樣子, 是一個 4 維的向量。
print("x.shape :", x.shape)
print(len(x))
print(x)
print(x[7])

# 經 PCA 之後, 濃縮成 2 維向量。
print("X.shape :", X.shape)
print(len(X))
print(X)
print(X[7])

# 看看 PCA 後, 來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
show()

# 看來好像真的會比較容易切開, 我們來試試是否真的這樣。先來分訓練和測試資料。

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = SVC()

clf.fit(x_train, y_train)

SVC()

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3, cmap="Paired")  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

# 分好 features 跟 target
X = iris.data
Y = iris.target  # 資料集目標

# 照著題目的說明，只拿花萼的 features 來用
# 分好訓練跟測試資料，再把「正確答案」的分佈畫一下做個確認

X = X[:, :2]

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train)
show()

# 設定一個 SVM 的函數學習機，把訓練資料放進去 train
clf = SVC()

clf.fit(x_train, y_train)

"""
SVC(C=1.0, break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,    decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,    max_iter=-1, probability=False, random_state=None, shrinking=True,
,    tol=0.001, verbose=False)
"""

# 稍微瞄一下預測結果跟正確答案的差距，發現大致上做得還不錯！
# 而且好像比原本用花瓣的 features 還要好！
# 選擇 features 真的很重要！

y_predict = clf.predict(x_test)
print(y_predict - y_test)
y_predict - y_test

"""
array([ 0,  0,  0,  0,  0,  1,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  0,
,        0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1])
"""

# 當然要畫個圖看一下，這樣還可以確認哪些特殊的情況下模型會分不好
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)
show()

# 也可以畫這種的

y_predict = clf.predict(x_test)

plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict)
show()

# 照著題目的說明，換另一種 SVM 來試試看

from sklearn.svm import NuSVC

clf1 = NuSVC()

clf1.fit(x_train, y_train)

"""
NuSVC(break_ties=False, cache_size=200, class_weight=None, coef0=0.0,
,      decision_function_shape='ovr', degree=3, gamma='scale', kernel='rbf',
,      max_iter=-1, nu=0.5, probability=False, random_state=None, shrinking=True,
,      tol=0.001, verbose=False)
"""

"""
嗚，好像變差了
但這件事告訴我們，不同的模型在不同的參數情況下，
也會學出不同的結果跟好壞，
因此適時的做實驗調整模型跟參數也是很重要的！
"""

y_predict = clf1.predict(x_test)
plt.scatter(x_test[:, 0], x_test[:, 1], c=y_predict - y_test)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

x = iris.data
y = iris.target  # 資料集目標

X = x[:, :2]
Y = y

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap="Paired")
plt.title("原始資料")

show()

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print(y_pred - y_test)

x0 = np.linspace(3.8, 8.2, 500)
y0 = np.linspace(1.8, 4.7, 500)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=Y)

show()

# PCA 可以救鳶尾花嗎？

from sklearn.decomposition import PCA

pca = PCA(n_components=2)

pca.fit(x)

X = pca.transform(x)

# 我們稍稍的「欣賞一下」 PCA 對我們的資料集做了什麼，來看看某朵鳶尾花的資料。
# pca.transform([[6.3, 2.3, 4.4, 1.3]])
# 真的變成平面上一個點！來看看整個分布的狀況。

plt.scatter(X[:, 0], X[:, 1], c=y, cmap="Paired")
show()

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = SVC(gamma="scale")

clf.fit(x_train, y_train)

x0 = np.arange(-4, 4.2, 0.02)
y0 = np.arange(-1.5, 1.7, 0.02)

xm, ym = np.meshgrid(x0, y0)
P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # contourf 等高線面積圖
plt.scatter(X[:, 0], X[:, 1], c=y)
show()

print(x[87])

print(y[87])

print(pca.transform([[6.3, 2.3, 4.4, 1.3]]))

print(clf.predict([[0.81509524, -0.37203706]]))

print("X.shape :", X.shape)

# print(Z.reshape(X.shape))

# 畫完整分類
# 和以前一樣, 未來新的資料進來, 我們訓練好的也可以再做分類。

gd = np.array([[i, j] for i in np.arange(-4, 4, 0.4) for j in np.arange(-3, 3, 0.4)])

gdc = clf.predict(gd)

plt.scatter(gd[:, 0], gd[:, 1], s=50, c=gdc)
show()

x1, x2 = np.meshgrid(np.arange(-0.2, 1.2, 0.02), np.arange(-0.2, 1.2, 0.02))
Z = clf.predict(np.c_[x1.ravel(), x2.ravel()])
z = Z.reshape(x1.shape)
plt.contourf(x1, x2, z, alpha=0.3)  # contourf 等高線面積圖
# NG plt.scatter(x[:, 0], x[:, 1], s=100, c=clf.labels_)
show()

# 呈現出來
x0 = y0 = np.arange(-0.2, 1.2, 0.02)
xm, ym = np.meshgrid(x0, y0)

P = np.c_[xm.ravel(), ym.ravel()]
z = clf.predict(P)
Z = z.reshape(xm.shape)
plt.contourf(xm, ym, Z, alpha=0.3)  # contourf 等高線面積圖
# NG plt.scatter(x[:, 0], x[:, 1], c=clf.labels_)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

X = iris.data  # 獲取自變量
y = iris.target  # 獲取因變量  # 資料集目標

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = SVC(C=0.8, kernel="rbf", gamma=1)  # 高斯核，鬆弛度0.8
# clf = SVC(C=0.5, kernel='linear') # 線性核，鬆弛度0.5

clf.fit(X_train, y_train.ravel())

print("trian pred:%.3f" % (clf.score(X_train, y_train)))  # 對訓練集打分
print("test pred:%.3f" % (clf.score(X_test, y_test)))  # 對測試集打分
print(clf.support_vectors_)  # 支持向量列表，從中看到切分邊界
print(clf.n_support_)  # 每類別持向量個數

plt.plot(X_train[:, 0], X_train[:, 1], "o", color="#bbbbbb")
plt.plot(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], "o")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" some fail
from sklearn.model_selection import KFold

iris = datasets.load_iris()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

num = 5 # 5折交叉驗證
train_preds = np.zeros(X_train.shape[0]) # 用於保存預測結果
test_preds = np.zeros((X_test.shape[0], num))
kf = KFold(len(X_train), n_folds = num, shuffle=True, random_state=9487)
for i, (train_index, eval_index) in enumerate(kf):
    clf = SVC(C=1, gamma=0.125, kernel='rbf')
    clf.fit(X_train[train_index], y_train[train_index])
    train_preds[eval_index] += clf.predict(X_train[eval_index])
    test_preds[:,i] = clf.predict(X_test)
print(accuracy_score(y_train, train_preds)) # 返回結果: 0.971428571429
print(test_preds.mean(axis=1))

from sklearn.model_selection import cross_val_score # python 3使用
print(cross_val_score(clf, iris.data, iris.target).mean())
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("模型調參")

# 網格搜索
from sklearn.model_selection import GridSearchCV

iris = datasets.load_iris()

clf = SVC(random_state=1)

param_grid = {
    "kernel": ("linear", "rbf"),
    "C": [1, 2, 4],  # 制定參數範圍
    "gamma": [0.125, 0.25, 0.5, 1, 2, 4],
}
gs = GridSearchCV(
    estimator=clf, param_grid=param_grid, scoring="accuracy", cv=10, n_jobs=-1
)
gs = gs.fit(iris.data, iris.target)
y_pred = gs.predict(iris.data)  # 預測
print(gs.best_score_)
print(gs.best_params_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" some fail
from sklearn.model_selection import cross_val_score
from hyperopt import hp,STATUS_OK,Trials,fmin,tpe
from sklearn.ensemble import RandomForestClassifier

def f(params): # 定義評價函數
    t = params['type']
    del params['type']
    if t == 'svm':
        clf = SVC(**params)
    elif t == 'randomforest':
        clf = RandomForestClassifier(**params)
    else:
        return 0
    acc = cross_val_score(clf, iris.data, iris.target).mean() 
    return {'loss': -acc, 'status': STATUS_OK} # 求最小值:準確率加負號

iris = datasets.load_iris()

space = hp.choice('classifier_type', [ # 定義可選參數
    {
        'type': 'svm',
        'C': hp.uniform('C', 0, 10.0),
        'kernel': hp.choice('kernel', ['linear', 'rbf']),
        'gamma': hp.uniform('gamma', 0, 20.0)
    },
    {
        'type': 'randomforest',
        'max_depth': hp.choice('max_depth', range(1,20)),
        'max_features': hp.choice('max_features', range(1,5)),
        'n_estimators': hp.choice('n_estimators', range(1,20)),
        'criterion': hp.choice('criterion', ["gini", "entropy"])
    }
])
best = fmin(f, space, algo=tpe.suggest, max_evals=100)
print('best:',best) 
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

"""
plt.xlim([0, 10])
plt.scatter(*(zip(*X01)), c='r')
plt.scatter(*(zip(*X02)), c='g')
plt.plot([0, 10], [0, 15], "b")
plt.plot([0, 10], [2, 22], "b")

plt.scatter(5, 9, c="m")  # test point
plt.text(0.5, -1.5, "aaa")
plt.text(0.3, 2.5, "bbb")
plt.text(2.9, 14, "ccc")

plt.title('aaa')
show()
"""

print("------------------------------------------------------------")  # 60個

"""
plt.plot([0, 10], [0, 20], "r-", zorder=0)
plt.plot([0, 10], [5, 25], "g--", zorder=0)
plt.plot([0, 10], [-5, 15], "b--", zorder=0)

plt.annotate("", (0, 5), (0.55, -4), arrowprops=dict(arrowstyle="<->"))
plt.annotate("", (3.05, 18.1), (3.8, 7.75), arrowprops=dict(arrowstyle="<->"))

plt.scatter(*(zip(*X01)), zorder=1, c='r')
plt.scatter(*(zip(*X02)), zorder=1, c='g')

sv = X01[:2] + X02[:2]

plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)

plt.title('bbb')
show()
"""

print("------------------------------------------------------------")  # 60個

"""
# Hard margin
# Functional margin
# Geometric margin
# The optimal margin
# Lagrange multipliers


def flc(c, n=100):
    # Level curves of objective functions
    return np.array(
        [(c * np.cos(ang), c * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, n)]
    )


def g(n=100):
    # Constraint
    return np.array([(x, 1.0 / x) for x in np.linspace(0.1, 2.5, n)])


##### PLOT SETTINGS #####

plt.figure(figsize=(8, 8))
plt.xlim([-2.5, 2.5])
plt.ylim([-2.5, 2.5])
plt.grid(color="0.5", linestyle="--", linewidth=0.5)

##### LEVEL CURVES OF f(x, y) #####

for c in (0.2, 0.6, 1, 1.8, 2.2):
    plt.plot(*flc(c).T, color="C0")

plt.plot(*flc(np.sqrt(2)).T, color="C0", label="$f(x, y) = c$")

##### CONSTRAINTS #####

plt.plot(*g().T, color="C1", label="$g(x, y) = 0$")
plt.plot(*-g().T, color="C1")

##### INTERSECTIONS #####

plt.scatter(1, 1, c="C2", zorder=4)
plt.scatter(np.sqrt(0.345), np.sqrt(1 / 0.345), c="C3", zorder=4)

plt.legend()
plt.title('ccc')
show()

print("------------------------------------------------------------")  # 60個

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

ax = plt.figure().add_subplot(111, projection=Axes3D.name)

X, Y = np.meshgrid(np.linspace(-1, 3, 50), np.linspace(-5, 1, 50))
L = X**2 + Y * (X - 1)

ax.plot_surface(X, Y, L, cmap=cm.hsv)

ax.view_init(elev=45, azim=120)

ax.set_xlabel("$x$", labelpad=20)
ax.set_ylabel("$\lambda$", labelpad=20)
ax.set_zlabel("$\mathcal{L}$", labelpad=10)
plt.title("3D畫圖")
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# Non-linear SVM
"""
    SVM can be applied to non-linear problems using the kernel trick
    However, before we go there, lets consider a simple non-linear problem

Example
    Lets consider two classes of 2D points:
        inside a circle
        outside a circle
"""


def generate_circle_data(R1=0, R2=1, N=500):
    """Generate N points in a circle for radius range (R1, R2)"""
    r = lambda: R1 + np.random.random() * (R2 - R1)

    return np.array(
        [(r() * np.cos(ang), r() * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, N)]
    )


C01 = generate_circle_data()
C02 = generate_circle_data(1, 2)

plt.scatter(*C01.T, marker=".")
plt.scatter(*C02.T, marker=".")
plt.title('eee')
show()

print("------------------------------")  # 30個

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

ax = plt.figure().add_subplot(111, projection=Axes3D.name)

Z01 = np.array([x**2 + y**2 for x, y in C01])
Z02 = np.array([x**2 + y**2 for x, y in C02])

ax.scatter(*C01.T, Z01, cmap=cm.hsv)
ax.scatter(*C02.T, Z02, cmap=cm.hsv)

ax.view_init(elev=15, azim=60)
plt.title('fff')
show()
'''
print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]


plt.plot([0, 10], [0, 20], "C2-", zorder=0)
plt.plot([0, 10], [4, 24], "C3-", zorder=0)

plt.scatter(3, 9, c="C1", marker=",")

plt.scatter(*(zip(*X01)), zorder=1)
plt.scatter(*(zip(*X02)), zorder=1)
plt.title("ggg")
show()

print("------------------------------------------------------------")  # 60個

plt.plot([0, 10], [0, 20], "C2-", zorder=0)
plt.plot([0, 10], [5, 25], "C2--", zorder=0)
plt.plot([0, 10], [-5, 15], "C2--", zorder=0)

plt.scatter(3, 9, c="C1", marker=",")
plt.annotate("", (3.05, 8.7), (3.5, 1.75), arrowprops=dict(arrowstyle="<->"))
plt.text(3.5, 4.5, "$\\xi_i$")

plt.annotate("", (0, 5), (0.55, -4), arrowprops=dict(arrowstyle="<->"))
plt.text(0.5, -1.5, "$m$")
plt.text(0.3, 2.5, "$m$")

plt.annotate("", (3.05, 18.1), (3.8, 7.75), arrowprops=dict(arrowstyle="<->"))
plt.text(2.9, 14, "$m_i$")

plt.scatter(*(zip(*X01)), zorder=1)
plt.scatter(*(zip(*X02)), zorder=1)

sv = X01[:2] + X02[:2]

plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)
plt.title("hhh")
show()

# Regularization

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SMO algorithm

plt.xticks([], [])
plt.yticks([], [])
plt.xlim([0, 1])
plt.ylim([0, 1])

plt.text(1.05, 0.5, "$\mu_1 = C$")
plt.text(-0.1, 0.5, "$\mu_1 = 0$")
plt.text(0.5, 1.05, "$\mu_2 = C$")
plt.text(0.5, -0.05, "$\mu_2 = 0$")

plt.plot(
    (0.6, 1), (0, 0.75), label="$y_1 \\neq y_2 \Rightarrow \mu_1 - \mu_2 = \gamma$"
)
plt.plot((0.4, 0), (0, 0.75), label="$y_1 = y_2 \Rightarrow \mu_1 + \mu_2 = \gamma$")

plt.legend()
plt.title("iii")
show()

print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

plt.xlim([0, 10])

plt.scatter(*(zip(*X01)))
plt.scatter(*(zip(*X02)))
plt.title("jjj")
show()

print("------------------------------------------------------------")  # 60個

# class I
X01 = [(2, 9), (7, 19), (1, 10), (3, 19), (4, 16), (5, 18)]

# class II
X02 = [(4, 3), (6, 7), (1, -10), (3, -1), (9, 5), (5, -7)]

# create a classifier
clf = svm.SVC(kernel="linear")

# train classifier - assign -1 label for X01 and 1 for X02
clf.fit(X01 + X02, [-1] * len(X01) + [1] * len(X02))

"""
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='linear',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)
"""

# Lets visualize the result

sv = clf.support_vectors_  # support vectors
w = clf.coef_[0]  # weights
b = clf.intercept_  # intercept

# w[0] * x + w[1] * y + b = 0
f = lambda x: -(b + w[0] * x) / w[1]

# plot training data
plt.scatter(*(zip(*X01)))
plt.scatter(*(zip(*X02)))

# plt decision boundary
plt.plot([1, 9], [f(1), f(9)])

# mark support vectors
plt.scatter(*(zip(*sv)), zorder=1, facecolors="none", edgecolors="r", s=500)
plt.title("kkk")
show()

print("------------------------------------------------------------")  # 60個

# Circle


def generate_circle_data(R1=0, R2=1, N=500):
    """Generate N points in a circle for radius range (R1, R2)"""
    r = lambda: R1 + np.random.random() * (R2 - R1) + np.random.normal(0, 0.2)

    return np.array(
        [(r() * np.cos(ang), r() * np.sin(ang)) for ang in np.linspace(0, 2 * np.pi, N)]
    )


C01 = generate_circle_data()
C02 = generate_circle_data(1, 2)

plt.scatter(*C01.T, marker=".")
plt.scatter(*C02.T, marker=".")
plt.title("lll")
show()

print("mmmmmmmmmmmmm")
sys.exit()

print("------------------------------------------------------------")  # 60個

print("4種 SVM 核心 比較")
"""
We will consider 4 different kernels:
        linear
        polynomial of degree 3
        polynomial of degree 10
        Gaussian radial basis function (RBF)
"""

# create classifier with different kernels
clf_linear = svm.SVC(kernel="linear")
clf_rbf = svm.SVC(kernel="rbf")
clf_poly3 = svm.SVC(kernel="poly", degree=3)
clf_poly10 = svm.SVC(kernel="poly", degree=10)

titles = ("Linear", "RBF", "Polynomial, degree = 3", "Plynomial, degree = 10")

# create a mesh to plot in
xx, yy = np.meshgrid(np.arange(-3, 3, 0.01), np.arange(-3, 3, 0.01))

# loop over classifiers
for i, clf in enumerate((clf_linear, clf_rbf, clf_poly3, clf_poly10)):
    # train classifier - assign -1 label for C01 and 1 for C02
    clf.fit(np.concatenate((C01, C02), axis=0), [-1] * len(C01) + [1] * len(C02))

    # visualize results
    plt.subplot(2, 2, i + 1)

    # decision boundary
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    # training data
    plt.scatter(*C01.T, marker=".")
    plt.scatter(*C02.T, marker=".")

    plt.title(titles[i])

plt.tight_layout()
plt.title("mmm")
show()

print("------------------------------------------------------------")  # 60個

# Multiclass classification

# Example: blobs

# generate 5 blobs with fixed random generator
X, Y = make_blobs(n_samples=500, centers=8, random_state=300)

plt.scatter(*X.T, c=Y, marker=".", cmap="Dark2")
plt.title("nnn")
show()

print("------------------------------------------------------------")  # 60個

# We can use the same function as last time to train and visualize


def train_and_look(classifier, X, Y, ax=None, title="", cmap="Dark2"):
    """Train classifier on (X,Y). Plot data and prediction."""
    # create new axis if not provided
    ax = ax or plt.gca()

    ax.set_title(title)

    # plot training data
    ax.scatter(*X.T, c=Y, marker=".", cmap=cmap)

    # train a cliassifier
    classifier.fit(X, Y)

    # create a grid of testing points
    x_, y_ = np.meshgrid(
        np.linspace(*ax.get_xlim(), num=200), np.linspace(*ax.get_ylim(), num=200)
    )

    # convert to an array of 2D points
    test_data = np.vstack([x_.ravel(), y_.ravel()]).T

    # make a prediction and reshape to grid structure
    z_ = classifier.predict(test_data).reshape(x_.shape)

    # arange z bins so class labels are in the middle
    z_levels = np.arange(len(np.unique(Y)) + 1) - 0.5

    # plot contours corresponding to classifier prediction
    ax.contourf(x_, y_, z_, alpha=0.25, cmap=cmap, levels=z_levels)


fig, ax = plt.subplots(1, 3, figsize=(15, 5))

title = ("Linear", "RBF", "Polynomial")

settings = ({"kernel": "linear"}, {"kernel": "rbf"}, {"kernel": "poly", "degree": 5})

# train and look at SVM with different kernels
for i in range(0, 3):
    train_and_look(svm.SVC(**settings[i]), X, Y, ax=ax[i], title=title[i])

plt.title("ooo")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" no boston
#SVM regression

#Example - Boston Housing dataset

from sklearn.datasets import load_boston

boston = load_boston()

print(boston.DESCR)

#Visualize dataset

for i, feature in enumerate(boston.data.T):
    plt.subplot(3, 5, i+1)
    plt.scatter(feature, boston.target, marker='.')
    plt.title(boston.feature_names[i])
  
plt.tight_layout()
plt.title('ppp')
show()

print("------------------------------------------------------------")  # 60個

boston_pd = pd.DataFrame(boston.data)     # load features
boston_pd.columns = boston.feature_names  # add features names
boston_pd['PRICE'] = boston.target        # add a column with price

boston_pd.head()

#Test SVR

from sklearn.svm import SVR

regressor = SVR(kernel="linear")
regressor.fit(boston.data, boston.target)

prediction = regressor.predict(boston.data)

plt.xlabel("True price")
plt.ylabel("Predicted price")

plt.scatter(boston.target, prediction, marker='.')
plt.title('qqq last')
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
支持向量机

支持向量机(support vector machines,SVM)

支持向量机方法包括：
1.线性可分支持向量机
2.线性支持向量机
3.非线性支持向量机
"""
from sklearn import svm
import numpy as np
import matplotlib.pyplot as plt

# 构建正态分布来产生数字,20行2列*2
train_x = np.r_[np.random.randn(20, 2) - [2, 2], np.random.randn(20, 2) + [2, 2]]

# 构建 20个class0，20个class1
label_y = [0] * 20 + [1] * 20

# svm设置：
clf = svm.SVC(kernel="linear")
clf.fit(train_x, label_y)

# 获取weights
weights = clf.coef_[0]

rate = -weights[0] / weights[1]  # 斜率
# 画图划线
xx = np.linspace(-5, 5)  # (-5,5)之间x的值
yy = rate * xx - (clf.intercept_[0]) / weights[1]  # xx带入y，截距

# 画出与点相切的线
b = clf.support_vectors_[0]
# yy_down 是线 yy的下边的边界线
yy_down = rate * xx + (b[1] - rate * b[0])
b = clf.support_vectors_[-1]
# yy_up 是线 yy的上边的边界线
yy_up = rate * xx + (b[1] - rate * b[0])


# 测试, 两个中括号！
for i in range(20):
    test_x = np.random.randn(1, 2) * 10
    print("测试:点({},{}) 所属类别{}".format(test_x[0][0], test_x[0][1], clf.predict(test_x)))

plt.figure(figsize=(8, 4))
plt.plot(xx, yy)
# 绘制左上角的线
plt.plot(xx, yy_up)
# 绘制 左下角的线
plt.plot(xx, yy_down)
plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=80)
plt.scatter(train_x[:, 0], train_x[:, 1], c=label_y, cmap=plt.cm.Paired)  # [:，0]列切片，第0列
plt.axis("tight")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 非线性支持向量机

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops

ops.reset_default_graph()

sess = tf.Session()

# 加载数据

# iris.数据 [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([[x[0], x[3]] for x in iris.data])
y_vals = np.array([1 if y == 0 else -1 for y in iris.target])
class1_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class1_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] == 1]
class2_x = [x[0] for i, x in enumerate(x_vals) if y_vals[i] == -1]
class2_y = [x[1] for i, x in enumerate(x_vals) if y_vals[i] == -1]

# 声明模型变量

# 批量大小
batch_size = 150

# 初始化占位符
x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)
prediction_grid = tf.placeholder(shape=[None, 2], dtype=tf.float32)

# 创建变量
b = tf.Variable(tf.random_normal(shape=[1, batch_size]))

# 本案例采用高斯核函数，将低维空间数据转换为高维空间数据

# 高斯核函数 (RBF)
gamma = tf.constant(-50.0)
sq_vec = tf.multiply(2.0, tf.matmul(x_data, tf.transpose(x_data)))
my_kernel = tf.exp(tf.multiply(gamma, tf.abs(sq_vec)))

# SVM模型的损失函数
first_term = tf.reduce_sum(b)
b_vec_cross = tf.matmul(tf.transpose(b), b)
y_target_cross = tf.matmul(y_target, tf.transpose(y_target))
second_term = tf.reduce_sum(
    tf.multiply(my_kernel, tf.multiply(b_vec_cross, y_target_cross))
)
loss = tf.negative(tf.subtract(first_term, second_term))

# 声明预测时所采用的的核函数 RBF

rA = tf.reshape(tf.reduce_sum(tf.square(x_data), 1), [-1, 1])
rB = tf.reshape(tf.reduce_sum(tf.square(prediction_grid), 1), [-1, 1])
pred_sq_dist = tf.add(
    tf.subtract(rA, tf.multiply(2.0, tf.matmul(x_data, tf.transpose(prediction_grid)))),
    tf.transpose(rB),
)
pred_kernel = tf.exp(tf.multiply(gamma, tf.abs(pred_sq_dist)))

# 声明预测时所采用的的很函数RBF
prediction_output = tf.matmul(tf.multiply(tf.transpose(y_target), b), pred_kernel)
prediction = tf.sign(prediction_output - tf.reduce_mean(prediction_output))
accuracy = tf.reduce_mean(
    tf.cast(tf.equal(tf.squeeze(prediction), tf.squeeze(y_target)), tf.float32)
)

# 优化器的设置
my_opt = tf.train.GradientDescentOptimizer(0.01)
train_step = my_opt.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()
sess.run(init)

# 开始训练
loss_vec = []
batch_accuracy = []
for i in range(300):
    rand_index = np.random.choice(len(x_vals), size=batch_size)
    rand_x = x_vals[rand_index]
    rand_y = np.transpose([y_vals[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})

    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)

    acc_temp = sess.run(
        accuracy, feed_dict={x_data: rand_x, y_target: rand_y, prediction_grid: rand_x}
    )
    batch_accuracy.append(acc_temp)

    if (i + 1) % 75 == 0:
        print("Step #" + str(i + 1))
        print("Loss = " + str(temp_loss))

# 构建绘图时的数据点
# Create a mesh to plot points in
x_min, x_max = x_vals[:, 0].min() - 1, x_vals[:, 0].max() + 1
y_min, y_max = x_vals[:, 1].min() - 1, x_vals[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))
grid_points = np.c_[xx.ravel(), yy.ravel()]
[grid_predictions] = sess.run(
    prediction,
    feed_dict={
        x_data: x_vals,
        y_target: np.transpose([y_vals]),
        prediction_grid: grid_points,
    },
)
grid_predictions = grid_predictions.reshape(xx.shape)

# 绘制图形
plt.contourf(xx, yy, grid_predictions, cmap=plt.cm.Paired, alpha=0.8)
plt.plot(class1_x, class1_y, "ro", label="I. setosa")
plt.plot(class2_x, class2_y, "kx", label="Non setosa")
plt.title("Gaussian SVM Results on Iris Data")
plt.xlabel("Petal Length")
plt.ylabel("Sepal Width")
plt.legend(loc="lower right")
plt.ylim([-0.5, 3.0])
plt.xlim([3.5, 8.5])
plt.show()

# Plot batch accuracy
plt.plot(batch_accuracy, "k-", label="Accuracy")
plt.title("Batch Accuracy")
plt.xlabel("Generation")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()

# Plot loss over time
plt.plot(loss_vec, "k-")
plt.title("Loss per Generation")
plt.xlabel("Generation")
plt.ylabel("Loss")
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 支持向量机
# 线性支持向量机
# 线性支持向量机的TensorFlw实现

import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn import datasets
from tensorflow.python.framework import ops

ops.reset_default_graph()

# 创建计算图
sess = tf.Session()

# 加载数据并划分数据，80%数据用来训练，20%的数据用来做测试

# 加载数据
# iris数据 [(Sepal Length, Sepal Width, Petal Length, Petal Width)]
iris = datasets.load_iris()
x_vals = np.array([[x[0], x[3]] for x in iris.data])
y_vals = np.array([1 if y == 0 else -1 for y in iris.target])

# 加载数据
train_indices = np.random.choice(len(x_vals), round(len(x_vals) * 0.8), replace=False)
test_indices = np.array(list(set(range(len(x_vals))) - set(train_indices)))
x_vals_train = x_vals[train_indices]
x_vals_test = x_vals[test_indices]
y_vals_train = y_vals[train_indices]
y_vals_test = y_vals[test_indices]

# 声明参数
batch_size = 100  # 批量大小
max_iter = 500  # 最大迭代次数

# 初始化占位符
x_data = tf.placeholder(shape=[None, 2], dtype=tf.float32)
y_target = tf.placeholder(shape=[None, 1], dtype=tf.float32)

# 创建变量
A = tf.Variable(tf.random_normal(shape=[2, 1]))
b = tf.Variable(tf.random_normal(shape=[1, 1]))


# 声明操作 模型
model_output = tf.subtract(tf.matmul(x_data, A), b)

# 声明L2正则化
l2_norm = tf.reduce_sum(tf.square(A))

# 声明损失函数
# = max(0, 1-pred*actual) + alpha * L2_norm(A)^2
# L2 正则化参数 alpha
alpha = tf.constant([0.01])
# Margin term in loss
classification_term = tf.reduce_mean(
    tf.maximum(0.0, tf.subtract(1.0, tf.multiply(model_output, y_target)))
)
# 损失函数
loss = tf.add(classification_term, tf.multiply(alpha, l2_norm))

# 声明预测函数
prediction = tf.sign(model_output)
accuracy = tf.reduce_mean(tf.cast(tf.equal(prediction, y_target), tf.float32))

# 声明优化器
my_opt = tf.train.GradientDescentOptimizer(0.01)
train_step = my_opt.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()
sess.run(init)

# 开始训练
loss_vec = []
train_accuracy = []
test_accuracy = []
for i in range(max_iter):
    rand_index = np.random.choice(len(x_vals_train), size=batch_size)
    rand_x = x_vals_train[rand_index]
    rand_y = np.transpose([y_vals_train[rand_index]])
    sess.run(train_step, feed_dict={x_data: rand_x, y_target: rand_y})

    temp_loss = sess.run(loss, feed_dict={x_data: rand_x, y_target: rand_y})
    loss_vec.append(temp_loss)

    train_acc_temp = sess.run(
        accuracy,
        feed_dict={x_data: x_vals_train, y_target: np.transpose([y_vals_train])},
    )
    train_accuracy.append(train_acc_temp)

    test_acc_temp = sess.run(
        accuracy, feed_dict={x_data: x_vals_test, y_target: np.transpose([y_vals_test])}
    )
    test_accuracy.append(test_acc_temp)

    if (i + 1) % 100 == 0:
        print(
            "Step #"
            + str(i + 1)
            + " A = "
            + str(sess.run(A))
            + " b = "
            + str(sess.run(b))
        )
        print("损失为 " + str(temp_loss))

# 提取系数
[[a1], [a2]] = sess.run(A)
[[b]] = sess.run(b)
slope = -a2 / a1
y_intercept = b / a1

# 提取 x1 and x2 vals
x1_vals = [d[1] for d in x_vals]

# Get best fit line
best_fit = []
for i in x1_vals:
    best_fit.append(slope * i + y_intercept)

# 分离数据
setosa_x = [d[1] for i, d in enumerate(x_vals) if y_vals[i] == 1]
setosa_y = [d[0] for i, d in enumerate(x_vals) if y_vals[i] == 1]
not_setosa_x = [d[1] for i, d in enumerate(x_vals) if y_vals[i] == -1]
not_setosa_y = [d[0] for i, d in enumerate(x_vals) if y_vals[i] == -1]

# 分类效果展示
plt.plot(setosa_x, setosa_y, "o", label="I. setosa")
plt.plot(not_setosa_x, not_setosa_y, "x", label="Non-setosa")
plt.plot(x1_vals, best_fit, "r-", label="Linear Separator", linewidth=3)
plt.ylim([0, 10])
plt.legend(loc="lower right")
plt.title("Sepal Length vs Pedal Width")
plt.xlabel("Pedal Width")
plt.ylabel("Sepal Length")
plt.show()

# 训练和测试精度展示
plt.plot(train_accuracy, "k-", label="Training Accuracy")
plt.plot(test_accuracy, "r--", label="Test Accuracy")
plt.title("Train and Test Set Accuracies")
plt.xlabel("Generation")
plt.ylabel("Accuracy")
plt.legend(loc="lower right")
plt.show()

# 损失与迭代次数的关系
plt.plot(loss_vec, "k-")
plt.title("Loss per Generation")
plt.xlabel("Generation")
plt.ylabel("Loss")
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


"""
xmin, xmax, ymin, ymax = -8, 8, -8, 8
#plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
"""

print("計算兩陣列的雷同率")
y = np.array(
    [
        0,
        2,
        1,
        2,
        2,
        0,
        0,
        0,
        0,
        1,
        1,
        2,
        0,
        2,
        0,
        1,
        1,
        0,
        1,
        2,
        2,
        2,
        2,
        0,
        2,
        0,
        2,
        2,
        1,
        2,
        2,
        2,
        0,
        2,
        2,
        0,
        1,
        1,
        2,
        0,
        1,
        1,
        1,
        1,
        2,
        2,
        0,
        1,
        2,
        1,
        0,
        1,
        1,
        1,
        2,
        2,
        0,
        2,
        1,
        1,
        1,
        0,
        0,
        2,
        0,
        1,
        1,
        0,
        2,
        2,
        2,
        2,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        2,
        1,
        1,
        0,
        0,
        1,
        0,
        2,
        0,
        0,
        2,
        1,
        1,
        0,
        0,
        1,
        2,
        1,
        0,
        2,
        1,
    ]
)
y_pred = np.array(
    [
        0,
        2,
        1,
        2,
        2,
        0,
        0,
        0,
        0,
        1,
        1,
        0,
        0,
        2,
        0,
        2,
        0,
        0,
        1,
        2,
        2,
        2,
        2,
        0,
        2,
        1,
        2,
        2,
        1,
        2,
        2,
        2,
        0,
        2,
        2,
        0,
        0,
        1,
        2,
        0,
        1,
        1,
        2,
        1,
        2,
        2,
        0,
        0,
        2,
        1,
        0,
        1,
        1,
        1,
        2,
        2,
        0,
        2,
        1,
        1,
        1,
        0,
        0,
        2,
        0,
        1,
        1,
        0,
        2,
        2,
        2,
        2,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        2,
        1,
        1,
        0,
        0,
        1,
        0,
        2,
        0,
        0,
        2,
        1,
        2,
        0,
        0,
        2,
        2,
        1,
        0,
        2,
        1,
    ]
)

print("type y_pred :", type(y_pred))
print("len y_pred :", len(y_pred))

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
# print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)


# X = iris.data[:, :2]  # We only take the first two features
