"""
標準 神經網路 做手寫辨識

Keras 可以用各種不同的深度學習套件當底層, 指定用 Tensorflow 以確保執行的一致性。

%env KERAS_BACKEND=tensorflow

讀入 MNIST 數據庫

MNIST 是有一堆 0-9 的手寫數字圖庫。有 6 萬筆訓練資料, 1 萬筆測試資料。
它是 "Modified" 版的 NIST 數據庫, 原來的版本有更多資料。
這個 Modified 的版本是由 LeCun, Cortes, 及 Burges 等人做的。可以參考這個數據庫的原始網頁。

MNIST 可以說是 Deep Learning 最有名的範例, 它被 Deep Learning 大師 Hinton 稱為「機器學習的果蠅」。
2.2.1 由 Keras 讀入 MNIST

Keras 很貼心的幫我們準備好 MNIST 數據庫, 我們可以這樣讀進來 (第一次要花點時間)。
http://yann.lecun.com/exdb/mnist/

用tensorflow讀入 MNSIT 數據集
from tensorflow.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 標準 1 遠端檔案
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 標準 2 本地檔案
mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()
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

from keras.datasets import mnist
from tensorflow.keras.datasets import mnist

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("訓練資料長度 :", len(x_train))
print("測試資料長度 :", len(x_test))

print("看第 1234 筆訓練資料")

n = 1234
print("內容 :", x_train[n])
print("大小 :", x_train[n].shape)
print("目標 :", y_train[n])

plt.imshow(x_train[n], cmap="Greys")
plt.show()

x_train = x_train.reshape(60000, 784) / 255
x_test = x_test.reshape(10000, 784) / 255

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print(y_train[n])

# array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

# 3 層 100 100 100
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# step01. 打造函數學習機
model = Sequential()
model.add(Dense(100, input_dim=784, activation="relu"))
model.add(Dense(100, activation="relu"))
model.add(Dense(100, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss="mse", optimizer=SGD(lr=0.087), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

print("x_train.shape :", x_train.shape)

# 學習訓練.fit
# 共有N個樣品, 一次做 batch_size 個, 一輪需要做 N / batch_size 次
# model.fit(x_train, y_train, batch_size=100, epochs=10)# 學習訓練.fit
# model.fit(x_train, y_train, batch_size=1000, epochs=10)# 學習訓練.fit
model.fit(x_train, y_train, batch_size=2000, epochs=1)  # 遞迴 epochs 次# 學習訓練.fit

y_pred = model.predict_step(x_test)  # 預測.predict
print(y_pred)

n = 5566
print("神經網路預測", y_pred[n])
print(y_pred[n].shape)

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.python.keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
train_feature_normalize = train_feature_vector / 255
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

model = Sequential()  # 建立模型

model.add(
    Dense(
        units=256,  # 輸入層：784, 隱藏層：256
        input_dim=784,
        kernel_initializer="normal",
        activation="relu",
    )
)
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))  # 輸出層：10
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
model.fit(
    x=train_feature_normalize,
    y=train_label_onehot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

scores = model.evaluate(test_feature_normalize, test_label_onehot)  # 評估準確率

print("\n準確率=", scores[1])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("寫入 模型")

from tensorflow.python.keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
train_feature_normalize = train_feature_vector / 255
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

model = Sequential()  # 建立模型

model.add(
    Dense(
        units=256,  # 輸入層：784, 隱藏層：256
        input_dim=784,
        kernel_initializer="normal",
        activation="relu",
    )
)
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))  # 輸出層：10
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
model.fit(
    x=train_feature_normalize,
    y=train_label_onehot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

# 評估準確率
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print("\n準確率=", scores[1])

model.save("tmp_Mnist_mlp_model.h5")

print("tmp_Mnist_mlp_model.h5 模型儲存完畢!")


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
sys.exit()

print("讀取 模型")
from tensorflow.keras.models import load_model

model = load_model("mynn01.h5")

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_test = x_test.reshape(10000, 784) / 255

y_pred = model.predict_classes(x_test)

print(y_pred)


def myNN(n):
    k = int(n)
    print("神經網路預測", y_pred[k])
    plt.imshow(x_test[k].reshape(28, 28), cmap="Greys")


myNN(9487)


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("看 label")
from tensorflow.python.keras.utils import np_utils

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

print(train_label[0:5])
train_label_onehot = np_utils.to_categorical(train_label)
print(train_label_onehot[0:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("看 graph")

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
# print(train_feature_vector[0])
train_feature_normalize = train_feature_vector / 255
print(train_feature_normalize[0])


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 一些 fail
print('Auto-Keras')

from keras.datasets import mnist
from autokeras import ImageClassifier
from autokeras.constant import Constant
import autokeras
from keras.utils import plot_model
    
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))
clf = ImageClassifier(verbose=True, augment=False)
clf.fit(x_train, y_train, time_limit=500 * 60)  # 學習訓練.fit
clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)
y = clf.evaluate(x_test, y_test)
print(y * 100)
clf.export_keras_model('model.h5')
plot_model(clf, to_file='model.png')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
