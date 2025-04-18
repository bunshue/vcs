"""
機器學習_決策樹(Decision Tree)
機器學習_決策樹分類(Decision Tree Classifier)
機器學習_迴歸樹(Decision Tree Regression / Regression Tree)
"""
print("------------------------------------------------------------")  # 60個

# 共同
import re
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

from common1 import *


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

import json
import scipy
import sklearn
import sklearn.linear_model
import sklearn.svm as svm
import sklearn.tree as tree
from sklearn import metrics
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_hastie_10_2
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn.tree import DecisionTreeClassifier  # 決策樹分類(Decision Tree Classifier)
from sklearn.tree import DecisionTreeRegressor  # 迴歸樹
from sklearn.tree import plot_tree  # 繪製樹狀圖
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import classification_report  # 分類報告
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_curve
from sklearn.metrics import recall_score

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用 iris 資料
# X, y = datasets.load_iris(return_X_y=True) # same
iris = datasets.load_iris()
X = iris.data  # 取出4欄資料
y = iris.target

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf.fit(x_train, y_train)  # 學習訓練.fit

# 決策樹可視化存檔
# sklearn.tree.export_graphviz(clf, out_file="tmp_tree1.dot")

# 對測試數據做預測
y_pred = clf.predict(x_test)  # 預測.predict

print("真實答案 :\n", y_test, sep="")
print("預測結果 :\n", y_pred, sep="")
print("預測差值 :\n", y_pred - y_test, sep="")

# 輸出準確性
print(f"訓練資料的準確性 = {clf.score(x_train, y_train)}")
print(f"測試資料的準確性 = {clf.score(x_test, y_test)}")
print(f"全部資料的準確性 = {clf.score(X, y)}")

scores = cross_val_score(clf, X, y, cv=5)
print("看一下5次的成績 :", scores)
print("平均 :", scores.mean())

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


print("決策樹")

iris = datasets.load_iris()

X = iris.data[:, [2, 3]]  # 取出2欄資料, 為了畫圖
y = iris.target

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)  # 決策樹函數學習機

clf.fit(x_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(x_test)  # 預測.predict
"""
print("真實答案 :\n", y, sep="")
print("預測結果 :\n", y_pred, sep="")
print("預測差值 :\n", y_pred - y, sep="")
"""
X_combined = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))

plot_decision_regions(X_combined, y_combined, classifier=clf)
plt.xlabel("瓣長")
plt.ylabel("瓣寬")
plt.legend()
plt.title("決策樹")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
AllElectronics.csv 14筆資料 5個欄位
age, income, student, credit_rating, buys_computer
1,   3,      0,       1,             0
1,   3,      0,       2,             0
2,   3,      0,       1,             1
3,   2,      0,       1,             1
3,   1,      1,       1,             1
3,   1,      1,       2,             0
2,   1,      1,       2,             1
1,   2,      0,       1,             0
"""

# 決策樹

pd.set_option("display.max_columns", None)

data = pd.read_csv("data/AllElectronics.csv", skipinitialspace=True)
print(data.shape)
cc = data.head()
print("(全部)前5筆資料 :\n", cc, sep="")

# 資料 取出前4欄位 age ~ credit_rating
X = data.loc[:, "age":"credit_rating"]

# 目標 取出第5欄位 是否購買電腦
y = data["buys_computer"]

cc = X.head()
print("(資料)前5筆資料 :\n", cc, sep="")

# CART算法(分类树)
# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=9487,
)  # 決策樹函數學習機  # 当前支持计算信息增益和GINI

clf.fit(X, y)  # 學習訓練.fit

# 決策樹可視化存檔
# sklearn.tree.export_graphviz(clf, out_file="tmp_cart2.dot")

import pydotplus
from IPython.display import Image  # 用IPython

# 決策樹可視化存檔
dot_data = sklearn.tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=X.columns,
    max_depth=5,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)

# Image(graph.create_png())   # 用IPython顯示圖片 skip

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 決策樹分類

""" Social_Network_Ads.csv 400筆資料 5個欄位
User ID,  Gender, Age, EstimatedSalary, Purchased
15624510, Male,   19,  19000,           0
15810944, Male,   35,  20000,           0
15668575, Female, 26,  43000,           0
15603246, Female, 27,  57000,           0
"""

df = pd.read_csv("data/Social_Network_Ads.csv")
# print(df) # 包含df之column與index

# 不包含df之column與index 只有資料內容 400筆資料 5個欄位
print("df之資料內容 :\n", df.values, sep="")

# 資料 取出第3 4欄
X = df.iloc[:, [2, 3]].values
# 目標 取出第5欄
y = df.iloc[:, 4].values

# print("X 第3 4欄 : (年齡 薪資)\n", X, sep="")
# print("y 第5欄 : (是否購買)\n", y, sep="")

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放 Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# Fitting Decision Tree Classification to the Training set

clf = DecisionTreeClassifier(criterion="entropy", random_state=9487)  # 決策樹函數學習機

clf.fit(X_train, y_train)  # 學習訓練.fit

# 預測測試資料
y_pred = clf.predict(X_test)  # 預測.predict

# 混淆矩陣
cm = confusion_matrix(y_test, y_pred)
print("混淆矩陣 :\n", cm, sep="")

# 畫訓練資料結果 Visualising the Training set results
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.figure(figsize=(12, 5))
plt.subplot(121)
plt.contourf(
    X1,
    X2,
    clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Decision Tree Classification (訓練資料)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

# show()

# 畫測試資料結果 Visualising the Test set results
X_set, y_set = X_test, y_test

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

plt.subplot(122)
plt.contourf(
    X1,
    X2,
    clf.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
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
plt.title("Decision Tree Classification (測試資料)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

plt.suptitle("決策樹")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from graphviz import Digraph

styles = {
    "top": {"shape": "ellipse", "style": "filled", "color": "lightblue"},
    "no": {"shape": "circle", "style": "filled", "color": "red"},
    "yes": {"shape": "circle", "style": "filled", "color": "lightgreen"},
    "qst": {"shape": "rect"},
}

example_tree = Digraph()

example_tree.node("top", "Should I attend the ML lecture?", styles["top"])
example_tree.node("q1", "Do I fulfill requirements?", styles["qst"])

example_tree.node("q2", "Do I like CS?", styles["qst"])
example_tree.node("no1", "No ", styles["no"])

example_tree.node("q3", "Is the lecture early in the morning?", styles["qst"])
example_tree.node("no2", "No ", styles["no"])

example_tree.node("no3", "No ", styles["no"])
example_tree.node("yes", "Yes", styles["yes"])

example_tree.edge("top", "q1")

example_tree.edge("q1", "q2", "Yes")
example_tree.edge("q1", "no1", "No")

example_tree.edge("q2", "q3", "Yes")
example_tree.edge("q2", "no2", "No")

example_tree.edge("q3", "no3", "Yes")
example_tree.edge("q3", "yes", "No")

example_tree

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# first define some points representing two classes
grid = np.mgrid[0:10:2, 0:10:2]
set01 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set01 = np.delete(set01, [17, 18, 19, 22, 24], axis=0)

grid = np.mgrid[6:16:2, 0:10:2]
set02 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set02 = np.delete(set02, [0, 1, 5, 6, 8], axis=0)

plt.scatter(*set01.T)
plt.scatter(*set02.T)

plt.text(
    15,
    4,
    "There are two attributes: x and y\n\n"
    "    * each decision node splits dataset based on one of the attributes\n\n"
    "    * each leaf node defines a class label",
)
show()

plt.scatter(*set01.T)
plt.scatter(*set02.T)

plt.plot([5, 5], [0, 8], "r")
plt.plot([0, 14], [3, 3], "g")

plt.text(
    15,
    3,
    "We start with [20, 20] (blue, orange)\n\n"
    "Red line splits dataset in [15, 0] (left) and [5, 20] (right)\n\n"
    "Green line split dataset in [10, 6] (bottom) and [10, 14] (top)\n\n"
    "Red line is a winner and should be the root of our tree",
)
show()

tree = Digraph()

tree.edge("x > 5?\n[20, 20]", "blue\n[15, 0]", "No")
tree.edge("x > 5?\n[20, 20]", "y > 3?\n[5, 20]", "Yes")

tree.edge("y > 3?\n[5, 20]", "x > 9?\n[4, 6]", "No")
tree.edge("y > 3?\n[5, 20]", "almost orange\n[1, 14]", "Yes")

tree.edge("x > 9?\n[4, 6]", "blue\n[4, 0]", "No")
tree.edge("x > 9?\n[4, 6]", "orange\n[0, 6]", "Yes")

tree.edge("almost orange\n[1, 14]", "Should we continue?\nOr would it be overfitting?")

tree

tree = Digraph()

tree.edge("y > 3?\n[20, 20]", "x > 9?\n[10, 6]", "No")
tree.edge("y > 3?\n[20, 20]", "x > 5?\n[10, 14]", "Yes")

tree.edge("x > 9?\n[10, 6]", "blue\n[10, 0]", "No")
tree.edge("x > 9?\n[10, 6]", "orange\n[0, 6]", "Yes")

tree.edge("x > 5?\n[10, 14]", "blue\n[9, 0]", "No")
tree.edge("x > 5?\n[10, 14]", "almost orange\n[1, 14]", "Yes")

tree

# ID3 and C4.5 algorithms
"""
ID3 (Iterative Dichotomiser 3)
C4.5 - extension of ID3 (why C4.5? C stands for programming language and 4.5 for version?)
C5.0/See5 - improved C4.5 (commercial; single-threaded Linux version is available under GPL though)
"""

x = np.arange(0.01, 1.01, 0.01)

plt.xlabel("p")
plt.ylabel("I(p)")

plt.plot(x, -np.log2(x), label="bit")
plt.plot(x, -np.log(x), label="nat")
plt.plot(x, -np.log10(x), label="dit")

plt.legend()
show()

p = np.arange(0.01, 1.0, 0.01)

plt.annotate(
    "we are surprised",
    xy=(0.5, 1),  # 箭頭尾
    xytext=(0.5, 0.75),  # 字的位置
    arrowprops=dict(facecolor="black", shrink=0.1),
)

plt.annotate(
    "we are not that surprised",
    xy=(1, 0.1),  # 箭頭尾
    xytext=(0.5, 0.25),  # 字的位置
    arrowprops=dict(facecolor="black", shrink=0.1),
)

plt.plot(p, -p * np.log2(p) - (1 - p) * np.log2(1 - p))

plt.xlabel("p")
plt.ylabel("H")

show()

from mpl_toolkits import mplot3d

# grid of p, q probabilities
p, q = np.meshgrid(np.arange(0.01, 1.0, 0.01), np.arange(0.01, 1.0, 0.01))

# remove (set to 0) points which do not fulfill P <= 1
idx = p + q > 1
p[idx] = 0
q[idx] = 0

# calculate entropy (disable warnings - we are aware of log(0))
# np.warnings.filterwarnings("ignore")
h = -p * np.log2(p) - q * np.log2(q) - (1 - p - q) * np.log2(1 - p - q)

# make a plot
plt.axes(projection="3d").plot_surface(p, q, h)

show()


def entropy(*probs):
    """Calculate information entropy"""
    try:
        total = sum(probs)
        return sum([-p / total * math.log(p / total, 2) for p in probs])
    except:
        return 0


print(entropy(4, 5), entropy(2, 1), entropy(2, 2))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Play Golf dataset
    Popular dataset to explain decision trees
    4 features:
        outlook: rainy, overcast, sunny
        temperature: cool, mild, hot
        humidity: normal, high
        windy: false, true

    Possible outcomes (play golf?):
        false
        true
"""


