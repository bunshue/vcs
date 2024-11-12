"""



"""

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

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

print('載入 mnist')
from tensorflow.keras.datasets import mnist

#(x_train, y_train), (x_test, y_test) = mnist.load_data()  # 或改成以下4行

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist['x_train'], mnist['y_train']  
x_test, y_test = mnist['x_test'], mnist['y_test']  
mnist.close()


print('訓練資料長度 :', len(x_train))
print('測試資料長度 :', len(x_test))


print('看第 1234 筆訓練資料')

n = 1234
print('內容 :', x_train[n])
print('大小 :', x_train[n].shape)
print('目標 :', y_train[n])

plt.imshow(x_train[n], cmap='Greys')
#plt.show()

x_train = x_train.reshape(60000, 784) / 255
x_test = x_test.reshape(10000, 784) / 255

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print(y_train[n])

#array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

#3 層 100 100 100
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

#step01. 打造函數學習機
model = Sequential()
model.add(Dense(100, input_dim=784, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='mse', optimizer=SGD(lr=0.087), metrics=['accuracy'])
model.summary()

print("x_train.shape :", x_train.shape)

# 學習訓練.fit
# 共有N個樣品, 一次做 batch_size 個, 一輪需要做 N / batch_size 次
#model.fit(x_train, y_train, batch_size=100, epochs=10)
#model.fit(x_train, y_train, batch_size=1000, epochs=10)
model.fit(x_train, y_train, batch_size=2000, epochs=1) # 遞迴 epochs 次

y_pred = model.predict_step(x_test)  # 預測.predict
print(y_pred)

n = 5566
print('神經網路預測', y_pred[n])
print(y_pred[n].shape)

plt.imshow(x_test[n].reshape(28,28), cmap='Greys')
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print('寫入 模型 TBD')

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
sys.exit()

print('讀取 模型')
from tensorflow.keras.models import load_model

model = load_model('mynn01.h5')

from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist['x_train'], mnist['y_train']
x_test, y_test = mnist['x_test'], mnist['y_test']
mnist.close()
"""

x_test = x_test.reshape(10000, 784)/255

y_pred = model.predict_classes(x_test)

print(y_pred)

def myNN(n):
  k = int(n)
  print('可愛神經網路預測', y_pred[k])
  plt.imshow(x_test[k].reshape(28,28), cmap='Greys')

myNN(9487)


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

