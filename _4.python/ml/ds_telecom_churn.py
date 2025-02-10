"""
# 客户流失预警模型

电信客户流失数据    telecom_churn

telecom_churn.csv 3463筆資料 20欄位
subscriberID,churn,gender,AGE,edu_class,incomeCode,duration,feton,peakMinAv,peakMinDiff,posTrend,negTrend,nrProm,prom,curPlan,avgplan,planChange,posPlanChange,negPlanChange,call_10086
19164958, 1, 0, 20, 2, 12, 16, 0, 113,   -8, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0
39244924, 1, 1, 20, 0, 21,  5, 0, 274, -371, 0, 1, 2, 1, 3, 2, 2, 1, 0, 1
39578413, 1, 0, 11, 1, 47,  3, 0, 392, -784, 0, 1, 0, 0, 3, 3, 0, 0, 0, 1
40992265, 1, 0, 43, 0,  4, 12, 0,  31,  -76, 0, 1, 2, 1, 3, 3, 0, 0, 0, 1
43061957, 1, 1, 60, 0,  9, 14, 0, 129, -334, 0, 1, 0, 0, 3, 3, 0, 0, 0, 0
47196850, 0, 0, 20, 2, 24,  9, 1, 281,  309, 1, 0, 0, 0, 2, 2, 0, 0, 0, 1
51236987, 1, 1, 17, 2, 13,  5, 0, 348,  -29, 0, 1, 1, 1, 3, 3, 0, 0, 0, 1
subscriberID 用户ID
churn 因变量：是否流失（1表示流失，0表示未流失）
gender 性别（男、女）
AGE 年龄
edu_class 教育程度（小学及以下、初中、高中/中专/技校、大专、本科、研究生及以上）
incomeCode 收入水平（1-10分别代表不同的收入区间）
duration 已加入运营商的时长（月）
feton 上月ARPU值（平均每个用户每月产生的收入）
peakMinAv 月峰值通话时间（分钟）
peakMinDiff 非月峰值通话时间（分钟）
posTrend 正向情感倾向得分
negTrend 负向情感倾向得分
nrProm 最近6个月参与的营销活动次数
prom 是否参与当前的营销活动（1表示参与，0表示未参与）
curPlan 当前套餐类型（A/B/C三种）
avgplan 历史平均套餐价格
planChange 套餐变更次数
posPlanChange 套餐升级次数
negPlanChange 套餐降级次数
call_10086 最近3个月拨打10086客服的次数
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

# import tensorflow as tf
from common1 import *
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.svm import SVC  # 支持向量机
from sklearn.model_selection import cross_val_score, KFold  # 交叉验证
from sklearn.neighbors import KNeighborsClassifier  # kNN
from sklearn.tree import DecisionTreeClassifier  # 決策樹分類(Decision Tree Classifier)
from sklearn.tree import DecisionTreeRegressor  # 迴歸樹
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import roc_curve
from sklearn.manifold import MDS
from sklearn.decomposition import PCA

# 不要顯示一些警告
import warnings

warnings.filterwarnings("ignore")  # 忽视报错


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import plotly.graph_objects as go
import plotly.express as px

# 数据清洗与格式转换

# 导入数据并查看
# 加载数据集
df = pd.read_csv("./data/telecom_churn.csv")

# 将所有列展示出来
df_names = df.columns.tolist()
print(df_names)

cc = df.head()
print("前5筆資料 :\n", cc, sep="")

# 查看信息表，清什么，可以看到ID属于个人信息没有用。其次要转换，将str转换为float

# 查看数据、缺失值、重复值、总体概览
cc = df.isna().sum()
print(cc)

# 重复值
cc = df.duplicated().sum()
print(cc)

# 总体
cc = df.info()
print(cc)

cc = df.describe()
print(cc)

# describe()可以返回具体的结果，对于每一列
# 数量、平均值、标准差、25%、分位、50%、分位数、最大值、很多时候可以得到NA的数量和比例

# 缺失值处理：连续值--平均数、众数、中位数 非数值型特征---统计个数用众数据填充 当然还可以通过随机森林等算法做预测---同时消耗的代价也比较大

# 数据并没有什么问题
# 数据集甚至将类型都转换好了
# 但是我们在这里写一下一般是怎末转换的
# 将比如说将数据转换为数值类型
# 比如标签转换

# df = df.replace({'男':1,'女':0,'No Data': -1})
# df = df.replace({'有':1,'无':0,'No Data': -1})

# 归一化数据

"""
for feature in data:
    df[feature] = pd.Categorical(df[feature]).codes