# first row = headers
src = "http://chem-eng.utoronto.ca/~datamining/dmc/datasets/weather_nominal.csv"
src = "data/weather-nominal-weka.csv"

golf_data = pd.read_csv(src)

print(golf_data)

# Play golf entropy

cc = entropy(9, 5)
print(cc)

# Play golf vs outlook

cc = entropy(3, 2), 0, entropy(2, 3)
print(cc)

# (0.9709505944546686, 0, 0.9709505944546686)

# Results for all features

tree = Digraph()

tree.edge("outlook", "sunny")
tree.edge("outlook", "overcast")
tree.edge("outlook", "rainy")

tree.edge("overcast", "yes")

print(tree)

# Next branch

cc = golf_data.loc[golf_data["outlook"] == "sunny"]
print(cc)

tree.edge("sunny", "windy")

tree.edge("windy", "false")
tree.edge("windy", "true")

tree.edge("false", "yes")
tree.edge("true", "no")

print(tree)

# Last branch

cc = golf_data.loc[golf_data["outlook"] == "rainy"]
print(cc)

tree.edge("rainy", "humidity")

tree.edge("humidity", "high")
tree.edge("humidity", "normal")

tree.edge("normal", "yes")
tree.edge("high", "no ")

print(tree)

# Information gain for name

h = entropy(4, 6)  # dataset entropy H(T)

# one John plays and the other one doesn't
# in other cases entropy = 0
g_name = h - 2 / 10 * entropy(1, 1)

print(g_name)

# 0.7709505944546686

# Information gain for sex

# 5 men - 3 play
# 5 women - 3 play
g_sex = h - 5 / 10 * entropy(2, 3) - 5 / 10 * entropy(2, 3)

print(g_sex)

# 0.0

# Information gain for age

# 4 old people - 1 plays
# 6 young people - 5 play
g_age = h - 4 / 10 * entropy(1, 3) - 6 / 10 * entropy(1, 5)

print(g_age)

# 0.256425891682003

# Information gain ratio for name

# 2x John, 2x Alex, 6x unique name
cc = g_name / entropy(2, 2, *[1] * 6)
print(cc)

# 0.26384995435159336

# Information gain ratio for sex

# 5 males and 5 females - zero stays zero though
cc = g_sex / entropy(5, 5)
print(cc)

# 0.0

#  Information gain ratio for age

# 4x old and 6x young
cc = g_age / entropy(4, 6)
print(cc)

# 0.26409777505314147

print("Two possible values:\n")

for i in range(0, 11):
    print("\t({}, {}) split -> entropy = {}".format(i, 10 - i, entropy(i, 10 - i)))

print("\n10 possible values:", entropy(*[1] * 10))

# calculate entropy for all possible thresholds
e18 = 2 / 10 * entropy(1, 1) + 8 / 10 * entropy(3, 5)
e24 = 4 / 10 * entropy(1, 3) + 6 / 10 * entropy(3, 3)
e31 = 6 / 10 * entropy(1, 5) + 4 / 10 * entropy(3, 1)
e50 = 9 / 10 * entropy(4, 5) + 1 / 10 * entropy(0, 1)

print("With threshold = {}, entropy = {}".format(18, e18))
print("With threshold = {}, entropy = {}".format(24, e24))
print("With threshold = {}, entropy = {}".format(31, e31))
print("With threshold = {}, entropy = {}".format(50, e50))

# First example - step by step

# first define some points representing two classes
grid = np.mgrid[0:10:2, 0:10:2]
set01 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set01 = np.delete(set01, [17, 18, 19, 22, 24], axis=0)

grid = np.mgrid[6:16:2, 0:10:2]
set02 = np.vstack([grid[0].ravel(), grid[1].ravel()]).T
set02 = np.delete(set02, [0, 1, 5, 6, 8], axis=0)

plt.scatter(*set01.T)
plt.scatter(*set02.T)

show()

# Validation set

# split dataset to training and validation set
# note, we should splt them randomly
# but here we do this by hand
valid_idx = [3, 7, 10, 14, 18]

blue_valid = set01[valid_idx]
blue_train = np.delete(set01, valid_idx, axis=0)

orange_valid = set02[valid_idx]
orange_train = np.delete(set02, valid_idx, axis=0)

# circles - training set
# x - validation set
plt.scatter(*blue_train.T)
plt.scatter(*blue_valid.T, color="C0", marker="x")
plt.scatter(*orange_train.T)
plt.scatter(*orange_valid.T, color="C1", marker="x")

show()

# Thresholds finder


def info_gain(Nb, No, nb, no):
    """Calculate information gain for given split"""
    h = entropy(Nb, No)  # H(S)
    total = Nb + No  # total number of samples
    subtotal = nb + no  # number of samples in subset

    return (
        h
        - subtotal / total * entropy(nb, no)
        - (total - subtotal) / total * entropy(Nb - nb, No - no)
    )


# Feature X

Nb = 15
No = 15

splits = {
    "0": (4, 0),
    "2 ": (8, 0),
    "4": (11, 0),
    "6": (13, 3),
    "8": (15, 4),
    "10": (15, 8),
    "12": (15, 11),
}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

# 4 samples with x = 0, 4 samples with x = 2 etc
cc = info_gain(Nb, No, *splits["4"]) / entropy(4, 4, 3, 5, 3, 4, 3, 4)
print(cc)

# Feature Y

Nb = 15
No = 15

splits = {"0": (4, 2), "2": (8, 5), "4": (10, 8), "6": (13, 11)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

cc = info_gain(Nb, No, *splits["2"]) / entropy(6, 7, 5, 6, 6)
print(cc)

# The root

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "[4, 15]", "Yes")

print(tree)

plt.xlim([5.5, 14.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)

show()

# Check x maximum information gain ratio

Nb = 4
No = 15

splits = {"6": (2, 3), "8": (4, 4), "10": (4, 8), "12": (4, 11)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

print(
    "Information gain ratio with x > 8:",
    info_gain(Nb, No, *splits["8"]) / entropy(5, 3, 4, 3, 4),
)

# Information gain ratio with x > 8: 0.14010311259651076

# Check y maximum information gain ratio

Nb = 4
No = 15

splits = {"0": (2, 2), "2": (3, 5), "4": (3, 6), "6": (4, 9)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))


print(
    "Information gain ratio with y > 6:",
    info_gain(Nb, No, *splits["6"]) / entropy(4, 4, 3, 4, 4),
)

# Information gain ratio with y > 6: 0.05757775370755489

# Once again x is a winner
# And we have a new node

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

print(tree)

# Branch x<= 8

# We will continue until the tree is fully grown

plt.xlim([5.5, 8.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)

show()

# Again, the best cut may be pretty obvious, but lets check the math
# We have one possible cut in x

Nb = 4
No = 4


print("Information gain ratio with x > 6:", info_gain(Nb, No, 2, 3) / entropy(5, 3))

# Information gain ratio with x > 6: 0.05112447853477686

# And usual threshold candidates in y

splits = {"0": (2, 0), "2": (3, 0), "4": (3, 1), "6": (4, 2)}

for threshold, (no, nb) in splits.items():
    print("Threshold = {}\t -> {}".format(threshold, info_gain(Nb, No, no, nb)))

print(
    "Information gain ratio with y > 2:",
    info_gain(Nb, No, *splits["2"]) / entropy(2, 1, 1, 2, 2),
)

# Information gain ratio with y > 2: 0.24390886253128827

# And the tree is growing

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "[1, 4]", "Yes")

tree

# Branch y > 2

plt.xlim([5.5, 8.5])
plt.ylim([3.5, 8.5])

plt.scatter(*blue_train.T)
plt.scatter(*orange_train.T)

show()

Nb = 1
No = 4

print("Information gain ratio with x > 6:", info_gain(Nb, No, 0, 3) / entropy(3, 2))

# Information gain ratio with x > 6: 0.33155970728682876

print("Information gain ratio with y > 4:", info_gain(Nb, No, 0, 1) / entropy(1, 2, 2))

print("Information gain ratio with y > 6:", info_gain(Nb, No, 1, 2) / entropy(1, 2, 2))

# Information gain ratio with y > 4: 0.047903442721748145
# Information gain ratio with y > 6: 0.11232501392736344

# The final tree

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "x > 6?\n[1, 4]", "Yes")

tree.edge("x > 6?\n[1, 4]", "orange\n[0, 3]", "No")
tree.edge("x > 6?\n[1, 4]", "y > 6?\n[1, 1]", "Yes")

tree.edge("y > 6?\n[1, 1]", "blue\n[1, 0]", "No")
tree.edge("y > 6?\n[1, 1]", "orange\n[0, 1]", "Yes")

tree

"""
It is likely that this tree is overfitted
We will proceed with pruning as it was explained
But first lets implement decision rules to measure accuracy
"""


def tree_nominal(x, y):
    """Implementation of above tree"""
    if x <= 4:
        return "blue"
    elif x > 8:
        return "orange"
    elif y <= 2:
        return "blue"
    elif x <= 6:
        return "orange"
    else:
        return "orange" if y > 6 else "blue"


# Sanity check

# If the tree is built correctly we expect 100% accuracy on training set

for x, y in blue_train:
    print(tree_nominal(x, y), end=" ")

# blue blue blue blue blue blue blue blue blue blue blue blue blue blue blue

for x, y in orange_train:
    print(tree_nominal(x, y), end=" ")

# orange orange orange orange orange orange orange orange orange orange orange orange orange orange orange

# Accuracy before pruning


def accuracy(samples, tree):
    # Just print the result of classification
    for x, y in samples:
        print("({}, {}) -> {}".format(x, y, tree(x, y)))


cc = accuracy(blue_valid, tree_nominal)
print(cc)

""" NG
cc = accuracy(orange_valid, tree)
print(cc)
"""

"""
Pruning I
    We want to prune last decision node 
    In general, majority decides about the leaf node class
    As it is a tie here, lets check both
"""


def tree_prune01a(x, y):
    """Implementation of above tree"""
    if x <= 4:
        return "blue"
    elif x > 8:
        return "orange"
    elif y <= 2:
        return "blue"
    elif x <= 6:
        return "orange"
    else:
        return "blue"


def tree_prune01b(x, y):
    """Implementation of above tree"""
    if x <= 4:
        return "blue"
    elif x > 8:
        return "orange"
    elif y <= 2:
        return "blue"
    else:
        return "orange"


cc = accuracy(blue_valid, tree_prune01a)
print(cc)

cc = accuracy(orange_valid, tree_prune01a)
print(cc)

"""
    Pruning does not change the accuracy

    We always use Occam's razor and prune01a is preferred over nominal tree

    But lets see how prune01b works
"""
cc = accuracy(blue_valid, tree_prune01b)
print(cc)

cc = accuracy(orange_valid, tree_prune01b)
print(cc)

"""
    In this case we even get the increase of the accuracy

    We decide to prune a tree by replacing y>6 decision node with "orange" leaf node

Which automatically removes x> 6    decision node
"""

tree = Digraph()

tree.edge("x > 4?\n[15, 15]", "blue\n[11, 0]", "No")
tree.edge("x > 4?\n[15, 15]", "x > 8?\n[4, 15]", "Yes")

tree.edge("x > 8?\n[4, 15]", "y > 2?\n[4, 4]", "No")
tree.edge("x > 8?\n[4, 15]", "orange\n[0, 11]", "Yes")

tree.edge("y > 2?\n[4, 4]", "blue\n[3, 0]", "No")
tree.edge("y > 2?\n[4, 4]", "orange\n[1, 4]", "Yes")

