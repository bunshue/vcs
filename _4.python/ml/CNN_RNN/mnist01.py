"""
分析顯示 mnist 資料集

Keras: MNIST手寫數字辨識資料集
MNIST手寫數字辨識資料集

由於MNIST的資料大小適中，而且皆為單色影像(黑字白底)，
十分適合做為初學者第一個建立模型、訓練、與預測的資料集。

MNIST資料集是由60,000筆訓練資料、10,000筆測試資料所組成。
MNIST資料集裡的每一筆資料皆由images(數字的影像)與labels
(該圖片的真實數字，其實就是答案)所組成。

# 下載minst資料集檔案
# 資料集檔案位置: C:/Users/070601/.keras/datasets/mnist.npz

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# 共同
BATCH_SIZE = 300  # 每 BATCH_SIZE 筆調一次參數
EPOCHS = 1  # 遞迴次數, 訓練次數

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

from tensorflow.keras.datasets import mnist

# from keras.datasets import mnist
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD  # 優化器


def load_mnist_data(RATIO=1):
    # 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train[: int(len(x_train) / RATIO)]
    y_train = y_train[: int(len(y_train) / RATIO)]
    x_test = x_test[: int(len(x_test) / RATIO)]
    y_test = y_test[: int(len(y_test) / RATIO)]
    print("訓練資料x長度 :", len(x_train))
    print("訓練資料y長度 :", len(y_train))
    print("測試資料x長度 :", len(x_test))
    print("測試資料y長度 :", len(y_test))
    return (x_train, y_train), (x_test, y_test)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("各種讀取資料集的方法")

# 將minst資料集放在 系統 位置
# 下載minst資料集檔案
# 資料集檔案位置: C:/Users/070601/.keras/datasets/mnist.npz
# 用tensorflow讀入 MNSIT 數據集
from tensorflow.keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 標準 1 遠端檔案
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
# 標準 2 本地檔案
mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()
"""

# MNIST手寫數字辨識資料集
# MNIST資料集是由60,000筆 訓練資料 train data
# 10,000筆 測試資料 test data 所組成

# 查看 mnist資料集 內容
# 訓練資料 : (60000, 28, 28) #共60000張圖片資料，圖片像素28*28
# 測試資料 : (10000, 28, 28) #共10000張圖片資料，圖片像素28*28

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("畫出 mnist 數據集訓練資料的前10筆... 久")

(x_train, y_train), (x_test, y_test) = load_mnist_data()


def show_images_labels_predictions(images, labels, start_id, num=10):
    plt.gcf().set_size_inches(10, 6)
    if num > 25:
        num = 25
    for i in range(num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    # plt.show()


show_images_labels_predictions(x_train, y_train, 0, 10)

print("------------------------------------------------------------")  # 60個

from urllib.request import urlretrieve
import gradio as gr
from PIL import Image

# Loading the MNIST model and data
# 可下載最新之 .h5 檔案
# urlretrieve("https://gr-models.s3-us-west-2.amazonaws.com/mnist-model.h5", "mnist-model.h5")
# mnist-model.h5 路徑不能含中文
mnist_model_filename = "C:/_git/vcs/_big_files/mnist-model.h5"
model = tf.keras.models.load_model(mnist_model_filename)

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data(
    path="mnist.npz"
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("畫出 mnist 數據集訓練資料的前256筆... 久")

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 我們來看看訓練資料是不是 6 萬筆、測試資料是不是有 1 萬筆。

print("訓練資料x長度 :", len(x_train))
print("訓練資料y長度 :", len(y_train))
print("測試資料x長度 :", len(x_test))
print("測試資料y長度 :", len(y_test))


print("訓練資料 X(image)長度 :", len(x_train))
print("訓練資料 Y(label)長度 :", len(y_train))
print("測試資料 X(image)長度 :", len(x_test))
print("測試資料 Y(label)長度 :", len(y_test))

print("訓練資料 X(image)大小 :", x_train.shape)
print("訓練資料 Y(label)大小 :", y_train.shape)
print("測試資料 X(image)大小 :", x_test.shape)
print("測試資料 Y(label)大小 :", y_test.shape)

fig = plt.figure(figsize=(8, 8))
for i in range(256):
    ax = plt.subplot2grid((16, 16), (int(i / 16), int(i % 16)))
    ax.imshow(x_train[i], cmap=plt.cm.gray)
    ax.axis("off")
plt.suptitle("畫前256筆資料")
# plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# https://waternotetw.blogspot.com/2018/03/keras-mnist.html

# 匯入Keras及相關模組
# 匯入keras.utils因為後續要將label標籤轉換為One-hotencoding

from tensorflow.python.keras.utils import np_utils

# (x_train, y_train), (x_test, y_test) = load_mnist_data()
(x_train_image, y_train_label), (x_test_image, y_test_label) = load_mnist_data()

# 查看mnist資料集筆數
# 60,000筆的train data(訓練資料)與10,000筆的test data(測試資料)
print("train data=", len(x_train_image))
print("test data=", len(x_test_image))

# 每一筆mnist資料皆是由images(數字影像)與labels(數字真實值)所組成，
# images的部分為單色、28*28像素的影像檔案(圖片)，label則是該張影像檔案的真實數值(解答)
print("x_train_image :", x_train_image.shape)  # x_train_image : (60000, 28, 28)
print("y_train_label :", y_train_label.shape)  # 共60000張圖片資料，圖片像素28*28


# 建立plot_image函數，顯示images數字影像
def plot_image(image):  # 定義plot_image函數，傳入image作為參數
    fig = plt.gcf()  # 設定顯示圖形的大小
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap="binary")  # 傳入參數image、28*28像素的圖形，camp="binary"表示以黑白色顯示
    # plt.show()  # 顯示圖片


print("顯示第1筆訓練資料 圖形")
plot_image(x_train_image[1])

print("顯示第1筆訓練資料 結果")
print(y_train_label[1])

print("顯示多筆mnist資料內容")


# 匯入matplotlib.pyplot模組內容
# 顯示資料集內容
def plot_images_labels(
    images, labels, idx, num=10
):  # 定義plot_images_labels_prediction()函式
    fig = plt.gcf()  # 設定顯示圖形的大小
    fig.set_size_inches(10, 6)
    if num > 25:
        num = 25  # 如果顯示筆數參數大於25鎖定在25，避免輸出時發生錯誤
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)  # 建立subgraph子圖形為5行5列
        ax.imshow(images[idx], cmap="binary")  # 劃出subgraph子圖形
        title = "label=" + str(labels[idx])  # 設定子圖形的title，顯示標籤欄
        ax.set_title(title, fontsize=10)  # 子圖形的標題tilte與大小
        ax.set_xticks([])
        ax.set_yticks([])  # 設定不顯示刻度
        idx += 1  # 讀取下一筆
    # plt.show()  # 開始繪圖


print("顯示 第0到第9筆 訓練資料")
plot_images_labels(x_train_image, y_train_label, idx=0)

print("顯示 第0到第9筆 測試資料")
plot_images_labels(x_test_image, y_test_label, idx=0)

# 將image以reshape()轉換
# 先將原本28*28的2維數字影像，以reshape()轉換成1維向量，再以astype()轉換為float，共784個float數字
x_Train = x_train_image.reshape(60000, 28 * 28).astype("float32")
x_Test = x_test_image.reshape(10000, 28 * 28).astype("float32")

print("將二維 28X28 的影像 轉為 一維 784 資料 reshape")
print("轉換後的 訓練資料 大小 x_train:", x_Train.shape)
print("轉換後的 測試資料 大小 x_test:", x_Test.shape)

# 每個數字由0至255組成，代表圖形每一個點的灰階深淺
print("看第0筆一維影像內容")
print(x_train_image[0])

# 將數字影像image的數值正規化(normalization)
x_Train_normalization = x_Train / 255
x_Test_normalization = x_Test / 255

print("看標準化後第0筆一維影像內容")
print(x_Train_normalization[0])

# 查看訓練資料label標籤欄位的前五筆訓練資料
print("看前5筆 訓練資料")
print(y_train_label[:5])

