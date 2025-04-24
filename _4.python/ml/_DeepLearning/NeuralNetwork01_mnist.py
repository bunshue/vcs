"""
CNN 手寫辨識
Yann LeCun 被譽為 Deep Learning 的三巨頭之一。
他的 CNN (Convolutional Neural Networks) 是讓 Neural Network 重新受到重視的主因之一。

------------------------------

# 將minst資料集放在 系統 位置

下載minst資料集檔案 :
https://s3.amazonaws.com/img-datasets/mnist.npz
or
https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz

放在 :
C:/Users/xxxxxx/.keras/datasets/mnist.npz

------------------------------

深度神經網路 Deep Neural Networks (DNN)
1.捲積神經網路 Convolutional Neural Network (CNN)
2.循環神經網路 Recurrent Neural Network (RNN)

CNN包括了3個小層次

卷積層(Convolutional layer) 處理多數的計算、檢查圖像特徵。

池化層(Pooling layer)	圖像掃描及過濾，與卷積層不同的是降低了許多參數，提高了效率降低了複雜性。

全連接層(Fully connected layer) 根據前幾層處理程序來提取特徵進行圖像分類的地方，層層相扣每一層都有相連節點。

神經網路模型(CNN)

隱藏層的數量、隱藏層設計多少神經元

# 設定輸出層 softmax
activation="relu"

model.add(Flatten(input_shape=(28, 28)))  # 向量輸入拉平

幾個隱藏層、每層要幾個神經元, 用哪個激活函數

假如
    使用 3 個 hidden layers
    Hidden layer 1 用 6 個神經元
    Hidden layer 2 用 28 個神經元
    Hidden layer 3 用 2 個神經元
    激活函數 Activation Function 唯一指名 relu

# 組裝神經網路
1. 決定使用的 loss function, 一般是 mse
2. 決定 optimizer(優化器), 我們用標準的 SGD
3. 設 learning rate

為了一邊訓練一邊看到結果, 我們加設
metrics=["accuracy"]

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

分析顯示 mnist 資料集

MNIST手寫數字辨識資料集
MNIST資料集
60,000筆 訓練資料 train data
10,000筆 測試資料 test data

# 訓練資料 : (60000, 28, 28) #共60000張圖片資料，圖片像素28*28
# 測試資料 : (10000, 28, 28) #共10000張圖片資料，圖片像素28*28

MNIST資料集是由60,000筆訓練資料、10,000筆測試資料所組成。
MNIST資料集裡的每一筆資料皆由images(數字的影像)與labels
(該圖片的真實數字，其實就是答案)所組成。

由於MNIST的資料大小適中，而且皆為單色影像(黑字白底)，
十分適合做為初學者第一個建立模型、訓練、與預測的資料集。

# mnist資料集筆數
# 60,000筆的train data(訓練資料)與10,000筆的test data(測試資料)
# 共60000張圖片資料，圖片像素28*28

# 每一筆mnist資料皆是由images(數字影像)與labels(數字真實值)所組成，
# images的部分為單色、28*28像素的影像檔案(圖片)，label則是該張影像檔案的真實數值(解答)

標準 神經網路 做手寫辨識

讀入 MNIST 數據庫

MNIST 是有一堆 0-9 的手寫數字圖庫。有 6 萬筆訓練資料, 1 萬筆測試資料。
它是 "Modified" 版的 NIST 數據庫, 原來的版本有更多資料。
這個 Modified 的版本是由 LeCun, Cortes, 及 Burges 等人做的。可以參考這個數據庫的原始網頁。

MNIST 可以說是 Deep Learning 最有名的範例, 它被 Deep Learning 大師 Hinton 稱為「機器學習的果蠅」。
2.2.1 由 Keras 讀入 MNIST

Keras 很貼心的幫我們準備好 MNIST 數據庫, 我們可以這樣讀進來 (第一次要花點時間)。
http://yann.lecun.com/exdb/mnist/

Dense        全連接層
Conv2D       二維卷積層 Convolution Layer, Conv2D
MaxPooling2D 最大池化層
Dropout      隨機失活層
"""
print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import datetime
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


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# from keras.datasets import mnist  # same

# 用tensorflow讀入 MNSIT 數據集
from tensorflow.keras.datasets import mnist  # same

from tensorflow.keras.models import Sequential

"""
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Activation # 激活函數
from tensorflow.keras.layers import Conv2D  # 二維卷積層 Convolution Layer
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import BatchNormalization # 批次正規化
from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.layers.core import Activation # 激活函數
"""
from tensorflow.keras import optimizers
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical  # One-Hot Encoding

# from tensorflow.python.keras.utils import np_utils
# np_utils.to_categorical  # 用來後續將 label 標籤轉為 one-hot-encoding

from keras import utils

# from tensorflow.keras.optimizers import SGD  # 優化器
from keras.optimizers import SGD  # 優化器
from keras.optimizers import Adam  # 優化器
from keras.optimizers import RMSprop
from keras.models import load_model

# 共用的, 從 Keras 把相關套件讀進來。
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation  # 激活函數
from keras.layers import Flatten
from keras.layers import Conv2D  # 二維卷積層 Convolution Layer
from keras.layers import MaxPool2D  # 最大值池化
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import BatchNormalization  # 批次正規化

print("------------------------------------------------------------")  # 60個

# 共同
BATCH_SIZE = 300  # 每 BATCH_SIZE 筆調一次參數
EPOCHS = 1  # 遞迴次數, 訓練次數

INPUT_DIM = 784  # 輸入層: 28*28 = 784
VALIDATION_SPLIT = 0.2  # 驗證資料佔比

mnist_npz_filename = "D:/_git/vcs/_big_files/mnist.npz"
time_st = time.time()


