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

#第11讲 分类器
#KNN

from scipy import stats
import sklearn.model_selection as cross_validation

orgData = pd.read_csv('date_data2.csv')
cc = orgData.describe()
print(cc)

#选取自变量

X = orgData.ix[:, :4]
Y = orgData[['Dated']]
X.head()

#极值标准化, MMS特徵縮放
from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)

cc = X_scaled[1:5]
print(cc)

#划分训练集和测试集

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8, random_state=123)   #划分训练集和测试集

#建模

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)  # 默认欧氏距离
model.fit(train_data, train_target.values.flatten())
test_est = model.predict(test_data)

#验证

import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(test_target, test_est))

model.score(test_data, test_target)

#选择k值

for k in range(1, 15):
    k_model = KNeighborsClassifier(n_neighbors=k)
    k_model.fit(train_data, train_target.values.flatten())
    score = k_model.score(test_data, test_target)
    print(k, '\t', score)

#交叉验证选择k值

#應該也是改成 sklearn.model_selection
from sklearn.grid_search import ParameterGrid
from sklearn.grid_search import GridSearchCV 
from sklearn.model_selection import KFold

n_samples = len(train_data)
kf = KFold(n=n_samples, n_folds=3)
grid = ParameterGrid({'n_neighbors':[range(1,15)]})
estimator = KNeighborsClassifier()
gridSearchCV = GridSearchCV(estimator, grid, cv=kf)
gridSearchCV.fit(train_data, train_target.values.flatten())
gridSearchCV.cv_results_  # cv_results_ : 具體用法模型不同參數下交叉驗證的結果

gridSearchCV.best_params_

best = gridSearchCV.best_estimator_ 
best.score(test_data, test_target)

#练习：试一试哪些参数会影响结果

#朴素贝叶斯

cc = orgData.head()
print(cc)

orgData1 = orgData.ix[:, -3:]

orgData1.income_rank = orgData1.income_rank.astype('category')
orgData1.describe(include='all')

train_data1, test_data1, train_target1, test_target1 = cross_validation.train_test_split(
    orgData1, Y, test_size=0.3, train_size=0.7, random_state=123)

#建模

from sklearn.naive_bayes import BernoulliNB
NB = BernoulliNB(alpha=1)
NB.fit(train_data1, train_target1.values.flatten())
test_est1 = NB.predict(test_data1)

#验证

print(metrics.classification_report(test_target1, test_est1))

NB.score(train_data1, train_target1)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