# 使用np_utils.to_categorical()分別傳入y_train_label與y_test_label的label標籤欄位，執行One-hot encoding轉換
y_TrainOneHot = np_utils.to_categorical(y_train_label)
y_TestOneHot = np_utils.to_categorical(y_test_label)

print("輸出One-hot encoding轉換結果")
print(y_TrainOneHot[:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data(10)

x_train = x_train / 255
x_test = x_test / 255

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD  # 優化器

print("建立神經網路1")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Flatten(input_shape=(28, 28)))

# 第1層 用 20 個神經元
model.add(Dense(20, activation="relu"))
# 第1層 用 80 個神經元
model.add(Dense(80, activation="relu"))
# 第1層 用 100 個神經元
model.add(Dense(100, activation="relu"))
# 第1層 用 160 個神經元
model.add(Dense(160, activation="relu"))

# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="mse", optimizer=SGD(learning_rate=0.087), metrics=["accuracy"])

# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
# model.fit(x_train, y_train, batch_size=100, epochs=EPOCHS)  # 學習訓練.fit
model.fit(x_train, y_train, batch_size=2000, epochs=EPOCHS)  # 學習訓練.fit

print(y_train[33])
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 1.], dtype = float32)

print(y_test[2])
# array([0., 1., 0., 0., 0., 0., 0., 0., 0., 0.], dtype = float32)

print("預測")
# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x


def test(n):
    print("神經網路判斷為:", y_pred[n])
    plt.imshow(x_test[n], cmap="Greys")
    # plt.show()


test(123)

"""
print("久 .evaluate()...")
score = model.evaluate(x_test, y_test)

print("loss:", score[0])
print("正確率", score[1])

# loss: 0.01081830496697512
# 正確率 0.9308000206947327
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

# 顯示 Numpy 二維陣列內容
print(X_train[0])
print(Y_train[0])  # 標籤資料

plt.imshow(X_train[0], cmap="gray")
plt.title("顯示數字圖片 Label: " + str(Y_train[0]))
plt.axis("off")

# plt.show()


sub_plot = 330
for i in range(0, 9):
    ax = plt.subplot(sub_plot + i + 1)
    ax.imshow(X_train[i], cmap="gray")
    ax.set_title("Label: " + str(Y_train[i]))
    ax.axis("off")

plt.subplots_adjust(hspace=0.5)
plt.title("前9張圖")
# plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.utils import to_categorical

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

# 將圖片轉換成 4D 張量
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float32")

# 因為是固定範圍, 所以執行正規化, 從 0-255 至 0-1
X_train = X_train / 255
X_test = X_test / 255

# One-hot編碼
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

print("建立神經網路2")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(
    Conv2D(
        16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))

# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

cc = model.summary()  # 顯示模型摘要資訊
print(cc)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
history = model.fit(
    X_train, Y_train, validation_split=0.2, epochs=EPOCHS, batch_size=2000, verbose=2
)  # 學習訓練.fit

# 評估模型
print("久 .evaluate()...")
loss, accuracy = model.evaluate(X_train, Y_train, verbose=0)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))

print("久 .evaluate()...")
loss, accuracy = model.evaluate(X_test, Y_test, verbose=0)
print("測試資料集的準確度 = {:.2f}".format(accuracy))

# 訓練資料集的準確度 = 0.99
# 測試資料集的準確度 = 0.99

# 顯示訓練和驗證損失
loss = history.history["loss"]
epochs = range(1, len(loss) + 1)
val_loss = history.history["val_loss"]
plt.plot(epochs, loss, "bo-", label="Training Loss")
plt.plot(epochs, val_loss, "ro--", label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()

# plt.show()

# 顯示訓練和驗證準確度
acc = history.history["accuracy"]
epochs = range(1, len(acc) + 1)
val_acc = history.history["val_accuracy"]
plt.plot(epochs, acc, "bo-", label="Training Acc")
plt.plot(epochs, val_acc, "ro--", label="Validation Acc")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()

# plt.show()

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

# 選一個測試的數字圖片
i = 7
digit = X_test[i].reshape(28, 28)
# 將圖片轉換成 4D 張量
X_test_digit = X_test[i].reshape(1, 28, 28, 1).astype("float32")
# 因為是固定範圍, 所以執行正規化, 從 0-255 至 0-1
X_test_digit = X_test_digit / 255
# 繪出數字圖片
plt.figure()
plt.title("Example of Digit:" + str(Y_test[i]))
plt.imshow(digit, cmap="gray")
plt.axis("off")
# plt.show()

# (-0.5, 27.5, 27.5, -0.5)

# 預測結果的機率
probs = model.predict(X_test_digit, batch_size=1)[0]
print(probs)
plt.title("Probabilities for Each Digit Class")
plt.bar(np.arange(10), probs.reshape(10), align="center")
plt.xticks(np.arange(10), np.arange(10).astype(str))

# plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

n = 1234
print("看第", n, "筆訓練資料")
print("內容 :", x_train[n])
print("大小 :", x_train[n].shape)
print("目標 :", y_train[n])
plt.imshow(x_train[n], cmap="Greys")
# plt.show()

x_train = x_train.reshape(60000, 784) / 255
x_test = x_test.reshape(10000, 784) / 255

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

print("看第", n, "筆訓練資料")
print("轉換後的目標 :", y_train[n])

print("建立神經網路3")
print("建立 3 層神經網路 100 100 100")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(100, input_dim=784, activation="relu"))  # input_dim 輸入層: 784
model.add(Dense(100, activation="relu"))
model.add(Dense(100, activation="relu"))

# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="mse", optimizer=SGD(learning_rate=0.087), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

print("x_train.shape :", x_train.shape)
""" 久
# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
# model.fit(x_train, y_train, batch_size=100, epochs=EPOCHS)# 學習訓練.fit
# model.fit(x_train, y_train, batch_size=1000, epochs=EPOCHS)# 學習訓練.fit
model.fit(x_train, y_train, batch_size=2000, epochs=EPOCHS)  # 學習訓練.fit

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

# print(y_pred)

n = 1234

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")
#plt.show()

print("神經網路預測第", n, "筆訓練資料")
print(y_pred[n])
print(y_pred[n].shape)

plt.plot(y_pred[n])
#plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.python.keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

(train_feature, train_label), (test_feature, test_label) = load_mnist_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
train_feature_normalize = train_feature_vector / 255
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

print("建立神經網路4")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(
    Dense(
        units=256,  # units 隱藏層: 256
        input_dim=784,  # input_dim 輸入層: 784
        kernel_initializer="normal",
        activation="relu",
    )
)

# 設定輸出層
model.add(
    Dense(units=10, kernel_initializer="normal", activation="softmax")
)  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
model.fit(
    x=train_feature_normalize,
    y=train_label_onehot,
    validation_split=0.2,
    epochs=EPOCHS,
    batch_size=2000,
    verbose=2,
)
""" 久
print("久 .evaluate()...")
scores = model.evaluate(test_feature_normalize, test_label_onehot)  # 評估準確率
print("\n準確率=", scores[1])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("寫入 模型")

from tensorflow.python.keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense

(train_feature, train_label), (test_feature, test_label) = load_mnist_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
train_feature_normalize = train_feature_vector / 255
test_feature_normalize = test_feature_vector / 255
train_label_onehot = np_utils.to_categorical(train_label)
test_label_onehot = np_utils.to_categorical(test_label)

print("建立神經網路5")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(
    Dense(
        units=256,  # units 隱藏層: 256
        input_dim=784,  # input_dim 輸入層: 784
        kernel_initializer="normal",
        activation="relu",
    )
)

# 設定輸出層
model.add(
    Dense(units=10, kernel_initializer="normal", activation="softmax")
)  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
model.fit(
    x=train_feature_normalize,
    y=train_label_onehot,
    validation_split=0.2,
    epochs=EPOCHS,
    batch_size=2000,
    verbose=2,
)
"""
print("久 .evaluate()...")
# 評估準確率
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print("\n準確率=", scores[1])

print("將 模型存檔 存成 h5")
model.save("tmp_Mnist_mlp_model.h5")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之 MLP")

from tensorflow.keras.models import load_model

# 別人訓練出來的模型
model = load_model("Mnist_mlp_model.h5")

(x_train, y_train), (x_test, y_test) = load_mnist_data(10)

