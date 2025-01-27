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
import sklearn.model_selection as cross_validation
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
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

# 輸出準確性
print(f"訓練資料的準確性 = {clf.score(x_train, y_train)}")
print(f"測試資料的準確性 = {clf.score(x_test, y_test)}")

scores = cross_val_score(clf, X, y, cv=5)
print("看一下5次的成績 :", scores)
print("平均 :", scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = np.array([[180, 85], [174, 80], [170, 75], [167, 45], [158, 52], [155, 44]])
Y = np.array(["man", "man", "man", "woman", "woman", "woman"])

clf = DecisionTreeClassifier()  # 決策樹函數學習機

clf = clf.fit(X, Y)  # 學習訓練.fit

tree.export_graphviz(clf, out_file="tmp_tree1.dot")

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
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data[:, [2, 3]], iris.target, test_size=0.25
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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 第9讲 使用决策树做流失预警模型

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv("data/telecom_churn.csv", skipinitialspace=True)
churn = churn.dropna(axis=0, how="any")
cc = churn.head()
print(cc)

target = churn["churn"]
data = churn.loc[:, "gender":"call_10086"]
cc = data.head()
print(cc)

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    data, target, test_size=0.4, train_size=0.6, random_state=12345
)  # 划分训练集和测试集

# CART算法(分类树)

# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=100,
    min_samples_leaf=100,
    random_state=12345,
)  # 当前支持计算信息增益和GINI
clf.fit(train_data, train_target)

# 可以使用graphviz将树结构输出，在python中嵌入graphviz可参考：pygraphviz

tree.export_graphviz(clf, out_file="tmp_cart1.dot")

# cart预测

train_est = clf.predict(train_data)  # 用模型预测训练集的结果
train_est_p = clf.predict_proba(train_data)[:, 1]  # 用模型预测训练集的概率
test_est = clf.predict(test_data)  # 用模型预测测试集的结果
test_est_p = clf.predict_proba(test_data)[:, 1]  # 用模型预测测试集的概率

# 查看变量重要性等信息

import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵

print(metrics.classification_report(test_target, test_est))  # 计算评估指标

print(
    pd.DataFrame(
        zip(data.columns, clf.feature_importances_), columns=["feature", "importance"]
    )
)  # 变量重要性指标

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter9_1 DT_AllElectronics

# # 决策树

# get_ipython().magic('matplotlib inline')

# pd.set_option('display.max_columns', None)

data = pd.read_csv("data/AllElectronics.csv", skipinitialspace=True)
data.head()

target = data["buys_computer"]
data = data.loc[:, "age":"credit_rating"]
data.head()

# ## CART算法(分类树)
# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=5,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=12345,
)  # 当前支持计算信息增益和GINI
clf.fit(data, target)

# get_ipython().magic('pinfo DecisionTreeClassifier')

tree.export_graphviz(clf, out_file="tmp_cart2.dot")

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
import sklearn.tree as tree

dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=data.columns,
    max_depth=5,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)

# Image(graph.create_png())   # 用IPython顯示圖片 skip

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter9_2 DT_churn_classification_model

# ## 主要功能的帮助文档：
# [matplotlib](http://matplotlib.org/1.4.3/contents.html)
# [seaborn](http://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html)
# [pandas](http://pandas.pydata.org/pandas-docs/version/0.16.0/)
# [scikit-learn](http://scikit-learn.org/stable/)

churn = pd.read_csv("data/telecom_churn.csv")  # 读取已经整理好的数据
churn.head()

sns.barplot(x="edu_class", y="churn", data=churn)
plt.show()

sns.boxplot(x="churn", y="peakMinDiff", hue=None, data=churn)
plt.show()

sns.boxplot(x="churn", y="duration", hue="edu_class", data=churn)
plt.show()

# ##筛选变量
# * 筛选变量时可以应用专业知识，选取与目标字段相关性较高的字段用于建模，也可通过分析现有数据，用统计量辅助选择
# * 为了增强模型稳定性，自变量之间最好相互独立，可运用统计方法选择要排除的变量或进行变量聚类

corrmatrix = churn.corr(
    method="spearman"
)  # spearman相关系数矩阵，可选pearson相关系数，目前仅支持这两种,函数自动排除category类型
corrmatrix_new = corrmatrix[np.abs(corrmatrix) > 0.5]  # 选取相关系数绝对值大于0.5的变量，仅为了方便查看
#  为了增强模型稳定，根据上述相关性矩阵，可排除'posTrend','planChange','nrProm','curPlan'几个变量

# 连续型变量往往是模型不稳定的原因;
# 如果所有的连续变量都分箱了,可以统一使用卡方检验进行变量重要性检验
churn["duration_bins"] = pd.qcut(churn.duration, 5)  #  将duration字段切分为数量（大致）相等的5段
churn["churn"].astype("int64").groupby(churn["duration_bins"]).agg(["count", "mean"])