"""
#'\nfor feature in data:\n    df[feature] = pd.Categorical(df[feature]).codes\n    '
# 在这里我们需要删除没用的标签比如说id
df_new = df.drop({"subscriberID"}, axis=1)
print(df_new)  # 3463 X 19

print("------------------------------")  # 30個

# 探索性数据分析（EDA）
# 用图的方式把数据展示出来，告诉大家内些特征对模型有用，那些数据对模型没用
# 1.特征自己的信息
# 2.特征和特征之间的关系
# 3.特征和标签之间的关系

# 查看流失比例，以及关于打客服电话的个数分布

plt.subplot(121)
df["churn"].value_counts().plot(kind="bar")  # 将用户流失分组起来，流失多少人没用流失多少人
plt.title("流失和未流失比例")
plt.ylabel("数量")

plt.subplot(122)
df["call_10086"].value_counts().plot(kind="bar")
plt.title("打客服电话比例")
plt.ylabel("数量")
plt.suptitle("查看流失比例")
show()

print("------------------------------")  # 30個

# peakMinAv 月峰值通话时间（分钟） peakMinDiff 非月峰值通话时间（分钟）

plt.subplot(121)
df["peakMinAv"].plot(kind="kde")  # 峰值通话，图用的kde的图例
plt.xlabel("分钟数")
plt.ylabel("密度")
plt.title("峰值通话")

plt.subplot(122)
df["peakMinDiff"].plot(kind="kde")
plt.xlabel("分钟数")
plt.ylabel("密度")
plt.title("非峰值通话")
plt.suptitle("峰值通话/非峰值通话")
show()

print("------------------------------")  # 30個

# 数据有大有小有正有负，符合高斯分布，我们在做归一化的时候将数据作为float类型

# churn 因变量：是否流失（1表示流失，0表示未流失）
# prom 是否参与当前的营销活动（1表示参与，0表示未参与）

# 查看参与当前营销和流失的关系
# 查看流失与输入输入水平之间的关系
int_yes = df["churn"][df["prom"] == 1].value_counts()
int_no = df["churn"][df["prom"] == 0].value_counts()
# 做图例
df_int = pd.DataFrame({"参与营销": int_yes, "未参与营销": int_no})

df_int.plot(kind="bar", stacked=True)
show()

print("------------------------------")  # 30個

# 大概有1900未流失的客户，其中300人参与当月活动0.157 大概有1500流失用户其中有200人参与当月活动0.133

# 特征筛选
# 对于标签数据需要整合
# ds_result = churn_df['churn']
# shift+tab:condition是布尔类型的数组，每个条件都和x,y对应
# 相当于流失了/true为1，没有流失/false为0
# Y = np.where(ds_result == 'True',1,0)
# 删除无用数据
# to_drop = ['stale','Area Code']
# df = ds_tmp.drop(to_drop,axis=1)

cc = df_new.head()
print("前5筆資料 :\n", cc, sep="")

# 特征工程
# 我们需要做一些scala的工作，就是有些属性的scala太大了
# 对于逻辑回归和梯度下降来说，各个属性的scala差距太大，会对收敛速度有很大的影响
# 我们这里对所有的都做，其实可以对一些突出的特征做这种处理

y = df_new["churn"]
x = df_new.drop("churn", axis=1)
# 数量级不一样，通过scala实现去量纲的影响
# 在训练模型时之前经常要对数据进行数组转化，as_matrix()：把所有的特征都转化为np.float
X = x.astype(np.float32)
X

# 标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)
X
X.shape
# 建立多种模型
# 将数据进行拆分

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 初始化模型
models = []
models.append(("KNN", KNeighborsClassifier()))
models.append(("LR", LogisticRegression()))
models.append(("SVM", SVC()))
# 初始化
results = []
names = []
scoring = "accuracy"  # 准确率
for name, model in models:
    print("1111 :", name)
    print("2222 :", model)
    kfold = KFold(5, shuffle=True, random_state=9487)  # 5折
    cv_results = cross_val_score(model, X, y, cv=kfold)
    results.append(cv_results)  # 交叉验证给的结果分
    names.append(name)
    # 模型的标准差，体现模型的波动值,std越小越稳
    msg = "%s:%f(%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    print("------------------")

fig = plt.figure()
fig.suptitle("")
ax = fig.add_subplot(111)

plt.boxplot(results)
ax.set_xticklabels(names)
show()
"""
KNN:0.773030(0.010844)
------------------
LR:0.835399(0.008645)
------------------
SVM:0.831359(0.001487)
------------------
"""

sys.exit()

# 如果不进行标准化明显准确率没有标准化高
# 初始化
"""
results = []
names = []
scoring = 'accuracy'#准确率
for name,model in models:
    kfold = KFold(5,shuffle=True,random_state=9487)#5折
    cv_results = cross_val_score(model,x,y,cv=kfold)
    results.append(cv_results)#交叉验证给的结果分
    names.append(name)
    #模型的标准差，体现模型的波动值,std越小越稳
    msg = '%s:%f(%f)'%(name,cv_results.mean(),cv_results.std())
    print(msg)
    print('------------------')

