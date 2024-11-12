"""
Scikit-learn 詳解與企業應用_機器學習最佳入門與實戰

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_01_error_rate

# 整體學習的錯誤率計算

from scipy.special import comb

# 計算整體學習的錯誤率


def ensemble_error(n_classifier, error):
    k_start = int(math.ceil(n_classifier / 2.0))
    probs = [
        comb(n_classifier, k) * error**k * (1 - error) ** (n_classifier - k)
        for k in range(k_start, n_classifier + 1)
    ]
    return sum(probs)


cc = ensemble_error(n_classifier=11, error=0.25)
print(cc)

# 0.03432750701904297

# 測試各種錯誤率，並繪圖

error_range = np.arange(0.0, 1.01, 0.01)
ens_errors = [ensemble_error(n_classifier=11, error=error) for error in error_range]

# 修正中文亂碼
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

plt.plot(error_range, ens_errors, label="整體學習", linewidth=2)

plt.plot(error_range, error_range, linestyle="--", label="個別模型", linewidth=2)

plt.title("錯誤率比較", fontsize=18)
plt.xlabel("個別模型錯誤率", fontsize=14)
plt.ylabel("整體學習錯誤率", fontsize=14)
plt.legend(loc="upper left", fontsize=14)
plt.grid(alpha=0.5)

plt.show()

""" no df
#模型訓練
model = Kmeans()
model.fit(df)

#預測
cc = model.predict(10)
print(cc)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_02_majority_voting
# 多數決演算法(VotingClassifier)測試

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.naive_bayes import GaussianNB

estimators = [("svc", SVC()), ("rf", RandomForestClassifier()), ("nb", GaussianNB())]
clf = VotingClassifier(estimators)
clf.fit(X_train_std, y_train)

"""
VotingClassifier(estimators=[('svc', SVC()), ('rf', RandomForestClassifier()),
                             ('nb', GaussianNB())])
"""

# 模型評估

# 計算準確率
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")

# 97.37%

# 個別模型評估

svc = SVC()
svc.fit(X_train_std, y_train)
print(f"{svc.score(X_test_std, y_test)*100:.2f}%")

# 98.25%

rf = RandomForestClassifier()
rf.fit(X_train_std, y_train)
print(f"{rf.score(X_test_std, y_test)*100:.2f}%")

# 98.25%

nb = GaussianNB()
nb.fit(X_train_std, y_train)
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")

# 93.86%

# 模型預測

cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證

from sklearn.model_selection import cross_val_score

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

# 10_03_bagging_classifier

# Bagging演算法測試

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 模型訓練

from sklearn.ensemble import BaggingClassifier
from sklearn.naive_bayes import GaussianNB

base_estimator = GaussianNB()
clf = BaggingClassifier(estimator=base_estimator, n_estimators=50)
clf.fit(X_train_std, y_train)

"""
BaggingClassifier(estimator=GaussianNB(), n_estimators=50)
"""

# 模型評估

# 計算準確率
print(f"{clf.score(X_test_std, y_test)*100:.2f}%")

# 90.35%

# 個別模型評估

nb = GaussianNB()
nb.fit(X_train_std, y_train)
print(f"{nb.score(X_test_std, y_test)*100:.2f}%")

# 90.35%

# 模型預測

cc = clf.predict(X_test_std)
print(cc)

# 交叉驗證

from sklearn.model_selection import cross_val_score

clf2 = BaggingClassifier(estimator=base_estimator, n_estimators=50)
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

# 使用較複雜的資料集

from sklearn.datasets import make_classification

# 生成隨機分類資料
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    flip_y=0.3,
    random_state=5,
    shuffle=False,
)

# BaggingClassifier 交叉驗證
base_estimator = GaussianNB()
clf3 = BaggingClassifier(estimator=base_estimator)
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
from sklearn.neighbors import KNeighborsClassifier


# get the dataset
def get_dataset():
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=15, n_redundant=5, random_state=5
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
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
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
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_04_adaboost_from_scratch

# 自行開發Adaboost

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

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
        clf.fit(X_train, Y_train, sample_weight=w)
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


# 模型訓練