def load_mnist_data():
    # 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
    RATIO = 20  # debug, 一律 1/10
    print("資料量縮小 ", RATIO, "倍")
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train[: int(len(x_train) // RATIO)]
    y_train = y_train[: int(len(y_train) // RATIO)]
    x_test = x_test[: int(len(x_test) // RATIO)]
    y_test = y_test[: int(len(y_test) // RATIO)]
    print("訓練資料x長度 :", len(x_train))
    print("訓練資料y長度 :", len(y_train))
    print("測試資料x長度 :", len(x_test))
    print("測試資料y長度 :", len(y_test))
    return (x_train, y_train), (x_test, y_test)


def transform_data(x_train, y_train, x_test, y_test):
    # x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)
    x_train = x_train.reshape(len(x_train), 784)
    x_test = x_test.reshape(len(x_test), 784)

    # x訓練/測試資料 N個 轉成 28*28個 float32 數字
    # x_train = x_train.astype("float32")
    # x_test = x_test.astype("float32")

    # 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
    # x_train = x_train / 255
    # x_test = x_test / 255

    # One-Hot Encoding, 將數字轉為 One-hot 向量
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    return x_train, y_train, x_test, y_test


def transform_data4d(x_train, y_train, x_test, y_test):
    # 將圖片轉換成 4D 張量
    x_train = x_train.reshape(len(x_train), 28, 28, 1).astype("float32")
    x_test = x_test.reshape(len(x_test), 28, 28, 1).astype("float32")

    # 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
    x_train = x_train / 255
    x_test = x_test / 255

    # One-Hot Encoding, 將數字轉為 One-hot 向量
    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)
    return x_train, y_train, x_test, y_test


def check_model_fit_history1(history):
    # 檢查訓練 資料
    print("history")
    print(history)
    acc = history.history["accuracy"]
    print("訓練準確度 :", acc)
    plt.plot(acc, label="accuracy")
    plt.xlabel("epoch")
    plt.ylabel("accuracy")
    plt.legend()
    show()


def check_model_fit_history2(history):
    # 檢查訓練和驗證  資料
    # 評估訓練/驗證 的 損失和準確度, 有 validation_split 才可做
    print("history")
    print(history)

    loss = history.history["loss"]
    print("訓練損失 :", loss)

    val_loss = history.history["val_loss"]
    print("驗證損失 :", val_loss)

    acc = history.history["accuracy"]
    print("訓練準確度 :", acc)

    val_acc = history.history["val_accuracy"]
    print("驗證準確度 :", val_acc)

    epochs = range(1, len(loss) + 1)
    print("epochs1 = ", epochs)

    plt.plot(epochs, loss, "bo-", label="Training Loss")
    plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
    plt.title("Training and Validation Loss")
    plt.xlabel("Epochs")
    plt.ylabel("Loss")
    plt.legend()
    show()

    epochs = range(1, len(acc) + 1)

    print("epochs2 = ", epochs)

    plt.plot(epochs, acc, "bo-", label="Training Acc")
    plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy")
    plt.legend()
    show()


# 學習訓練.fit, 無驗證
def do_model_fit1(x_train, y_train):
    # 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
    history = model.fit(
        x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=0
    )
    # check_model_fit_history1(history)


# 學習訓練.fit, 有驗證 + validation_split split
# 模型訓練，epochs：執行週期，validation_split：驗證資料佔比
def do_model_fit2(x_train, y_train, validation_split):
    # 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
    history = model.fit(
        x_train,
        y_train,
        validation_split=validation_split,
        batch_size=BATCH_SIZE,
        epochs=EPOCHS,
        verbose=2,
    )
    # check_model_fit_history2(history)


def do_prediction(x_test):
    # y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
    predict_x = model.predict(x_test)
    classes_x = np.argmax(predict_x, axis=1)
    y_pred = classes_x
    return y_pred


def show_predict_result(x_test, y_pred, n):
    return
    print("第", n, "筆資料, 神經網路判斷為:", y_pred[n])
    plt.imshow(x_test[n], cmap="Greys")
    show()


def show_predict_result_1d(x_test, y_pred, n):
    return
    print("第", n, "筆資料, 神經網路判斷為:", y_pred[n])
    plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")
    show()


def evaluate_model(x_test, y_test):
    # 模型評估.evaluate, 評估準確率
    # loss, accuracy = model.evaluate(x_test, y_test, batch_size=128, verbose=0) 看起來一樣
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print("損失率 : {:.2f}".format(loss))
    print("正確率 : {:.2f}".format(accuracy))


# 全部拿來測試
def do_the_same1(x_train, y_train, x_test, y_test):
    # 做一樣的事
    # 學習訓練.fit
    do_model_fit1(x_train, y_train)
    # 預測
    y_pred = do_prediction(x_test)
    n = 123
    show_predict_result(x_test, y_pred, n)
    # 模型評估
    evaluate_model(x_test, y_test)


def do_the_same2(x_train, y_train, x_test, y_test):
    # 做一樣的事
    # 學習訓練.fit
    do_model_fit1(x_train, y_train)

    # 預測
    y_pred = do_prediction(x_test)
    n = 123
    show_predict_result_1d(x_test, y_pred, n)


# 分割測試資料以驗證
def do_the_same_with_validation(x_train, y_train, x_test, y_test, validation_split):
    # 做一樣的事
    # 學習訓練.fit
    do_model_fit2(x_train, y_train, validation_split=0.2)

    # 預測
    y_pred = do_prediction(x_test)
    n = 123
    show_predict_result_1d(x_test, y_pred, n)

    # 模型評估
    evaluate_model(x_test, y_test)


def do_cnn_test():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)
    # 全部拿來測試
    do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

    """
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)
    # 分割測試資料以驗證
    do_the_same_with_validation(x_train, y_train, x_test, y_test, VALIDATION_SPLIT)
    """


def do_cnn_test4d():
    (x_train, y_train), (x_test, y_test) = load_mnist_data()
    x_train, y_train, x_test, y_test = transform_data4d(
        x_train, y_train, x_test, y_test
    )
    # 全部拿來測試
    do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事


def print_y_data(y):
    N = 30  # 最多的個數
    R = 10  # 每R個換行
    length = len(y)
    if length > N:
        length = N
    if length <= 30:
        R = 31
    for i in range(length):
        print(y[i], end="")
        if i % R == (R - 1):
            print()
        else:
            print(end=" ")


def get_elapsed_time():
    global time_st
    current_time = datetime.datetime.now().strftime("%Y/%m/%d %a %H:%M:%S")
    print("現在時間 :", current_time)
    timeElapsed = time.time() - time_st
    timeElapsed = round(timeElapsed, 4)
    print("所花時間 : {} 秒".format(timeElapsed))
    time_st = time.time()


'''
print("------------------------------------------------------------")  # 60個
print("準備工作 ST")
print("------------------------------------------------------------")  # 60個

print("各種讀取資料集的方法")

# 用tensorflow讀入 MNSIT 數據集
from tensorflow.keras.datasets import mnist

# 標準 1 遠端檔案
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
# 標準 2 本地檔案
mnist_npz_filename = "D:/_git/vcs/_big_files/mnist.npz"

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("畫出 訓練資料的前100筆... 久")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

plt.figure(figsize=(7, 9))
N = 100
for i in range(N):
    plt.subplot(10, 10, i + 1)
    # plt.imshow(x_train[i], cmap="greys")  # gray
    # plt.imshow(x_train[i], cmap="binary") # cmam="binary"表示以黑白色顯示
    plt.imshow(x_train[i], cmap=plt.cm.gray)
    plt.title(str(y_train[i]))
    plt.axis("off")
plt.suptitle("訓練資料的前100筆")
# plt.subplots_adjust(hspace=0.5) 未知
show()

# plt.imshow(x_train[n], cmap=plt.get_cmap("gray_r"))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("MNIST手寫數字辨識資料集 資料內容")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 訓練
print("訓練資料 X(image)長度 :", len(x_train))
print("訓練資料 X(image)大小 :", x_train.shape)
print("訓練資料 Y(label)長度 :", len(y_train))
print("訓練資料 Y(label)大小 :", y_train.shape)

# 測試
print("測試資料 X(image)長度 :", len(x_test))
print("測試資料 X(image)大小 :", x_test.shape)
print("測試資料 Y(label)長度 :", len(y_test))
print("測試資料 Y(label)大小 :", y_test.shape)

print("mnist 資料集 內容")
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

# 有完整解說的
# https://waternotetw.blogspot.com/2018/03/keras-mnist.html

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 將image以reshape()轉換
# 先將原本28*28的2維數字影像，以reshape()轉換成1維向量，再以astype()轉換為float，共784個float數字
# 二維影像 (28, 28) 轉成 一維向量 (784,) 再轉成 784個 float32 數字
# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)
X_train = x_train.reshape(len(x_train), 28 * 28).astype("float32")
X_test = x_test.reshape(len(x_test), 28 * 28).astype("float32")

print("將二維 28X28 的影像 轉為 一維 784 資料 reshape")
print("轉換後的 訓練資料 大小 x_train:", X_train.shape)
print("轉換後的 測試資料 大小 x_test:", X_test.shape)

# 每個數字由0至255組成，代表圖形每一個點的灰階深淺
print("看 第0筆 二維影像內容")
print(x_train[0])
print("看 第0筆 一維影像內容")
print(X_train[0])

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
X_train_normalization = X_train / 255
X_test_normalization = X_test / 255

print("看標準化後 第0筆 一維影像內容")
print(X_train_normalization[0])

# 查看訓練資料label標籤欄位的前五筆訓練資料
print("看前5筆 訓練資料")
print(y_train[:5])

print("印出一些 訓練目標")
print_y_data(y_train)

print("印出一些 測試目標")
print_y_data(y_test)

print("------------------------------------------------------------")  # 60個

print("測試 One-Hot Encoding, 將數字轉為 One-hot 向量")
print("測試 One-Hot Encoding, 預設為10位元")
data1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
data2 = to_categorical(data1)

print("原資料 :")
print(data1)
print("轉換後 :")
print(data2)

print("測試 One-Hot Encoding, 設定20位元")
classes = 20
data1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
data3 = to_categorical(data1, classes)
print("原資料 :")
print(data1)
print("轉換後 :")
print(data3)

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = x_train.reshape(len(x_train), 784)
x_test = x_test.reshape(len(x_test), 784)

# 標準化輸入資料
print("x_train before div 255:", x_train[0][180:195])
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255
print("x_train before div 255 ", x_train[0][180:195])

print("y_train shape:", y_train.shape)
print(y_train[:10])

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print("y_train to_categorical shape=", y_train.shape)
print(y_train[:10])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 顯示資料內容
def printMatrixE(a):
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0, rows):
        str1 = ""
        for j in range(0, cols):
            str1 = str1 + ("%3.0f " % a[i, j])
        print(str1)
    print("")


print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

print("印出 第0筆 內容")
printMatrixE(x_train[0])
print("印出 第0筆 目標")
print(y_train[0])

print("------------------------------------------------------------")  # 60個
print("準備工作 SP")
print("------------------------------------------------------------")  # 60個
'''
get_elapsed_time()

# david : 簡單又正確率高, 以此為準
"""
#有完整解說的
參考 https://ithelp.ithome.com.tw/m/articles/10191404
有說明
"""

print("建立神經網路01 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(
    Dense(
        units=256, input_dim=INPUT_DIM, kernel_initializer="normal", activation="relu"
    )
)

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print("檢視模型架構")
model.summary()  # 檢視模型架構

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test()

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路02 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 設定隱藏層HL第2層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路03")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 設定隱藏層HL第2層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(rate=0.5))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路04")
print("建立 3 層神經網路 100 100 100")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 100 個神經元
model.add(Dense(100, input_dim=INPUT_DIM, activation="relu"))

# 設定隱藏層HL第2層, 用 100 個神經元
model.add(Dense(100, activation="relu"))

# 設定隱藏層HL第3層, 用 100 個神經元
model.add(Dense(100, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.087)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

(x_train, y_train), (x_test, y_test) = load_mnist_data()
x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)
do_the_same2(x_train, y_train, x_test, y_test)  # 做一樣的事

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路05 正確率高 僅正規化 沒有one-hot")

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Flatten(input_shape=(28, 28)))  # 向量輸入拉平

# 設定隱藏層HL第2層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(rate=0.2))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# NG 不知道為什麼
# (x_train, y_train), (x_test, y_test) = load_mnist_data()
# x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 特徵縮放
# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train, x_test = x_train / 255, x_test / 255

# 方法一 全部拿來測試
do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

"""
# 方法二 分割測試資料以驗證
do_the_same_with_validation(x_train, y_train, x_test, y_test, VALIDATION_SPLIT)
"""
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路06 Conv2D 正確率高 4D 張量")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    Conv2D(
        16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 再 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(32, kernel_size=(5, 5), padding="same", activation="relu"))

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定隨機失活層(Dropout層)
model.add(Dropout(0.5))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(0.5))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 將圖片轉換成 4D 張量
x_train = x_train.reshape(len(x_train), 28, 28, 1).astype("float32")
x_test = x_test.reshape(len(x_test), 28, 28, 1).astype("float32")

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train = x_train / 255
x_test = x_test / 255

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 全部拿來測試
do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

# ---------------------

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 選一個測試的數字圖片
i = 7
n = 7  # 123
digit = x_test[n].reshape(28, 28)
# print(digit)

# 將圖片轉換成 4D 張量
x_test_digit = x_test[n].reshape(1, 28, 28, 1).astype("float32")

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test_digit = x_test_digit / 255

plt.subplot(121)
plt.title("真實目標 :" + str(y_test[n]))
plt.imshow(digit, cmap="gray")
plt.axis("off")

plt.subplot(122)
probs = model.predict(x_test_digit, batch_size=1)[0]
print("預測結果的機率 :", probs)
plt.title("預測結果的機率\n每個數字的機率")
plt.bar(np.arange(10), probs.reshape(10), align="center")
plt.xticks(np.arange(10), np.arange(10).astype(str))

show()

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路07 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 隱藏層256
model.add(
    Dense(
        units=256,
        input_dim=INPUT_DIM,
        kernel_initializer="normal",
        activation="relu",
    )
)

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# 後續一樣
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路08 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 隱藏層256
model.add(
    Dense(
        units=256,
        input_dim=INPUT_DIM,
        kernel_initializer="normal",
        activation="relu",
    )
)

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# Channel
# CNN 要注意一張圖有多少個 channel, 開始我們因為只有灰階, 所以只有一個 channel。
# 因此我們要轉一下我們的資料格式:
# (28,28) --> (28, 28, 1)

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)
x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train = x_train / 255
x_test = x_test / 255

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("建立神經網路09")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定二維卷積層Convolution Layer, Conv2D, 用 16 個神經元, 參數 (3*3+1)*16=160 個
model.add(
    Conv2D(16, (3, 3), padding="same", input_shape=(28, 28, 1), activation="relu")
)

# 輸出 16 個 28x28 矩陣
# 事實上是 (28, 28, 16)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))
# (14,14,16)

# 第2層 用 32 個神經元, 使用參數 4640 個
# (3*3*16+1)*32 = 4640

# 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(32, (3, 3), padding="same", activation="relu"))
# output (14, 14, 32)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))
# output (7, 7, 32)

# 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 54 個神經元
model.add(Dense(54, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.087)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

do_the_same2(x_train, y_train, x_test, y_test)  # 做一樣的事
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

"""
輸入格式整理
如果你還記得, 我們每筆輸入資料都是 28x28 的陣列, CNN 其實就是吃「圖」的,
所以基本上不用像之前把每筆資料拉平。
「但。是。」平常的圖都有 R, G, B 三個 channels, 每個 channel 都是一個矩陣,
也就是一張圖可能是三個矩陣! 我們是灰階, 也就是只有一個 channel。
但這件事也要明確的告訴 Keras。
換句話說, 我們的輸入每筆資料型式要從 (28, 28) 換成 (28, 28, 1)!
"""

# print(x_train[1234].shape)
# (28, 28)
# CNN 要的是 (28, 28, 1)
# 確認一下...

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)

x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train = x_train / 255
x_test = x_test / 255

# 原來 28x28 矩陣...
# print(x_train[1234].shape)
# (28, 28, 1)

X = x_train[345]
X = X.reshape(28, 28)
plt.imshow(X, cmap="Greys")

# 輸出格式整理
# 和上次一樣, 我們用標準 1-hot 方式處理。

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# print(y_train[1234])
# array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0.], dtype=float32)

# x_train = x_train/255
# x_test = x_test/255

"""
2-3 打造你的 CNN
決定神經網路架構、讀入相關套件

CNN 我們一樣要決定用幾層的 CNN, 然後是不是每次都要做 max-pooling。
再來就是拉平、送入標準神經網路 (再度要決定幾層、幾個神經元)。

我們上課的時候, 同學建議要做 3 次的 convolution + max-pooling, filter 大小都是 5×5

    做 3 次 convolution, 每次都接 max-pooling
    filter 大小都是 3x3, max-pooling 都用 2x2 為一小區塊

CNN 一個小技巧是每層的 filters 數目是越來越多, 上課同學建議第一層 4 個,
因為要做三次, 所以我們 filters 數分別是 10, 20, 40。
做完 convolution 之後, 我們要拉平、再送入一個標準的神經網路。這個神經網路設計是這樣:
    只有 3 個隱藏層, 使用 :
    layer 1: 5
    layer 2: 8
    layer 3: 20
"""

print("建立神經網路10 正確率XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 第一個隱藏層一樣要告訴 Keras 我們輸入長什麼樣子。padding 設成 same 是每個 filter 會輸出原來 28x28 一樣大小的矩陣。
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    Conv2D(10, (3, 3), padding="same", input_shape=(28, 28, 1), activation="relu")
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPool2D(pool_size=(2, 2)))

# 再 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(20, (3, 3), padding="same", activation="relu"))

# 再 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPool2D(pool_size=(2, 2)))

# 再 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(40, (3, 3), padding="same", activation="relu"))

# 再 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPool2D(pool_size=(2, 2)))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 5 個神經元
model.add(Dense(5, activation="relu"))

# 設定隱藏層HL第2層, 用 8 個神經元
model.add(Dense(8, activation="relu"))

# 設定隱藏層HL第3層, 用 20 個神經元
model.add(Dense(20, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
# model.compile(optimizer=Adadelta(), loss="categorical_crossentropy", metrics=["accuracy"])

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.07)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

# 全部拿來測試
do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

# 儲存結果
# 結果看來還不差, 所以我們把結果存起來。上次我們介紹分別存架構和權重的方法, 這次我們看看怎麼樣一次就存入權重 + 結構!
model.save("tmp_myCNNmodel2.h5")

# 欣賞一下成果
# 我們示範一下怎麼讀回我們的神經網路。你會發現讀回來之後就可以直接使用了!!

del model
# 先把我們原來的 model 刪掉, 保證接下來的是讀進來的。我們要用一個 load_model 的函式。

# NG model = load_model("tmp_myCNNmodel2.h5")

# 小結論 我們到此, 基本上是「亂做」的神經網路。
# 有些同學在不斷試驗的過程中, 可能會發現有時會出現很糟糕的結果。
# 因此, 接下來我們要介紹怎麼樣用些簡單的手法, 能讓學習效果比較穩定, 而且有可能可以增加學習效率。

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
打造第一個神經網路
我們又說第一次要用標準神網路試試,
所以我們只需要再決定要幾個隱藏層、每層要幾個神經元, 用哪個激活函數就可以了。
2.3.1 決定神經網路架構、讀入相關套件
假如我們要這麼做:
    使用 3 個 hidden layers
    Hidden layer 1 用 6 個神經元
    Hidden layer 2 用 28 個神經元
    Hidden layer 3 用 2 個神經元
    激活函數 Activation Function 唯一指名 relu
"""

print("建立神經網路11 正確率XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Flatten(input_shape=(28, 28)))  # 向量輸入拉平

# 設定隱藏層HL第1層, 用 100 個神經元, 使用參數 28 * 28 * 6 + 6 = 4710 個
model.add(Dense(6, activation="relu"))

# 設定隱藏層HL第2層, 用 28 個神經元, 使用參數 6 * 28 + 28 = 196 個
model.add(Dense(28, activation="relu"))

# 設定隱藏層HL第3層, 用 2 個神經元, 使用參數 28 * 2 + 2 = 58 個
model.add(Dense(2, activation="relu"))

# 輸出有 10 個數字, 所以輸出層的神經元是 10 個
# 而如果我們的網路輸出是 (y1,y2,…,y10) 我們還希望 10∑i=1yi=1
# 這可能嗎, 結果是很容易, 就用 softmax 當激活函數就可以!!

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 共使用參數 4994 個

"""
檢視模型架構
Model: "sequential"
┌──────────────────┬──────────┐
│ Layer (type)      │ Output Shape  │  Param # 參數個數  │
├──────────────────┼──────────┤
│ flatten (Flatten) │ (None, 784)   │      0   │ 28 * 28 = 784 
├──────────────────┼─────┤
│ dense (Dense)     │ (None, 6)     │  4710    │ 28 * 28 * 6 + 6 = 4710
├──────────────────┼─────┤
│ dense_1 (Dense)   │ (None, 28)    │    196   │  6 * 28 + 28 = 196
├──────────────────┼─────┤
│ dense_2 (Dense)   │ (None, 2)     │     58   │ 28 * 2 + 2 = 58
├──────────────────┼─────┤
│ dense_3 (Dense)   │ (None, 10)    │     30   │  2 * 10 + 10 = 30
└──────────────────┴─────┘
 Total params: 4,994 (19.51 KB)
 Trainable params: 4,994 (19.51 KB)
 Non-trainable params: 0 (0.00 B)
"""

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.087)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

print("檢視模型架構222")
model.summary()  # 檢視模型架構

"""
訓練神經網路
現在要訓練的時候, 你會發現不是像以前沒頭沒腦把訓練資料送進去就好。
這裡我們還有兩件事要決定:
    1. 一次要訓練幾筆資料 (batch_size), 我們就 N = 100 筆調一次參數好了
    2. 這 6 萬筆資料一共要訓練幾次 (epochs), 我們訓練個 EPOCHS = 20 次試試
於是最精彩的就來了。你要有等待的心理準備...
"""

do_cnn_test4d()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
print("建立神經網路12 4D")

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Flatten(input_shape=(28, 28)))  # 向量輸入拉平

# 設定隱藏層HL第1層, 用 20 個神經元
model.add(Dense(20, activation="relu"))
"""
# ----------------------

print("建立神經網路13 XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 87 個神經元, 使用參數 28 * 28 * 87 + 87 = 68295 個
model.add(Dense(87, input_dim=INPUT_DIM, activation="relu"))

# 設定隱藏層HL第2層, 用 87 個神經元
model.add(Dense(87, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.087)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路14 XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 3層隱藏層HL, 每層 128 個神經元
model.add(Dense(128, activation="sigmoid"))
model.add(Dense(128, activation="sigmoid"))
model.add(Dense(128, activation="sigmoid"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(rate=0.5))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路15")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 設定隱藏層HL第2層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(rate=0.5))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路16 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 計算準確率
# 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)))

# 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定隨機失活層(Dropout層)
model.add(Dropout(0.5))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 128 個神經元
model.add(Dense(128, activation="relu"))

# 設定隨機失活層(Dropout層)
model.add(Dropout(0.5))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 訓練數據300張, 測試數據100張
# Conv層接收的是4軸維陣列(batch_size, 垂直尺寸, 水平尺寸, 顏色通道數)
# 因為MNIST中的數據是單通道, 含batch_size的話僅是三維數據, 所以要先轉換為四維數據

x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 全部拿來測試
do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

# 改成縮寫後, 正確率變低很多~~~~~~~
# do_cnn_test4d()

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 批次正規化

(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = np.reshape(a=x_train, newshape=(-1, 28, 28, 1))
x_test = np.reshape(a=x_test, newshape=(-1, 28, 28, 1))

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 使用 ReLU 函數當做啟動函數

print("建立神經網路17")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    Conv2D(
        input_shape=(28, 28, 1),
        filters=32,
        kernel_size=(2, 2),
        strides=(1, 1),
        padding="same",
    )
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定二維卷積層Convolution Layer, Conv2D
model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=(1, 1), padding="same"))

# 再 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256))

# 設定批次正規化層
model.add(BatchNormalization())

model.add(Activation("relu"))

# 設定隱藏層HL第1層, 用 128 個神經元
model.add(Dense(128))

# 設定批次正規化層
model.add(BatchNormalization())

model.add(Activation("relu"))

classes = 10  # 輸出神經元預設10個

# 設定隱藏層HL第1層, 用 10 個神經元
model.add(Dense(classes))

# 設定輸出層 softmax
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
history = model.fit(
    x_train,
    y_train,
    batch_size=BATCH_SIZE,
    epochs=EPOCHS,
    validation_data=(x_test, y_test),
)

check_model_fit_history2(history)
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

ESC = 27

import cv2

""" NG 無檔案 keras_model.h5
model = tf.keras.models.load_model("keras_model.h5", compile=False)   # 載入 model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)           # 設定資料陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()       # 讀取攝影機影像
    #img = cv2.resize(frame , (640//2, 480//2))   # 改變尺寸
    img = frame
    img = img[0:224, 80:304]               # 裁切為正方形，符合 model 大小
    image_array = np.asarray(img)          # 去除換行符號和結尾空白，產生文字陣列
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1  # 轉換成預測陣列
    data[0] = normalized_image_array
    prediction = model.predict(data)       # 預測結果
    a,b= prediction[0]                     # 取得預測結果
    if a>0.9:
        print("oxxo")
    if b>0.9:
        print("維他命")
        
    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 keras_model.h5
model = tf.keras.models.load_model("keras_model.h5", compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 2.5                      # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 5                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    #img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text("a")  # 使用 text() 函式，顯示文字
    if b>0.9:
        text("b")
    if c>0.9:
        text("c")
        
    cv2.imshow("ImageShow", img)
    
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 keras_model.h5
from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = "NotoSansTC-Regular.otf"          # 設定字型路徑

model = tf.keras.models.load_model("keras_model.h5", compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 50)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 np 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    #img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,c,bg= prediction[0]
    if a>0.9:
        text("剪刀")  # 使用 text() 函式，顯示文字
    if b>0.9:
        text("石頭")
    if c>0.9:
        text("布")

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 keras_model.h5
model = tf.keras.models.load_model("keras_model.h5", compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):      # 建立顯示文字的函式
    global img       # 設定 img 為全域變數
    org = (0,50)     # 文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 文字字型
    fontScale = 1                        # 文字尺寸
    color = (255,255,255)                # 顏色
    thickness = 2                        # 文字外框線條粗細
    lineType = cv2.LINE_AA               # 外框線條樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType) # 放入文字

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame , (640//2, 480//2))
    img frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]    # 印出每個項目的數值資訊
    print(a,b,bg)
    if a>0.999:              # 判斷有戴口罩
        text("ok~")
    if b>0.001:              # 判斷沒戴口罩
        text("no mask!!")

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案 keras_model_3.h5
from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = "NotoSansTC-Regular.otf"          # 設定字型路徑

model = tf.keras.models.load_model("keras_model_3.h5", compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 30)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 np 陣列

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

while True:
    ret, frame = cap.read()
    img = cv2.resize(frame , (640//2, 480//2))
    img = frame
    img = img[0:224, 80:304]
    image_array = np.asarray(img)
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized_image_array
    prediction = model.predict(data)
    a,b,bg= prediction[0]
    print(a,b,bg)
    if a>0.999:
        text("很乖")
    if b>0.001:
        text("沒戴口罩!!")

    cv2.imshow("ImageShow", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

get_elapsed_time()

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 訓練集資料
x_train = x_train.reshape(len(x_train), -1)  # 轉換資料形狀

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train = x_train.astype("float32") / 255  # 轉換資料型別
y_train = y_train.astype(np.float32)

# 測試集資料
x_test = x_test.reshape(len(x_test), -1)  # 轉換資料形狀

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test = x_test.astype("float32") / 255  # 轉換資料型別
y_test = y_test.astype(np.float32)

import cv2

knn = cv2.ml.KNearest_create()  # 建立 KNN 訓練方法
knn.setDefaultK(5)  # 參數設定
knn.setIsClassifier(True)

print("training...")
knn.train(x_train, cv2.ml.ROW_SAMPLE, y_train)  # 開始訓練
knn.save("tmp_mnist_knn.xml")  # 儲存訓練模型
print("ok")

print("testing...")
test_pre = knn.predict(x_test)  # 讀取測試集並進行辨識
test_ret = test_pre[1]
test_ret = test_ret.reshape(
    -1,
)
test_sum = test_ret == y_test
acc = test_sum.mean()  # 得到準確率
print(acc)

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" need Webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("開啟攝影機失敗")
    sys.exit()
else:
    print("Video device opened")

print("loading...")
knn = cv2.ml.KNearest_load("tmp_mnist_knn.xml")  # 載入模型
print("start...")

while True:
    ret, img = cap.read()
    #img = cv2.resize(img, (640//2, 480//2))  # 改變影像尺寸，加快處理效率
    x, y, w, h = 400, 200, 60, 60  # 定義擷取數字的區域位置和大小
    img_num = img.copy()  # 複製一個影像作為辨識使用
    img_num = img_num[y : y + h, x : x + w]  # 擷取辨識的區域

    img_num = cv2.cvtColor(img_num, cv2.COLOR_BGR2GRAY)  # 顏色轉成灰階
    # 針對白色文字，做二值化黑白轉換，轉成黑底白字
    ret, img_num = cv2.threshold(img_num, 127, 255, cv2.THRESH_BINARY_INV)
    output = cv2.cvtColor(img_num, cv2.COLOR_GRAY2BGR)  # 顏色轉成彩色
    img[0:60, 480:540] = output  # 將轉換後的影像顯示在畫面右上角

    img_num = cv2.resize(img_num, (28, 28))  # 縮小成 28x28，和訓練模型對照
    img_num = img_num.astype(np.float32)  # 轉換格式
    img_num = img_num.reshape(
        -1,
    )  # 打散成一維陣列資料，轉換成辨識使用的格式
    img_num = img_num.reshape(1, -1)
    # 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
    img_num = img_num / 255
    img_pre = knn.predict(img_num)  # 進行辨識
    num = str(int(img_pre[1][0][0]))  # 取得辨識結果

    text = num  # 印出的文字內容
    org = (x, y - 20)  # 印出的文字位置
    fontFace = cv2.FONT_HERSHEY_SIMPLEX  # 印出的文字字體
    fontScale = 2  # 印出的文字大小
    color = (0, 0, 255)  # 印出的文字顏色
    thickness = 2  # 印出的文字邊框粗細
    lineType = cv2.LINE_AA  # 印出的文字邊框樣式
    cv2.putText(img, text, org, fontFace, fontScale, color, thickness, lineType)  # 印出文字

    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)  # 標記辨識的區域

    cv2.imshow("WebCam", img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

get_elapsed_time()

hidden_neurons = 100

print("建立神經網路18")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 100 個神經元
model.add(Dense(hidden_neurons, input_dim=INPUT_DIM))

model.add(Activation("sigmoid"))

classes = 10  # 輸出神經元預設10個
model.add(Dense(classes, input_dim=hidden_neurons))

# 設定輸出層 softmax
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)
x_train = x_train.reshape(len(x_train), 784)
x_test = x_test.reshape(len(x_test), 784)

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("久1")

# 學習訓練.fit
do_model_fit1(x_train, y_train)

# 模型評估
evaluate_model(x_test, y_test)

weights = model.layers[0].get_weights()

import matplotlib.cm as cm

fig = plt.figure()

w = weights[0].T
for neuron in range(hidden_neurons):
    ax = fig.add_subplot(10, 10, neuron + 1)
    ax.axis("off")
    ax.imshow(np.reshape(w[neuron], (28, 28)), cmap=cm.Greys_r)

plt.savefig("tmp_neuron_images.png", dpi=300)
show()

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

hidden_neurons = 400

print("建立神經網路19")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 400 個神經元
model.add(Dense(hidden_neurons, input_dim=INPUT_DIM))

model.add(Activation("relu"))

classes = 10  # 輸出神經元預設10個
model.add(Dense(classes, input_dim=hidden_neurons))

# 設定輸出層 softmax
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="adadelta", loss="categorical_crossentropy", metrics=["accuracy"]
)

do_cnn_test()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

hidden_neurons = 200

print("建立神經網路20 4D")

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Convolution2D(32, (3, 3), input_shape=(28, 28, 1)))
model.add(Activation("relu"))
model.add(Convolution2D(32, (3, 3)))
model.add(Activation("relu"))

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# 設定隨機失活層(Dropout層)
model.add(Dropout(0.25))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 200 個神經元
model.add(Dense(hidden_neurons))

model.add(Activation("relu"))

classes = 10  # 輸出神經元預設10個
model.add(Dense(classes))
# 設定輸出層 softmax
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="adadelta", loss="categorical_crossentropy", metrics=["accuracy"]
)

do_cnn_test4d()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路21")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# Conv layer 1 output shape (32, 28, 28)
model.add(
    Convolution2D(
        filters=32,
        kernel_size=(5, 5),
        # border_mode="same",     # Padding method
        # dim_ordering="th",      # if use tensorflow, to set the input dimension order to theano ("th") style, but you can change it.
        input_shape=(28, 28, 1),
    )
)

model.add(Activation("relu"))

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(
    MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2),
        # border_mode="same",    # Padding method
    )
)

# Conv layer 2 output shape (64, 14, 14)
model.add(Convolution2D(64, 5, 5))
model.add(Activation("relu"))

# 再 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(MaxPooling2D(pool_size=(2, 2)))

# Fully connected layer 1 input shape (64 * 7 * 7) = (3136), output shape (1024)

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(Flatten())

# 設定隱藏層HL第1層, 用 1024 個神經元
model.add(Dense(1024))
model.add(Activation("relu"))

# Fully connected layer 2 to shape (10) for 10 classes
classes = 10  # 輸出神經元預設10個
model.add(Dense(classes))
# 設定輸出層 softmax
model.add(Activation("softmax"))

# 先設定優化器, 再組裝神經網路
adam = Adam(learning_rate=1e-4)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

do_cnn_test4d()
get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路22")

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Dense(units=10, activation=tf.nn.relu, input_dim=INPUT_DIM))
model.add(Dense(units=10, activation=tf.nn.relu))
model.add(Dense(units=10, activation=tf.nn.softmax))

# 先設定優化器, 再組裝神經網路
adam = Adam(learning_rate=0.001)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer=adam,
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）

(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = x_train.reshape(len(x_train), 784)
x_test = x_test.reshape(len(x_test), 784)

# 標準化輸入資料
print("x_train before div 255:", x_train[0][180:195])
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("真實目標 :", y_test[:20])

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# 全部拿來測試
# TBD do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

# 學習訓練.fit
# x_train, y_train 進行訓練的因和果的資料
# batch_size=BATCH_SIZE,  # 設定每次訓練的筆數
# epochs=EPOCHS,  # 設定訓練的次數，也就是機器學習的次數
do_model_fit1(x_train, y_train)

# 模型評估
evaluate_model(x_test, y_test)

y_pred = model.predict(x_test)  # 取得每一個結果的機率, 出現0~9的機率

# y_pred : <class "numpy.ndarray"> 10000 筆資料

# np.argmax() 取出 最大值索引, 10個機率裏 最大的機率 就是預測的結果
# np.argmax() 求最大值對應的索引, 將預測的機率轉換成類別
print(
    "前4項 預測結果 :",
    np.argmax(y_pred[0]),
    np.argmax(y_pred[1]),
    np.argmax(y_pred[2]),
    np.argmax(y_pred[3]),
)

ans = np.argmax(y_pred, axis=-1)
# print("ans :", ans)
print("前20項 預測結果 :", ans[:20])

# 預測
y_pred = do_prediction(x_test[:20])
print("預測結果 :\n", y_pred[:20], sep="")

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立神經網路23 正確率XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=3,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=9, kernel_size=(2, 2), padding="same", activation="relu"
    )  # or filters=3
)

# 設定隨機失活層(Dropout層)
model.add(tf.keras.layers.Dropout(rate=0.33))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())

# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(Dense(10, activation="relu"))

# or
# model.add(Dense(50, activation="relu"))
# model.add(Dense(50, activation="relu"))
# model.add(Dense(50, activation="relu"))

# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(Dense(units=10, activation=tf.nn.softmax))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer=tf.keras.optimizers.Adadelta(),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# TBD x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 全部拿來測試
# TBD do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事
# 學習訓練.fit
do_model_fit1(x_train, y_train)

# 模型評估
evaluate_model(x_test, y_test)

y_pred = model.predict(x_test)  # 取得每一個結果的機率
print(
    "預測結果 :",
    np.argmax(y_pred[0]),
    np.argmax(y_pred[1]),
    np.argmax(y_pred[2]),
    np.argmax(y_pred[3]),
)

# 預測
y_pred = do_prediction(x_test)

print("真實目標 :", y_test[:])
print("預測結果 :\n", y_pred, sep="")

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("久2")

from tensorflow.keras.callbacks import TensorBoard

print("建立神經網路24 正確率XXXX")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)

# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 設定隨機失活層(Dropout層)
model.add(tf.keras.layers.Dropout(rate=0.01))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())

# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(Dense(100, activation="relu"))

# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(Dense(100, activation="relu"))
model.add(Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(Dense(units=10, activation=tf.nn.softmax))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer=tf.keras.optimizers.Adadelta(),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# NG x_train, y_train, x_test, y_test = transform_data(x_train, y_train, x_test, y_test)

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("真實目標 :", y_test[:20])

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("久3")
# 全部拿來測試
# TBD do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事

# 學習訓練.fit
do_model_fit1(x_train, y_train)

# 模型評估
evaluate_model(x_test, y_test)

y_pred = model.predict(x_test)  # 取得每一個結果的機率
print(
    "預測結果 :",
    np.argmax(y_pred[0]),
    np.argmax(y_pred[1]),
    np.argmax(y_pred[2]),
    np.argmax(y_pred[3]),
)

# 預測
y_pred = do_prediction(x_test[:20])
print("預測結果 :\n", y_pred[:20], sep="")

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.callbacks import TensorBoard

print("建立神經網路25 Conv2D 正確率高")

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)

# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 設定池化層(Pooling layer, PL)	為 最大池化(Max Pooling)
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
# 設定二維卷積層Convolution Layer, Conv2D
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 設定隨機失活層(Dropout層)
model.add(tf.keras.layers.Dropout(rate=0.01))

# 設定向量輸入拉平, 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())

# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(Dense(100, activation="relu"))

# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(Dense(100, activation="relu"))
model.add(Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(Dense(units=10, activation=tf.nn.softmax))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer=tf.keras.optimizers.Adadelta(),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")

# 資料擴增
gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=8,
    width_shift_range=0.08,
    shear_range=0.3,
    height_shift_range=0.08,
    zoom_range=0.08,
)

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(len(x_train), 28, 28, 1)
x_test = x_test.reshape(len(x_test), 28, 28, 1)

# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("真實目標 :", y_test[:20])

# One-Hot Encoding, 將數字轉為 One-hot 向量
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# train_generator = gen.flow(x_train, y_train, batch_size=64)
train_generator = gen.flow(x_train, y_train, batch_size=128)

# 讀取模型架構
try:
    with open("data/model_ImageDataGenerator.h5", "r") as load_weights:
        # 讀取模型權重
        print("讀取模型權重")
        model.load_weights("data/model_ImageDataGenerator.h5")

except IOError:
    print("File not accessible")


# 保存模型架構
with open("tmp_model_ImageDataGenerator.json", "w") as json_file:
    json_file.write(model.to_json())

print("久4")
# 全部拿來測試
# TBD do_the_same1(x_train, y_train, x_test, y_test)  # 做一樣的事
# 學習訓練.fit 一般
do_model_fit1(x_train, y_train)

# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
history = model.fit(train_generator, epochs=EPOCHS)

# 模型評估
evaluate_model(x_test, y_test)

y_pred = model.predict(x_test)  # 取得每一個結果的機率
print(
    "預測結果 :",
    np.argmax(y_pred[0]),
    np.argmax(y_pred[1]),
    np.argmax(y_pred[2]),
    np.argmax(y_pred[3]),
)

# 預測
y_pred = do_prediction(x_test[:20])
print("預測結果 :\n", y_pred[:20], sep="")

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train[0])

plt.imshow(x_train[0], cmap=plt.cm.binary)
show()

print("答案")
print(y_train[0])

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

print(x_train[0])

plt.imshow(x_train[0], cmap=plt.cm.binary)
show()

model = Sequential()  # 建立空白的神經網路模型(CNN)

model.add(Flatten(input_shape=(28, 28)))  # 向量輸入拉平

# 設定隱藏層HL第1層, 用 128 個神經元
model.add(Dense(128, activation=tf.nn.relu))

# 設定隱藏層HL第2層, 用 128 個神經元
model.add(Dense(128, activation=tf.nn.relu))

# 設定隱藏層HL第3層, 用 10 個神經元
model.add(Dense(10, activation=tf.nn.softmax))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

"""
print("久5 long")

model.fit(x_train, y_train, epochs=EPOCHS)  # 學習訓練.fit

val_loss, val_acc = model.evaluate(x_test, y_test)
print("val_loss :", val_loss)
print("val_acc :", val_acc)

y_pred = model.predict(x_test)  # 取得每一個結果的機率
print("預測結果 :\n", y_pred, sep="")

print(np.argmax(y_pred[0]))

plt.imshow(x_test[0], cmap=plt.cm.binary)
show()

# 保存模型
model.save("tmp_epic_num_reader.model")

# 加载保存的模型
new_model = tf.keras.models.load_model("tmp_epic_num_reader.model")

# 测试保存的模型
y_pred = new_model.predict(x_test)
print(np.argmax(y_pred[0]))

get_elapsed_time()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 不是手寫數字的 CNN

model = Sequential([Dense(units=1, input_shape=[1])])

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="mean_squared_error")

# y = x
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
ys = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype=float)
print(type(xs))
print(xs)
print(type(ys))
print(ys)

model.fit(xs, ys, epochs=EPOCHS)

print("keras 預測")
xx = np.linspace(0.0, 10.0, 21)
yy = model.predict(xx)

"""
print(model.predict([2.5]))
print(model.predict([4.5]))
print(model.predict([6.0]))
print(model.predict([10.0]))
print(xx)
print(yy)
"""

x = np.linspace(0, 10, 100)
plt.plot(x, x, "b", lw=2, label="y = x")
plt.plot(xs, ys, "g-o", lw=1, ms=10, label="實驗點")
plt.scatter(xx, yy, c="red", marker="o", lw=4, label="預測點")

xmin, xmax, ymin, ymax = -1, 11, -1, 11
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
plt.legend()

show()

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Classifier example

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(len(X_train), -1) / 255.0  # normalize
X_test = X_test.reshape(len(X_test), -1) / 255.0  # normalize
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

model = Sequential()  # 建立空白的神經網路模型(CNN)

# 設定隱藏層HL第1層, 用 32 個神經元
model.add(Dense(32, input_dim=INPUT_DIM, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
rmsprop = RMSprop(learning_rate=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]
)

"""
print("久6 long")

# model.fit(X_train, y_train, epoch=2, batch_size=32)
model.fit(X_train, y_train, batch_size=32)

print("預測")
loss, accuracy = model.evaluate(X_test, y_test)
print("test loss: ", loss)
print("test accuracy: ", accuracy)

get_elapsed_time()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Regressor example")

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)  # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200,))

plt.scatter(X, Y)
show()

X_train, Y_train = X[:160], Y[:160]  # first 160 data points
X_test, Y_test = X[160:], Y[160:]  # last 40 data points

# build a neural network from the 1st layer to the last layer
model = Sequential()  # 建立空白的神經網路模型(CNN)

# model.add(Dense(input_dim=1, output_dim=1))
# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="mse")

""" NG
# training
print("Training -----------")
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print("train cost: ", cost)

# test
print("\nTesting ------------")
cost = model.evaluate(X_test, Y_test, batch_size=40)
print("test cost:", cost)
W, b = model.layers[0].get_weights()
print("Weights=", W, "\nbiases=", b)

Y_pred = model.predict(X_test)  # 取得每一個結果的機率
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)

show()
"""

get_elapsed_time()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import keras

# from tensorflow import keras


def preprocess(labels, images):
    """
    最简单的预处理函数:
            转numpy为Tensor、分类问题需要处理label为one_hot编码、处理训练数据
    """
    # 把numpy数据转为Tensor
    labels = tf.cast(labels, dtype=tf.int32)
    # labels 转为one_hot编码
    labels = tf.one_hot(labels, depth=10)
    # 顺手归一化
    images = tf.cast(images, dtype=tf.float32) / 255
    return labels, images


# abs_path_to_dataset=" ... dataset/MNIST/database3/mnist.npz"
# (x, y), (x_test, y_test) = keras.datasets.mnist.load_data(path=abs_path_to_dataset)#绝对路径
(x, y), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

db_train = tf.data.Dataset.from_tensor_slices((x, y))
print(db_train)
print(type(db_train))
db_train.shuffle(1000)
db_train.map(preprocess)
db_train.batch(64)
db_train.repeat(2)

print(type(db_train))
# print(db_train.output_shapes)
# (TensorShape([Dimension(28), Dimension(28)]), TensorShape([]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import tensorflow.examples.tutorials.mnist.input_data as input_data
 
mnist = input_data.read_data_sets("./database2/", one_hot=True)#相对路径
#tensorflow.contrib.learn.python.learn.datasets.mnist.DataSet
print(type(mnist))#<class "tensorflow.contrib.learn.python.learn.datasets.base.Datasets">
 
batch = mnist.train.next_batch(100)
print(type(batch))#<class "tuple">
 
x=mnist.train.images
y=mnist.train.labels
print(type(x),x.shape)#<class "numpy.ndarray"> (55000, 784)
print(type(y),y.shape)#<class "numpy.ndarray"> (55000, 10)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

get_elapsed_time()

print("先到此")
sys.exit()

print("------------------------------------------------------------")  # 60個
print("新")
print("------------------------------------------------------------")  # 60個

# RNN Classifier example

from keras.layers import SimpleRNN

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(-1, 28, 28) / 255.0  # normalize
X_test = X_test.reshape(-1, 28, 28) / 255.0  # normalize
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# build RNN model
model = Sequential()  # 建立空白的神經網路模型(CNN)

#建立SimpleRNN層
model.add(SimpleRNN(input_shape=(28,28),units=256,unroll=True))

#建立拋棄層
model.add(Dropout(0,1))

#建立輸出層
model.add(Dense(units=10,kernel_initializer='normal',activation='softmax'))

"""
        batch_input_shape=(
            None,
            TIME_STEPS,
            INPUT_SIZE,
        ),  # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
        units=256,
        output_dim=CELL_SIZE,
        unroll=True,
    )
)
"""

# 先設定優化器, 再組裝神經網路
adam = Adam(learning_rate=0.001)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

TIME_STEPS = 28  # same as the height of the image
INPUT_SIZE = 28  # same as the width of the image
BATCH_SIZE = 50
BATCH_INDEX = 0
CELL_SIZE = 50

# 訓練
for step in range(4001):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch = X_train[BATCH_INDEX : BATCH_INDEX + BATCH_SIZE, :, :]
    Y_batch = y_train[BATCH_INDEX : BATCH_INDEX + BATCH_SIZE, :]
    cost = model.train_on_batch(X_batch, Y_batch)
    BATCH_INDEX += BATCH_SIZE
    BATCH_INDEX = 0 if BATCH_INDEX >= len(X_train) else BATCH_INDEX

    if step % 500 == 0:
        cost, accuracy = model.evaluate(
            X_test, y_test, batch_size=y_test.shape[0], verbose=False
        )
        print("test cost: ", cost, "test accuracy: ", accuracy)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# RNN LSTM Regressor example

from keras.layers import LSTM
from keras.layers import TimeDistributed

BATCH_START = 0
TIME_STEPS = 20
BATCH_SIZE = 50
INPUT_SIZE = 1
CELL_SIZE = 20


def get_batch():
    global BATCH_START, TIME_STEPS
    # xs shape (50batch, 20steps)
    xs = np.arange(BATCH_START, BATCH_START + TIME_STEPS * BATCH_SIZE).reshape(
        (BATCH_SIZE, TIME_STEPS)
    ) / (10 * np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEPS
    # plt.plot(xs[0, :], res[0, :], "r", xs[0, :], seq[0, :], "b--")
    show()
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]


model = Sequential()  # 建立空白的神經網路模型(CNN)

# build a LSTM RNN
model.add(
    LSTM(
        batch_input_shape=(
            BATCH_SIZE,
            TIME_STEPS,
            INPUT_SIZE,
        ),  # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
        output_dim=CELL_SIZE,
        return_sequences=True,  # True: output at all steps. False: output as last step.
        stateful=True,  # True: the final state of batch1 is feed into the initial state of batch2
    )
)

# add output layer
OUTPUT_SIZE = 1
model.add(TimeDistributed(Dense(OUTPUT_SIZE)))

# 先設定優化器, 再組裝神經網路
adam = Adam(learning_rate=0.006)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(
    optimizer="adam",
    loss="mse",
)

print("Training ------------")
for step in range(501):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch, Y_batch, xs = get_batch()
    cost = model.train_on_batch(X_batch, Y_batch)
    pred = model.predict(X_batch, BATCH_SIZE)
    plt.plot(
        xs[0, :],
        Y_batch[0].flatten(),
        "r",
        xs[0, :],
        pred.flatten()[:TIME_STEPS],
        "b--",
    )
    plt.ylim((-1.2, 1.2))
    plt.draw()
    plt.pause(0.1)
    if step % 10 == 0:
        print("train cost: ", cost)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Autoencoder example

from keras.models import Model
from keras.layers import Input

(x_train, _), (x_test, y_test) = mnist.load_data()

# data pre-processing
x_train = x_train.astype("float32") / 255.0 - 0.5  # minmax_normalized
x_test = x_test.astype("float32") / 255.0 - 0.5  # minmax_normalized
x_train = x_train.reshape((len(x_train), -1))
x_test = x_test.reshape((len(x_test), -1))
print(x_train.shape)
print(x_test.shape)

# in order to plot in a 2D figure
encoding_dim = 2

# this is our input placeholder
input_img = Input(shape=(784,))

# encoder layers
encoded = Dense(128, activation="relu")(input_img)
encoded = Dense(64, activation="relu")(encoded)
encoded = Dense(10, activation="relu")(encoded)
encoder_output = Dense(encoding_dim)(encoded)

# decoder layers
decoded = Dense(10, activation="relu")(encoder_output)
decoded = Dense(64, activation="relu")(decoded)
decoded = Dense(128, activation="relu")(decoded)
decoded = Dense(784, activation="tanh")(decoded)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# save

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)  # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200,))
X_train, Y_train = X[:160], Y[:160]  # first 160 data points
X_test, Y_test = X[160:], Y[160:]  # last 40 data points

model = Sequential()  # 建立空白的神經網路模型(CNN)

# model.add(Dense(output_dim=1, input_dim=1))  # fails here
# 設定隱藏層HL第1層, 用 256 個神經元
model.add(Dense(256, activation="sigmoid", input_dim=INPUT_DIM))

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer="sgd", loss="mse")

for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)

# save
print("test before save: ", model.predict(X_test[0:2]))

model.save(
    "tmp_my_model.h5"
)  # HDF5 file, you have to pip3 install h5py if don't have it
del model  # deletes the existing model

# load
model = load_model("tmp_my_model.h5")
print("test after load: ", model.predict(X_test[0:2]))

"""
# save and load weights
model.save_weights("tmp_my_model_weights.h5")
model.load_weights("tmp_my_model_weights.h5")

