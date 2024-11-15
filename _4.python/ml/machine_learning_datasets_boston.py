"""
波士頓房價
506筆資料, 14個欄位
Number of Instances: 506 
Number of Attributes: 13 numeric/categorical predictive.
          Median Value (attribute 14) is usually the target.
Attribute Information (in order):
 - CRIM     per capita crime rate by town
 - ZN       proportion of residential land zoned for lots over 25,000 sq.ft.
 - INDUS    proportion of non-retail business acres per town
 - CHAS     Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
 - NOX      nitric oxides concentration (parts per 10 million)
 - RM       average number of rooms per dwelling
 - AGE      proportion of owner-occupied units built prior to 1940
 - DIS      weighted distances to five Boston employment centres
 - RAD      index of accessibility to radial highways
 - TAX      full-value property-tax rate per $10,000
 - PTRATIO  pupil-teacher ratio by town
 - B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town
 - LSTAT    % lower status of the population
 - MEDV     Median value of owner-occupied homes in $1000's
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

# 波士頓房價資料
# data_url = "http://lib.stat.cmu.edu/datasets/boston"
boston_filename = "data/datasets_boston.csv"  # 上述網址存成的檔案

# from sklearn.datasets import load_boston # 廢棄

print("------------------------------------------------------------")  # 60個

import sklearn
import sklearn.linear_model
from sklearn.model_selection import train_test_split

print("------------------------------------------------------------")  # 60個


def load_boston():
    raw_df = pd.read_csv(boston_filename, sep="\s+", skiprows=22, header=None)
    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]
    # print(data)
    # print(data.shape)
    # print(target)
    feature_names = [
        "CRIM",
        "ZN",
        "INDUS",
        "CHAS",
        "NOX",
        "RM",
        "AGE",
        "DIS",
        "RAD",
        "TAX",
        "PTRATIO",
        "B",
        "LSTAT",
    ]
    boston = pd.DataFrame(data, columns=feature_names)
    # print('boston.head()')
    # print(boston.head())
    target = pd.DataFrame(target, columns=["MEDV"])
    # print('target.head()')
    # print(target.head())
    y = target["MEDV"]
    return boston, y


X, y = load_boston()

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)


feature_names = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]

coef = pd.DataFrame(feature_names, columns=["features"])
coef["estimatedCoefficients"] = linear_regression.coef_
print(coef)

plt.scatter(X.RM, y)
plt.xlabel("每個住宅的平均房間數(RM)")
plt.ylabel("中位數房價(MEDV)")
plt.title("每個住宅的平均房間數和中位數房價的關聯性")

plt.show()

print("------------------------------")  # 30個

predicted_price = linear_regression.predict(X)
print(predicted_price[0:5])

MSE = np.mean((y - predicted_price) ** 2)  # 自己算MSE
print("MSE:", MSE)
print("R-squared:", linear_regression.score(X, y))

plt.scatter(y, predicted_price)
plt.xlabel("中位數房價")
plt.ylabel("預測的中位數房價")
plt.title("中位數房價 vs 預測的中位數房價")

plt.show()

print("------------------------------")  # 30個

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.33, random_state=9487)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(XTrain, yTrain)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

pred_train = linear_regression.predict(XTrain)
pred_test = linear_regression.predict(XTest)

plt.scatter(yTest, pred_test)
plt.xlabel("中位數房價")
plt.ylabel("預測的中位數房價")
plt.title("中位數房價 vs 預測的中位數房價")

plt.show()

MSE_train = np.mean((yTrain - pred_train) ** 2)  # 自己算MSE
MSE_test = np.mean((yTest - pred_test) ** 2)  # 自己算MSE
print("訓練資料的MSE:", MSE_train)
print("測試資料的MSE:", MSE_test)

print("訓練資料的R-squared:", linear_regression.score(XTrain, yTrain))
print("測試資料的R-squared:", linear_regression.score(XTest, yTest))

plt.scatter(pred_train, yTrain - pred_train, c="b", s=40, alpha=0.5, label="訓練資料集")
plt.scatter(pred_test, yTest - pred_test, c="r", s=40, label="測試資料集")
plt.hlines(y=0, xmin=0, xmax=50)
plt.title("殘差圖(Residual Plot)")
plt.ylabel("殘差值(Residual Value)")
plt.legend()

plt.show()

print("------------------------------")  # 30個

sns.set_style(
    "darkgrid", {"axes.axisbelow": False, "font.sans-serif": ["Microsoft JhengHei"]}
)

df = pd.DataFrame({"x": pred_train, "y": yTrain})
df2 = pd.DataFrame({"x": pred_test, "y": yTest})
sns.residplot(x="x", y="y", data=df)
sns.residplot(x="x", y="y", data=df2)
plt.title("殘差圖(Residual Plot)")
plt.ylabel("殘差值(Residual Value)")
# plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

boston, y = load_boston()

boston["MEDV"] = y

"""
sns.distplot(boston.MEDV, bins=30)
plt.show()

