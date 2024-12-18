"""
CNN


RNN


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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

EPOCHS = 1  # 遞迴次數, 訓練次數

import cv2
import tensorflow as tf
from keras.models import load_model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import LSTM


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
"""
在金融預測上的應用
神經網路
"""

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

# [2] 打造我們的神經網路函數學習機

print("建立神經網路1")
model = Sequential()
model.add(Dense(20, input_dim=5))
model.add(Activation("relu"))
model.add(Dense(20))
model.add(Activation("relu"))
model.add(Dense(1))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路


""" TBD

model.fit(x_train, yb_train, batch_size=100, epochs=20)  # 學習訓練.fit


#預測

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

YP_NN = yb_test[(y_pred==1).ravel()]

len(YP_NN)

458

len(YP_NN[YP_NN == 1])

246

246/458

0.537117903930131

結果真是慘慘慘, 怎麼會這樣呢?

"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


""" 訓練久
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from sklearn import preprocessing

df = pd.read_csv("data/iris.csv")

label_encoder = preprocessing.LabelEncoder()
df["target"] = label_encoder.fit_transform(df["target"])

dataset = df.values
np.random.shuffle(dataset)
X = dataset[:, 0:4].astype(float)
Y = to_categorical(dataset[:, 4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)  # STD特徵縮放

X_train, Y_train = X[:120], Y[:120]
X_test, Y_test = X[120:], Y[120:]

print("建立神經網路2")
model = Sequential()
model.add(Dense(6, input_shape=(4,), activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(3, activation="softmax"))

print("檢視神經網路")
model.summary()  # 檢視神經網路

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(X_train, Y_train, epochs=100, batch_size=5)

loss, accuracy = model.evaluate(X_test, Y_test)
print("Accuracy = {:.2f}".format(accuracy))

# y_pred = model.predict_classes(X_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(X_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print(y_pred)

Y_target = dataset[:, 4][120:].astype(int)
print(Y_target)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
# CNN
# Final 卷積層的實作

import urllib.request

# 定義卷積層運算的類別


class Conv:
    # 為了方便解釋, W固定為3x3, 並且不考慮stride和padding
    def __init__(self, W):
        self.W = W

    def f_prop(self, X):
        out = np.zeros((X.shape[0] - 2, X.shape[1] - 2))
        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                x = X[i : i + 3, j : j + 3]
                # 元素執行內積加總
                out[i, j] = np.dot(self.W.flatten(), x.flatten())
        return out


local_filename, headers = urllib.request.urlretrieve(
    "https://aidemyexcontentsdata.blob.core.windows.net/data/5100_cnn/circle.npy"
)

X = np.load(local_filename)

plt.imshow(X)

plt.title("The original image")

plt.show()

# 參考過濾器W2和W3, 來設置程式碼中的過濾器W1, 使其具有檢測垂直線條的能力

W1 = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
W2 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
W3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
W4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

plt.subplot(141)
plt.imshow(W1)
plt.subplot(142)
plt.imshow(W2)
plt.subplot(143)
plt.imshow(W3)
plt.subplot(144)
plt.imshow(W4)
plt.suptitle("kernel")
plt.show()

# 卷積運算
conv1 = Conv(W1)
C1 = conv1.f_prop(X)
conv2 = Conv(W2)
C2 = conv2.f_prop(X)
conv3 = Conv(W3)
C3 = conv3.f_prop(X)
conv4 = Conv(W4)
C4 = conv4.f_prop(X)

plt.subplot(141)
plt.imshow(C1)
plt.subplot(142)
plt.imshow(C2)
plt.subplot(143)
plt.imshow(C3)
plt.subplot(144)
plt.imshow(C4)

plt.suptitle("Convolution result")

plt.show()

# Final 池化層的實作

import urllib.request

# 定義卷積層運算的類別


class Conv:
    # 為了方便解釋, W固定為3x3, 並且不考慮stride和padding
    def __init__(self, W):
        self.W = W

    def f_prop(self, X):
        out = np.zeros((X.shape[0] - 2, X.shape[1] - 2))
        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                x = X[i : i + 3, j : j + 3]
                out[i, j] = np.dot(self.W.flatten(), x.flatten())
        return out


# 定義池化運算的類別


class Pool:
    # 為了方便解釋, 不考慮strides和padding

    def __init__(self, l):
        self.l = l

    def f_prop(self, X):
        l = self.l

        out = np.zeros((X.shape[0] // self.l, X.shape[1] // self.l))

        for i in range(out.shape[0]):
            for j in range(out.shape[1]):
                # 從檢視窗口所劃分出的子區域當中，用np.max()取各區域的最大值出來

                out[i, j] = np.max(X[i * l : (i + 1) * l, j * l : (j + 1) * l])

        return out


local_filename, headers = urllib.request.urlretrieve(
    "https://aidemyexcontentsdata.blob.core.windows.net/data/5100_cnn/circle.npy"
)

X = np.load(local_filename)

plt.imshow(X)

plt.title("The original image")

plt.show()

# 過濾器
W1 = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])
W2 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
W3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
W4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

# 卷積運算
conv1 = Conv(W1)
C1 = conv1.f_prop(X)
conv2 = Conv(W2)
C2 = conv2.f_prop(X)
conv3 = Conv(W3)
C3 = conv3.f_prop(X)
conv4 = Conv(W4)
C4 = conv4.f_prop(X)

plt.subplot(141)
plt.imshow(C1)
plt.subplot(142)
plt.imshow(C2)
plt.subplot(143)
plt.imshow(C3)
plt.subplot(144)
plt.imshow(C4)

plt.suptitle("Convolution result")

plt.show()

# 最大池化運算

pool = Pool(2)

P1 = pool.f_prop(C1)
P2 = pool.f_prop(C2)
P3 = pool.f_prop(C3)
P4 = pool.f_prop(C4)

plt.subplot(141)
plt.imshow(P1)

plt.subplot(142)
plt.imshow(P2)

plt.subplot(143)
plt.imshow(P3)

plt.subplot(144)
plt.imshow(P4)

plt.suptitle("Pooling result")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用 tf.Keras 建構 CNN 模型

from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.utils import to_categorical

print("建立神經網路13")
model = Sequential()

# 卷積層與池化層--------------------------------------------------------------
model.add(
    Conv2D(
        input_shape=(28, 28, 1),
        filters=32,
        kernel_size=(2, 2),
        strides=(1, 1),
        padding="same",
    )
)

model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=(1, 1), padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(1, 1)))

# --------------------------------------------------------------

model.add(Flatten())
model.add(Dense(256, activation="sigmoid"))
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

print("檢視神經網路")
model.summary()  # 檢視神經網路

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
我們終於要介紹三大神經網路的最後一個, 也就是 RNN。
RNN 有不少的變型, 例如 LSTM 和 GRU 等等, 不過我們都通稱叫 RNN。
RNN 是一種「有記憶」的神經網路, 非常適合時間序列啦, 或是不定長度的輸入資料。

我們來看看怎麼樣用 RNN 做電影評論的「情意分析」,
也就是知道一則評論究竟是「正評」還是「負評」。
"""