x_test = x_test.reshape(len(x_test), 784) / 255

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x


def myNN(n):
    k = int(n)
    print("神經網路預測", y_pred[k])
    plt.imshow(x_test[k].reshape(28, 28), cmap="Greys")
    # plt.show()


myNN(123)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("看 label")
from tensorflow.python.keras.utils import np_utils

(train_feature, train_label), (test_feature, test_label) = load_mnist_data()

print(train_label[0:5])
train_label_onehot = np_utils.to_categorical(train_label)
print(train_label_onehot[0:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("看 graph")

(train_feature, train_label), (test_feature, test_label) = load_mnist_data()

train_feature_vector = train_feature.reshape(len(train_feature), 784).astype("float32")
# print(train_feature_vector[0])
train_feature_normalize = train_feature_vector / 255
print(train_feature_normalize[0])


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 一些 fail
print('Auto-Keras')

from autokeras import ImageClassifier
from autokeras.constant import Constant
import autokeras
from keras.utils import plot_model
    
(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = x_train.reshape(x_train.shape + (1,))
x_test = x_test.reshape(x_test.shape + (1,))

clf = ImageClassifier(verbose=True, augment=False)

clf.fit(x_train, y_train, time_limit=500 * 60)  # 學習訓練.fit

clf.final_fit(x_train, y_train, x_test, y_test, retrain=True)

print("久 .evaluate()...")
y = clf.evaluate(x_test, y_test)
print(y * 100)

clf.export_keras_model('tmp_model.h5')
plot_model(clf, to_file='model.png')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
參考 https://ithelp.ithome.com.tw/m/articles/10191404
有說明
"""
# 導入函式庫
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation, Flatten

# from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding
from tensorflow.python.keras.utils import np_utils

from matplotlib import pyplot as plt

(X_train, y_train), (X_test, y_test) = load_mnist_data()

print("建立神經網路6")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

# Add Input layer, 隱藏層(hidden layer) 有 256個輸出變數
model.add(
    Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu")
)  # units 隱藏層: 256, input_dim 輸入層: 784

# 設定輸出層
model.add(
    Dense(units=10, kernel_initializer="normal", activation="softmax")
)  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 將 training 的 label 進行 one-hot encoding，例如數字 7 經過 One-hot encoding 轉換後是 0000001000，即第7個值為 1
y_TrainOneHot = np_utils.to_categorical(y_train)
y_TestOneHot = np_utils.to_categorical(y_test)

# 將 training 的 input 資料轉為2維
X_train_2D = X_train.reshape(60000, 28 * 28).astype("float32")
X_test_2D = X_test.reshape(10000, 28 * 28).astype("float32")

x_Train_norm = X_train_2D / 255
x_Test_norm = X_test_2D / 255

""" fit 很久

# 學習訓練.fit
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
model.fit(x=x_Train_norm, y=y_TrainOneHot, validation_split=0.2, epochs=EPOCHS, batch_size=8000, verbose=2)
# 學習訓練.fit

# 顯示訓練成果(分數)
print("久 .evaluate()...")
scores = model.evaluate(x_Test_norm, y_TestOneHot)  
print()  
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1]*100.0))  

# 預測(prediction)
X = x_Test_norm[0:10,:]
predictions = np.argmax(model.predict(X), axis=-1)
# get prediction result
print(predictions)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 讀取 mnist

DATA_URL = 'https://storage.googleapis.com/tensorflow/tf-keras-datasets/mnist.npz'

path = tf.keras.utils.get_file('mnist.npz', DATA_URL)
with np.load(path) as data:
    train_examples = data['x_train']
    train_labels = data['y_train']
    test_examples = data['x_test']
    test_labels = data['y_test']
print('done')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
CNN 還是手寫辨識
Yann LeCun 被譽為 Deep Learning 的三巨頭之一。
他的 CNN (Convolutional Neural Networks) 是讓 Neural Network 重新受到重視的主因之一。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
(x_train, y_train), (x_test, y_test) = load_mnist_data()

# Channel
# CNN 要注意一張圖有多少個 channel, 開始我們因為只有灰階, 所以只有一個 channel。
# 因此我們要轉一下我們的資料格式:
# (28,28) --> (28, 28, 1)

x_train = x_train.reshape(60000, 28, 28, 1) / 255
x_test = x_test.reshape(10000, 28, 28, 1) / 255

print(x_train[87].shape)
#(28, 28, 1)

print(y_train[87])
#9

from tensorflow.keras.utils import to_categorical
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

#讀入必要的函式
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten

print("建立神經網路7")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Conv2D(16, (3,3), padding='same',
                input_shape=(28,28,1),
                activation='relu'))

# 輸出 16 個 28x28 矩陣
# 事實上是 (28, 28, 16)

model.add(MaxPooling2D(pool_size=(2,2)))
# (14,14,16)

model.add(Conv2D(32, (3,3), padding='same',
                activation='relu'))
# output (14, 14, 32)

model.add(MaxPooling2D(pool_size=(2,2)))
# output (7, 7, 32)

model.add(Conv2D(64, (3,3), padding='same',
                activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(54, activation='relu'))
model.add(Dense(10, activation='softmax'))

print("檢視神經網路")
model.summary()  #檢視神經網路

# 3*3 (權重) + 1 (bias)
#(3*3+1)*16 = 160

#(3*3*16+1)*32 = 4640

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss='mse', optimizer=SGD(learning_rate=0.087), metrics=['accuracy'])

model.fit(x_train, y_train, batch_size=128, epochs=EPOCHS)  # 學習訓練.fit

#預測
# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x


def my_predict(n):
    print('我可愛的 CNN 預測是', y_pred[n])
    X = x_test[n].reshape(28,28)
    plt.imshow(X, cmap='Greys')
    #plt.show()

n = 123
my_predict(n)

print("久 .evaluate()...")
score = model.evaluate(x_test, y_test)

loss, acc = score
print('測試資料的正確率為', acc)

#把我們的 model 存起來
model.save('tmp_myCNNmodel.h5')
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
2-1 初始準備
基本上和之前是一樣的, 我們就不再說明。
2-2 讀入 MNIST 數據庫
由 Keras 讀入 MNIST
基本上和我們上次一樣, 這次因為 Keras 已偷偷把數據庫存在你的電腦, 所以會快很多!
"""

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

print(x_train[1234].shape)

# (28, 28)
# CNN 要的是 (28, 28, 1)
# 確認一下...

x_train = x_train.reshape(60000, 28, 28, 1) / 255
x_test = x_test.reshape(10000, 28, 28, 1) / 255

# 原來 28x28 矩陣...

print(x_train[1234].shape)

# (28, 28, 1)

X = x_train[1234]
X = X.reshape(28, 28)
plt.imshow(X, cmap="Greys")

"""
輸出格式整理
和上次一樣, 我們用標準 1-hot 方式處理。
"""

print(y_train[1234])
# 3

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

print(y_train[1234])

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

from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.layers import Conv2D, MaxPool2D
from keras.optimizers import SGD  # 優化器

print("建立神經網路8")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

# 第一個隱藏層一樣要告訴 Keras 我們輸入長什麼樣子。padding 設成 same 是每個 filter 會輸出原來 28x28 一樣大小的矩陣。

model.add(
    Conv2D(10, (3, 3), padding="same", input_shape=(28, 28, 1), activation="relu")
)

# Max-Pooling!

model.add(MaxPool2D(pool_size=(2, 2)))

# 第二次 Convolution!

model.add(Conv2D(20, (3, 3), padding="same", activation="relu"))

# 再 Max-Pooling!

model.add(MaxPool2D(pool_size=(2, 2)))

# 第三次 Convolution!

model.add(Conv2D(40, (3, 3), padding="same", activation="relu"))

# Max-Pooling 最終回。

model.add(MaxPool2D(pool_size=(2, 2)))

# 然後我們要送進一般的神經網路了。記得這是要拉平的, 還在 Keras 會幫我們做!

model.add(Flatten())
model.add(Dense(5, activation="relu"))
model.add(Dense(8, activation="relu"))
model.add(Dense(20, activation="relu"))

# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

# 組裝
# 和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
# model.compile(loss="categorical_crossentropy",
#              optimizer=Adadelta(),
#              metrics=['accuracy'])

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="mse", optimizer=SGD(learning_rate=0.07), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

''' skip
print("久 .fit()...")
model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS)  # 學習訓練.fit

# 這裡因為第一次訓練有點遜 (CNN 標準), 所以我再執行 fit 一次, 因此實際上是訓練了 20 次。??

"""
2-5 結果測試
分數