correlation_matrix = boston.corr().round(2)
sns.heatmap(correlation_matrix, annot=True)
plt.show()
"""

X = boston.loc[:, "CRIM":"LSTAT"].values
Y = boston.MEDV

x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=9487
)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

y_pred = linear_regression.predict(x_test)

plt.scatter(y_test, y_pred, s=50)
plt.show()

X = boston[["NOX", "AGE", "DIS"]].values

print(boston.columns)

X = boston[
    [
        "CRIM",
        "ZN",
        "INDUS",
        "NOX",
        "RM",
        "AGE",
        "DIS",
        "RAD",
        "TAX",
        "PTRATIO",
        "B",
        "LSTAT",
    ]
].values
print(X)

x_train, x_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.2, random_state=9487
)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

cc = boston[:3]
print(cc)

X = boston

# X = boston.data[:, [5,]]
# X = boston.data
# y = boston.target

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

y_pred = linear_regression.predict(X)

print(linear_regression.coef_)
print(linear_regression.intercept_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

boston, y = load_boston()

X = boston
boston["MEDV"] = y

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

from sklearn.preprocessing import StandardScaler

# boston = load_boston()

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

print("權重值：{}".format(linear_regression.coef_))
print("偏置值：{}\n".format(linear_regression.intercept_))

y_predict = linear_regression.predict(x_test)
y_real = y_test

print(y_predict)
print(y_real)

"""
for i in range(5):
    print("預測值{}：{}，真實值：{}".format(i + 1, y_predict[i], y_real[i]))
"""

# another

from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

std_x = StandardScaler()
x_train = std_x.fit_transform(x_train)
x_test = std_x.transform(x_test)

std_y = StandardScaler()
y_train = y_train
y_test = y_test

sgd = SGDRegressor()
sgd.fit(x_train, y_train)
print("權重值：{}".format(sgd.coef_))
print("偏置值：{}\n".format(sgd.intercept_))

y_predict = sgd.predict(x_test)
y_real = y_test

print(y_predict)

print(y_real)
"""
for i in range(5):
    print("預測值：{}，真實值：{}".format(y_predict[i], y_real[i]))
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X, y = load_boston()

X["MEDV"] = y

print(X.shape)

# print(X[0])
# print(boston.feature_names)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=9487
)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

start = time.perf_counter()

linear_regression.fit(X_train, y_train)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

train_score = linear_regression.score(X_train, y_train)
cv_score = linear_regression.score(X_test, y_test)
print(
    "耗時 : {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}".format(
        time.perf_counter() - start, train_score, cv_score
    )
)

print("------------------------------")  # 30個

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    # linear_regression = LinearRegression(normalize=True)
    # 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
    pipeline = Pipeline(
        [
            ("polynomial_features", polynomial_features),
            ("linear_regression", linear_regression),
        ]
    )
    return pipeline


model = polynomial_model(degree=2)

start = time.perf_counter()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
cv_score = model.score(X_test, y_test)
print(
    "耗時 : {0:.6f}; train_score: {1:0.6f}; cv_score: {2:.6f}".format(
        time.perf_counter() - start, train_score, cv_score
    )
)

print("------------------------------")  # 30個

from common.utils import plot_learning_curve
from sklearn.model_selection import ShuffleSplit

cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=9487)
plt.figure(figsize=(10, 6))
title = "Learning Curves (degree={0})"
degrees = [1, 2, 3]

start = time.perf_counter()
plt.figure(figsize=(10, 6))
for i in range(len(degrees)):
    plt.subplot(1, 3, i + 1)
    plot_learning_curve(
        plt,
        polynomial_model(degrees[i]),
        title.format(degrees[i]),
        X,
        y,
        ylim=(0.01, 1.01),
        cv=cv,
    )

