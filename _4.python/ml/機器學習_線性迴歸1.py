"""
線性迴歸

機器學習：建立線性迴歸資料與預測

線性迴歸（linear regression)

什麼是線性迴歸？

    Finding the curve that best fits your data is called regression, and when that curve is a straight line, it's called linear regression.
    找出符合資料規律的直線，就叫線性迴歸。

建立迴歸資料 make_regression

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
from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料

print("------------------------------------------------------------")  # 60個

# 簡單資料 y = x
xx = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
yy0 = xx  # 理想資料, y = x
yy1 = np.array([0, 1, 4, 3, 4, 5, 6, 3, 8, 9, 10])  # 真實資料

"""
# 複雜資料 f(x) = sin(3.2x) + 0.8x
N = 50
xx = np.linspace(0, 5, N)
yy0 = np.sin(3.2 * x) + 0.8 * x
yy1 = np.sin(3.2 * x) + 0.8 * x + 0.3 * np.random.randn(N)
"""
'''
print("------------------------------------------------------------")  # 60個

print("資料來源 : make_regression 1")
# 使用make_regression()方法，建立200個樣本(samples)，
# 只有一種特徵(features)和一種標籤類別（label），
# 我們將noise設為10，這樣資料會比較分散一點。

X, y = datasets.make_regression(n_samples=200, n_features=1, n_targets=1, noise=10)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

# 因為要再繪出預測的資料圖，所以將預測資料放到 y_pred 變數內：
y_pred = linear_regression.predict(X[:200, :])  # 預測.predict

plt.scatter(X, y, linewidths=0.1)
plt.plot(X, y_pred, c="red")  # 用線性迴歸找出的線

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : make_regression 2")

x, y = datasets.make_regression(n_samples=100, n_features=1, noise=20)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

print('預測 x測試資料x_test')
y_pred = linear_regression.predict(x_test)  # 預測.predict

plt.axis([-3, 3, -150, 150])  # 設定各軸顯示範圍

"""
plt.scatter(x, y, s=200, label = '原始資料')
plt.scatter(x_train, y_train, s=30, label="訓練數據")
plt.scatter(x_test, y_test, s=30, label="測試數據")
"""
plt.scatter(x, y, c="blue", marker="o", lw=8, label="原始資料")
plt.scatter(x_train, y_train, c="red", marker="o", lw=4, label="訓練數據")
plt.scatter(x_test, y_test, c="green", marker="o", lw=4, label="測試數據")

# 使用測試數據 x_test 和此 x_test 預測的 y_pred 繪製迴歸直線
plt.plot(x_test, y_pred, color="red", label="迴歸直線")

# 將測試的 y 與預測的 y_pred 計算 決定係數r2

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 r2_score')
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
# print(f"決定係數 = {r2.round(2)}") NG

plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 2 飲料 做成df")

# 氣溫
xxx = np.array([29, 28, 34, 31, 25, 29, 32, 31, 24, 33, 25, 31, 26, 30])

# 營業額
yyy = np.array(
    [7.7, 6.2, 9.3, 8.4, 5.9, 6.4, 8.0, 7.5, 5.8, 9.1, 5.1, 7.3, 6.5, 8.4]
)

X = pd.DataFrame(xxx, columns=["氣溫"])

target = pd.DataFrame(yyy, columns=["營業額"])
y = target["營業額"]

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

print(type(X))
print(type(y))

linear_regression.fit(X, y)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

# 預測氣溫 24 ~ 34 度的業績
new_xxx = pd.DataFrame(np.array([24, 26, 28, 30, 32, 34]), columns=["氣溫"])

y_pred = linear_regression.predict(new_xxx)  # 預測.predict
print(y_pred)

plt.scatter(xxx, yyy, s=100, c='b', label = '原始資料')
plt.plot(new_xxx, y_pred, color="red", marker="o", markersize=10, label="線性回歸")  # 線性回歸曲線
plt.title("使用當日氣溫來預測當日的業積")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 4 身高體重")
print("由[身高]來預測體重")
print("一維資料 線性迴歸")

heights = np.array(
    [147.9, 163.5, 159.8, 155.1, 163.3, 158.7, 172.0, 161.2, 153.9, 161.6]
)
weights = np.array([41.7, 60.2, 47.0, 53.2, 48.3, 55.2, 58.5, 49.0, 46.7, 52.5])

X = pd.DataFrame(heights, columns=["身高"])
target = pd.DataFrame(weights, columns=["體重"])
y = target["體重"]

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

# 預測身高150, 160, 170的體重
new_heights = pd.DataFrame(np.array([150, 160, 170]), columns=["身高"])

predicted_weights = linear_regression.predict(new_heights)  # 預測.predict
print(predicted_weights)

plt.scatter(heights, weights)  # 繪點

y_pred = linear_regression.predict(X)  # 預測.predict

plt.plot(heights, y_pred, color="blue")
plt.plot(new_heights["身高"], predicted_weights, color="red", marker="o", markersize=10)
plt.title("使用學生的身高來預測體重")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 5 腰圍身高體重")
print("由[腰圍和身高]來預測體重")
print("二維資料 線性迴歸")

waist_heights = np.array(
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
weights = np.array([50, 60, 65, 65, 70, 75, 80, 85, 90, 81])

X = pd.DataFrame(waist_heights, columns=["腰圍", "身高"])
target = pd.DataFrame(weights, columns=["體重"])
y = target["體重"]

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

# 預測腰圍和身高[66,164],[82,172]的體重
new_waist_heights = pd.DataFrame(np.array([[66, 164], [82, 172]]), columns=["腰圍", "身高"])
predicted_weights = linear_regression.predict(new_waist_heights)  # 預測.predict
print(predicted_weights)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 6 店面積 距捷運 月營收")
print("由[店面積和距捷運]來預測月營收")
print("二維資料 線性迴歸")

area_dists = np.array(
    [
        [10, 80],
        [8, 0],
        [8, 200],
        [5, 200],
        [7, 300],
        [8, 230],
        [7, 40],
        [9, 0],
        [6, 330],
        [9, 180],
    ]
)
sales = np.array([46.9, 36.6, 37.1, 20.8, 24.6, 29.7, 36.6, 43.6, 19.8, 36.4])
X = pd.DataFrame(area_dists, columns=["店面積", "距捷運"])
target = pd.DataFrame(sales, columns=["月營收"])
y = target["月營收"]

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)

# 預測店面積和距捷運[10,100]的營業額
new_area_dists = pd.DataFrame(np.array([[10, 100]]), columns=["店面積", "距捷運"])
y_pred = linear_regression.predict(new_area_dists)  # 預測.predict
print(y_pred)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7a")

x  = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍線藍點

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

#x訓練資料要轉為 NX1 陣列
X = x.reshape(len(x), 1)

y1 = y1.reshape(len(y1), 1)

linear_regression.fit(X, y1)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

Y = linear_regression.predict(X)  # 預測.predict

plt.plot(x, Y, "ro-", lw=3, label="線性迴歸")  # 線性回歸曲線
#plt.plot(x, Y, color="red", marker="o", markersize=10, label="線性回歸")  # 線性回歸曲線

plt.title("線性迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7b 資料分割")

x  = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    x, y1, test_size=0.2, random_state=9487
)  # 訓練組8成, 測試組2成
plt.scatter(x_train, y_train, s=100, c="b", label="真實資料(訓練組)")  # 真實資料
plt.scatter(x_test, y_test, s=300, c="m", label="真實資料(測試組)")  # 真實資料

#x訓練資料要轉為 NX1 陣列
X_train = x_train.reshape(len(x_train), 1)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train, y_train)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

#拿測試資料做預測
#x測試資料要轉為 NX1 陣列
X_test = x_test.reshape(len(x_test), 1)
Y_test = linear_regression.predict(X_test)  # 預測.predict

plt.plot(x_test, Y_test, "ro-", lw=3, label="線性迴歸")  # 線性回歸曲線
#plt.plot(x_test, Y_test, color="red", marker="o", markersize=10, label="線性回歸")  # 線性回歸曲線

plt.title("線性迴歸")
plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------")  # 30個

# 有x測試資料預測到的結果和真實y測試資料比對

#拿測試資料做預測
#x測試資料要轉為 NX1 陣列
X_test = x_test.reshape(len(x_test), 1)
Y_test = linear_regression.predict(X_test)  # 預測.predict

print('預測資料(Y_test) :', Y_test)
print('真實測試資料(y_test) :', y_test)

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
mse = np.sum((y_test - Y_test) ** 2) / len(y_test)
print("MSE =", mse)

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, Y_test)
print(f"MSE = {mse:.4f}")

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 r2_score')
from sklearn.metrics import r2_score
r2 = r2_score(y_test, Y_test)
print(f"R2 = {r2:.4f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7c 理想+亂數資料")

x  = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

# 做線性迴歸, 用 sklearn 裡的 SVR 來做線性迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

#x訓練資料要轉為 NX1 陣列
X = x.reshape(len(x), 1)
#print(x.shape)
#print(X.shape)

svr_lin.fit(X, y1)  # 學習訓練.fit

y_pred = svr_lin.predict(X)  # 預測.predict

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線 tbd
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍線藍點
plt.plot(x, y_pred, "ro-", lw=3, label="SVR線性迴歸")  # SVR線性回歸曲線
#plt.plot(x, y_pred, color="red", marker="o", markersize=10, label="SVR線性迴歸")  # SVR線性迴歸

plt.title("SVR線性迴歸1")
#plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print("------------------------------")  # 30個

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

#x訓練資料要轉為 NX1 陣列
X = x.reshape(len(x), 1)

linear_regression.fit(X, y1)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

y_pred = linear_regression.predict(X)  # 預測.predict

plt.plot(x, y0, "lime", lw=5, label="理想資料")  # 理想資料, y = x 綠線
plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍線藍點
plt.plot(x, y_pred, "ro-", lw=3, label="線性迴歸")  # 線性回歸曲線
#plt.plot(x, y_pred, color="red", marker="o", markersize=10, label="線性回歸")  # 線性回歸曲線

plt.title("線性迴歸2")
#plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(
    x, y1, test_size=0.2, random_state=9487
)  # 訓練組8成, 測試組2成

#x訓練資料要轉為 NX1 陣列
x_train = x_train.reshape(len(x_train), 1)

#x測試資料要轉為 NX1 陣列
x_test = x_test.reshape(len(x_test), 1)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

print('預測 x測試資料x_test')
y_pred = linear_regression.predict(x_test)  # 預測.predict

plt.plot(x_test, y_pred, "r")
# plt.plot(x_test.ravel(), y_pred, 'g')
plt.scatter(x_test, y_test, label="原始測試資料")
# plt.scatter(x_test.ravel(), y_test)

plt.scatter(x_train, y_train)
plt.plot(x_train, linear_regression.predict(x_train), "r", label="訓練結果")

# 我們在「訓練」這個函數時只有以下這些資料。
plt.scatter(x_train, y_train, label="原始訓練資料")  # 原始訓練資料

plt.title("線性迴歸")
#plt.axis([0, 10, 0, 10])  # 設定各軸顯示範圍
plt.legend()
plt.grid()

plt.show()

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
from sklearn.metrics import mean_squared_error
mse_t = mean_squared_error(y_train, linear_regression.predict(x_train))
print("MSE =", mse_t)

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 r2_score')
from sklearn.metrics import r2_score
r2_t = r2_score(y_train, linear_regression.predict(x_train))
print("R2 =", r2_t)

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"MSE = {mse:.4f}")

from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(f"R2 = {r2:.4f}")

# 用訓練資料來 fit 函數 方法一
# 記得現在我們只用 80% 的資料去訓練。

# 做線性迴歸, 用 sklearn 裡的 SVR 來做線性迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

X_train = x_train.reshape(len(x_train), 1)

svr_lin.fit(X_train, y_train)  # 學習訓練.fit

Y_train = svr_lin.predict(X_train)  # 預測.predict

plt.scatter(x_train, y_train)  # 原始訓練資料

plt.plot(x_train, Y_train, "ro-")
#plt.plot(x_train, Y_train, color="red", marker="o", markersize=10, label="訓練資料2")  # 訓練資料2

plt.title("訓練資料2")

plt.show()

# 用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test), 1)
Y_test = svr_lin.predict(X_test)  # 預測.predict

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
mse = np.sum((y_test - Y_test) ** 2) / len(y_test)
print("MSE =", mse)

plt.scatter(x_test, y_test)
plt.scatter(x_test, Y_test, c="r")
plt.title("測試結果1")

plt.show()

# 用訓練資料來 fit 函數 方法二
# 記得現在我們只用 80% 的資料去訓練。

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X_train = x_train.reshape(len(x_train), 1)

linear_regression.fit(x_train, y_train)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")

Y_train = linear_regression.predict(X_train)  # 預測.predict

plt.scatter(x_train, y_train)  # 原始訓練資料
plt.plot(x_train, Y_train, color="red", marker="o", markersize=10, label="線性回歸")  # 線性回歸曲線

plt.title("線性回歸測試結果")

plt.show()

# 用測試資料試試我們預測準不準
X_test = x_test.reshape(len(x_test), 1)

Y_test = linear_regression.predict(X_test)  # 預測.predict

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
mse = np.sum((y_test - Y_test) ** 2) / len(y_test)
print("MSE =", mse)

plt.scatter(x_test, y_test, c="b")
plt.scatter(x_test, Y_test, c="r")
plt.title("測試結果2")

plt.show()

x  = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

plt.plot(x, y1, "bo-", label="真實資料")  # 真實資料, 藍線藍點
plt.title("待處理的資料")

plt.show()

# 使用SVR

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y1, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

# 準備生這個函數

# 做線性迴歸, 用 sklearn 裡的 SVR 來做線性迴歸
svr_rbf = sklearn.svm.SVR(kernel="rbf", C=1e3, gamma=0.3)  # SVR 函數學習機, rbf

# 做線性迴歸, 用 sklearn 裡的 SVR 來做線性迴歸
svr_lin = sklearn.svm.SVR(kernel="linear", C=1e3)  # SVR 函數學習機, linear

# 做線性迴歸, 用 sklearn 裡的 SVR 來做線性迴歸
svr_poly = sklearn.svm.SVR(kernel="poly", C=1e3, degree=4)  # SVR 函數學習機, poly

X_train = x_train.reshape(len(x_train), 1)

svr_rbf.fit(X_train, y_train)  # 學習訓練.fit
svr_lin.fit(X_train, y_train)  # 學習訓練.fit
svr_poly.fit(X_train, y_train)  # 學習訓練.fit

# 看看訓練成果

X = x.reshape(len(x), 1)

y_pred_rbf = svr_rbf.predict(X)  # 預測.predict
y_pred_lin = svr_lin.predict(X)  # 預測.predict
y_pred_poly = svr_poly.predict(X)  # 預測.predict

plt.scatter(x, y1, s=100, c='r', label = '原始資料')
plt.plot(x, y_pred_rbf, label="rbf")
plt.plot(x, y_pred_lin, label="linear")
plt.plot(x, y_pred_poly, label="polynomial")

plt.legend()
plt.title("比較各種方法")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 自建資料 7d 各種方法比較")

x  = xx
y0 = yy0  # 理想資料
y1 = yy1  # 真實資料

print("------------------------------")  # 30個
# 使用 線性學習機 學習

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機
X = x.reshape(len(x), 1)
linear_regression.fit(X, y1)  # 學習訓練.fit
print(f"斜率  = {linear_regression.coef_[0].round(2)}")
print(f"截距  = {linear_regression.intercept_.round(2)}")
y_pred_lin = linear_regression.predict(X)  # 預測.predict

print("------------------------------")  # 30個
# 使用 6 次多項式 學習

X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])
regression_poly = sklearn.linear_model.LinearRegression()  # 函數學習機
regression_poly.fit(X_poly, y1)  # 學習訓練.fit
y_pred_poly = regression_poly.predict(X_poly)  # 預測.predict

print("------------------------------")  # 30個
# 使用 Radial Basis Function (RBF)
#（高斯）徑向基函數核（英語：Radial basis function kernel），或稱為RBF核

def RBF(x, center, sigma):
    k = np.exp(-((x - center) ** 2) / (2 * sigma**2))
    return k

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
regression_rbf.fit(X_rbf, y1)  # 學習訓練.fit
y_pred_rbf = regression_rbf.predict(X_rbf)  # 預測.predict


print("------------------------------")  # 30個
# 三種一起比較

plt.plot(x, y0, color="lime", label="理想資料")  # 理想資料
plt.plot(x, y1, color="m", marker="o", markersize=10, label="真實資料")  # 線性回歸曲線

plt.plot(x, y_pred_lin, "r", label="線性學習機 預測結果")
plt.plot(x, y_pred_poly, "g", label="6次多項式 預測結果")
plt.plot(x, y_pred_rbf, "b", label="RBF 預測結果")


plt.title("各種方法比較")
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("資料來源 : 內建資料 1 計程車小費資料集EDA")

# 計程車小費資料集EDA

from sklearn import datasets, preprocessing

df = sns.load_dataset("tips")
cc = df.head()
print(cc)

# 2. 資料清理、資料探索與分析

# 對小費繪製直方圖
sns.histplot(x="tip", data=df)
plt.show()

df["log_tip"] = np.log(df["tip"])
sns.kdeplot(x="log_tip", data=df)
plt.show()

# 散佈圖
sns.scatterplot(x="total_bill", y="tip", data=df)
plt.show()

# 三維散佈圖
sns.scatterplot(x="total_bill", y="tip", hue="sex", data=df)
plt.show()

# joint plot
sns.jointplot(data=df, x="total_bill", y="tip", hue="day")
plt.show()

df.day.unique()

# ['Sun', 'Sat', 'Thur', 'Fri']
# Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']

# 觀察週間對小費的影響

sns.barplot(x="day", y="tip", data=df)
plt.show()

# 箱型圖
sns.boxplot(x="day", y="tip", data=df)
plt.show()

# 類別變數轉換為數值
df.sex = df.sex.map({"Female": 0, "Male": 1}).astype(int)
df.smoker = df.smoker.map({"No": 0, "Yes": 1}).astype(int)
df.day = df.day.map({"Thur": 1, "Fri": 2, "Sat": 3, "Sun": 4}).astype(int)
df.time = df.time.map({"Lunch": 0, "Dinner": 1}).astype(int)

cc = df.info()
print(cc)

# 繪製pair plot
sns.pairplot(data=df, height=1)
plt.show()

# 熱力圖
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=0.5)
plt.show()

cc = df.isna().sum()
print(cc)

# 3. 不須進行特徵工程

# 4. 資料分割

# 指定X，並轉為 Numpy 陣列
X = df.drop("tip", axis=1).values
y = df.tip.values
print(y)

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# 訓練組8成, 測試組2成

# 查看陣列維度
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# ((195, 7), (49, 7), (195,), (49,))

# 特徵縮放
scaler = preprocessing.StandardScaler()
X_train_std = scaler.fit_transform(X_train)
X_test_std = scaler.transform(X_test)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train_std, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(X_test_std)  # 預測.predict

# 計算分數 計算 r2、MSE
print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 MSE')
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(f"MSE = {mse:.4f}")

print('計算 真實測試資料(y_test) 和 預測資料(Y_test)的 r2_score')
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(f"R2 = {r2:.4f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

df = pd.read_excel("C:/_git/vcs/_4.python/__code/Python-PM2.5-DataAnalyzing-master/各種演算法比較/20160101-20190101(Daily)迴歸分析.xlsx")

"""
cc = df.head(10)
print(cc)

