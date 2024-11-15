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

from sklearn import datasets
from sklearn.model_selection import train_test_split

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
print("------------------------------------------------------------")  # 60個

# 11_01_self_training

# 自我訓練(Self-training)測試

from sklearn.svm import SVC
from sklearn.semi_supervised import SelfTrainingClassifier

# 載入資料集

X, y = datasets.load_iris(return_X_y=True)
X = X[:, :2]

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 設定 30% 資料為沒有標註(-1)

rng = np.random.RandomState(0)
y_rand = rng.rand(y_train.shape[0])
y_30 = np.copy(y_train)
y_30[y_rand < 0.3] = -1
cc = np.count_nonzero(y_30 == -1)
print(cc)

y_30_index = np.where(y_30 == -1)[0]
print(y_30_index)

print(type(y_30_index))

# 模型訓練

base_classifier = SVC(kernel="rbf", gamma=0.5, probability=True)
clf = SelfTrainingClassifier(base_classifier).fit(X_train, y_30)

# 繪製決策邊界

# 建立 mesh grid
x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

# 每個標籤不同顏色(RGB)
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# 繪製等高線
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
plt.axis("off")

# 繪製實際點
colors = [color_map[y] for y in y_30]
plt.scatter(X_train[:, 0], X_train[:, 1], c=colors, edgecolors="black")

plt.show()

# SVM 模型評估

base_classifier.fit(X_train, y_30)
cc = base_classifier.score(X_test, y_test)
print(cc)

# 0.6666666666666666

# Self-training 模型評估

cc = clf.score(X_test, y_test)
print(cc)

# 0.7666666666666667


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 完整資料進行模型評估

rng = np.random.RandomState(42)
X, y = datasets.load_iris(return_X_y=True)
random_unlabeled_points = rng.rand(y.shape[0]) < 0.3
y[random_unlabeled_points] = -1

svc = SVC(probability=True, gamma="auto")
self_training_model = SelfTrainingClassifier(svc)
self_training_model.fit(X, y)

"""
SelfTrainingClassifier(base_estimator=SVC(gamma='auto', probability=True))
"""

svc.fit(X[y >= 0], y[y >= 0])
cc = svc.score(X, y)
print(cc)

# 0.66

X, y = datasets.load_iris(return_X_y=True)
cc = self_training_model.score(X, y)
print(cc)

# 0.9733333333333334

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_02_label_propagation

# 標註傳播(Label propagation)測試

import numpy as np
from sklearn.datasets import make_classification
from sklearn.semi_supervised import LabelPropagation

# 載入資料集

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=1
)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1, stratify=y
)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)

# (500,)

# Label propagation 模型訓練與評估

clf = LabelPropagation()
clf.fit(X_train_mixed, y_train_mixed)
cc = clf.score(X_test, y_test)
print(cc)

# 0.856

# LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()
clf2.fit(X_train_lab, y_train_lab)
cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依Label propagation傳播結果進行模型訓練與評估

clf3 = LogisticRegression()
clf3.fit(X_train_mixed, tran_labels)
cc = clf3.score(X_test, y_test)
print(cc)
# 0.862

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_03_label_spreading

# LabelSpreading 測試

import numpy as np
from sklearn.datasets import make_classification
from sklearn.semi_supervised import LabelSpreading

# 載入資料集

X, y = make_classification(
    n_samples=1000, n_features=2, n_informative=2, n_redundant=0, random_state=1
)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=1, stratify=y
)

# 設定 50% 資料為沒有標註(-1)

X_train_lab, X_test_unlab, y_train_lab, y_test_unlab = train_test_split(
    X_train, y_train, test_size=0.5, random_state=1, stratify=y_train
)
X_train_mixed = np.concatenate((X_train_lab, X_test_unlab))
nolabel = [-1 for _ in range(len(y_test_unlab))]
y_train_mixed = np.concatenate((y_train_lab, nolabel))
cc = y_train_mixed.shape
print(cc)
# (500,)

