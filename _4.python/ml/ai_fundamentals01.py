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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(0, 1, N)
y = np.sqrt(X) + 0.2 * np.random.rand(N) - 0.1

X = X.reshape(-1, 1)
y = y.reshape(-1, 1)

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    return pipeline


print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit


def plot_learning_curve(
    estimator,
    title,
    X,
    y,
    ylim=None,
    cv=None,
    n_jobs=1,
    train_sizes=np.linspace(0.1, 1.0, 5),
):
    """
    Generate a simple plot of the test and training learning curve.

    Parameters
    ----------
    estimator : object type that implements the "fit" and "predict" methods
        An object of that type which is cloned for each validation.

    title : string
        Title for the chart.

    X : array-like, shape (n_samples, n_features)
        Training vector, where n_samples is the number of samples and
        n_features is the number of features.

    y : array-like, shape (n_samples) or (n_samples, n_features), optional
        Target relative to X for classification or regression;
        None for unsupervised learning.

    ylim : tuple, shape (ymin, ymax), optional
        Defines minimum and maximum yvalues plotted.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
          - None, to use the default 3-fold cross-validation,
          - integer, to specify the number of folds.
          - An object to be used as a cross-validation generator.
          - An iterable yielding train/test splits.

        For integer/None inputs, if ``y`` is binary or multiclass,
        :class:`StratifiedKFold` used. If the estimator is not a classifier
        or if ``y`` is neither binary nor multiclass, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validators that can be used here.

    n_jobs : integer, optional
        Number of jobs to run in parallel (default 1).
    """
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes
    )
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    plt.plot(train_sizes, train_scores_mean, "o--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, "o-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")
    return plt


# 為了讓學習曲線更平滑，交叉驗證數據集的得分計算 10 次，每次都重新選中 20% 的數據計算一遍
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
titles = [
    "Learning Curves (Under Fitting)",
    "Learning Curves",
    "Learning Curves (Over Fitting)",
]
degrees = [1, 3, 10]

plt.figure(figsize=(18, 4))
for i in range(len(degrees)):
    plt.subplot(1, 3, i + 1)
    plot_learning_curve(
        polynomial_model(degrees[i]), titles[i], X, y, ylim=(0.75, 1.01), cv=cv
    )

plt.show()

print("------------------------------------------------------------")  # 60個

# from sklearn.datasets.samples_generator import make_blobs    old
from sklearn.datasets import make_blobs

# 生成數據
centers = [[-2, 2], [2, 2], [0, 4]]
X, y = make_blobs(n_samples=60, centers=centers, random_state=0, cluster_std=0.60)

# 畫出數據
plt.figure(figsize=(12, 8))
c = np.array(centers)
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 畫出樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="orange")  # 畫出中心點

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.neighbors import KNeighborsClassifier

# 模型訓練
k = 5
clf = KNeighborsClassifier(n_neighbors=k)
clf.fit(X, y)

# 進行預測
X_sample = [0, 2]
X_sample = np.array(X_sample).reshape(1, -1)
y_sample = clf.predict(X_sample)
neighbors = clf.kneighbors(X_sample, return_distance=False)

# 畫出示意圖
plt.figure(figsize=(12, 8))
plt.scatter(X[:, 0], X[:, 1], c=y, s=100, cmap="cool")  # 樣本
plt.scatter(c[:, 0], c[:, 1], s=100, marker="^", c="k")  # 中心點
plt.scatter(X_sample[0][0], X_sample[0][1], marker="x", s=100, cmap="cool")  # 待預測的點

for i in neighbors[0]:
    # 預測點與距離最近的 5 個樣本的連線
    plt.plot([X[i][0], X_sample[0][0]], [X[i][1], X_sample[0][1]], "k--", linewidth=0.6)

plt.show()

print("------------------------------------------------------------")  # 60個

# 生成訓練樣本
N = 40
X = 5 * np.random.rand(N, 1)
y = np.cos(X).ravel()

# 添加一些噪聲
y += 0.2 * np.random.rand(N) - 0.1

# 訓練模型
from sklearn.neighbors import KNeighborsRegressor

k = 5
knn = KNeighborsRegressor(k)
knn.fit(X, y)

