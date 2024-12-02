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

from sklearn import linear_model,metrics
from sklearn.model_selection import train_test_split
from sklearn.neural_network import BernoulliRBM#⼆值型的RBM网络
import sklearn.model_selection as cross_validation
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.metrics as metrics

model_data = pd.read_csv("broadband.csv")
model_data.head()

target = model_data["BROADBAND"]
orgData1 = model_data.ix[ :,1:-2]

import sklearn.model_selection as cross_validation

train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    orgData1, target, test_size=0.4, train_size=0.6, random_state=12345)  #划分训练集和测试集

clf = tree.DecisionTreeClassifier(criterion='entropy', max_depth=3, min_samples_split=5)
clf.fit(train_data, train_target)
test_est = clf.predict(test_data)
print("decision tree accuracy:")
print(metrics.classification_report(test_target,test_est))

gbc = ensemble.GradientBoostingClassifier()
gbc.fit(train_data, train_target)
test_est = gbc.predict(test_data)
print("gradient boosting accuracy:")
print(metrics.classification_report(test_target,test_est))

abc = ensemble.AdaBoostClassifier(n_estimators=100)
abc.fit(train_data, train_target)
test_est = abc.predict(test_data)
print("abc classifier accuracy:")
print(metrics.classification_report(test_target,test_est))

rfc = ensemble.RandomForestClassifier(criterion='entropy', n_estimators=3, max_features=0.5, min_samples_split=5)
rfc.fit(train_data, train_target)
test_est = rfc.predict(test_data)
print("random forest accuracy:")
print(metrics.classification_report(test_target,test_est))

 



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