# LabelSpreading 模型訓練與評估

clf = LabelSpreading()
clf.fit(X_train_mixed, y_train_mixed)
cc = clf.score(X_test, y_test)
print(cc)
# 0.854

# LogisticRegression 模型訓練與評估

from sklearn.linear_model import LogisticRegression

clf2 = LogisticRegression()
clf2.fit(X_train_lab, y_train_lab)
cc = clf2.score(X_test, y_test)
print(cc)

# 0.848

# 取得訓練資料標註

tran_labels = clf.transduction_
cc = tran_labels.shape
print(cc)
# (500,)

# 再依LabelSpreading傳播結果進行模型訓練與評估

clf3 = LogisticRegression()
clf3.fit(X_train_mixed, tran_labels)
cc = clf3.score(X_test, y_test)
print(cc)

# 0.858

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_04_label_propagation_digits_active_learning

# Label Propagation digits active learning

from scipy import stats
from sklearn.semi_supervised import LabelSpreading
from sklearn.metrics import classification_report, confusion_matrix

# 載入資料集

digits = datasets.load_digits()
rng = np.random.RandomState(0)
indices = np.arange(len(digits.data))
rng.shuffle(indices)

# 取前 330 筆資料
X = digits.data[indices[:330]]
y = digits.target[indices[:330]]
images = digits.images[indices[:330]]

# 參數設定
n_total_samples = len(y)
n_labeled_points = 40  # 初始取40筆標註資料
max_iterations = 5  # 5 個執行週期

unlabeled_indices = np.arange(n_total_samples)[n_labeled_points:]
cc = len(unlabeled_indices)
print(cc)

# Label propagation 模型訓練與評估

f = plt.figure()
for i in range(max_iterations):
    y_train = np.copy(y)
    y_train[unlabeled_indices] = -1

    # LabelSpreading 模型訓練
    lp_model = LabelSpreading(gamma=0.25, max_iter=20)
    lp_model.fit(X, y_train)

    # 預測
    predicted_labels = lp_model.transduction_[unlabeled_indices]
    true_labels = y[unlabeled_indices]

    print(f"Iteration {i} {70 * '_'}")
    print(
        f"Label Spreading model: {n_labeled_points} labeled & "
        + f"{n_total_samples - n_labeled_points} unlabeled ({n_total_samples} total)"
    )

    if i == 0 or i == max_iterations - 1:
        print(classification_report(true_labels, predicted_labels))

    print("Confusion matrix")
    cm = confusion_matrix(true_labels, predicted_labels, labels=lp_model.classes_)
    print(cm)

    # 計算熵，以找出最不確定的五筆資料
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[
        np.in1d(uncertainty_index, unlabeled_indices)
    ][:5]

    # 記錄最不確定的五筆資料
    delete_indices = np.array([], dtype=int)
    f.text(
        0.05,
        (1 - (i + 1) * 0.183),
        f"model {i + 1}\n\nfit with\n{n_labeled_points} labels",
        size=10,
    )
    for index, image_index in enumerate(uncertainty_index):
        image = images[image_index]

        sub = f.add_subplot(5, 5, index + 1 + (5 * i))
        sub.imshow(image, cmap=plt.cm.gray_r, interpolation="none")
        sub.set_title(
            f"predict: {lp_model.transduction_[image_index]}\ntrue: {y[image_index]}",
            size=10,
        )
        sub.axis("off")

        # 將最不確定的五筆資料加入待刪除的陣列
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))

    # 將最不確定的五筆資料加入標註資料
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)

print("\n最不確定的五筆資料：")
plt.subplots_adjust(left=0.2, bottom=0.03, right=0.9, top=0.9, wspace=0.2, hspace=0.85)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#  11_05_shapley_value_from_scratch

# 自行計算 Shapley value
# How to calculate shapley values from scratch

import random
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

# 載入資料

