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
from sklearn import tree
from sklearn import metrics
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_hastie_10_2
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn.model_selection import GridSearchCV
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

# 資料一, 使用 make_blobs 資料
N = 30  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 3  # centers, 分群數
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")
X, y = make_blobs(n_samples=N, centers=GROUPS, n_features=M)

# 資料二, 使用 iris 資料
# X, y = datasets.load_iris(return_X_y=True) # same
iris = datasets.load_iris()
X = iris.data  # 取出4欄資料
y = iris.target

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf.fit(x_train, y_train)  # 學習訓練.fit

# 存檔 sklearn.tree.export_graphviz(clf, out_file="tmp_tree1.dot")# 存檔

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

X = iris.data[:, [2, 3]]  # 取出2欄資料
y = iris.target

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=3)  # 決策樹函數學習機

clf.fit(x_train, y_train)  # 學習訓練.fit

y_pred = clf.predict(x_test)  # 預測.predict

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
plt.show()

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

# 07_07_decision_tree_from_scratch

# 自行開發決策樹

# 計算熵(entropy)


# 熵公式
def entropy_func(c, n):
    return -(c * 1.0 / n) * math.log(c * 1.0 / n, 2)
    # gini
    # return 1-(c*1.0/n)**2


"""
# 熵公式
def entropy_func(c, n):
    # return -(c*1.0/n)*math.log(c*1.0/n, 2)
    # gini
    return 1 - (c * 1.0 / n) ** 2
"""


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

clf = DecisionTreeClassifier()  # criterion='entropy')

clf.fit(X_train, y_train)  # 學習訓練.fit

# 計算準確率
y_pred = clf.predict(X_test)  # 預測.predict
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

plt.figure(figsize=(14, 5))
plot_tree(clf, feature_names=feature_names)  # 繪製樹狀圖
plt.title("迴歸樹, 用plot_tree畫圖")

show()

# 使用 graphviz 繪製圖形
# 安裝 graphviz (https://graphviz.org/download/)
# 將安裝路徑的bin加入環境變數Path中(C:\Program Files (x86)\Graphviz2.XX\bin)
# pip install graphviz pydotplus

from pydotplus import graph_from_dot_data
from sklearn.tree import export_graphviz

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

# dot 格式存檔

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
    plot1.set_xlabel("Number of iterations", fontsize=12)
    label_format = "{:,.0f}"
    plot1.set_xticklabels([label_format.format(x) for x in range(0, 450, 50)])
    plot1.set_ylabel("Error rate", fontsize=12)
    plot1.set_title("Error rate vs number of iterations", fontsize=16)
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
clf_tree = DecisionTreeClassifier(max_depth=1, random_state=1)
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

clf_1 = tree.DecisionTreeClassifier(criterion="entropy")
clf_1.fit(train_data, train_target)
train_est = clf_1.predict(train_data)
train_est_p = clf_1.predict_proba(train_data)[:, 1]

test_est = clf_1.predict(test_data)
print(test_est)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

clf_2 = svm.SVC()
clf_2.fit(train_data, train_target)
train_est = clf_2.predict(train_data)
test_est = clf_2.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

from sklearn.naive_bayes import GaussianNB

clf_3 = GaussianNB()
clf_3.fit(train_data, train_target)
train_est = clf_3.predict(train_data)
test_est = clf_3.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機

clf_4 = MLPClassifier()  # 多層感知器分類器 函數學習機

clf_4.fit(train_data, train_target)

train_est = clf_4.predict(train_data)
test_est = clf_4.predict(test_data)

print(accuracy_score(test_target, test_est))

# 混淆矩陣
cm = confusion_matrix(test_target, test_est)
print("混淆矩陣 :\n", cm, sep="")

y_pred = [0, 2, 1, 3]
y_true = [0, 1, 2, 3]
print(accuracy_score(y_true, y_pred))
print(accuracy_score(y_true, y_pred, normalize=False))

print("混淆矩陣")
y_true = [2, 0, 2, 2, 0, 1]
y_pred = [0, 0, 2, 2, 0, 2]

# 混淆矩陣
cm = confusion_matrix(y_true, y_pred)
print("混淆矩陣 :\n", cm, sep="")

print("混淆矩陣")
y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]

# 混淆矩陣
cm = confusion_matrix(y_true, y_pred, labels=["ant", "bird", "cat"])
print("混淆矩陣 :\n", cm, sep="")

y = np.array([1, 1, 2, 2])
scores = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = roc_curve(y, scores, pos_label=2)
print(fpr)
print(tpr)
print(thresholds)

plt.plot(fpr, tpr)

show()

y_true = [0, 1, 2, 0, 1, 2]
y_pred = [0, 2, 1, 0, 0, 1]
cc = recall_score(y_true, y_pred, average="macro")  # doctest: +ELLIPSIS
print(cc)

cc = recall_score(y_true, y_pred, average="micro")
print(cc)

cc = recall_score(y_true, y_pred, average="weighted")
print(cc)

cc = recall_score(y_true, y_pred, average=None)
print(cc)

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
)
rf_clf = RandomForestClassifier(class_weight="balanced")
# randomize the data, and run the cross validation for 5 times
cv = ShuffleSplit(X_data.shape[0], n_iter=5, test_size=0.3, random_state=0)
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
