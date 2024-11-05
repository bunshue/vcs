"""
線性迴歸1

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

import sklearn.linear_model

print("------------------------------------------------------------")  # 60個

N = 11
x = np.linspace(0, 10, N)
y0 = x
y1 = y0 + 0.5 * np.random.randn(N)  # 加上noise

plt.plot(x, y0, "lime", lw=5, label="理想資料(無noise)")  # 無 noise, 畫預設 y = x 綠線
plt.plot(x, y1, "b", label="真實資料(有noise)")  # 有 noise, 藍線
plt.scatter(x, y1, c="b", s=100, label="真實資料(有noise)")  # 有 noise, 藍點
plt.title("原始資料")
plt.legend()
plt.grid()

plt.show()

print("------------------------------------------------------------")  # 60個

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X = x.reshape(N, 1)

linear_regression.fit(X, y1)  # 學習訓練.fit

Y = linear_regression.predict(X)  # 預測.predict

plt.plot(x, y0, "lime", lw=5, label="理想資料(無noise)")  # 無 noise, 畫預設 y = x 紅線
plt.plot(x, y1, "b", label="真實資料(有noise)")  # 有 noise
plt.scatter(x, y1, s=100, label="真實資料(有noise)")  # 有 noise
plt.plot(x, Y, "r", lw=3)  # 線性回歸曲線
plt.title("線性迴歸")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 標準函數訓練及測試
# 分訓練資料、測試資料
# 一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」,
# 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。
# 這是我們可以用sklearn.cross_validation 裡的 train_test_split來亂數選一定百分比的資料來用。

from sklearn.model_selection import train_test_split

N = 11
x = np.linspace(0, 10, N)
y0 = x
y1 = y0 + 0.5 * np.random.randn(N)  # 加上noise

plt.plot(x, y0, "lime", lw=5, label="理想資料(無noise)")  # 無 noise, 畫預設 y = x 紅線

# 把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。
x_train, x_test, y_train, y_test = train_test_split(
    x, y1, test_size=0.2, random_state=9487
)

print("訓練資料長度 :", len(x_train))
print("訓練資料內容 :", x_train)
print("測試資料長度 :", len(x_test))
print("測試資料內容 :", x_test)
print("y_train :", y_train)
print("y_test :", y_test)

X_train = x_train.reshape(len(x_train), 1)

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

linear_regression.fit(X_train, y_train)  # 學習訓練.fit

Y_train = linear_regression.predict(X_train)  # 預測.predict

plt.scatter(x_train, y_train, s=100, c="r")
plt.plot(x_train, Y_train, "g", lw=5)  # 線性回歸曲線
plt.title("訓練結果")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test), 1)
Y_test = linear_regression.predict(X_test)  # 預測.predict

mse = np.sum((Y_test - y_test) ** 2) / len(y_test)
print("MSE =", mse)
plt.plot(x, y0, "lime", lw=5, label="理想資料(無noise)")  # 無 noise, 畫預設 y = x 紅線
plt.scatter(x, y0, c="y", s=200, label="理想資料(無noise)")
plt.scatter(x_test, y_test, c="lime", s=100, label="真實資料(有noise)")
plt.scatter(x_test, Y_test, c="r", s=100, label="預測結果")
plt.title("看誤差")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

from sklearn.metrics import mean_squared_error, r2_score

Y_test = linear_regression.predict(X_test)  # 預測.predict
mse = mean_squared_error(y_test, Y_test)
r2 = r2_score(y_test, Y_test)

print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")
print("MSE =", mse)
print("R2 =", r2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("不是線性的目標函數")

# f(x) = sin(3.2x) + 0.8x

x = np.linspace(0, 5, 50)
y = np.sin(3.2 * x) + 0.8 * x + 0.3 * np.random.randn(50)
plt.scatter(x, y, label="原始資料")
plt.plot(x, y)
plt.title("不是線性的目標函數 f(x) = sin(3.2x) + 0.8x")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 標準線性學習機

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X = x.reshape(len(x), 1)

linear_regression.fit(X, y)  # 學習訓練.fit

plt.scatter(x, y, label="原始資料")
plt.plot(x, y)
plt.plot(x, linear_regression.predict(X), "r", label="標準線性學習機 預測結果")
plt.title("使用 標準線性學習機 學習的結果")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 多項式
# 使用 6 次多項式 學習

X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])

regression_poly = sklearn.linear_model.LinearRegression()  # 函數學習機

regression_poly.fit(X_poly, y)  # 學習訓練.fit

plt.scatter(x, y, label="原始資料")
plt.plot(x, y)
plt.plot(x, regression_poly.predict(X_poly), "r", label="多項式 預測結果")
plt.title("使用 6 次多項式 學習的結果")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 用 RBF!!


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

regression_rbf.fit(X_rbf, y)  # 學習訓練.fit

plt.scatter(x, y, label="原始資料")
plt.plot(x, y)
plt.plot(x, regression_rbf.predict(X_rbf), "r", label="RBF 預測結果")
plt.title("使用 RBF 學習的結果")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個

# 三種一起比較
Y_lin = linear_regression.predict(X)  # 預測.predict
Y_poly = regression_poly.predict(X_poly)  # 預測.predict
Y_rbf = regression_rbf.predict(X_rbf)  # 預測.predict

plt.scatter(x, y)

plt.plot(x, Y_lin, "r", label="標準線性學習機")
plt.plot(x, Y_poly, "g", label="6 次多項式")
plt.plot(x, Y_rbf, "b", label="RBF")
plt.title("三種一起比較")
plt.legend()
plt.grid()
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




# plt.plot([1, 9],[1, 9],'r', lw = 10)

