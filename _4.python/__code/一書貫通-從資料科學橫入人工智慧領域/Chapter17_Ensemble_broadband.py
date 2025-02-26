"""

Ensemble_broadband

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

from sklearn import linear_model, metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM  # 二值型的RBM网络
from sklearn.model_selection import GridSearchCV
import sklearn.model_selection as cross_validation
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.metrics as metrics

print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
cc = model_data.head()
print(cc)

target = model_data["BROADBAND"]
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")
cc = model_data.head()
print(cc)

target = model_data["BROADBAND"]
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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
