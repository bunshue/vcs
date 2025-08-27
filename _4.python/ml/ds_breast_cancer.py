"""
#乳癌診斷預測 => 分類問題

breast_cancer

569組資料 30個特徵

特徵：
feature_names : [
 'mean radius' 'mean texture' 'mean perimeter' 'mean area'
 'mean smoothness' 'mean compactness' 'mean concavity'
 'mean concave points' 'mean symmetry' 'mean fractal dimension'
 'radius error' 'texture error' 'perimeter error' 'area error'
 'smoothness error' 'compactness error' 'concavity error'
 'concave points error' 'symmetry error' 'fractal dimension error'
 'worst radius' 'worst texture' 'worst perimeter' 'worst area'
 'worst smoothness' 'worst compactness' 'worst concavity'
 'worst concave points' 'worst symmetry' 'worst fractal dimension'
]

半徑(radius) 平均值、標準誤、最差值
紋理(texture) 平均值、標準誤、最差值
周長(perimeter) 平均值、標準誤、最差值
面積(area) 平均值、標準誤、最差值
平滑度(smoothness) 平均值、標準誤、最差值
緊湊度(compactness) 平均值、標準誤、最差值
凹度(concavity) 平均值、標準誤、最差值
凹點(concave points) 平均值、標準誤、最差值
對稱(symmetry) 平均值、標準誤、最差值
碎形維度(fractal dimension) 平均值、標準誤、最差值
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

from sklearn import datasets
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_text
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score  # F値
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay  # 混淆矩陣圖
from sklearn.datasets import make_classification
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier
from sklearn.pipeline import make_pipeline

import sklearn

# 不要顯示一些警告
import warnings

warnings.filterwarnings("ignore")


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("乳癌診斷預測 基本數據")

breast_cancer = datasets.load_breast_cancer()

print("feature_names :", breast_cancer.feature_names)
print("target_names :", breast_cancer.target_names)

X = breast_cancer.data
y = breast_cancer.target

# X = X[:, :10]  # 原本有30個特徵, 取出前10個特徵
print(X.shape)

print("全部資料 做邏輯迴歸")
logistic_regression = LogisticRegression()
logistic_regression.fit(X, y)
y_pred = logistic_regression.predict(X)
print(f"計算準確率 : {accuracy_score(y, y_pred)*100:.2f}%")

print("資料分割 做邏輯迴歸")
# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
logistic_regression = LogisticRegression()
logistic_regression.fit(X_train, y_train)
y_pred = logistic_regression.predict(X_test)
print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

print(
    "data shape: {0}; no. positive: {1}; no. negative: {2}".format(
        X.shape, y[y == 1].shape[0], y[y == 0].shape[0]
    )
)
print(breast_cancer.data[0])

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LogisticRegression(solver="liblinear")

model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print("決定係數R2(R-squared) train_score :", train_score)
print("決定係數R2(R-squared) test_score :", test_score)

# 樣本預測
y_pred = model.predict(X_test)
print("matchs: {0}/{1}".format(np.equal(y_pred, y_test).sum(), y_test.shape[0]))

# 預測概率：找出低于 90% 概率的樣本個數
y_pred_proba = model.predict_proba(X_test)
print("sample of predict probability: {0}".format(y_pred_proba[0]))
y_pred_proba_0 = y_pred_proba[:, 0] > 0.1
result = y_pred_proba[y_pred_proba_0]
y_pred_proba_1 = result[:, 1] > 0.1
print(result[y_pred_proba_1])

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


# 增加多項式預處理
def polynomial_model(degree=1, **kwarg):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    logistic_regression = LogisticRegression(**kwarg)
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("logistic_regression", logistic_regression),
        ]
    )
    return pipeline


model = polynomial_model(degree=2, penalty="l1", solver="liblinear")

start = time.time()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)

print("耗時 : {0:.6f}".format(time.time() - start))
print("決定係數R2(R-squared) train_score :", train_score)
print("決定係數R2(R-squared) cv_score :", cv_score)

logistic_regression = model.named_steps["logistic_regression"]
print(
    "model parameters shape: {0}; count of non-zero element: {1}".format(
        logistic_regression.coef_.shape, np.count_nonzero(logistic_regression.coef_)
    )
)

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
title = "Learning Curves (degree={0}, penalty={1})"
degrees = [1, 2]
penalty = "l1"

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(
        plt,
        polynomial_model(
            degree=degrees[i], penalty=penalty, solver="liblinear", max_iter=300
        ),
        title.format(degrees[i], penalty),
        X,
        y,
        ylim=(0.8, 1.01),
        cv=cv,
    )

print("耗時 : {0:.6f}".format(time.time() - start))

show()

print("------------------------------")  # 30個

penalty = "l2"

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(
        plt,
        polynomial_model(degree=degrees[i], penalty=penalty, solver="lbfgs"),
        title.format(degrees[i], penalty),
        X,
        y,
        ylim=(0.8, 1.01),
        cv=cv,
    )

print("耗時 : {0:.6f}".format(time.time() - start))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

print(
    "data shape: {0}; no. positive: {1}; no. negative: {2}".format(
        X.shape, y[y == 1].shape[0], y[y == 0].shape[0]
    )
)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("RBF / 高斯核函數 / 徑向基函數核 (Radial basis function kernel)")
clf = SVC(C=1.0, kernel="rbf", gamma=0.1)

clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("決定係數R2(R-squared) train_score :", train_score)
print("決定係數R2(R-squared) test_score :", test_score)


from common.utils import plot_param_curve
from sklearn.model_selection import GridSearchCV  # 網格搜索

gammas = np.linspace(0, 0.0003, 30)
param_grid = {"gamma": gammas}
clf = GridSearchCV(SVC(), param_grid, cv=5)
# clf = GridSearchCV(SVC(), param_grid, cv=5, scoring='roc_auc',n_jobs=-1)

clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

# 有錯誤
# plt.figure(figsize=(10, 4), dpi=144)
# cv_results_ : 具體用法模型不同參數下交叉驗證的結果
# plot_param_curve(plt, gammas, clf.cv_results_, xlabel='gamma')
# show()

print("------------------------------")  # 30個

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
title = "Learning Curves for Gaussian Kernel"

start = time.time()
plt.figure(figsize=(10, 4), dpi=144)
plot_learning_curve(
    plt, SVC(C=1.0, kernel="rbf", gamma=0.01), title, X, y, ylim=(0.5, 1.01), cv=cv
)

print("耗時 : {0:.6f}".format(time.time() - start))

show()

print("------------------------------")  # 30個

print("多項式核函數")
clf = SVC(C=1.0, kernel="poly", degree=2)

clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("決定係數R2(R-squared) train_score :", train_score)
print("決定係數R2(R-squared) test_score :", test_score)

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
title = "Learning Curves with degree={0}"
degrees = [1, 2]

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(
        plt,
        SVC(C=1.0, kernel="poly", degree=degrees[i]),
        title.format(degrees[i]),
        X,
        y,
        ylim=(0.8, 1.01),
        cv=cv,
        n_jobs=4,
    )

print("耗時 : {0:.6f}".format(time.time() - start))

show()

print("------------------------------")  # 30個

print("多項式 LinearSVC")

from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline


def create_model(degree=2, **kwarg):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    scaler = MinMaxScaler()
    linear_svc = LinearSVC(**kwarg)
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("scaler", scaler),
            ("linear_svc", linear_svc),
        ]
    )
    return pipeline


clf = create_model(penalty="l1", dual=False)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("決定係數R2(R-squared) train_score :", train_score)
print("決定係數R2(R-squared) test_score :", test_score)

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
title = "Learning Curves for LinearSVC with Degree={0}"
degrees = [1, 2]

start = time.time()
plt.figure(figsize=(12, 4), dpi=144)
for i in range(len(degrees)):
    plt.subplot(1, len(degrees), i + 1)
    plot_learning_curve(
        plt,
        create_model(penalty="l1", dual=False, degree=degrees[i]),
        title.format(degrees[i]),
        X,
        y,
        ylim=(0.8, 1.01),
        cv=cv,
    )

print("耗時 : {0:.6f}".format(time.time() - start))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Non-linear models
=================
Here we focuse on non-linear models for classification. Nevertheless, each
classification model has its regression counterpart.
"""

