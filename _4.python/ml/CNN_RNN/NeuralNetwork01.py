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

import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

print("------------------------------------------------------------")  # 60個
'''
"""
在金融預測上的應用
神經網路
連 SVM 都沒辦法, 那一定是方法還不夠高級, 所以我們用更高級的神經網路來做做看!
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

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Final 用 tf.Keras 建構 CNN 模型

from tensorflow.keras.layers import Activation, Dense, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.models import load_model
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

# Final 使用 CNN 辨識 cifar10 圖片資料集

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dropout, Flatten, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import load_model
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

print("建立神經網路15")
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
#model.fit(X_train, y_train, batch_size=128, epochs=10, validation_split=0.2)# 學習訓練.fit
model.fit(X_train, y_train, batch_size=1280, epochs=1, validation_split=0.2)# 學習訓練.fit

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

print("檢視神經網路")
model.summary()  #檢視神經網路

"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 標準化

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

plt.suptitle("The original image", fontsize=12)
plt.show()

# 建立 ImageDataGenerator 的操作物件

datagen = ImageDataGenerator(samplewise_center=True, samplewise_std_normalization=True)

# 進行標準化

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), X_batch.max())

X_batch += 127.0

X_batch = X_batch.astype("uint8")

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle("Standardization result", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個

# 白化

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

plt.suptitle("The original image", fontsize=12)

plt.show()

# 建立ImageDataGenerator的操作物件

datagen = ImageDataGenerator(zca_whitening=True)

# 白化處理

datagen.fit(X_train)  # 學習訓練.fit

g = datagen.flow(X_train, y_train, shuffle=False)

X_batch, y_batch = g.next()

# 讓生成的圖像效果, 看起來更明顯

X_batch *= 127.0 / max(abs(X_batch.min()), abs(X_batch.max()))

X_batch += 127

X_batch = X_batch.astype("uint8")

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(X_batch[i])

plt.suptitle("Whitening result", fontsize=12)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 遷移學習

# 下載VGG16有問題

"""
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dropout, Flatten, Input
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
# 學習訓練.fit
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

import numpy

from keras.datasets import cifar10
from keras.models import Sequential

# from keras.layers.core import Dense, Activation 改為以下
from tensorflow.python.keras.layers.core import Dense, Activation
from keras.layers import Convolution2D, MaxPooling2D, Flatten
from keras.layers import Dropout
from tensorflow.python.keras.utils import np_utils

batch_size = 100
hidden_neurons = 200
classes = 10
epochs = 20

(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()
"""
下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下
"""

Y_train = np_utils.to_categorical(Y_train, classes)
Y_test = np_utils.to_categorical(Y_test, classes)

model = Sequential()
model.add(Convolution2D(32, (3, 3), input_shape=(32, 32, 3)))
model.add(Activation("relu"))
model.add(Convolution2D(32, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(Convolution2D(64, (3, 3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(hidden_neurons))
model.add(Activation("relu"))
model.add(Dropout(0.5))
model.add(Dense(classes))
model.add(Activation("softmax"))

model.compile(
    loss="categorical_crossentropy", metrics=["accuracy"], optimizer="adadelta"
)

model.fit(
    X_train,
    Y_train,
    batch_size=batch_size,
    epochs=epochs,
    validation_split=0.1,
    verbose=1,
)

score = model.evaluate(X_test, Y_test, verbose=1)
print("Test accuracy:", score[1])

numpy.set_printoptions(threshold="nan")
index = 0
for layer in model.layers:
    filename = "conv_layer_" + str(index)
    f1 = open(filename, "w+")
    f1.write(repr(layer.get_weights()))
    f1.close()
    print(filename + " has been opened and closed")
    index = index + 1


print("------------------------------------------------------------")  # 60個
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
