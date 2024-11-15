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
import tensorflow as tf

print("------------------------------------------------------------")  # 60個
"""
print("畫出 mnist 數據集訓練資料的前10筆... 久")

(train_feature, train_label), (test_feature, test_label) = mnist.load_data()


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
    plt.show()


show_images_labels_predictions(train_feature, train_label, 0, 10)
"""
print("------------------------------------------------------------")  # 60個
'''
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

print("畫出 mnist 數據集訓練資料的前256筆... 久")

# MNIST手寫數字辨識資料集
# MNIST資料集是由60,000筆 訓練資料 train data
# 10,000筆 測試資料 test data 所組成

# 方法一 將minst資料集放在 系統 位置
# 下載minst資料集檔案
# 資料集檔案位置：C:/Users/070601/.keras/datasets/mnist.npz
(x_train, y_train), (x_test, y_test) = mnist.load_data()

"""
#方法二 將minst資料集放在 特定 位置
mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()
"""

# 查看 mnist資料集 內容
# 訓練資料 : (60000, 28, 28) #共60000張圖片資料，圖片像素28*28
# 測試資料 : (10000, 28, 28) #共10000張圖片資料，圖片像素28*28

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
plt.show()
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# https://waternotetw.blogspot.com/2018/03/keras-mnist.html

# 匯入Keras及相關模組
# 匯入keras.utils因為後續要將label標籤轉換為One-hotencoding
from tensorflow.python.keras.utils import np_utils

# (x_train, y_train), (x_test, y_test) = mnist.load_data()
(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

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
    plt.show()  # 顯示圖片


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
    plt.show()  # 開始繪圖


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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# (x_train, y_train), (x_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

x_train = x_train / 255
x_test = x_test / 255

from tensorflow.python.keras.utils import np_utils

y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.optimizers import SGD

model = Sequential()  # 建立模型, 函數學習機
model.add(Flatten(input_shape=(28, 28)))
model.add(Dense(20, activation="relu"))
model.add(Dense(80, activation="relu"))
model.add(Dense(100, activation="relu"))
model.add(Dense(160, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss="mse", optimizer=SGD(learning_rate=0.087), metrics=["accuracy"])

# 學習訓練.fit
# 共有N個樣品, 一次做 batch_size 個, 一輪需要做 N / batch_size 次
# model.fit(x_train, y_train, batch_size = 100, epochs = 20)  # 學習訓練.fit
model.fit(x_train, y_train, batch_size=2000, epochs=1)  # 遞迴 epochs 次# 學習訓練.fit

print(y_train[33])
# array([0., 0., 0., 0., 0., 0., 0., 0., 0., 1.], dtype = float32)

print(y_test[2])
# array([0., 1., 0., 0., 0., 0., 0., 0., 0., 0.], dtype = float32)

print("預測")
print(model.predict(np.array([x_test[87]])))
# print(model.predict_classes(np.array([x_test[87]])))
# array([3])

print("預測")
# predict = model.predict_classes(x_test)
predict = model.predict_step(x_test)

print(predict)

# array([7, 2, 1, ..., 4, 5, 6])


def test(測試編號):
    plt.imshow(x_test[測試編號], cmap="Greys")
    print("神經網路判斷為:", predict[測試編號])


test(1287)

plt.show()

# 神經網路判斷為: 8

"""
# 久
score = model.evaluate(x_test, y_test)

print("loss:", score[0])
print("正確率", score[1])

# loss: 0.01081830496697512
# 正確率 0.9308000206947327
"""

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
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

from tensorflow.keras.datasets import mnist

# 載入 MNIST 資料集, 如果是第一次載入會自行下載資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 顯示 Numpy 二維陣列內容
print(X_train[0])
print(Y_train[0])  # 標籤資料

plt.imshow(X_train[0], cmap="gray")
plt.title("顯示數字圖片 Label: " + str(Y_train[0]))
plt.axis("off")

plt.show()


sub_plot = 330
for i in range(0, 9):
    ax = plt.subplot(sub_plot + i + 1)
    ax.imshow(X_train[i], cmap="gray")
    ax.set_title("Label: " + str(Y_train[i]))
    ax.axis("off")

plt.subplots_adjust(hspace=0.5)
plt.title('前9張圖')
plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Dropout
from tensorflow.keras.utils import to_categorical

# 載入資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# 將圖片轉換成 4D 張量
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype("float32")
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1).astype("float32")

# 因為是固定範圍, 所以執行正規化, 從 0-255 至 0-1
X_train = X_train / 255
X_test = X_test / 255

# One-hot編碼
Y_train = to_categorical(Y_train)
Y_test = to_categorical(Y_test)

model = Sequential()  # 建立模型, 函數學習機
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
model.add(Dense(10, activation="softmax"))

cc = model.summary()  # 顯示模型摘要資訊
print(cc)

# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 學習訓練.fit
# 共有N個樣品, 一次做 batch_size 個, 一輪需要做 N / batch_size 次
history = model.fit(
    X_train, Y_train, validation_split=0.2, epochs=1, batch_size=2000, verbose=2
)  # 遞迴 epochs 次# 學習訓練.fit
  
# 評估模型
loss, accuracy = model.evaluate(X_train, Y_train, verbose=0)
print("訓練資料集的準確度 = {:.2f}".format(accuracy))
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

plt.show()

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

plt.show()

# 載入資料集
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
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
plt.show()

# (-0.5, 27.5, 27.5, -0.5)

# 預測結果的機率
probs = model.predict(X_test_digit, batch_size=1)[0]
print(probs)
plt.title("Probabilities for Each Digit Class")
plt.bar(np.arange(10), probs.reshape(10), align="center")
plt.xticks(np.arange(10), np.arange(10).astype(str))

plt.show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.datasets import mnist

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("訓練資料長度 :", len(x_train))
print("測試資料長度 :", len(x_test))

n = 1234
print("看第", n, "筆訓練資料")
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

print("看第", n, "筆訓練資料")
print("轉換後的目標 :", y_train[n])

print("建立 3 層神經網路 100 100 100")

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

model = Sequential()  # 建立模型, 函數學習機
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
# print(y_pred)

n = 1234

plt.imshow(x_test[n].reshape(28, 28), cmap="Greys")
plt.show()

print("神經網路預測第", n, "筆訓練資料")
print(y_pred[n])
print(y_pred[n].shape)

plt.plot(y_pred[n])
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

model = Sequential()  # 建立模型, 函數學習機

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
    epochs=1,
    batch_size=2000,
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

model = Sequential()  # 建立模型, 函數學習機

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
    batch_size=2000,
    verbose=2,
)

# 評估準確率
scores = model.evaluate(test_feature_normalize, test_label_onehot)
print("\n準確率=", scores[1])

print("將 模型存檔 存成 h5")
model.save("tmp_Mnist_mlp_model.h5")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("讀取模型, 並使用之")

from tensorflow.keras.models import load_model

model = load_model("tmp_mnist_mlp_model.h5")

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
"""
參考 https://ithelp.ithome.com.tw/m/articles/10191404
有說明
"""
# 導入函式庫
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten

# from keras.utils import np_utils  # 用來後續將 label 標籤轉為 one-hot-encoding
from tensorflow.python.keras.utils import np_utils

from matplotlib import pyplot as plt

# 載入 MNIST 資料庫的訓練資料，並自動分為『訓練組』及『測試組』
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 建立簡單的線性執行的模型
model = Sequential()  # 建立模型, 函數學習機
# Add Input layer, 隱藏層(hidden layer) 有 256個輸出變數
model.add(
    Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu")
)
# Add output layer
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

# 編譯: 選擇損失函數、優化方法及成效衡量方式
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
# 共有N個樣品, 一次做 batch_size 個, 一輪需要做 N / batch_size 次
model.fit(x=x_Train_norm, y=y_TrainOneHot, validation_split=0.2, epochs=1, batch_size=8000, verbose=2)
# 遞迴 epochs 次# 學習訓練.fit

# 顯示訓練成果(分數)
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