#資料長度
print(len(df))
print(len(df["PM25"]))

cc = df.info()
print(cc)

cc = df.describe()
print(cc)
"""
cc = df.set_index("Date")
print(cc)

"""
df.dtypes
df.isnull().sum()
df.isnull().any()
"""

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

y = df["PM25"].values

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=9487)
# 訓練組8成, 測試組2成

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

"""
sns.heatmap(df.corr())
plt.show()

cc = df.corr()
print(cc)
"""
y_pred = linear_regression.predict(x_test)  # 預測.predict

df = pd.DataFrame({"測試資料": y_test, "預測結果": y_pred})
df1 = df.head(25)
# print(df1)

df1.plot(kind="bar", figsize=(10, 8))
plt.grid(which="major", linestyle="-", linewidth="0.5", color="green")
plt.grid(which="minor", linestyle=":", linewidth="0.5", color="black")
plt.show()

# 載入迴歸常見的評估指標
from sklearn import metrics
print("評估 測試資料 與 預測結果 的差異")

# Mean Absolute Error (MAE)代表平均誤差，公式為所有實際值及預測值相減的絕對值平均。
cc = metrics.mean_absolute_error(y_test, y_pred)
print("MAE : Mean Absolute Error :", cc)

# Mean Squared Error (MSE)比起MSE可以拉開誤差差距，算是蠻常用的指標，公式所有實際值及預測值相減的平方的平均
cc = metrics.mean_squared_error(y_test, y_pred)
print("MSE : Mean Squared Error :", cc)

# Root Mean Squared Error (RMSE)代表MSE的平方根。比起MSE更為常用，因為更容易解釋y。
cc = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print("RMS : Root Mean Squared Error :", cc)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

N = 50
x = np.linspace(0, 1, N)
y = 1.2 * x + 0.8 + 0.2 * np.random.randn(N)

plt.scatter(x, y)

plt.grid()
plt.title("真實資料")

plt.show()

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 訓練組8成, 測試組2成

"""
【重點】注意輸入格式
只有一個 feature 時, 我們要小心的是, 很多機器學習、深度學習的套件, 都不希望我們用
x=[x1,x2,…,xn]
這樣子去做, 而是希望變成
x=[[x1],[x2],…,[xn]]
這種形式!
"""

xx = np.array([3, 9, 8, 1, 2])
yy = np.array([1, 3, 9, 2, 4])

"""
xx.shape
xx.reshape(5,1)
xx = xx.reshape(len(xx),1)
"""

# 正式轉我們的訓練資料

x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

y_pred = linear_regression.predict(x_test)  # 預測.predict

# x: x_test
# y: y_pred
# x_test.ravel()

plt.plot(x_test.ravel(), y_pred, "r")

plt.scatter(x_test.ravel(), y_test)

plt.grid()
plt.title("aaaa")
plt.show()


# 計算分數
from sklearn.metrics import mean_squared_error, r2_score

mse_t = mean_squared_error(y_train, linear_regression.predict(x_train))
r2_t = r2_score(y_train, linear_regression.predict(x_train))
print("訓練資料")
print("MSE =", mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# 造資料, 調整成 sklearn 會接受的形狀
x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

X = x.reshape(len(x), 1)

linear_regression.fit(X, y)  # 學習訓練.fit

Y = linear_regression.predict(X)  # 預測.predict

plt.scatter(x, y)
plt.plot(x, Y, "r")
plt.show()

# 結果看起來不錯，會有微小誤差的原因，則是因為真實世界的資料有不可避免的雜訊

print("------------------------------")  # 30個

# 均勻地在 0 到 5 之間取一百個點，再隨便決定一個函數，叫做 y = f(x) = 1.9x + 0.8 好了
# 為了增加真實感，加上一點雜訊

x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

# 開開心心地讓 sklearn 幫我們分離出訓練資料跟測試資料，測試資料的比例是 0.3 的話，
# 訓練資料就會自動是 0.7 了呢，真是方便！
# random_state 可以是耍寶用的 87 ，要選其他數字也當然可以

# 資料分割, x_train, y_train 訓練資料, x_test, y_test 測試資料
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# 訓練組8成, 測試組2成

x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

# 用 plot 把「訓練資料」的正確答案畫成一條線，再把模型 predict 出來的結果描點畫在同一張圖上
# 可以清楚的看到結果

plt.scatter(x_train, y_train)
plt.plot(x_train, linear_regression.predict(x_train), "r")
plt.show()


# 跟上面一樣的做法，只是這次對象換成「測試資料」

plt.scatter(x_test, y_test)
plt.plot(x_test, linear_regression.predict(x_test), "r")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
Machine Learning 練習篇-Multiple Regression多元回歸糖尿病案例

diabetes dataset 資料集是一個糖尿病的資料集
主要包括442筆資料,10個屬性值,分別是:
Age(年齡)、Sex(性別)、Body mass index(體質指數)、
Average Blood Pressure(平均血壓)、S1-S6一年後疾病級數指標,
Target為一年後患疾病的定量指標。

題目1
建立線性多元回歸的預測模型,繪製散佈圖來比較一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。

題目2
建立線性多元回歸的預測模型,只取Age(年齡)、Sex(性別)、Body mass index(體質指數)、Average Blood Pressure(平均血壓)作為解釋變數,產生模型,並匯出散佈圖來比較預測一年後患疾病的定量指標和實際一年後患疾病的定量指標結果。
"""

