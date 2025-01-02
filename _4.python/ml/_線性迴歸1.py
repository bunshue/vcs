"""
機器學習：建立線性迴歸資料與預測

線性迴歸（linear regression)
    Finding the curve that best fits your data is called regression,
    and when that curve is a straight line, it's called linear regression.
    找出符合資料規律的直線，就叫線性迴歸。

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

建立迴歸資料 make_regression

資料分為
一維Xy 畫X-y
多維Xy 畫y-y_pred
一維df 畫df-y
多維df 畫y-y_pred

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
from sklearn import linear_model
import sklearn.linear_model
from sklearn import datasets
from sklearn import preprocessing
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso


def show():
    # return
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

print("測試 PolynomialFeatures")

# 使用 PolynomialFeatures 產生多項式
from sklearn.preprocessing import PolynomialFeatures

X = np.array([[1.0, 2.0, 3.0]])

for DEGREE in range(5):
    print(DEGREE, "次方")
    poly = PolynomialFeatures(degree=DEGREE)  # DEGREE 次方
    print("原陣列 :", X)
    X_poly = poly.fit_transform(X)  # 轉換
    print("轉換後 :", X_poly)
    print(X_poly.shape)

print("------------------------------------------------------------")  # 60個

# 簡單資料 y = x
xx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
xx2d = np.array(
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]
)

yy0 = xx  # 理想資料, y = x
yy1 = np.array([0, 1, 4, 3, 4, 5, 6, 3, 8, 9, 10])  # 真實資料

"""
# 複雜資料 f(x) = sin(3.2x) + 0.8x
N = 50
xx = np.linspace(0, 5, N)
yy0 = np.sin(3.2 * x) + 0.8 * x
yy1 = np.sin(3.2 * x) + 0.8 * x + 0.3 * np.random.randn(N)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 一維Xy 畫X-y
print("資料來源 : 建立迴歸資料 make_regression 1 無 / 有 資料分割")

N = 100  # n_samples, 樣本數
M = 1  # n_features, 特徵數(資料的維度)
print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y = datasets.make_regression(n_samples=N, n_features=M, n_targets=1, noise=10)
# X, y = datasets.make_regression(n_samples=N, n_features=M, noise=10)
# N個樣本, M種特徵(features), 1種標籤類別(target), noise為分散程度

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# 全部資料, 訓練預測畫圖
print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 一維Xy")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

plt.subplot(211)
plt.scatter(X, y, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(X, y_pred, c="r", lw=5, label="線性迴歸1")

XX = np.array([-3, 3])
YY = XX * linear_regression.coef_ + linear_regression.intercept_
plt.plot(XX, YY, c="g", label="線性迴歸2")

plt.title("線性迴歸 一維Xy 無分割")
plt.legend()

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 分割資料, 訓練預測畫圖
print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 一維Xy")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict

plt.subplot(212)
plt.scatter(X, y, s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(x_test, y_pred, c="r", label="線性迴歸")
plt.title("線性迴歸 一維Xy 有分割")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多維線性回歸
# 多維Xy 畫y-y_pred

N = 10  # n_samples, 樣本數
M = 3  # n_features, 特徵數(資料的維度)
print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y = datasets.make_regression(n_samples=N, n_features=M)
# X : N X M 陣列, y : N X 1 陣列

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

plt.plot(y, color="r", lw=10, label="真實資料")
plt.plot(y_pred, color="g", lw=4, label="預測結果")
print("多維Xy 畫y-y_pred")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多維Xy 畫y-y_pred
# multi_variables_nonlinear_regression
# 多元非線性迴歸(Multiple Non-Linear Regression)

# N = 300  # n_samples, 樣本數
N = 30  # n_samples, 樣本數
M = 2  # n_features, 特徵數(資料的維度)
print("make_regression,", N, "個樣本, ", M, "個特徵")

X, y = datasets.make_regression(n_samples=N, n_features=M, noise=50)
# N個樣本, M種特徵(features), 1種標籤類別(target), noise為分散程度

print(X)
print(type(X))
print(X.shape)

plt.scatter(X[:, 0], X[:, 1], s=30, c="b", label="真實資料")  # 真實資料, 藍點
plt.show()

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
# plt.rcParams["legend.fontsize"] = 10
ax.plot(X[:, 0], X[:, 1], y, "o", markersize=8, color="blue", alpha=0.5)
plt.xlabel("x")
plt.ylabel("y")
plt.title("測試資料")
show()

# 使用 PolynomialFeatures 產生多項式
from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree=2)  # 2 次方
X_new = poly.fit_transform(X)  # 轉換

print(X_new)
print(type(X_new))
print(X_new.shape)

cc = poly.get_feature_names_out(["x1", "x2"])
print(cc)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X_new, y, test_size=0.2)

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X_train_std), type(y_train))
print("資料大小 :", X_train_std.shape, y_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test_std)  # 預測.predict

# 使用原始特徵的模型評分

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X_train_std), type(y_train))
print("資料大小 :", X_train_std.shape, y_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test_std)  # 預測.predict

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多維df 資料來源 : 自建資料 5 做成df, 二維資料 線性迴歸")

# 多維df 畫y-y_pred

xxx = np.array(
    [
        [67, 160],
        [68, 165],
        [70, 167],
        [65, 170],
        [80, 165],
        [85, 167],
        [78, 178],
        [79, 182],
        [95, 175],
        [89, 172],
    ]
)
yyy = np.array([50, 60, 65, 65, 70, 75, 80, 85, 90, 81])

X = pd.DataFrame(xxx, columns=["第一欄", "第二欄"])  # DataFrame
target = pd.DataFrame(yyy, columns=["目標"])
y = target["目標"]  # Series

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

# 預測 第一欄 和 第二欄 [66,164],[82,172] 的 目標
# new_df = pd.DataFrame(np.array([[66, 164], [82, 172]]), columns=["第一欄", "第二欄"])
# y_pred = linear_regression.predict(new_df)  # 預測.predict

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict, 傳入df

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7a")