np.set_printoptions(precision=2)

# Support Vector Machines (SVM)

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# Preprocessing: unequal variance of input features, requires scaling for svm.

ax = sns.displot(
    x=X_train.std(axis=0),
    kind="kde",
    bw_adjust=0.2,
    cut=0,
    fill=True,
    height=3,
    aspect=1.5,
)
_ = ax.set_xlabels("Std-dev").tight_layout()

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# Fit-predict
# Probalility is a logistic of the decision_function

svm = SVC(kernel="rbf", probability=True).fit(X_train, y_train)
y_pred = svm.predict(X_test)
y_score = svm.decision_function(X_test)
y_prob = svm.predict_proba(X_test)[:, 1]

ax = sns.relplot(x=y_score, y=y_prob, hue=y_pred, height=2, aspect=1.5)
_ = ax.set_axis_labels("decision function", "Probability").tight_layout()

# Scores

print(
    "bAcc: %.2f, AUC: %.2f (AUC with proba: %.2f)"
    % (
        metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
        metrics.roc_auc_score(y_true=y_test, y_score=y_score),
        metrics.roc_auc_score(y_true=y_test, y_score=y_prob),
    )
)

# Usefull internals: indices of support vectors within original X
np.all(X_train[svm.support_, :] == svm.support_vectors_)

forest = RandomForestClassifier(n_estimators=100)

forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)
y_prob = forest.predict_proba(X_test)[:, 1]

# Scores
print(
    "bAcc: %.2f, AUC: %.2f "
    % (
        metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
        metrics.roc_auc_score(y_true=y_test, y_score=y_prob),
    )
)