X, y = datasets.load_breast_cancer(return_X_y=True, as_frame=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練

clf = make_pipeline(StandardScaler(), LogisticRegression())
clf.fit(X_train.values, y_train)

"""
Pipeline(steps=[('standardscaler', StandardScaler()),
                ('logisticregression', LogisticRegression())])
"""

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
print(f"Shaply value calulated from shap: {shap_values[1][j]:.5}")

# Using 455 background data samples could cause slower run times. Consider using shap.sample(data, K) or shap.kmeans(data, K) to summarize the background as K samples.

# Shaply value calulated from shap: 0.01366

# -----------------------------------------------------------------

# 範例2. 自行計算 Shapley value
# 載入套件

from sklearn.tree import DecisionTreeRegressor, plot_tree

# 載入資料

with open("./data/housing.data", encoding="utf8") as f:
    data = f.readlines()
all_fields = []
for line in data:
    line2 = line[1:].replace("   ", " ").replace("  ", " ")
    fields = []
    for item in line2.split(" "):
        fields.append(float(item.strip()))
        if len(fields) == 14:
            all_fields.append(fields)
df = pd.DataFrame(all_fields)
df.columns = "CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT,MEDV".split(",")
cc = df.head()
print(cc)

# 模型訓練

y = df["MEDV"]
df = df[["RM", "LSTAT", "DIS", "NOX"]]

clf = DecisionTreeRegressor(max_depth=3)
clf.fit(df, y)
fig = plt.figure(figsize=(20, 5))
ax = fig.add_subplot(111)
_ = plot_tree(clf, ax=ax, feature_names=df.columns)
plt.show()

# 以 SHAP 套件計算 Shapley value

import shap
import tabulate

explainer = shap.TreeExplainer(clf)
shap_values = explainer.shap_values(df[:1])  # 第一筆資料
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

# Shapley value + Y平均數 = 預測值

cc = shap_values.sum() + y.mean(), clf.predict(df[:1])[0]
print(cc)

# (22.905200000000004, 22.9052)

# 自行計算 Shapley value

from itertools import combinations
import scipy


# 計算特定組合的邊際貢獻
def pred_tree(clf, coalition, row, node=0):
    left_node = clf.tree_.children_left[node]
    right_node = clf.tree_.children_right[node]
    is_leaf = left_node == right_node

    if is_leaf:
        return clf.tree_.value[node].squeeze()

    feature = row.index[clf.tree_.feature[node]]
    if feature in coalition:
        if row.loc[feature] <= clf.tree_.threshold[node]:
            # go left
            return pred_tree(clf, coalition, row, node=left_node)
        else:  # go right
            return pred_tree(clf, coalition, row, node=right_node)

    # take weighted average of left and right
    wl = clf.tree_.n_node_samples[left_node] / clf.tree_.n_node_samples[node]
    wr = clf.tree_.n_node_samples[right_node] / clf.tree_.n_node_samples[node]
    value = wl * pred_tree(clf, coalition, row, node=left_node)
    value += wr * pred_tree(clf, coalition, row, node=right_node)
    return value


# 計算特定組合的平均邊際貢獻
def make_value_function(clf, row, col):
    def value(c):
        marginal_gain = pred_tree(clf, c + [col], row) - pred_tree(clf, c, row)
        num_coalitions = scipy.special.comb(len(row) - 1, len(c))
        return marginal_gain / num_coalitions

    return value


# 各種組合
def make_coalitions(row, col):
    rest = [x for x in row.index if x != col]
    for i in range(len(rest) + 1):
        for x in combinations(rest, i):
            yield list(x)


# 計算 Shapley value
def compute_shap(clf, row, col):
    v = make_value_function(clf, row, col)
    return sum([v(coal) / len(row) for coal in make_coalitions(row, col)])


# 顯示 Shapley value
print(
    tabulate.tabulate(
        pd.DataFrame(
            {
                "shap_value": shap_values.squeeze(),
                "my_shap": [
                    compute_shap(clf, df[:1].T.squeeze(), x) for x in df.columns
                ],
                "feature_value": df[:1].values.squeeze(),
            },
            index=df.columns,
        ),
        tablefmt="github",
        headers="keys",
    )
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_06_shap_test

# SHAP套件測試
# An introduction to explainable AI with Shapley values

import shap
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 載入資料集

df = pd.read_csv("./data/ca_housing.csv")
cc = df.head()
print(cc)

# 資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(["median_house_value", "ocean_proximity"], axis=1)
y = df["median_house_value"]

# 模型訓練與評估

# scaler = StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

model = LinearRegression()
model.fit(X, y)
print("Model coefficients:")
for i in range(X.shape[1]):
    print(X.columns[i], "=", model.coef_[i].round(5))

# 單一特徵影響力

feature_name = "median_income"
X100 = shap.utils.sample(X, 100)
shap.partial_dependence_plot(
    feature_name,
    model.predict,
    X100,
    ice=False,
    model_expected_value=True,
    feature_expected_value=True,
)

# 衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(model.predict, X100)
shap_values = explainer(X)
shap.partial_dependence_plot(
    feature_name,
    model.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    ice=False,
    shap_values=shap_values[sample_ind : sample_ind + 1, :],
)

# Exact explainer: 20434it [01:32, 205.74it/s]

# 以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:, feature_name])
plt.show()

# 單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
plt.show()

# 加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)
model_ebm.fit(X, y)

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
fig, ax = shap.partial_dependence_plot(
    feature_name,
    model_ebm.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    show=False,
    ice=False,
    shap_values=shap_values_ebm[sample_ind : sample_ind + 1, :],  # 第 21 筆資料
)
plt.show()

shap.plots.scatter(shap_values_ebm[:, feature_name])
plt.show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
plt.show()

shap.plots.beeswarm(shap_values_ebm)
plt.show()

shap.plots.bar(shap_values_ebm)
plt.show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook? If this notebook was from another user you must also trust this notebook (File -> Trust notebook). If you are viewing this notebook on github the Javascript has been stripped for security. If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 11_07_mlflow_test

# MLflow 測試

import warnings
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn

# 載入資料集

X, y = datasets.load_diabetes(return_X_y=True)

# 資料分割

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 模型訓練與評估

# 定義模型參數
alpha = 1
l1_ratio = 1

with mlflow.start_run():
    # 模型訓練
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio)
    model.fit(X_train, y_train)

    # 模型評估
    pred = model.predict(X_test)
    rmse = mean_squared_error(pred, y_test)
    abs_error = mean_absolute_error(pred, y_test)
    r2 = r2_score(pred, y_test)

    # MLflow 記錄
    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("abs_error", abs_error)
    mlflow.log_metric("r2", r2)

    # MLflow 記錄模型
    mlflow.sklearn.log_model(model, "model")

# 2023/01/28 10:05:26 WARNING mlflow.utils.environment: Encountered an unexpected error while inferring pip requirements (model URI: C:\WINDOWS\TEMP\tmpxl4956z4\model\model.pkl, flavor: sklearn), fall back to return ['scikit-learn==1.2.0', 'cloudpickle==1.6.0']. Set logging level to DEBUG to see the full traceback.

# 模型評估
""" NG
cc = mlflow.sklearn.log_model(lr, "model")
print(cc)

#平均分數: 0.9303030303030303, 標準差: 0.08393720596645175
"""

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
from sklearn.model_selection import cross_val_score

scores = cross_val_score(model, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: 0.12143159519945441, 標準差: 0.4732757387323812

svc = LinearSVR()
svc.fit(X_train_std, y_train)
from sklearn.model_selection import cross_val_score

scores = cross_val_score(svc, X_test_std, y_test, cv=10)
print(f"平均分數: {np.mean(scores)}, 標準差: {np.std(scores)}")

# 平均分數: -1.0399780386178537, 標準差: 0.36412901584183494

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