print("耗時 : {0:.6f}".format(time.perf_counter() - start))

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

X, y = load_boston()

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

print(linear_regression.predict(X))
print(linear_regression.coef_)
print(linear_regression.intercept_)
print(linear_regression.get_params())
print(linear_regression.score(X, y))  # R^2 coefficient of determination

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
"""
原本的說明


今天我們要使用的是「波士頓房價資料」。
boston_dataset = load_boston()
print(boston_dataset.DESCR)

boston_dataset.feature_names

array(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD',
,       'TAX', 'PTRATIO', 'B', 'LSTAT'], dtype='<U7')

boston_dataset.data[:5]

array([[6.3200e-03, 1.8000e+01, 2.3100e+00, 0.0000e+00, 5.3800e-01,
,        6.5750e+00, 6.5200e+01, 4.0900e+00, 1.0000e+00, 2.9600e+02,
,        1.5300e+01, 3.9690e+02, 4.9800e+00],
,       [2.7310e-02, 0.0000e+00, 7.0700e+00, 0.0000e+00, 4.6900e-01,
,        6.4210e+00, 7.8900e+01, 4.9671e+00, 2.0000e+00, 2.4200e+02,
,        1.7800e+01, 3.9690e+02, 9.1400e+00],
,       [2.7290e-02, 0.0000e+00, 7.0700e+00, 0.0000e+00, 4.6900e-01,
,        7.1850e+00, 6.1100e+01, 4.9671e+00, 2.0000e+00, 2.4200e+02,
,        1.7800e+01, 3.9283e+02, 4.0300e+00],
,       [3.2370e-02, 0.0000e+00, 2.1800e+00, 0.0000e+00, 4.5800e-01,
,        6.9980e+00, 4.5800e+01, 6.0622e+00, 3.0000e+00, 2.2200e+02,
,        1.8700e+01, 3.9463e+02, 2.9400e+00],
,       [6.9050e-02, 0.0000e+00, 2.1800e+00, 0.0000e+00, 4.5800e-01,
,        7.1470e+00, 5.4200e+01, 6.0622e+00, 3.0000e+00, 2.2200e+02,
,        1.8700e+01, 3.9690e+02, 5.3300e+00]])

boston = pd.DataFrame(boston_dataset.data,
                     columns=boston_dataset.feature_names)

boston.head()

	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33
,

boston['MEDV'] = boston_dataset.target
boston.head()  # 多了一 欄

	CRIM	ZN	INDUS	CHAS	NOX	RM	AGE	DIS	RAD	TAX	PTRATIO	B	LSTAT	MEDV
0	0.00632	18.0	2.31	0.0	0.538	6.575	65.2	4.0900	1.0	296.0	15.3	396.90	4.98	24.0
1	0.02731	0.0	7.07	0.0	0.469	6.421	78.9	4.9671	2.0	242.0	17.8	396.90	9.14	21.6
2	0.02729	0.0	7.07	0.0	0.469	7.185	61.1	4.9671	2.0	242.0	17.8	392.83	4.03	34.7
3	0.03237	0.0	2.18	0.0	0.458	6.998	45.8	6.0622	3.0	222.0	18.7	394.63	2.94	33.4
4	0.06905	0.0	2.18	0.0	0.458	7.147	54.2	6.0622	3.0	222.0	18.7	396.90	5.33	36.2
,

boston.columns
Index(['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
,       'PTRATIO', 'B', 'LSTAT', 'MEDV'],
,      dtype='object')

X = boston[['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']].values

X
array([[6.3200e-03, 1.8000e+01, 2.3100e+00, ..., 1.5300e+01, 3.9690e+02,
,        4.9800e+00],
,       [2.7310e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9690e+02,
,        9.1400e+00],
,       [2.7290e-02, 0.0000e+00, 7.0700e+00, ..., 1.7800e+01, 3.9283e+02,
,        4.0300e+00],
,       ...,
,       [6.0760e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
,        5.6400e+00],
,       [1.0959e-01, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9345e+02,
,        6.4800e+00],
,       [4.7410e-02, 0.0000e+00, 1.1930e+01, ..., 2.1000e+01, 3.9690e+02,
,        7.8800e+00]])


"""
