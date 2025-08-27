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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