tree

"""
Pruning II

    Now, lets see the accuracy after removing y>2 node

    It is once again a tie, so lets check both scenarios
"""


def tree_prune02a(x, y):
    """Implementation of above tree"""
    if x <= 4:
        return "blue"
    else:
        return "orange"


def tree_prune02b(x, y):
    """Implementation of above tree"""
    if x <= 4:
        return "blue"
    elif x > 8:
        return "orange"
    else:
        return "blue"


cc = accuracy(blue_valid, tree_prune02a)
print(cc)

cc = accuracy(orange_valid, tree_prune02a)
print(cc)

cc = accuracy(blue_valid, tree_prune02b)
print(cc)

cc = accuracy(orange_valid, tree_prune02b)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# CART
# Gini impurity

p = np.arange(0.01, 1.0, 0.01)

plt.xlabel("p")
plt.ylabel("surprise factor")
plt.plot(p, -p * np.log2(p) - (1 - p) * np.log2(1 - p), label="Entropy")
show()

plt.plot(p, -2 * p * (p - 1), label="Gini impurity")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Play Golf

# Lets consider once again Play Golf dataset

# first row = headers
src = "http://chem-eng.utoronto.ca/~datamining/dmc/datasets/weather_nominal.csv"
src = "data/weather-nominal-weka.csv"

golf_data = pd.read_csv(src)

print(golf_data)

# Gini impurity


def gini(*distribution):
    """Calculate gini impurity for given ditribution of samples"""
    sum2 = sum(distribution) ** 2  # normalization factor

    return 1 - sum([p**2 for p in distribution]) / sum2


def gini_split(s1, s2, g1, g2):
    """Calcualte impurity for given split

    s1 -- the size of S1 subset
    s1 -- the size of S2 subset
    g1 -- I(S1)
    g2 -- I(S2)
    """
    s = s1 + s2  # the total set size

    return s1 / s * g1 + s2 / s * g2


"""
            | Play golf |
            =============
            | yes | no  |
      -------------------
      | yes |  2  |  3  | 5
rainy | no  |  7  |  2  | 9
      -------------------
               9     5
"""
cc = gini_split(5, 9, gini(2, 3), gini(7, 2))
print(cc)

# 0.3936507936507937
"""
            | Play golf |
            =============
            | yes | no  |
      -------------------
      | yes |  3  |  2  | 5
sunny | no  |  6  |  3  | 9
      -------------------
               9     5

"""
cc = gini_split(5, 9, gini(3, 2), gini(6, 3))
print(cc)

# 0.45714285714285713
"""
               | Play golf |
               =============
               | yes | no  |
         -------------------
         | yes |  4  |  0  | 4
overcast | no  |  5  |  5  | 10
         -------------------
                  9     5
"""
cc = gini_split(4, 10, gini(4, 0), gini(5, 5))
print(cc)

# 0.35714285714285715

# Scikit learn

from sklearn.preprocessing import LabelEncoder

# pandas.DataFrame.apply applies a function to given axis (0 by default)
# LabelEncoder encodes class labels with values between 0 and n-1
golf_data_num = golf_data.apply(LabelEncoder().fit_transform)

cc = golf_data_num
print(cc)

# Now, lets splits our dataset to features and labels

# DataFrame.iloc makes an access thourgh indices
# we want all rows and first 4 columns for features
# and the last column for labels
data = np.array(golf_data_num.iloc[:, :4])
target = np.array(golf_data_num.iloc[:, 4])

# Once data is prepared, creating a tree is as easy as 2 + 2 -1

golf_tree = DecisionTreeClassifier()  # 決策樹函數學習機
golf_tree.fit(data, target)
show()

# sklearn.tree supports drawing a tree using graphviz

import graphviz

# dot is a graph description language
# 決策樹可視化存檔
dot = sklearn.tree.export_graphviz(
    golf_tree,
    out_file=None,
    feature_names=golf_data.columns.values[:4],
    class_names=["no", "yes"],
    filled=True,
    rounded=True,
    special_characters=True,
)

# we create a graph from dot source using graphviz.Source
graph = graphviz.Source(dot)
graph

# Regression

X = np.random.sample(50)
Y = np.array([x**2 + np.random.normal(0, 0.05) for x in X])

plt.scatter(X, Y, color="b")
plt.plot([0.3, 0.3], [-0.2, 1.2], "g--")
plt.plot([0.6, 0.6], [-0.2, 1.2], "g--")
plt.xlabel("x")
plt.ylabel("y")

show()

# The corresponding tree would look like this

tree = Digraph()

tree.edge("x < 0.3?", "?", "No")
tree.edge("x < 0.3?", "x < 0.6?", "Yes")

tree.edge("x < 0.6?", "? ", "No")
tree.edge("x < 0.6?", "?  ", "Yes")

tree


def avg(X, Y, x_min, x_max):
    """Return the average value in (x_min, x_max) range"""
    n = 0  # number of samples in given split
    avg = 0  # average value

    for x, y in zip(X, Y):
        if x >= x_min and x < x_max:
            n += 1
            avg += y

    return avg / n


plt.scatter(X, Y, color="b")

plt.plot([0.3, 0.3], [-0.2, 1.2], "g--")
plt.plot([0.6, 0.6], [-0.2, 1.2], "g--")

y = avg(X, Y, 0, 0.3)
plt.plot([0.0, 0.3], [y, y], "r")

y = avg(X, Y, 0.3, 0.6)
plt.plot([0.3, 0.6], [y, y], "r")

y = avg(X, Y, 0.6, 1)
plt.plot([0.6, 1.0], [y, y], "r")
show()

# Growing a tree

# create a decision tree regressor
fit = DecisionTreeRegressor()

# and grow it (note that X must be reshaped)
fit.fit(np.reshape(X, (-1, 1)), Y)
show()

# prepare test sample with "newaxis" trick
X_test = np.arange(0.0, 1.0, 0.01)[:, np.newaxis]
Y_test = fit.predict(X_test)

plt.scatter(X, Y, color="b")
plt.plot(X_test, Y_test)
show()

# Tree: cross-validation


class TreeCV:
    """Perform a cross-validation for chosen hyperparameter"""

    def __init__(self, X, Y, hp="max_depth"):
        """Save training data"""
        self.X = X  # features
        self.Y = Y  # targets
        self.hp = hp  # hyperparameter

    def set_method(self, hp):
        """Set hyperparameter to use"""
        self.hp = hp

    def cross_me(self, *hp_vals):
        """Perform cross validation for given hyperparameter values"""
        self.scores = []  # the accuracy table
        self.best = None  # the best fit

        best_score = 0

        for hp in hp_vals:
            # create a tree with given hyperparameter cut
            fit = DecisionTreeRegressor(**{self.hp: hp})

            # calculate a cross validation scores and a mean value
            score = cross_val_score(fit, np.reshape(X, (-1, 1)), Y).mean()

            # update best fit if necessary
            if score > best_score:
                self.best = fit
                best_score = score

            self.scores.append([hp, score])

        # train the best fit
        self.best.fit(np.reshape(X, (-1, 1)), Y)

    def plot(self):
        """Plot accuracy as a function of hyperparameter values and best fit"""
        plt.figure(figsize=(15, 5))

        plt.subplot(1, 2, 1)

        plt.xlabel(self.hp)
        plt.ylabel("accuracy")

        plt.plot(*zip(*self.scores))

        plt.subplot(1, 2, 2)

        X_test = np.arange(0.0, 1.0, 0.01)[:, np.newaxis]
        Y_test = self.best.predict(X_test)

        plt.scatter(self.X, self.Y, color="b", marker=".", label="Training data")
        plt.plot(X_test, X_test * X_test, "g", label="True distribution")
        plt.plot(X_test, Y_test, "r", label="Decision tree")

        plt.legend()


# Traning dataset

X = np.random.sample(200)
Y = np.array([x**2 + np.random.normal(0, 0.05) for x in X])

# max_depth

tree_handler = TreeCV(X, Y)
tree_handler.cross_me(*range(1, 10))
tree_handler.plot()
show()

# min_samples_leaf

tree_handler.set_method("min_samples_leaf")
tree_handler.cross_me(*range(1, 10))
tree_handler.plot()
show()

""" OLD
# min_impurity_split
# min_impurity_split is depracated so lets disable warnings
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

tree_handler.set_method("min_impurity_split")
tree_handler.cross_me(*np.arange(0.0, 5e-3, 1e-4))
tree_handler.plot()
show()
"""

# min_impurity_decrease

tree_handler.set_method("min_impurity_decrease")
tree_handler.cross_me(*np.arange(0.0, 5e-4, 1e-5))
tree_handler.plot()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Bias-Variance trade-off

# fake bias, variance and noise
complexity = np.arange(1, 2, 0.1)
variance = np.power(complexity, 5)
bias2 = variance[::-1]
irreducible = [10 * np.random.normal(abs(x - 1.5), 0.01) for x in complexity]

# total error = variance + bias^2 + irreducible
total = variance + bias2 + irreducible

plt.xticks([])
plt.yticks([])

plt.xlabel("Algorithm complexity")
plt.ylabel("Error")

plt.plot(complexity, variance, "C0o-", label="Variance")
plt.plot(complexity, bias2, "C1o-", label="Bias^2")
plt.plot(
    complexity, total, "C2o-", label="Total = Bias^2 + Variance + Irreducible error"
)

plt.plot([1.5, 1.5], [0, 25], "C3--")

plt.text(1.0, 7, "$\longleftarrow$ better chance of generalizing", color="C0")
plt.text(1.6, 7, "better chance of approximating $\longrightarrow$", color="C1")

plt.legend()
show()

# Quick math

# Example

from math import sin, cos, pi, exp


def get_dataset(N=20, sigma=0.1):
    """Generate N training samples"""
    # X is a set of random points from [-1, 1]
    X = 2 * np.random.sample(N) - 1
    # Y are corresponding target values (with noise included)
    Y = np.array([sin(pi * x) + np.random.normal(0, sigma) for x in X])

    return X, Y


# plot a sample
X, Y = get_dataset()

x_ = np.arange(-1, 1, 0.01)

plt.scatter(X, Y, color="C1")
plt.plot(x_, np.sin(np.pi * x_), "C0--")
show()

# generate 100 datasets with default settings
datasets = [get_dataset() for i in range(100)]

# and plot them all together with true signal
for i in range(100):
    plt.scatter(datasets[i][0], datasets[i][1], marker=".")

plt.plot(x_, np.sin(np.pi * x_), "C0--")
show()

# Now we need to fit each polynomial to each dataset separately


def get_fit(N, data):
    """Find a fit of polynomial of order N to data = (X, Y)"""
    return np.poly1d(np.polyfit(data[0], data[1], N))


# for the whole range of possible polynomials orders
# create a list of fits to different datasets
fits = [[get_fit(order, data) for data in datasets] for order in range(1, 10)]

plt.figure(figsize=(13, 10))

for order in range(1, 10):
    plt.subplot(3, 3, order)
    plt.ylim([-1.5, 1.5])

    for g in fits[order - 1]:
        plt.plot(x_, g(x_), "C1-", linewidth=0.1)

    plt.plot(x_, np.sin(np.pi * x_), "C0--")
    plt.title("Polynomial of order {}".format(order))

plt.tight_layout()
show()

# Training and test errors

# fake error
complexity = np.arange(0.1, 2, 0.1)
train_error = -np.log(complexity)
test_error = -np.log(complexity) + np.power(complexity, 1)

plt.xticks([])
plt.yticks([])

