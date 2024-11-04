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

#第9讲 使用决策树做流失预警模型

from scipy import stats
import sklearn.cross_validation as cross_validation
import statsmodels.api as sm
import statsmodels.formula.api as smf

churn = pd.read_csv('telecom_churn.csv', skipinitialspace=True)
churn = churn.dropna(axis=0, how='any')
cc = churn.head()
print(cc)

target = churn['churn']
data = churn.ix[:, 'gender':'call_10000']
cc = data.head()
print(cc)

import sklearn.cross_validation as cross_validation

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    data, target, test_size=0.4, train_size=0.6, random_state=12345)   #划分训练集和测试集

#CART算法(分类树)

#建立CART模型

import sklearn.tree as tree

clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_split=100, min_samples_leaf=100, random_state=12345)  # 当前支持计算信息增益和GINI
clf.fit(train_data, train_target)

#可以使用graphviz将树结构输出，在python中嵌入graphviz可参考：pygraphviz

tree.export_graphviz(clf, out_file='cart.dot')

#cart预测

train_est = clf.predict(train_data)  # 用模型预测训练集的结果
train_est_p = clf.predict_proba(train_data)[:, 1]  # 用模型预测训练集的概率
test_est = clf.predict(test_data)  # 用模型预测测试集的结果
test_est_p = clf.predict_proba(test_data)[:, 1]  # 用模型预测测试集的概率

#查看变量重要性等信息

import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵

print(metrics.classification_report(test_target, test_est))  # 计算评估指标

print(pd.DataFrame(zip(data.columns, clf.feature_importances_), columns=['feature', 'importance']))  # 变量重要性指标

 



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

