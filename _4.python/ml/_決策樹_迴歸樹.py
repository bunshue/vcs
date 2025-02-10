"""
機器學習_決策樹(Decision Tree)

機器學習_決策樹分類(Decision Tree Classifier)

機器學習_迴歸樹(Regression Tree)

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

from common1 import *


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

import scipy
import sklearn.linear_model
from sklearn import tree
from sklearn import metrics
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier  # 決策樹分類(Decision Tree Classifier)
from sklearn.tree import DecisionTreeRegressor  # 迴歸樹
from sklearn.tree import plot_tree
from matplotlib.colors import ListedColormap
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report  # 分類報告
from sklearn.metrics import roc_curve

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 資料一, 使用 make_blobs 資料
N = 30  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(n_samples=N, centers=GROUPS, n_features=M)

# 資料二, 使用 iris 資料
X, y = datasets.load_iris(return_X_y=True)

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf.fit(x_train, y_train)  # 學習訓練.fit

# 對測試數據做預測
y_pred = clf.predict(x_test)  # 預測.predict
print("預測結果 :", y_pred[:30])
print("測試目標 :", y_test[:30])

# 輸出準確性
print(f"訓練資料的準確性 = {clf.score(x_train, y_train)}")
print(f"測試資料的準確性 = {clf.score(x_test, y_test)}")
print(f"全部資料的準確性 = {clf.score(X, y)}")

scores = cross_val_score(clf, X, y, cv=5)
print("看一下5次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
y = np.array(["man", "man", "man", "woman", "woman", "woman"])

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf = clf.fit(X, y)  # 學習訓練.fit

# 存檔 sklearn.tree.export_graphviz(clf, out_file="tmp_tree1.dot")# 存檔

prediction = clf.predict([[173, 76]])  # 預測.predict
print(prediction)

plt.plot(X[:3, 0], X[:3, 1], "rx", label="男生")
plt.plot(X[3:, 0], X[3:, 1], "g.", label="女生")
plt.plot([173], [76], "r^", label="預測點")  # 預測點
plt.ylabel("體重")
plt.xlabel("身高")
plt.legend()

show()

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


def do_decision_tree():
    iris = datasets.load_iris()
    # 資料分割
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data[:, [2, 3]], iris.target, test_size=0.2
    )
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)  # 決策樹函數學習機

    clf.fit(x_train, y_train)  # 學習訓練.fit

    y_pred = clf.predict(x_test)  # 預測.predict

    X_combined = np.vstack((x_train, x_test))
    y_combined = np.hstack((y_train, y_test))

    plot_decision_regions(X_combined, y_combined, classifier=clf)
    plt.xlabel("petal length [cm]")
    plt.ylabel("petal width [cm]")
    plt.legend(loc="upper left")
    show()


print("決策樹")
do_decision_tree()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
AllElectronics.csv 14筆資料 5個欄位
age,income,student,credit_rating,buys_computer
1,3,0,1,0
1,3,0,2,0
2,3,0,1,1
3,2,0,1,1
3,1,1,1,1
3,1,1,2,0
2,1,1,2,1
1,2,0,1,0
1,1,1,1,1
3,2,1,1,1
1,2,1,2,1
2,2,0,2,1
2,3,1,1,1
3,2,0,2,0
"""

# DT_AllElectronics

# 決策樹

pd.set_option("display.max_columns", None)

data = pd.read_csv("data/AllElectronics.csv", skipinitialspace=True)
print(data.shape)
cc = data.head()
print("前5筆資料 :\n", cc, sep="")

# 目標 取出第5欄位 是否購買電腦
y = data["buys_computer"]

# 資料 age~credit_rating 共4欄位
X = data.loc[:, "age":"credit_rating"]
cc = X.head()
print("前5筆資料 :\n", cc, sep="")

# CART算法(分类树)
# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=9487,
)  # 決策樹函數學習機  # 当前支持计算信息增益和GINI

clf.fit(X, y)

# 存檔 sklearn.tree.export_graphviz(clf, out_file="tmp_cart2.dot")# 存檔

# 可以使用graphviz将树结构输出，在python中嵌入graphviz可参考：[pygraphviz](http://www.blogjava.net/huaoguo/archive/2012/12/21/393307.html)

# # 可视化
# 使用dot文件进行决策树可视化需要安装一些工具：
# - 第一步是安装graphviz。linux可以用apt-get或者yum的方法安装。如果是windows，就在官网下载msi文件安装。
#    无论是linux还是windows，装完后都要设置环境变量，将graphviz的bin目录加到PATH，
#    比如windows，将C:/Program Files (x86)/Graphviz2.38/bin/加入了PATH
# - 第二步是安装python插件graphviz： pip install graphviz
# - 第三步是安装python插件pydotplus: pip install pydotplus

import pydotplus
from IPython.display import Image  # 用IPython

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
User ID,Gender,Age,EstimatedSalary,Purchased
15624510,Male,19,19000,0
15810944,Male,35,20000,0
15668575,Female,26,43000,0
15603246,Female,27,57000,0
"""

df = pd.read_csv("data/Social_Network_Ads.csv")
# print(df) # 包含df之column與index
print("df之資料內容")
print(df.values)  # 不包含df之column與index 只有資料內容 400筆資料 5個欄位

X = df.iloc[:, [2, 3]].values  # 取出第3 4欄
y = df.iloc[:, 4].values  # 取出第5欄

print("X 第3 4欄 :(年齡 薪資)\n", X, sep="")
print("y 第5欄 :(是否購買)\n", y, sep="")

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Feature Scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)  # STD特徵縮放
X_test = scaler.transform(X_test)  # STD特徵縮放

# Fitting Decision Tree Classification to the Training set

clf = DecisionTreeClassifier(criterion="entropy", random_state=9487)  # 決策樹函數學習機

clf.fit(X_train, y_train)  # 學習訓練.fit

# Predicting the Test set results
y_pred = clf.predict(X_test)  # 預測.predict

# 混淆矩陣
cm = confusion_matrix(y_test, y_pred)
print("混淆矩陣 :\n", cm, sep="")

# Visualising the Training set results
X_set, y_set = X_train, y_train

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

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
plt.title("Decision Tree Classification (Training set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

# Visualising the Test set results
X_set, y_set = X_test, y_test

X1, X2 = np.meshgrid(
    np.arange(start=X_set[:, 0].min() - 1, stop=X_set[:, 0].max() + 1, step=0.01),
    np.arange(start=X_set[:, 1].min() - 1, stop=X_set[:, 1].max() + 1, step=0.01),
)

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
plt.title("Decision Tree Classification (Test set)")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Scikit-learn迴歸樹測試

# 生成隨機資料

rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))

# 訓練兩個模型

regr_1 = DecisionTreeRegressor(max_depth=2)
regr_1.fit(X, y)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_2.fit(X, y)

# DecisionTreeRegressor(max_depth=5)

# 預測

X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)  # 預測.predict
y_2 = regr_2.predict(X_test)  # 預測.predict

# 模型繪圖

plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.title("Decision Tree Regression 迴歸樹")
plt.xlabel("data")
plt.ylabel("target")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 自行計算 Shapley value

# 載入資料

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

# 模型訓練
y = df["MEDV"]
df = df[["RM", "LSTAT", "DIS", "NOX"]]

clf = DecisionTreeRegressor(max_depth=3)

clf.fit(df, y)  # 學習訓練.fit

fig = plt.figure(figsize=(20, 5))

ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)

plt.title("333")

show()

# 以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

# Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

# 自行計算 Shapley value

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
                "my_shap": [
                    compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns
                ],
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

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