plt.xlabel("Algorithm complexity")
plt.ylabel("Error")

plt.plot(complexity, train_error, "C0o-", label="Training error")
plt.plot(complexity, test_error, "C1o-", label="Test error")

plt.text(0.1, 0.25, "$\longleftarrow$ high bias", color="C0")
plt.text(1.5, 0.25, "high variance $\longrightarrow$", color="C1")

plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Ensemble learning

# Random forest

# Intuitive / naive example

# Boosted trees

# AdaBoost

N = 500  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 8  # centers, 分群數
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, Y = make_blobs(n_samples=N, centers=GROUPS, random_state=9487)

plt.scatter(*X.T, c=Y, marker=".", cmap="Dark2")
show()

# Train and visualize


def train_and_look(classifier, X, Y, ax=None, title="", cmap="Dark2"):
    # Train classifier on (X,Y). Plot data and prediction.
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


# Let check how it works on a decision tree classifier with default sklearn setting

train_and_look(DecisionTreeClassifier(), X, Y)
show()

# Decision tree

# create a figure with 9 axes 3x3
fig, ax = plt.subplots(3, 3, figsize=(15, 15))

# train and look at decision trees with different max depth
for max_depth in range(0, 9):
    train_and_look(
        DecisionTreeClassifier(max_depth=max_depth + 1),
        X,
        Y,
        ax=ax[max_depth // 3][max_depth % 3],
        title="Max depth = {}".format(max_depth + 1),
    )
show()
"""
    max_depth <= 3 - undefitting
    max_depth <= 6 - quite good
    max_depth > 6 - overfitting
"""

# Random forest

# Lets do the same with random forests (100 trees in each forest)

from sklearn.ensemble import RandomForestClassifier as RF

# create a figure with 9 axes 3x3
fig, ax = plt.subplots(3, 3, figsize=(15, 15))

# train and look at decision trees with different max depth
for max_depth in range(0, 9):
    train_and_look(
        RF(n_estimators=100, max_depth=max_depth + 1),
        X,
        Y,
        ax=ax[max_depth // 3][max_depth % 3],
        title="Max depth = {}".format(max_depth + 1),
    )
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
决策树

决策树(decision tree)是一种基本的分类与回归方法。在处理分类问题中，其主要优点是模型具有可读性，分类速度快。

决策树模型定义：

分类决策树模型是一种描述对实例进行分类的树形结构。决策树又结点和有向边组成。结点类型包括：内部结点和叶结点。其中内部结点表示一个特征或属性，叶结点表示一个类。

决策树的学习通常包括3个步骤：
第一步：特征选择；
第二步：决策树的生成；
第三步：决策树的修剪。
常用的算法有ID3、 C4.5和CART。
特征选择

特征选择的目的在于选取对训练数据能够分类的特征，即特征选择是决定用哪个特征来划分特征空间。在实际场景中，特征的种类是多种多样的，选择不同的特征会决定产生不同的决策树。那究竟如何选择特征会更好？这里的关键就是确定选择特征的准则。信息增益(information gain)就是这样一种准则。
"""


# 构建数据
def create_data():
    datasets = [
        ["青年", "否", "否", "一般", "否"],
        ["青年", "否", "否", "好", "否"],
        ["青年", "是", "否", "好", "是"],
        ["青年", "是", "是", "一般", "是"],
        ["青年", "否", "否", "一般", "否"],
        ["中年", "否", "否", "一般", "否"],
        ["中年", "否", "否", "好", "否"],
        ["中年", "是", "是", "好", "是"],
        ["中年", "否", "是", "非常好", "是"],
        ["中年", "否", "是", "非常好", "是"],
        ["老年", "否", "是", "非常好", "是"],
        ["老年", "否", "是", "好", "是"],
        ["老年", "是", "否", "好", "是"],
        ["老年", "是", "否", "非常好", "是"],
        ["老年", "否", "否", "一般", "否"],
    ]
    labels = ["年龄", "有工作", "有自己的房子", "信贷情况", "类别"]
    # 返回数据集和每个维度的名称
    return datasets, labels


# 获取数据集和标签集
datasets, labels = create_data()
train_data = pd.DataFrame(datasets, columns=labels)
cc = train_data
print(cc)

# 定义熵、经验条件熵、信息增益等

print(labels)


# 熵
def calc_ent(datasets):
    data_length = len(datasets)
    label_count = {}
    for i in range(data_length):
        label = datasets[i][-1]
        if label not in label_count:
            label_count[label] = 0
        label_count[label] += 1
    ent = -sum(
        [(p / data_length) * math.log(p / data_length, 2) for p in label_count.values()]
    )
    return ent


# 经验条件熵
def cond_ent(datasets, axis=0):
    data_length = len(datasets)
    feature_sets = {}
    for i in range(data_length):
        feature = datasets[i][axis]
        if feature not in feature_sets:
            feature_sets[feature] = []
        feature_sets[feature].append(datasets[i])
    cond_ent = sum(
        [(len(p) / data_length) * calc_ent(p) for p in feature_sets.values()]
    )
    return cond_ent


# 信息增益
def info_gain(ent, cond_ent):
    return ent - cond_ent


def info_gain_train(datasets):
    count = len(datasets[0]) - 1
    ent = calc_ent(datasets)
    best_feature = []
    for i in range(count):
        i_info_gain = info_gain(ent, cond_ent(datasets, axis=i))
        best_feature.append((i, i_info_gain))
        print("特征-({}) - info_gain - {:.3f}".format(labels[i], i_info_gain))
    # 比较大小
    best_ = max(best_feature, key=lambda x: x[-1])
    return "特征-({})的信息增益最大，选择为根节点特征".format(labels[best_[0]])


info_gain_train(np.array(datasets))

"""
特征-(年龄) - info_gain - 0.083
特征-(有工作) - info_gain - 0.324
特征-(有自己的房子) - info_gain - 0.420
特征-(信贷情况) - info_gain - 0.363

'特征-(有自己的房子)的信息增益最大，选择为根节点特征'
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 决策树的生成, 常见的算法有ID3、C4.5

# 決策樹的生成 之一 ID3算法
# ID3算法的具体操作为：从根结点开始，对结点计算所有可能的特征信息增益，然后选择信息增益最大的特征作为结点特征，由该特征的不同取值建立子结点；再对子结点递归调用以上方法，构建决策树；知道所有特征的信息增益均很小或者没有特征可以选择为止。最后生成一个决策树。


# ID3算法
def recurse_train_ID3(train_set, train_label, features):
    LEAF = "leaf"
    INTERNAL = "internal"

    # 步骤1—如果训练集train_set中的所有实例都属于同一类Ck
    label_set = set(train_label)
    if len(label_set) == 1:
        return Tree(LEAF, Class=label_set.pop())

    # 步骤2—如果特征集features为空
    class_len = [
        (i, len(list(filter(lambda x: x == i, train_label)))) for i in range(class_num)
    ]  # 计算每一个类出现的个数
    (max_class, max_len) = max(class_len, key=lambda x: x[1])

    if len(features) == 0:
        return Tree(LEAF, Class=max_class)

    # 步骤3—计算信息增益,并选择信息增益最大的特征
    max_feature = 0
    max_gda = 0
    D = train_label
    for feature in features:
        # print(type(train_set))
        A = np.array(train_set[:, feature].flat)  # 选择训练集中的第feature列（即第feature个特征）
        gda = calc_ent_grap(A, D)
        if gda > max_gda:
            max_gda, max_feature = gda, feature

    # 步骤4—信息增益小于阈值
    if max_gda < epsilon:
        return Tree(LEAF, Class=max_class)

    # 步骤5—构建非空子集
    sub_features = list(filter(lambda x: x != max_feature, features))
    tree = Tree(INTERNAL, feature=max_feature)

    max_feature_col = np.array(train_set[:, max_feature].flat)
    feature_value_list = set(
        [max_feature_col[i] for i in range(max_feature_col.shape[0])]
    )  # 保存信息增益最大的特征可能的取值 (shape[0]表示计算行数)
    for feature_value in feature_value_list:
        index = []
        for i in range(len(train_label)):
            if train_set[i][max_feature] == feature_value:
                index.append(i)

        sub_train_set = train_set[index]
        sub_train_label = train_label[index]

        sub_tree = recurse_train_ID3(sub_train_set, sub_train_label, sub_features)
        tree.add_tree(feature_value, sub_tree)

    return tree


# 定义经验熵、条件熵、信息增益等


# 计算数据集x的经验熵H(x)
def calc_ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        logp = np.log2(p)
        ent -= p * logp

    return ent


# 计算条件熵H(y/x)
def calc_condition_ent(x, y):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        sub_y = y[x == x_value]
        temp_ent = calc_ent(sub_y)
        ent += (float(sub_y.shape[0]) / y.shape[0]) * temp_ent

    return ent


# 计算信息增益
def calc_ent_grap(x, y):
    base_ent = calc_ent(y)
    condition_ent = calc_condition_ent(x, y)
    ent_grap = base_ent - condition_ent

    return ent_grap


import cv2

# 定义树结构


class Tree(object):
    def __init__(self, node_type, Class=None, feature=None):
        self.node_type = node_type  # 节点类型（internal或leaf）
        self.dict = {}  # dict的键表示特征Ag的可能值ai，值表示根据ai得到的子树
        self.Class = Class  # 叶节点表示的类，若是内部节点则为none
        self.feature = feature  # 表示当前的树即将由第feature个特征划分（即第feature特征是使得当前树中信息增益最大的特征）

    def add_tree(self, key, tree):
        self.dict[key] = tree

    def predict(self, features):
        if self.node_type == "leaf" or (features[self.feature] not in self.dict):
            return self.Class

        tree = self.dict.get(features[self.feature])
        return tree.predict(features)


# 图像处理需要用到二值化


# 二值化
def binaryzation(img):
    cv_img = img.astype(np.uint8)
    cv2.threshold(cv_img, 50, 1, cv2.THRESH_BINARY_INV, cv_img)
    return cv_img


def binaryzation_features(trainset):
    features = []

    for img in trainset:
        img = np.reshape(img, (28, 28))
        cv_img = img.astype(np.uint8)

        img_b = binaryzation(cv_img)
        # hog_feature = np.transpose(hog_feature)
        features.append(img_b)

    features = np.array(features)
    features = np.reshape(features, (-1, feature_len))

    return features


# 训练
def train(train_set, train_label, features):
    return recurse_train_ID3(train_set, train_label, features)


def predict(test_set, tree):
    result = []
    for features in test_set:
        tmp_predict = tree.predict(features)
        result.append(tmp_predict)
    return np.array(result)


# 训练测试

import cv2

"""
本测试采用MNIST图像数据集
说明：
mnist数据集有10个类别，分别为0,1,2,3,4,5,6,7,8,9
因此用变量class_num=10表示类别数

mnist数据中的image的shape为(28,28)，即每个image的特征数为28*28=784
所有设置feature_len=784

本实验的训练数据为lihang-dl-train.csv,文件的数据是mnist image数据

"""
class_num = 10
feature_len = 784
epsilon = 0.001  # 设定阈值

print("读取数据")

time_1 = time.time()

raw_data = pd.read_csv("D:/_git/vcs/_big_files/lihang-dl-train.csv", header=0)
data = raw_data.values

imgs = data[::, 1::]
features = binaryzation_features(imgs)  # 图片二值化(很重要，不然预测准确率很低)
labels = data[::, 0]

# 避免过拟合，采用交叉验证，随机选取20%数据作为测试集，剩余为训练集
# 資料分割
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2
)

time1 = time.time()

# 通过ID3算法生成决策树
print("开始训练")
tree = train(train_features, train_labels, list(range(feature_len)))
time2 = time.time()
print("训练花费时间: %f seconds" % (time2 - time1))

print("开始预测")
test_predict = predict(test_features, tree)
time3 = time.time()
print("预测花费时间 %f seconds" % (time3 - time2))

for i in range(len(test_predict)):
    if test_predict[i] == None:
        test_predict[i] = epsilon
score = accuracy_score(test_labels, test_predict)
print("精度为 %f" % score)
"""
读取数据
开始训练
训练花费时间: 317.695612 seconds
开始预测
预测花费时间 0.147270 seconds
精度为 0.861833
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 決策樹的生成 之二 C4.5算法

# C4.5算法是基于ID3算法的改进，C4.5在生成的过程中使用信息增益比来选择特征。


def recurse_train_C45(train_set, train_label, features):
    LEAF = "leaf"
    INTERNAL = "internal"

    # 步骤1—如果训练集train_set中的所有实例都属于同一类Ck
    label_set = set(train_label)
    if len(label_set) == 1:
        return Tree(LEAF, Class=label_set.pop())

    # 步骤2—如果特征集features为空
    class_len = [
        (i, len(list(filter(lambda x: x == i, train_label)))) for i in range(class_num)
    ]  # 计算每一个类出现的个数
    (max_class, max_len) = max(class_len, key=lambda x: x[1])

    if len(features) == 0:
        return Tree(LEAF, Class=max_class)

    # 步骤3—计算信息增益,并选择信息增益最大的特征
    max_feature = 0
    max_gda = 0
    D = train_label
    for feature in features:
        # print(type(train_set))
        A = np.array(train_set[:, feature].flat)  # 选择训练集中的第feature列（即第feature个特征）
        gda = calc_ent_grap(A, D)
        if calc_ent(A) != 0:  # 计算信息增益比，这是与ID3算法唯一的不同
            gda /= calc_ent(A)
        if gda > max_gda:
            max_gda, max_feature = gda, feature

    # 步骤4—信息增益小于阈值
    if max_gda < epsilon:
        return Tree(LEAF, Class=max_class)

    # 步骤5—构建非空子集
    sub_features = list(filter(lambda x: x != max_feature, features))
    tree = Tree(INTERNAL, feature=max_feature)

    max_feature_col = np.array(train_set[:, max_feature].flat)
    # 保存信息增益最大的特征可能的取值 (shape[0]表示计算行数)
    feature_value_list = set(
        [max_feature_col[i] for i in range(max_feature_col.shape[0])]
    )
    for feature_value in feature_value_list:
        index = []
        for i in range(len(train_label)):
            if train_set[i][max_feature] == feature_value:
                index.append(i)

        sub_train_set = train_set[index]
        sub_train_label = train_label[index]

        sub_tree = recurse_train_C45(sub_train_set, sub_train_label, sub_features)
        tree.add_tree(feature_value, sub_tree)

    return tree


# 定义经验熵、条件熵、信息增益等


# 计算数据集x的经验熵H(x)
def calc_ent(x):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        p = float(x[x == x_value].shape[0]) / x.shape[0]
        logp = np.log2(p)
        ent -= p * logp

    return ent


# 计算条件熵H(y/x)
def calc_condition_ent(x, y):
    x_value_list = set([x[i] for i in range(x.shape[0])])
    ent = 0.0
    for x_value in x_value_list:
        sub_y = y[x == x_value]
        temp_ent = calc_ent(sub_y)
        ent += (float(sub_y.shape[0]) / y.shape[0]) * temp_ent

    return ent


# 计算信息增益
def calc_ent_grap(x, y):
    base_ent = calc_ent(y)
    condition_ent = calc_condition_ent(x, y)
    ent_grap = base_ent - condition_ent

    return ent_grap


# 训练


import cv2


# 定义树结构
class Tree(object):
    def __init__(self, node_type, Class=None, feature=None):
        self.node_type = node_type  # 节点类型（internal或leaf）
        self.dict = {}  # dict的键表示特征Ag的可能值ai，值表示根据ai得到的子树
        self.Class = Class  # 叶节点表示的类，若是内部节点则为none
        self.feature = feature  # 表示当前的树即将由第feature个特征划分（即第feature特征是使得当前树中信息增益最大的特征）

    def add_tree(self, key, tree):
        self.dict[key] = tree

    def predict(self, features):
        if self.node_type == "leaf" or (features[self.feature] not in self.dict):
            return self.Class

        tree = self.dict.get(features[self.feature])
        return tree.predict(features)


# 图像处理需要用到二值化


# 二值化
def binaryzation(img):
    cv_img = img.astype(np.uint8)
    cv2.threshold(cv_img, 50, 1, cv2.THRESH_BINARY_INV, cv_img)
    return cv_img


def binaryzation_features(trainset):
    features = []

    for img in trainset:
        img = np.reshape(img, (28, 28))
        cv_img = img.astype(np.uint8)

        img_b = binaryzation(cv_img)
        # hog_feature = np.transpose(hog_feature)
        features.append(img_b)

    features = np.array(features)
    features = np.reshape(features, (-1, feature_len))

    return features


def train(train_set, train_label, features):
    return recurse_train_C45(train_set, train_label, features)


def predict(test_set, tree):
    result = []
    for features in test_set:
        tmp_predict = tree.predict(features)
        result.append(tmp_predict)
    return np.array(result)


# 训练测试

import cv2

class_num = 10
feature_len = 784
epsilon = 0.001  # 设定阈值

print("读取数据")

raw_data = pd.read_csv("D:/_git/vcs/_big_files/lihang-dl-train.csv", header=0)
data = raw_data.values

imgs = data[::, 1::]
features = binaryzation_features(imgs)  # 图片二值化(很重要，不然预测准确率很低)
labels = data[::, 0]

# 避免过拟合，采用交叉验证，随机选取20%数据作为测试集，剩余为训练集
# 資料分割
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0.2
)

# 通过C4.5算法生成决策树
print("开始训练")
time1 = time.time()
tree = train(train_features, train_labels, list(range(feature_len)))
time2 = time.time()
print("训练花费时间： %f seconds" % (time2 - time1))

print("开始预测")
test_predict = predict(test_features, tree)
time3 = time.time()
print("预测花费时间 %f seconds" % (time3 - time2))

# 预测精度
for i in range(len(test_predict)):
    if test_predict[i] == None:
        test_predict[i] = epsilon
score = accuracy_score(test_labels, test_predict)
print("精度为： %f" % score)

"""
读取数据
开始训练
训练花费时间： 1861.676888 seconds
开始预测
预测花费时间 0.972255 seconds
精度为： 0.842424
"""

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

# 迴歸樹

# 生成隨機資料
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))  # 加上雜訊

plt.plot(X, y)
plt.title("原始資料")
show()

# 訓練兩個迴歸樹模型 最大深度不同
clf_1 = DecisionTreeRegressor(max_depth=2)  # 迴歸樹函數學習機
clf_1.fit(X, y)  # 學習訓練.fit

clf_2 = DecisionTreeRegressor(max_depth=5)  # 迴歸樹函數學習機
clf_2.fit(X, y)  # 學習訓練.fit

# 預測
# 測試資料 500點
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]

y_pred_1 = clf_1.predict(X_test)  # 預測.predict
y_pred_2 = clf_2.predict(X_test)  # 預測.predict

# 模型繪圖
plt.scatter(X, y, s=20, edgecolor="r", c="darkorange", label="真實資料")
plt.plot(X_test, y_pred_1, color="g", label="最大深度=2", linewidth=2)
plt.plot(X_test, y_pred_2, color="b", label="最大深度=5", linewidth=2)
plt.title("迴歸樹")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 自行計算 Shapley value

"""
housing.data 506筆資料 14欄位
純文字 無檔頭 需讀出來分割處理
 0.00632  18.00   2.310  0  0.5380  6.5750  65.20  4.0900   1  296.0  15.30 396.90   4.98  24.00
 0.02731   0.00   7.070  0  0.4690  6.4210  78.90  4.9671   2  242.0  17.80 396.90   9.14  21.60
 0.02729   0.00   7.070  0  0.4690  7.1850  61.10  4.9671   2  242.0  17.80 392.83   4.03  34.70
 0.03237   0.00   2.180  0  0.4580  6.9980  45.80  6.0622   3  222.0  18.70 394.63   2.94  33.40
 0.06905   0.00   2.180  0  0.4580  7.1470  54.20  6.0622   3  222.0  18.70 396.90   5.33  36.20
 0.02985   0.00   2.180  0  0.4580  6.4300  58.70  6.0622   3  222.0  18.70 394.12   5.21  28.70
"""

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print("前5筆資料 :\n", cc, sep="")

# 資料 取出4欄位
X = df[["RM", "LSTAT", "DIS", "NOX"]]

# 目標 取出 MEDV 欄位
y = df["MEDV"]

clf = DecisionTreeRegressor(max_depth=3)  # 迴歸樹函數學習機

clf.fit(X, y)  # 學習訓練.fit

plt.figure(figsize=(14, 5))
plot_tree(clf, feature_names=X.columns)  # 繪製樹狀圖
plt.title("迴歸樹, 用plot_tree畫圖")

show()

print("\n以 SHAP 套件計算 Shapley value")

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(X[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": X[:1].values.squeeze(),
            },
            index=X.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("Shapley value + Y平均數 = 預測值")
cc = shap_values.sum() + y.mean(), clf.predict(X[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

print("\n自行計算 Shapley value")

from itertools import combinations


# 計算特定組合的邊際貢獻
def pred_tree(clf, coalition, row, node=0):
    left_node = clf.tree_.children_left[node]
    right_node = clf.tree_.children_right[node]
    is_leaf = left_node == right_node

    if is_leaf:
        return clf.tree_.value[node].squeeze()

    feature = row.index[clf.tree_.feature[node]]
    if feature in coalition:
        if row.loc[feature] <= clf.tree_.threshold[node]:
            # go left
            return pred_tree(clf, coalition, row, node=left_node)
        else:  # go right
            return pred_tree(clf, coalition, row, node=right_node)

    # take weighted average of left and right
    wl = clf.tree_.n_node_samples[left_node] / clf.tree_.n_node_samples[node]
    wr = clf.tree_.n_node_samples[right_node] / clf.tree_.n_node_samples[node]
    value = wl * pred_tree(clf, coalition, row, node=left_node)
    value += wr * pred_tree(clf, coalition, row, node=right_node)
    return value


# 計算特定組合的平均邊際貢獻
def make_value_function(clf, row, col):
    def value(c):
        marginal_gain = pred_tree(clf, c + [col], row) - pred_tree(clf, c, row)
        num_coalitions = scipy.special.comb(len(row) - 1, len(c))
        return marginal_gain / num_coalitions

    return value


# 各種組合
def make_coalitions(row, col):
    rest = [x for x in row.index if x != col]
    for i in range(len(rest) + 1):
        for x in combinations(rest, i):
            yield list(x)


# 計算 Shapley value
def compute_shap(clf, row, col):
    v = make_value_function(clf, row, col)
    return sum([v(coal) / len(row) for coal in make_coalitions(row, col)])


# 顯示 Shapley value
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "my_shap": [compute_shap(clf, X[:1].T.squeeze(), x) for x in X.columns],
                "feature_value": X[:1].values.squeeze(),
            },
            index=X.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 自行開發決策樹
# 計算熵(entropy)


# 熵公式
def entropy_func(c, n):
    return -(c * 1.0 / n) * math.log(c * 1.0 / n, 2)
    # gini
    # return 1-(c*1.0/n)**2    # 或者


# 依特徵值切割成兩類，分別計算熵，再加總
# 計算同一節點內的熵，只有兩個類別
def entropy_cal(c1, c2):
    if c1 == 0 or c2 == 0:
        return 0
    return entropy_func(c1, c1 + c2) + entropy_func(c2, c1 + c2)


# 視每個特徵都是類別變數，依每個類別切割，分別計算熵
# 計算同一節點內的熵，多個類別
def entropy_of_one_division(division):
    s = 0
    n = len(division)
    classes = set(division)
    # 計算每一類別的熵，再加總
    for c in classes:
        n_c = sum(division == c)
        e = n_c * 1.0 / n * entropy_cal(sum(division == c), sum(division != c))
        s += e
    return s, n


# 依分割條件計算熵
def get_entropy(y_predict, y_real):
    if len(y_predict) != len(y_real):
        print("They have to be the same length")
        return None
    n = len(y_real)
    # 左節點
    s_true, n_true = entropy_of_one_division(y_real[y_predict])
    # 右節點
    s_false, n_false = entropy_of_one_division(y_real[~y_predict])
    # 左、右節點加權總和
    s = n_true * 1.0 / n * s_true + n_false * 1.0 / n * s_false
    return s


# 決策樹演算法類別


class my_DecisionTreeClassifier(object):
    def __init__(self, max_depth=3):
        self.depth = 0
        self.max_depth = max_depth

    # 訓練
    def fit(self, x, y, par_node={}, depth=0):
        if par_node is None:
            return None
        elif len(y) == 0:
            return None
        elif self.all_same(y):
            return {"val": float(y[0])}
        elif depth >= self.max_depth:
            return None
        else:
            # 計算資訊增益
            col, cutoff, entropy = self.find_best_split_of_all(x, y)
            if cutoff is not None:
                y_left = y[x[:, col] < cutoff]
                y_right = y[x[:, col] >= cutoff]
                par_node = {
                    "col": feature_names[col],
                    "index_col": int(col),
                    "cutoff": float(cutoff),
                    "val": float(np.round(np.mean(y))),
                }
                par_node["left"] = self.fit(
                    x[x[:, col] < cutoff], y_left, {}, depth + 1
                )
                par_node["right"] = self.fit(
                    x[x[:, col] >= cutoff], y_right, {}, depth + 1
                )
                self.depth += 1
            self.trees = par_node
            return par_node

    # 比較所有特徵找到最佳切割條件
    def find_best_split_of_all(self, x, y):
        col = None
        min_entropy = 1
        cutoff = None
        for i, c in enumerate(x.T):
            entropy, cur_cutoff = self.find_best_split(c, y)
            if entropy == 0:  # 找到最佳切割條件
                return i, cur_cutoff, entropy
            elif entropy <= min_entropy:
                min_entropy = entropy
                col = i
                cutoff = cur_cutoff
        return col, cutoff, min_entropy

    # 根據一個特徵找到最佳切割條件
    def find_best_split(self, col, y):
        min_entropy = 10
        n = len(y)
        for value in set(col):
            y_predict = col < value
            my_entropy = get_entropy(y_predict, y)
            if my_entropy <= min_entropy:
                min_entropy = my_entropy
                cutoff = value
        return min_entropy, cutoff

    # 檢查是否節點中所有樣本均屬同一類
    def all_same(self, items):
        return all(x == items[0] for x in items)

    # 預測
    def predict(self, x):
        tree = self.trees
        results = np.array([0] * len(x))
        for i, c in enumerate(x):
            try:
                results[i] = self._get_prediction(c)
            except:
                pass
        return results

    # 預測一筆
    def _get_prediction(self, row):
        cur_layer = self.trees
        while cur_layer is not None and cur_layer.get("cutoff"):
            if row[cur_layer["index_col"]] < cur_layer["cutoff"]:
                cur_layer = cur_layer["left"]
            else:
                cur_layer = cur_layer["right"]
        else:
            return cur_layer.get("val") if cur_layer is not None else None


wine = datasets.load_wine()

feature_names = wine.feature_names
X, y = wine.data, wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = my_DecisionTreeClassifier()

output = clf.fit(X_train, y_train)  # 學習訓練.fit

print(json.dumps(output, indent=4))

# 計算準確率
y_pred = clf.predict(X_test)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")
# 30.56%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("決策樹")

wine = datasets.load_wine()

feature_names = wine.feature_names
X, y = wine.data, wine.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()  # criterion='entropy'   # 決策樹函數學習機

clf.fit(X_train, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = clf.predict(X_test)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

plt.figure(figsize=(14, 5))
plot_tree(clf, feature_names=feature_names)  # 繪製樹狀圖
plt.title("迴歸樹, 用plot_tree畫圖")

show()

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

# 決策樹可視化存檔
dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=wine.target_names,
    feature_names=wine.feature_names,
    out_file=None,
)

graph = graph_from_dot_data(dot_data)
# graph.write_png('tmp_wine_tree.png')  NG

# 決策樹可視化存檔
dot_data = export_graphviz(
    clf,
    filled=True,
    rounded=True,
    class_names=wine.target_names,
    feature_names=wine.feature_names,
    out_file="tmp_wine_tree.dot",
)

# 取得樹狀圖的相關資訊

n_nodes = clf.tree_.node_count
children_left = clf.tree_.children_left
children_right = clf.tree_.children_right
feature = clf.tree_.feature
threshold = clf.tree_.threshold

node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
is_leaves = np.zeros(shape=n_nodes, dtype=bool)
stack = [(0, -1)]  # seed is the root node id and its parent depth
while len(stack) > 0:
    node_id, parent_depth = stack.pop()
    node_depth[node_id] = parent_depth + 1

    # If we have a test node
    if children_left[node_id] != children_right[node_id]:
        stack.append((children_left[node_id], parent_depth + 1))
        stack.append((children_right[node_id], parent_depth + 1))
    else:
        is_leaves[node_id] = True

print(f"樹狀圖共有{n_nodes}個節點:")
for i in range(n_nodes):
    depth = node_depth[i] * "\t"
    if is_leaves[i]:
        print(f"{depth}node={i} leaf node.")
    else:
        print(
            f"{depth}node={i} child node: go to node {children_left[i]} if X[:, "
            + f"{feature[i]}] <= {threshold[i]} else to node {children_right[i]}."
        )
print()

node_indicator = clf.decision_path(X)
leave_id = clf.apply(X)
sample_id = 0
node_index = node_indicator.indices[
    node_indicator.indptr[sample_id] : node_indicator.indptr[sample_id + 1]
]

print(f"Rules used to predict sample {sample_id}: ")
for node_id in node_index:
    if leave_id[sample_id] == node_id:
        continue

    if X[sample_id, feature[node_id]] <= threshold[node_id]:
        threshold_sign = "<="
    else:
        threshold_sign = ">"

    print(
        "decision id node {} : (X[{}, {}] (= {}) {} {})".format(
            node_id,
            sample_id,
            feature[node_id],
            X[sample_id, feature[node_id]],
            threshold_sign,
            threshold[node_id],
        )
    )

# For a group of samples, we have the following common node.
sample_ids = [0, 1]
common_nodes = node_indicator.toarray()[sample_ids].sum(axis=0) == len(sample_ids)

common_node_id = np.arange(n_nodes)[common_nodes]

print(
    "\nThe following samples %s share the node %s in the tree"
    % (sample_ids, common_node_id)
)
print("It is %s %% of all nodes." % (100 * len(common_node_id) / n_nodes,))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


def get_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))


def print_error_rate(err):
    print("Error rate: Training: %.4f - Test: %.4f" % err)


def generic_clf(Y_train, X_train, Y_test, X_test, clf):
    clf.fit(X_train, Y_train)
    pred_train = clf.predict(X_train)
    pred_test = clf.predict(X_test)
    return get_error_rate(pred_train, Y_train), get_error_rate(pred_test, Y_test)


# ADABOOST


def adaboost_clf(Y_train, X_train, Y_test, X_test, M, clf):
    n_train, n_test = len(X_train), len(X_test)
    # Initialize weights
    w = np.ones(n_train) / n_train
    pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

    for i in range(M):
        # Fit a classifier with the specific weights
        clf.fit(X_train, Y_train, sample_weight=w)
        pred_train_i = clf.predict(X_train)
        pred_test_i = clf.predict(X_test)
        # Indicator function
        miss = [int(x) for x in (pred_train_i != Y_train)]
        # Equivalent with 1/-1 to update weights
        miss2 = [x if x == 1 else -1 for x in miss]
        # Error
        err_m = np.dot(w, miss) / sum(w)
        # Alpha
        alpha_m = 0.5 * np.log((1 - err_m) / float(err_m))
        # New weights
        w = np.multiply(w, np.exp([float(x) * alpha_m for x in miss2]))
        # Add to prediction
        pred_train = [
            sum(x) for x in zip(pred_train, [x * alpha_m for x in pred_train_i])
        ]
        pred_test = [sum(x) for x in zip(pred_test, [x * alpha_m for x in pred_test_i])]

    pred_train, pred_test = np.sign(pred_train), np.sign(pred_test)
    # Return error rate in train and test set
    return get_error_rate(pred_train, Y_train), get_error_rate(pred_test, Y_test)


def plot_error_rate(er_train, er_test):
    df_error = pd.DataFrame([er_train, er_test]).T
    df_error.columns = ["Training", "Test"]
    plot1 = df_error.plot(
        linewidth=3, figsize=(8, 6), color=["lightblue", "darkblue"], grid=True
    )
    plot1.set_xlabel("Number of iterations")
    label_format = "{:,.0f}"
    plot1.set_xticklabels([label_format.format(x) for x in range(0, 450, 50)])
    plot1.set_ylabel("Error rate")
    plot1.set_title("Error rate vs number of iterations")
    plt.axhline(y=er_test[0], linewidth=1, color="red", ls="dashed")
    show()


# 主程式
print("aa")
# Read data
x, y = make_hastie_10_2()
print("bb")
df = pd.DataFrame(x)
df["Y"] = y

# 資料分割
train, test = train_test_split(df, test_size=0.2)

X_train, Y_train = train.iloc[:, :-1], train.iloc[:, -1]
X_test, Y_test = test.iloc[:, :-1], test.iloc[:, -1]

print("cc")

# Fit a simple decision tree first
clf_tree = DecisionTreeClassifier(max_depth=1, random_state=1)  # 決策樹函數學習機
er_tree = generic_clf(Y_train, X_train, Y_test, X_test, clf_tree)

print("dd")

# Fit Adaboost classifier using a decision tree as base estimator
# Test with different number of iterations
er_train, er_test = [er_tree[0]], [er_tree[1]]
x_range = range(10, 410, 50)
for i in x_range:
    print(i)
    er_i = adaboost_clf(Y_train, X_train, Y_test, X_test, i, clf_tree)
    er_train.append(er_i[0])
    er_test.append(er_i[1])

# Compare error rate vs number of iterations
plot_error_rate(er_train, er_test)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data = pd.read_excel("data/loan.xlsx")
target = data["Type"]
data.drop("Type", axis="columns", inplace=True)

# 資料分割
train_data, test_data, train_target, test_target = train_test_split(
    data, target, test_size=0.2
)

print("------------------------------")  # 30個

print("使用 DecisionTreeClassifier")
clf_1 = DecisionTreeClassifier(criterion="entropy")  # 決策樹函數學習機
clf_1.fit(train_data, train_target)
train_est = clf_1.predict(train_data)
train_est_p = clf_1.predict_proba(train_data)[:, 1]

test_est = clf_1.predict(test_data)
print(test_est)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

print("------------------------------")  # 30個

print("使用 SVC")
clf_2 = svm.SVC()
clf_2.fit(train_data, train_target)
train_est = clf_2.predict(train_data)
test_est = clf_2.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

print("------------------------------")  # 30個

print("使用 GaussianNB")

from sklearn.naive_bayes import GaussianNB

clf_3 = GaussianNB()
clf_3.fit(train_data, train_target)
train_est = clf_3.predict(train_data)
test_est = clf_3.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

print("------------------------------")  # 30個

print("使用 MLPClassifier")

from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機

clf_4 = MLPClassifier()  # 多層感知器分類器 函數學習機

clf_4.fit(train_data, train_target)

train_est = clf_4.predict(train_data)
test_est = clf_4.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# View more python learning tutorial on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.

This data set is from: http://archive.ics.uci.edu/ml/datasets/Bank+Marketing
Which is a real bank marketing data set. The required data are included in this example folder. You can download and
practice by yourself.

The 'bank-full.csv' data set has:
1) 17 inputs features (age, job, marital, education, default, balance, housing, loan,
   contact, day, month, duration, campaign, pdays, previous, poutcome);
2) 1 output (The answer yes or no to deposit to the bank); and
3) 45211 samples

We will use this data set for training and testing.
"""

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import ShuffleSplit
from sklearn import preprocessing


def feature_utility(data, selected_feature_name, target_name):
    target_classes = data[target_name].unique()
    feature_classes = data[selected_feature_name].unique()
    indices = np.arange(len(feature_classes))
    percentages = np.zeros((len(target_classes), len(feature_classes)))
    for j, feature_class in enumerate(feature_classes):
        particular_feature = data[selected_feature_name][
            data[selected_feature_name] == feature_class
        ]
        feature_total = len(particular_feature)
        for i, target_class in enumerate(target_classes):
            class_count = len(particular_feature[data[target_name] == target_class])
            percentage = class_count / feature_total
            percentages[i, j] = percentage

    colors = ["r", "b", "g"]
    width = 1
    bars = []
    for i in range(len(target_classes)):
        c_number = int(i % len(colors))
        color = colors[c_number]
        if i == 0:
            bar = plt.bar(indices, percentages[i, :], width, color=color)
        else:
            bar = plt.bar(
                indices,
                percentages[i, :],
                width,
                color=color,
                bottom=percentages[:i, :].sum(axis=0),
            )
        bars.append(bar)

    plt.xticks(indices + width / 2, feature_classes)
    plt.ylabel("Percentage")
    plt.xlabel(selected_feature_name)
    plt.legend([bar[0] for bar in bars], target_classes, loc="best")
    show()


def encode_label(data):
    la_en = preprocessing.LabelEncoder()
    for col in [
        "job",
        "marital",
        "education",
        "default",
        "housing",
        "loan",
        "contact",
        "month",
        "poutcome",
        "y",
    ]:
        data[col] = bank_data[col].astype("category")
        data[col] = la_en.fit_transform(bank_data[col])
    return data


dataset_path = ["data/bank.csv", "data/bank-full.csv"]
bank_data = pd.read_csv(dataset_path[1], sep=";")
print(bank_data.head())

# good categorical features: job, marital, education, housing, loan, contact, month, poutcome
# bad categorical features: default
# feature_utility(bank_data, 'housing', 'y')

bank_data = encode_label(bank_data)
# print(bank_data.dtypes)
# print(bank_data.head())

X_data, y_data = bank_data.iloc[:, :-1], bank_data.iloc[:, -1]
# show the percentage of answer yes and no.
answer_no, answer_yes = y_data.value_counts()
print("Percentage of answering no: ", answer_no / (answer_no + answer_yes))

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.2)