我們來看測試資料 (我們的 CNN 沒看過的)
"""

print("久 .evaluate()...")
score = model.evaluate(x_test, y_test)

# 我們來看成績, 順便用 Python 3.6 開始的 f-string format 方式。
print(f"測試資料的 loss: {score[0]:.5f}")
print(f"測試資料的正確率: {score[1]}")

# 測試資料的 loss: 0.02530
# 測試資料的正確率: 0.8328999876976013

# 儲存結果
# 結果看來還不差, 所以我們把結果存起來。上次我們介紹分別存架構和權重的方法, 這次我們看看怎麼樣一次就存入權重 + 結構!

model.save("tmp_myCNNmodel.h5")

# 欣賞一下成果
# 我們示範一下怎麼讀回我們的神經網路。你會發現讀回來之後就可以直接使用了!!

del model
# 先把我們原來的 model 刪掉, 保證接下來的是讀進來的。我們要用一個 load_model 的函式。

from keras.models import load_model

model = load_model("myCNNmodel.h5")

# 我們用另一個方式: 每次選 5 個顯示, 看是不是有正確辨識。

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

# 看來真的可以直接用!!
pick = np.random.randint(1, 9999, 5)

for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[pick[i]].reshape(28, 28), cmap="Greys")
    plt.title(y_pred[pick[i]])
    plt.axis("off")

"""
小結論
我們到此, 基本上是「亂做」的神經網路。
有些同學在不斷試驗的過程中, 可能會發現有時會出現很糟糕的結果。
因此, 接下來我們要介紹怎麼樣用些簡單的手法, 能讓學習效果比較穩定, 而且有可能可以增加學習效率。
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之 CNN")

from tensorflow.keras.models import load_model

# 別人訓練出來的模型
model = load_model("Mnist_cnn_model.h5")

(x_train, y_train), (x_test, y_test) = load_mnist_data(10)

x_test = x_test.reshape(len(x_test), 28, 28, 1) / 255

#y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

def myCNN(n):
    print("CNN神經網路預測 :", y_pred[n])
    X = x_test[n].reshape(28, 28)
    plt.imshow(X, cmap="Greys")
    #plt.show()


n = 123
myCNN(n)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.models import load_model
import glob, cv2


def show_images_labels_predictions(images, labels, predictions, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        if len(predictions) > 0:  # 有傳入預測資料
            title = "ai = " + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
            title += "\nlabel = " + str(labels[start_id])
        else:  # 沒有傳入預測資料
            title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    #plt.show()


files = glob.glob("imagedata\*.jpg")  # 建立測試資料
test_feature = []
test_label = []
for file in files:
    img = cv2.imread(file)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰階
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
    test_feature.append(img)
    label = file[10:11]  # "imagedata\1.jpg"第10個字元1為label
    test_label.append(int(label))

test_feature = np.array(test_feature)  # 串列轉為矩陣
test_label = np.array(test_label)  # 串列轉為矩陣
test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
test_feature_normalize = test_feature_vector / 255

# 別人訓練出來的模型
model = load_model("Mnist_mlp_model.h5")

# y_pred = model.predict_classes(test_feature_normalize) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(test_feature_normalize)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

show_images_labels_predictions(
    test_feature, test_label, y_pred, 0, len(test_feature)
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data(12)

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
# plt.show()

plt.imshow(x_train[87], cmap="Greys")
plt.title("顯示編號87號的訓練資料")
# plt.show()

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
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD # 優化器

"""
2.3.2 建構我們的神經網路
和以前做迴歸或機器學習一樣, 我們就打開個「函數學習機」。
標準一層一層傳遞的神經網路叫 Sequential, 於是我們打開一個空的神經網路。
"""

print("建立神經網路9")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

"""
我們每次用 add 去加一層, 從第一個隱藏層開始。
而第一個隱藏層因為 Keras 當然猜不到輸入長什麼樣子, 所以我們要告訴它。
而全連結的神經網路其實都是一個向量輸入, 也就是要先「拉平」。
"""

model.add(Flatten(input_shape=(28, 28)))

# 第1層 用 6 個神經元
model.add(Dense(6, activation="relu"))

"""
第二層 hidden layer 因為前面輸出是 6, 現在輸入是 28, 就不用再說了!
這裡的 28 只告訴 Keras, 我們第二層是用 28 個神經元!
"""
# 第1層 用 28 個神經元
model.add(Dense(28, activation="relu"))

# 第3層 用 2 個神經元
model.add(Dense(2, activation="relu"))

# 輸出有 10 個數字, 所以輸出層的神經元是 10 個!
# 而如果我們的網路輸出是 (y1,y2,…,y10) 我們還希望 10∑i=1yi=1
# 這可能嗎, 結果是很容易, 就用 softmax 當激發函數就可以!!
# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

# 至此我們的第一個神經網路就建好了!

"""
2.3.3 組裝

和之前比較不一樣的是我們還要做 compile 才正式把我們的神經網路建好。
你可以發現我們還需要做幾件事:
    1. 決定使用的 loss function, 一般是 mse
    2. 決定 optimizer(優化器), 我們用標準的 SGD
    3. 設 learning rate
為了一邊訓練一邊看到結果, 我們加設
metrics=['accuracy']
本行基本上和我們的神經網路功能沒有什麼關係。
"""

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="mse", optimizer=SGD(learning_rate=0.087), metrics=["accuracy"])

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

print(
    "資料共有 :",
    len(x_train),
    "筆, 每",
    BATCH_SIZE,
    "筆調一次參數, 共需調",
    len(x_train) / BATCH_SIZE,
    "次",
)
print("訓練次數 :", EPOCHS)

print("x_train len")
print(len(x_train))
print("y_train len")
print(len(y_train))

model.fit(x_train, y_train, batch_size=BATCH_SIZE, epochs=EPOCHS)  # 學習訓練.fit

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print(y_pred)

print("預測2")
y_pred = (model.predict_classes(x_test) > 0.5).astype("int32")
print(y_pred)

# array([7, 2, 1, ..., 7, 7, 0]) 有問題~~~~~~~~
# 寫個小程式, 秀出某測試資料的樣子, 還有我們可愛神經網路辨識的結果。


def test(num):
    plt.imshow(x_test[num], cmap="Greys")
    print("num =", num)
    print("神經網路判斷為 : ", y_pred[num])
    print()


n = 123
test(n)
# plt.show()
print("神經網路判斷為 : ", y_pred[n])

# 神經網路判斷為 : 3   有問題~~~~~~~
# 到底測試資料總的狀況如何呢? 我們可以給我們神經網路「考一下試」。

print("x_test len")
print(len(x_test))
print("y_test len")
print(len(y_test))

print("久 .evaluate()...")
score = model.evaluate(x_test, y_test)
print()

print("loss:", score[0])
print("正確率", score[1])

# loss: 0.06821700274944305
# 正確率 0.4345

# 2-7 訓練好的神經網路存起來!
# 如果對訓練成果滿意, 我們當然不想每次都再訓練一次!
# 我們可以把神經網路的架構和訓練好的參數都存起來, 以供日後使用!
# pip install h5py

model_json = model.to_json()
open("tmp_stupid_model.json", "w").write(model_json)
model.save_weights("tmp_stupid_model_weights.h5")
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = load_mnist_data()

x_train = x_train / 255
x_test = x_test / 255

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.optimizers import SGD  # 優化器

print("建立神經網路10")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Flatten(input_shape=(28, 28)))

model.add(Dense(20, activation="relu"))

print("使用TensorFlow")

"""
標準 神經網路 做手寫辨識
Keras 可以用各種不同的深度學習套件當底層, 指定用 Tensorflow 以確保執行的一致性。
%env KERAS_BACKEND=tensorflow
"""

n = 9487
print(x_train[n])
print(y_train[n])
# 1
plt.imshow(x_train[n], cmap="Greys")
# plt.show()


