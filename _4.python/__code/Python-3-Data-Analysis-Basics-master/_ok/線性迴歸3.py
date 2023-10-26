"""
colab_機器學習入門2022


"""

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

#迴歸法預測函數

#製作數據
x = np.linspace(0, 1, 300)
y = 1.2*x + 0.8 + 0.1*np.random.randn(300)

plt.scatter(x,y)

"""
分訓練資料、測試資料

一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用

sklearn.model_selection

裡的

train_test_split

來亂數選一定百分比的資料來用。
"""

from sklearn.model_selection import train_test_split

#把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size = 0.2,
                                                    random_state = 9487)
print(f"訓練資料有 {len(x_train)} 筆,")
print(f"測試資料有 {len(x_test)} 筆。")



xx = np.array([3, 9, 8, 1, 2])
yy = np.array([1, 3, 9, 2, 4])

#目前 xx 是個 5 維向量。
print(xx.shape)

#用 reshape 改成 5×1 的矩陣。
xx = xx.reshape(len(xx), 1)

#正式轉我們的訓練資料
x_train = x_train.reshape(len(x_train),1)
x_test = x_test.reshape(len(x_test), 1)

#接著進入 AI 建模三部曲。
#step 1. 開一台「線性迴歸機」

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

#step 2. fit 學習、訓練
regr.fit(x_train, y_train)

LinearRegression()

#step 3. predict 預測
y_pred = regr.predict(x_test)

plt.plot(x_test.ravel(), y_pred, 'r')
plt.scatter(x_test.ravel(), y_test)
plt.show()

#計算分數
from sklearn.metrics import mean_squared_error, r2_score
mse_t = mean_squared_error(y_train, regr.predict(x_train))
r2_t = r2_score(y_train, regr.predict(x_train))

print('訓練資料')
print('MSE =', mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('作業完成')