# 生成足夠密集的點并進行預測
T = np.linspace(0, 5, 500)[:, np.newaxis]
y_pred = knn.predict(T)
print(knn.score(X, y))

# 畫出擬合曲線
plt.figure(figsize=(12, 8))
plt.scatter(X, y, c="g", label="data", s=100)  # 畫出訓練樣本
plt.plot(T, y_pred, c="k", label="prediction", lw=4)  # 畫出擬合曲線
plt.axis("tight")
plt.title("KNeighborsRegressor (k = %i)" % k)
plt.show()

print("------------------------------------------------------------")  # 60個

# 加載數據
data = pd.read_csv("datasets/pima-indians-diabetes/diabetes.csv")
print("dataset shape {}".format(data.shape))

print(data.head())

print(data.groupby("Outcome").size())

X = data.iloc[:, 0:8]
Y = data.iloc[:, 8]
print("shape of X {}; shape of Y {}".format(X.shape, Y.shape))

print("------------------------------")  # 30個

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

from sklearn.neighbors import KNeighborsClassifier, RadiusNeighborsClassifier

models = []
models.append(("KNN", KNeighborsClassifier(n_neighbors=2)))
models.append(
    ("KNN with weights", KNeighborsClassifier(n_neighbors=2, weights="distance"))
)
models.append(
    (
        "Radius Neighbors",
        RadiusNeighborsClassifier(
            #    n_neighbors=2, radius=500.0)))
            radius=500.0
        ),
    )
)

results = []
for name, model in models:
    model.fit(X_train, Y_train)
    results.append((name, model.score(X_test, Y_test)))
for i in range(len(results)):
    print("name: {}; score: {}".format(results[i][0], results[i][1]))

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

print("------------------------------")  # 30個

# 模型訓練

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train, Y_train)
train_score = knn.score(X_train, Y_train)
test_score = knn.score(X_test, Y_test)
print("train score: {}; test score: {}".format(train_score, test_score))

from sklearn.model_selection import ShuffleSplit
from common.utils import plot_learning_curve

knn = KNeighborsClassifier(n_neighbors=2)
cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
plt.figure(figsize=(10, 6))
plot_learning_curve(
    plt, knn, "Learn Curve for KNN Diabetes", X, Y, ylim=(0.0, 1.01), cv=cv
)

plt.show()

print("------------------------------")  # 30個

# 數據可視化

from sklearn.feature_selection import SelectKBest

selector = SelectKBest(k=2)
X_new = selector.fit_transform(X, Y)
print(X_new[0:5])

results = []
for name, model in models:
    kfold = KFold(n_splits=10)
    cv_result = cross_val_score(model, X_new, Y, cv=kfold)
    results.append((name, cv_result))
for i in range(len(results)):
    print("name: {}; cross val score: {}".format(results[i][0], results[i][1].mean()))

# 畫出數據
plt.figure(figsize=(10, 6))
plt.ylabel("BMI")
plt.xlabel("Glucose")
plt.scatter(X_new[Y == 0][:, 0], X_new[Y == 0][:, 1], c="r", s=20, marker="o")  # 畫出樣本
plt.scatter(X_new[Y == 1][:, 0], X_new[Y == 1][:, 1], c="g", s=20, marker="^")  # 畫出樣本

plt.show()

print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(-2 * np.pi, 2 * np.pi, N)
Y = np.sin(X) + 0.2 * np.random.rand(N) - 0.1
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = LinearRegression()
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    return pipeline


from sklearn.metrics import mean_squared_error

degrees = [2, 3, 5, 10]
results = []
for d in degrees:
    model = polynomial_model(degree=d)
    model.fit(X, Y)
    train_score = model.score(X, Y)
    mse = mean_squared_error(Y, model.predict(X))
    results.append({"model": model, "degree": d, "score": train_score, "mse": mse})
for r in results:
    print(
        "degree: {}; train score: {}; mean squared error: {}".format(
            r["degree"], r["score"], r["mse"]
        )
    )

print("------------------------------")  # 30個

from matplotlib.figure import SubplotParams

plt.figure(figsize=(12, 6), dpi=200, subplotpars=SubplotParams(hspace=0.3))
for i, r in enumerate(results):
    fig = plt.subplot(2, 2, i + 1)
    plt.xlim(-8, 8)
    plt.title("LinearRegression degree={}".format(r["degree"]))
    plt.scatter(X, Y, s=5, c="b", alpha=0.5)
    plt.plot(X, r["model"].predict(X), "r-")