# 3. 資料整理
# 先看個範例, 因為 numpy 「廣播」的特性, 我們對 array 中所有數字要同除以一個數可瞬間完成!
cc = np.array([3, 78, 95, 99]) / 100
print(cc)

# array([0.03, 0.78, 0.95, 0.99])

# 現在才是我們真的要做的, 這個動作叫 "normalization"。

x_train = x_train / 255
x_test = x_test / 255
cc = x_train.shape
print(cc)

# (60000, 28, 28)

# 28*28 = 784

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)
cc = y_train[9487]
print(cc)

print("建立神經網路11")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(87, input_dim=784, activation="relu"))  # input_dim 輸入層: 784

model.add(Dense(87, activation="relu"))

# 設定輸出層
model.add(Dense(10, activation="softmax"))  # 輸出層的神經元 10 個

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="mse", optimizer=SGD(learning_rate=0.087), metrics=["accuracy"])

print("檢視神經網路")
model.summary()  # 檢視神經網路

# 784*87 + 87 = 68295
"""
# NG here
# model.fit(x_train, y_train, batch_size = 100, epochs=EPOCHS)# 學習訓練.fit
# model.fit(x_train, y_train, batch_size = 1200, epochs=EPOCHS)# 學習訓練.fit
model.fit(x_train, y_train, batch_size=2400, epochs=EPOCHS)  # 學習訓練.fit

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

n = 123
print("神經網路預測是:", y_pred[n])

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")

# 神經網路預測是: 6
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
""" 久
from keras.models import load_model


def show_images_labels_predictions(images, labels, predictions, start_id, num=10):
    plt.gcf().set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, i + 1)
        ax.imshow(images[start_id], cmap="binary")  # 顯示黑白圖片
        if len(predictions) > 0:  # 有傳入預測資料
            title = "ai = " + str(predictions[start_id])
            # 預測正確顯示(o), 錯誤顯示(x)
            title += " (o)" if predictions[start_id] == labels[start_id] else " (x)"
            title += "\nlabel = " + str(labels[start_id])
        else:  # 沒有傳入預測資料
            title = "label = " + str(labels[start_id])
        ax.set_title(title, fontsize=12)  # X,Y軸不顯示刻度
        ax.set_xticks([])
        ax.set_yticks([])
        start_id += 1
    #plt.show()


(train_feature, train_label), (test_feature, test_label) = load_mnist_data()

test_feature_vector = test_feature.reshape(len(test_feature), 784).astype("float32")
test_feature_normalize = test_feature_vector / 255

# 別人訓練出來的模型
model = load_model("Mnist_mlp_model.h5")

# y_pred = model.predict_classes(test_feature_normalize) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(test_feature_normalize)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

show_images_labels_predictions(test_feature, test_label, y_pred, 0)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.datasets import mnist

# from keras.datasets import mnist

from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路12")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

# plot_model(model, show_shapes=True, show_layer_names=False)
# 目前plot_model不能用

print("------------------------------------------------------------")  # 60個

from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)
X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

print("建立神經網路13")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))
model.add(Dense(128, activation="relu"))
model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

# 跑很久
"""
#history = model.fit(X_train, y_train, verbose=1, batch_size=32,epochs=3)
history = model.fit(X_train, y_train, verbose=1, batch_size=960,epochs=1)

plt.plot(history.history["accuracy"], label="accuracy")

plt.ylabel("accuracy")

plt.xlabel("epoch")

plt.legend(loc="best")

#plt.show()
"""
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路14")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, verbose=0)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

# evaluate loss: 0.0431341715157032
# evaluate acc: 0.9291999936103821

print("------------------------------------------------------------")  # 60個

from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路15")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, verbose=0)

for i in range(10):
    plt.subplot(1, 10, i + 1)
    plt.imshow(X_test[i].reshape((28, 28)), "gray")

# plt.show()

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

print("------------------------------------------------------------")  # 60個
"""
from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路16")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元
model.add(Dense(256, activation='sigmoid', input_dim=784))
model.add(Dense(128, activation='relu'))

#超參數設定(二)：加入Dropout層
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation='softmax'))

#超參數設定(三)：損失函數與優化器
sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
model.fit(X_train, y_train, verbose=0, batch_size=BATCH_SIZE, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2699148654937744
#evaluate acc: 0.9211999773979187

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路17")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

#超參數設定(一)：隱藏層的數量、隱藏層設計多少神經元

model.add(Dense(256, activation='sigmoid', input_dim=784))

# 比較參數

def funcA():
    model.add(Dense(128, activation='sigmoid'))

def funcB():
    model.add(Dense(128, activation='sigmoid'))
    model.add(Dense(128, activation='sigmoid'))
    model.add(Dense(128, activation='sigmoid'))

def funcC():
    model.add(Dense(1568, activation='sigmoid'))

# 選用模型A時就將B和C這兩行註解掉
# ---------------------------
funcA()

#funcB()

#funcC()

# ---------------------------

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=BATCH_SIZE, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2971647381782532
#evaluate acc: 0.9146999716758728

#15-3 超參數設定(二)：加入Dropout層

from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路18")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation='sigmoid', input_dim=784))

model.add(Dense(128, activation='relu'))

#超參數設定(二)：Dropout

#model.add(Dropout(rate=0.5))

model.add(Dense(10, activation='softmax'))

sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=BATCH_SIZE, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.25099998712539673
#evaluate acc: 0.9276999831199646

#15-4 超參數設定(三)：損失函數與優化器

from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路19")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation='sigmoid', input_dim=784))
model.add(Dense(128, activation='relu'))
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation='softmax'))

#超參數設定(三)：優化器與學習率

# 比較參數
# lr = 0.01/0.1/1.0
lr = 0.01

sgd = optimizers.SGD(learning_rate=lr)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd,loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(X_train, y_train, verbose=0, batch_size=BATCH_SIZE, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.2721501886844635

#evaluate acc: 0.9229000210762024

print('------------------------------------------------------------')	#60個
"""
from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路20")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))
model.add(Dense(128, activation="relu"))
model.add(Dropout(rate=0.5))
model.add(Dense(10, activation="softmax"))

sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# 比較參數
# BATCH_SIZE = 16 / 32 / 64

model.fit(X_train, y_train, verbose=0, batch_size=BATCH_SIZE, epochs=3)

score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

# evaluate loss: 0.2627638280391693
# evaluate acc: 0.92330002784729

print("------------------------------------------------------------")  # 60個

# 超參數設定(五)：epochs

from tensorflow.keras.layers import Dropout
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = X_train.reshape(X_train.shape[0], 784)

X_test = X_test.reshape(X_test.shape[0], 784)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路21")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(256, activation="sigmoid", input_dim=784))

model.add(Dense(128, activation="relu"))

model.add(Dropout(rate=0.5))

model.add(Dense(10, activation="softmax"))

sgd = optimizers.SGD(learning_rate=0.01)

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=sgd, loss="categorical_crossentropy", metrics=["accuracy"])

# 比較參數
# EOPCHS = 5/10/60

"""
#做很久
model.fit(X_train, y_train, verbose=1, batch_size=BATCH_SIZE, epochs=EOPCHS)
score = model.evaluate(X_test, y_test, verbose=0)

print("evaluate loss: {0[0]}\nevaluate acc: {0[1]}".format(score))

#evaluate loss: 0.23109018802642822

#evaluate acc: 0.9323999881744385
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# Final 使用 CNN 辨識手寫數字圖片

from tensorflow.keras.layers import Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import plot_model

(X_train, y_train), (X_test, y_test) = load_mnist_data()

# 訓練數據300張, 測試數據100張

# Conv層接收的是4軸維陣列(batch_size, 垂直尺寸, 水平尺寸, 顏色通道數)

# 因為MNIST中的數據是單通道, 含batch_size的話僅是三維數據, 所以要先轉換為四維數據

X_train = X_train.reshape(-1, 28, 28, 1)

X_test = X_test.reshape(-1, 28, 28, 1)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

print("建立神經網路22")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

# --------------------------------------------------------------

# 計算準確率

model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)))

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu"))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.5))

model.add(Flatten())

model.add(Dense(128, activation="relu"))

model.add(Dropout(0.5))

model.add(Dense(10, activation="softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

"""
#做很久
#model.fit(X_train, y_train, batch_size = 128, epochs=EPOCHS, verbose = 1)# 學習訓練.fit
model.fit(X_train, y_train, batch_size = 1280, epochs=EPOCHS, verbose = 1)# 學習訓練.fit

