"""
機器學習入門


"""

import sys
import numpy as np
import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

"""
01.讀入基本套件

機器學習其實基本上和我們一直以來說的一樣, 就是我們要學一個未知的函數
f(x)=y

如果是分類, 基本上就是有一筆資料 x=(x1,x2,…,xk), 我們想知道這
f(x)=y,其中的 y 就是某一個類別。

這種學函數的方法, 又可以分為:

    supervised learning
    unsupervised learning

其中的 supervised learning 就是我們有一組知道答案的訓練資料, 然後找到我們要的函數。而 unsupervised learning 就神了, 我們不知道答案, 卻要電腦自己去學!

做數據分析, 幾乎每一次都要讀入這些套件!
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 用 Seaborn 畫圖, 並設好圖的大小

import seaborn as sns
sns.set(rc={'figure.figsize':(11.7,8.27)})


#02. 關於 overfitting

#我們在數據分析, 就是收集了歷史資料, 比如說這些數據。

X = np.random.randn(6)
Y = np.random.randn(6)
plt.scatter(X, Y, c='r', s=100)
plt.grid()
plt.title('aaaa')
plt.show()

x = np.linspace(0, 1, 200)
y = -(x-1)**2+1
plt.plot(x,y)
plt.grid()
plt.title('aaaa')
plt.show()


#真實世界看來比較像是這樣...

X = np.linspace(0, 1, 20)
Y = -(X-1)**2+1 + 0.08*np.random.randn(20)
plt.scatter(X,Y, c='r',s=50)
plt.plot(x,y)
plt.grid()
plt.title('aaaa')
plt.show()

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x),'r')
plt.scatter(X,Y, c='r',s=50)
plt.plot(x,y)
plt.ylim(0, 2)
plt.grid()
plt.title('這叫很低的 bias, 很高的 variance')
plt.show()

"""
03. 迴歸法預測函數
03-1. 假的數據真的迴歸
做一條直線

我們來一條線, 比如說 f(x)=1.2x+0.8

準備好個 1000 個點 (現場建議, 雖然多了一點...)

加入 noise 項, 看來更真實 大概的想法就是, 我們真實世界的問題, 化成函數, 我們假設背後有個美好的函數。但相信我們很少看到真實世界的資料那麼漂亮。在統計上, 我們就是假設

𝑓(𝑥)+𝜀(𝑥)

也就是都有個 noise 項。
"""

x = np.linspace(0, 1, 300)

y = 1.2*x + 0.8 + 0.2*np.random.randn(300)

#畫出圖形來。

plt.scatter(x,y)

plt.grid()
plt.title('aaaa')
plt.show()


"""
分訓練資料、測試資料

一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用

sklearn.model_selection 裡的 train_test_split

來亂數選一定百分比的資料來用。
"""
from sklearn.model_selection import train_test_split

#把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                   test_size = 0.2,
                                                   random_state = 9487)

#len(x_train)    #80%
#len(x_test)     #20%

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

#正式轉我們的訓練資料

x_train = x_train.reshape(len(x_train),1)
x_test = x_test.reshape(len(x_test), 1)

#step 1. 開一台「線性迴歸機」

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

#step 2. fit 學習、訓練

regr.fit(x_train, y_train)

#step 3. predict 預測

Ypred = regr.predict(x_test)

# x: x_test
# y: Ypred
# x_test.ravel()

plt.plot(x_test.ravel(), Ypred, 'r')

plt.scatter(x_test.ravel(), y_test)

plt.grid()
plt.title('aaaa')
plt.show()


#計算分數
from sklearn.metrics import mean_squared_error, r2_score
mse_t = mean_squared_error(y_train, regr.predict(x_train))
r2_t = r2_score(y_train, regr.predict(x_train))
print('訓練資料')
print('MSE =', mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, Ypred)
r2 = r2_score(y_test, Ypred)
print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")




print('------------------------------------------------------------')	#60個


print('作業完成')