plt.show()

print("------------------------------------------------------------")  # 60個

""" 波士頓房價 資料庫已移除

from sklearn.datasets import load_boston

boston = load_boston()
X = boston.data
y = boston.target
print(X.shape)

print(X[0])

print(boston.feature_names)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

start = time.clock()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('耗時 : {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}'.format(time.clock()-start, train_score, cv_score))

print("------------------------------------------------------------")  # 60個

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree,
                                             include_bias=False)
    linear_regression = LinearRegression(normalize=True)
    pipeline = Pipeline([("polynomial_features", polynomial_features),
                         ("linear_regression", linear_regression)])
    return pipeline

model = polynomial_model(degree=2)

start = time.clock()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print('耗時 : {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}'.format(time.clock()-start, train_score, cv_score))

print("------------------------------------------------------------")  # 60個

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)
plt.figure(figsize=(18, 4))
title = 'Learning Curves (degree={0})'
degrees = [1, 2, 3]

start = time.clock()
plt.figure(figsize=(18, 4), dpi=200)
for i in range(len(degrees)):
    plt.subplot(1, 3, i + 1)
    plot_learning_curve(plt, polynomial_model(degrees[i]), title.format(degrees[i]), X, y, ylim=(0.01, 1.01), cv=cv)

print('耗時 : {0:.6f}'.format(time.clock()-start))

plt.show()

"""
print("------------------------------------------------------------")  # 60個

# 載入數據
from sklearn.datasets import load_breast_cancer

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

print("------------------------------------------------------------")  # 60個

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


def read_dataset(fname):
    # 指定第一列作為行索引
    data = pd.read_csv(fname, index_col=0)
    # 丟棄無用的數據
    data.drop(["Name", "Ticket", "Cabin"], axis=1, inplace=True)
    # 處理性別數據
    data["Sex"] = (data["Sex"] == "male").astype("int")
    # 處理登船港口數據
    labels = data["Embarked"].unique().tolist()
    data["Embarked"] = data["Embarked"].apply(lambda n: labels.index(n))
    # 處理缺失數據
    data = data.fillna(0)
    return data


train = read_dataset("datasets/titanic/train.csv")
print(train.head())

from sklearn.model_selection import train_test_split

y = train["Survived"].values
X = train.drop(["Survived"], axis=1).values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("train dataset: {0}; test dataset: {1}".format(X_train.shape, X_test.shape))

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

print("------------------------------------------------------------")  # 60個

from sklearn.tree import export_graphviz