# 計算準確率
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 將前10張圖片畫出來
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i].reshape((28,28)), 'gray')

plt.suptitle("The first ten of the test data",fontsize=20)

#plt.show()

# 顯示前10張圖片的預測結果

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

print("檢視神經網路")
model.summary()  #檢視神經網路

"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 批次正規化

from tensorflow.keras.layers import (
    Activation,
    Conv2D,
    Dense,
    Flatten,
    MaxPooling2D,
    BatchNormalization,
)
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = load_mnist_data()

X_train = np.reshape(a=X_train, newshape=(-1, 28, 28, 1))

X_test = np.reshape(a=X_test, newshape=(-1, 28, 28, 1))

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 使用 ReLU 函數當做啟動函數

print("建立神經網路23")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(
    Conv2D(
        input_shape=(28, 28, 1),
        filters=32,
        kernel_size=(2, 2),
        strides=(1, 1),
        padding="same",
    )
)

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=32, kernel_size=(2, 2), strides=(1, 1), padding="same"))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dense(256))

# 批次正規化

model.add(BatchNormalization())

model.add(Activation("relu"))

model.add(Dense(128))

# 批次正規化

model.add(BatchNormalization())

model.add(Activation("relu"))

model.add(Dense(10))

model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

"""
# 執行訓練
# 做很久
# 學習訓練.fit
history = model.fit(X_train, y_train, batch_size=32, epochs=3, validation_data=(X_test, y_test))

# 做可視化處理

plt.plot(history.history['accuracy'], label='acc', ls='-', marker='o')

plt.plot(history.history['val_accuracy'], label='val_acc', ls='-', marker='x')

plt.ylabel('accuracy')

plt.xlabel('epoch')

plt.suptitle("model", fontsize=12)

#plt.show()
"""


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
使用 tensorflow + keras



"""

import os
import sys
import time
import math
import random

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

ESC = 27

import cv2
import numpy as np

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
model = tf.keras.models.load_model('keras_model.h5', compile=False)   # 載入 model
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
        print('oxxo')
    if b>0.9:
        print('維他命')
        
    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
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
        text('a')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('b')
    if c>0.9:
        text('c')
        
    cv2.imshow('ImageShow', img)
    
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 50)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

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
        text('剪刀')  # 使用 text() 函式，顯示文字
    if b>0.9:
        text('石頭')
    if c>0.9:
        text('布')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
model = tf.keras.models.load_model('keras_model.h5', compile=False)  # 載入模型
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
        text('ok~')
    if b>0.001:              # 判斷沒戴口罩
        text('no mask!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" NG 無檔案
from PIL import ImageFont, ImageDraw, Image  # 載入 PIL 相關函式庫

fontpath = 'NotoSansTC-Regular.otf'          # 設定字型路徑

model = tf.keras.models.load_model('keras_model_3.h5', compile=False)  # 載入模型
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)          # 設定資料陣列

def text(text):   # 建立顯示文字的函式
    global img    # 設定 img 為全域變數
    font = ImageFont.truetype(fontpath, 30)  # 設定字型與文字大小
    imgPil = Image.fromarray(img)            # 將 img 轉換成 PIL 影像
    draw = ImageDraw.Draw(imgPil)            # 準備開始畫畫
    draw.text((0, 0), text, fill=(255, 255, 255), font=font)  # 寫入文字
    img = np.array(imgPil)                   # 將 PIL 影像轉換成 numpy 陣列

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
        text('很乖')
    if b>0.001:
        text('沒戴口罩!!')

    cv2.imshow('ImageShow', img)
    k = cv2.waitKey(1)
    if k == ESC:
        break

cap.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist
from keras import utils

(x_train, y_train), (x_test, y_test) = load_mnist_data()

# 訓練集資料
x_train = x_train.reshape(x_train.shape[0], -1)  # 轉換資料形狀
x_train = x_train.astype("float32") / 255  # 轉換資料型別
y_train = y_train.astype(np.float32)

# 測試集資料
x_test = x_test.reshape(x_test.shape[0], -1)  # 轉換資料形狀
x_test = x_test.astype("float32") / 255  # 轉換資料型別
y_test = y_test.astype(np.float32)

knn = cv2.ml.KNearest_create()  # 建立 KNN 訓練方法
knn.setDefaultK(5)  # 參數設定
knn.setIsClassifier(True)
""" 久
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
"""
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

from keras.datasets import mnist
from keras.models import Sequential

# from keras.layers.core import Dense, Activation 改為以下
from tensorflow.python.keras.layers.core import Dense, Activation
from tensorflow.python.keras.utils import np_utils

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

classes = 10
Y_train = np_utils.to_categorical(Y_train, classes)
Y_test = np_utils.to_categorical(Y_test, classes)

input_size = 784
batch_size = BATCH_SIZE
hidden_neurons = 100

print("建立神經網路24")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(hidden_neurons, input_dim=input_size))
model.add(Activation("sigmoid"))
model.add(Dense(classes, input_dim=hidden_neurons))
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(loss="categorical_crossentropy", metrics=["accuracy"], optimizer="sgd")

""" long
# 共有N個樣品, 一次做 BATCH_SIZE 個, 一輪需要做 N / BATCH_SIZE 次
model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=1)
print('Test accuracy:', score[1]) 

weights = model.layers[0].get_weights()

import matplotlib.pyplot as plt     
import matplotlib.cm as cm 
import numpy

fig = plt.figure()
  
w = weights[0].T          
for neuron in range(hidden_neurons):         
    ax = fig.add_subplot(10, 10, neuron+1)
    ax.axis("off")
    ax.imshow(numpy.reshape(w[neuron], (28, 28)), cmap = cm.Greys_r)

plt.savefig("neuron_images.png", dpi=300)    
#plt.show()  
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# restricted_boltzmann_machine

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

tf.disable_v2_behavior()

# from tensorflow.examples.tutorials.mnist import input_data

VISIBLE_NODES = 784
HIDDEN_NODES = 400
LEARNING_RATE = 0.01

# mnist = input_data.read_data_sets("MNIST_data/")

(train_images, train_labels), (test_images, test_labels) = load_mnist_data()

input_placeholder = tf.placeholder("float", shape=(None, VISIBLE_NODES))

weights = tf.Variable(
    tf.random_normal(
        (VISIBLE_NODES, HIDDEN_NODES), mean=0.0, stddev=1.0 / VISIBLE_NODES
    )
)
hidden_bias = tf.Variable(tf.zeros([HIDDEN_NODES]))
visible_bias = tf.Variable(tf.zeros([VISIBLE_NODES]))

hidden_activation = tf.nn.sigmoid(tf.matmul(input_placeholder, weights) + hidden_bias)
visible_reconstruction = tf.nn.sigmoid(
    tf.matmul(hidden_activation, tf.transpose(weights)) + visible_bias
)

final_hidden_activation = tf.nn.sigmoid(
    tf.matmul(visible_reconstruction, weights) + hidden_bias
)

positive_phase = tf.matmul(tf.transpose(input_placeholder), hidden_activation)
negative_phase = tf.matmul(
    tf.transpose(visible_reconstruction), final_hidden_activation
)

weight_update = weights.assign_add(LEARNING_RATE * (positive_phase - negative_phase))
visible_bias_update = visible_bias.assign_add(
    LEARNING_RATE * tf.reduce_mean(input_placeholder - visible_reconstruction, 0)
)
hidden_bias_update = hidden_bias.assign_add(
    LEARNING_RATE * tf.reduce_mean(hidden_activation - final_hidden_activation, 0)
)

train_op = tf.group(weight_update, visible_bias_update, hidden_bias_update)

loss_op = tf.reduce_sum(tf.square(input_placeholder - visible_reconstruction))

session = tf.Session()  # tensorflow 1.0才有的指令

session.run(tf.initialize_all_variables())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist
from keras.models import Sequential

