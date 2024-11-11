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

import sklearn.linear_model

print("------------------------------------------------------------")  # 60個
'''
# 尋找銀行行銷活動目標客戶

from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("./data/banking.csv")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# y 各類別資料筆數統計

sns.countplot(x="y", data=df)
plt.show()

# y 各類別資料筆數統計
cc = df.y.value_counts()
print(cc)

series1 = df.y.value_counts()
series1.plot.pie(figsize=(6, 6), autopct="%1.1f%%")
plt.legend()
plt.show()

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

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# ((32950, 63), (8238, 63), (32950,), (8238,))

# 特徵縮放

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 91.53%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectKBest 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

X, y = datasets.load_iris(return_X_y=True)
print(X.shape)

# (150, 4)

# SelectKBest 特徵選取

clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# (150, 2)

# 顯示特徵分數
cc = clf.scores_
print(cc)

# 顯示 p value
print(clf.pvalues_)

# 顯示特徵名稱

ds = datasets.load_iris()
cc = np.array(ds.feature_names)[clf.scores_.argsort()[-2:][::-1]]
print(cc)

X = pd.DataFrame(ds.data, columns=ds.feature_names)
clf = SelectKBest(chi2, k=2)
X_new = clf.fit_transform(X, y)
cc = clf.get_feature_names_out()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇2個特徵
X = X[clf.get_feature_names_out()].values

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix(y_test, y_pred), display_labels=ds.target_names
)
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SelectPercentile 單變數特徵選取(Univariate feature selection)

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import SelectPercentile, chi2

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# SelectPercentile 特徵選取

clf = SelectPercentile(chi2, percentile=10)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 71.94%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 98.33%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
GenericUnivariateSelect 單變數特徵選取(Univariate feature selection)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import GenericUnivariateSelect, chi2

X, y = datasets.load_digits(return_X_y=True)
print(X.shape)

# GenericUnivariateSelect 特徵選取

# 使用 SelectKBest, 20 個特徵
clf = GenericUnivariateSelect(chi2, mode="k_best", param=20)
X_new = clf.fit_transform(X, y)
print(X_new.shape)

# 顯示特徵分數
print(clf.scores_)

# 顯示 p value
print(clf.pvalues_)

# 3. 不須進行特徵工程

# 4. 資料分割

# 選擇部份特徵
X = X_new

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_digits(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (1437, 64) (360, 64) (1437,) (360,)
# 97.22%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
遞迴特徵消去法(Recursive feature elimination)
"""

from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.feature_selection import RFE
from sklearn.svm import SVC

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

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
cc = X_train.shape, X_test.shape, y_train.shape, y_test.shape
print(cc)

# 特徵縮放

scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

# 計算準確率
print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# 93.33%

# 混淆矩陣
from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, y_pred))

# 混淆矩陣圖
from sklearn.metrics import ConfusionMatrixDisplay

disp = ConfusionMatrixDisplay(confusion_matrix=confusion_matrix(y_test, y_pred))
disp.plot()
plt.show()

# 使用全部特徵

X, y = datasets.load_iris(return_X_y=True)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# 特徵縮放
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = clf.predict(X_test_std)  # 預測.predict

print(f"{accuracy_score(y_test, y_pred)*100:.2f}%")

# (120, 4) (30, 4) (120,) (30,)
# 96.67%

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

num_pos = 500

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], num_pos)
subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))
y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y)

plt.show()

print('------------------------------')	#30個

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X, y)  # 學習訓練.fit

y_pred = clf.predict(X)  # 預測.predict

print(np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1)) * 1.0 / len(y))
# 0.99

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y, y_pred))
# [[495   5]
# [  5 495]]

print('------------------------------')	#30個

# 繪制分類邊界


def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8)
    plt.title(title)
    plt.show()

# 預測.predict
plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

print('------------------------------')	#30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


def logistic_regression(X, y, l_rate, iterations, add_intercept=True):
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

        if epoch % 100 == 0:
            print("After iter {}; accuracy: {}".format(epoch + 1, accu))
    return theta, accu_history


theta, accu = logistic_regression(X, y, 1, 2000)

print(accu)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import matplotlib

plt.style.use("bmh")
colors = ["#A60628", "#467821"]
plt.cmap = matplotlib.colors.ListedColormap(colors)

matplotlib.rcParams["figure.figsize"] = (10.0, 6.0)

num_pos = 500

# Bivariate normal distribution mean [0, 0] [0.5, 4], with a covariance matrix

subset1 = np.random.multivariate_normal([0, 0], [[1, 0.6], [0.6, 1]], num_pos)

subset2 = np.random.multivariate_normal([0.5, 4], [[1, 0.6], [0.6, 1]], num_pos)

X = np.vstack((subset1, subset2))

y = np.hstack((np.zeros(num_pos), np.ones(num_pos)))

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cmap, marker="o", s=40)

plt.show()

# 做邏輯迴歸, 用 sklearn 裡的 LogisticRegression 來做邏輯迴歸
clf = sklearn.linear_model.LogisticRegression()  # 邏輯迴歸函數學習機

clf.fit(X, y)  # 學習訓練.fit

print(clf.intercept_, clf.coef_, clf.classes_)
# (array([-5.7268742]), array([[-1.43492343,  3.15471817]]), array([0., 1.]))

y_pred = clf.predict(X)  # 預測.predict
print(y_pred.shape)
print(np.sum(y_pred.reshape(-1, 1) == y.reshape(-1, 1)) * 1.0 / len(y))

# (1000L,)
# 0.99

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y, y_pred))
sns.heatmap(confusion_matrix(y, y_pred))

plt.show()

"""
[[495   5]

 [  5 495]]
"""

# 繪制分類邊界
plt.style.use("bmh")


def plot_decision_boundary(pred_func, X, y, title):
    # Set min and max values and give it some padding
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    h = 0.01
    # Generate a grid of points with distance h between them
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    # Predict the function value for the whole grid (get class for each grid point)
    Z = pred_func(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    # print(Z)
    # Plot the contour and training examples
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=40, alpha=0.8, cmap=plt.cmap)
    plt.title(title)
    plt.show()


# run on the training dataset with predict function

# 預測.predict
plot_decision_boundary(lambda x: clf.predict(x), X, y, "logistic regression prediction")

plt.show()

print("------------------------------")  # 30個


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def log_likelihood(X, y, theta):
    scores = np.dot(X, theta)
    ll = np.sum(y * scores - np.log(1 + np.exp(scores)))
    return ll


def logistic_regression(X, y, l_rate, iterations, add_intercept=True):
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

        if epoch % 5 == 0:
            print("After iter {}; accuracy: {}".format(epoch + 1, accu))

    return theta, accu_history


theta, accu = logistic_regression(X, y, 1, 500)

print(theta)

"""
array([[-599.88926069],
,       [-181.5414528 ],
,       [ 328.95859873]])
"""
print(accu)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_csv("C:/_git/vcs/_4.python/__code/Python-PM2.5-DataAnalyzing-master/data/200811-201811c.csv")
cc = df.head()
print(cc)
# Danger分類點說明
# 對敏感族群不健康為PM2.5數值在35.5以上

# 用heatmap(.isnull())來找出缺失的資料在哪些欄位

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap="viridis")

plt.show()

print("------------------------------")  # 30個

# 用countplot來看Nox是否影響健康

sns.countplot(x="Danger", hue="Nox", data=df, palette="RdBu_r")

plt.show()

print("------------------------------")  # 30個

# 用直方圖看年齡分佈。缺失資料在此不計。

sns.distplot(df["PM25"].dropna(), kde=False, bins=30)

plt.show()

print("------------------------------")  # 30個

# 用直方圖看Nox的分佈

df["Nox"].hist(bins=40, figsize=(10, 4))

plt.show()

print("------------------------------")  # 30個

X = df.drop("Danger", axis=1)
y = df["Danger"]

# 將資料分成訓練組及測試組
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.75, random_state=42
)  # 訓練組2.5成, 測試組7.5成

print(X.shape)
print(y.shape)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# 載入邏輯迴歸，並訓練模型
from sklearn.linear_model import LogisticRegression

logistic_regression = LogisticRegression(solver="liblinear")
logistic_regression.fit(X_train, y_train)

predictions = logistic_regression.predict(X_test)

from sklearn.metrics import classification_report

print(classification_report(y_test, predictions))


from sklearn.metrics import confusion_matrix

cc = confusion_matrix(y_test, predictions)
print(cc)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
