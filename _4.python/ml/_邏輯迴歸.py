"""
邏輯迴歸 (logistic regression)

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

import joblib
import sklearn.linear_model
from common1 import *
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler  # 特徵縮放
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay  # 混淆矩陣圖
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn import metrics


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 1000  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 6  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

d_sta = StandardScaler().fit_transform(X)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, y_train, y_test = train_test_split(d_sta, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(dx_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(dx_test)  # 預測.predict

# 輸出準確性
print(f"訓練資料的準確性 = {logistic_regression.score(dx_train, y_train)}")
print(f"測試資料的準確性 = {logistic_regression.score(dx_test, y_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

X, y = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

d_sta = StandardScaler().fit_transform(X)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, y_train, y_test = train_test_split(d_sta, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(dx_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(dx_test)  # 預測.predict

# 輸出準確性
print(f"訓練資料的準確性 = {logistic_regression.score(dx_train, y_train)}")
print(f"測試資料的準確性 = {logistic_regression.score(dx_test, y_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_regression_with_nonlinear_data

# 以二次迴歸預測世界人口數

from sklearn.datasets import make_circles

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=9487)

# 資料切割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=9487)

# 繪製訓練及測試資料
_, (train_ax, test_ax) = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))
train_ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train)
train_ax.set_ylabel("Feature #1")
train_ax.set_xlabel("Feature #0")
train_ax.set_title("Training data")

test_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
test_ax.set_xlabel("Feature #0")
_ = test_ax.set_title("Testing data")
show()

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

# cc = logistic_regression.coef_, lr.intercept_
# print(cc)

y_pred = logistic_regression.predict(X_test)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 48.80%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 30
group0 = np.random.normal(-1, 1, size=N)
group1 = np.random.normal(3, 1, size=N)

x = np.r_[group0, group1]
X = x.reshape((N * 2, -1))
print(X)

y = np.r_[np.zeros(N), np.ones(N)]  # 目標,前半0, 後半1
print(y)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

# yy = np.array([-5, -4, -3, -2, -1, 0, 1, 2 ,3, 4, 5])  # 真實資料
# YY = yy.reshape(len(yy), 1)

y_pred = logistic_regression.predict(X)  # 預測.predict
print(y_pred)

y_pred_prob = logistic_regression.predict_proba(X)  # 預測機率.predict_proba
print(y_pred_prob)

plt.subplot(211)
plt.hist(group0, alpha=0.3, label="第0群, 對應到0")
plt.hist(group1, alpha=0.3, label="第1群, 對應到1")
plt.legend()

plt.subplot(212)
plt.plot(
    range(len(y_pred)), y_pred, color="lime", marker="o", markersize=10, label="預測結果"
)
plt.plot(range(len(y_pred_prob)), y_pred_prob[:, 0], "ro-", label="對應到第0群的機率")
plt.plot(range(len(y_pred_prob)), y_pred_prob[:, 1], "go-", label="對應到第1群的機率")
plt.legend()
show()

print(logistic_regression.predict_proba([[0]])[:, 1])  # 預測機率.predict_proba
print(logistic_regression.predict_proba([[0], [1], [2]])[:, 1])  # 預測機率.predict_proba

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 尋找銀行行銷活動目標客戶

from sklearn import preprocessing

df = pd.read_csv("./data/banking.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# y 各類別資料筆數統計

sns.countplot(x="y", data=df)
show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6, 6), autopct="%1.1f%%")
plt.legend()
show()

cat_vars = [
    "job",
    "marital",
    "education",
    "default",
    "housing",
    "loan",
    "contact",
    "month",
    "day_of_week",
    "poutcome",
]
for var in cat_vars:
    cat_list = "var" + "_" + var
    cat_list = pd.get_dummies(df[var], prefix=var)
    data1 = df.join(cat_list)
    df = data1

data_vars = df.columns.values.tolist()
to_keep = [i for i in data_vars if i not in cat_vars]
data_final = df[to_keep]
cc = data_final.columns.values
print(cc)

df = data_final
print(df)

# 是否有含遺失值(Missing value)
cc = df.isnull().sum()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.drop("y", axis=1).values
y = df.y.values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# ((32950, 63), (8238, 63), (32950,), (8238,))

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

from sklearn.metrics import classification_report

cc = classification_report(y_test, y_pred)
print("分類報告 :\n", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib

plt.style.use("bmh")
colors = ["#A60628", "#467821"]
plt.cmap = matplotlib.colors.ListedColormap(colors)

# Bivariate normal distribution mean [0, 0] [0.5, 4], with a covariance matrix

N = 10
subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], N)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], N)
print(subset1)
print()
print(subset2)
print()

X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(N), np.ones(N)))  # 目標,前半0, 後半1
print(X)
print()

# plt.scatter(X[:, 0], X[:, 1], c=y)
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cmap, marker="o", s=40)
plt.scatter(X[:N, 0], X[:N, 1], c="r", label="第0群, 對應到0")
plt.scatter(X[N : N * 2 - 1, 0], X[N : N * 2 - 1, 1], c="g", label="第1群, 對應到1")
plt.legend()
show()

print("------------------------------")  # 30個

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

print(logistic_regression.intercept_)
print(logistic_regression.coef_)
print(logistic_regression.classes_)

y_pred = logistic_regression.predict(X)  # 預測.predict

cc = np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1))
print(cc)
cc = cc * 1.0 / len(y)
print("正確率 :", cc)

print("混淆矩陣 :\n", confusion_matrix(y, y_pred))

print("繪製熱圖")
sns.heatmap(confusion_matrix(y, y_pred))
show()

print("繪制分類邊界")
plt.style.use("bmh")

# Set min and max values and give it some padding
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
h = 0.01

# Generate a grid of points with distance h between them
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Predict the function value for the whole grid (get class for each grid point)
Z = logistic_regression.predict(np.c_[xx.ravel(), yy.ravel()])  # 預測.predict
Z = Z.reshape(xx.shape)
# print(Z)

# Plot the contour and training examples
plt.contourf(xx, yy, Z, alpha=0.3)
plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8)
# plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8, cmap=plt.cmap)
plt.title("logistic regression prediction")

show()

print("------------------------------")  # 30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


# l_rate, iterations = 1, 500
l_rate, iterations = 1, 2000
add_intercept = True

if add_intercept:
    intercept = np.ones((X.shape[0], 1))
    X = np.hstack((intercept, X))

theta = np.zeros(X.shape[1]).reshape(-1, 1)
y = y.reshape(-1, 1)
accu_history = [0] * iterations
ll_history = [0.0] * iterations

for epoch in range(iterations):
    x_theta = np.dot(X, theta)
    y_hat = sigmoid(x_theta)
    error = y - y_hat
    gradient = np.dot(X.T, error)
    theta = theta + l_rate * gradient
    y_pred = np.round(y_hat)

    accu = np.sum(y_pred == y) * 1.0 / len(y)
    accu_history[epoch] = accu

    # if epoch % 5 == 0:
    if epoch % 100 == 0:
        print("After iter {}; accuracy: {}".format(epoch + 1, accu))

print("theta")
print(theta)

print("結果")
print(accu_history)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("data/200811-201811d.csv")
cc = df.head()
print(cc)

# print(df[df.數學 >= 80])

cc = df[df.PM25 > 30]
print(cc)
print(len(cc))

cc = df[df["PM25"] > 30]
print(cc)
print(len(cc))

# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

"""
# 用heatmap(.isnull())來找出缺失的資料在哪些欄位
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")
show()
"""
print("------------------------------")  # 30個

plt.title("用countplot來看Nox是否影響健康")

sns.countplot(x="Danger", hue="Nox", data=df, palette="RdBu_r")

show()

print("------------------------------")  # 30個

plt.title("用直方圖看PM25分佈")

sns.distplot(df["PM25"].dropna(), kde=False, bins=30)

show()

print("------------------------------")  # 30個

plt.title("用直方圖看Nox的分佈")

df["Nox"].hist(bins=30)

show()

print("------------------------------")  # 30個

X = df.drop("Danger", axis=1)
y = df["Danger"]  # 目標, 0 : 不危險, 1 : 危險

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

logistic_regression = sklearn.linear_model.LogisticRegression(
    solver="liblinear"
)  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

from sklearn.metrics import classification_report

cc = classification_report(y_test, y_pred)
print("分類報告 :\n", cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectKBest 單變數特徵選取(Univariate feature selection)
# SelectKBest 挑選出K個分數最高的特徵

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# SelectKBest 特徵選取

logistic_regression = SelectKBest(chi2, k=2)
X_new = logistic_regression.fit_transform(X, y)
print(X_new.shape)
# (150, 2)

print("顯示特徵分數")
cc = logistic_regression.scores_
print(cc)

print("顯示 p value")
cc = logistic_regression.pvalues_
print(cc)

# 顯示特徵名稱
print("鳶尾花資料集")
ds = datasets.load_iris()
cc = np.array(ds.feature_names)[logistic_regression.scores_.argsort()[-2:][::-1]]
print(cc)

X = pd.DataFrame(ds.data, columns=ds.feature_names)
logistic_regression = SelectKBest(chi2, k=2)
X_new = logistic_regression.fit_transform(X, y)
cc = logistic_regression.get_feature_names_out()
print(cc)

# 選擇2個特徵
X = X[logistic_regression.get_feature_names_out()].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()

show()

# 使用全部特徵
print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectPercentile 單變數特徵選取(Univariate feature selection)

from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import chi2

print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# SelectPercentile 特徵選取

logistic_regression = SelectPercentile(chi2, percentile=10)
X_new = logistic_regression.fit_transform(X, y)
print(X_new.shape)

print("顯示特徵分數")
cc = logistic_regression.scores_
print(cc)

print("顯示 p value")
cc = logistic_regression.pvalues_
print(cc)

# 選擇部份特徵
X = X_new

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# GenericUnivariateSelect 單變數特徵選取(Univariate feature selection)

from sklearn.feature_selection import GenericUnivariateSelect, chi2

print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# GenericUnivariateSelect 特徵選取

# 使用 SelectKBest, 20 個特徵
clf = GenericUnivariateSelect(chi2, mode="k_best", param=20)

X_new = clf.fit_transform(X, y)
print(X_new.shape)

print("顯示特徵分數")
cc = clf.scores_
print(cc)

print("顯示 p value")
cc = clf.pvalues_
print(cc)

# 選擇部份特徵
X = X_new

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("數字資料集")
X, y = datasets.load_digits(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 遞迴特徵消去法(Recursive feature elimination)

from sklearn.feature_selection import RFE
from sklearn.svm import SVC

print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# RFE 特徵選取

svc = SVC(kernel="linear", C=1)

clf = RFE(estimator=svc, n_features_to_select=2, step=1)

X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 特徵重要性排名
print(clf.ranking_)

# 選擇2個特徵
X = X_new

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣 :\n", confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
show()

# 使用全部特徵
print("鳶尾花資料集")
X, y = datasets.load_iris(return_X_y=True)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)  # STD特徵縮放
X_test_std = scaler.transform(X_test)  # STD特徵縮放

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 500  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
GROUPS = 2  # centers, 分群數
STD = 0.3  # cluster_std, 資料標準差
print("make_blobs,", N, "個樣本, ", M, "個特徵, 分成", GROUPS, "群")

dx, dy = make_blobs(n_samples=N, n_features=M, centers=GROUPS)

scaler = StandardScaler()
dx_std = scaler.fit_transform(dx)  # STD特徵縮放

dx_train, dx_test, dy_train, dy_test = train_test_split(dx_std, dy, test_size=0.2)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(dx_train, dy_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(dx_test)  # 預測.predict

print(logistic_regression.score(dx_train, dy_train))
print(logistic_regression.score(dx_test, dy_test))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
from sklearn.feature_extraction.text import CountVectorizer
import joblib

train_df = pd.read_csv('Fake_news_data/train.csv')

train_df.dropna()

train_text = train_df['text'].astype(str)
train_label = train_df['label']

count_vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
count_train = count_vectorizer.fit_transform(train_text)

joblib.dump(count_vectorizer, 'count_vectorizer.pkl')

X_train, X_test, Y_train, Y_test = train_test_split(
    count_train, train_label, test_size=0.2)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train, Y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test)  # 預測.predict

print(f"計算準確率 : {accuracy_score(Y_test, y_pred)*100:.2f}%")

joblib.dump(logistic_regression, 'logistic_regression.pkl')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

y = iris.target  # 資料集目標

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.values

# 訓練資料, 測試資料, 訓練目標, 測試目標
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("特徵縮放")
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(logistic_regression, "tmp_my_model_clf1.joblib")
joblib.dump(scaler, "tmp_my_model_scaler1.joblib")

print("------------------------------")  # 30個

print("讀取模型")
# 載入模型與標準化轉換模型
logistic_regression2 = joblib.load("tmp_my_model_clf1.joblib")
scaler = joblib.load("tmp_my_model_scaler1.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]  # 山鳶尾 變色鳶尾 維吉尼亞鳶尾
print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

y = iris.target  # 資料集目標

# 集中
cc = (
    df["sepal length (cm)"].mean(),
    df["sepal length (cm)"].median(),
    df["sepal length (cm)"].mode(),
)
print(cc)

# 計算變異數(variance)、標準差(standard deviation)、IQR
cc = (
    df["sepal length (cm)"].var(),
    df["sepal length (cm)"].std(),
    df["sepal length (cm)"].quantile(0.75) - df["sepal length (cm)"].quantile(0.25),
)
print(cc)
# (0.6856935123042505, 0.8280661279778629, 1.3000000000000007)

# 計算偏態(skewness)及峰度(kurtosis)
cc = df["sepal length (cm)"].skew(), df["sepal length (cm)"].kurt()
print(cc)

# 自行計算偏態
mean1 = df["sepal length (cm)"].mean()
std1 = df["sepal length (cm)"].std()
n = len(df["sepal length (cm)"])
skew1 = (
    (((df["sepal length (cm)"] - mean1) / std1) ** 3).sum() * n / ((n - 1) * (n - 2))
)
print(skew1)

# 0.31491095663697277

# 自行計算峰度
M2 = (((df["sepal length (cm)"] - mean1) / std1) ** 2).mean()
M4 = (((df["sepal length (cm)"] - mean1) / std1) ** 4).mean()
K = M4 / (M2**2)
print(K - 3)

# -0.5735679489249756

from scipy.stats import kurtosis

print(kurtosis(df["sepal length (cm)"], axis=0, bias=True))

# -0.5735679489249765

# 直方圖
sns.histplot(x="sepal length (cm)", data=df)
show()

# 直方圖平滑化
sns.kdeplot(x="sepal length (cm)", data=df)
show()

# 右偏

data1 = np.random.normal(0, 1, 500)
data2 = np.random.normal(5, 1, 100)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
show()

# 右偏

data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(5, 1, 500)
data = np.concatenate((data1, data2))
sns.kdeplot(data=data)
pd.DataFrame(data).skew()
show()

# 關聯度

df["y"] = y
cc = df.corr()
print(cc)

# 箱型圖
sns.boxplot(data=df)
plt.title("鳶尾花資料分布箱型圖")
show()

print("是否有含遺失值(Missing value)")
cc = df.isnull().sum()
print(cc)

print("y 各類別資料筆數統計")
"""
sns.countplot(x=y)
plt.title("y 各類別資料筆數統計")
show()
"""
print("以Pandas函數統計各類別資料筆數")
cc = pd.Series(y).value_counts()
print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.values

# 訓練資料, 測試資料, 訓練目標, 測試目標
# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

print("特徵縮放")
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = logistic_regression.predict(X_test_std)  # 預測.predict

print("計算準確率 測試目標 與 預測目標 接近程度")
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

print("混淆矩陣")
print(confusion_matrix(y_test, y_pred))

print("混淆矩陣圖")
disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=iris.target_names
)
disp.plot()
plt.title("混淆矩陣圖")
show()

print("將 模型存檔 使用 joblib")
joblib.dump(logistic_regression, "tmp_my_model_clf2.joblib")
joblib.dump(scaler, "tmp_my_model_scaler2.joblib")

print("------------------------------")  # 60個

print("讀取模型")
# 載入模型與標準化轉換模型
logistic_regression2 = joblib.load("tmp_my_model_clf2.joblib")
scaler = joblib.load("tmp_my_model_scaler2.joblib")

# 測試資料
sepal_length, sepal_width, petal_length, petal_width = 5.8, 3.5, 4.4, 1.3

X_new = [[sepal_length, sepal_width, petal_length, petal_width]]

""" NG
X_new = scaler.transform(X_new)

