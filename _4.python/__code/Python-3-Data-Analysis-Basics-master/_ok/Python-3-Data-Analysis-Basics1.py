"""

Python-3-Data-Analysis-Basics 1


"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
'''
print('------------------------------------------------------------')	#60個

x = np.linspace(0, 1, 200)
y = -(x - 1) ** 2 + 1

X = np.random.rand(6)
Y = np.random.rand(6)

def myplot(n = 1):
    plt.scatter(X, Y, c = 'r', s = 100)
    x = np.linspace(0, 1, 1000)
    y = 0.5*np.sin(n*x) + 0.5
    plt.plot(x, y)

myplot(5)
plt.show()

print('------------------------------------------------------------')	#60個

#過度擬合 (overfitting)

#用拉格朗日 (Lagrange) 插值法學起來!

x = np.linspace(0, 1, 200)
y = -(x - 1) ** 2 + 1
plt.plot(x, y, 'lime')

X = np.linspace(0, 1, 20)
Y = -(X-1) ** 2 + 1 + 0.08 * np.random.randn(20)
plt.scatter(X,Y, c = 'b', s = 50)

z = np.polyfit(X, Y, 19)
p = np.poly1d(z)
plt.plot(x, p(x),'r')

xmin, xmax, ymin, ymax = 0, 1, 0, 1.5
plt.axis([xmin, xmax, ymin, ymax])  #設定各軸顯示範圍

plt.show()

print('------------------------------------------------------------')	#60個



"""
#【秘技】分列 X, Y 的變成點座標

等一下我們會大量的把資料變換形式, 現在我們先熱身。在畫圖時常常用到把 x, y 座標分列。現在我們要合成點要怎麼做呢? 也就是說
X1 <-- [1,2,3,4]
Y1 <-- [5,6,7,8]
希望變成
[[1,5], [2,6], [3,7], [4,8]]
"""

X1 = np.array([1,2,3,4])
Y1 = np.array([5,6,7,8])

#NumPy 有個神奇的方式會幫我們做!

ccc = np.c_[X1, Y1]
print(ccc)


"""
【重要插播】meshgrid 用法

為了用 contourf (填充型的等高線) 呈現我們成果, 我們要介紹一個初學有點難理解、meshgrid 的概念。

meshgrid 是產生格點的方式, 通常是我們要畫 3D 曲面啦、或是等高線的時候要先為我們在 xy 平面上「佈點」, 然後算出每點的高度 Z。

我們要做的是給定 x 方向座標, y 方向座標, 然後就產生格點, 如圖示。
"""


#於是我們再度用我們的 X1, Y1 示範。

X1 = np.array([1,2,3,4])

Y1 = np.array([5,6,7,8])

#因為 matplotlib 很愛 x, y-座標分開, 經 meshgrid 後也是分開的! 所以我們用 Xm 和 Ym 來接。

Xm, Ym = np.meshgrid(X1,Y1)

#看一下內容...

print(Xm)
print(Ym)

#等等, 這什麼啊? 原來 meshgrid 存網格的 x 座標是一列一列存的。
#同理我們可以理解 Ym 的內容為什麼是這樣了...

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

#01 numpy 的 filter

egg = np.array([3, -5, 10, 23, -5, 11])

idx = (egg >= 0)

print(idx)

#array([ True, False,  True,  True, False,  True])

print(egg[idx])

#array([ 3, 10, 23, 11])

print(egg[egg >= 0])

#array([ 3, 10, 23, 11])


x = np.linspace(-10, 10, 1000)

y = np.sin(x)

plt.plot(x, y)

plt.scatter(x[y>0], y[y>0], c='r')
plt.show()

#02 Overfitting

Px = np.random.rand(6)
Py = np.random.rand(6)
plt.scatter(Px, Py, c='r', s=50)

plt.show()

x = np.linspace(0, 1, 1000)

y = 0.5*np.sin(x) + 0.5

plt.scatter(Px, Py, c='r', s=50)

plt.plot(x, y)

plt.show()

def myplot(n=1):

    y = 0.5*np.sin(n*x) + 0.5

    plt.scatter(Px, Py, c='r', s=50)

    plt.plot(x, y)

myplot(3)
plt.show()

print('------------------------------------------------------------')	#60個

'''

import numpy as np

import matplotlib.pyplot as plt

from keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下6行

import numpy as np  
path = 'C:/_git/vcs/_4.python/ml/mnist.npz'
mnist = np.load(path)  
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()  

x_train = x_train/255

x_test = x_test/255

from keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)

y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential

from keras.layers import Dense, Flatten

from keras.optimizers import SGD

model = Sequential()

model.add(Flatten(input_shape=(28, 28)))

model.add(Dense(20, activation='relu'))


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

print('作業完成')