with open("titanic.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png


# 參數選擇 max_depth
def cv_score(d):
    clf = DecisionTreeClassifier(max_depth=d)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


depths = range(2, 15)
scores = [cv_score(d) for d in depths]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = depths[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel("max depth of decision tree")
plt.ylabel("score")
plt.plot(depths, cv_scores, ".g-", label="cross-validation score")
plt.plot(depths, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


# 訓練模型，并計算評分
def cv_score(val):
    clf = DecisionTreeClassifier(criterion="gini", min_impurity_decrease=val)
    clf.fit(X_train, y_train)
    tr_score = clf.score(X_train, y_train)
    cv_score = clf.score(X_test, y_test)
    return (tr_score, cv_score)


# 指定參數范圍，分別訓練模型，并計算評分
values = np.linspace(0, 0.005, 50)
scores = [cv_score(v) for v in values]
tr_scores = [s[0] for s in scores]
cv_scores = [s[1] for s in scores]

# 找出評分最高的模型參數
best_score_index = np.argmax(cv_scores)
best_score = cv_scores[best_score_index]
best_param = values[best_score_index]
print("best param: {0}; best score: {1}".format(best_param, best_score))

# 畫出模型參數與模型評分的關系
plt.figure(figsize=(10, 6), dpi=144)
plt.grid()
plt.xlabel("threshold of entropy")
plt.ylabel("score")
plt.plot(values, cv_scores, ".g-", label="cross-validation score")
plt.plot(values, tr_scores, ".r--", label="training score")
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_curve(train_sizes, cv_results, xlabel):
    train_scores_mean = cv_results["mean_train_score"]
    train_scores_std = cv_results["std_train_score"]
    test_scores_mean = cv_results["mean_test_score"]
    test_scores_std = cv_results["std_test_score"]
    plt.figure(figsize=(10, 6), dpi=144)
    plt.title("parameters turning")
    plt.grid()
    plt.xlabel(xlabel)
    plt.ylabel("score")
    plt.fill_between(
        train_sizes,
        train_scores_mean - train_scores_std,
        train_scores_mean + train_scores_std,
        alpha=0.1,
        color="r",
    )
    plt.fill_between(
        train_sizes,
        test_scores_mean - test_scores_std,
        test_scores_mean + test_scores_std,
        alpha=0.1,
        color="g",
    )
    plt.plot(train_sizes, train_scores_mean, ".--", color="r", label="Training score")
    plt.plot(
        train_sizes, test_scores_mean, ".-", color="g", label="Cross-validation score"
    )

    plt.legend(loc="best")


from sklearn.model_selection import GridSearchCV

thresholds = np.linspace(0, 0.005, 50)
# Set the parameters by cross-validation
param_grid = {"min_impurity_decrease": thresholds}

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

plot_curve(thresholds, clf.cv_results_, xlabel="gini thresholds")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import GridSearchCV

entropy_thresholds = np.linspace(0, 0.01, 50)
gini_thresholds = np.linspace(0, 0.005, 50)

# Set the parameters by cross-validation
param_grid = [
    {"criterion": ["entropy"], "min_impurity_decrease": entropy_thresholds},
    {"criterion": ["gini"], "min_impurity_decrease": gini_thresholds},
    {"max_depth": range(2, 10)},
    {"min_samples_split": range(2, 30, 2)},
]

clf = GridSearchCV(DecisionTreeClassifier(), param_grid, cv=5, return_train_score=True)
clf.fit(X, y)
print("best param: {0}\nbest score: {1}".format(clf.best_params_, clf.best_score_))

print("------------------------------------------------------------")  # 60個

print("生成決策樹圖形")

clf = DecisionTreeClassifier(
    criterion="entropy", min_impurity_decrease=0.002857142857142857
)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print("train score: {0}; test score: {1}".format(train_score, test_score))

# 導出 titanic.dot 文件
with open("titanic.dot", "w") as f:
    f = export_graphviz(clf, out_file=f)

# 1. 在電腦上安裝 graphviz
# 2. 運行 `dot -Tpng titanic.dot -o titanic.png`
# 3. 在當前目錄查看生成的決策樹 titanic.png

print("------------------------------------------------------------")  # 60個

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2]])
class2 = np.array([[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4]])

plt.figure(figsize=(8, 6), dpi=144)

