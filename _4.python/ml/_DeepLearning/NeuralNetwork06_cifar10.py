"""
cifar10

The CIFAR-10 dataset 資料集網站

https://www.cs.toronto.edu/~kriz/cifar.html

CIFAR-10資料集，又稱加拿大高等研究院資料集（Canadian Institute for Advanced Research）
是一個常用於訓練機器學習和電腦視覺演算法的圖像集合。

CIFAR-10資料集包含60,000張32×32像素的彩色圖像，分為10個不同的類別。
這10個類別分別是飛機、汽車、鳥類、貓、鹿、狗、青蛙、馬、船和卡車，
每個類別有6,000張圖片。

下載
https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz

# old
將檔案改名成
cifar-10-batches-py.tar.gz
放在C:/Users/070601/.keras/datasets/之下

# new
將檔案改名成並放在:
C:/Users/070601/.keras/datasets/cifar-10-batches-py-target_archive

抓取檔案程式在:
C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/keras/src/utils/file_utils.py

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from sklearn import datasets
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from tensorflow.keras.datasets import cifar10


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
https://ithelp.ithome.com.tw/articles/10248873
Day 20 ~ AI從入門到放棄 - 新的資料集
Day 21 ~ AI從入門到放棄 - 訓練模型
"""

"""
今天要介紹給大家的資料集是cifar10，
資料集內含10個類別的圖片，分別是飛機、汽車、鳥、貓、鹿、狗、青蛙、馬、船、卡車，
其與mnist的主要不同之處在於維度，
cifar10是彩色圖片的資料集，有三個channel，
mnist的黑白圖片僅有一個channel，
我們先透過keras載入這個資料集，並看看它的shape如何。
"""

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(r"x_train.shape = ", x_train.shape)
print(r"y_train.shape = ", y_train.shape)
print(r"x_test.shape = ", x_test.shape)
print(r"y_test.shape = ", y_test.shape)

"""
一共有60000張32X32大小的彩色圖片，被分成50000張的訓練集跟10000張的測試集，每個類別有6000張圖片，已經被依照比例分配至訓練集和測試集。

需要注意的是channel的先後問題，如果你有自己製作或在網路下載別人的資料集，需要注意資料集的shape，分為channels_first與channels_last兩種，tensorflow預設為channels_last，以cifar10作為例子，為大家展示這兩種shape的不同。
"""
channels_first = (60000, 3, 32, 32)
channels_last = (60000, 32, 32, 3)

text = ["飛機", "汽車", "鳥", "貓", "鹿", "狗", "青蛙", "馬", "船", "卡車"]
plt.figure(figsize=(16, 10), facecolor="w")
for i in range(5):
    for j in range(8):
        index = random.randrange(0, 50000)
        plt.subplot(5, 8, i * 8 + j + 1)
        plt.title("label: {}".format(text[y_train[index][0]]))
        plt.imshow(x_train[index])
        plt.axis("off")

show()

# 我們明天來開始對付這個資料集，它還有一個cifar100的兄弟，大家可以去搜尋看看。

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = cifar10.load_data()
x_train = x_train / 255
x_test = x_test / 255

from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

from tensorflow.keras.models import Sequential

model = Sequential()

from tensorflow.keras.layers import Conv2D, Dense, Dropout, Flatten, MaxPool2D

model.add(
    Conv2D(
        filters=64,
        input_shape=(32, 32, 3),
        kernel_size=(3, 3),
        strides=(1, 1),
        padding="same",
        activation="relu",
    )
)

model.add(MaxPool2D(pool_size=(2, 2)))

model.add(
    Conv2D(
        filters=64,
        kernel_size=(3, 3),
        strides=(1, 1),
        padding="same",
        activation="relu",
    )
)

model.add(MaxPool2D(pool_size=(2, 2)))

model.add(
    Conv2D(
        filters=64,
        kernel_size=(3, 3),
        strides=(1, 1),
        padding="same",
        activation="relu",
    )
)

model.add(MaxPool2D(pool_size=(2, 2)))

model.add(Flatten())

model.add(Dropout(rate=0.2))