# Extra Trees (Low Variance)
# Extra Trees is like Random Forest, in that it builds multiple trees and splits nodes using random
# subsets of features, but with two key differences: it does not bootstrap observations
# (meaning it samples without replacement), and nodes are split on random splits, not best splits.
# So, in summary, ExtraTrees:
# builds multiple trees with bootstrap = False by default, which means it samples without replacement
# nodes are split based on random splits among a random subset of the features selected at every node
# In Extra Trees, randomness doesn’t come from bootstrapping of data, but rather comes from
# the random splits of all observations.
# ExtraTrees is named for (Extremely Randomized Trees).

from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(
    n_estimators=100, learning_rate=0.1, subsample=0.5, random_state=0
)
gb.fit(X_train, y_train)

y_pred = gb.predict(X_test)
y_prob = gb.predict_proba(X_test)[:, 1]

print(
    "bAcc: %.2f, AUC: %.2f "
    % (
        metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
        metrics.roc_auc_score(y_true=y_test, y_score=y_prob),
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("学習データと検証データに分割")

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model_svc = SVC()

model_svc.fit(X_train, y_train)

y_train_pred = model_svc.predict(X_train)
y_test_pred = model_svc.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_train, y_train_pred)*100:.2f}%")
print(f"計算準確率 : {accuracy_score(y_test, y_test_pred)*100:.2f}%")

model_rfc = RandomForestClassifier()

model_rfc.fit(X_train, y_train)

y_train_pred = model_rfc.predict(X_train)
y_test_pred = model_rfc.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_train, y_train_pred)*100:.2f}%")
print(f"計算準確率 : {accuracy_score(y_test, y_test_pred)*100:.2f}%")

print("------------------------------")  # 30個

print("交差検証（クロスバリデーション）")

from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True)

model_rfc_1 = RandomForestClassifier()

cross_val_score(model_rfc_1, X, y, cv=cv, scoring="accuracy")

cross_val_score(model_rfc_1, X, y, cv=cv, scoring="f1")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Hyperparameter 超參數 ハイパーパラメータの探索")

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

X = X[:, :10]  # 原本有30個特徵, 取出前10個特徵

from sklearn.model_selection import GridSearchCV  # 網格搜索
from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True)

param_grid = {"max_depth": [5, 10, 15], "n_estimators": [10, 20, 30]}

model_rfc_2 = RandomForestClassifier()

grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring="accuracy")
grid_search.fit(X, y)

print(grid_search.best_score_)
print(grid_search.best_params_)

grid_search = GridSearchCV(model_rfc_2, param_grid, cv=cv, scoring="f1")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 最近 k 鄰數量：n_neighbors

# 取得特徵與標籤資料

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size=0.2)

cv_scores = []  # 用來收集交叉驗證準確率的 list

test_scores = []  # 用來收集測試集準確率的 list

x = np.arange(10) + 1  # 圖表 X 軸 (KNN 模型的 k 值)

for k in x:
    knn = KNeighborsClassifier(n_neighbors=k).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(knn, dx_train, dy_train, cv=5).mean())
    test_scores.append(knn.score(dx_test, dy_test))

plt.title("KNN hyperparameter")
plt.plot(x, cv_scores, label="CV score")  # 繪製交叉驗證折線圖
plt.plot(x, test_scores, label="Test score")  # 繪製測試集預測折線圖
plt.xlabel("k neighbors")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用 GridSearchCV 自動搜尋最佳 k 值

from sklearn.model_selection import GridSearchCV  # 網格搜索

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx, dy, test_size=0.2)

param_grid = {"n_neighbors": np.arange(10) + 1}  # 要網格搜尋的參數
model = GridSearchCV(KNeighborsClassifier(), param_grid)
model.fit(dx_train, dy_train)  # 用最佳模型來做訓練

print("Best params:", model.best_params_)  # 傳回最佳參數
print("CV score:", model.best_score_.round(3))

cc = model.score(dx_test, dy_test)
print("決定係數R2(R-squared) :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 邏輯斯迴歸的 C：常規化強度

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)  # 資料標準化

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

cv_scores = []
test_scores = []

x = [10**n for n in range(-4, 5)]

x_str = [str(n) for n in x]  # X 軸各數值『名稱』

for c in x:
    logistic_regression = LogisticRegression(C=c, max_iter=1000).fit(dx_train, dy_train)
    cv_scores.append(
        cross_val_score(logistic_regression, dx_train, dy_train, cv=5).mean()
    )
    test_scores.append(logistic_regression.score(dx_test, dy_test))

