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

#Ensemble methods

train = pd.read_csv("imb_train.csv")
test = pd.read_csv("imb_test.csv")
cc = train.head()
print(cc)

count_classes = pd.value_counts(train['cls'], sort = True).sort_index()
count_classes.plot(kind = 'bar')
plt.show()

features_train=train.loc[:,"x1":"x2"]
labels_train=train["cls"]

features_test=test.loc[:,"x1":"x2"]
labels_test=test["cls"]

#随机过采样

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=0)
os_features,os_labels = ros.fit_sample(features_train,labels_train)

cc = len(os_labels[os_labels==1])
print(cc)

#过采样SMOTE

from imblearn.over_sampling import SMOTE

oversampler=SMOTE(random_state=0)
os_features,os_labels=oversampler.fit_sample(features_train,labels_train)

cc = len(os_labels[os_labels==1])
print(cc)

#综合采样

from imblearn.combine import SMOTETomek

smote_tomek = SMOTETomek(random_state=0)
os_features,os_labels= smote_tomek.fit_sample(features_train,labels_train)

#CART分类树

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(criterion='gini', 
                             max_depth=3, 
                             class_weight=None,
                             random_state=1234)  # 支持计算Entropy和GINI
clf.fit(os_features,os_labels)

import sklearn.metrics as metrics

print(metrics.classification_report(labels_test,clf.predict(features_test)))

train_est = clf.predict(features_train)  
train_est_p = clf.predict_proba(features_train)[:, 1]  
test_est = clf.predict(features_test)  
test_est_p = clf.predict_proba(features_test)[:, 1]  
fpr_test, tpr_test, th_test = metrics.roc_curve(
    labels_test, test_est_p)

fpr_train, tpr_train, th_train = metrics.roc_curve(
    labels_train, train_est_p)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, 'b--')
plt.plot(fpr_train, tpr_train, 'r-')
plt.title('ROC curve')
plt.show()

print(metrics.roc_auc_score(labels_test, test_est_p))



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