labels = ["setosa", "versicolor", "virginica"]  # 山鳶尾 變色鳶尾 維吉尼亞鳶尾
print("### 預測品種是：", labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict
"""

""" 使用 streamlit 與人互動

import streamlit as st

# 設定 st 標題
st.title('鳶尾花（Iris）預測')

# 製作4個 st slider
sepal_length = st.slider('花萼長度:', min_value=3.0, max_value=8.0, value=5.8)
sepal_width = st.slider('花萼寬度:', min_value=2.0, max_value=5.0, value=3.5)
petal_length = st.slider('花瓣長度:', min_value=1.0, max_value=7.0, value=4.4)
petal_width = st.slider('花瓣寬度:', min_value=0.1, max_value=2.5, value=1.3)

if st.button('預測'):  # 當按下 預測 按鈕
    X_new = [[sepal_length,sepal_width,petal_length,petal_width]]
    X_new = scaler.transform(X_new)
    st.write('### 預測品種是：', labels[logistic_regression2.predict(X_new)[0]])  # 預測.predict
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("自建 邏輯迴歸")

# logistic_regression_SGD
# 以梯度下降法求解羅吉斯迴歸

iris = datasets.load_iris()

# 只取前兩個特徵，方便繪圖
X = iris.data[:, :2]
# 只取前兩個類別
y = (iris.target != 0) * 1

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
show()

# 建立羅吉斯迴歸類別


class MyLogisticRegression:
    def __init__(self, lr=0.01, num_iter=100000, fit_intercept=True, verbose=False):
        self.lr = lr
        self.num_iter = num_iter
        self.fit_intercept = fit_intercept
        self.verbose = verbose

    # 加入偏差項(1)至X
    def __add_intercept(self, X):
        intercept = np.ones((X.shape[0], 1))
        return np.concatenate((intercept, X), axis=1)

    # 羅吉斯函數
    def __sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    # 損失函數
    def __loss(self, h, y):
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    # 以梯度下降法訓練模型
    def fit(self, X, y):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        # 權重初始值給 0
        self.theta = np.zeros(X.shape[1])

        # 正向傳導與反向傳導
        for i in range(self.num_iter):
            # WX
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            # 梯度
            gradient = np.dot(X.T, (h - y)) / y.size
            # 更新權重
            self.theta -= self.lr * gradient

            # 依據更新的權重計算損失
            z = np.dot(X, self.theta)
            h = self.__sigmoid(z)
            loss = self.__loss(h, y)

            # 列印損失
            if self.verbose == True and i % 10000 == 0:
                print(f"loss: {loss} \t")

    # 預測機率
    def predict_prob(self, X):
        if self.fit_intercept:
            X = self.__add_intercept(X)

        return self.__sigmoid(np.dot(X, self.theta))

    # 預測
    def predict(self, X):
        return self.predict_prob(X).round()


# 做邏輯迴歸, 自建模型
logistic_regression = MyLogisticRegression(lr=0.1, num_iter=300000)  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict

cc = (y_pred == y).mean()
print(cc)

print("羅吉斯迴歸係數")
print(logistic_regression.theta)
# array([-25.89066442,  12.523156  , -13.40150447])

# 分類結果繪圖
plt.figure(figsize=(10, 6))

plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
x1_min, x1_max = (
    X[:, 0].min(),
    X[:, 0].max(),
)
x2_min, x2_max = (
    X[:, 1].min(),
    X[:, 1].max(),
)
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]

