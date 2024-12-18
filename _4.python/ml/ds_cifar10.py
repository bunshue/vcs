"""
cifar10

CIFAR-10資料集，又稱加拿大高等研究院資料集（Canadian Institute for Advanced Research）
是一個常用於訓練機器學習和電腦視覺演算法的圖像集合。

CIFAR-10資料集包含60,000張32×32像素的彩色圖像，分為10個不同的類別。
這10個類別分別是飛機、汽車、鳥類、貓、鹿、狗、青蛙、馬、船和卡車，
每個類別有6,000張圖片。

下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras\datasets/之下



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

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個


# Final 使用 CNN 辨識 cifar10 圖片資料集

from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
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

plt.suptitle("The first ten of the test data")
show()

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

plt.suptitle("The original image")
show()

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

plt.suptitle("Standardization result")

show()

print("------------------------------------------------------------")  # 60個
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

plt.suptitle("The original image")

show()

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

plt.suptitle("Whitening result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個



# 遷移學習

# 下載VGG16有問題

"""
from tensorflow.keras import optimizers
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers Flatten
from tensorflow.keras.layers Input
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
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

plt.suptitle("The first ten of the test data")

show()

# 前10張的預測結果
pred = np.argmax(model.predict(X_test[0:10]), axis=1)

print(pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from keras.datasets import cifar10
from keras.models import Sequential

from tensorflow.python.keras.layers.core import Dense
from tensorflow.python.keras.layers.core import Activation
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
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

np.set_printoptions(threshold="nan")
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