# 一維Xy 畫X-y

x = xx
y0 = yy0  # 理想資料
y = yy1  # 真實資料

X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列
# y = y.reshape(len(y), 1) 可以不用

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 一維Xy")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

plt.subplot(211)
plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線
plt.title("線性迴歸 一維Xy")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

print("------------------------------")  # 30個

print("一維df 資料來源 : 自建資料 2 做成df")
# 一維df 畫df-y
xxx = xx
yy0 = yy0  # 理想資料
yyy = yy1  # 真實資料

X = pd.DataFrame(xxx, columns=["第一欄"])  # DataFrame

target = pd.DataFrame(yyy, columns=["目標"])
y = target["目標"]  # Series

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 一維df")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict, 傳入df

plt.subplot(212)
plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(xxx, yyy, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(X["第一欄"], y_pred, color="r", marker="o", markersize=8, label="線性迴歸")
plt.title("線性迴歸 一維df")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7c SVR(linear) 迴歸")

# 一維Xy 畫X-y

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料
X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列

# 迴歸, 用 sklearn 裡的 SVR 的 linear 來做迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

print("資料型態 :", type(X), type(y1))
print("資料大小 :", X.shape, y1.shape)
print("迴歸型態 : 一維Xy")
svr_lin.fit(X, y1)  # 學習訓練.fit, SVR(linear) 迴歸

y_pred_lin = svr_lin.predict(X)  # 預測.predict, SVR(linear)

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred_lin, color="r", marker="o", markersize=8, label="SVR線性迴歸")  # SVR線性迴歸

plt.title("SVR(linear) 迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7c SVR(rbf/linear/poly) 迴歸")

# 一維Xy 畫X-y

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料
X = x.reshape(len(x), 1)  # x訓練資料要轉為 NX1 陣列

# 迴歸, 用 sklearn 裡的 SVR 的 rbf 來做迴歸
svr_rbf = sklearn.svm.SVR(kernel="rbf", C=1e3, gamma=0.3)  # SVR 函數學習機, rbf

# 迴歸, 用 sklearn 裡的 SVR 的 linear 來做迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

# 迴歸, 用 sklearn 裡的 SVR 的 poly 來做迴歸
svr_poly = sklearn.svm.SVR(kernel="poly", C=1e3, degree=4)  # SVR 函數學習機, poly

print("資料型態 :", type(X), type(y1))
print("資料大小 :", X.shape, y1.shape)
svr_rbf.fit(X, y1)  # 學習訓練.fit, SVR(rbf) 迴歸
print("資料型態 :", type(X), type(y1))
print("資料大小 :", X.shape, y1.shape)
svr_lin.fit(X, y1)  # 學習訓練.fit, SVR(linear) 迴歸
print("資料型態 :", type(X), type(y1))
print("資料大小 :", X.shape, y1.shape)
svr_poly.fit(X, y1)  # 學習訓練.fit, SVR(poly) 迴歸

y_pred_rbf = svr_rbf.predict(X)  # 預測.predict, SVR(rbf)
y_pred_lin = svr_lin.predict(X)  # 預測.predict, SVR(linear)
y_pred_poly = svr_poly.predict(X)  # 預測.predict, SVR(poly)

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.plot(x, y_pred_rbf, color="m", marker="o", markersize=8, label="rbf")  # SVR(rbf)
plt.plot(
    x, y_pred_lin, color="r", marker="o", markersize=8, label="linear"
)  # SVR(linear)
plt.plot(x, y_pred_poly, color="y", marker="o", markersize=8, label="poly")  # SVR(poly)
plt.title("SVR(rbf/linear/poly) 迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 使用 Radial Basis Function (RBF)
# （高斯）徑向基函數核（英語：Radial basis function kernel），或稱為RBF核
def RBF(x, center, sigma):
    k = np.exp(-((x - center) ** 2) / (2 * sigma**2))
    return k


print("資料來源 : 自建資料 7d 線性/多項式/RBF")

x = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X = x.reshape(len(x), 1)

print("資料型態 :", type(X), type(y1))
print("資料大小 :", X.shape, y1.shape)
linear_regression.fit(X, y1)  # 學習訓練.fit

# 使用 6 次多項式 學習
X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])

regression_poly = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X_poly), type(y1))
print("資料大小 :", X_poly.shape, y1.shape)
regression_poly.fit(X_poly, y1)  # 學習訓練.fit

# 使用 RBF
sigma = 0.3
X_rbf = np.array(
    [
        [
            RBF(k, 0.5, sigma),
            RBF(k, 1.5, sigma),
            RBF(k, 2.5, sigma),
            RBF(k, 3.5, sigma),
            RBF(k, 4.5, sigma),
        ]
        for k in x
    ]
)

regression_rbf = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X_rbf), type(y1))
print("資料大小 :", X_rbf.shape, y1.shape)
regression_rbf.fit(X_rbf, y1)  # 學習訓練.fit

y_pred_lin = linear_regression.predict(X)  # 預測.predict
y_pred_poly = regression_poly.predict(X_poly)  # 預測.predict
y_pred_rbf = regression_rbf.predict(X_rbf)  # 預測.predict

plt.plot(x, y0, color="lime", label="理想資料")  # 理想資料
plt.plot(x, y1, color="m", marker="o", markersize=8, label="真實資料")  # 線性迴歸曲線
plt.plot(x, y_pred_lin, "r", label="線性學習機 預測結果")
plt.plot(x, y_pred_poly, "g", label="6次多項式 預測結果")
plt.plot(x, y_pred_rbf, "b", label="RBF 預測結果")

plt.title("各種方法比較")
plt.legend()
plt.grid()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多維Xy df格式轉多維ndarray 資料來源 : 內建資料 1 計程車小費資料集EDA")

# 多維Xy 畫y-y_pred

"""
計程車小費資料集EDA  共244筆資料, 7個欄位
total_bill 全部車資
tip        小費
sex        性別
smoker     是否抽煙
day        週間
time       午晚
size
"""

df = sns.load_dataset("tips")