print("------------------------------------------------------------")  # 60個

from tensorflow.keras.datasets import imdb

""" imdb 資料在
https://storage.googleapis.com/tensorflow/tf-keras-datasets/imdb.npz
"""

# 讀取 本地檔案
imdb_npz_filename = "C:/_git/vcs/_big_files/imdb.npz"

(x_train, y_train), (x_test, y_test) = imdb.load_data(
    path=imdb_npz_filename,
    num_words=10,
    skip_top=0,
    maxlen=None,
    seed=9487,
    start_char=0,
    # oov_char="OOV",
    index_from=0,
)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)

# from keras.datasets import imdb
# (x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=10000)
# 2. 讀入數據
# 讀入 IMDB 電影數據庫影評的部份。

# 要注意這裡我們限制只選「最常用」1 萬字, 也就是超過這範圍的就當不存在。
# 這是文字分析常會做的事。


print("訓練總筆數:", len(x_train))
print("測試總筆數:", len(x_test))

# 25000
# 25000

print(len(x_train[0]))

# 218

print(len(x_train[1]))

# 189

print(y_train[0])

# 1

print(y_train[1])

# 0

# 輸入資料部份
# 我們來看一下輸入部份長什麼樣子?

for n in x_train[24999]:
    print(n, end=" ")
# 注意這其實是一個 list 而不是 array, 原因是每筆資料 (每段影評) 長度自然是不一樣的! 我們檢查一下前 10 筆的長度就可以知道。

print(len(x_train[24999]))

# 153

print(len(x_train[9982]))

# 156

print(len(x_train[9487]))

# 104
# 最後要說明的是, 在每筆輸入資料的數字都代表英文的一個單字。編號方式是在我們資料庫裡所有文字的排序: 也就是出現頻率越高, 代表的數字就越小。


# 3. 資料處理
x_train = sequence.pad_sequences(x_train, maxlen=100)
x_test = sequence.pad_sequences(x_test, maxlen=100)

# 4. step 01: 打造一個函數學習機

model = Sequential()