dt_clf = DecisionTreeClassifier(
    class_weight="balanced",
)  # 決策樹函數學習機
rf_clf = RandomForestClassifier(class_weight="balanced")

# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=9487)

print(cross_val_score(dt_clf, X_data, y_data, cv=cv, scoring="f1").mean())
print(cross_val_score(rf_clf, X_data, y_data, cv=cv, scoring="f1").mean())

# dt_clf.fit(X_train, y_train)
# print(dt_clf.score(X_test, y_test))
# rf_clf.fit(X_train, y_train)
# print(rf_clf.score(X_test, y_test))

# print(rf_clf.predict(X_test.iloc[10, :][np.newaxis, :]))
# print(y_test.iloc[10])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
决策树可视化（使用sklearn.tree 的export_graphviz方法）
可视化工具Graphviz

Graphviz 应用程序中有多种工具可以生成各种类型的图表（dot、neato、circo、twopi 等）。
本文将重点介绍用于生成层级图的 dot 工具。

dot渲染的图具有明确方向性。
neato渲染的图缺乏方向性。
twopi渲染的图采用放射性布局。
circo渲染的图采用环型布局。
fdp渲染的图缺乏方向性。
sfdp渲染大型的图，图片缺乏方向性。


graphviz强大而便捷的关系图/流程图绘制方法让我们联想到机器学习中的Decision Tree的展示方式。幸运的是，scikit-learn提供了生成.dot文件的接口，在python编辑环境操作如下：



