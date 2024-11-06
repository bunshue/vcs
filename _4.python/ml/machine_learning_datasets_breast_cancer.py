"""
breast_cancer


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
import seaborn as sns

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.datasets import load_breast_cancer

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""

#乳癌診斷預測
ds = datasets.load_breast_cancer()
"""

#學習分類

data = load_breast_cancer()

X = data.data
y = data.target

X = X[:, :10]

from sklearn.linear_model import LogisticRegression
logistic_regression = LogisticRegression()
logistic_regression.fit(X, y)

y_pred = logistic_regression.predict(X)

from sklearn.metrics import accuracy_score
accuracy_score(y, y_pred)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 學習分類
data = load_breast_cancer()
X = data.data
y = 1 - data.target
# ラベルの0と1を反転

X = X[:, :10]
from sklearn.linear_model import LogisticRegression

logistic_regression = LogisticRegression()
logistic_regression.fit(X, y)
y_pred = logistic_regression.predict(X)



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cancer = load_breast_cancer()

X = cancer.data
y = cancer.target
print(
    "data shape: {0}; no. positive: {1}; no. negative: {2}".format(
        X.shape, y[y == 1].shape[0], y[y == 0].shape[0]
    )
)
print(cancer.data[0])

print(cancer.feature_names)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(solver="liblinear")
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print(
    "train score: {train_score:.6f}; test score: {test_score:.6f}".format(
        train_score=train_score, test_score=test_score
    )
)

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

from sklearn.linear_model import LogisticRegression
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
print(
    "耗時 : {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}".format(
        time.time() - start, train_score, cv_score
    )
)

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

plt.show()

print("------------------------------")	#30個

import warnings

warnings.filterwarnings("ignore")

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

cancer = load_breast_cancer()
X = cancer.data
y = cancer.target
print(
    "data shape: {0}; no. positive: {1}; no. negative: {2}".format(
        X.shape, y[y == 1].shape[0], y[y == 0].shape[0]
    )
)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


print("高斯核函數")

from sklearn.svm import SVC

clf = SVC(C=1.0, kernel="rbf", gamma=0.1)

clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

from common.utils import plot_param_curve
from sklearn.model_selection import GridSearchCV

gammas = np.linspace(0, 0.0003, 30)
param_grid = {"gamma": gammas}
clf = GridSearchCV(SVC(), param_grid, cv=5)
# clf = GridSearchCV(SVC(), param_grid, cv=5, scoring='roc_auc',n_jobs=-1)

clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

# 有錯誤
# plt.figure(figsize=(10, 4), dpi=144)
# plot_param_curve(plt, gammas, clf.cv_results_, xlabel='gamma')
# plt.show()

print("------------------------------")	#30個

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

plt.show()

print("------------------------------")	#30個

print("多項式核函數")

from sklearn.svm import SVC

clf = SVC(C=1.0, kernel="poly", degree=2)

clf.fit(X_train, y_train)

train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

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

plt.show()

print("------------------------------")	#30個

print("多項式 LinearSVC")

from sklearn.svm import LinearSVC
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
print("train score: {0}; test score: {1}".format(train_score, test_score))

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

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Non-linear models
=================