model.add(Embedding(10000, 128))
model.add(LSTM(128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation="sigmoid"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("檢視神經網路1")
model.summary()  # 檢視神經網路

# (128+128+1)*4*128 = 131584

""" 久
# 學習訓練.fit
model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))

model_json = model.to_json()
open("imdb_model_architecture.json", "w").write(model_json)
model.save_weights("imdb_model_weights.h5")
"""

print("------------------------------------------------------------")  # 60個

# new~~~~~~


# 輸出資料部份
# 輸出方面應該很容易想像, 我們來看看前 10 筆。
# 結果自然就是 0 (負評) 或 1 (正評)。

print(y_train[:10])

# array([1, 0, 0, 1, 0, 0, 1, 0, 1, 0])

print(y_train[24999])

# 0

# 送入神經網路的輸入處理
# 雖然 RNN 是可以處理不同長度的輸入, 在寫程式時我們還是要
# 1.設輸入文字長度的上限
# 2.把每段文字都弄成一樣長, 太短的後面補上 0

from keras.preprocessing import sequence

x_train = sequence.pad_sequences(x_train, maxlen=150)
x_test = sequence.pad_sequences(x_test, maxlen=150)

print(x_train.shape)

# (25000, 150)

# 至此我們可以來寫我們的第一個 RNN 了!

# 09-03 打造你的 RNN
"""
這裡我們選用 LSTM, 基本上用哪種 RNN 寫法都是差不多的!
決定神經網路架構

    先將 10000 維的文字壓到 N 維
    然後用 K 個 LSTM 神經元做隱藏層
    最後一個 output, 直接用 sigmoid 送出

建構我們的神經網路

文字我們用 1-hot 表示是很標準的方式, 不過要注意的是, 因為我們指定要 1 萬個字, 所以每個字是用 1 萬維的向量表示! 這一來很浪費記憶空間, 二來字和字間基本上是沒有關係的。我們可以用某種「合理」的方式, 把字壓到比較小的維度, 這些向量又代表某些意思 (比如說兩個字代表的向量角度小表相關程度大) 等等。

這聽來很複雜的事叫 "word embedding", 而事實上 Keras 會幫我們做。我們只需告訴 Keras 原來最大的數字是多少 (10000), 還有我們打算壓到幾維 (N)。
"""

N = 3  # 文字要壓到 N 維
K = 12  # LSTM 有 K 個神經元

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Embedding
from keras.layers import LSTM

model = Sequential()

model.add(Embedding(10000, N))

# LSTM 層, 我們做 K 個 LSTM Cells。

model.add(LSTM(K))

# 單純透過 sigmoid 輸出。

model.add(Dense(1, activation="sigmoid"))

# 優化器(optimizer) : Adam
# 損失函數(loss) : binary_crossentropy
# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

print("檢視神經網路2")
model.summary()  # 檢視神經網路

# (4*7 + 4)*K = 128

# 09-04 訓練

"""
我們用的 embedding 中, 會被 batch_size 影響輸入。輸入的 shape 會是

(batch_size, 每筆上限)

也就是 (32,100) 輸出是 (32,100,128), 其中 128 是我們決定要壓成幾維的向量。
"""

""" 久
# 學習訓練.fit
model.fit(x_train, y_train, batch_size=32, epochs=5)

# 09-05 檢視結果
# 分數
# 我們照例來看看測試資料的分數。

score = model.evaluate(x_test, y_test)
print(f"測試資料的 loss = {score[0]}")
print(f"測試資正確率 = {score[1]}")

# 測試資料的 loss = 0.36388471513748166
# 測試資正確率 = 0.852400004863739

# 儲存結果
# 這裡有 8 成我們可以正確分辨, 看來還不差, 照例我們把結果存檔。

model_json = model.to_json()

open("imdb_model_arch.json", "w").write(model_json)

model.save_weights("imdb_model_weights.h5")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
ddprice = pd.DataFrame(df["收盤價"])

print(df.head())

df = df.drop(["日期"], axis=1)

data_all = np.array(df).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length - 1):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = Sequential()

model.add(LSTM(input_shape=(10, 1), units=256, unroll=False))  # LSTM層
model.add(Dense(units=1))  # 輸出層：1 個神經元

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])

model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1, verbose=2)

predict = model.predict(test_x)
predict = np.reshape(predict, (predict.size,))  # 轉換為1維矩陣
predict = scaler.inverse_transform([[i] for i in predict_y])  # 還原
test_y = scaler.inverse_transform(test_y)  # 還原

plt.plot(predict, "b:")  # 預測
plt.plot(test_y, "r-")  # 收盤價
plt.legend(["predict", "realdata"])

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
dfprice = pd.DataFrame(df["收盤價"])

data_all = np.array(dfprice).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為Label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = Sequential()

model.add(LSTM(input_shape=(sequence_length, 1), units=256, unroll=False))  # LSTM層
model.add(Dense(units=1))  # 輸出層：1個神經元

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="mse", metrics=["accuracy"])

model.fit(train_x, train_y, batch_size=100, epochs=300, validation_split=0.1, verbose=2)

print("將 模型存檔 存成 h5")
model.save("tmp_stock_rnn_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.preprocessing import MinMaxScaler

sequence_length = 10  # 特徵資料個數
split = 0.95  # 訓練資料比率

pd.options.mode.chained_assignment = None  # 取消顯示pandas資料重設警告
filename = "twstock_all.csv"
df = pd.read_csv(filename, encoding="big5")  # 以pandas讀取檔案
dfprice = pd.DataFrame(df["收盤價"])

data_all = np.array(dfprice).astype(float)  # 轉為浮點型別矩陣
scaler = MinMaxScaler()
data_all = scaler.fit_transform(data_all)  # 將數據縮放為0~1之間
data = []
for i in range(len(data_all) - sequence_length):
    data.append(data_all[i : i + sequence_length + 1])  # 每筆data資料有11欄
reshaped_data = np.array(data).astype("float64")
x = reshaped_data[:, :-1]  # 第1至第10個欄位為特徵
y = reshaped_data[:, -1]  # 第11個欄位為label
split_boundary = int(reshaped_data.shape[0] * split)  # 分離資料
train_x = x[:split_boundary]  # 訓練特徵資料
test_x = x[split_boundary:]  # test特徵資料
train_y = y[:split_boundary]  # 訓練label資料
test_y = y[split_boundary:]  # test的label資料

model = load_model("tmp_stock_rnn_model.h5")

predict = model.predict(test_x)
predict = np.reshape(predict, (predict.size,))  # 轉換為1維矩陣
predict = scaler.inverse_transform([[i] for i in predict])  # 還原
test_y = scaler.inverse_transform(test_y)  # 還原

plt.plot(predict, "b:")  # 預測
plt.plot(test_y, "r-")  # 收盤價
plt.legend(["predict", "realdata"])

show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("CNN 預測")

import glob


def show_images_predictions(images, y_pred, num=10):
    plt.gcf().set_size_inches(8, 8)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[i], cmap="binary")  # 顯示黑白圖片
        ax.set_title("p=" + str(y_pred[i]))
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()


files = glob.glob("imagedata\*.jpg")  # 建立測試資料
print('找到 :', len(files), '個檔案')

test_feature = []
for file in files:
    #print("檔案 :", file)
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    test_feature.append(img)

print('找到 :', len(test_feature), '張圖')

test_feature = np.array(test_feature)  # 串列轉為矩陣
test_feature_vector = test_feature.reshape(len(test_feature), 28, 28, 1).astype(
    "float32"
)
test_feature_normalize = test_feature_vector / 255

model = load_model("Mnist_cnn_model.h5")

predict_x = model.predict(test_feature_normalize)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x
print('預測結果 :', y_pred)

show_images_predictions(test_feature, y_pred, len(test_feature))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.models import model_from_json

#在 28X28的方塊內 用滑鼠寫數字

print("用滑鼠寫數字")
print("按S, 用 CNN 來辨識")
print("按C, 清除")
print("按ESC, 離開")

# 讀取模型架構
json_file = open("data/model.json", "r")

loaded_model_json = json_file.read()
json_file.close()

model = model_from_json(loaded_model_json)

# 讀取模型權重
model.load_weights("data/model.h5")

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)


def CNN():
    W = 28
    H = 28

    img2 = cv2.resize(img, (W, H))
    
    b = img2.astype(dtype=np.float32)
    
    # 將原始資料轉為正確的影像排列方式
    x_test = b.reshape(1, 28, 28, 1)
    
    # 標準化輸入資料
    x_test /= 255
    
    # 輸出結果
    # y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
    predict_x = model.predict(x_test)
    classes_x = np.argmax(predict_x, axis=1)
    y_pred = classes_x
    print("predict_classes:", y_pred)

#用滑鼠在cv2上寫字部分 已做成範例
W, H = 280, 280
drawing = False
img = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)
cv2.namedWindow("image")


def draw_circle(event, x, y, flags, param):
    global img, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img, (x, y), 1, (255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img, (x, y), 1, (255), -1)


cv2.setMouseCallback("image", draw_circle)

while True:
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("s"):
        print("Save")
        cv2.imwrite("tmp_1.jpg", img)
        CNN()
    elif k == ord("c"):
        print("Clear")
        img = np.full(shape=(H, W, 1), fill_value=0, dtype=np.uint8)
    elif k == 27:
        print("ESC")
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個
