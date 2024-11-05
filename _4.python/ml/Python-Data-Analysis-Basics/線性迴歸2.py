"""
線性迴歸2
迴歸法預測函數


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

# SVR 迴歸的預測
# 數據分析

# 1. 線性迴歸

# 一條直線
# f(x) = 1.2 x + 0.8

# 準備好個 N 個點
N = 100
x = np.linspace(0, 5, N)
y = 1.2 * x + 0.8

plt.scatter(x, y)
plt.plot(x, y, "lime")
plt.title("理想資料")
plt.show()

# 加入 noise 項, 假設 f(x)+ε(x), 也就是都有個 noise 項。

y = 1.2 * x + 0.8 + 0.5 * np.random.randn(N)

plt.scatter(x, y)
plt.plot(x, 1.2 * x + 0.8, "lime")
plt.title("理想資料加上雜訊")
plt.show()

# 做線性迴歸找出那條線

# 方法一
# 做線性迴歸有很多套件, 但我們這裡用 sklearn.svm 裡的 SVR 來做各種迴歸。

from sklearn.svm import SVR

svr_lin = SVR(kernel="linear", C=1e3)

"""
x資料不能直接用 要改成X
原來我們 x 的資料型態是
[x1,x2,…,x50],
但 sklearn 希望每個 x 是個向量, 也就是:
[[x1],[x2],…,[x50]]
"""

X = x.reshape(len(x), 1)

print(x.shape)
print(X.shape)

svr_lin.fit(X, y)  # 學習訓練.fit

y_pred = svr_lin.predict(X)  # 預測.predict

plt.scatter(x, y)
plt.plot(x, y_pred, "r")
plt.plot(x, 1.2 * x + 0.8, "lime")

plt.title("SVR線性迴歸1")
plt.show()


# 當然可以預測沒出現過的...
# 注意資料的輸入方式。

print(svr_lin.predict([[6.2]]))  # 預測.predict
print(svr_lin.predict([[6.2], [7.4], [8]]))  # 預測.predict

# 方法二

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

"""
這裡要注意我們本來的 x 是
[x1,x2,…,x50]
但現在要的是
[[x1],[x2],…,[x50]]
"""

X = x.reshape(len(x), 1)

linear_regression.fit(X, y)  # 學習訓練.fit

y_pred = linear_regression.predict(X)  # 預測.predict

plt.scatter(x, y)
plt.plot(x, y_pred, "r")
plt.title("線性迴歸2")
plt.show()

# 2. 標準函數訓練及測試
# 分訓練資料、測試資料
# 一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」,
# 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。
# 這是我們可以用 sklearn.cross_validation 裡的 train_test_split 來亂數選一定百分比的資料來用。
# 哦, 這看起來是線性的函數 (廢話, 我們自己生的)。現在我們來做線性迴歸。
# 開始前我們來做一件事, 就是我們喜歡只拿一部份的資料來學習, 叫「訓練資料」, 另外留一部份當「測試資料」。
# 測試資料在「訓練」期電腦是沒看過的, 所以我們可以「考他」。
# 要把我們完整資料分測試、訓練很簡單, 因為 SciKit Learn 自己會幫我們做。指令叫 train_test_split (實在有夠白話)。

"""
分訓練資料、測試資料
一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」,
就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用
sklearn.model_selection 裡的 train_test_split 來亂數選一定百分比的資料來用。
"""

from sklearn.model_selection import train_test_split

# 把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=9487
)
print(f"訓練資料有 {len(x_train)} 筆,")  # 80%
print(f"測試資料有 {len(x_test)} 筆。")  # 20%

xx = np.array([3, 9, 8, 1, 2])
yy = np.array([1, 3, 9, 2, 4])

# 目前 xx 是個 5 維向量。
print(xx.shape)

# 用 reshape 改成 5×1 的矩陣。
xx = xx.reshape(len(xx), 1)

"""
執行之後會回傳回四個 array, 分別是 x 的訓練、測試, y 的訓練測試。所以我們準備用
x_train, x_test, y_train, y_test
來「接」。接著要放我們原來的 x, y 這很自然, 然後
test_size=0.2
是說我們要留 20% 當測試, 這比例當然是自己可以調的。最後神奇的一步說
random_state=9487
這是確保你之後回來執行這個程式, 隨機取的 80% 訓練資料、20% 測試資料是一樣的 (那個數字你可以自己選)。
為什麼我們要這樣做啊? 原因之一是因為以後我們學得比較多, 有可能第一次沒有訓練得很滿意, 我們想調整我們的「函數學習機」, 再學一次。這時如果是換了訓練資料我們就不太能確定最後學好或學壞, 是因為我們的調整, 還是不同的資料產生的結果。
檢查訓練、測試資料是不是照我們的意思去分 (疑心病幹嘛那麼重)。
"""

"""
再來很重要, 從現在到以後, 很多學函數的方法, 都要求我們訓練資料要排成一列一列的。也就說原本的
[x1,x2,…,x80]
要換成這樣
[[x1],[x2],…,[x80]]
好在我們學過 reshape, 這小事...
"""

# 正式轉我們的訓練資料
x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# 接下來就是召喚 LinearRegression 學習機了。

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

# 從現在的線性迴歸, 到等一下的機器學習, 再到之後的神經網路。我們每一次其實就是先開一台空的「函數學習機」, 現在我們要開一台「迴歸機」。

# 因為線性迴歸實在太簡單, 通常也不太需要調校什麼, 我們就可以直接訓練了。訓練就用 fit, 然後把訓練資料餵進去...

linear_regression.fit(x_train, y_train)  # 學習訓練.fit

# 然後就學完了!　我們來試用一下。因為我們的學數學習機喜歡一次吃很多資料一起告訴你答案, 所以就算只有一筆也要這樣下指令。
print("打印一些結果")
print(linear_regression.predict([[1.3]]))  # 預測.predict
print(linear_regression.predict([[2.7], [1.5]]))  # 預測.predict

# 我們當然可以餵測試資料進去, 畢竟只有這些我們是有答案、但我們的學習機是還沒學過的。

y_pred = linear_regression.predict(x_test)  # 預測.predict

plt.plot(x_test, y_pred, "r")
# plt.plot(x_test.ravel(), y_pred, 'g')
plt.scatter(x_test, y_test)
# plt.scatter(x_test.ravel(), y_test)
plt.title("原始測試資料")
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

plt.scatter(x_train, y_train)
plt.plot(x_train, linear_regression.predict(x_train), "r")
plt.title("訓練結果")
plt.show()

# 我們在「訓練」這個函數時只有以下這些資料。
plt.scatter(x_train, y_train)  # 原始訓練資料
plt.title("原始訓練資料")
plt.show()

# 用訓練資料來 fit 函數 方法一
# 記得現在我們只用 80% 的資料去訓練。

svr_lin = SVR(kernel="linear", C=1e3)
X_train = x_train.reshape(len(x_train), 1)
svr_lin.fit(X_train, y_train)  # 學習訓練.fit

Y_train = svr_lin.predict(X_train)  # 預測.predict

plt.scatter(x_train, y_train)  # 原始訓練資料

plt.plot(x_train, Y_train, "r")
plt.title("訓練資料2")
plt.show()

# 用測試資料試試我們預測準不準

X_test = x_test.reshape(len(x_test), 1)
Y_test = svr_lin.predict(X_test)  # 預測.predict
mse = np.sum((Y_test - y_test) ** 2) / len(y_test)
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
linear_regression.fit(X_train, y_train)  # 學習訓練.fit

Y_train = linear_regression.predict(X_train)  # 預測.predict

plt.scatter(x_train, y_train)  # 原始訓練資料
plt.plot(x_train, Y_train, "r")
plt.title("線性回歸測試結果")
plt.show()

# 用測試資料試試我們預測準不準
X_test = x_test.reshape(len(x_test), 1)
Y_test = linear_regression.predict(X_test)
mse = np.sum((Y_test - y_test) ** 2) / len(y_test)

print("MSE =", mse)

plt.scatter(x_test, y_test, c="b")
plt.scatter(x_test, Y_test, c="r")
plt.title("測試結果2")
plt.show()

# 3. 不是線性的目標函數
# 這裡我們用個非線性的函數來生假數據:
# f(x) = sin(3.2x) + 0.8x
# 一樣準備加上一些 noise。
# 3. 生成假資料

# 準備好個 N 個點
N = 50
x = np.linspace(0, 5, N)
y = np.sin(3.2 * x) + 0.8 * x + 0.3 * np.random.randn(N)

plt.plot(x, y)
plt.title("待處理的資料 f = sin(3.2x) + 0.8x + noise")
plt.show()

# 使用SVR

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1)

# 準備生這個函數
svr_rbf = SVR(kernel="rbf", C=1e3, gamma=0.3)
svr_lin = SVR(kernel="linear", C=1e3)
svr_poly = SVR(kernel="poly", C=1e3, degree=4)

X_train = x_train.reshape(len(x_train), 1)

svr_rbf.fit(X_train, y_train)  # 學習訓練.fit
svr_lin.fit(X_train, y_train)  # 學習訓練.fit
svr_poly.fit(X_train, y_train)  # 學習訓練.fit

# 看看訓練成果

X = x.reshape(len(x), 1)
Y_rbf = svr_rbf.predict(X)  # 預測.predict
Y_lin = svr_lin.predict(X)  # 預測.predict
Y_poly = svr_poly.predict(X)  # 預測.predict

plt.scatter(x, y)
plt.plot(x, Y_rbf, label="rbf")
plt.plot(x, Y_lin, label="linear")
plt.plot(x, Y_poly, label="polynomial")

plt.legend()
plt.title("比較各種方法")
plt.show()

# 標準線性學

# 做線性迴歸, 用 sklearn 裡的 LinearRegression 來做線性迴歸
linear_regression = sklearn.linear_model.LinearRegression()  # 函數學習機

X = x.reshape(len(x), 1)

linear_regression.fit(X, y)  # 學習訓練.fit

plt.scatter(x, y)
plt.plot(x, linear_regression.predict(X), "r")
plt.title("標準線性學")
plt.show()

# 果然超級不準, 該如何是好?
# 多項式
# 我們來用 6 次多項式學

X_poly = np.array([[k, k**2, k**3, k**4, k**5, k**6] for k in x])

regr_poly = sklearn.linear_model.LinearRegression()  # 函數學習機

regr_poly.fit(X_poly, y)  # 學習訓練.fit

plt.scatter(x, y)
plt.plot(x, regr_poly.predict(X_poly), "r")
plt.title("多項式")

plt.show()

# 用 RBF
# ϕi=e−∥x−ci∥2/2σ2


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

regr_rbf = sklearn.linear_model.LinearRegression()  # 函數學習機

regr_rbf.fit(X_rbf, y)  # 學習訓練.fit

plt.scatter(x, y)

plt.plot(x, regr_rbf.predict(X_rbf), "r")
plt.title("RBF")

plt.show()

# 三種一起比較

Y_lin = linear_regression.predict(X)
Y_poly = regr_poly.predict(X_poly)
Y_rbf = regr_rbf.predict(X_rbf)

plt.scatter(x, y)
plt.plot(x, Y_lin, label="linear")
plt.plot(x, Y_poly, label="polynomial")
plt.plot(x, Y_rbf, label="rbf")
plt.legend()
plt.title("三種一起比較")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