# save and load fresh network without trained weights
from keras.models import model_from_json
json_string = model.to_json()
model = model_from_json(json_string)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

# (x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()


# 我們 "predict" 放的是我們神經網路的學習結果。
# 這裡用 predict_classes 會讓我們 Keras 選 10 個輸出機率最大的那類。

# 預測
y_pred = do_prediction(x_test)

# 我們 "predict" 放的是我們神經網路的學習結果。
# 這裡用 predict_classes 會讓我們 Keras 選 10 個輸出機率最大的那類。

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 方法二 將minst資料集放在 特定 位置
mnist = np.load(mnist_npz_filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("檢視模型架構")
model.summary()  # 檢視模型架構

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


import keras

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 把訓練好的神經網路存起來
# 我們可以把神經網路的架構和訓練好的參數都存起來, 以供日後使用!
# pip install h5py

# 學習訓練完成後, 將模型存檔
# After model.fit(...)

# 保存模型架構
with open("tmp_model.json", "w") as json_file:
    json_file.write(model.to_json())

# 保存模型權重
print("將 模型存檔 存成 h5")
model.save("tmp_Mnist_mlp_model.h5")
model.save_weights("tmp_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之 MLP")

# 別人訓練出來的模型
model = load_model("data/Mnist_mlp_model.h5")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test = x_test.reshape(len(x_test), 784) / 255

# 預測
y_pred = do_prediction(x_test)

n = 123
show_predict_result_1d(x_test, y_pred, n)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之 CNN")

# 別人訓練出來的模型
model = load_model("data/Mnist_cnn_model.h5")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,)

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test = x_test.reshape(len(x_test), 28, 28, 1) / 255