KNN:0.698228(0.015081)
------------------
LR:0.825869(0.007094)
------------------
SVM:0.762914(0.012649)
------------------
"""
# "\nresults = []\nnames = []\nscoring = 'accuracy'#准确率\nfor name,model in models:\n    kfold = KFold(5,shuffle=True,random_state=9487)#5折\n    cv_results = cross_val_score(model,x,y,cv=kfold)\n    results.append(cv_results)#交叉验证给的结果分\n    names.append(name)\n    #模型的标准差，体现模型的波动值,std越小越稳\n    msg = '%s:%f(%f)'%(name,cv_results.mean(),cv_results.std())\n    print(msg)\n    print('------------------')\n\nKNN:0.698228(0.015081)\n------------------\nLR:0.825869(0.007094)\n------------------\nSVM:0.762914(0.012649)\n------------------\n"
# 模型优化调参
# 不会调优 这里还是觉得准确率不高,我们试一下决策树，随机森林看看

clf = DecisionTreeClassifier(criterion="entropy")  # 实例化模型，添加criterion参数
clf = clf.fit(X_train, y_train)  # 使用实例化好的模型进行拟合操作
score = clf.score(X_test, y_test)  # 返回预测的准确度
score
# 0.7907647907647908

# 随机森林看一下
# 初始化随机森林
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=9487)
# 训练模型
rf_classifier.fit(X_train, y_train)
score2 = rf_classifier.score(X_test, y_test)
score2
# 0.847041847041847

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用决策树做客户流失预警模型

churn = pd.read_csv("data/telecom_churn.csv", skipinitialspace=True)

# churn.iloc[3, 2] = np.nan#假設第3Row第2欄資料缺失(從0算起)

# 刪除所有 NaN 的記錄, 本例並無NaN資料
churn = churn.dropna(axis=0, how="any")  # dropna()刪除含有NaN的列
cc = churn.head()
# print("前5筆資料 :\n", cc, sep="")

print("取出資料欄位X, 後18欄位")
X = churn.loc[:, "gender":"call_10086"]
print(X.shape)
cc = X.head()
# print("前5筆資料 :\n", cc, sep="")

print("取出目標欄位y, 是否流失 0:未流失, 1:流失")
y = churn["churn"]

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""
分类与回归树（classification and regression tree，CART）是决策树算法中的一种，
与其他决策树算法相同，同样由特征选择，树的生成与剪枝组成。
CART被广泛应用，且被用于树的集成模型，例如，GBDT、RF等集成算法的基学习器都是CART树。
决策树是典型的非线性模型，GBDT和RF因此也是非线性模型。
"""

# CART算法(分类树)

# 建立CART模型

clf = DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    min_samples_split=100,
    min_samples_leaf=100,
    random_state=9487,
)  # 決策樹函數學習機  # 当前支持计算信息增益和GINI

clf.fit(x_train, y_train)

# 使用graphviz将树结构输出，在python中嵌入graphviz可参考：pygraphviz
# 存檔 sklearn.tree.export_graphviz(clf, out_file="tmp_cart1.dot") #存檔

# cart预测