print(df.columns)  # df 的所有欄位名稱
# df.info()  # 這樣就已經把結果印出來

# 資料清理、資料探索與分析
# 類別變數轉換為數值
# 性別: "Female" / "Male" => 0 / 1, 字串 => 整數
# 抽菸: "No" / "Yes" => 0 / 1, 字串 => 整數
# 週間: "Thur" / "Fri" / "Sat" / "Sun" => 1 / 2 / 3 / 4, 字串 => 整數
# 午晚: "Lunch" / "Dinner" => 0 / 1, 字串 => 整數
cc = df.head()
print("資料整理前 :")
print(cc)

print("資料整理")
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

cc = df.head()
print("資料整理後 :")
print(cc)
print("就是把4個欄位裡面的字串轉成數值")

print("找出df的內容是否有NA")
cc = df.isna()  # 找出df的內容是否為NA
# print(cc)
cc = df.isna().sum()  # 加總df的內容是否為NA 可知是否把所有欄位皆無空資料
# print(cc)

# 指定X，並轉為 Numpy 陣列
X = df.drop("tip", axis=1).values  # 砍掉 tip 欄位 => 資料
y = df.tip.values  # tip 欄位 取出來 => 目標
# print(X)
# print(y)

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 特徵縮放 => StandardScaler() 調整成 mean = 0, sd = 1
scaler = preprocessing.StandardScaler()

x_train_std = scaler.fit_transform(x_train)  # 特徵縮放
x_test_std = scaler.transform(x_test)  # 特徵縮放

