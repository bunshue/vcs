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

# Ensemble methods

train = pd.read_csv("data/imb_train.csv")
test = pd.read_csv("data/imb_test.csv")
cc = train.head()
print(cc)

count_classes = pd.value_counts(train["cls"], sort=True).sort_index()
count_classes.plot(kind="bar")
plt.show()

features_train = train.loc[:, "x1":"x2"]
labels_train = train["cls"]

features_test = test.loc[:, "x1":"x2"]
labels_test = test["cls"]

# 随机过采样

from imblearn.over_sampling import RandomOverSampler

ros = RandomOverSampler(random_state=0)
os_features, os_labels = ros.fit_sample(features_train, labels_train)

cc = len(os_labels[os_labels == 1])
print(cc)

# 过采样SMOTE

from imblearn.over_sampling import SMOTE

oversampler = SMOTE(random_state=0)
os_features, os_labels = oversampler.fit_sample(features_train, labels_train)

cc = len(os_labels[os_labels == 1])
print(cc)

# 综合采样

from imblearn.combine import SMOTETomek

smote_tomek = SMOTETomek(random_state=0)
os_features, os_labels = smote_tomek.fit_sample(features_train, labels_train)

# CART分类树

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(
    criterion="gini", max_depth=3, class_weight=None, random_state=1234
)  # 支持计算Entropy和GINI
clf.fit(os_features, os_labels)

import sklearn.metrics as metrics

print(metrics.classification_report(labels_test, clf.predict(features_test)))

train_est = clf.predict(features_train)
train_est_p = clf.predict_proba(features_train)[:, 1]
test_est = clf.predict(features_test)
test_est_p = clf.predict_proba(features_test)[:, 1]
fpr_test, tpr_test, th_test = metrics.roc_curve(labels_test, test_est_p)

fpr_train, tpr_train, th_train = metrics.roc_curve(labels_train, train_est_p)

plt.figure(figsize=[3, 3])
plt.plot(fpr_test, tpr_test, "b--")
plt.plot(fpr_train, tpr_train, "r-")
plt.title("ROC curve")
plt.show()

print(metrics.roc_auc_score(labels_test, test_est_p))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# chapter16 Imbalance

import pandas as pd
import matplotlib.pyplot as plt

train = pd.read_csv("data/imb_train.csv")
test = pd.read_csv("data/imb_test.csv")
train.head()

y_train = train["cls"]
X_train = train.ix[:, :"X5"]
y_test = test["cls"]
X_test = test.ix[:, :"X5"]

print("train_size: %s" % len(y_train), "test_size: %s" % len(y_test))


# In[4]:


plt.figure(figsize=[3, 2])
count_classes = pd.value_counts(y_train, sort=True)
count_classes.plot(kind="bar")
plt.show()


# In[6]:
# 1、采用抽样的方法

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek

ros = RandomOverSampler(random_state=0, ratio="auto")  # 随机过采样
sos = SMOTE(random_state=0)  # SMOTE过采样
kos = SMOTETomek(random_state=0)  # 综合采样

X_ros, y_ros = ros.fit_sample(X_train, y_train)
X_sos, y_sos = sos.fit_sample(X_train, y_train)
X_kos, y_kos = kos.fit_sample(X_train, y_train)

# %%
print("ros: %s, sos:%s, kos:%s" % (len(y_ros), len(y_sos), len(y_kos)))


# In[7]:


y_ros.sum(), y_sos.sum(), y_kos.sum()


# In[8]:


from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

clf = DecisionTreeClassifier(criterion="gini", random_state=1234)
param_grid = {"max_depth": [3, 4, 5, 6], "max_leaf_nodes": [4, 6, 8, 10, 12]}
cv = GridSearchCV(clf, param_grid=param_grid, scoring="f1")


# In[9]:


data = [[X_train, y_train], [X_ros, y_ros], [X_sos, y_sos], [X_kos, y_kos]]

for features, labels in data:
    cv.fit(features, labels)
    predict_test = cv.predict(X_test)

    print(
        "auc:%.3f" % metrics.roc_auc_score(y_test, predict_test),
        "recall:%.3f" % metrics.recall_score(y_test, predict_test),
        "precision:%.3f" % metrics.precision_score(y_test, predict_test),
    )


# In[10]:

# 2、采用改变样本权重的方法
param_grid2 = {
    "max_depth": [3, 4, 5, 6],
    "max_leaf_nodes": [4, 6, 8, 10, 12],
    "class_weight": [{0: 1, 1: 5}, {0: 1, 1: 10}, {0: 1, 1: 15}],
}

cv2 = GridSearchCV(clf, param_grid=param_grid2, scoring="f1")


# In[11]:


cv2.fit(X_train, y_train)
predict_test2 = cv2.predict(X_test)

print(
    "auc:%.3f" % metrics.roc_auc_score(y_test, predict_test2),
    "recall:%.3f" % metrics.recall_score(y_test, predict_test2),
    "precision:%.3f" % metrics.precision_score(y_test, predict_test2),
)


# In[11]:


cv2.best_params_

# %%


print("------------------------------------------------------------")  # 60個