Here we focuse on non-linear models for classification. Nevertheless, each
classification model has its regression counterpart.
"""

from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler

from sklearn import metrics
from sklearn.model_selection import train_test_split

np.set_printoptions(precision=2)
#pd.set_option('precision', 2)

# Support Vector Machines (SVM)

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.5, stratify=y, random_state=42)

# %%
# Preprocessing: unequal variance of input features, requires scaling for svm.

ax = sns.displot(x=X_train.std(axis=0), kind="kde", bw_adjust=.2, cut=0,
                 fill=True, height=3, aspect=1.5,)
_ = ax.set_xlabels("Std-dev").tight_layout()

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# %%
# Fit-predict
# Probalility is a logistic of the decision_function

svm = SVC(kernel='rbf', probability=True).fit(X_train, y_train)
y_pred = svm.predict(X_test)
y_score = svm.decision_function(X_test)
y_prob = svm.predict_proba(X_test)[:, 1]

ax = sns.relplot(x=y_score, y=y_prob, hue=y_pred, height=2, aspect=1.5)
_ = ax.set_axis_labels("decision function", "Probability").tight_layout()

# %% Scores

print("bAcc: %.2f, AUC: %.2f (AUC with proba: %.2f)" % (
      metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
      metrics.roc_auc_score(y_true=y_test, y_score=y_score),
      metrics.roc_auc_score(y_true=y_test, y_score=y_prob)))

# Usefull internals: indices of support vectors within original X
np.all(X_train[svm.support_, :] == svm.support_vectors_)



from sklearn.ensemble import RandomForestClassifier

forest = RandomForestClassifier(n_estimators = 100)
forest.fit(X_train, y_train)

y_pred = forest.predict(X_test)
y_prob = forest.predict_proba(X_test)[:, 1]


# %% Scores

print("bAcc: %.2f, AUC: %.2f " % (
      metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
      metrics.roc_auc_score(y_true=y_test, y_score=y_prob)))

# %%
# Extra Trees (Low Variance)
#
# Extra Trees is like Random Forest, in that it builds multiple trees and splits nodes using random subsets of features, but with two key differences: it does not bootstrap observations (meaning it samples without replacement), and nodes are split on random splits, not best splits. So, in summary, ExtraTrees:
# builds multiple trees with bootstrap = False by default, which means it samples without replacement
# nodes are split based on random splits among a random subset of the features selected at every node
# In Extra Trees, randomness doesn’t come from bootstrapping of data, but rather comes from the random splits of all observations.
# ExtraTrees is named for (Extremely Randomized Trees).


from sklearn.ensemble import GradientBoostingClassifier

gb = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1,
                                subsample=0.5, random_state=0)
gb.fit(X_train, y_train)

y_pred = gb.predict(X_test)
y_prob = gb.predict_proba(X_test)[:, 1]

print("bAcc: %.2f, AUC: %.2f " % (
      metrics.balanced_accuracy_score(y_true=y_test, y_pred=y_pred),
      metrics.roc_auc_score(y_true=y_test, y_score=y_prob)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("学習データと検証データに分割")

data = load_breast_cancer()
X = data.data
y = data.target
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

from sklearn.svm import SVC

model_svc = SVC()
model_svc.fit(X_train, y_train)
y_train_pred = model_svc.predict(X_train)
y_test_pred = model_svc.predict(X_test)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

from sklearn.ensemble import RandomForestClassifier

model_rfc = RandomForestClassifier()
model_rfc.fit(X_train, y_train)
y_train_pred = model_rfc.predict(X_train)
y_test_pred = model_rfc.predict(X_test)
from sklearn.metrics import accuracy_score

print(accuracy_score(y_train, y_train_pred))
print(accuracy_score(y_test, y_test_pred))

print("------------------------------")  # 30個

print("交差検証（クロスバリデーション）")

from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

cv = KFold(5, shuffle=True)

from sklearn.ensemble import RandomForestClassifier

model_rfc_1 = RandomForestClassifier()
cross_val_score(model_rfc_1, X, y, cv=cv, scoring="accuracy")

cross_val_score(model_rfc_1, X, y, cv=cv, scoring="f1")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Hyperparameter 超參數 ハイパーパラメータの探索")

data = load_breast_cancer()
X = data.data
y = 1 - data.target  # ラベルの0と1を反転
X = X[:, :10]

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
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

# 13-1-1 最近 k 鄰數量：n_neighbors

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# 取得特徵與標籤資料

dx, dy = load_breast_cancer(return_X_y=True)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-1-2 用 GridSearchCV 自動搜尋最佳 k 值

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV

dx, dy = load_breast_cancer(return_X_y=True)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx, dy, test_size=0.2, random_state=0
)

param_grid = {"n_neighbors": np.arange(10) + 1}  # 要網格搜尋的參數
model = GridSearchCV(KNeighborsClassifier(), param_grid)
model.fit(dx_train, dy_train)  # 用最佳模型來做訓練

print("Best params:", model.best_params_)  # 傳回最佳參數
print("CV score:", model.best_score_.round(3))
#print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-2-1 邏輯斯迴歸的 C：常規化強度

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)  # 資料標準化
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

cv_scores = []
test_scores = []

x = [10**n for n in range(-4, 5)]

x_str = [str(n) for n in x]  # X 軸各數值『名稱』

for c in x:
    logistic_regression = LogisticRegression(C=c, max_iter=1000).fit(dx_train, dy_train)
    cv_scores.append(cross_val_score(logistic_regression, dx_train, dy_train, cv=5).mean())
    test_scores.append(logistic_regression.score(dx_test, dy_test))

plt.title("Logistic Regression hyperparameter")
plt.plot(x_str, cv_scores, label="CV score")
plt.plot(x_str, test_scores, label="Test score")
plt.xlabel("C")
plt.ylabel("accuracy (%)")
plt.legend()
plt.grid(True)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-2-2 線性 SVC 的 C：常規化強度

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import LinearSVC

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-3-1 C, gamma 與 kernel 參數

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

dx, dy = load_breast_cancer(return_X_y=True)
dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

x = [10**n for n in range(-2, 3)]

param_grid = {"C": x, "gamma": x, "kernel": ["linear", "rbf", "poly", "sigmoid"]}

model = GridSearchCV(SVC(), param_grid)
model.fit(dx_train, dy_train)

print("Best params: ", model.best_params_)
print("CV score:", model.best_score_.round(3))
print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-3-2 使用 RandomizedSearchCV 更快速尋找較適當的參數

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.model_selection import RandomizedSearchCV

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

param_grid = {
    "C": np.linspace(1, 100, 100),
    "gamma": np.linspace(0.01, 1, 100),
    "kernel": ["linear", "rbf", "poly", "sigmoid"],
}

model = RandomizedSearchCV(SVC(), param_grid, n_iter=100)
model.fit(dx_train, dy_train)

print("Best params:", model.best_params_)
print("CV score:", model.best_score_.round(3))
print("Test score:", model.score(dx_test, dy_test).round(3))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-4-1 決策樹的最大深度：max_depth

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

dx, dy = load_breast_cancer(return_X_y=True)
feature_names = list(load_breast_cancer().feature_names)

dx_std = StandardScaler().fit_transform(dx)
dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

model = DecisionTreeClassifier(max_depth=3).fit(dx_train, dy_train)

print(export_text(model, feature_names=feature_names))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 13-4-2 隨機森林的規模 n_estimators 與亂數種子 random_state

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier

dx, dy = load_breast_cancer(return_X_y=True)

dx_std = StandardScaler().fit_transform(dx)

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("學習曲線和驗證曲線")

from sklearn.ensemble import RandomForestClassifier


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
    plt.show()


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

from sklearn import neighbors, datasets
from sklearn.model_selection import train_test_split

data = datasets.load_breast_cancer()
X = data.data  # 自變量
y = data.target  # 因變量
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)
clf = neighbors.KNeighborsClassifier(5)  # 設鄰居數爲5個
clf.fit(x_train, y_train)  # 訓練模型
print(clf.score(x_test, y_test))  # 給模型打分
print(clf.predict([x_test[0]]), y_test[0], clf.predict_proba([x_test[0]]))

print("------------------------------")	#30個

from sklearn.metrics import accuracy_score
from scipy.spatial import distance
import operator


def classify(inX, dataSet, labels, k):
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


ret = [classify(x_test[i], x_train, y_train, 5) for i in range(len(x_test))]
print(accuracy_score(y_test, ret))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Min-max scaling

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 測試資料
data = np.array([[-1, 2], [-0.5, 6], [0, 10], [1, 18]])
print(data)

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
cc = scaler.fit_transform(data)
print(cc)

# 驗證

# 計算最大值、最小值
max1 = np.max(data, axis=0)
min1 = np.min(data, axis=0)
print(max1, min1)

# Min-max scaling 計算
cc = (data - min1) / (max1 - min1)
print(cc)

# 載入資料集

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 98.25%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 96.49%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 標準化(Standardization)

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 測試資料
data = np.array([[0, 0], [0, 0], [1, 1], [1, 1]])
print(data)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
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

# 載入資料集

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

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

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)

"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""
# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 96.49%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X, y = datasets.load_iris(return_X_y=True)
X, y = datasets.load_breast_cancer(return_X_y=True)

# 3. 不須進行特徵工程

# 4. 資料分割

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

# 5. 選擇演算法

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

# 6. 模型訓練

clf.fit(X_train_std, y_train)
"""
LogisticRegression()

In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook.
On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.
"""

# 7. 模型計分

y_pred = clf.predict(X_test_std)
print(y_pred)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 95.61%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 不進行特徵縮放

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 94.74%



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