print("訓練資料 特徵縮放前, mean = ", x_train.mean(), ", sd = ", x_train.std())
print("訓練資料 特徵縮放後, mean = ", x_train_std.mean(), ", sd = ", x_train_std.std())
print("測試資料 特徵縮放前, mean = ", x_test.mean(), ", sd = ", x_test.std())
print("測試資料 特徵縮放後, mean = ", x_test_std.mean(), ", sd = ", x_test_std.std())

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x_train_std), type(y_train))
print("資料大小 :", x_train_std.shape, y_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(x_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test_std)  # 預測.predict

# 評估
print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

# 畫圖
plt.plot(y_test, color="r", lw=4, label="真實資料")
plt.plot(y_pred, color="g", lw=4, label="預測結果")
print("多維Xy 畫y_test-y_pred")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多維Xy df格式轉多維ndarray 空氣盒子 多元線性回歸(Multiple Linear Regression)")

# 多維Xy 畫y-y_pred

# 空氣盒子
# 共 15188 筆資料, 16欄位
df = pd.read_excel("data/20160101-20190101(Daily)迴歸分析.xlsx")
"""
print(df.columns)  # df 的所有欄位名稱
print(df.dtypes)  # df 的欄位的資料型態
print(df.isnull().sum())  # 有無空白欄位 總和
print(df.isnull().any())  # 有無空白欄位 任何
"""
print("資料長度")
print(len(df))
print(len(df["PM25"]))

# df.info()  # 這樣就已經把結果印出來

cc = df.set_index("Date")  # 將Date欄位設定為索引欄位

# 指定X，並轉為 Numpy 陣列
# 取出一些欄位 => 資料 (ndarray)
x = df[
    [
        "SO2",
        "CO",
        "O3",
        "PM10",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
].values

y = df["PM25"].values  # PM25 欄位 取出來 => 目標 (ndarray)

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# x_train為13維陣列資料, y_train為1維陣列資料
print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

"""
sns.heatmap(df.corr())
show()
cc = df.corr()
print(cc)
"""

y_pred = linear_regression.predict(x_test)  # 預測.predict

# 評估
print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

# 畫圖 資料太多, 畫前50個
plt.plot(y_test[:50], color="r", lw=4, label="真實資料")
plt.plot(y_pred[:50], color="g", lw=4, label="預測結果")
print("多維Xy 畫y_test-y_pred")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 20190305-空氣盒子數據Scikit-Learn線性迴歸實作

# 多維df 畫y-y_pred

df = pd.read_csv("data/200811-201811a.csv")  # 共有 1447 筆資料

X = df["PM25"].values.reshape(-1, 1)  # 轉成 1447 X 1
y = df["CO"].values.reshape(-1, 1)  # 轉成 1447 X 1

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict

# 評估
print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

# 畫圖 資料太多, 畫前50個
plt.plot(y_test[:50], color="r", lw=4, label="真實資料")
plt.plot(y_pred[:50], color="g", lw=4, label="預測結果")
print("多維Xy 畫y_test-y_pred")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多維df 畫y-y_pred

df = pd.read_csv("data/200811-201811a.csv")
"""
print(df)

cc = df.describe()
print(cc)

cc = df.isnull().any()
print(cc)
"""
df = df.fillna(method="ffill")  # 將空值填入, ffill()拿前一個值往下填, 承上
print(df)

y = df["PM25"].values

print("------------------------------")  # 30個

# 訓練線性模型

# X是想探索的自變數，Y是依變數。

X = df[
    [
        "SO2",
        "CO",
        "O3",
        "Nox",
        "NO",
        "NO2",
        "THC",
        "NMHC",
        "CH4",
        "WindSpeed",
        "TEMP",
        "Humidity",
    ]
]

y = df["PM25"]

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

""" NG
coeff_df = pd.DataFrame(linear_regression.coef_,X.columns,columns=['Coefficient'])  
print(coeff_df)
"""

# 列出訓練的變數
print(x_train.columns)

y_pred = linear_regression.predict(x_test)  # 預測.predict

# 看實際值及預測值之間的殘差分佈圖
sns.distplot((y_test - y_pred))
show()

# 評估
print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

# 畫圖 資料太多, 畫前50個
plt.plot(np.array(y_test[:50]), color="r", lw=4, label="真實資料")
plt.plot(y_pred[:50], color="g", lw=4, label="預測結果")
print("多維df/Xy 畫y_test-y_pred")
plt.legend()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 2008年11月至2018年11月資料清洗

df = pd.read_csv("data/200811-201811a.csv")

# df.dtypes

df["SO2"] = pd.to_numeric(df.SO2, errors="coerce")
df["CO"] = pd.to_numeric(df.CO, errors="coerce")
# df["CO2"] = pd.to_numeric(df.CO2, errors='coerce')
df["O3"] = pd.to_numeric(df.O3, errors="coerce")
df["PM25"] = pd.to_numeric(df.PM25, errors="coerce")
df["Nox"] = pd.to_numeric(df.Nox, errors="coerce")
df["NO"] = pd.to_numeric(df.NO, errors="coerce")
df["NO2"] = pd.to_numeric(df.NO2, errors="coerce")
df["THC"] = pd.to_numeric(df.THC, errors="coerce")
df["NMHC"] = pd.to_numeric(df.NMHC, errors="coerce")
df["CH4"] = pd.to_numeric(df.CH4, errors="coerce")
df["WindSpeed"] = pd.to_numeric(df.WindSpeed, errors="coerce")
df["TEMP"] = pd.to_numeric(df.TEMP, errors="coerce")
df["Humidity"] = pd.to_numeric(df.Humidity, errors="coerce")

# 處理缺失值
df = df.fillna(0)

# 檢查屬性是否已經改變
# df.dtypes

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("多元线性回归(Multiple Linear Regression)")

# 多維Xy 畫y-y_pred

# 檔案 => df => np.ndarray
df = pd.read_csv("data/50_Startups.csv")
X = df.iloc[:, :-1].values  # 全部資料
Y = df.iloc[:, 4].values  # 第4欄的全部資料(收益)
Z = df.iloc[:, 0].values  # 第0欄的全部資料(R&D花費)

# 缺失資料之處理
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=0.0, strategy="mean")
imputer = imputer.fit(X[:, 0:3])
X[:, 0:3] = imputer.transform(X[:, 0:3])
print(X)

# 将类别数据数字化

# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

labelencoder = LabelEncoder()
print("original:")
print(X[:10])
# print(X[: , 3])
X[:, 3] = labelencoder.fit_transform(X[:, 3])
# print(X[: , 3])
print("labelencoder:")
print(X[:10])
ct = ColumnTransformer([("encoder", OneHotEncoder(), [3])], remainder="passthrough")
X = ct.fit_transform(X)
# onehotencoder = OneHotEncoder(categorical_features = [3])
# X = onehotencoder.fit_transform(X).toarray()
print("onehot:")
print(X[:10])

"""
躲避虚拟变量陷阱
在回归预测中我们需要所有的数据都是numeric的，但是会有一些非numeric的数据，
比如国家，省，部门，性别。这时候我们需要设置虚拟变量（Dummy variable）。
做法是将此变量中的每一个值，衍生成为新的变量，是设为1，否设为0.
举个例子，“性别”这个变量,我们可以虚拟出“男”和”女”两虚拟变量，
男性的话“男”值为1，”女”值为0；女性的话“男”值为0，”女”值为1。
但是要注意，这时候虚拟变量陷阱就出现了。
就拿性别来说，其实一个虚拟变量就够了，比如 1 的时候是“男”， 0 的时候是”非男”，即为女。
如果设置两个虚拟变量“男”和“女”，语义上来说没有问题，可以理解，
但是在回归预测中会多出一个变量，多出的这个变量将会对回归预测结果产生影响。
一般来说，如果虚拟变量要比实际变量的种类少一个。
在多重线性回归中，变量不是越多越好，而是选择适合的变量。这样才会对结果准确预测。
如果category类的特征都放进去，拟合的时候，所有权重的计算，都可以有两种方法实现，
一种是提高某个category的w，一种是降低其他category的w，这两种效果是等效的，
也就是发生了共线性,虚拟变量系数相加和为1，出现完全共线陷阱。
但是下面测试尽然和想法不一致。。。
"""

# Avoiding Dummy Variable Trap
X1 = X[:, 1:]

print(X1)
print(X)

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
x1_train, x1_test, y1_train, y1_test = train_test_split(X1, Y, test_size=0.2)

# 多元線性回歸(Multiple Linear Regression)")
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

linear_regression2 = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x1_train), type(y1_train))
print("資料大小 :", x1_train.shape, y1_train.shape)
print("迴歸型態 : 多維Xy")
linear_regression2.fit(x1_train, y1_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict
y1_pred = linear_regression2.predict(x1_test)  # 預測.predict
print(y_pred)
print(y1_pred)

print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG OneHotEncoder
# 檔案 => df => np.ndarray
df = pd.read_csv("data/50_Startups.csv")
X = df.iloc[:, :-1].values  # 全部資料
Y = df.iloc[:, 4].values  # 第4欄的全部資料(收益)

# 将类别数据数字化

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features=[3])
X = onehotencoder.fit_transform(X).toarray()

# 躲避虚拟变量陷阱

X = X[:, 1:]

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(x_train), type(y_train))
print("資料大小 :", x_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(x_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict
print(y_pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 多維df 畫y-y_pred

# regularization_housing
# 過度擬合與regularization
# 載入房價資料集

train_df = pd.read_csv("./data/house_train.csv", index_col="ID")

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X_train), type(y_train))
print("資料大小 :", X_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X_train, y_train)  # 學習訓練.fit

print(f"訓練判定係數: {linear_regression.score(X_train, y_train)}")
print(f"測試判定係數: {linear_regression.score(X_test, y_test)}")

y_pred = linear_regression.predict(X_test)  # 預測.predict

# 訓練判定係數: 0.7268827869293253
# 測試判定係數: 0.7254687959254533

# 生成新特徵，為舊特徵的平方

# 指定 X、Y
X = train_df.drop("medv", axis=1)
y = train_df["medv"]

# 生成新特徵，為舊特徵的平方
X["crim_2"] = X["crim"] ** 2
X["zn_2"] = X["zn"] ** 2
X["indus_2"] = X["indus"] ** 2
X["chas_2"] = X["chas"] ** 2
X["nox_2"] = X["nox"] ** 2
X["rm_2"] = X["rm"] ** 2
X["age_2"] = X["age"] ** 2
X["dis_2"] = X["dis"] ** 2
X["rad_2"] = X["rad"] ** 2
X["tax_2"] = X["tax"] ** 2
X["ptratio_2"] = X["ptratio"] ** 2
X["black_2"] = X["black"] ** 2
X["lstat_2"] = X["lstat"] ** 2

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

# 建立管線
steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", LinearRegression()),
]
pipeline = Pipeline(steps)