from sklearn.tree import DecisionTreeClassifier

# max_depth 一定要設定
weak_learner = DecisionTreeClassifier(max_depth=3)
pred = Adaboost(y_train, X_train, y_test, X_test, 50, weak_learner)

# 模型評估

# 計算準確率
print(f"{(1-pred[1])*100:.2f}%")

# 97.37%

# 個別模型評估

weak_learner.fit(X_train, y_train)
print(f"{weak_learner.score(X_test, y_test)*100:.2f}%")

# 93.86%


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_05_scikit-learn_adaBoost

# Bagging演算法測試

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import learning_curve

from sklearn.datasets import load_digits

# 載入資料集

dataset = load_digits()
X = dataset["data"]
y = dataset["target"]

plt.imshow(X[4].reshape(8, 8))
plt.show()

# 個別模型評估

clf = DecisionTreeClassifier()
scores_ada = cross_val_score(clf, X, y, cv=6)
cc = scores_ada.mean()
print(cc)

# 0.7952173913043478

# AdaBoost模型評估

clf = AdaBoostClassifier(DecisionTreeClassifier())
scores_ada = cross_val_score(clf, X, y, cv=6)
cc = scores_ada.mean()
print(cc)

# 0.8019435154217764

clf.fit(X, y)
cc = clf.estimator_errors_
print(cc)

cc = clf.estimator_weights_
print(cc)

score = []
for depth in [1, 2, 10]:
    clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=depth))
    scores_ada = cross_val_score(clf, X, y, cv=6)
    score.append(scores_ada.mean())
print(score)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_06_gradient_boost

# 自行開發『梯度提升決策樹』(Gradient Boosting Decision Tree)

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 建立Gradient Boost模型

from sklearn.tree import DecisionTreeRegressor


class GradientBooster:
    # 初始化
    def __init__(
        self,
        max_depth=8,
        min_samples_split=5,
        min_samples_leaf=5,
        max_features=3,
        lr=0.1,
        num_iter=1000,
    ):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.min_samples_leaf = min_samples_leaf
        self.max_features = max_features
        self.lr = lr
        self.num_iter = num_iter
        self.y_mean = 0

    # 計算 MSE
    def __calculate_loss(self, y, y_pred):
        loss = (1 / len(y)) * 0.5 * np.sum(np.square(y - y_pred))
        return loss

    # 計算梯度
    def __take_gradient(self, y, y_pred):
        grad = -(y - y_pred)
        return grad

    # 單一模型訓練
    def __create_base_model(self, X, y):
        base = DecisionTreeRegressor(
            criterion="squared_error",
            max_depth=self.max_depth,
            min_samples_split=self.min_samples_split,
            min_samples_leaf=self.min_samples_leaf,
            max_features=self.max_features,
        )
        base.fit(X, y)
        return base

    # 預測
    def predict(self, models, X):
        pred_0 = np.array([self.y_mean] * X.shape[0])
        pred = pred_0  # .reshape(len(pred_0),1)

        # 加法模型預測
        for i in range(len(models)):
            temp = models[i].predict(X)
            pred -= self.lr * temp

        return pred

    # 模型訓練
    def train(self, X, y):
        models = []
        losses = []
        self.y_mean = np.mean(y)
        pred = np.array([np.mean(y)] * len(y))

        # 加法模型訓練
        for epoch in range(self.num_iter):
            loss = self.__calculate_loss(y, pred)
            losses.append(loss)
            grads = self.__take_gradient(y, pred)
            base = self.__create_base_model(X, grads)
            r = base.predict(X)
            pred -= self.lr * r
            models.append(base)

        return models, losses, pred


# 模型訓練

G = GradientBooster()
models, losses, pred = G.train(X_train, y_train)

# 繪製損失函數

import seaborn as sns

sns.set_style("darkgrid")
ax = sns.lineplot(x=range(1000), y=losses)
ax.set(xlabel="Epoch", ylabel="Loss", title="Loss vs Epoch")
plt.show()

# 模型評估

from sklearn.metrics import mean_squared_error