# 預測
y_pred = do_prediction(x_test)

n = 123
show_predict_result_1d(x_test, y_pred, n)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之 MLP")

import glob, cv2

files = glob.glob("data\imagedata\*.jpg")  # 建立測試資料
x_test = []
y_test = []
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    x_test.append(img)
    label = file[10:11]  # "imagedata\1.jpg"第10個字元1為label
    y_test.append(int(label))

x_test = np.array(x_test)  # 串列轉為矩陣
y_test = np.array(y_test)  # 串列轉為矩陣

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,) 再轉成 28*28個 float32 數字
x_test = x_test.reshape(len(x_test), 784).astype("float32")

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test = x_test / 255

# 別人訓練出來的模型
model = load_model("data/Mnist_mlp_model.h5")

# 預測
y_pred = do_prediction(x_test)

# 畫出來
images, labels, predictions, start_id, num = (
    x_test,
    y_test,
    y_pred,
    0,
    len(x_test),
)
""" no plot
if num > 25:
    num = 25
for i in range(0, num):
    plt.subplot(16, 16, i + 1)
    plt.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
    if len(predictions) > 0:  # 有傳入預測資料
        title = "ai = " + str(predictions[start_id])
        # 預測正確顯示(o), 錯誤顯示(x)
        title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
        title += "\n" + str(labels[start_id])
    else:  # 沒有傳入預測資料
        title = str(labels[start_id])
    plt.title(title)
    plt.xlabel("")
    plt.ylabel("")
    start_id += 1
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,) 再轉成 28*28個 float32 數字
x_test = x_test.reshape(len(x_test), 784).astype("float32")

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_test = x_test / 255

# 別人訓練出來的模型
model = load_model("data/Mnist_mlp_model.h5")

# 預測
y_pred = do_prediction(x_test)

"""
# 畫出來
images, labels, predictions, start_id, num = x_test, y_test, y_pred, 0, 25