model.add(Dense(units=10, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

print("檢視模型架構")
model.summary()  # 檢視模型架構

from tensorflow.keras.callbacks import (
    ModelCheckpoint,
    CSVLogger,
    TerminateOnNaN,
    EarlyStopping,
)

mcp = ModelCheckpoint(
    filepath="cifar10-{epoch:02d}.keras",
    monitor="val_loss",
    verbose=0,
    save_best_only=True,
    save_weights_only=False,
    mode="auto",
    save_freq="epoch",
)
log = CSVLogger(filename="tmp_cifar10.csv", separator=",", append=False)
ton = TerminateOnNaN()
esl = EarlyStopping(
    monitor="val_loss", patience=7, mode="auto", restore_best_weights=True
)
esa = EarlyStopping(
    monitor="val_accuracy", patience=7, mode="auto", restore_best_weights=True
)

from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增

datagen = ImageDataGenerator(
    width_shift_range=0.1,  # 平移範圍 W 10%
    height_shift_range=0.1,  # 平移範圍 H 10%
    shear_range=0.1,
    rotation_range=20,  # 旋轉角度 +-20度
    horizontal_flip=True,  # 左右翻轉
)

# 資料分割
x_train, x_valid, y_train, y_valid = train_test_split(
    x_train, y_train, test_size=0.1, random_state=int(time.time())
)

batch_size = 50
hist = model.fit(
    x=datagen.flow(x_train, y_train, batch_size=batch_size),
    steps_per_epoch=x_train.shape[0] // batch_size,
    epochs=2,  # 50
    validation_data=(x_valid, y_valid),
    callbacks=[mcp, log, ton, esl, esa],
    verbose=2,
)

score = model.evaluate(x_test, y_test, verbose=0)
print("Test loss:", score[0])
print("正確率 Test accuracy:", score[1])

print("dddd11")
y_predict = model.predict(x_test)  # 很久
print("dddd22")

y_predict = np.argmax(y_predict, axis=1)

print("dddd33")

y_test = np.argmax(y_test, axis=1)

wrong = np.not_equal(y_predict, y_test)

label = np.arange(*y_test.shape)[wrong]

print("dddd44")

text = ["飛機", "汽車", "鳥", "貓", "鹿", "狗", "青蛙", "馬", "船", "卡車"]

plt.figure(figsize=(16, 10), facecolor="w")
for i in range(5):
    for j in range(8):
        index = random.choice(label)
        plt.subplot(5, 8, i * 8 + j + 1)
        plt.title(
            "label: {}, predict: {}".format(
                text[y_test[index]], text[y_predict[index]]
            ),
            fontproperties="Microsoft YaHei",
        )
        plt.imshow(x_test[index])
        plt.axis("off")

show()

"""
大多都是把一種動物辨識成另一種動物，或是一種交通工具辨識成另一種交通工具，混淆兩者的情況沒有太多，模型還是有學到一些東西的，畫個混淆矩陣來看，因為要把標籤換成中文，所以改了一下程式。
"""

y_test = np.array(list(map(lambda x: text[x], y_test)))
y_predict = np.array(list(map(lambda x: text[x], y_predict)))
df = pd.DataFrame({"y_Actual": y_test, "y_Predicted": y_predict})
pd.crosstab(
    df["y_Actual"], df["y_Predicted"], rownames=["Actual"], colnames=["Predicted"]
)


"""
貓好像經常被誤認為狗，發生了206次，不過也不能怪模型了，這圖解析度也不高，有些圖片用人眼看也需要一些時間才能反應出來，這裡畫個訓練時的loss和accuracy給大家看吧，程式有所更改，因為我們將epoch調高了，也有可能發生EarlyStopping的情況，所以不能把數字寫死了，在本次訓練中，模型在第34次epoch停止，模型被回退到第27次時的狀態了，比起mnist的圖看起來，有種掙扎的感覺。
"""

history = hist.history
epoch = len(history["loss"])
x = np.arange(epoch)
plt.figure(facecolor="w")
plt.plot(x, history["loss"], label="loss")
plt.plot(x, history["val_loss"], label="val_loss")
plt.plot(x, history["accuracy"], label="accuracy")
plt.plot(x, history["val_accuracy"], label="val_accuracy")

plt.xlim(0, epoch - 1)
plt.xticks(
    [i for i in range(0, epoch, epoch // 5)],
    [str(i) for i in range(0, epoch, epoch // 5)],
)
plt.xlabel("epoch")
plt.ylim(0, 1)
plt.ylabel("acc-loss")
plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Final 使用 CNN 辨識 cifar10 圖片資料集

from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.utils import plot_model

# 下載數據
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

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

print("檢視模型架構")
model.summary()  # 檢視模型架構

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 標準化

from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

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

from tensorflow.keras.preprocessing.image import ImageDataGenerator  # 資料擴增

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

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
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers Flatten
from tensorflow.keras.layers Input
from tensorflow.keras.models import Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

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
from tensorflow.keras.utils import to_categorical  # One-Hot Encoding

batch_size = 100
hidden_neurons = 200
classes = 10
epochs = 20

(X_train, Y_train), (X_test, Y_test) = cifar10.load_data()

Y_train = to_categorical(Y_train, classes)
Y_test = to_categorical(Y_test, classes)

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
