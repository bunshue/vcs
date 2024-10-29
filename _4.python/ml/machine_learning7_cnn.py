"""

必學！Python 資料科學‧機器學習最強套件 CNN 1


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

plt.title("The original image", fontsize=12)

plt.show()

# 參考過濾器W2和W3, 來設置程式碼中的過濾器W1, 使其具有檢測垂直線條的能力

W1 = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])

W2 = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])

W3 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

W4 = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])

plt.subplot(1, 4, 1)
plt.imshow(W1)
plt.subplot(1, 4, 2)
plt.imshow(W2)
plt.subplot(1, 4, 3)
plt.imshow(W3)
plt.subplot(1, 4, 4)
plt.imshow(W4)
plt.suptitle("kernel", fontsize=12)
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

plt.subplot(1, 4, 1)
plt.imshow(C1)
plt.subplot(1, 4, 2)
plt.imshow(C2)
plt.subplot(1, 4, 3)
plt.imshow(C3)
plt.subplot(1, 4, 4)
plt.imshow(C4)

plt.suptitle("Convolution result", fontsize=12)

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

plt.title("The original image", fontsize=12)

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

plt.subplot(1, 4, 1)
plt.imshow(C1)
plt.subplot(1, 4, 2)
plt.imshow(C2)
plt.subplot(1, 4, 3)
plt.imshow(C3)
plt.subplot(1, 4, 4)
plt.imshow(C4)

plt.suptitle("Convolution result", fontsize=12)

plt.show()

# 最大池化運算

pool = Pool(2)

P1 = pool.f_prop(C1)

P2 = pool.f_prop(C2)

P3 = pool.f_prop(C3)

P4 = pool.f_prop(C4)

plt.subplot(1, 4, 1)
plt.imshow(P1)

plt.subplot(1, 4, 2)
plt.imshow(P2)

plt.subplot(1, 4, 3)
plt.imshow(P3)

plt.subplot(1, 4, 4)
plt.imshow(P4)

plt.suptitle("Pooling result", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

# Final 用 tf.Keras 建構 CNN 模型

from tensorflow.keras.layers import Activation, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical

# 建立模型物件
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
model.summary()

# Final 使用 CNN 辨識手寫數字圖片

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import plot_model

# 下載數據

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

# 訓練數據300張, 測試數據100張

# Conv層接收的是4軸維陣列(batch_size, 垂直尺寸, 水平尺寸, 顏色通道數)

# 因為MNIST中的數據是單通道, 含batch_size的話僅是三維數據, 所以要先轉換為四維數據

X_train = X_train.reshape(-1, 28, 28, 1)

X_test = X_test.reshape(-1, 28, 28, 1)

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 建立模型物件

model = Sequential()

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

# --------------------------------------------------------------
model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

"""
#做很久
#model.fit(X_train, y_train, batch_size = 128, epochs = 5, verbose = 1)
model.fit(X_train, y_train, batch_size = 1280, epochs = 1, verbose = 1)

# 計算準確率
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 將前10張圖片畫出來
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i].reshape((28,28)), 'gray')

plt.suptitle("The first ten of the test data",fontsize=20)

plt.show()

# 顯示前10張圖片的預測結果

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

model.summary()

"""

print("------------------------------------------------------------")  # 60個

# Final 使用 CNN 辨識 cifar10 圖片資料集

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dense, Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import plot_model

# 下載數據
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""

X_train = X_train

X_test = X_test

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 建立模型物件

model = Sequential()

model.add(
    Conv2D(32, (3, 3), padding="same", activation="relu", input_shape=X_train.shape[1:])
)
model.add(Conv2D(32, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))

# 編譯模型
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

"""
# 訓練模型 做很久
#model.fit(X_train, y_train, batch_size=128, epochs=10, validation_split=0.2)
model.fit(X_train, y_train, batch_size=1280, epochs=1, validation_split=0.2)

# 計算準確率
scores = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 將測試集前10張圖片畫出來
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i])

plt.suptitle("The first ten of the test data",fontsize=20)
plt.show()