# 預測 訓練資料
train_pred = clf.predict(x_train)  # 預測.predict  # 用模型预测训练集的结果
train_pred_p = clf.predict_proba(x_train)[:, 1]  # 用模型预测训练集的概率

# 預測 測試資料
test_pred = clf.predict(x_test)  # 預測.predict  # 用模型预测测试集的结果
test_pred_p = clf.predict_proba(x_test)[:, 1]  # 用模型预测测试集的概率

# 混淆矩陣
cm = confusion_matrix(y_test, test_pred, labels=[0, 1])
print("混淆矩陣 :\n", cm, sep="")

# 计算评估指标, 分類報告
cc = classification_report(y_test, test_pred)
print("分類報告 :\n", cc, sep="")

print("變量重要性指標 :")
print(
    pd.DataFrame(
        zip(X.columns, clf.feature_importances_), columns=["feature", "importance"]
    )
)  # 变量重要性指标

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DT_churn_classification_model

churn = pd.read_csv("data/telecom_churn.csv")  # 读取已经整理好的数据
cc = churn.head()
print("前5筆資料 :\n", cc, sep="")

sns.barplot(x="edu_class", y="churn", data=churn)
plt.title("教育程度 與 是否流失 的關係")
show()

sns.boxplot(x="churn", y="peakMinDiff", hue=None, data=churn)
plt.title("是否流失 與 非月峰值通话时间（分钟） 的關係")
show()

sns.boxplot(x="churn", y="duration", hue="edu_class", data=churn)
plt.title("是否流失 與 已加入运营商的时长（月） 的關係")
show()

# 筛选变量
# 筛选变量时可以应用专业知识，选取与目标字段相关性较高的字段用于建模，也可通过分析现有数据，用统计量辅助选择
# 为了增强模型稳定性，自变量之间最好相互独立，可运用统计方法选择要排除的变量或进行变量聚类

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
# 计算卡方值需要应用到sklearn模块，但该模块当前版本不支持pandas的category类型变量，
# 会出现警告信息，可忽略该警告或将变量转换为int类型

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

# 建模
# 根据数据分析结果选取建模所需字段，同时抽取一定数量的记录作为建模数据
# 将建模数据划分为训练集和测试集
# 选择模型进行建模

# 根据模型不同，对自变量类型的要求也不同，为了示例，本模型仅引入'AGE'这一个连续型变量
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

cc = model_data.head()
print("前5筆資料 :\n", cc, sep="")

y = model_data["churn"]  # 选取目标变量
X = model_data.loc[:, "gender":]  # 选取自变量

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 选择决策树进行建模

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=8, min_samples_split=5
)  # 決策樹函數學習機  # 当前支持计算信息增益和GINI

clf.fit(x_train, y_train)  #  使用训练数据建模

# 預測 訓練資料
train_pred = clf.predict(x_train)  # 預測.predict  #  用模型预测训练集的结果
train_pred_p = clf.predict_proba(x_train)[:, 1]  # 用模型预测训练集的概率

# 預測 測試資料
test_pred = clf.predict(x_test)  # 預測.predict  #  用模型预测测试集的结果
test_pred_p = clf.predict_proba(x_test)[:, 1]  #  用模型预测测试集的概率

pd.DataFrame(
    {"y_test": y_test, "test_pred": test_pred, "test_pred_p": test_pred_p}
).T  # 查看测试集预测结果与真实结果对比

# 模型评估
# 混淆矩陣
cm = confusion_matrix(y_test, test_pred, labels=[0, 1])
print("混淆矩陣 :\n", cm, sep="")

# 计算评估指标, 分類報告
cc = classification_report(y_test, test_pred)
print("分類報告 :\n", cc, sep="")

print("變量重要性指標 :")
print(pd.DataFrame(list(zip(X.columns, clf.feature_importances_))))  # 变量重要性指标

# 察看预测值的分布情况
red, blue = sns.color_palette("Set1", 2)

sns.histplot(test_pred_p[y_test == 1], kde=False, bins=15, color=red)
plt.title("1111")
show()

sns.histplot(test_pred_p[y_test == 0], kde=False, bins=15, color=blue)
plt.title("2222")
show()