y_pred = G.predict(models, X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 62.47630199377564

# 個別模型評估

model = DecisionTreeRegressor(
    max_depth=8, min_samples_split=5, min_samples_leaf=5, max_features=3
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 75.54768636162939

# Scikit-learn GradientBoostingRegressor 模型評估

from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor(
    n_estimators=1000,
    criterion="squared_error",
    max_depth=8,
    min_samples_split=5,
    min_samples_leaf=5,
    max_features=3,
)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

# RMSE: 60.69114783838949

# Scikit-learn GradientBoostingClassifier 模型評估

from sklearn.datasets import make_hastie_10_2
from sklearn.ensemble import GradientBoostingClassifier

X, y = make_hastie_10_2(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

clf = GradientBoostingClassifier(
    n_estimators=100, learning_rate=1.0, max_depth=1, random_state=0
).fit(X_train, y_train)
cc = clf.score(X_test, y_test)
print(cc)

# 0.9229166666666667

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_07_xgboost

# XGBoost測試

#!pip install xgboost -U

"""
Requirement already satisfied: xgboost in c:\anaconda3\lib\site-packages (1.6.1)
Collecting xgboost
  Downloading xgboost-1.7.3-py3-none-win_amd64.whl (89.1 MB)
     ---------------------------------------- 89.1/89.1 MB 8.7 MB/s eta 0:00:00
Requirement already satisfied: numpy in c:\anaconda3\lib\site-packages (from xgboost) (1.23.5)
Requirement already satisfied: scipy in c:\anaconda3\lib\site-packages (from xgboost) (1.9.3)
Installing collected packages: xgboost
  Attempting uninstall: xgboost
    Found existing installation: xgboost 1.6.1
    Uninstalling xgboost-1.6.1:
      Successfully uninstalled xgboost-1.6.1
Successfully installed xgboost-1.7.3

"""

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from xgboost import XGBRegressor

model = XGBRegressor()
model.fit(X_train, y_train)

"""
XGBRegressor(base_score=None, booster=None, callbacks=None,
             colsample_bylevel=None, colsample_bynode=None,
             colsample_bytree=None, early_stopping_rounds=None,
             enable_categorical=False, eval_metric=None, feature_types=None,
             gamma=None, gpu_id=None, grow_policy=None, importance_type=None,
             interaction_constraints=None, learning_rate=None, max_bin=None,
             max_cat_threshold=None, max_cat_to_onehot=None,
             max_delta_step=None, max_depth=None, max_leaves=None,
             min_child_weight=None, missing=nan, monotone_constraints=None,
             n_estimators=100, n_jobs=None, num_parallel_tree=None,
             predictor=None, random_state=None, ...)
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10, scoring="neg_mean_squared_error")
print(scores)

# 平均分數與標準差

print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -5473.1857409034155, 標準差: 3004.388074594913


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用分類模型

from xgboost import XGBClassifier

X, y = datasets.load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = XGBClassifier()
model.fit(X_train, y_train)
scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.9484848484848485, 標準差: 0.05626498372008225

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10_08_stacking
# 堆疊(Stacking)測試

from sklearn import datasets
from sklearn.model_selection import train_test_split

# 載入資料集

X, y = datasets.load_breast_cancer(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
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

model.fit(X_train, y_train)

"""
StackingClassifier(estimators=[('knn', KNeighborsClassifier()),
                               ('cart', DecisionTreeClassifier()),
                               ('svm', SVC()), ('bayes', GaussianNB())],
                   final_estimator=LogisticRegression())
"""

# 模型評估

from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.9303030303030303, 標準差: 0.08393720596645175


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 使用迴歸模型

from sklearn.linear_model import RidgeCV
from sklearn.svm import LinearSVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import StackingRegressor
from sklearn.preprocessing import StandardScaler

X, y = datasets.load_diabetes(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

estimators = [("lr", RidgeCV()), ("svr", LinearSVR(random_state=42))]

model = StackingRegressor(
    estimators=estimators,
    final_estimator=RandomForestRegressor(n_estimators=10, random_state=42),
)
model.fit(X_train_std, y_train)
scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()
svc.fit(X_train_std, y_train)
scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