if num > 25:
    num = 25
for i in range(0, num):
    plt.subplot(5, 5, i + 1)
    plt.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
    if len(predictions) > 0:  # 有傳入預測資料
        title = "ai = " + str(predictions[start_id])
        # 預測正確顯示(o), 錯誤顯示(x)
        title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
        title += "\n" + str(labels[start_id])
    else:  # 沒有傳入預測資料
        title = str(labels[start_id])
    plt.title(title)
    plt.xlabel("")
    plt.ylabel("")
    start_id += 1
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 讀取 mnist

DATA_URL = "https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz"

path = tf.keras.utils.get_file("mnist.npz", DATA_URL)
with np.load(path) as data:
    train_examples = data["x_train"]
    train_labels = data["y_train"]
    test_examples = data["x_test"]
    test_labels = data["y_test"]
print("done")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from urllib.request import urlretrieve
import gradio as gr
from PIL import Image

# Loading the MNIST model and data
# 可下載最新之 .h5 檔案
# urlretrieve("https://gr-models.s3-us-west-2.amazonaws.com/mnist-model.h5", "mnist-model.h5")
# mnist-model.h5 路徑不能含中文
mnist_model_filename = "D:/_git/vcs/_big_files/mnist-model.h5"
model = tf.keras.models.load_model(mnist_model_filename)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(
    path="mnist.npz"
)