print("資料型態 :", type(X_train), type(y_train))
print("資料大小 :", X_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
pipeline.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {pipeline.score(X_train, y_train)}")
print(f"測試判定係數: {pipeline.score(X_test, y_test)}")

# 訓練判定係數: 1.0
# 測試判定係數: -60.45752231085903

# l2 Regularization or Ridge Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Ridge(alpha=10, fit_intercept=True)),
]

ridge_pipe = Pipeline(steps)

print("資料型態 :", type(X_train), type(y_train))
print("資料大小 :", X_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
ridge_pipe.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {ridge_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {ridge_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.9411030494647765
# 測試判定係數: 0.8158674422432347

# l1 Regularization or Lasso Regression

steps = [
    ("scalar", StandardScaler()),
    ("poly", PolynomialFeatures(degree=2)),
    ("model", Lasso(alpha=0.3, fit_intercept=True)),
]

lasso_pipe = Pipeline(steps)

print("資料型態 :", type(X_train), type(y_train))
print("資料大小 :", X_train.shape, y_train.shape)
print("迴歸型態 : 多維df")
lasso_pipe.fit(X_train, y_train)  # 學習訓練.fit

# 模型評分
print(f"訓練判定係數: {lasso_pipe.score(X_train, y_train)}")
print(f"測試判定係數: {lasso_pipe.score(X_test, y_test)}")

# 訓練判定係數: 0.8525646297860277
# 測試判定係數: 0.8367938135279831

print("結論：L1 test score 最高")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性迴歸

df = pd.read_csv("./data/population.csv")
X = df[["year"]].values
y = df[["pop"]].values

plt.scatter(X, y, c="blue", marker="o", s=2, label="實際")
plt.legend()
plt.grid()
show()

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

print("使用公式預測2050年人口數 : (使用 線性迴歸)")

m = linear_regression.coef_[0][0]  # 取出斜率
k = linear_regression.intercept_[0]  # 取出截距
print(f"斜率  = {m.round(2)}")
print(f"截距  = {k.round(2)}")


# TBD 畫線性迴歸線
"""
XX = np.array([-3, 3])
YY = XX * linear_regression.coef_ + linear_regression.intercept_
plt.plot(XX,YY,c="g",label="線性迴歸2")
"""

# 預測 20XX.....

"""
x = 2050
population = (
    (x**2) * linear_regression.coef_[0]
    + x * linear_regression.coef_[1]
    + linear_regression.intercept_
)
print(population)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# regression_vs_time_series

# 迴歸(Regression)與時間序列(Time Series) 比較

df = pd.read_csv("./data/monthly-airline-passengers.csv")
print(df)

# 資料轉換

# 設定為日期的資料型態
df["Date"] = pd.to_datetime(df["Month"])

# 設定日期為 DataFrame 的索引值
df = df.set_index("Date")

# 依照資料內容設定日期的頻率
df.index = pd.DatetimeIndex(df.index.values, freq=df.index.inferred_freq)
# 將原有欄位刪除
df.drop("Month", axis=1, inplace=True)

# 繪圖

plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
show()

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# X = df.index.astype(str).map(lambda x:x[:4]+x[5:7]).values.reshape(df.shape[0], -1)
X = np.arange(df.shape[0]).reshape(-1, 1)
y = df["Passengers"]

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

# 實際樣本點
plt.figure(figsize=(10, 5))
sns.lineplot(x=df.index, y="Passengers", data=df)
plt.title("airline passengers")
# show()

# 預測迴歸線
plt.plot(df.index, y_pred)
show()

# 殘差線圖
plt.plot(df.index, np.abs(df["Passengers"] - y_pred))
show()

# 定態測試(Augmented Dickey–Fuller Test for Stationarity)

from statsmodels.tsa.stattools import adfuller

result = adfuller(df["Passengers"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: 0.8153688792060482
p value: 0.991880243437641
滯後期數(Lags): 13
資料筆數: 130
"""

# 結論：p > 0.05 ==> 非定態

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

fig = plot_acf(df["Passengers"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df["Passengers"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# 時間序列(Time Series)

from statsmodels.tsa.arima.model import ARIMA

# 建立時間序列資料
series = df.copy()

# AR(1) 模型訓練
ar = ARIMA(df, order=(1, 0, 0))

model = ar.fit()  # 學習訓練.fit

print("檢視神經網路")
model.summary()  # 檢視神經網路

cc = model.params
print(cc)

cc = df["Passengers"].mean()
print(cc)

# 繪圖比較實際值與預測值

cc = model.fittedvalues
print(cc)

series["Passengers"].plot(figsize=(12, 6), color="black", linestyle="-", label="實際值")
model.fittedvalues.plot(
    figsize=(12, 6), color="green", linestyle=":", lw=2, label="預測值"
)
plt.legend()
show()

print(f"AR MSE = {(np.sum(model.resid**2) / len(model.resid)):.2f}")
# AR MSE = 1301.63

linear_regression2 = sklearn.linear_model.LinearRegression()  # 函數學習機

# 複製資料
series2 = series.copy()

# 將前一期 y 當作 x
series2["Passengers_1"] = series2["Passengers"].shift(-1)
series2.dropna(inplace=True)
X = series2["Passengers"].values.reshape(series2.shape[0], -1)

print("資料型態 :", type(X), type(series2["Passengers_1"]))
print("資料大小 :", X.shape, series2["Passengers_1"].shape)
print("迴歸型態 : 多維df")
linear_regression2.fit(X, series2["Passengers_1"])  # 學習訓練.fit

series2["TS"] = model.fittedvalues
series2["LR"] = (
    linear_regression2.coef_ * series["Passengers"] + linear_regression2.intercept_
)
series2["LR"].plot(color="green", linestyle="-.", lw=2, legend="LR")
series2["TS"].plot(figsize=(12, 6), color="red", linestyle=":", lw=2, legend="TS")
show()

cc = series2[["TS", "LR"]]
print(cc)

# AR(1) 殘差(residual)繪圖

residuals = pd.DataFrame(model.resid)
residuals.plot()
show()

# 資料分割
X_train, X_test = train_test_split(series, test_size=0.2, shuffle=False)

# 模型訓練、預測與繪圖

# AR(1) 模型訓練
ar_1 = ARIMA(X_train[["Passengers"]], order=(1, 0, 0))

model_1 = ar_1.fit()  # 學習訓練.fit

# 預測 12 個月
y_pred = model_1.predict(X_train.shape[0], X_train.shape[0] + 12 - 1)  # 預測.predict

# 繪圖
plt.rcParams["font.sans-serif"] = ["Arial Unicode MS"]
plt.rcParams["axes.unicode_minus"] = False

series["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_1.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
y_pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
show()

# 改用 SARIMAX (Seasonal ARIMA) 演算法
# 一次差分(First-order Differencing)

df_diff = df.copy()
df_diff["Passengers_diff"] = df_diff["Passengers"] - df_diff["Passengers"].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff"].plot()
show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)

"""
ADF統計量: -2.8292668241699994
p value: 0.0542132902838255
滯後期數(Lags): 12
資料筆數: 130
"""

from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

fig = plot_acf(df_diff["Passengers_diff"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df_diff["Passengers_diff"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# 二次差分(Second-order Differencing)

df_diff["Passengers_diff_2"] = df_diff["Passengers_diff"] - df_diff[
    "Passengers_diff"
].shift(1)
df_diff.dropna(inplace=True)
df_diff["Passengers_diff_2"].plot()
show()

# 使用ADF檢定

result = adfuller(df_diff["Passengers_diff_2"])
print(
    f"ADF統計量: {result[0]}\np value: {result[1]}"
    + f"\n滯後期數(Lags): {result[2]}\n資料筆數: {result[3]}"
)
"""
Test Stat: -16.384231542468505
p value: 2.7328918500142407e-29
Lags: 11
Num observations: 130
"""
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

fig = plot_acf(df_diff["Passengers_diff_2"], lags=20)
fig.set_size_inches(10, 5)
show()

fig = plot_pacf(df_diff["Passengers_diff_2"], lags=20, method="ywm")
fig.set_size_inches(10, 5)
show()

# SARIMAX

# 資料分割
X_train, X_test = train_test_split(df_diff, test_size=0.2, shuffle=False)

# SARIMAX
import statsmodels.api as sm

ar_diff = sm.tsa.statespace.SARIMAX(
    X_train[["Passengers"]], order=(1, 2, 1), seasonal_order=(1, 2, 1, 12)
)

print("到這邊會脫離程式......................")

"""
# 這個 .fit 有問題 會脫離程式
model_diff = ar_diff.fit()  # 學習訓練.fit

# 預測 12 個月
y_pred = model_diff.predict(X_train.shape[0], X_train.shape[0] + 12 - 1, dynamic=True)  # 預測.predict
print(y_pred)

df_diff["y_pred"] = np.concatenate((model_diff.fittedvalues.values, y_pred.values))
cc = df_diff["y_pred"]
print(cc)

# 繪圖

df_diff["Passengers"].plot(color="black", linestyle="-", label="實際值")
model_diff.fittedvalues.plot(color="green", linestyle=":", lw=2, label="訓練資料預測值")
y_pred.plot(figsize=(12, 5), color="red", lw=2, label="測試資料預測值")
plt.legend()
show()

print(f"SARIMAX MSE = {(np.sum(model_diff.resid**2) / len(model_diff.resid)):.2f}")
# SARIMAX MSE = 427.67

# 結論：SARIMAX 準確率比迴歸高
# 時間序列 MSE： 427， 迴歸 MSE： 2091

from statsmodels.tsa.seasonal import seasonal_decompose

decomp = pd.read_csv("./data/monthly-airline-passengers.csv")
decomp["Date"] = pd.to_datetime(decomp["Month"])
decomp = decomp.set_index("Date")
decomp.index = pd.DatetimeIndex(df.index.values, freq=decomp.index.inferred_freq)
decomp.drop("Month", axis=1, inplace=True)

s_dc = seasonal_decompose(decomp["Passengers"], model="additive")
decomp["SDC_Seasonal"] = s_dc.seasonal
decomp["SDC_Trend"] = s_dc.trend
decomp["SDC_Error"] = s_dc.resid
decomp["SDC_TS"] = s_dc.trend + s_dc.seasonal

print("ddddd")

plt.title("Trend components")
decomp["Passengers"].plot(
    figsize=(12, 6), color="black", linestyle="-", legend="Passengers"
)
decomp["SDC_Trend"].plot(
    figsize=(12, 6), color="blue", linestyle="-.", lw=2, legend="SDC_Trend"
)
decomp["SDC_TS"].plot(figsize=(12, 6), color="green", linestyle=":", lw=2, legend="TS")

show()

# 效應分解(Decomposition)

# Plot the original time series, trend, seasonal and random components
fig, axarr = plt.subplots(4, sharex=True)
fig.set_size_inches(5.5, 5.5)

decomp["Passengers"].plot(ax=axarr[0], color="b", linestyle="-")
axarr[0].set_title("Monthly Passengers")

pd.Series(data=decomp["SDC_Trend"], index=decomp.index).plot(
    color="r", linestyle="-", ax=axarr[1]
)
axarr[1].set_title("Trend component in monthly employment")

pd.Series(data=decomp["SDC_Seasonal"], index=decomp.index).plot(
    color="g", linestyle="-", ax=axarr[2]
)
axarr[2].set_title("Seasonal component in monthly employment")

pd.Series(data=decomp["SDC_Error"], index=decomp.index).plot(
    color="k", linestyle="-", ax=axarr[3]
)
axarr[3].set_title("Irregular variations in monthly employment")

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=2.0)
fig = plt.xticks(rotation=10)

show()

MSE = (decomp["SDC_Error"] ** 2).sum() / decomp["SDC_Error"].shape[0]
print("MSE=", MSE)
# ('MSE=', 340.80467800107556)

#結論：時間序列預測準確率比迴歸高
#時間序列 MSE： 340， 迴歸 MSE： 2091
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SHAP套件測試
# An introduction to explainable AI with Shapley values

import shap

# 載入資料集
df = pd.read_csv("./data/ca_housing.csv")
cc = df.head()
print(cc)

# 資料清理

# 刪除 missing value
df.dropna(inplace=True)

X = df.drop(["median_house_value", "ocean_proximity"], axis=1)
y = df["median_house_value"]

# scaler = preprocessing.StandardScaler()
# X2 = scaler.fit_transform(X)
# X = pd.DataFrame(X2, columns=X.columns)

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

length = X.shape[1]
print("X的欄位數 :", length)
print("Model coefficients:")
for i in range(length):
    print(
        "第", i, "欄, 欄名 :", X.columns[i], ", 迴歸係數 :", linear_regression.coef_[i].round(5)
    )

# 單一特徵影響力
feature_name = "median_income"
X100 = shap.utils.sample(X, 100)

""" 會畫圖
#會畫圖
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    ice=False,
    model_expected_value=True,
    feature_expected_value=True,
)

# 衡量特徵Shapley value

sample_ind = 20  # 第 21 筆資料
explainer = shap.Explainer(linear_regression.predict, X100)
shap_values = explainer(X)

#會畫圖
shap.partial_dependence_plot(
    feature_name,
    linear_regression.predict,
    X100,
    model_expected_value=True,
    feature_expected_value=True,
    ice=False,
    shap_values=shap_values[sample_ind : sample_ind + 1, :],
)

# Exact explainer: 20434it [01:32, 205.74it/s]

# 以單一特徵所有資料的Shapley value繪製散佈圖

shap.plots.scatter(shap_values[:, feature_name])
show()

# 單一資料的特徵影響力(Local Feature Importance)

cc = X.iloc[sample_ind]
print(cc)

shap.plots.waterfall(shap_values[sample_ind], max_display=14)
show()

# 加法模型(Generalized additive models, GAM)

# !pip install interpret

import interpret.glassbox

# 使用 Boosting 演算法
model_ebm = interpret.glassbox.ExplainableBoostingRegressor(interactions=0)

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
model_ebm.fit(X, y)  # 學習訓練.fit

# 加法模型 Shapley value
explainer_ebm = shap.Explainer(model_ebm.predict, X100)
shap_values_ebm = explainer_ebm(X)

# 特徵影響力
#會畫圖
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
show()

shap.plots.scatter(shap_values_ebm[:, feature_name])
show()

shap.plots.waterfall(shap_values_ebm[sample_ind])
show()

shap.plots.beeswarm(shap_values_ebm)
show()

shap.plots.bar(shap_values_ebm)
show()

shap.initjs()
shap.plots.force(shap_values_ebm[sample_ind])
"""

"""
Visualization omitted, Javascript library not loaded!
Have you run `initjs()` in this notebook?
If this notebook was from another user you must also trust this notebook (File -> Trust notebook).
If you are viewing this notebook on github the Javascript has been stripped for security.
If you are using JupyterLab this error is because a JupyterLab extension has not yet been written.
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 200

X = np.linspace(-2 * np.pi, 2 * np.pi, N)
Y = np.sin(X) + 0.2 * np.random.rand(N) - 0.1
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


def polynomial_model(degree=1):
    polynomial_features = PolynomialFeatures(degree=degree, include_bias=False)
    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
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
    model.fit(X, Y)  # 學習訓練.fit
    train_score = model.score(X, Y)
    mse = mean_squared_error(Y, model.predict(X))  # 均方誤差 Mean Squared Error (MSE)
    results.append({"model": model, "degree": d, "score": train_score, "mse": mse})
for r in results:
    print(
        "degree: {}; train score: {}; mean squared error: {}".format(
            r["degree"], r["score"], r["mse"]
        )
    )

print("------------------------------")  # 30個

from matplotlib.figure import SubplotParams

plt.figure(figsize=(12, 8), subplotpars=SubplotParams(hspace=0.3))
for i, r in enumerate(results):
    fig = plt.subplot(2, 2, i + 1)
    plt.xlim(-8, 8)
    plt.title("線性回歸 degree={}".format(r["degree"]))
    plt.scatter(X, Y, s=5, c="b", alpha=0.5)
    plt.plot(X, r["model"].predict(X), "r-")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 線性迴歸

X = pd.DataFrame([1, 2, 3, 4])
y = pd.DataFrame([1, 3, 3, 4])

x_test = pd.DataFrame([1.5, 3, 5])

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict
print(y_pred)

# visualize results
plt.scatter(X, y)
# plt.scatter(x_test, y_pred, color="red")
# plt.plot(x_test, y_pred, color="blue")
plt.plot(x_test, y_pred, "ro-")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# BrainBody

dataframe = pd.read_fwf("data/brain_body.txt")
X = dataframe[["Brain"]]
y = dataframe[["Body"]]

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

plt.scatter(X, y)
plt.plot(X, y_pred)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# BrainBody-Exam

dataframe = pd.read_fwf("data/brain_body.txt")
X = dataframe[["Body"]]
y = dataframe[["Brain"]]

linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print("資料型態 :", type(X), type(y))
print("資料大小 :", X.shape, y.shape)
print("迴歸型態 : 多維df")
linear_regression.fit(X, y)  # 學習訓練.fit

# 全預測
y_pred = linear_regression.predict(X)  # 預測.predict

print(linear_regression.predict(pd.DataFrame(data=[[170]])))

plt.scatter(X, y)
plt.plot(X, y_pred)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], "rx")
plt.plot([1, 2, 3, 4], [0, 0.3, 0.6, 0.9], "g--")

X = 1 + np.arange(30) / 10
delta = np.random.uniform(low=-0.1, high=0.1, size=(30,))
Y = 0.3 * X - 0.3 + delta
plt.plot(X, Y, "bo")

plt.legend(("price", "passenger", "noise"), loc="best")
plt.xlabel("X")
plt.ylabel("Y")
show()

sum1 = 0.0
i = 0
for X1 in X:
    Y1 = 0.3 * X1 - 0.3
    Y2 = 0.3 * X1 - 0.3 + delta[i]
    sum1 = sum1 + abs(Y1 - Y2)
    i = i + 1

print("誤差值", sum1 / 30)

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

# 共同取出
"""
如果公式是y=mx+k
m : 斜率
k : 截距
"""
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

print("迴歸係數(斜率):", linear_regression.coef_)

# 測試資料型態
xxx = np.array([3, 9, 8, 1, 2])
yyy = np.array([1, 3, 9, 2, 4])

print("目前 xxx 是個 5 維向量")
print(xxx.shape)

# xxx訓練資料要轉為 NX1 陣列
xxx = xxx.reshape(len(xxx), 1)
print(xxx.shape)


print("打印一些結果")
print(linear_regression.predict([[1.3]]))  # 預測.predict
print(linear_regression.predict([[2.7], [1.5]]))  # 預測.predict


# 預測

print(svr_lin.predict([[6.2]]))  # 預測.predict
print(svr_lin.predict([[6.2], [7.4], [8]]))  # 預測.predict

temp = [[23]]  # 輸入特徵值(氣溫)
p = linear_regression.predict(temp)  # 輸出標籤(預測的銷售量)  # 預測.predict
print(p)

temp = [[23], [18], [36]]
p = linear_regression.predict(temp)  # 預測.predict
print(p)


# SVR 函數學習機, rbf / linear / poly


plt.axis([-3, 3, -150, 150])  # 設定各軸顯示範圍
plt.xlim(-3, 3)
plt.ylim(-150, 150)


# -------------------------

"""
# 決定模型：取出線性迴歸模型的 m、b 參數
print("線性迴歸的模型為 y = f(x) = mx + k")
print("m 為 ", linear_regression.coef_)
print("k 為 ", linear_regression.intercept_)

m = linear_regression.coef_[0][0]  # 取出斜率
k = linear_regression.intercept_[0]  # 取出截距
print(f"斜率  = {m.round(2)}")
print(f"截距  = {k.round(2)}")

y2 = m * xs + k
plt.plot(xs, ys, "b-o", lw=1, ms=10, label="實驗值")
plt.plot(xs, y2, "r", lw=2, label="迴歸直線")  # 繪製迴歸直線

xxx = 10
predicted = m * xxx + k
print(f"x = 10 的 預測值 = {predicted}")
plt.plot(xxx, predicted, "ro", lw=1, ms=12, label="預測值")


"""

# 預測
cc = linear_regression.predict([[6]])  # 預測.predict


plt.plot(xxx, yyy, "go:")


# 資料的寫法
X = [[1], [2], [3], [4], [5]]
y = [88, 72, 90, 76, 92]
linear_regression.fit(X, y)  # 學習訓練.fit


# 資料的寫法
# x = np.array([[22], [26], [23], [28], [27], [32], [30]])      # 溫度
# y = np.array([[15], [35], [21], [62], [48], [101], [86]])     # 飲料銷售數量
# x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype = float)
# y = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype = float)
xs = np.array([[0.0], [1.0], [2.0], [3.0], [4.0], [5.0]], dtype=float)
ys = np.array([[0.0], [1.0], [2.0], [5.0], [4.0], [5.0]], dtype=float)

linear_regression.fit(xs, ys)  # 學習訓練.fit


"""
因變數 x
應變數
y0 理想資料
y1 真實資料

1. 理想資料 lime
2. 真實資料 b
3. 線性迴歸 red
   其他迴歸

"""

plt.scatter(X, y, c="blue", marker="o", lw=0.1, label="真實資料")

# 標準
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍點藍線
plt.scatter(x, y1, s=100, c="b", label="真實資料")  # 真實資料, 藍點
plt.plot(x, Y, color="r", marker="o", markersize=8, label="線性迴歸")  # 線性迴歸曲線

print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y_test, y_pred)

# grid的寫法
plt.grid(which="major", linestyle="-", lw="0.5", color="green")
plt.grid(which="minor", linestyle=":", lw="0.5", color="black")

# 資料分割
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 應該沒有用
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
linear_regression.fit(x_train, y_train)  # 學習訓練.fit
plt.scatter(X, Y, color="b", label="真實資料")
y_pred = linear_regression.predict(x_test)  # 預測.predict
plt.plot(x_test, y_pred, "mo-", label="線性迴歸2")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 評估
print("真實資料")
print_y_data(y1)

print("線性迴歸")
print_y_data(y_pred)

print("評估 : 計算 測試資料 與 預測結果 的差異")
evaluate_result(y1, y_pred)

print("預測的寫法")
y_pred2 = linear_regression.predict([[0], [1]])  # 預測.predict
print(y_pred2)


# 有x測試資料預測到的結果和真實y測試資料比對
X_test = x_test.reshape(len(x_test), 1)  # x測試資料要轉為 NX1 陣列
y_pred = linear_regression.predict(X_test)  # 預測.predict


ax.plot(X[:, 0], X[:, 1], y, "o", markersize=8, color="blue", alpha=0.5)


"""
自建資料1
print("線性迴歸, 輸入資料的寫法")
X = [[10.0], [8.0], [13.0], [9.0], [11.0], [14.0], [6.0], [4.0], [12.0], [7.0], [5.0]]
y = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
"""
"""
自建資料2
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 4, 5, 6])
X = x.reshape((-1, 1))
"""
