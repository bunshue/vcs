"""



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
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
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

"""
电信客户流失数据

telecom_churn

数据文档 数据说明 变量的含义： 列名 含义 subscriberID 用户ID churn 因变量：是否流失（1表示流失，0表示未流失） gender 性别（男、女） AGE 年龄 edu_class 教育程度（小学及以下、初中、高中/中专/技校、大专、本科、研究生及以上） incomeCode 收入水平（1-10分别代表不同的收入区间） duration 已加入运营商的时长（月） feton 上月ARPU值（平均每个用户每月产生的收入） peakMinAv 月峰值通话时间（分钟） peakMinDiff 非月峰值通话时间（分钟） posTrend 正向情感倾向得分 negTrend 负向情感倾向得分 nrProm 最近6个月参与的营销活动次数 prom 是否参与当前的营销活动（1表示参与，0表示未参与） curPlan 当前套餐类型（A/B/C三种） avgplan 历史平均套餐价格 planChange 套餐变更次数 posPlanChange 套餐升级次数 negPlanChange 套餐降级次数 call_10086 最近3个月拨打10086客服的次数

#数据清洗与格式转换
#查看数据
"""

# import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px

# 导入数据并查看
# 加载数据集
df = pd.read_csv("./data/telecom_churn.csv")
# 将所有列展示出来
df_names = df.columns.tolist()
df_names
df.head(5)

# 查看信息表，清什么，可以看到ID属于个人信息没有用。其次要转换，将str转换为float

# 查看数据、缺失值、重复值、总体概览
df.isna().sum()

# 重复值
df.duplicated().sum()

# 总体
df.info()

df.describe()

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
df_new

# 探索性数据分析（EDA）
# 用图的方式把数据展示出来，告诉大家内些特征对模型有用，那些数据对模型没用 1.特征自己的信息 2.特征和特征之间的关系 3.特征和标签之间的关系

# 查看流失比例，以及关于打客服电话的个数分布

fig = plt.figure()

fig.set(alpha=0.3)  # 设定图表颜色alpha参数
plt.subplot2grid((1, 2), (0, 0))  # 图像几行几列，从第0行第零列
# bar:条形直方图
df["churn"].value_counts().plot(kind="bar")  # 将用户流失分组起来，流失多少人没用流失多少人
plt.title("流失和未流失比例")
plt.ylabel("数量")

plt.subplot2grid((1, 2), (0, 1))
df["call_10086"].value_counts().plot(kind="bar")
plt.title("打客服电话比例")
plt.ylabel("数量")
plt.show()

# peakMinAv 月峰值通话时间（分钟） peakMinDiff 非月峰值通话时间（分钟）

plt.subplot2grid((1, 2), (0, 0))
df["peakMinAv"].plot(kind="kde")  # 峰值通话，图用的kde的图例
plt.xlabel("分钟数")
plt.ylabel("密度")
plt.title("峰值通话")

plt.subplot2grid((1, 2), (0, 1))
df["peakMinDiff"].plot(kind="kde")
plt.xlabel("分钟数")
plt.ylabel("密度")
plt.title("非峰值通话")
plt.show()

# 数据有大有小有正有负，符合高斯分布，我们在做归一化的时候将数据作为float类型

# churn 因变量：是否流失（1表示流失，0表示未流失） prom 是否参与当前的营销活动（1表示参与，0表示未参与）

# 查看参与当前营销和流失的关系
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
# 查看流失与输入输入水平之间的关系
int_yes = df["churn"][df["prom"] == 1].value_counts()
int_no = df["churn"][df["prom"] == 0].value_counts()
# 做图例
df_int = pd.DataFrame({"参与营销": int_yes, "未参与营销": int_no})

df_int.plot(kind="bar", stacked=True)
plt.show()

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
df_new.head(5)

# 特征工程
# 我们需要做一些scala的工作，就是有些属性的scala太大了 对于逻辑回归和梯度下降来说，各个属性的scala差距太大，会对收敛速度有很大的影响 我们这里对所有的都做，其实可以对一些突出的特征做这种处理

y = df_new["churn"]
x = df_new.drop("churn", axis=1)
# 数量级不一样，通过scala实现去量纲的影响
# 在训练模型时之前经常要对数据进行数组转化，as_matrix()：把所有的特征都转化为np.float
X = x.astype(np.float32)
X

# 标准化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)
X
X.shape
# 建立多种模型
# 将数据进行拆分
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
from sklearn.linear_model import LogisticRegression  # 逻辑回归
from sklearn.svm import SVC  # 支持向量机
from sklearn.model_selection import cross_val_score, KFold  # 交叉验证
from sklearn.neighbors import KNeighborsClassifier  # kNN

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
    kfold = KFold(5, shuffle=True, random_state=0)  # 5折
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
plt.show()
"""
KNN:0.773030(0.010844)
------------------
LR:0.835399(0.008645)
------------------
SVM:0.831359(0.001487)
------------------
"""

# 如果不进行标准化明显准确率没有标准化高
# 初始化
"""
results = []
names = []
scoring = 'accuracy'#准确率
for name,model in models:
    kfold = KFold(5,shuffle=True,random_state=0)#5折
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
# "\nresults = []\nnames = []\nscoring = 'accuracy'#准确率\nfor name,model in models:\n    kfold = KFold(5,shuffle=True,random_state=0)#5折\n    cv_results = cross_val_score(model,x,y,cv=kfold)\n    results.append(cv_results)#交叉验证给的结果分\n    names.append(name)\n    #模型的标准差，体现模型的波动值,std越小越稳\n    msg = '%s:%f(%f)'%(name,cv_results.mean(),cv_results.std())\n    print(msg)\n    print('------------------')\n\nKNN:0.698228(0.015081)\n------------------\nLR:0.825869(0.007094)\n------------------\nSVM:0.762914(0.012649)\n------------------\n"
# 模型优化调参
# 不会调优 这里还是觉得准确率不高,我们试一下决策树，随机森林看看

from sklearn import tree  # 树的模块

clf = tree.DecisionTreeClassifier(criterion="entropy")  # 实例化模型，添加criterion参数
clf = clf.fit(X_train, y_train)  # 使用实例化好的模型进行拟合操作
score = clf.score(X_test, y_test)  # 返回预测的准确度
score
# 0.7907647907647908

# 随机森林看一下
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 初始化随机森林
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
# 训练模型
rf_classifier.fit(X_train, y_train)
score2 = rf_classifier.score(X_test, y_test)
score2
# 0.847041847041847


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