"""

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_wine
from sklearn.tree import export_graphviz

import graphviz

# 加载数据集，将数据和类别区分呢
wine = load_wine()
X = wine.data
y = wine.target
# print(pd.DataFrame(X))
# print(pd.DataFrame(y))
print(wine.feature_names)

# 資料分割
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf.fit(xtrain, ytrain)

# 评估模型使用十次交叉验证
score = cross_val_score(clf, X, y, cv=10, scoring="accuracy")
print(np.mean(score))
print(clf.feature_importances_)

# 目前使用中文有問題
# feature_name = ['酒精','苹果酸','灰','灰的碱性','镁','总酚','类黄酮','非黄烷类酚类','花青素','颜色强度','色调','od280/od315稀释葡萄酒','脯氨酸']
# 決策樹可視化存檔
with open("tmp_wine3.dot", "w", encoding="utf-8") as f:
    # f = export_graphviz(clf, feature_names=feature_name, out_file=f)
    f = export_graphviz(clf, feature_names=wine.feature_names, out_file=f)

# 決策樹可視化存檔
export_graphviz(clf, out_file="tmp_wine4.dot", feature_names=wine.feature_names)

print("------------------------------------------------------------")  # 60個

from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn import metrics as ms
import graphviz

iris = datasets.load_iris()
X = iris.data  # 取出4欄資料
y = iris.target

x = X

########预处理#############
min_max_scaler = preprocessing.MinMaxScaler()
X_train = min_max_scaler.fit_transform(x)

n_components = 2  # 降維後的維度
pca = PCA(n_components=n_components)  # 保留的特征 PCA 降维
X_train = pca.fit_transform(X_train)

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X_train, y, test_size=0.2)

###############模型###########
dtc = DecisionTreeClassifier(criterion="entropy")  # 決策樹函數學習機
clf = dtc.fit(x_train, y_train)
# print(clf.predict(x_test))
# print(y_test)
print("精确率", ms.precision_score(y_test, clf.predict(x_test), average="micro"))

# 決策樹可視化存檔
dot_data = sklearn.tree.export_graphviz(clf, out_file="tmp_iris.dot")
print(dot_data)

""" 上述的 out_file="None" 才可以使用
graph = graphviz.Source(dot_data)
print(graph)