# 顯示測試集前10張圖片的答案
labels = np.argmax(y_test[:10],axis=1)

print(labels)

# 顯示測試集前10張圖片的預測結果

pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)

model.summary()

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
'''
#標準化

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i])

plt.suptitle('The original image', fontsize=12)
plt.show()

# 建立 ImageDataGenerator 的操作物件

datagen = ImageDataGenerator(samplewise_center=True, 
                samplewise_std_normalization=True)

# 進行標準化

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), X_batch.max())

X_batch += 127.0

X_batch = X_batch.astype('uint8')

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle('Standardization result', fontsize=12)

plt.show()

print('------------------------------------------------------------')	#60個

#白化

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator

(X_train, y_train), (X_test, y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""

X_train = X_train[:300]

X_test = X_test[:100]

y_train = y_train[:300]

y_test = y_test[:100]

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_train[i])

plt.suptitle('The original image', fontsize=12)

plt.show()

# 建立ImageDataGenerator的操作物件

datagen = ImageDataGenerator(zca_whitening=True)

# 白化處理

datagen.fit(X_train)

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), abs(X_batch.max()))

X_batch += 127

X_batch = X_batch.astype('uint8')

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle('Whitening result', fontsize=12)

plt.show()
'''
print("------------------------------------------------------------")  # 60個

# 批次正規化

from tensorflow.keras.datasets import mnist
from tensorflow.keras.layers import (
    Activation,
    Conv2D,
    Dense,
    Flatten,
    MaxPooling2D,
    BatchNormalization,
)
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical

# (X_train, y_train), (X_test, y_test) = mnist.load_data() 改成以下4行
mnist = np.load(mnist_npz_filename)
X_train, y_train = mnist["x_train"], mnist["y_train"]
X_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()

X_train = np.reshape(a=X_train, newshape=(-1, 28, 28, 1))

X_test = np.reshape(a=X_test, newshape=(-1, 28, 28, 1))

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 使用 ReLU 函數當做啟動函數

model = Sequential()

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

# 執行compile
model.compile(optimizer="sgd", loss="categorical_crossentropy", metrics=["accuracy"])

"""
# 執行訓練
# 做很久
history = model.fit(X_train, y_train, batch_size=32, epochs=3, validation_data=(X_test, y_test))

# 做可視化處理

plt.plot(history.history['accuracy'], label='acc', ls='-', marker='o')

plt.plot(history.history['val_accuracy'], label='val_acc', ls='-', marker='x')

plt.ylabel('accuracy')

plt.xlabel('epoch')

plt.suptitle("model", fontsize=12)

plt.show()
"""

print("------------------------------------------------------------")  # 60個

# 遷移學習

# 下載VGG16有問題

"""
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

#下載
#https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
#將檔案改名成
#cifar-10-batches-py.tar.gz
#放在C:/Users/070601/.keras/datasets/之下

y_train = to_categorical(y_train)

y_test = to_categorical(y_test)

# 定義輸入形式

input_tensor = Input(shape=(32, 32, 3))

vgg16 = VGG16(include_top=False, weights='imagenet', input_tensor=input_tensor)

top_model = vgg16.output

top_model = Flatten(input_shape=vgg16.output_shape[1:])(top_model)

top_model = Dense(256, activation='sigmoid')(top_model)

top_model = Dropout(0.5)(top_model)

top_model = Dense(10, activation='softmax')(top_model)

# 將vgg16和top_model做連接, 建構出 model 模型

model = Model(inputs=vgg16.input, outputs=top_model)

# 將前19層的權重固定住, 不做訓練
for layer in model.layers[:19]:
    layer.trainable = False

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 訓練批量是32, epoch是3
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=32, epochs=5)

# 評估準確度

scores = model.evaluate(X_test, y_test, verbose=1)

print('Test loss:', scores[0])
print('Test accuracy:', scores[1])

# 對前10張做可視化處理
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_test[i])

plt.suptitle("The first ten of the test data",fontsize=16)

plt.show()

# 前10張的預測結果
pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)
"""
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