plt.title("Logistic Regression hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("C")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性 SVC 的 C：常規化強度

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

cv_scores = []
test_scores = []

x = [10**n for n in range(-4, 5)]
x_str = [str(n) for n in x]

for c in x:
    linear_svc = LinearSVC(C=c, max_iter=10000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(linear_svc, dx_train, dy_train, cv=5).mean())
    test_scores.append(linear_svc.score(dx_test, dy_test))

plt.title("Linear SVM hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("C")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# C, gamma 與 kernel 參數

from sklearn.model_selection import GridSearchCV  # 網格搜索
from sklearn.model_selection import RandomizedSearchCV

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

x = [10**n for n in range(-2, 3)]

param_grid = {"C": x, "gamma": x, "kernel": ["linear", "rbf", "poly", "sigmoid"]}

model = GridSearchCV(SVC(), param_grid)
model.fit(dx_train, dy_train)

print("Best params: ", model.best_params_)
print("CV score:", model.best_score_.round(3))

cc = model.score(dx_test, dy_test)
print("決定係數R2(R-squared) :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用 RandomizedSearchCV 更快速尋找較適當的參數

from sklearn.model_selection import RandomizedSearchCV

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

param_grid = {
    "C": np.linspace(1, 100, 100),
    "gamma": np.linspace(0.01, 1, 100),
    "kernel": ["linear", "rbf", "poly", "sigmoid"],
}

model = RandomizedSearchCV(SVC(), param_grid, n_iter=100)
model.fit(dx_train, dy_train)

print("Best params:", model.best_params_)
print("CV score:", model.best_score_.round(3))

cc = model.score(dx_test, dy_test)
print("決定係數R2(R-squared) :", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 決策樹的最大深度：max_depth

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

cv_scores = []

test_scores = []

x = np.arange(12) + 1

x_str = [str(n) for n in x]

for d in x:
    tree = DecisionTreeClassifier(max_depth=d).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(tree, dx_train, dy_train, cv=5).mean())
    test_scores.append(tree.score(dx_test, dy_test))

plt.title("Decision Tree hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("Max depth")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

dx, dy = datasets.load_breast_cancer(return_X_y=True)

breast_cancer = datasets.load_breast_cancer()
feature_names = list(breast_cancer.feature_names)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

model = DecisionTreeClassifier(max_depth=3).fit(dx_train, dy_train)

print(export_text(model, feature_names=feature_names))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 隨機森林的規模 n_estimators

dx, dy = datasets.load_breast_cancer(return_X_y=True)

# 特徵縮放
dx_std = sklearn.preprocessing.StandardScaler().fit_transform(dx)

# 資料分割
dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

cv_scores = []
test_scores = []

x = (np.arange(10) + 1) * 50
x_str = [str(n) for n in x]

for t in x:
    tree = RandomForestClassifier(n_estimators=t, max_depth=3, random_state=0)
    tree.fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(tree, dx_train, dy_train, cv=5).mean())
    test_scores.append(tree.score(dx_test, dy_test))

plt.title("Random Forest hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("Number of trees")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("學習曲線和驗證曲線")


def draw_curve(params, train_score, test_score):
    train_mean = np.mean(train_score, axis=1)  # 均值
    train_std = np.std(train_score, axis=1)  # 標準差
    test_mean = np.mean(test_score, axis=1)
    test_std = np.std(test_score, axis=1)
    plt.plot(params, train_mean, "--", color="g", label="training")
    plt.fill_between(
        params, train_mean + train_std, train_mean - train_std, alpha=0.2, color="g"
    )  # 以半透明方式繪圖區域
    plt.plot(params, test_mean, "o-", color="b", label="testing")
    plt.fill_between(
        params, test_mean + test_std, test_mean - test_std, alpha=0.2, color="b"
    )
    plt.grid()  # 顯示網格
    plt.legend()  # 顯示圖例文字
    plt.ylim(0.5, 1.05)  # 設定y軸顯示範圍
    show()


from sklearn.model_selection import learning_curve

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data
y = breast_cancer.target

clf = RandomForestClassifier()

params = np.linspace(0.1, 1.0, 10)  # 從0.1到1，切分成10份

train_sizes, train_score, test_score = learning_curve(
    clf, X, y, train_sizes=params, cv=10, scoring="accuracy"
)  # 10折交叉驗證

draw_curve(params, train_score, test_score)


from sklearn.model_selection import validation_curve

params = [10, 20, 40, 80, 160, 240]

train_score, test_score = validation_curve(
    RandomForestClassifier(),
    X,
    y,
    param_name="n_estimators",
    cv=10,
    scoring="accuracy",
    param_range=params,
)

draw_curve(params, train_score, test_score)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("K近鄰算法")

breast_cancer = datasets.load_breast_cancer()

X = breast_cancer.data  # 自變量
y = breast_cancer.target  # 因變量

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = KNeighborsClassifier(5)  # 設鄰居數爲5個

clf.fit(x_train, y_train)  # 訓練模型

cc = clf.score(x_test, y_test)
print("決定係數R2(R-squared) :", cc)

print(clf.predict([x_test[0]]), y_test[0], clf.predict_proba([x_test[0]]))

print("------------------------------")  # 30個

from scipy.spatial import distance
import operator


def classify(inX, dataSet, labels, k):
    # print('do classify')
    # S=np.cov(dataSet.T)   #協方差矩陣，爲計算馬氏距離
    # SI = np.linalg.inv(S)  #協方差矩陣的逆矩陣
    # distances = np.array(distance.cdist(dataSet, [inX], 'mahalanobis', VI=SI)).reshape(-1)
    distances = np.array(distance.cdist(dataSet, [inX], "euclidean").reshape(-1))
    sortedDistIndicies = distances.argsort()  # 取排序的索引，用於label排序
    classCount = {}
    for i in range(k):  # 訪問距離最近的五個實例
        voteILabel = labels[sortedDistIndicies[i]]
        classCount[voteILabel] = classCount.get(voteILabel, 0) + 1
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )
    return sortedClassCount[0][0]  # 取最多的分類


print(x_test)
print(len(x_test))

ret = [classify(x_test[i], x_train, y_train, 5) for i in range(len(x_test))]
print(ret)

print(f"計算準確率 : {accuracy_score(y_test, ret)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Min-max scaling

# 測試資料
data = np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18]])
print(data)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
cc = scaler.fit_transform(data)
print(cc)

# 計算最大值、最小值
max1 = np.max(data, axis=0)
min1 = np.min(data, axis=0)
print(max1, min1)

# Min-max scaling 計算
cc = (data - min1) / (max1 - min1)
print(cc)

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)


# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
# ((455, 30), (114, 30), (455,), (114,))

# 特徵縮放
scaler = MinMaxScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = LogisticRegression()

clf.fit(X_train_std, y_train)
"""
LogisticRegression()
In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

y_pred = clf.predict(X_test_std)
print(y_pred)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 98.25%

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 不進行特徵縮放

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.49%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 標準化(Standardization)

# 測試資料
data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
print(data)

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
cc = scaler.fit_transform(data)
print(cc)

cc = scaler.mean_
print(cc)

# 驗證

# 計算平均數、標準差
mean1 = np.mean(data, axis=0)
std1 = np.std(data, axis=0)
print(mean1, std1)

# 標準化計算
cc = (data - mean1) / std1
print(cc)

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = LogisticRegression()

clf.fit(X_train_std, y_train)

# 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 不進行特徵縮放

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 92.98%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# MaxAbsScaler
# 簡單測試

# 測試資料

data = np.array([[1.0, -1.0, 2.0], [2.0, 0.0, 0.0], [0.0, 1.0, -1.0]])
print(data)

from sklearn.preprocessing import MaxAbsScaler

scaler = MaxAbsScaler()
cc = scaler.fit_transform(data)
print(cc)

# 驗證

# 計算最大值
max1 = np.max(data, axis=0)

# MaxAbsScaler計算
cc = data / max1
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)
# ((455, 30), (114, 30), (455,), (114,))

# 特徵縮放
scaler = MaxAbsScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = LogisticRegression()

clf.fit(X_train_std, y_train)

# 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 96.49%

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 不進行特徵縮放

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

from sklearn.preprocessing import RobustScaler

scaler = RobustScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

clf = LogisticRegression()

clf.fit(X_train_std, y_train)

y_pred = clf.predict(X_test_std)
print(y_pred)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 95.61%

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 不進行特徵縮放

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 94.74%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# roc_breast_cancer

# 實作乳癌診斷，並繪製ROC曲線

breast_cancer = datasets.load_breast_cancer()

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    breast_cancer.data[:, :6], breast_cancer.target, test_size=0.20
)

# 特徵縮放
pipe = make_pipeline(sklearn.preprocessing.StandardScaler(), SVC(probability=True))

pipe.fit(X_train, y_train)  # 學習訓練.fit

# 模型預測
y_pred_proba = pipe.predict_proba(X_test)
cc = np.around(y_pred_proba, 2)
print(cc)

# 預測值(第2欄)與實際值合併

df = pd.DataFrame({"predict": np.around(y_pred_proba[:, 1], 2), "actual": y_test})
print(df)

# 依預測值降冪排序

df2 = df.sort_values(by="predict", ascending=False)
print(df2)

# 繪製ROC曲線

from sklearn.metrics import roc_curve, roc_auc_score, auc

fpr, tpr, threshold = roc_curve(df["actual"], df["predict"])
auc1 = auc(fpr, tpr)
plt.title("ROC 曲線")
plt.plot(fpr, tpr, color="orange", label="AUC = %0.2f" % auc1)
plt.legend(loc="lower right")
plt.plot([0, 1], [0, 1], "r--")
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel("真陽率")
plt.xlabel("偽陽率")
show()

cc = roc_auc_score(df2.actual, df2.predict)
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# majority_voting
# 多數決演算法(VotingClassifier)測試

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

from sklearn.ensemble import VotingClassifier
from sklearn.naive_bayes import GaussianNB

estimators = [("svc", SVC()), ("rf", RandomForestClassifier()), ("nb", GaussianNB())]

clf = VotingClassifier(estimators)

clf.fit(X_train_std, y_train)  # 學習訓練.fit

"""
VotingClassifier(estimators=[('svc', SVC()), ('rf', RandomForestClassifier()),
                             ('nb', GaussianNB())])