plt.title("Decision Boundary")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.arrow(4, 4, -1, -1, shape="full", color="r")
plt.plot([3, 3], [0.5, 6], "--b")
plt.arrow(4, 4, -1, 0, shape="full", color="b", linestyle="--")
plt.annotate(
    r"margin 1",
    xy=(3.5, 4),
    xycoords="data",
    xytext=(3.1, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"margin 2",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(4, 3.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"support vector",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"support vector",
    xy=(2, 2),
    xycoords="data",
    xytext=(0.5, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 6), dpi=144)

plt.title("Support Vector Machine")

plt.xlim(0, 8)
plt.ylim(0, 6)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")
plt.arrow(4, 4, -1, -1, shape="full", color="b")
plt.annotate(
    r"$w^T x + b = 0$",
    xy=(5, 1),
    xycoords="data",
    xytext=(6, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$w^T x + b = 1$",
    xy=(6, 2),
    xycoords="data",
    xytext=(7, 2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$w^T x + b = -1$",
    xy=(3.5, 0.5),
    xycoords="data",
    xytext=(4.5, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"d",
    xy=(3.5, 3.5),
    xycoords="data",
    xytext=(2, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"A",
    xy=(4, 4),
    xycoords="data",
    xytext=(5, 4.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

plt.figure(figsize=(13, 6), dpi=144)

# sub plot 1
plt.subplot(1, 2, 1)

X, y = make_blobs(
    n_samples=100,
    n_features=2,
    centers=[(1, 1), (2, 2)],
    random_state=4,
    shuffle=False,
    cluster_std=0.4,
)

plt.title("Non-linear Separatable")

plt.xlim(0, 3)
plt.ylim(0, 3)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], marker="o")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], marker="s")
plt.plot([0.5, 2.5], [2.5, 0.5], "-r")

# sub plot 2
plt.subplot(1, 2, 2)

class1 = np.array([[1, 1], [1, 3], [2, 1], [1, 2], [2, 2], [1.5, 1.5], [1.2, 1.7]])
class2 = np.array(
    [[4, 4], [5, 5], [5, 4], [5, 3], [4, 5], [6, 4], [5.5, 3.5], [4.5, 4.5], [2, 1.5]]
)

plt.title("Slack Variable")

plt.xlim(0, 7)
plt.ylim(0, 7)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [5, 1], "-r")
plt.plot([0, 4], [4, 0], "--b", [2, 6], [6, 2], "--b")
plt.arrow(2, 1.5, 2.25, 2.25, shape="full", color="b")
plt.annotate(
    r"violate margin rule.",
    xy=(2, 1.5),
    xycoords="data",
    xytext=(0.2, 0.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"normal sample. $\epsilon = 0$",
    xy=(4, 5),
    xycoords="data",
    xytext=(4.5, 5.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$\epsilon > 0$",
    xy=(3, 2.5),
    xycoords="data",
    xytext=(3, 1.5),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(8, 4), dpi=144)

plt.title("Cost")

plt.xlim(0, 4)
plt.ylim(0, 2)
plt.xlabel("$y^{(i)} (w^T x^{(i)} + b)$")
plt.ylabel("Cost")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.plot([0, 1], [1.5, 0], "-r")
plt.plot([1, 3], [0.015, 0.015], "-r")
plt.annotate(
    r"$J_i = R \epsilon_i$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1 - \epsilon_i$",
    xy=(0.7, 0.5),
    xycoords="data",
    xytext=(1, 1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$J_i = 0$ for $y^{(i)} (w^T x^{(i)} + b) \geq 1$",
    xy=(1.5, 0),
    xycoords="data",
    xytext=(1.8, 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個

plt.figure(figsize=(13, 6), dpi=144)

class1 = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [3, 2], [4, 1], [5, 1]])
class2 = np.array(
    [[2.2, 4], [1.5, 5], [1.8, 4.6], [2.4, 5], [3.2, 5], [3.7, 4], [4.5, 4.5], [5.4, 3]]
)

# sub plot 1
plt.subplot(1, 2, 1)

plt.title("Non-linear Separatable in Low Dimension")

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.yticks(())
plt.xlabel("X1")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")
ax.spines["left"].set_color("none")

plt.scatter(class1[:, 0], np.zeros(class1[:, 0].shape[0]) + 0.05, marker="o")
plt.scatter(class2[:, 0], np.zeros(class2[:, 0].shape[0]) + 0.05, marker="s")

# sub plot 2
plt.subplot(1, 2, 2)

plt.title("Linear Separatable in High Dimension")

plt.xlim(0, 6)
plt.ylim(0, 6)
plt.xlabel("X1")
plt.ylabel("X2")
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(class1[:, 0], class1[:, 1], marker="o")
plt.scatter(class2[:, 0], class2[:, 1], marker="s")
plt.plot([1, 5], [3.8, 2], "-r")

plt.show()

print("------------------------------------------------------------")  # 60個


def plot_hyperplane(clf, X, y, h=0.02, draw_sv=True, title="hyperplan"):
    # create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    plt.title(title)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap="hot", alpha=0.5)

    markers = ["o", "s", "^"]
    colors = ["b", "r", "c"]
    labels = np.unique(y)
    for label in labels:
        plt.scatter(
            X[y == label][:, 0],
            X[y == label][:, 1],
            c=colors[label],
            marker=markers[label],
        )
    if draw_sv:
        sv = clf.support_vectors_
        plt.scatter(sv[:, 0], sv[:, 1], c="y", marker="x")


from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.3)
clf = svm.SVC(C=1.0, kernel="linear")
clf.fit(X, y)

plt.figure(figsize=(12, 4), dpi=144)
plot_hyperplane(clf, X, y, h=0.01, title="Maximum Margin Hyperplan")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn import svm
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=100, centers=3, random_state=0, cluster_std=0.8)
clf_linear = svm.SVC(C=1.0, kernel="linear")
clf_poly = svm.SVC(C=1.0, kernel="poly", degree=3)
clf_rbf = svm.SVC(C=1.0, kernel="rbf", gamma=0.5)
clf_rbf2 = svm.SVC(C=1.0, kernel="rbf", gamma=0.1)

plt.figure(figsize=(10, 10), dpi=144)

clfs = [clf_linear, clf_poly, clf_rbf, clf_rbf2]
titles = [
    "Linear Kernel",
    "Polynomial Kernel with Degree=3",
    "Gaussian Kernel with $\gamma=0.5$",
    "Gaussian Kernel with $\gamma=0.1$",
]
for clf, i in zip(clfs, range(len(clfs))):
    clf.fit(X, y)
    plt.subplot(2, 2, i + 1)
    plot_hyperplane(clf, X, y, title=titles[i])

plt.show()

print("------------------------------------------------------------")  # 60個

# 載入數據
from sklearn.datasets import load_breast_cancer

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

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

from sklearn.datasets import load_files

""" 缺資料
print("loading train dataset ...")
t = time.time()
news_train = load_files('datasets/mlcomp/379/train')
print("summary: {0} documents in {1} categories.".format(
    len(news_train.data), len(news_train.target_names)))
print("done in {0} seconds".format(time.time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

print("vectorizing train dataset ...")
t = time.time()
vectorizer = TfidfVectorizer(encoding='latin-1')
X_train = vectorizer.fit_transform((d for d in news_train.data))
print("n_samples: %d, n_features: %d" % X_train.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_train.filenames[0], X_train[0].getnnz()))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

from sklearn.naive_bayes import MultinomialNB

print("traning models ...".format(time.time() - t))
t = time.time()
y_train = news_train.target
clf = MultinomialNB(alpha=0.0001)
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
print("train score: {0}".format(train_score))
print("done in {0} seconds".format(time.time() - t))
"""
print("------------------------------------------------------------")  # 60個

""" 缺資料
print("loading test dataset ...")
t = time.time()
news_test = load_files('datasets/mlcomp/379/test')
print("summary: {0} documents in {1} categories.".format(
    len(news_test.data), len(news_test.target_names)))
print("done in {0} seconds".format(time.time() - t))

print("------------------------------")  # 30個

print("vectorizing test dataset ...")
t = time.time()
X_test = vectorizer.transform((d for d in news_test.data))
y_test = news_test.target
print("n_samples: %d, n_features: %d" % X_test.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    news_test.filenames[0], X_test[0].getnnz()))
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

pred = clf.predict(X_test[0])
print("predict: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[pred[0]]))
print("actually: {0} is in category {1}".format(
    news_test.filenames[0], news_test.target_names[news_test.target[0]]))

print("------------------------------")  # 30個

print("predicting test dataset ...")
t = time.time()
pred = clf.predict(X_test)
print("done in %fs" % (time.time() - t))

print("------------------------------")  # 30個

from sklearn.metrics import classification_report

print("classification report on test set for classifier:")
print(clf)
print(classification_report(y_test, pred,
                            target_names=news_test.target_names))

print("------------------------------")  # 30個

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, pred)
print("confusion matrix:")
print(cm)

print("------------------------------")  # 30個

# Show confusion matrix
plt.figure(figsize=(8, 8), dpi=144)
plt.title('Confusion matrix of the classifier')
ax = plt.gca()                                  
ax.spines['right'].set_color('none')            
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.xaxis.set_ticks_position('none')
ax.yaxis.set_ticks_position('none')
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.matshow(cm, fignum=1, cmap='gray')
plt.colorbar()

plt.show()
"""
print("------------------------------------------------------------")  # 60個

print("PCA 算法模擬")

A = np.array([[3, 2000], [2, 3000], [4, 5000], [5, 8000], [1, 2000]], dtype="float")

# 數據歸一化
mean = np.mean(A, axis=0)
norm = A - mean
# 數據縮放
scope = np.max(norm, axis=0) - np.min(norm, axis=0)
norm = norm / scope
print(norm)

U, S, V = np.linalg.svd(np.dot(norm.T, norm))
print(U)

U_reduce = U[:, 0].reshape(2, 1)
print(U_reduce)

R = np.dot(norm, U_reduce)
print(R)

Z = np.dot(R, U_reduce.T)
print(Z)

print(np.multiply(Z, scope) + mean)

print("------------------------------")  # 30個

print("使用 sklearn 包實現")

from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler


def std_PCA(**argv):
    scaler = MinMaxScaler()
    pca = PCA(**argv)
    pipeline = Pipeline([("scaler", scaler), ("pca", pca)])
    return pipeline


pca = std_PCA(n_components=1)
R2 = pca.fit_transform(A)
print(R2)

print(pca.inverse_transform(R2))

print("------------------------------------------------------------")  # 60個

print("降維及恢復示意圖")

plt.figure(figsize=(8, 8), dpi=144)

plt.title("Physcial meanings of PCA")

ymin = xmin = -1
ymax = xmax = 1
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
ax = plt.gca()  # gca 代表當前坐標軸，即 'get current axis'
ax.spines["right"].set_color("none")  # 隱藏坐標軸
ax.spines["top"].set_color("none")

plt.scatter(norm[:, 0], norm[:, 1], marker="s", c="b")
plt.scatter(Z[:, 0], Z[:, 1], marker="o", c="r")
plt.arrow(0, 0, U[0][0], U[1][0], color="r", linestyle="-")
plt.arrow(0, 0, U[0][1], U[1][1], color="r", linestyle="--")
plt.annotate(
    r"$U_{reduce} = u^{(1)}$",
    xy=(U[0][0], U[1][0]),
    xycoords="data",
    xytext=(U_reduce[0][0] + 0.2, U_reduce[1][0] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"$u^{(2)}$",
    xy=(U[0][1], U[1][1]),
    xycoords="data",
    xytext=(U[0][1] + 0.2, U[1][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"raw data",
    xy=(norm[0][0], norm[0][1]),
    xycoords="data",
    xytext=(norm[0][0] + 0.2, norm[0][1] - 0.2),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)
plt.annotate(
    r"projected data",
    xy=(Z[0][0], Z[0][1]),
    xycoords="data",
    xytext=(Z[0][0] + 0.2, Z[0][1] - 0.1),
    fontsize=10,
    arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"),
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs

X, y = make_blobs(
    n_samples=200,
    n_features=2,
    centers=4,
    cluster_std=1,
    center_box=(-10.0, 10.0),
    shuffle=True,
    random_state=1,
)

plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())
plt.scatter(X[:, 0], X[:, 1], s=20, marker="o")

plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

n_clusters = 3
kmean = KMeans(n_clusters=n_clusters)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.score(X))))

labels = kmean.labels_
centers = kmean.cluster_centers_
markers = ["o", "^", "*"]
colors = ["r", "b", "y"]

plt.figure(figsize=(6, 4), dpi=144)
plt.xticks(())
plt.yticks(())

# 畫樣本
for c in range(n_clusters):
    cluster = X[labels == c]
    plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
# 畫出中心點
plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
for i, c in enumerate(centers):
    plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])

plt.show()

print("------------------------------------------------------------")  # 60個


def fit_plot_kmean_model(n_clusters, X):
    plt.xticks(())
    plt.yticks(())

    # 使用 k-均值算法進行擬合
    kmean = KMeans(n_clusters=n_clusters)
    kmean.fit_predict(X)

    labels = kmean.labels_
    centers = kmean.cluster_centers_
    markers = ["o", "^", "*", "s"]
    colors = ["r", "b", "y", "k"]

    # 計算成本
    score = kmean.score(X)
    plt.title("k={}, score={}".format(n_clusters, (int)(score)))

    # 畫樣本
    for c in range(n_clusters):
        cluster = X[labels == c]
        plt.scatter(cluster[:, 0], cluster[:, 1], marker=markers[c], s=20, c=colors[c])
    # 畫出中心點
    plt.scatter(centers[:, 0], centers[:, 1], marker="o", c="white", alpha=0.9, s=300)
    for i, c in enumerate(centers):
        plt.scatter(c[0], c[1], marker="$%d$" % i, s=50, c=colors[i])


from sklearn.cluster import KMeans

n_clusters = [2, 3, 4]

plt.figure(figsize=(10, 3), dpi=144)
for i, c in enumerate(n_clusters):
    plt.subplot(1, 3, i + 1)
    fit_plot_kmean_model(c, X)

plt.show()

print("------------------------------------------------------------")  # 60個

from time import time
from sklearn.datasets import load_files

""" 無檔案
print("loading documents ...")
t = time()
docs = load_files('datasets/clustering/data')
print("summary: {0} documents in {1} categories.".format(
    len(docs.data), len(docs.target_names)))
print("done in {0} seconds".format(time() - t))

from sklearn.feature_extraction.text import TfidfVectorizer

max_features = 20000
print("vectorizing documents ...")
t = time()
vectorizer = TfidfVectorizer(max_df=0.4, 
                             min_df=2, 
                             max_features=max_features, 
                             encoding='latin-1')
X = vectorizer.fit_transform((d for d in docs.data))
print("n_samples: %d, n_features: %d" % X.shape)
print("number of non-zero features in sample [{0}]: {1}".format(
    docs.filenames[0], X[0].getnnz()))
print("done in {0} seconds".format(time() - t))

print("------------------------------------------------------------")  # 60個

from sklearn.cluster import KMeans

print("clustering documents ...")
t = time()
n_clusters = 4
kmean = KMeans(n_clusters=n_clusters, 
               max_iter=100,
               tol=0.01,
               verbose=1,
               n_init=3)
kmean.fit(X)
print("kmean: k={}, cost={}".format(n_clusters, int(kmean.inertia_)))
print("done in {0} seconds".format(time() - t))

print(len(kmean.labels_))

cc = kmean.labels_[1000:1010]
print(cc)

cc = docs.filenames[1000:1010]
print(cc)

print('------------------------------')	#30個

#from __future__ import print_function

print("Top terms per cluster:")

order_centroids = kmean.cluster_centers_.argsort()[:, ::-1]

terms = vectorizer.get_feature_names()
for i in range(n_clusters):
    print("Cluster %d:" % i, end='')
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind], end='')
    print()

a = np.array([[20, 10, 30, 40], [100, 300, 200, 400], [1, 5, 3, 2]])
cc = a.argsort()[:, ::-1]
print(cc)

a = np.array([10, 30, 20, 40])
cc = a.argsort()[::-1]
print(cc)
"""
print("------------------------------------------------------------")  # 60個

from sklearn import metrics

label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Adjusted Rand-Index for random sample: %.3f"
    % metrics.adjusted_rand_score(label_true, label_pred)
)
label_true = [1, 1, 3, 3, 2, 2]
label_pred = [3, 3, 2, 2, 1, 1]
print(
    "Adjusted Rand-Index for same structure sample: %.3f"
    % metrics.adjusted_rand_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "Homogeneity score for same structure sample: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [0, 1, 2, 3]
print(
    "Homogeneity score for each cluster come from only one class: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "Homogeneity score for each cluster come from two class: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Homogeneity score for random sample: %.3f"
    % metrics.homogeneity_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "Completeness score for same structure sample: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print(
    "Completeness score for each class assign to only one cluster: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "Completeness score for each class assign to two class: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)
label_true = np.random.randint(1, 4, 6)
label_pred = np.random.randint(1, 4, 6)
print(
    "Completeness score for random sample: %.3f"
    % metrics.completeness_score(label_true, label_pred)
)

from sklearn import metrics

label_true = [1, 1, 2, 2]
label_pred = [2, 2, 1, 1]
print(
    "V-measure score for same structure sample: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
label_true = [0, 1, 2, 3]
label_pred = [1, 1, 2, 2]
print(
    "V-measure score for each class assign to only one cluster: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
print(
    "V-measure score for each class assign to only one cluster: %.3f"
    % metrics.v_measure_score(label_pred, label_true)
)
label_true = [1, 1, 2, 2]
label_pred = [1, 2, 1, 2]
print(
    "V-measure score for each class assign to two class: %.3f"
    % metrics.v_measure_score(label_true, label_pred)
)
"""
from sklearn import metrics

labels = docs.target
print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, kmean.labels_))
print("Completeness: %0.3f" % metrics.completeness_score(labels, kmean.labels_))
print("V-measure: %0.3f" % metrics.v_measure_score(labels, kmean.labels_))
print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, kmean.labels_))
print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, kmean.labels_, sample_size=1000))
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