# from keras.layers.core import Dense, Activation 改為以下
from tensorflow.python.keras.layers.core import Dense, Activation
from tensorflow.python.keras.utils import np_utils

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

X_train = X_train.reshape(60000, 784)
X_test = X_test.reshape(10000, 784)

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255

classes = 10
Y_train = np_utils.to_categorical(Y_train, classes)
Y_test = np_utils.to_categorical(Y_test, classes)

input_size = 784
hidden_neurons = 400

print("建立神經網路25")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Dense(hidden_neurons, input_dim=input_size))
model.add(Activation("relu"))
model.add(Dense(classes, input_dim=hidden_neurons))
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(
    loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adadelta"
)
""" NG
model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=1)
print('Test accuracy:', score[1]) 
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.datasets import mnist

print("------------------------------------------------------------")  # 60個

from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Dropout, Flatten

from tensorflow.python.keras.utils import np_utils

input_size = 784
hidden_neurons = 200
classes = 10

(X_train, Y_train), (X_test, Y_test) = load_mnist_data()

X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000, 28, 28, 1)

X_train = X_train.astype("float32")
X_test = X_test.astype("float32")
X_train /= 255
X_test /= 255

Y_train = np_utils.to_categorical(Y_train, classes)
Y_test = np_utils.to_categorical(Y_test, classes)

print("建立神經網路26")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

model.add(Convolution2D(32, (3, 3), input_shape=(28, 28, 1)))
model.add(Activation("relu"))
model.add(Convolution2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(hidden_neurons))
model.add(Activation("relu"))
model.add(Dense(classes))
model.add(Activation("softmax"))

# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(
    loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adadelta"
)
""" 久
model.fit(X_train, Y_train, batch_size=BATCH_SIZE, epochs=EPOCHS, validation_split = 0.1, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=1)
print('Test accuracy:', score[1])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
To know more or get code samples, please visit my website:
https://morvanzhou.github.io/tutorials/
Or search: 莫烦Python
Thank you for supporting!
"""

# please note, all tutorial code are running under python3.5.
# If you use the version like python2.7, please modify the code accordingly

# 6 - CNN example

# to try tensorflow, un-comment following two lines
# import os
# os.environ['KERAS_BACKEND']='tensorflow'

import numpy as np

np.random.seed(1337)  # for reproducibility
from keras.datasets import mnist
from tensorflow.python.keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam  # 優化器

# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape (60,000 28x28), y shape (10,000, )
(X_train, y_train), (X_test, y_test) = load_mnist_data()

# data pre-processing
X_train = X_train.reshape(-1, 1, 28, 28) / 255.0
X_test = X_test.reshape(-1, 1, 28, 28) / 255.0
y_train = np_utils.to_categorical(y_train, num_classes=10)
y_test = np_utils.to_categorical(y_test, num_classes=10)

print("建立神經網路27")
model = Sequential()  # 建立空白的神經網路模型(CNN), 函數學習機, 簡單的線性執行的模型

# Conv layer 1 output shape (32, 28, 28)
model.add(
    Convolution2D(
        filters=32,
        kernel_size=(5, 5),
        # border_mode='same',     # Padding method
        # dim_ordering='th',      # if use tensorflow, to set the input dimension order to theano ("th") style, but you can change it.
        input_shape=(28, 28, 1),
    )
)

model.add(Activation("relu"))

# Pooling layer 1 (max pooling) output shape (32, 14, 14)
model.add(
    MaxPooling2D(
        pool_size=(2, 2),
        strides=(2, 2),
        # border_mode='same',    # Padding method
    )
)

# Conv layer 2 output shape (64, 14, 14)
model.add(Convolution2D(64, 5, 5))
model.add(Activation("relu"))

# Pooling layer 2 (max pooling) output shape (64, 7, 7)
model.add(MaxPooling2D(pool_size=(2, 2)))

# Fully connected layer 1 input shape (64 * 7 * 7) = (3136), output shape (1024)
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation("relu"))

# Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(10))
model.add(Activation("softmax"))

# Another way to define your optimizer(優化器)
adam = Adam(learning_rate=1e-4)

""" NG
# 組裝神經網路, 編譯模型 : 選擇損失函數、優化方法及成效衡量方式
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training ------------')
# Another way to train the model
model.fit(X_train, y_train, epoch=1, batch_size=BATCH_SIZE,)

print('\nTesting ------------')
# Evaluate the model with the metrics we defined earlier
loss, accuracy = model.evaluate(X_test, y_test)

print('\ntest loss: ', loss)
print('\ntest accuracy: ', accuracy)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""


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

import tensorflow as tf
import keras

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

print("------------------------------------------------------------")  # 60個


# 顯示資料內容
def printMatrixE(a):
    return
    rows = a.shape[0]
    cols = a.shape[1]
    for i in range(0, rows):
        str1 = ""
        for j in range(0, cols):
            str1 = str1 + ("%3.0f " % a[i, j])
        print(str1)
    print("")


print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist
# from tensorflow.examples.tutorials.mnist import input_data

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])
print("y_train[0] = " + str(y_train[0]))

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])

# 顯示其中的圖形
num = 0
plt.title("x_train[%d]  Label: %d" % (num, y_train[num]))
plt.imshow(x_train[num], cmap=plt.get_cmap("gray_r"))
# plt.show()

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])

# 顯示其中的圖形
num = 0
plt.title("x_train[%d]  Label: %d" % (num, y_train[num]))
plt.imshow(x_train[num], cmap=plt.get_cmap("gray_r"))
# plt.show()


def display_mult_flat(start, stop, label):
    images = x_train[start].reshape([1, 784])  # 784=28*28
    for i in range(start + 1, stop):
        label2 = int(y_train[i])
        if label == label2:
            images = np.concatenate((images, x_train[i].reshape([1, 28 * 28])))
    plt.imshow(images, cmap=plt.get_cmap("gray_r"))
    # plt.show()


display_mult_flat(0, 2000, 7)
display_mult_flat(0, 2000, 1)

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

from sklearn.datasets import load_digits

# 影像的類別數目
num_classes = 10

# 輸入的手寫影像解析度
img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("x_train before reshape:", x_train.shape)
# 將原始資料轉為正確的影像排列方式
dim = img_rows * img_cols * 1
x_train = x_train.reshape(x_train.shape[0], dim)
x_test = x_test.reshape(x_test.shape[0], dim)
print("x_train after reshape:", x_train.shape)

# 標準化輸入資料
print("x_train before div 255:", x_train[0][180:195])
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255
print("x_train before div 255 ", x_train[0][180:195])


print("y_train shape:", y_train.shape)
print(y_train[:10])
# 將數字轉為 One-hot 向量
category = 10
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)
print("y_train2 to_categorical shape=", y_train2.shape)  # 輸出 (60000, 10)
print(y_train2[:10])

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

from sklearn.datasets import load_digits

# 影像的類別數目
num_classes = 10

# 輸入的手寫影像解析度
img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("x_train before reshape:", x_train.shape)
# 將原始資料轉為正確的影像排列方式
dim = img_rows * img_cols * 1
x_train = x_train.reshape(x_train.shape[0], dim)
x_test = x_test.reshape(x_test.shape[0], dim)
print("x_train after reshape:", x_train.shape)

# 標準化輸入資料
print("x_train before div 255:", x_train[0][180:195])
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255
print("x_train before div 255 ", x_train[0][180:195])


print("y_train shape:", y_train.shape)
print(y_train[:10])
# 將數字轉為 One-hot 向量
category = 10
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)
print("y_train2 to_categorical shape=", y_train2.shape)  # 輸出 (60000, 10)
print(y_train2[:10])


# 建立模型
model = tf.keras.models.Sequential()
model.add(
    tf.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim)
)  # 784=28*28
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer=tf.keras.optimizers.Adam(lr=0.001),
    loss=tf.keras.losses.categorical_crossentropy,
    metrics=["accuracy"],
)
# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）

# 顯示模型
model.summary()

# 訓練模型
history = model.fit(
    x_train,
    y_train2,  # 進行訓練的因和果的資料
    batch_size=1000,  # 設定每次訓練的筆數
    epochs=200,  # 設定訓練的次數，也就是機器學習的次數
    verbose=1,
)

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)  # 計算測試正確率
print("score:", score)  # 輸出測試正確率
predict = model.predict(x_test)  # 取得每一個結果的機率
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)  # 取得預測答案1