"""

print("計算準確率 :")
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")

print("決定係數R2(R-squared) :", clf.score(X_test_std, y_test))

# 97.37%

# 個別模型評估

svc = SVC()

svc.fit(X_train_std, y_train)  # 學習訓練.fit

print(f"{svc.score(X_test_std, y_test)*100:.2f}%")
# 98.25%

print("決定係數R2(R-squared) :", svc.score(X_test_std, y_test))

rf = RandomForestClassifier()

rf.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{rf.score(X_test_std, y_test)*100:.2f}%")
# 98.25%

print("決定係數R2(R-squared) :", rf.score(X_test_std, y_test))

nb = GaussianNB()

nb.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")
# 93.86%

print("決定係數R2(R-squared) :", nb.score(X_test_std, y_test))

# 模型預測
cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證
scores = cross_val_score(estimator=clf, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.91666667 1.         0.91666667 0.91666667 0.90909091 1.
 0.90909091 0.90909091 1.         1.        ]
平均值: 0.95, 標準差: 0.04
"""

scores = cross_val_score(estimator=svc, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.91666667 1.         0.91666667 1.         0.90909091 1.
 0.90909091 0.90909091 1.         1.        ]
平均值: 0.96, 標準差: 0.04
"""

scores = cross_val_score(estimator=rf, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.91666667 0.91666667 0.91666667 1.         1.
 1.         1.         1.         1.        ]
平均值: 0.96, 標準差: 0.06
"""

scores = cross_val_score(estimator=nb, X=X_test_std, y=y_test, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [1.         1.         0.91666667 0.91666667 0.90909091 1.
 0.81818182 0.90909091 1.         1.        ]
平均值: 0.95, 標準差: 0.06
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# bagging_classifier

# Bagging演算法測試

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
scaler = sklearn.preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB

base_estimator = GaussianNB()

clf = BaggingClassifier(base_estimator, n_estimators=50)

clf.fit(X_train_std, y_train)  # 學習訓練.fit

print("計算準確率")
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")
# 90.35%

print("決定係數R2(R-squared) :", clf.score(X_test_std, y_test))

# 個別模型評估
nb = GaussianNB()

nb.fit(X_train_std, y_train)  # 學習訓練.fit
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")
# 90.35%

print("決定係數R2(R-squared) :", nb.score(X_test_std, y_test))

# 模型預測
cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證
clf2 = BaggingClassifier(base_estimator, n_estimators=50)
scores = cross_val_score(estimator=clf2, X=X_test_std, y=y_test, cv=10, n_jobs=-1)

print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.75       0.91666667 0.83333333 0.90909091 0.90909091
 1.         1.         0.90909091 1.        ]
平均值: 0.91, 標準差: 0.08
"""
scores = cross_val_score(
    estimator=GaussianNB(), X=X_test_std, y=y_test, cv=10, n_jobs=-1
)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.83333333 0.66666667 0.91666667 0.83333333 0.81818182 0.90909091
 1.         1.         0.90909091 1.        ]
平均值: 0.89, 標準差: 0.10
"""
# 生成隨機分類資料
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    flip_y=0.3,
    random_state=9487,
    shuffle=False,
)

