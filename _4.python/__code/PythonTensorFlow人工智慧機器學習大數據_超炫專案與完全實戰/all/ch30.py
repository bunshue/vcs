"""

keras

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

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist
# from tensorflow.examples.tutorials.mnist import input_data

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])
print("y_train[0] = " + str(y_train[0]))

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])

# 顯示其中的圖形
num = 0
plt.title("x_train[%d]  Label: %d" % (num, y_train[num]))
plt.imshow(x_train[num], cmap=plt.get_cmap("gray_r"))
plt.show()

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

printMatrixE(x_train[0])

# 顯示其中的圖形
num = 0
plt.title("x_train[%d]  Label: %d" % (num, y_train[num]))
plt.imshow(x_train[num], cmap=plt.get_cmap("gray_r"))
plt.show()


def display_mult_flat(start, stop, label):
    images = x_train[start].reshape([1, 784])  # 784=28*28
    for i in range(start + 1, stop):
        label2 = int(y_train[i])
        if label == label2:
            images = np.concatenate((images, x_train[i].reshape([1, 28 * 28])))
    plt.imshow(images, cmap=plt.get_cmap("gray_r"))
    plt.show()


display_mult_flat(0, 2000, 7)
display_mult_flat(0, 2000, 1)

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

from sklearn.datasets import load_digits

# 影像的類別數目
num_classes = 10

# 輸入的手寫影像解析度
img_rows, img_cols = 28, 28

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
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
y_train2 = tf.contrib.keras.utils.to_categorical(y_train, category)
y_test2 = tf.contrib.keras.utils.to_categorical(y_test, category)
print("y_train2 to_categorical shape=", y_train2.shape)  # 輸出 (60000, 10)
print(y_train2[:10])

print("------------------------------------------------------------")  # 60個

# from tensorflow.examples.tutorials.mnist

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
print("x_train = " + str(x_train.shape))
print("y_train = " + str(y_train.shape))

from sklearn.datasets import load_digits

# 影像的類別數目
num_classes = 10

# 輸入的手寫影像解析度
img_rows, img_cols = 28, 28

# 載入資料（將資料打散，放入 train 與 test 資料集）
# (x_train, y_train), (x_test, y_test) = tf.contrib.keras.datasets.mnist.load_data()
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
y_train2 = tf.contrib.keras.utils.to_categorical(y_train, category)
y_test2 = tf.contrib.keras.utils.to_categorical(y_test, category)
print("y_train2 to_categorical shape=", y_train2.shape)  # 輸出 (60000, 10)
print(y_train2[:10])


# 建立模型
model = tf.contrib.keras.models.Sequential()
model.add(
    tf.contrib.keras.layers.Dense(units=10, activation=tf.nn.relu, input_dim=dim)
)  # 784=28*28
model.add(tf.contrib.keras.layers.Dense(units=10, activation=tf.nn.relu))
model.add(tf.contrib.keras.layers.Dense(units=category, activation=tf.nn.softmax))
model.compile(
    optimizer=tf.keras.optimizers.Adam(lr=0.001),
    loss=tf.contrib.keras.losses.categorical_crossentropy,
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
predict2 = model.predict_classes(x_test[:10])  # 取得預測答案2
print("predict_classes:", predict2[:10])  # 輸出預測答案2
print("y_test", y_test[:10])  # 實際測試的果

print("------------------------------------------------------------")  # 60個
