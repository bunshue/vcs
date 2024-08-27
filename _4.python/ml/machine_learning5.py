"""
機器學習入門


"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import time
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

# 02. 關於 overfitting

# 我們在數據分析, 就是收集了歷史資料, 比如說這些數據。

X = np.random.randn(6)
Y = np.random.randn(6)
plt.scatter(X, Y, c="r", s=100)
plt.grid()
plt.title("aaaa")
plt.show()

x = np.linspace(0, 1, 200)
y = -((x - 1) ** 2) + 1
plt.plot(x, y)
plt.grid()
plt.title("aaaa")
plt.show()


# 真實世界看來比較像是這樣...

X = np.linspace(0, 1, 20)
Y = -((X - 1) ** 2) + 1 + 0.08 * np.random.randn(20)
plt.scatter(X, Y, c="r", s=50)
plt.plot(x, y)
plt.grid()
plt.title("aaaa")
plt.show()

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x), "r")
plt.scatter(X, Y, c="r", s=50)
plt.plot(x, y)
plt.ylim(0, 2)
plt.grid()
plt.title("這叫很低的 bias, 很高的 variance")
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

y = 1.2 * x + 0.8 + 0.2 * np.random.randn(300)

# 畫出圖形來。

plt.scatter(x, y)

plt.grid()
plt.title("aaaa")
plt.show()


"""
分訓練資料、測試資料

一般我們想要看算出來的逼近函數在預測上是不是可靠, 會把一些資料留給「測試」, 就是不讓電腦在計算時「看到」這些測試資料。等函數學成了以後, 再來測試準不準確。這是我們可以用

sklearn.model_selection 裡的 train_test_split

來亂數選一定百分比的資料來用。
"""
from sklearn.model_selection import train_test_split

# 把原來的 x, y 中的 80% 給 training data, 20% 給 testing data。

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=9487
)

# len(x_train)    #80%
# len(x_test)     #20%

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

# step 1. 開一台「線性迴歸機」

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

# step 2. fit 學習、訓練

regr.fit(x_train, y_train)

# step 3. predict 預測

Ypred = regr.predict(x_test)

# x: x_test
# y: Ypred
# x_test.ravel()

plt.plot(x_test.ravel(), Ypred, "r")

plt.scatter(x_test.ravel(), y_test)

plt.grid()
plt.title("aaaa")
plt.show()


# 計算分數
from sklearn.metrics import mean_squared_error, r2_score

mse_t = mean_squared_error(y_train, regr.predict(x_train))
r2_t = r2_score(y_train, regr.predict(x_train))
print("訓練資料")
print("MSE =", mse_t)
print("R2 =", r2_t)

mse = mean_squared_error(y_test, Ypred)
r2 = r2_score(y_test, Ypred)
print("測試資料")
print(f"MSE = {mse:.4f}")
print(f"R2 = {r2:.4f}")


print("------------------------------------------------------------")  # 60個

"""
Python-3-Data-Analysis-Basics 1

"""

print("------------------------------------------------------------")  # 60個


"""
在金融預測上的應用

"""

print("------------------------------------------------------------")  # 60個

"""
神經網路
連 SVM 都沒辦法, 那一定是方法還不夠高級, 所以我們用更高級的神經網路來做做看!
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

# [2] 打造我們的神經網路函數學習機

model = Sequential()

model.add(Dense(20, input_dim=5))

model.add(Activation("relu"))

model.add(Dense(20))

model.add(Activation("relu"))

model.add(Dense(1))