# 做可視化處理

acc = history.history["accuracy"]
print("訓練準確度 :", acc)

val_acc = history.history["val_accuracy"]
print("驗證準確度 :", val_acc)

plt.plot(acc, label="acc", ls="-", marker="o")
plt.plot(val_acc, label="val_acc", ls="-", marker="x")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.suptitle("model")
show()

plt.plot(history.history["acc"])
plt.plot(history.history["loss"])
plt.title("model accuracy")
plt.ylabel("acc & loss")
plt.xlabel("epoch")
plt.legend(["acc", "loss"], loc="upper left")
show()


""" 一些 fail
print("Auto-Keras")

from autokeras import ImageClassifier
from autokeras.constant import Constant
import autokeras
    
(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))

clf = ImageClassifier(verbose=True, augment=False)

clf.fit(x_train, y_train, time_limit=500 * 60)  # 學習訓練.fit

clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)

# 模型評估.evaluate, 評估準確率, 久7
y = clf.evaluate(x_test, y_test)
print(y * 100)

clf.export_keras_model("tmp_model.h5")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

plt.plot(history.history["acc"])
plt.plot(history.history["loss"])
plt.title("model accuracy")
plt.ylabel("acc & loss")
plt.xlabel("epoch")
plt.legend(["acc", "loss"], loc="upper left")
show()

# 我們用另一個方式: 每次選 5 個顯示, 看是不是有正確辨識。

# 預測
y_pred = do_prediction(x_test)

"""
print("任意挑幾個畫出來")
pick = np.random.randint(0, len(y_pred), 5)
print(pick)

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[pick[i]].reshape(28, 28), cmap="Greys")
    plt.title("預測 :" + str(y_pred[pick[i]]))
    plt.xlabel("")
    plt.ylabel("")
    #plt.axis("off")

