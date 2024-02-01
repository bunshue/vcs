import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt 

#打開一個線性迴歸的函數學習機

from sklearn.linear_model import LinearRegression
regr = LinearRegression()

#造資料, 調整成 sklearn 會接受的形狀

x = np.linspace(0, 5, 100)
y = 1.9*x + 0.8 + 0.5*np.random.randn(100)

X = x.reshape(len(x), 1)

#把資料放進函數學習機，開始它的訓練

regr.fit(X, y)

#用 predict 看一下訓練的成果，順便畫個圖

Y = regr.predict(X)

plt.scatter(x, y)
plt.plot(x, Y, 'r' )
plt.show()

#結果看起來不錯，會有微小誤差的原因，則是因為真實世界的資料有不可避免的雜訊

print('------------------------------------------------------------')	#60個

import numpy as np
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#均勻地在 0 到 5 之間取一百個點，再隨便決定一個函數，叫做 y = f(x) = 1.9x + 0.8 好了
#為了增加真實感，加上一點雜訊

x = np.linspace(0, 5, 100)
y = 1.9*x + 0.8 + 0.5*np.random.randn(100)

#開開心心地讓 sklearn 幫我們分離出訓練資料跟測試資料，測試資料的比例是 0.3 的話，
#訓練資料就會自動是 0.7 了呢，真是方便！
#random_state 可以是耍寶用的 87 ，要選其他數字也當然可以

x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                    test_size = 0.3,
                                                    random_state = 87)
x_train = x_train.reshape(len(x_train), 1)
x_test = x_test.reshape(len(x_test), 1)

#一樣叫出一個線性迴歸的函數學習機，再放進「訓練資料」讓它開始訓練

regr = LinearRegression()
regr.fit(x_train, y_train)

#用 plot 把「訓練資料」的正確答案畫成一條線，再把模型 predict 出來的結果描點畫在同一張圖上
#可以清楚的看到結果

plt.scatter(x_train, y_train)
plt.plot(x_train, regr.predict(x_train), 'r')
plt.show()


#跟上面一樣的做法，只是這次對象換成「測試資料」

plt.scatter(x_test, y_test)
plt.plot(x_test, regr.predict(x_test), 'r')
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個





