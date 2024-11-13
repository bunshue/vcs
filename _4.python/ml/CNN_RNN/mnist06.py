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

from keras.datasets import mnist

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 我們來看看訓練資料是不是 6 萬筆、測試資料是不是有 1 萬筆。

print("訓練資料x長度 :", len(x_train))
print("訓練資料y長度 :", len(y_train))
print("測試資料x長度 :", len(x_test))
print("測試資料y長度 :", len(y_test))

RATIO = 4

x_train = x_train[: int(len(x_train) / RATIO)]
y_train = y_train[: int(len(y_train) / RATIO)]
x_test = x_test[: int(len(x_test) / RATIO)]
y_test = y_test[: int(len(y_test) / RATIO)]

print("訓練資料x長度 :", len(x_train))
print("訓練資料y長度 :", len(y_train))
print("測試資料x長度 :", len(x_test))
print("測試資料y長度 :", len(y_test))

"""
2.2.2 數據庫的內容

每筆輸入 (x) 就是一個手寫的 0-9 中一個數字的圖檔, 大小為 28x28
而輸出 (y) 當然就是「正確答案」
"""

fig = plt.figure(figsize=(10, 10))
for i in range(100):
    ax = plt.subplot2grid((10, 10), (int(i / 10), int(i % 10)))
    ax.imshow(x_train[i], cmap=plt.cm.gray)
    ax.axis("off")
plt.suptitle("畫前100筆資料")
plt.show()

# 編號87的訓練資料
# x_train[87]

# 因為是圖檔, 當然可以顯示出來!
plt.imshow(x_train[87], cmap="Greys")
plt.title("編號87的訓練資料")
plt.show()

print("編號87的訓練資料 的 shape :", x_train[87].shape)
print("編號87的訓練資料 的 目標  :", y_train[87])

"""
2.2.3 輸入格式整理

我們現在要用標準神經網路學學手寫辨識。
原來的每筆數據是個 28x28 的矩陣 (array),
但標準神經網路只吃「平平的」, 也就是每次要 28x28=784 長的向量。
因此我們要用 reshape 調校一下。
"""

print("訓練資料 x_train.shape =", x_train.shape)
print("測試資料 x_test.shape =", x_test.shape)

# 我們做一下 normalization, 把所有的數字都改為 0 到 1 之間。
x_train = x_train / 255
x_test = x_test / 255

"""
x_train = x_train/255
x_test = x_test/255
x_train.shape
#(60000, 28, 28)
#28*28 = 784
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
y_train[9487]
"""

"""
2.2.4 輸出格式整理

我們可能會想, 我們想學的函數是這樣的型式:

其實這樣不太好! 為什麼呢? 比如說我們的輸入 x 是一張 0 的圖,
因為我們訓練的神經網路總會有點誤差, 所以可能會得到:

那這意思是有可能是 0, 也有可能是 1 嗎!!??
可是 0 和 1 根本不像啊。換句話說分類的問題這樣做其實不合理!

於是我們會做 "1-hot enconding", 也就是

0 -> [1, 0, 0, 0, 0, 0, 0, 0, 0]
1 -> [0, 1, 0, 0, 0, 0, 0, 0, 0]
5 -> [0, 0, 0, 0, 0, 1, 0, 0, 0]
8 -> [0, 0, 0, 0, 0, 0, 0, 0, 1]

等等。因為分類問題基本上都要做這件事, Keras 其實已幫我們準備好套件!
"""

# from keras.utils import np_utils old 改如下
from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

# 我們來看看剛剛是 9 的 87 號數據的答案。

print("編號87的訓練資料 的 目標  :", y_train[87])

# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 1.], dtype=float32)
#       0   1   2   3   4   5   6   7   8   9
# 和我們想的一樣! 至此我們可以打造我們的神經網路了。


"""
2-3 打造第一個神經網路
我們決定了我們的函數是
^f:R784→R10
這個樣子。而我們又說第一次要用標準神網路試試,
所以我們只需要再決定要幾個隱藏層、每層要幾個神經元, 用哪個激發函數就可以了。
2.3.1 決定神經網路架構、讀入相關套件
假如我們要這麼做:
    使用 3 個 hidden layers
    Hidden layer 1 用 6 個神經元
    Hidden layer 2 用 28 個神經元
    Hidden layer 3 用 2 個神經元
    Activation Function 唯一指名 relu
"""

# 於是從 Keras 把相關套件讀進來。
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD

"""
2.3.2 建構我們的神經網路
和以前做迴歸或機器學習一樣, 我們就打開個「函數學習機」。
標準一層一層傳遞的神經網路叫 Sequential, 於是我們打開一個空的神經網路。
"""

model = Sequential()  # 打開一個空的神經網路

"""
我們每次用 add 去加一層, 從第一個隱藏層開始。
而第一個隱藏層因為 Keras 當然猜不到輸入長什麼樣子, 所以我們要告訴它。
而全連結的神經網路其實都是一個向量輸入, 也就是要先「拉平」。
"""

# 第一層 用 6 個神經元
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(6, activation="relu"))

"""
第二層 hidden layer 因為前面輸出是 6, 現在輸入是 28, 就不用再說了!
這裡的 28 只告訴 Keras, 我們第二層是用 28 個神經元!
"""
# 第二層 用 28 個神經元
model.add(Dense(28, activation="relu"))

# 第三層 用 2 個神經元
model.add(Dense(2, activation="relu"))

# 輸出有 10 個數字, 所以輸出層的神經元是 10 個!
# 而如果我們的網路輸出是 (y1,y2,…,y10) 我們還希望 10∑i=1yi=1
# 這可能嗎, 結果是很容易, 就用 softmax 當激發函數就可以!!
model.add(Dense(10, activation="softmax"))