fpr_test, tpr_test, th_test = roc_curve(y_test, test_pred_p)
fpr_train, tpr_train, th_train = roc_curve(y_train, train_pred_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve 1")

show()

# 这里表现出了过渡拟合的情况
# 参数调优

param_grid = {
    "criterion": ["entropy", "gini"],
    "max_depth": [2, 3, 4, 5, 6, 7, 8],
    "min_samples_split": [4, 8, 12, 16, 20, 24, 28],
}
clf = DecisionTreeClassifier()  # 決策樹函數學習機

clfcv = GridSearchCV(estimator=clf, param_grid=param_grid, scoring="roc_auc", cv=4)
clfcv.fit(x_train, y_train)

# 查看模型预测结果
train_pred = clfcv.predict(x_train)  # 預測.predict  #  用模型预测训练集的结果
train_pred_p = clfcv.predict_proba(x_train)[:, 1]  # 用模型预测训练集的概率
test_pred = clfcv.predict(x_test)  # 預測.predict  #  用模型预测测试集的结果
test_pred_p = clfcv.predict_proba(x_test)[:, 1]  #  用模型预测测试集的概率

fpr_test, tpr_test, th_test = roc_curve(y_test, test_pred_p)
fpr_train, tpr_train, th_train = roc_curve(y_train, train_pred_p)
plt.figure(figsize=[6, 6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title("ROC curve 2")
show()

cc = clfcv.best_params_
print(cc)

clf = DecisionTreeClassifier(
    criterion="entropy", max_depth=5, min_samples_split=24
)  # 決策樹函數學習機  # 当前支持计算信息增益和GINI

clf.fit(x_train, y_train)  #  使用训练数据建模

# 可视化
# 使用dot文件进行决策树可视化需要安装一些工具：
# - 第一步是安装[graphviz](http://www.graphviz.org/)。
#   如果是windows，就在官网下载msi文件安装。
#   无论是linux还是windows，装完后都要设置环境变量，将graphviz的bin目录加到PATH，
#   比如windows，将C:/Program Files (x86)/Graphviz2.38/bin/加入了PATH
# - 第二步是安装python插件graphviz： pip install graphviz
# - 第三步是安装python插件pydotplus: pip install pydotplus

import pydotplus
from IPython.display import Image  # 用IPython

dot_data = sklearn.tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=x_train.columns,
    max_depth=5,
    class_names=["0", "1"],
    filled=True,
)

graph = pydotplus.graph_from_dot_data(dot_data)
# Image(graph.create_png())   # 用IPython顯示圖片 skip

"""
# 模型保存/读取
import pickle
model_file = open(r'clf.model', 'wb')
pickle.pickle.dump(clf, model_file)
model_file.close()

model_load_file = open(r'clf.model', 'rb')
model_load = pickle.pickle.load(model_load_file)
model_load_file.close()

test_pred_load = model_load.predict(x_test)  # 預測.predict
pd.crosstab(test_pred_load,test_pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 逻辑回归

# subscriberID="个人客户的ID"
# churn="是否流失：1=流失";
# Age="年龄"
# incomeCode="用户居住区域平均收入的代码"
# peakMinAv="统计期间内最高单月通话时长"
# peakMinDiff="统计期间结束月份与开始月份相比通话时长增加数量"
# posTrend="该用户通话时长是否呈现出上升态势：是=1"
# negTrend="该用户通话时长是否呈现出下降态势：是=1"
# nrProm="电话公司营销的数量"
# prom="最近一个月是否被营销过：是=1"
# curPlan="统计时间开始时套餐类型：1=最高通过200分钟；2=300分钟；3=350分钟；4=500分钟"
# avPlan="统计期间内平均套餐类型"
# planChange="统计期间是否更换过套餐：1=是"
# posPlanChange="统计期间是否提高套餐：1=是"
# negPlanChange="统计期间是否降低套餐：1=是"

from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf

# pd.set_option('display.max_columns', None)

# 导入数据和数据清洗

churn = pd.read_csv(r"data/telecom_churn.csv", skipinitialspace=True)
print(churn.shape)

cc = churn.head()
print("前5筆資料 :\n", cc, sep="")

# 分类变量的相关关系

# 交叉表

cross_table = pd.crosstab(churn.posTrend, churn.churn, margins=True)
cross_table

# 列联表


def percConvert(ser):
    return ser / float(ser[-1])


cross_table.apply(percConvert, axis=1)

cc = stats.chi2_contingency(cross_table.iloc[:2, :2])
print("chisq = %6.4f\np-value = %6.4f\ndof = %i\nexpected_freq = %s" % cc, sep="")

# 逻辑回归

churn.plot(kind="scatter", x="duration", y="churn")
plt.title("已加入运营商的时长（月） 與 是否流失 的關係")
show()

# •随机抽样，建立训练集与测试集

train = churn.sample(frac=0.7, random_state=9487).copy()
test = churn[~churn.index.isin(train.index)].copy()
print(" 训练集样本量: %i \n 测试集样本量: %i" % (len(train), len(test)))

lg = smf.glm(
    "churn ~ duration",
    data=train,
    family=sm.families.Binomial(sm.families.links.logit()),
).fit()
lg.summary()

# 预测
train["proba"] = lg.predict(train)  # 預測.predict
test["proba"] = lg.predict(test)  # 預測.predict

cc = test["proba"].head()
print("前5筆資料 :\n", cc, sep="")

# 模型评估
# 设定阈值

test["prediction"] = (test["proba"] > 0.3).astype("int")

# 混淆矩阵

pd.crosstab(test.churn, test.prediction, margins=True)

# 计算准确率

acc = sum(test["prediction"] == test["churn"]) / np.float(len(test))
print("The accurancy is %.2f" % acc)

for i in np.arange(0.1, 0.9, 0.1):
    prediction = (test["proba"] > i).astype("int")
    confusion_matrix = pd.crosstab(prediction, test.churn, margins=True)
    precision = confusion_matrix.loc[0, 0] / confusion_matrix.loc["All", 0]
    recall = confusion_matrix.loc[0, 0] / confusion_matrix.loc[0, "All"]
    Specificity = confusion_matrix.loc[1, 1] / confusion_matrix.loc[1, "All"]
    f1_score = 2 * (precision * recall) / (precision + recall)
    print(
        "threshold: %s, precision: %.2f, recall:%.2f ,Specificity:%.2f , f1_score:%.2f"
        % (i, precision, recall, Specificity, f1_score)
    )


# 绘制ROC曲线

fpr_test, tpr_test, th_test = metrics.roc_curve(test.churn, test.proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train.churn, train.proba)

plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
show()

print("AUC = %.4f" % metrics.auc(fpr_test, tpr_test))

# 包含分类预测变量的逻辑回归

formula = "churn ~ C(avgplan)"

lg_m = smf.glm(
    formula=formula, data=train, family=sm.families.Binomial(sm.families.links.logit())
).fit()
lg_m.summary()


# 多元逻辑回归
# 向前法
def forward_select(data, response):
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = float("inf"), float("inf")
    while remaining:
        aic_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {}".format(response, " + ".join(selected + [candidate]))
            aic = (
                smf.glm(
                    formula=formula,
                    data=data,
                    family=sm.families.Binomial(sm.families.links.logit()),
                )
                .fit()
                .aic
            )
            aic_with_candidates.append((aic, candidate))
        aic_with_candidates.sort(reverse=True)
        best_new_score, best_candidate = aic_with_candidates.pop()
        if current_score > best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
            print("aic is {},continuing!".format(current_score))
        else:
            print("forward selection over!")
            break

    formula = "{} ~ {} ".format(response, " + ".join(selected))
    print("final formula is {}".format(formula))
    model = smf.glm(
        formula=formula,
        data=data,
        family=sm.families.Binomial(sm.families.links.logit()),
    ).fit()
    return model


candidates = [
    "churn",
    "duration",
    "AGE",
    "edu_class",
    "incomeCode",
    "feton",
    "peakMinAv",
    "peakMinDiff",
    "call_10086",
]
data_for_select = train[candidates]

lg_m1 = forward_select(data=data_for_select, response="churn")
lg_m1.summary()

# Seemingly wrong when using 'statsmmodels.stats.outliers_influence.variance_inflation_factor'


def vif(df, col_i):
    from statsmodels.formula.api import ols

    cols = list(df.columns)
    cols.remove(col_i)
    cols_noti = cols
    formula = col_i + "~" + "+".join(cols_noti)
    r2 = ols(formula, df).fit().rsquared
    return 1.0 / (1.0 - r2)


exog = train[candidates].drop(["churn"], axis=1)

for i in exog.columns:
    print(i, "\t", vif(df=exog, col_i=i))

sys.exit()

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