model.add(Activation("sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# 看一下我們神經網路長什麼樣子, 有沒有做錯。

model.summary()


""" TBD
#[3] 訓練

model.fit(x_train, yb_train, batch_size=100, epochs=20)


#[4] 預測

#看起來不太妙, 我們來試試預測...

NN_pred = model.predict_classes(x_test)

YP_NN = yb_test[(NN_pred==1).ravel()]

len(YP_NN)

458

len(YP_NN[YP_NN == 1])

246

246/458

0.537117903930131

結果真是慘慘慘, 怎麼會這樣呢?

"""

print("------------------------------------------------------------")  # 60個

"""
13.畫我們練習成果的討論


"""

print("------------------------------------------------------------")  # 60個

# 02 [練習] 圖形化我們的成果

# 1. 上次的成果拿回來使用

# 記得上次我們做了個鳶尾花分類器。
# 1.1 找回我們的分類器

from sklearn.externals import joblib

clf = joblib.load("iris_clf_01.pkl")

# 真的可以用了嗎?

print(clf.predict([[2, 3]]))


# 可以! 太棒了!
# 1.2 看看我們分類的全貌

# 我們用一下之前的方式, 畫出我們想要看到我們可愛的 SVM 是怎麼以花萼長度、花萼寬度來分類的。
# 上次我們用了 Python 所謂 "list comprehension" 的作法 (本質上是 for 迴圈), 現在我們換個方式看來比較「高級」的方式。

xt, yt = np.meshgrid(np.arange(-2, 2, 0.5), np.arange(-1, 1, 0.5))

print(xt)
print(yt)

# 看得出來 meshgrid 做了什麼呢? 基本上它就是說我們在 x, y 兩個指定範圍的長方型當中, 依我們指定的間隔找出格點。
# 這些格點的座標分成 x 座標一個 array, y 座標一個。x 或 y 座標的 array, 的座標是一列一列標記的。
# 要是你覺得這樣的表示法很討厭, 我們也可以讓它變一長串的向量。

print(xt.ravel())

# 注意這其實原來的 xt 並沒有變哦。

print(xt)

# 我們可以把 (x,y) 一點一點的座標收集起來嗎?

print(np.c_[xt.ravel(), yt.ravel()])


# 把資料的型式這樣變來變去會是數據分析非常非常常做的事情。
# 我們經這麼多廢話後終於可以來做正事。

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.2), np.arange(1.5, 5.0, 0.2))

Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z)
plt.show()

# 雖然看來我們用了比較多白痴的方法做出一樣的事, 不過一些技巧之後也可以常常使用。
# 1.3 快速換個配色

plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.show()


plt.scatter(xx.ravel(), yy.ravel(), s=50, c=Z, cmap=plt.cm.prism, alpha=0.8)
plt.show()


# 1.4 取回鳶尾花訓練資料

from sklearn.datasets import load_iris

iris = load_iris()

x = iris.data[:, :2]

y = iris.target

# 我們來畫畫比較。

plt.subplot(121)

plt.scatter(x[:, 0], x[:, 1], s=50, c=y)

plt.subplot(122)

plt.scatter(x[:, 0], x[:, 1], s=50, c=clf.predict(x))

plt.show()

# 左邊的是訓練資料, 右邊是用我們 SVM 分類器分出來的。你有看出差異嗎? 是不是很難看出? 我們來用用另一個方式。

# 1.5 畫圖的另一個方式

xx, yy = np.meshgrid(np.arange(3, 8.5, 0.02), np.arange(1.5, 5.0, 0.02))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.show()


Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
plt.scatter(x[:, 0], x[:, 1], s=50, c=y, cmap=plt.cm.coolwarm)
plt.show()

print("------------------------------------------------------------")  # 60個

# 打開一個線性迴歸的函數學習機

from sklearn.linear_model import LinearRegression

regr = LinearRegression()

# 造資料, 調整成 sklearn 會接受的形狀

x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

X = x.reshape(len(x), 1)

# 把資料放進函數學習機，開始它的訓練

regr.fit(X, y)

# 用 predict 看一下訓練的成果，順便畫個圖

Y = regr.predict(X)

plt.scatter(x, y)
plt.plot(x, Y, "r")
plt.show()

# 結果看起來不錯，會有微小誤差的原因，則是因為真實世界的資料有不可避免的雜訊

print("------------------------------------------------------------")  # 60個

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# 均勻地在 0 到 5 之間取一百個點，再隨便決定一個函數，叫做 y = f(x) = 1.9x + 0.8 好了
# 為了增加真實感，加上一點雜訊

x = np.linspace(0, 5, 100)
y = 1.9 * x + 0.8 + 0.5 * np.random.randn(100)

# 開開心心地讓 sklearn 幫我們分離出訓練資料跟測試資料，測試資料的比例是 0.3 的話，
# 訓練資料就會自動是 0.7 了呢，真是方便！
# random_state 可以是耍寶用的 87 ，要選其他數字也當然可以

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.3, random_state=87
)
x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

# 一樣叫出一個線性迴歸的函數學習機，再放進「訓練資料」讓它開始訓練

regr = LinearRegression()
regr.fit(x_train, y_train)

# 用 plot 把「訓練資料」的正確答案畫成一條線，再把模型 predict 出來的結果描點畫在同一張圖上
# 可以清楚的看到結果

plt.scatter(x_train, y_train)
plt.plot(x_train, regr.predict(x_train), "r")
plt.show()


# 跟上面一樣的做法，只是這次對象換成「測試資料」

plt.scatter(x_test, y_test)
plt.plot(x_test, regr.predict(x_test), "r")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個