# 至此我們的第一個神經網路就建好了!

"""
2.3.3 組裝

和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。
你可以發現我們還需要做幾件事:
    1. 決定使用的 loss function, 一般是 mse
    2. 決定 optimizer, 我們用標準的 SGD
    3. 設 learning rate
為了一邊訓練一邊看到結果, 我們加設
metrics=['accuracy']
本行基本上和我們的神經網路功能沒有什麼關係。
"""

model.compile(loss="mse", optimizer=SGD(lr=0.087), metrics=["accuracy"])

"""
2-4 檢視我們的神經網路

我們可以檢視我們神經網路的架構, 可以確認一下是不是和我們想像的一樣。
2.4.1 看 model 的 summary
"""
print("檢視神經網路")
model.summary()  # 檢視神經網路

"""
很快算算參數數目和我們想像是否是一樣的!
784*6 + 6 = 4710
6*28 + 28 = 196
28*2 + 2 = 58
2*10 + 10 = 30

2-5 訓練你的第一個神經網路

恭喜! 我們完成了第一個神經網路。
現在要訓練的時候, 你會發現不是像以前沒頭沒腦把訓練資料送進去就好。
這裡我們還有兩件事要決定:
    1. 一次要訓練幾筆資料 (batch_size), 我們就 N = 100 筆調一次參數好了
    2. 這 6 萬筆資料一共要訓練幾次 (epochs), 我們訓練個 EPOCHS = 20 次試試

於是最精彩的就來了。你要有等待的心理準備...
"""

N = 600  # 每 N 筆調一次參數
EPOCHS = 1  # 訓練次數

print("資料共有 :", len(x_train), "筆, 每", N, "筆調一次參數, 共需調", len(x_train) / N, "次")
print("訓練次數 :", EPOCHS)

model.fit(x_train, y_train, batch_size=N, epochs=EPOCHS)  # 學習訓練.fit

# 2-6 試用我們的結果
# 我們 "predict" 放的是我們神經網路的學習結果。
# 這裡用 predict_classes 會讓我們 Keras 選 10 個輸出機率最大的那類。

# predict = model.predict_classes(x_test) 改成以下一行

predict = model.predict_step(x_test)
print("aaaaaaa")
print(predict)
predict = (model.predict(x_test) > 0.5).astype("int32")
print("bbbbbbb")
print(predict)

# array([7, 2, 1, ..., 7, 7, 0]) 有問題~~~~~~~~

# 寫個小程式, 秀出某測試資料的樣子, 還有我們可愛神經網路辨識的結果。


def test(num):
    plt.imshow(x_test[num], cmap="Greys")
    print("num =", num)
    print("神經網路判斷為 : ", predict[num])
    print()


predict_number = 87
test(predict_number)
plt.show()
print("神經網路判斷為 : ", predict[predict_number])

# 神經網路判斷為 : 3

# 到底測試資料總的狀況如何呢? 我們可以給我們神經網路「考一下試」。

score = model.evaluate(x_test, y_test)

print()
print("------------------------------------------------------------")
print("loss:", score[0])
print("正確率", score[1])

# loss: 0.06821700274944305
# 正確率 0.4345


# 2-7 訓練好的神經網路存起來!
# 如果對訓練成果滿意, 我們當然不想每次都再訓練一次! 我們可以把神經網路的架構和訓練好的參數都存起來, 以供日後使用!
# pip install h5py

model_json = model.to_json()
open("stupid_model.json", "w").write(model_json)
model.save_weights("stupid_model_weights.h5")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

""" 暫存
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train/255
x_test = x_test/255

#from keras.utils import np_utils old 改如下
from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD
model = Sequential()
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(20, activation='relu'))

"""


print("使用TensorFlow")


"""
標準 神經網路 做手寫辨識

Keras 可以用各種不同的深度學習套件當底層, 指定用 Tensorflow 以確保執行的一致性。

%env KERAS_BACKEND=tensorflow

"""

# 讀入 Tensorflow, 其實我們沒用到, 玩爽的而已。

import tensorflow as tf

# from tensorflow.keras.datasets import mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()

n = 9487

print(x_train[n])
print(y_train[n])

# 1

plt.imshow(x_train[n], cmap="Greys")


# 3. 資料整理

# 先看個範例, 因為 numpy 「廣播」的特性, 我們對 array 中所有數字要同除以一個數可瞬間完成!

np.array([3, 78, 95, 99]) / 100

# array([0.03, 0.78, 0.95, 0.99])

# 現在才是我們真的要做的, 這個動作叫 "normalization"。

x_train = x_train / 255

x_test = x_test / 255

x_train.shape

(60000, 28, 28)

# 28*28 = 784

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
y_train[9487]


# 打造神經網路

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

model = Sequential()
model.add(Dense(87, input_dim=784, activation="relu"))
model.add(Dense(87, activation="relu"))
model.add(Dense(10, activation="softmax"))

# 4. 組裝我們的神經網路

model.compile(loss="mse", optimizer=SGD(lr=0.087), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

# 784*87 + 87 = 68295

# 5. 訓練

# model.fit(x_train, y_train, batch_size = 100, epochs = 20)# 學習訓練.fit
# model.fit(x_train, y_train, batch_size = 1200, epochs = 1)# 學習訓練.fit
model.fit(x_train, y_train, batch_size=2400, epochs=1)  # 學習訓練.fit

# 6. 訓練成果

# result = model.predict_classes(x_test) #old

result = model.predict_step(x_test)

n = 9999

print("神經網路預測是:", result[n])

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")

# 神經網路預測是: 6


print("作業完成")