# BaggingClassifier 交叉驗證
base_estimator = GaussianNB()
clf3 = BaggingClassifier(base_estimator)
scores = cross_val_score(estimator=clf3, X=X, y=y, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.63 0.89 0.91 0.92 0.53 0.57 0.82 0.73 0.79 0.56]
平均值: 0.73, 標準差: 0.14
"""
scores = cross_val_score(estimator=base_estimator, X=X, y=y, cv=10, n_jobs=-1)
print(f"K折分數: %s" % scores)
print(f"平均值: {np.mean(scores):.2f}, 標準差: {np.std(scores):.2f}")
"""
K折分數: [0.63 0.89 0.9  0.93 0.54 0.58 0.82 0.72 0.79 0.56]
平均值: 0.74, 標準差: 0.14
"""

# 參數調校

# explore bagging ensemble k for knn effect on performance
from numpy import mean
from numpy import std
from sklearn.model_selection import RepeatedStratifiedKFold


# get the dataset
def get_dataset():
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        random_state=9487,
    )
    return X, y


# get a list of models to evaluate
def get_models():
    models = dict()
    # evaluate k values from 1 to 20
    for i in range(1, 21):
        # define the base model
        base = KNeighborsClassifier(n_neighbors=i)
        # define the ensemble model
        models[str(i)] = BaggingClassifier(base)
    return models


# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
    # define the evaluation procedure
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=9487)
    # evaluate the model and collect the results
    scores = cross_val_score(model, X, y, scoring="accuracy", cv=cv, n_jobs=-1)
    return scores


# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    # evaluate the model
    scores = evaluate_model(model, X, y)
    # store the results
    results.append(scores)
    names.append(name)
    # summarize the performance along the way
    print(">%s %.3f (%.3f)" % (name, mean(scores), std(scores)))
# plot model performance for comparison
plt.boxplot(results, labels=names, showmeans=True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# adaboost_from_scratch

# 自行開發Adaboost

X, y = datasets.load_breast_cancer(return_X_y=True)

y[y == 0] = -1
# X, y = datasets.make_hastie_10_2()
print(y)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立Adaboost模型


# 計算錯誤率
def get_error_rate(pred, Y):
    return sum(pred != Y) / float(len(Y))


# Adaboost模型
def Adaboost(Y_train, X_train, Y_test, X_test, M, clf):
    n_train, n_test = len(X_train), len(X_test)
    # 初始化權重(weights)，每一筆資料權重都一樣
    w = np.ones(n_train) / n_train
    # 預測初始值為 0
    pred_train, pred_test = [np.zeros(n_train), np.zeros(n_test)]

    # 訓練 M 次
    for i in range(M):
        # 訓練
        clf.fit(X_train, Y_train, sample_weight=w)  # 學習訓練.fit
        pred_train_i = clf.predict(X_train)
        pred_test_i = clf.predict(X_test)

        # 更新權重，預測正確為 1，預測錯誤為 -1
        miss = [int(x) for x in (pred_train_i != Y_train)]
        miss2 = [x if x == 1 else -1 for x in miss]
        # 計算分類錯誤率
        err_m = np.dot(w, miss) / sum(w)
        # 計算 θ
        theta_m = 0.5 * np.log((1 - err_m) / float(err_m))
        # 權重更新
        w = np.multiply(w, np.exp([float(x) * theta_m for x in miss2]))
        # 累加至預測值
        pred_train = [
            sum(x) for x in zip(pred_train, [x * theta_m for x in pred_train_i])
        ]
        pred_test = [sum(x) for x in zip(pred_test, [x * theta_m for x in pred_test_i])]

    # np.sign：returns -1 if x < 0, 0 if x==0, 1 if x > 0
    pred_train, pred_test = np.sign(pred_train), np.sign(pred_test)
    # 回傳訓練及測試資料的錯誤率
    return get_error_rate(pred_train, Y_train), get_error_rate(pred_test, Y_test)


# max_depth 一定要設定
weak_learner = DecisionTreeClassifier(max_depth=3)
pred = Adaboost(y_train, X_train, y_test, X_test, 50, weak_learner)

# 模型評估

# 計算準確率
print(f"{(1-pred[1])*100:.2f}%")
# 97.37%

# 個別模型評估
weak_learner.fit(X_train, y_train)  # 學習訓練.fit
print(f"{weak_learner.score(X_test, y_test)*100:.2f}%")
# 93.86%

print("決定係數R2(R-squared) :", weak_learner.score(X_test, y_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 堆疊(Stacking)測試

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import StackingClassifier


def get_models():
    models = []
    models.append(("knn", KNeighborsClassifier()))
    models.append(("cart", DecisionTreeClassifier()))
    models.append(("svm", SVC()))
    models.append(("bayes", GaussianNB()))
    return models


estimators = get_models()

model = StackingClassifier(estimators=estimators, final_estimator=LogisticRegression())

model.fit(X_train, y_train)  # 學習訓練.fit

# 模型評估
scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# shapley_value_from_scratch

# 自行計算 Shapley value
# How to calculate shapley values from scratch

X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放
clf = make_pipeline(sklearn.preprocessing.StandardScaler(), LogisticRegression())

clf.fit(X_train.values, y_train)  # 學習訓練.fit

# 自行計算第16個特徵的Shapley value

x = X_test.iloc[0]  # 第一筆測試資料
j = 15  # 第16個特徵
M = 1000  # 測試 1000 次
n_features = len(x)
marginal_contributions = []
feature_idxs = list(range(n_features))
feature_idxs.remove(j)
for _ in range(M):
    # 抽樣訓練資料一筆資料
    z = X_train.sample(1).values[0]
    # 所有組合
    x_idx = random.sample(
        feature_idxs,
        min(
            max(int(0.2 * n_features), random.choice(feature_idxs)),
            int(0.8 * n_features),
        ),
    )
    z_idx = [idx for idx in feature_idxs if idx not in x_idx]

    # 含第16個特徵的X，在組合內以測試資料填入，不在組合內以訓練資料填入
    x_plus_j = np.array([x[i] if i in x_idx + [j] else z[i] for i in range(n_features)])
    # 不含第16個特徵的X
    x_minus_j = np.array(
        [z[i] if i in z_idx + [j] else x[i] for i in range(n_features)]
    )

    # 計算邊際貢獻(marginal contribution)
    marginal_contribution = (
        clf.predict_proba(x_plus_j.reshape(1, -1))[0][1]
        - clf.predict_proba(x_minus_j.reshape(1, -1))[0][1]
    )
    marginal_contributions.append(marginal_contribution)

# 計算邊際貢獻平均值
phi_j_x = sum(marginal_contributions) / len(marginal_contributions)
print(f"Shaply value for feature {j}: {phi_j_x:.5}")

# Shaply value for feature 15: 0.010254

cc = X.columns[j]
print(cc)

#'compactness error'

# 以 SHAP 套件驗證

import shap

explainer = shap.KernelExplainer(clf.predict_proba, X_train.values)
shap_values = explainer.shap_values(x)

""" NG
print(f"Shaply value calulated from shap: {shap_values[1][j]:.5}")
"""

# Using 455 background data samples could cause slower run times.
# Consider using shap.sample(data, K)
# or shap.kmeans(data, K) to summarize the background as K samples.

# Shaply value calulated from shap: 0.01366

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Boosting
# Adaboost Classifier

breast_cancer = datasets.load_breast_cancer()

x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# 資料分割
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y)

clf_boosting = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), n_estimators=200)
clf_boosting.fit(train_x, train_y)
predictions = clf_boosting.predict(test_x)
print(
    "For Boosting : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions), 2),
        round(accuracy_score(test_y, predictions), 2),
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Random Forest as a bagging classifier

breast_cancer = datasets.load_breast_cancer()
x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)
# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# 資料分割
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y)

clf_bagging = RandomForestClassifier(n_estimators=200, max_depth=1)
clf_bagging.fit(train_x, train_y)
predictions = clf_bagging.predict(test_x)
print(
    "For Bagging : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions), 2),
        round(accuracy_score(test_y, predictions), 2),
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Stacking
breast_cancer = datasets.load_breast_cancer()

x = pd.DataFrame(breast_cancer.data, columns=breast_cancer.feature_names)
y = pd.Categorical.from_codes(breast_cancer.target, breast_cancer.target_names)

# Transforming string Target to an int
encoder = LabelEncoder()
binary_encoded_y = pd.Series(encoder.fit_transform(y))

# 資料分割
train_x, test_x, train_y, test_y = train_test_split(x, binary_encoded_y)

boosting_clf_ada_boost = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), n_estimators=3
)

bagging_clf_rf = RandomForestClassifier(
    n_estimators=200, max_depth=1, random_state=9487
)

clf_rf = RandomForestClassifier(n_estimators=200, max_depth=1, random_state=9487)

clf_ada_boost = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1, random_state=9487), n_estimators=3
)

clf_logistic_reg = LogisticRegression(solver="liblinear", random_state=9487)


# Customizing and Exception message
class NumberOfClassifierException(Exception):
    pass


# Creating a stacking class
class Stacking:

    """
    This is a test class for stacking !
    Please fill Free to change it to fit your needs
    We suppose that at least the First N-1 Classifiers have
    a predict_proba function.
    """

    def __init__(self, classifiers):
        if len(classifiers) < 2:
            raise numberOfClassifierException(
                "You must fit your classifier with 2 classifiers at least"
            )
        else:
            self._classifiers = classifiers

    def fit(self, data_x, data_y):
        stacked_data_x = data_x.copy()
        for classfier in self._classifiers[:-1]:
            classfier.fit(data_x, data_y)
            stacked_data_x = np.column_stack(
                (stacked_data_x, classfier.predict_proba(data_x))
            )

        last_classifier = self._classifiers[-1]
        last_classifier.fit(stacked_data_x, data_y)

    def predict(self, data_x):
        stacked_data_x = data_x.copy()
        for classfier in self._classifiers[:-1]:
            prob_predictions = classfier.predict_proba(data_x)
            stacked_data_x = np.column_stack((stacked_data_x, prob_predictions))

        last_classifier = self._classifiers[-1]
        return last_classifier.predict(stacked_data_x)


bagging_clf_rf.fit(train_x, train_y)
boosting_clf_ada_boost.fit(train_x, train_y)

classifers_list = [clf_rf, clf_ada_boost, clf_logistic_reg]
clf_stacking = Stacking(classifers_list)
clf_stacking.fit(train_x, train_y)

predictions_bagging = bagging_clf_rf.predict(test_x)
predictions_boosting = boosting_clf_ada_boost.predict(test_x)
predictions_stacking = clf_stacking.predict(test_x)

print(
    "For Bagging : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_bagging), 2),
        round(accuracy_score(test_y, predictions_bagging), 2),
    )
)
print(
    "For Boosting : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_boosting), 2),
        round(accuracy_score(test_y, predictions_boosting), 2),
    )
)
print(
    "For Stacking : F1 Score {}, Accuracy {}".format(
        round(f1_score(test_y, predictions_stacking), 2),
        round(accuracy_score(test_y, predictions_stacking), 2),
    )
)

"""
Comparaison
Metric 	Bagging 	Boosting 	Stacking
Accuracy 	0.90 	0.94 	0.98
F1-Score 	0.88 	0.93 	0.98
"""

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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