y_pred = logistic_regression.predict_prob(grid).reshape(xx1.shape)

plt.contour(xx1, xx2, y_pred, [0.5], linewidths=1, colors="black")
show()

# 以 Scikit-learn 驗證

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression(C=1e20)  # 邏輯迴歸函數學習機

logistic_regression.fit(X, y)  # 學習訓練.fit

y_pred = logistic_regression.predict(X)  # 預測.predict
cc = (y_pred == y).mean()
print(cc)

cc = logistic_regression.intercept_, logistic_regression.coef_
print(cc)

plt.figure(figsize=(10, 6))
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], color="b", label="0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], color="r", label="1")
plt.legend()
x1_min, x1_max = (
    X[:, 0].min(),
    X[:, 0].max(),
)
x2_min, x2_max = (
    X[:, 1].min(),
    X[:, 1].max(),
)
xx1, xx2 = np.meshgrid(np.linspace(x1_min, x1_max), np.linspace(x2_min, x2_max))
grid = np.c_[xx1.ravel(), xx2.ravel()]
y_pred_prob = logistic_regression.predict_proba(grid)[:, 1].reshape(
    xx1.shape
)  # 預測機率.predict_proba

plt.contour(xx1, xx2, y_pred_prob, [0.5], linewidths=1, colors="black")
show()

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