# y_pred = model.predict_classes(x_test[:10]) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test[:10])
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred[:10])  # 輸出預測答案2
print("y_test", y_test[:10])  # 實際測試的果

print("------------------------------------------------------------")  # 60個

import tensorflow as tf
from sklearn.datasets import load_digits

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

from keras.datasets import fashion_mnist
from tensorflow.keras.datasets import mnist

# (x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# x_train=x_train[:1000]
# x_test=x_test[:1000]
# y_train=y_train[:1000]
# y_test=y_test[:1000]

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, 10)
y_test2 = tf.keras.utils.to_categorical(y_test, 10)

# 建立模型
model = tf.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(
    tf.keras.layers.Conv2D(
        filters=3,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)
# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))
# 2D 的 Convolution Layer
model.add(
    tf.keras.layers.Conv2D(
        filters=9, kernel_size=(2, 2), padding="same", activation="relu"
    )  # or filters=3
)
# Dropout Layer
model.add(tf.keras.layers.Dropout(rate=0.33))

# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())
# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(10, activation="relu"))

# or
# model.add(tf.keras.layers.Dense(50, activation="relu"))
# model.add(tf.keras.layers.Dense(50, activation="relu"))
# model.add(tf.keras.layers.Dense(50, activation="relu"))

# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(units=10, activation=tf.nn.softmax))

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)

model.summary()

model.fit(x_train, y_train2, batch_size=1024, epochs=20, verbose=1)

# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred)
print("y_test", y_test[:])

# 保存模型架構
with open("model.json", "w") as json_file:
    json_file.write(tmp_model.to_json())
# 保存模型權重
model.save_weights("tmp_model.h5")

print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_digits
from tensorflow.keras.callbacks import TensorBoard

# 影像的類別數目
category = 10

# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)


# 建立模型
model = tf.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)

model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# Dropout Layer
model.add(tf.keras.layers.Dropout(rate=0.01))

# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())
# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))

model.summary()

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")

history = model.fit(x_train, y_train2, batch_size=100, epochs=400, verbose=1)
# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred[:20])
print("y_test", y_test[:20])

import matplotlib.pyplot as plt

plt.plot(history.history["acc"])
plt.plot(history.history["loss"])
plt.title("model accuracy")
plt.ylabel("acc & loss")
plt.xlabel("epoch")
plt.legend(["acc", "loss"], loc="upper left")
# plt.show()

# 保存模型架構
with open("model.json", "w") as json_file:
    json_file.write(tmp_model.to_json())
# 保存模型權重
model.save_weights("tmp_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import load_digits
from tensorflow.keras.callbacks import TensorBoard

# 影像的類別數目
category = 10


# 載入資料（將資料打散，放入 train 與 test 資料集）
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# 將原始資料轉為正確的影像排列方式
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)


# 標準化輸入資料
x_train = x_train.astype("float32")
x_test = x_test.astype("float32")
x_train /= 255
x_test /= 255

print("x_train shape:", x_train.shape)
print(x_train.shape[0], "train samples")
print(x_test.shape[0], "test samples")

# 將數字轉為 One-hot 向量
y_train2 = tf.keras.utils.to_categorical(y_train, category)
y_test2 = tf.keras.utils.to_categorical(y_test, category)


# 建立模型
model = tf.keras.models.Sequential()

# 加入 2D 的 Convolution Layer，接著一層 ReLU 的 Activation 函數
model.add(
    tf.keras.layers.Conv2D(
        filters=32,
        kernel_size=(3, 3),
        padding="same",
        activation="relu",
        input_shape=(28, 28, 1),
    )
)

model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# 2D 的 Max-Pooling Layer
model.add(tf.keras.layers.MaxPool2D(pool_size=(2, 2)))

# 2D 的 Convolution Layer
model.add(
    tf.keras.layers.Conv2D(
        filters=40, kernel_size=(2, 2), padding="same", activation="relu"
    )
)

# Dropout Layer
model.add(tf.keras.layers.Dropout(rate=0.01))

# 將 2D 影像轉為 1D 向量
model.add(tf.keras.layers.Flatten())
# 連接 Fully Connected Layer，接著一層 ReLU 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
# 連接 Fully Connected Layer，接著一層 Softmax 的 Activation 函數
model.add(tf.keras.layers.Dense(units=category, activation=tf.nn.softmax))

model.summary()

# 設定模型的 Loss 函數、Optimizer 以及用來判斷模型好壞的依據（metrics）
model.compile(
    loss=tf.keras.losses.categorical_crossentropy,
    optimizer=tf.keras.optimizers.Adadelta(),
    metrics=["accuracy"],
)

tensorboard = TensorBoard(log_dir="logs")
# 訓練模型


gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rotation_range=8,
    width_shift_range=0.08,
    shear_range=0.3,
    height_shift_range=0.08,
    zoom_range=0.08,
)


train_generator = gen.flow(x_train, y_train2, batch_size=64)
train_generator = gen.flow(x_train, y_train2, batch_size=128)
# 讀取模型架構
try:
    with open("model_ImageDataGenerator.h5", "r") as load_weights:
        # 讀取模型權重
        model.load_weights("model_ImageDataGenerator.h5")

except IOError:
    print("File not accessible")

checkpoint = tf.keras.callbacks.ModelCheckpoint(
    "tmp_model_ImageDataGenerator.h5",
    monitor="accuracy",
    verbose=1,
    save_best_only=True,
    mode="auto",
    save_freq=1,
)

# 保存模型架構
with open("tmp_model_ImageDataGenerator.json", "w") as json_file:
    json_file.write(model.to_json())

history = model.fit(train_generator, callbacks=[checkpoint], epochs=400)
""" 
history=model.fit(x_train, y_train2,
          batch_size=10000,
          epochs=400,
          verbose=1)
"""
# history = model.fit_generator(train_generator, y_train2, epochs=400)
history = model.fit(train_generator, epochs=400)


# 測試
score = model.evaluate(x_test, y_test2, batch_size=128)
# 輸出結果
print("score:", score)

predict = model.predict(x_test)
print(
    "Ans:",
    np.argmax(predict[0]),
    np.argmax(predict[1]),
    np.argmax(predict[2]),
    np.argmax(predict[3]),
)

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x

print("predict_classes:", y_pred[:20])
print("y_test", y_test[:20])

import matplotlib.pyplot as plt

plt.plot(history.history["acc"])
plt.plot(history.history["loss"])
plt.title("model accuracy")
plt.ylabel("acc & loss")
plt.xlabel("epoch")
plt.legend(["acc", "loss"], loc="upper left")
plt.show()


# 保存模型架構
with open("tmp_model_img.json", "w") as json_file:
    json_file.write(model.to_json())
# 保存模型權重
model.save_weights("tmp_model_img.h5")

# 保存模型架構
with open("tmp_model.json", "w") as json_file:
    json_file.write(model.to_json())
# 保存模型權重
model.save_weights("tmp_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 提示：generate code with tensorflow mnist
import tensorflow as tf
from tensorflow import keras

# Load the dataset
mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess the data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Define the model architecture
model = keras.models.Sequential(
    [
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation="relu"),
        keras.layers.Dense(10, activation="softmax"),
    ]
)

# Compile the model
model.compile(
    optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"]
)

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Test accuracy:", test_acc)


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

# y_pred = model.predict_classes(x_test) # TensorFlow2.6已刪除predict_classes()
predict_x = model.predict(x_test)
classes_x = np.argmax(predict_x, axis=1)
y_pred = classes_x


# 我們 "predict" 放的是我們神經網路的學習結果。
# 這裡用 predict_classes 會讓我們 Keras 選 10 個輸出機率最大的那類。

# 方法一 將minst資料集放在 系統 位置
# 下載minst資料集檔案
# 資料集檔案位置: C:/Users/070601/.keras/datasets/mnist.npz
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 方法二 將minst資料集放在 特定 位置
mnist = np.load(mnist_npz_filename)

"""
Dense        全連接層
Conv2D       二維卷積層
MaxPooling2D 最大池化層
Dropout      隨機失活層

"""


