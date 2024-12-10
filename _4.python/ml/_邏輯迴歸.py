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

from common1 import *
import sklearn.linear_model
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler  # 特徵縮放
from sklearn.metrics import confusion_matrix  # 混淆矩陣
from sklearn.metrics import ConfusionMatrixDisplay  # 混淆矩陣圖


from sklearn import metrics


def show():
    plt.show()
    pass


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

print(logistic_regression.predict_proba([[0]])[:, 1])
print(logistic_regression.predict_proba([[0], [1], [2]])[:, 1])

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

# 3. 不須進行特徵工程

# 4. 資料分割

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
"""
print("測試資料")
print(X)
print("真實答案")
print(y)
print("預測結果")
print(y_pred)
"""
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
Z = logistic_regression.predict(np.c_[xx.ravel(), yy.ravel()])
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
    preds = np.round(y_hat)

    accu = np.sum(preds == y) * 1.0 / len(y)
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

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

logistic_regression = sklearn.linear_model.LogisticRegression(
    solver="liblinear"
)  # 邏輯迴歸函數學習機
logistic_regression.fit(X_train, y_train)

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

# 3. 不須進行特徵工程

# 4. 資料分割

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

# 3. 不須進行特徵工程

# 4. 資料分割

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

# 3. 不須進行特徵工程

# 4. 資料分割

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
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

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
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

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

# 3. 不須進行特徵工程

# 4. 資料分割

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
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

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
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_blobs  # 集群資料集

N = 500
print("產生", N, "筆資料 2維 2群")
dx, dy = make_blobs(n_samples=N, n_features=2, centers=2, random_state=0)

scaler = StandardScaler()
dx_std = scaler.fit_transform(dx)  # STD特徵縮放

dx_train, dx_test, dy_train, dy_test = train_test_split(
    dx_std, dy, test_size=0.2, random_state=0
)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

logistic_regression.fit(dx_train, dy_train)  # 學習訓練.fit

predictions = logistic_regression.predict(dx_test)  # 預測.predict

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
    count_train, train_label, test_size=0.2, random_state=7)

classifier = LogisticRegression()
classifier.fit(X_train, Y_train)
pred = classifier.predict(X_test)

print(f"計算準確率 : {accuracy_score(Y_test, pred)*100:.2f}%")

joblib.dump(classifier, 'classifier.pkl')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 06_04_logistic_regression_with_nonlinear_data

# 以二次迴歸預測世界人口數

from sklearn.datasets import make_circles

X, y = make_circles(n_samples=1_000, factor=0.3, noise=0.05, random_state=0)

# 資料切割
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)

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

logistic_regression = LogisticRegression()

logistic_regression.fit(X_train, y_train)

# cc = logistic_regression.coef_, lr.intercept_
# print(cc)

y_pred = logistic_regression.predict(X_test)
print(f"計算準確率 : {accuracy_score(y_test, y_pred)*100:.2f}%")
# 48.80%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data, label = make_blobs(n_samples=1000, n_features=2, centers=2, random_state=9487)

d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
lo_model = LogisticRegression()

# 建立訓練數據模型
lo_model.fit(dx_train, label_train)  # 學習訓練.fit

# 對測試數據做預測
pred = lo_model.predict(dx_test)

# 輸出測試數據的 label
print(label_test)

# 輸出預測數據的 label
print(pred)

# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

data, label = make_blobs(n_samples=200, n_features=2, centers=2, random_state=9487)

d_sta = StandardScaler().fit_transform(data)  # 標準化

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
dx_train, dx_test, label_train, label_test = train_test_split(
    d_sta, label, test_size=0.2, random_state=9487
)
# 訓練組8成, 測試組2成

# 建立分類模型
lo_model = LogisticRegression()

# 建立訓練數據模型
lo_model.fit(dx_train, label_train)  # 學習訓練.fit

# 對測試數據做預測
pred = lo_model.predict(dx_test)

# 輸出測試數據的 label
print(label_test)

# 輸出預測數據的 label
print(pred)

# 輸出準確性
print(f"訓練資料的準確性 = {lo_model.score(dx_train, label_train)}")
print(f"測試資料的準確性 = {lo_model.score(dx_test, label_test)}")

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


# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
logistic_regression = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機
