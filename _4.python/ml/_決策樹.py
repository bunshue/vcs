"""
機器學習_決策樹

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
import sklearn.linear_model
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from matplotlib.colors import ListedColormap

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf = clf.fit(X, Y)  # 學習訓練.fit

prediction = clf.predict([[173, 76]])  # 預測.predict
print(prediction)

plt.plot(X[:3, 0], X[:3, 1], "rx", label="男生")
plt.plot(X[3:, 0], X[3:, 1], "g.", label="女生")
plt.plot([173], [76], "r^", label="預測點")  # 預測點
plt.ylabel("體重")
plt.xlabel("身高")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import tree

# from sklearn.externals.six import StringIO
import pydot
from os import system

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf = clf.fit(X, Y)  # 學習訓練.fit

tree.export_graphviz(clf, out_file="tmp_tree222.dot")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup markers generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )

    z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)  # 預測.predict
    z = z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot all samples
    X_test, y_test = X[test_idx, :], y[test_idx]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.8,
            c=cmap(idx),
            marker=markers[idx],
            label=cl,
        )

    # hightlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(
            X_test[:, 0],
            X_test[:, 1],
            # c='',
            alpha=1.0,
            linewidth=1,
            marker="o",
            s=55,
            label="test set",
        )


print("------------------------------------------------------------")  # 60個


def do_decision_tree():
    iris = datasets.load_iris()
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data[:, [2, 3]], iris.target, test_size=0.25, random_state=4
    )
    clf = DecisionTreeClassifier(
        criterion="entropy", max_depth=3, random_state=0
    )  # 決策樹函數學習機
    clf.fit(x_train, y_train)  # 學習訓練.fit
    y_pred = clf.predict(x_test)  # 預測.predict

    X_combined = np.vstack((x_train, x_test))
    y_combined = np.hstack((y_train, y_test))

    plot_decision_regions(X_combined, y_combined, classifier=clf)
    plt.xlabel("petal length [cm]")
    plt.ylabel("petal width [cm]")
    plt.legend(loc="upper left")
    plt.show()


print("決策樹")
do_decision_tree()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
