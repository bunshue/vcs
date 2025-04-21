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

from sklearn.model_selection import train_test_split
import sklearn.tree as tree
import sklearn.ensemble as ensemble
import sklearn.metrics as metrics
from sklearn.model_selection import GridSearchCV

print("------------------------------------------------------------")  # 60個

# 宽带营销的数据"broadband.csv"
model_data = pd.read_csv("data/broadband.csv")

target = model_data["BROADBAND"]
orgData1 = model_data.ix[:, 1:-2]  # 所有 .ix[ 改成 .loc[

# from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score,  precision_recall_curve, average_precision_score
from sklearn import metrics


def metrics_roc(ts_real_Y, tr_real_Y, ts_pred_prob, tr_pred_prob):
    fpr_test, tpr_test, th_test = metrics.roc_curve(ts_real_Y, ts_pred_prob)
    fpr_train, tpr_train, th_train = metrics.roc_curve(tr_real_Y, tr_pred_prob)
    plt.figure(figsize=[3, 3])
    plt.plot(fpr_test, tpr_test, "b--")
    plt.plot(fpr_train, tpr_train, "r-")
    plt.title("ROC curve::Test is Blue")
    print("Test AUC = %.4f" % metrics.auc(fpr_test, tpr_test))
    print("Train AUC = %.4f" % metrics.auc(fpr_train, tpr_train))
    plt.show()


def metrics_pr(ts_real_Y, tr_real_Y, ts_pred_prob, tr_pred_prob):
    precision_test, recall_test, th_test = metrics.precision_recall_curve(
        ts_real_Y, ts_pred_prob
    )
    precision_train, recall_train, th_train = metrics.precision_recall_curve(
        tr_real_Y, tr_pred_prob
    )
    plt.figure(figsize=[3, 3])
    plt.plot(recall_test, precision_test, "b--")
    plt.plot(recall_train, precision_train, "r-")
    plt.title("precision-Recall curve:Test is Blue")
    print("Test AP = %.4f" % metrics.average_precision_score(ts_real_Y, ts_pred_prob))
    print("Train AP = %.4f" % metrics.average_precision_score(tr_real_Y, tr_pred_prob))
    plt.show()


# https://pypi.org/project/scikit-plot/0.3.4/
import scikitplot as skplt  # pip install scikit-plot


def plot_result(Y, pred, pred_proba):
    # 输出混淆矩阵
    skplt.metrics.plot_confusion_matrix(Y, pred)
    plt.show()
    # 输出roc曲线
    skplt.metrics.plot_roc_curve(Y, pred_proba, curves=("each_class"))
    plt.show()
    # 输出pr曲线
    skplt.metrics.plot_precision_recall_curve(Y, pred_proba, curves=("each_class"))
    plt.show()
    # 输出ks曲线
    skplt.metrics.plot_ks_statistic(Y, pred_proba)
    plt.show()


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

# 使用scikitplot
test_est = clfcv.predict(test_data)
# train_est = clfcv.predict(train_data)
y_predicted_probas = clfcv.predict_proba(test_data)
plot_result(test_target, test_est, y_predicted_probas)

# 使用sklearn.metrics
tr_pred_prob = clfcv.predict_proba(train_data)[:, 1]
ts_pred_prob = clfcv.predict_proba(test_data)[:, 1]
metrics_roc(test_target, train_target, ts_pred_prob, tr_pred_prob)

metrics_pr(test_target, train_target, ts_pred_prob, tr_pred_prob)

################################################################################################
# GBDT
gbc = ensemble.GradientBoostingClassifier(
    learning_rate=0.1, max_depth=2, min_samples_split=20, n_estimators=100
)
gbc.fit(train_data, train_target)
# 使用scikitplot
test_est = gbc.predict(test_data)
y_predicted_probas = gbc.predict_proba(test_data)
plot_result(test_target, test_est, y_predicted_probas)

# 使用sklearn.metrics
tr_pred_prob = gbc.predict_proba(train_data)[:, 1]
ts_pred_prob = gbc.predict_proba(test_data)[:, 1]
metrics_roc(test_target, train_target, ts_pred_prob, tr_pred_prob)

metrics_pr(test_target, train_target, ts_pred_prob, tr_pred_prob)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