os.environ["PATH"] += os.pathsep + 'C:\\Users\\070601\\Desktop\\'
# NG graph.render("test", view=True)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Random Forest applied to LendingClub data set
"""
    credit.policy: 1 if the customer meets the credit underwriting criteria of LendingClub.com, and 0 otherwise.
    purpose: The purpose of the loan (takes values "credit_card", "debt_consolidation", "educational", "major_purchase", "small_business", and "all_other").
    int.rate: The interest rate of the loan, as a proportion (a rate of 11% would be stored as 0.11). Borrowers judged by LendingClub.com to be more risky are assigned higher interest rates.
    installment: The monthly installments owed by the borrower if the loan is funded.
    log.annual.inc: The natural log of the self-reported annual income of the borrower.
    dti: The debt-to-income ratio of the borrower (amount of debt divided by annual income).
    fico: The FICO credit score of the borrower.
    days.with.cr.line: The number of days the borrower has had a credit line.
    revol.bal: The borrower's revolving balance (amount unpaid at the end of the credit card billing cycle).
    revol.util: The borrower's revolving line utilization rate (the amount of the credit line used relative to total credit available).
    inq.last.6mths: The borrower's number of inquiries by creditors in the last 6 months.
    delinq.2yrs: The number of times the borrower had been 30+ days past due on a payment in the past 2 years.
    pub.rec: The borrower's number of derogatory public records (bankruptcy filings, tax liens, or judgments).
    not.fully.paid: The quantity of interest for classification - whether the borrower paid back the money in full or not
"""
df = pd.read_csv("data/loan_data.csv")

# Check out the info(), head(), and describe() methods on loans

# df.info()

# df.describe()

# df.head()

print(
    "Follwoing is a breakup of credit approval status. 1 means approved credit, 0 means not approved."
)
print(df["credit.policy"].value_counts())

# Exploratory Data Analysis

df[df["credit.policy"] == 1]["fico"].plot.hist(
    bins=30, alpha=0.5, color="blue", label="Credit.Policy=1"
)
df[df["credit.policy"] == 0]["fico"].plot.hist(
    bins=30, alpha=0.5, color="red", label="Credit.Policy=0"
)
plt.legend()
plt.title("Histogram of FICO score by approved or disapproved credit policies")
plt.xlabel("FICO score")
show()

# Presence or absence of statistical difference of various factors between credit approval status

sns.boxplot(x=df["credit.policy"], y=df["int.rate"])
plt.title("Interest rate varies between risky and non-risky borrowers")
plt.xlabel("Credit policy")
plt.ylabel("Interest rate")
show()

sns.boxplot(x=df["credit.policy"], y=df["log.annual.inc"])
plt.title("Income level does not make a big difference in credit approval odds")
plt.xlabel("Credit policy")
plt.ylabel("Log. annual income")
show()

sns.boxplot(x=df["credit.policy"], y=df["days.with.cr.line"])
plt.title("Credit-approved users have a slightly higher days with credit line")
plt.xlabel("Credit policy")
plt.ylabel("Days with credit line")
show()

sns.boxplot(x=df["credit.policy"], y=df["dti"])
plt.title("Debt-to-income level does not make a big difference in credit approval odds")
plt.xlabel("Credit policy")
plt.ylabel("Debt-to-income ratio")
show()

# Countplot of loans by purpose, with the color hue defined by not.fully.paid

plt.figure(figsize=(10, 6))
sns.countplot(x="purpose", hue="not.fully.paid", data=df, palette="Set1")
plt.title("Bar chart of loan purpose colored by not fully paid status")
plt.xlabel("Purpose")
show()

# Trend between FICO score and interest rate

sns.jointplot(x="fico", y="int.rate", data=df, color="purple", size=12)
show()

# lmplot to see if the trend differed between not.fully.paid and credit.policy

plt.figure(figsize=(14, 7))
sns.lmplot(
    y="int.rate",
    x="fico",
    data=df,
    hue="credit.policy",
    col="not.fully.paid",
    palette="Set1",
)
show()

# Setting up the Data
# Categorical Features

df_final = pd.get_dummies(df, ["purpose"], drop_first=True)

df_final.head()

# Train Test Split