show()
"""

# 將前10張圖片畫出來
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].reshape((28, 28)), "gray")

plt.suptitle("The first ten of the test data")

show()

# 顯示前10張圖片的預測結果

for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(x_test[i].reshape((28, 28)), "gray")

show()

# 比較參數
# EOPCHS = 5/10/60

# 比較參數
# BATCH_SIZE = 16 / 32 / 64

print("看 graph seems useless")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

print(x_train[0])
print(x_train[0].shape)

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,) 再轉成 28*28個 float32 數字
x_train = x_train.reshape(len(x_train), 784).astype("float32")
print(x_train[0])
print(x_train[0].shape)

# 將數字影像image的數值正規化(normalization), 從 0~255 => 0~1
x_train = x_train / 255

print(x_train[0])
print(x_train[0].shape)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pip install tf-nightly

import tensorflow as tf

print(tf.__version__)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# x訓練/測試資料 N個 二維影像 (28, 28) 轉成 N個 一維向量 (28*28,) 再轉成 28*28個 float32 數字
x_train = x_train.reshape(len(x_train), 784).astype("float32")
x_test = x_test.reshape(len(x_test), 784).astype("float32")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 設定隱藏層HL第1層, 用 20 個神經元
model.add(Dense(20, activation="relu"))

# 設定隱藏層HL第2層, 用 80 個神經元
model.add(Dense(80, activation="relu"))

# 設定隱藏層HL第3層, 用 100 個神經元
model.add(Dense(100, activation="relu"))

# 設定隱藏層HL第4層, 用 160 個神經元
model.add(Dense(160, activation="relu"))

# 設定輸出層, 用 10 個神經元, 激活函數選 softmax
model.add(Dense(10, activation="softmax"))

# 先設定優化器, 再組裝神經網路
sgd = SGD(learning_rate=0.087)

# 組裝神經網路, 編譯模型 : 選擇優化器(optimizer)、損失函數(loss)、效能衡量指標(metrics)
model.compile(optimizer=sgd, loss="mse", metrics=["accuracy"])

# 數據庫的內容
# 每筆輸入 (x) 就是一個手寫的 0-9 中一個數字的圖檔, 大小為 28x28
# 而輸出 (y) 當然就是「正確答案」

# mnist = input_data.read_data_sets("MNIST_data/")

plt.imshow(image, "gray")
# plt.imshow(X_test[i].reshape((28,28)), "gray")

"""
訓練目標 前300
5 0 4 1 9 2 1 3 1 4 3 5 3 6 1 7 2 8 6 9 4 0 9 1 1 2 4 3 2 7
3 8 6 9 0 5 6 0 7 6 1 8 7 9 3 9 8 5 9 3 3 0 7 4 9 8 0 9 4 1
4 4 6 0 4 5 6 1 0 0 1 7 1 6 3 0 2 1 1 7 9 0 2 6 7 8 3 9 0 4
6 7 4 6 8 0 7 8 3 1 5 7 1 7 1 1 6 3 0 2 9 3 1 1 0 4 9 2 0 0
2 0 2 7 1 8 6 4 1 6 3 4 5 9 1 3 3 8 5 4 7 7 4 2 8 5 8 6 7 3
4 6 1 9 9 6 0 3 7 2 8 2 9 4 4 6 4 9 7 0 9 2 9 5 1 5 9 1 2 3
2 3 5 9 1 7 6 2 8 2 2 5 0 7 4 9 7 8 3 2 1 1 8 3 6 1 0 3 1 0
0 1 7 2 7 3 0 4 6 5 2 6 4 7 1 8 9 9 3 0 7 1 0 2 0 3 5 4 6 5
8 6 3 7 5 8 0 9 1 0 3 1 2 2 3 3 6 4 7 5 0 6 2 7 9 8 5 9 2 1
1 4 4 5 6 4 1 2 5 3 9 3 9 0 5 9 6 5 7 4 1 3 4 0 4 8 0 4 3 6
測試目標 前 300
7 2 1 0 4 1 4 9 5 9 0 6 9 0 1 5 9 7 3 4 9 6 6 5 4 0 7 4 0 1
3 1 3 4 7 2 7 1 2 1 1 7 4 2 3 5 1 2 4 4 6 3 5 5 6 0 4 1 9 5
7 8 9 3 7 4 6 4 3 0 7 0 2 9 1 7 3 2 9 7 7 6 2 7 8 4 7 3 6 1
3 6 9 3 1 4 1 7 6 9 6 0 5 4 9 9 2 1 9 4 8 7 3 9 7 4 4 4 9 2
5 4 7 6 7 9 0 5 8 5 6 6 5 7 8 1 0 1 6 4 6 7 3 1 7 1 8 2 0 2
9 9 5 5 1 5 6 0 3 4 4 6 5 4 6 5 4 5 1 4 4 7 2 3 2 7 1 8 1 8
1 8 5 0 8 9 2 5 0 1 1 1 0 9 0 3 1 6 4 2 3 6 1 1 1 3 9 5 2 9
4 5 9 3 9 0 3 6 5 5 7 2 2 7 1 2 8 4 1 7 3 3 8 8 7 9 2 2 4 1
5 9 8 7 2 3 0 4 4 2 4 1 9 5 7 7 2 8 2 6 8 5 7 7 9 1 8 1 8 0
3 0 1 9 9 4 1 8 2 1 2 9 7 5 9 2 6 4 1 5 8 2 9 2 0 4 0 0 2 8
"""

"""
    fig = plt.gcf()  # 設定顯示圖形的大小
    fig.set_size_inches(2, 2)

    fig = plt.gcf()  # 設定顯示圖形的大小
    fig.set_size_inches(10, 6)
"""

# 第1層 用 16 個神經元, 使用參數 160 個
# 3*3 (權重) + 1 (bias)
# (3*3+1)*16 = 160