# 題目1
from sklearn import datasets

# 載入資料集
diabetes = datasets.load_diabetes()

# print(diabetes.DESCR)
print("keys")
print(diabetes.keys())
print("feature_names")
print(diabetes.feature_names)
# ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
target = pd.DataFrame(diabetes.target, columns=["Target"])

print("Target為一年後患疾病的定量指標")
y = target["Target"]  # Series
print()
print(y)
print()

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X, y)  # 學習訓練.fit

print(
    "迴歸係數:", linear_regression.coef_
)  # 迴歸係數: [ -10.01219782 -239.81908937  519.83978679  324.39042769 -792.18416163 476.74583782  101.04457032  177.06417623  751.27932109   67.62538639]
print("截距:", linear_regression.intercept_)  # 截距: 152.1334841628965

predicted_diabetes = linear_regression.predict(X)
plt.scatter(y, predicted_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")

plt.show()

"""

#題目2
###################### 4 items ##############################
X1 = diabetes.data[:,:4]
X1 = pd.DataFrame(X1, columns=["age","sex","bmi", "bp"])
#print(X1)

target = pd.DataFrame(diabetes.target ,columns=["Target"])
y1 = target["Target"]

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression_4items = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression_4items.fit(X1,y1)  # 學習訓練.fit

print("迴歸係數:", linear_regression_4items.coef_)
print("截距:", linear_regression_4items.intercept_)
predicted_4items_diabetes = linear_regression_4items.predict(X1)
plt.scatter(y1 ,predicted_4items_diabetes)
plt.xlabel("Quantitative Measure")
plt.ylabel("Predicted Quantitative Measure")
plt.title("Quantitative Measure vs Predicted Quantitative Measure")
plt.show()

"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
糖尿病数据（适用于回归任务）

这是一个糖尿病的数据集，主要包括442行数据，10个属性值，分别是：
Age(年龄)、性别(Sex)、Body mass index(体质指数)、Average Blood Pressure(平均血压)、
S1~S6一年后疾病级数指标。

Target为一年后患疾病的定量指标，因此适合与回归任务

"""

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score


def do_linear_regression():
    diabetes = datasets.load_diabetes()

    X = diabetes.data[:, np.newaxis, 2]
    print("Data shape: ", X.shape)

    x_train, x_test, y_train, y_test = train_test_split(
        X, diabetes.target, test_size=0.1, random_state=4
    )

    linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

    linear_regression.fit(x_train, y_train)  # 學習訓練.fit

    y_pred = linear_regression.predict(x_test)  # 預測.predict

    plt.scatter(x_test, y_test, color="black")
    plt.plot(x_test, y_pred, color="blue", linewidth=3)
    plt.show()


print("線性迴歸")
do_linear_regression()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
x資料不能直接用 要改成X
原來我們 x 的資料型態是
[x1,x2,…,x50],
但 sklearn 希望每個 x 是個向量, 也就是:
[[x1],[x2],…,[x50]]
"""


"""
這裡要注意我們本來的 x 是
[x1,x2,…,x50]
但現在要的是
[[x1],[x2],…,[x50]]
"""


"""
再來很重要, 從現在到以後, 很多學函數的方法, 都要求我們訓練資料要排成一列一列的。也就說原本的
[x1,x2,…,x80]
要換成這樣
[[x1],[x2],…,[x80]]
好在我們學過 reshape, 這小事...
"""


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
linear_regression.fit(xs, ys)  # 學習訓練.fit
print("迴歸係數(斜率):", linear_regression.coef_)
print("截距:", linear_regression.intercept_)


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