bins = [0, 4, 8, 12, 22, 73]
churn["duration_bins"] = pd.cut(churn["duration"], bins, labels=False)
churn["churn"].astype("int64").groupby(churn["duration_bins"]).agg(["mean", "count"])

# 根据卡方值选择与目标关联较大的分类变量
# 计算卡方值需要应用到sklearn模块，但该模块当前版本不支持pandas的category类型变量，会出现警告信息，可忽略该警告或将变量转换为int类型

import sklearn.feature_selection as feature_selection

churn["gender"] = churn["gender"].astype("int")
churn["edu_class"] = churn["edu_class"].astype("int")
churn["feton"] = churn["feton"].astype("int")
feature_selection.chi2(
    churn[
        [
            "gender",
            "edu_class",
            "feton",
            "prom",
            "posPlanChange",
            "duration_bins",
            "curPlan",
            "call_10086",
        ]
    ],
    churn["churn"],
)  # 选取部分字段进行卡方检验
# 根据结果显示，'prom'、'posPlanChange'、'curPlan'字段可以考虑排除

# ## 建模
# * 根据数据分析结果选取建模所需字段，同时抽取一定数量的记录作为建模数据
# * 将建模数据划分为训练集和测试集
# * 选择模型进行建模

#  根据模型不同，对自变量类型的要求也不同，为了示例，本模型仅引入'AGE'这一个连续型变量
# model_data = churn[['subscriberID','churn','gender','edu_class','feton','duration_bins']]
model_data = churn[
    [
        "subscriberID",
        "churn",
        "gender",
        "edu_class",
        "feton",
        "duration_bins",
        "call_10086",
        "AGE",
    ]
]  # 第二可选方案
model_data.head()

target = model_data["churn"]  # 选取目标变量
data = model_data.loc[:, "gender":]  # 选取自变量

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    data, target, test_size=0.4, train_size=0.6, random_state=12345
)  # 划分训练集和测试集

# 选择决策树进行建模

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=8, min_samples_split=5
)  # 当前支持计算信息增益和GINI
clf.fit(train_data, train_target)  #  使用训练数据建模

# 查看模型预测结果
train_est = clf.predict(train_data)  #  用模型预测训练集的结果
train_est_p = clf.predict_proba(train_data)[:, 1]  # 用模型预测训练集的概率
test_est = clf.predict(test_data)  #  用模型预测测试集的结果
test_est_p = clf.predict_proba(test_data)[:, 1]  #  用模型预测测试集的概率
pd.DataFrame(
    {"test_target": test_target, "test_est": test_est, "test_est_p": test_est_p}
).T  # 查看测试集预测结果与真实结果对比

# ## 模型评估
import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(test_target, test_est))  # 计算评估指标
print(pd.DataFrame(list(zip(data.columns, clf.feature_importances_))))  # 变量重要性指标

# 察看预测值的分布情况
red, blue = sns.color_palette("Set1", 2)
sns.histplot(test_est_p[test_target == 1], kde=False, bins=15, color=red)
sns.histplot(test_est_p[test_target == 0], kde=False, bins=15, color=blue)
plt.show()

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve")
plt.show()
# 这里表现出了过渡拟合的情况
#########################################################################################
# 参数调优

from sklearn.model_selection import GridSearchCV

param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = DecisionTreeClassifier()

clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(train_data, train_target)

# 查看模型预测结果
train_est = clfcv.predict(train_data)  #  用模型预测训练集的结果
train_est_p = clfcv.predict_proba(train_data)[:, 1]  # 用模型预测训练集的概率
test_est = clfcv.predict(test_data)  #  用模型预测测试集的结果
test_est_p = clfcv.predict_proba(test_data)[:, 1]  #  用模型预测测试集的概率

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve")
plt.show()

clfcv.best_params_

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=5, min_samples_split=24
)  # 当前支持计算信息增益和GINI

clf.fit(train_data, train_target)  #  使用训练数据建模

# ### 可视化
# 使用dot文件进行决策树可视化需要安装一些工具：
#
# - 第一步是安装[graphviz](http://www.graphviz.org/)。linux可以用apt-get或者yum的方法安装。如果是windows，就在官网下载msi文件安装。无论是linux还是windows，装完后都要设置环境变量，将graphviz的bin目录加到PATH，比如windows，将C:/Program Files (x86)/Graphviz2.38/bin/加入了PATH
# - 第二步是安装python插件graphviz： pip install graphviz
# - 第三步是安装python插件pydotplus: pip install pydotplus

import pydotplus
from IPython.display import Image  # 用IPython
import sklearn.tree as tree

dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=train_data.columns,
    max_depth=5,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())   # 用IPython顯示圖片 skip

"""
# ## 模型保存/读取

import pickle as pickle

model_file = open(r'clf.model', 'wb')
pickle.dump(clf, model_file)
model_file.close()

model_load_file = open(r'clf.model', 'rb')
model_load = pickle.load(model_load_file)
model_load_file.close()

test_est_load = model_load.predict(test_data)
pd.crosstab(test_est_load,test_est)
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
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
