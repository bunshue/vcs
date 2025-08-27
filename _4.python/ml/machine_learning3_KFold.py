"""
KFold





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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import sklearn
import sklearn.linear_model
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV  # 網格搜索
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.model_selection import PredefinedSplit
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score  # R-Squared擬合度, 決定係數
from sklearn.metrics import recall_score  # 再現率
from sklearn.metrics import roc_auc_score
from sklearn.metrics import balanced_accuracy_score


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
sklearn.model_selection.KFold
class sklearn.model_selection.KFold(n_splits=5, *, shuffle=False, random_state=None)

K折交叉验证器

提供训练集或测试集索引以将数据切分为训练集或测试集。将数据集切分为k个连续的交叉（默认情况下不打乱数据）。

然后将每折交叉用作一次验证，而剩下的k-1折交叉形成训练集。

参数	说明
n_splits	int, default=5	折数。必须至少为2。
		0.22版本中：n_splits默认值从3更改为5。）
shuffle		bool, default=False在切分之前是否打乱数据。注意，每次切分内的样本都不会被打乱。

另见：
StratifiedKFold 考虑组信息，以避免因类分布不均衡而造成交叉（对于二进制或多类分类任务）。
GroupKFold 具有非重叠组的K折迭代器变体。
RepeatedKFold 重复K折n次。

第一个n_samples % n_splits的大小为 n_samples // n_splits + 1，其他几折的大小为n_samples // n_splits ，其中n_samples为样本数。

随机CV切分器可能会为每个切分调用返回不同的结果。您可以通过将random_state 设置为整数使结果相同。
"""

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])
kf = KFold(n_splits=2)
cc = kf.get_n_splits(X)
print(cc)
# 2
print(kf)
# KFold(n_splits=2, random_state=None, shuffle=False)
for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

# TRAIN: [2 3] TEST: [0 1]
# TRAIN: [0 1] TEST: [2 3]

