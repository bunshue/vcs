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

#第十讲 使用神经网络进行客户流失预警

from sklearn.neural_network import MLPClassifier
from scipy import stats
import sklearn.cross_validation as cross_validation
import statsmodels.api as sm
import statsmodels.formula.api as smf

data = pd.read_csv('telecom_churn.csv')
cc = data.head()
print(cc)

#随机抽样，建立训练集与测试集
train, test = cross_validation.train_test_split(data, test_size=1000)

from sklearn import preprocessing
#进行极差标准化
train_X = train.ix[:, 3:-1]
test_X = test.ix[:, 3:-1]
scaler = preprocessing.MinMaxScaler().fit(train_X)
train_X = scaler.transform(train_X)
test_X = scaler.transform(test_X)
train_Y = train['churn'].get_values()  # 为满足后续(pybrain)建模需要做相应变换
test_Y = test['churn'].get_values()

#http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html#sklearn.neural_network.MLPClassifier

clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                     hidden_layer_sizes=(100), random_state=1)

clf.fit(train_X, train_Y) 

test_Y_pred=clf.predict(test_X)

#Index

cc = pd.crosstab(test_Y, test_Y_pred)
print(cc)

from pybrain.tools.validation import Validator

cc = Validator.classificationPerformance( test_Y_pred, test_Y )
print(cc)

import sklearn.metrics as metrics
print(metrics.classification_report(test_Y, test_Y_pred))

#ROC Curve

test_est_p=clf.predict_proba(test_X)[:,1]
train_est_p=clf.predict_proba(train_X)[:,1]

fpr_test, tpr_test, th_test = metrics.roc_curve(test_Y, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_Y, train_est_p)
plt.figure(figsize=[6,6])
plt.plot(fpr_test, tpr_test,color='red')
plt.plot(fpr_train, tpr_train,color='black')
plt.title('ROC curve')
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