X = df_final.drop("not.fully.paid", axis=1)
y = df_final["not.fully.paid"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# X.head()

# Training a Decision Tree Model

# Create an instance of DecisionTreeClassifier() called dtree and fit it to the training data.

dtree = DecisionTreeClassifier(criterion="gini", max_depth=None)  # 決策樹函數學習機

dtree.fit(X_train, y_train)

# Predictions and Evaluation of Decision Tree

# Create predictions from the test set and create a classification report and a confusion matrix.

predictions = dtree.predict(X_test)

from sklearn.metrics import classification_report, confusion_matrix

print(classification_report(y_test, predictions))

cm = confusion_matrix(y_test, predictions)
print(cm)
print("Accuracy of prediction:", round((cm[0, 0] + cm[1, 1]) / cm.sum(), 3))

# Training the Random Forest model

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(n_estimators=600)

rfc.fit(X_train, y_train)

# Predictions and Evaluation

rfc_pred = rfc.predict(X_test)

cr = classification_report(y_test, predictions)

print(cr)

# Show the Confusion Matrix for the predictions.

cm = confusion_matrix(y_test, rfc_pred)
print(cm)

# Running a loop with increasing number of trees in the random forest and checking accuracy of confusion matrix

# Criterion 'gini' or 'entropy'

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (criterion: 'gini')"
)
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="entropy"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (criterion: 'entropy')"
)
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

# Fixing max tree depth

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (max depth: None)"
)
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=10, max_depth=5, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title("Number of trees in the Random Forest vs. prediction accuracy (max depth: 5)")
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

# Minimum sample split criteria

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=2, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (minimum sample split: 2)"
)
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

nsimu = 21
accuracy = [0] * nsimu
ntree = [0] * nsimu
for i in range(1, nsimu):
    rfc = RandomForestClassifier(
        n_estimators=i * 5, min_samples_split=20, max_depth=None, criterion="gini"
    )
    rfc.fit(X_train, y_train)
    rfc_pred = rfc.predict(X_test)
    cm = confusion_matrix(y_test, rfc_pred)
    accuracy[i] = (cm[0, 0] + cm[1, 1]) / cm.sum()
    ntree[i] = i * 5

plt.figure(figsize=(10, 6))
plt.scatter(x=ntree[1:nsimu], y=accuracy[1:nsimu], s=60, c="red")
plt.title(
    "Number of trees in the Random Forest vs. prediction accuracy (minimum sample split: 20)"
)
plt.xlabel("Number of trees")
plt.ylabel("Prediction accuracy from confusion matrix")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Ensemble methods

train = pd.read_csv("data/imb_train.csv")
test = pd.read_csv("data/imb_test.csv")
cc = train.head()
print(cc)

count_classes = pd.value_counts(train["cls"], sort=True).sort_index()
count_classes.plot(kind="bar")
plt.show()

features_train = train.loc[:, "x1":"x2"]
labels_train = train["cls"]

features_test = test.loc[:, "x1":"x2"]
labels_test = test["cls"]

# 随机过采样

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=0)

os_features, os_labels = ros.fit_resample(features_train, labels_train)

cc = len(os_labels[os_labels == 1])
print(cc)

# 过采样SMOTE

from imblearn.over_sampling import SMOTE

oversampler = SMOTE(random_state=0)
""" NG
os_features, os_labels = oversampler.fit_resample(features_train, labels_train)

cc = len(os_labels[os_labels == 1])
print(cc)

# 综合采样

from imblearn.combine import SMOTETomek

smote_tomek = SMOTETomek(random_state=0)
os_features, os_labels = smote_tomek.fit_sample(features_train, labels_train)

# CART分类树

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(
    criterion="gini", max_depth=3, class_weight=None, random_state=1234
)  # 支持计算Entropy和GINI
clf.fit(os_features, os_labels)

import sklearn.metrics as metrics

print(metrics.classification_report(labels_test, clf.predict(features_test)))

train_est = clf.predict(features_train)
train_est_p = clf.predict_proba(features_train)[:, 1]
test_est = clf.predict(features_test)
test_est_p = clf.predict_proba(features_test)[:, 1]
fpr_test, tpr_test, th_test = metrics.roc_curve(labels_test, test_est_p)

fpr_train, tpr_train, th_train = metrics.roc_curve(labels_train, train_est_p)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
plt.show()

print(metrics.roc_auc_score(labels_test, test_est_p))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter16 Imbalance

import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("data/imb_train.csv")
test = pd.read_csv("data/imb_test.csv")
train.head()

""" NG
y_train = train["cls"]
X_train = train.ix[:, :"X5"]
y_test = test["cls"]
X_test = test.ix[:, :"X5"]

print("train_size: %s" % len(y_train), "test_size: %s" % len(y_test))

plt.figure(figsize=[3, 2])
count_classes = pd.value_counts(y_train, sort=True)
count_classes.plot(kind="bar")

plt.show()

# 1、采用抽样的方法

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek

ros = RandomOverSampler(random_state=0, ratio="auto")  # 随机过采样
sos = SMOTE(random_state=0)  # SMOTE过采样
kos = SMOTETomek(random_state=0)  # 综合采样

X_ros, y_ros = ros.fit_sample(X_train, y_train)
X_sos, y_sos = sos.fit_sample(X_train, y_train)
X_kos, y_kos = kos.fit_sample(X_train, y_train)

print("ros: %s, sos:%s, kos:%s" % (len(y_ros), len(y_sos), len(y_kos)))

y_ros.sum(), y_sos.sum(), y_kos.sum()

from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

clf = DecisionTreeClassifier(criterion="gini", random_state=1234)
param_grid = {"max_depth": [3, 4, 5, 6], "max_leaf_nodes": [4, 6, 8, 10, 12]}
cv = GridSearchCV(clf, param_grid=param_grid, scoring="f1")

data = [[X_train, y_train], [X_ros, y_ros], [X_sos, y_sos], [X_kos, y_kos]]

for features, labels in data:
    cv.fit(features, labels)
    predict_test = cv.predict(X_test)

    print(
        "auc:%.3f" % metrics.roc_auc_score(y_test, predict_test),
        "recall:%.3f" % metrics.recall_score(y_test, predict_test),
        "precision:%.3f" % metrics.precision_score(y_test, predict_test),
    )

# 2、采用改变样本权重的方法
param_grid2 = {
    "max_depth": [3, 4, 5, 6],
    "max_leaf_nodes": [4, 6, 8, 10, 12],
    "class_weight": [{0: 1, 1: 5}, {0: 1, 1: 10}, {0: 1, 1: 15}],
}

cv2 = GridSearchCV(clf, param_grid=param_grid2, scoring="f1")

cv2.fit(X_train, y_train)
predict_test2 = cv2.predict(X_test)

print(
    "auc:%.3f" % metrics.roc_auc_score(y_test, predict_test2),
    "recall:%.3f" % metrics.recall_score(y_test, predict_test2),
    "precision:%.3f" % metrics.precision_score(y_test, predict_test2),
)

cv2.best_params_

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM  # 二值型的RBM网络
from sklearn.model_selection import GridSearchCV
import sklearn.model_selection as cross_validation
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.metrics as metrics

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
cc = model_data.head()
print(cc)

target = model_data["BROADBAND"]
""" NG
orgData1 = model_data.ix[:, 1:-2]

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    orgData1, target, test_size=0.2
)

clf = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3, min_samples_split=5)
clf.fit(train_data, train_target)
test_est = clf.predict(test_data)
print("decision tree accuracy:")
print(metrics.classification_report(test_target, test_est))

gbc = ensemble.GradientBoostingClassifier()
gbc.fit(train_data, train_target)
test_est = gbc.predict(test_data)
print("gradient boosting accuracy:")
print(metrics.classification_report(test_target, test_est))

abc = ensemble.AdaBoostClassifier(n_estimators=100)
abc.fit(train_data, train_target)
test_est = abc.predict(test_data)
print("abc classifier accuracy:")
print(metrics.classification_report(test_target, test_est))

rfc = ensemble.RandomForestClassifier(
    criterion="entropy", n_estimators=3, max_features=0.5, min_samples_split=5
)
rfc.fit(train_data, train_target)
test_est = rfc.predict(test_data)
print("random forest accuracy:")
print(metrics.classification_report(test_target, test_est))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
cc = model_data.head()
print(cc)

target = model_data["BROADBAND"]
""" NG
orgData1 = model_data.ix[:, 1:-2]

train_data, test_data, train_target, test_target = train_test_split(
    orgData1, target, test_size=0.2
)

# 决策树算法
param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = tree.DecisionTreeClassifier()
clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(train_data, train_target)

test_est = clfcv.predict(test_data)
print("decision tree accuracy:")
print(metrics.classification_report(test_target, test_est))
print("decision tree AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est)
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 随机森林
param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [7, 8, 10, 12],
    "n_estimators": [11, 13, 15],  # 决策树个数-随机森林特有参数
    "max_features": [0.2, 0.3, 0.4, 0.5],  # 每棵决策树使用的变量占比-随机森林特有参数
    "min_samples_split": [4, 8, 12, 16],
}

rfc = ensemble.RandomForestClassifier()
rfccv = GridSearchCV(estimator=rfc, param_grid=param_grid, scoring="roc_auc", cv=4)
rfccv.fit(train_data, train_target)
test_est = rfccv.predict(test_data)
print("random forest accuracy:")
print(metrics.classification_report(test_target, test_est))
print("random forest AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est)
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

print(rfccv.best_params_)

# 由于一般缺乏对网格搜索参数的经验，建议把最优参数打印出来，看看取值是否在边届上
# 如果在边界上，就需要扩大搜索范围；
# 网格搜索需要有宽到细多进行几次。

# Adaboost算法
param_grid = {
    #'base_estimator':['DecisionTreeClassifier'],
    "learning_rate": [0.1, 0.3, 0.5, 0.7, 1]
}
abc = ensemble.AdaBoostClassifier(n_estimators=100, algorithm="SAMME")
abccv = GridSearchCV(estimator=abc, param_grid=param_grid, scoring="roc_auc", cv=4)
abccv.fit(train_data, train_target)
test_est = abccv.predict(test_data)
print("abc classifier accuracy:")
print(metrics.classification_report(test_target, test_est))
print("abc classifier AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est)
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

print(abccv.best_params_)

# GBDT
param_grid = {
    "loss": ["deviance", "exponential"],
    "learning_rate": [0.1, 0.3, 0.5, 0.7, 1],
    "n_estimators": [10, 15, 20, 30],  # 决策树个数-GBDT特有参数
    "max_depth": [1, 2, 3],  # 单棵树最大深度-GBDT特有参数
    "min_samples_split": [2, 4, 8, 12, 16, 20],
}

gbc = ensemble.GradientBoostingClassifier()
gbccv = GridSearchCV(estimator=gbc, param_grid=param_grid, scoring="roc_auc", cv=4)
gbccv.fit(train_data, train_target)
test_est = gbccv.predict(test_data)
print("gradient boosting accuracy:")
print(metrics.classification_report(test_target, test_est))
print("gradient boosting AUC:")
fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est)
print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

print(gbccv.best_params_)
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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("比較df是否相同")
cc = df.a.equals(df.b)
print(cc)


# plot
X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])

plt.plot(X[:3, 0], X[:3, 1], "rx", label="男生")
plt.plot(X[3:, 0], X[3:, 1], "g.", label="女生")
plt.plot([173], [76], "r^", label="預測點")  # 預測點
plt.ylabel("體重")
plt.xlabel("身高")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


X_combined = np.vstack((x_train, x_test))
y_combined = np.hstack((y_train, y_test))