"""
方法	说明
get_n_splits(self[, X, y, groups])	返回交叉验证器中的切分迭代次数。
split(self, X[, y, groups])	生成索引以将数据切分为训练集和测试集。
__init__（self，n_splits = 5，*，shuffle = False，random_state = None ）

初始化self。详情可参阅 type（self）的帮助。

get_n_splits（self，X = None，y = None，groups = None ）

返回交叉验证器中的切分迭代次数。

参数	说明
X	object
始终被忽略，为了兼容性而存在。
y	object
始终被忽略，为了兼容性而存在。
groups	object
始终被忽略，为了兼容性而存在。
返回值	说明
n_splits	int
返回交叉验证器中拆分迭代的次数。
split（self，X，y = None，groups = None ）

生成索引以将数据切分为训练集和测试集。

参数	说明
X	object
用于训练的数据，其中n_samples是样本数量，n_features是特征数量。
y	object
监督学习问题的目标变量。
groups	object
将数据集切分为训练集或测试集时使用的样本的分组标签。
输出	说明
train	ndarray	切分的训练集索引。
test	ndarray	切分的测试集索引。
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Resampling methods

N = 100  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
T = 1  # n_targets, 標籤類別
NOISE = 10  # noise, 分散程度

print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y = datasets.make_regression(n_samples=N, n_features=M, n_informative=10)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, shuffle=True)

mod = sklearn.linear_model.Ridge(alpha=10)

mod.fit(X_train, y_train)

y_pred_test = mod.predict(X_test)
print("Test R2: %.2f" % r2_score(y_test, y_pred_test))

# 資料分割
train_idx, validation_idx = train_test_split(
    np.arange(X_train.shape[0]), test_size=0.2, shuffle=True
)

split_inner = PredefinedSplit(test_fold=validation_idx)
print("Train set size: %i" % X_train[train_idx].shape[0])
print("Validation set size: %i" % X_train[validation_idx].shape[0])
print("Test set size: %i" % X_test.shape[0])

lm_cv = GridSearchCV(
    sklearn.linear_model.Ridge(),
    {"alpha": 10.0 ** np.arange(-3, 3)},
    cv=split_inner,
    n_jobs=5,
)

# Fit, indluding model selection with internal Train/validation split
lm_cv.fit(X_train, y_train)

# Predict
y_pred_test = lm_cv.predict(X_test)
print("Test R2: %.2f" % r2_score(y_test, y_pred_test))

estimator = sklearn.linear_model.Ridge(alpha=10)

cv = KFold(n_splits=5, shuffle=True, random_state=9487)

r2_train = list()
r2_test = list()

for train, test in cv.split(X):
    # print(train, test)
    estimator.fit(X[train, :], y[train])
    r2_train.append(r2_score(y[train], estimator.predict(X[train, :])))
    r2_test.append(r2_score(y[test], estimator.predict(X[test, :])))

print("Train r2:%.2f" % np.mean(r2_train))
print("Test  r2:%.2f" % np.mean(r2_test))

scores = cross_val_score(estimator=estimator, X=X, y=y, cv=5)
print("Test  r2:%.2f" % scores.mean())

cv = KFold(n_splits=5, shuffle=True, random_state=9487)
scores = cross_val_score(estimator=estimator, X=X, y=y, cv=cv)
print("Test  r2:%.2f" % scores.mean())

scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv, scoring=["r2", "neg_mean_absolute_error"]
)

print(
    "Test R2:%.2f; MAE:%.2f"
    % (scores["test_r2"].mean(), -scores["test_neg_mean_absolute_error"].mean())
)

N = 100  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(
    n_samples=N, n_features=M, shuffle=True, n_informative=10
)

mod = sklearn.linear_model.LogisticRegression(C=1, solver="lbfgs")

cv = StratifiedKFold(n_splits=5)

# Lists to store scores by folds (for macro measure only)
bacc, auc = [], []

for train, test in cv.split(X, y):
    mod.fit(X[train, :], y[train])
    bacc.append(roc_auc_score(y[test], mod.decision_function(X[test, :])))
    auc.append(balanced_accuracy_score(y[test], mod.predict(X[test, :])))

print("Test AUC : %.2f; bACC : %.2f" % (np.mean(bacc), np.mean(auc)))

# `cross_val_score()`: single metric

scores = cross_val_score(estimator=mod, X=X, y=y, cv=5)

print("Test ACC : %.2f" % scores.mean())


# Provide your own CV and score
def balanced_acc(estimator, X, y, **kwargs):
    """Balanced acuracy scorer."""
    return recall_score(y, estimator.predict(X), average=None).mean()


scores = cross_val_score(estimator=mod, X=X, y=y, cv=cv, scoring=balanced_acc)
print("Test bACC : %.2f" % scores.mean())

# `cross_validate()`: multi metric, + time, etc.

scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv, scoring=["balanced_accuracy", "roc_auc"]
)

print(
    "Test AUC : %.2f; bACC : %.2f"
    % (scores["test_roc_auc"].mean(), scores["test_balanced_accuracy"].mean())
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=True)

cv_inner = StratifiedKFold(n_splits=5, shuffle=True, random_state=9487)

# Cross-validation for model selection
lm_cv = GridSearchCV(
    sklearn.linear_model.LogisticRegression(),
    {"C": 10.0 ** np.arange(-3, 3)},
    cv=cv_inner,
    n_jobs=5,
)

# Fit, indluding model selection with internal CV
lm_cv.fit(X_train, y_train)

# Predict
y_pred_test = lm_cv.predict(X_test)
print("Test bACC : %.2f" % balanced_accuracy_score(y_test, y_pred_test))

# Cross-validation for both model (outer) evaluation and model (inner) selection
# ------------------------------------------------------------------------------

cv_outer = StratifiedKFold(n_splits=5, shuffle=True, random_state=9487)

cv_inner = StratifiedKFold(n_splits=5, shuffle=True, random_state=9487)

# Cross-validation for model (inner) selection
lm_cv = GridSearchCV(
    sklearn.linear_model.Ridge(),
    {"alpha": 10.0 ** np.arange(-3, 3)},
    cv=cv_inner,
    n_jobs=5,
)

# Cross-validation for model (outer) evaluation
scores = cross_validate(
    estimator=mod, X=X, y=y, cv=cv_outer, scoring=["balanced_accuracy", "roc_auc"]
)

print(
    "Test AUC : %.2f; bACC : %.2f, Time: %.2fs"
    % (
        scores["test_roc_auc"].mean(),
        scores["test_balanced_accuracy"].mean(),
        scores["fit_time"].sum(),
    )
)

# Models with built-in cross-validation
# --------------------------------------
# Let sklearn select the best parameters over a default grid.
# **Classification**

print("== Logistic Ridge (L2 penalty) ==")
mod_cv = sklearn.linear_model.LogisticRegressionCV(
    class_weight="balanced", scoring="balanced_accuracy", n_jobs=-1, cv=5
)
scores = cross_val_score(estimator=mod_cv, X=X, y=y, cv=5)
print("Test  ACC : %.2f" % scores.mean())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Parallel computation with joblib

N = 20  # n_samples, 樣本數
M = 5  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(n_samples=N, n_features=M, n_informative=2)

cv = StratifiedKFold(n_splits=5)

# Use `cross_validate` function

estimator = sklearn.linear_model.LogisticRegression(C=1, solver="lbfgs")
cv_results = cross_validate(estimator, X, y, cv=cv, n_jobs=5)
print(np.mean(cv_results["test_score"]), cv_results["test_score"])

# Sequential computation
# If we want have full control of the operations performed within each fold (retrieve the models parameters, etc.). We would like to parallelize the folowing sequetial code:

estimator = sklearn.linear_model.LogisticRegression(C=1, solver="lbfgs")
y_test_pred_seq = np.zeros(len(y))  # Store predictions in the original order
coefs_seq = list()
for train, test in cv.split(X, y):
    X_train, X_test, y_train, y_test = X[train, :], X[test, :], y[train], y[test]
    estimator.fit(X_train, y_train)
    y_test_pred_seq[test] = estimator.predict(X_test)
    coefs_seq.append(estimator.coef_)

test_accs = [
    accuracy_score(y[test], y_test_pred_seq[test]) for train, test in cv.split(X, y)
]
print(np.mean(test_accs), test_accs)
coefs_cv = np.array(coefs_seq)
print(coefs_cv)

print(coefs_cv.mean(axis=0))
print("Std Err of the coef")
print(coefs_cv.std(axis=0) / np.sqrt(coefs_cv.shape[0]))

# Parallel computation with joblib

from joblib import Parallel
from joblib import delayed
from sklearn.base import is_classifier
from sklearn.base import clone


def _split_fit_predict(estimator, X, y, train, test):
    X_train, X_test, y_train, y_test = X[train, :], X[test, :], y[train], y[test]
    estimator.fit(X_train, y_train)
    return [estimator.predict(X_test), estimator.coef_]


estimator = sklearn.linear_model.LogisticRegression(C=1, solver="lbfgs")

parallel = Parallel(n_jobs=5)
cv_ret = parallel(
    delayed(_split_fit_predict)(clone(estimator), X, y, train, test)
    for train, test in cv.split(X, y)
)

y_test_pred_cv, coefs_cv = zip(*cv_ret)

# Retrieve predictions in the original order
y_test_pred = np.zeros(len(y))
for i, (train, test) in enumerate(cv.split(X, y)):
    y_test_pred[test] = y_test_pred_cv[i]

test_accs = [
    accuracy_score(y[test], y_test_pred[test]) for train, test in cv.split(X, y)
]
print(np.mean(test_accs), test_accs)

# Test same predictions and same coeficients

assert np.all(y_test_pred == y_test_pred_seq)
assert np.allclose(np.array(coefs_cv).squeeze(), np.array(coefs_seq).squeeze())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 100  # n_samples, 樣本數
M = 100  # n_features, 特徵數(資料的維度)
print("make_classification,", N, "個樣本, ", M, "個特徵")
X, y = datasets.make_classification(n_samples=N, n_features=M, n_informative=10)

model = sklearn.linear_model.LogisticRegression(C=1)

nperm = 100
scores_perm = np.zeros((nperm, 3))  # 3 scores acc, recall0, recall1

for perm in range(0, nperm):
    # perm = 0; y == yp
    # first run on non-permuted samples
    yp = y if perm == 0 else np.random.permutation(y)
    # CV loop
    y_test_pred = np.zeros(len(yp))
    cv = StratifiedKFold(5)
    for train, test in cv.split(X, y):
        X_train, X_test, y_train, y_test = X[train, :], X[test, :], yp[train], yp[test]
        model.fit(X_train, y_train)
        y_test_pred[test] = model.predict(X_test)
    scores_perm[perm, 0] = accuracy_score(yp, y_test_pred)
    scores_perm[perm, [1, 2]] = recall_score(yp, y_test_pred, average=None)

# Empirical permutation based p-values
pval = np.sum(scores_perm >= scores_perm[0, :], axis=0) / nperm

print(
    "ACC:%.2f(P=%0.3f); SPC:%.2f(P=%0.3f); SEN:%.2f(P=%0.3f)"
    % (
        scores_perm[0, 0],
        pval[0],
        scores_perm[0, 1],
        pval[1],
        scores_perm[0, 2],
        pval[2],
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
y = np.array([1, 2, 3, 4])

kf = KFold(n_splits=2)
kf.get_n_splits(X)
print(kf)
for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
