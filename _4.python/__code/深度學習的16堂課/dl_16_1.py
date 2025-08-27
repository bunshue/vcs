"""
深度學習的16堂課
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

import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_classification
from sklearn.datasets import make_regression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.model_selection import cross_val_score  # Cross Validation
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier  # 隨機森林分類函數學習機
from sklearn.ensemble import RandomForestRegressor  # 隨機森林函數學習機
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from matplotlib.colors import ListedColormap


def show():
    plt.show()
    pass

EPOCHS = 50

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# Ch05 先動手實作！５ 行程式體驗神經網路模型
# 5.2.3 在 Colab 讀入 MNIST 資料集

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(X_train.shape)

np.set_printoptions(linewidth=np.inf)  # 讓列印出來的資料不斷行
print(X_train[0])

print(y_train.shape)

print(y_train[0:12])

# array([5, 0, 4, 1, 9, 2, 1, 3, 1, 4, 3, 5], dtype=uint8)

plt.figure(figsize=(5, 5))
for k in range(12):
    plt.subplot(3, 4, k + 1)
    plt.imshow(X_train[k], cmap="gray")
plt.tight_layout()
plt.show()

# 5.2.4 資料預處理

X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

X_train /= 255
X_test /= 255

print(X_train[0])

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)

print(y_train[0])

# array([0., 0., 0., 0., 0., 1., 0., 0., 0., 0.], dtype=float32)

# 5.2.5 開始建立神經網路模型！5 行程式就搞定！

model = Sequential()
model.add(Dense(64, activation="sigmoid", input_shape=(784,)))
model.add(Dense(10, activation="softmax"))

model.compile(
    loss="mean_squared_error",
    optimizer=optimizers.SGD(learning_rate=0.01),
    metrics=["accuracy"],
)

# 5.2.6 訓練神經網路模型

model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 8.4 規劃隱藏層與各層神經元的數量

np.random.seed(42)

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout  # new!
from tensorflow.keras import callbacks
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import backend as K
from scipy.ndimage.filters import gaussian_filter1d


class GradHistory(callbacks.Callback):
    def on_train_begin(self, logs={}):
        # Initialize list of hidden layers
        self.layers = [layer for layer in self.model.layers if "hidden_" in layer.name]

        # Initialize grads dict with empty list
        self.grads = {layer.name: [] for layer in self.layers}

        # Grab the initial weights from the model
        self.prev_w = [layer.get_weights()[0] for layer in self.layers]

    def on_epoch_end(self, batch, logs={}):
        # Get the weights at the end of the epoch
        curr_w = [layer.get_weights()[0] for layer in self.layers]

        # Get the LR at the end of the epoch
        lr = K.get_value(self.model.optimizer.lr)

        # Convert the previous and currents weights to gradients
        grads_ = [(prev - curr) for curr, prev in zip(curr_w, self.prev_w)]

        # Move the grads into the self.grads dict
        for i, layer in enumerate(grads_):
            self.grads[self.layers[i].name].append(layer)
        self.prev_w = curr_w

    def on_train_end(self, logs={}):
        # At the end of training, take the euclidean norm of each array of gradients in each layer at each epoch.
        self.norms = {
            k: [np.sqrt(np.sum([x * x for x in epoch])) for epoch in v]
            for k, v in self.grads.items()
        }


(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)


def build_model(hidden=2):
    model = Sequential()
    model.add(Dense(30, activation="sigmoid", input_shape=(784,), name="input"))

    for h in range(hidden):
        model.add(Dense(30, activation="sigmoid", name="hidden_{}".format(h)))

    model.add(Dense(10, activation="softmax"))

    return model


def build_and_train(hidden=1, epochs=epochs):
    model = build_model(hidden)
    history = GradHistory()
    model.compile(
        loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"]
    )
    model.fit(
        X_train[:1000],
        y_train[:1000],
        batch_size=1,
        epochs=epochs,
        verbose=0,
        callbacks=[history],
    )

    return history


""" NG
norms_5 = build_and_train(5, EPOCHS)


def plot(history, hidden, log=False):
    fig = plt.figure(figsize=(8, 6), dpi=300)

    layers = [layer for layer in history.norms.keys()]
    values = [history.norms[layer] for layer in layers]

    for layer, values in zip(layers[::-1], values[::-1]):
        ys = np.array(values[:])
        xs = np.array(range(ys.shape[0]))
        ys_smooth = gaussian_filter1d(ys, sigma=3)
        plt.plot(xs, ys_smooth, label=layer)

    plt.title("Learning speed with {} hidden layers".format(hidden))
    plt.ylabel("Learning speed")
    if log:
        plt.yscale("log")
    plt.xlabel("Epoch")
    plt.legend(loc="upper right")
    plt.show()


plot(norms_5, 5, True)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 8.5 範例：建構多層神經網路

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import optimizers
from tensorflow.keras.utils import plot_model
from tensorflow.keras.utils import to_categorical

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 資料預處理

X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)

# 規劃神經網路結構

model = Sequential()
model.add(Dense(64, activation="relu", input_shape=(784,)))
model.add(Dense(64, activation="relu"))
model.add(Dense(10, activation="softmax"))

model.summary()

# 模型編譯

model.compile(
    loss="categorical_crossentropy",
    optimizer=optimizers.SGD(learning_rate=0.01),
    metrics=["accuracy"],
)

# 訓練神經網路!

model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Ch09 改善神經網路的訓練成效
9.1 權重初始化 (weight initialization)
9.1.1 從《ch09-weight_initialization.ipynb》範例看起
"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.initializers import (
    Zeros,
    RandomNormal,
    glorot_normal,
    glorot_uniform,
)

n_input = 784
n_dense = 256

# 設定權重的初始值

b_init = Zeros()

w_init = RandomNormal(stddev=1.0)
# w_init = glorot_normal()
# w_init = glorot_uniform()

# 建構神經網路

model = Sequential()
model.add(
    Dense(
        n_dense, input_dim=n_input, kernel_initializer=w_init, bias_initializer=b_init
    )
)
model.add(Activation("sigmoid"))
# model.add(Activation('tanh'))
# model.add(Activation('relu'))

# 產生輸入資料, 並算出密集層 256 個神經元的激活值

x = np.random.random((1, n_input))

a = model.predict(x)

# 畫圖查看各激活值的分布

_ = plt.hist(np.transpose(a))
# 註：由於神經網路的初始權重參數是隨機設定的, 參雜了隨機性, 因此底下 (或您重跑一次) 的結果會與書中有小差異
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 9.5 實作：用 tf.Keras 建構深度神經網路

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout  # new!
from tensorflow.keras.layers import BatchNormalization  # new!
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import SGD

# 9.5.2 神經網路的構造

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)

model = Sequential()

model.add(Dense(64, activation="relu", input_shape=(784,)))
model.add(BatchNormalization())

model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())

model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(10, activation="softmax"))

model.summary()

# 9.5.3 設定優化器 (編譯模型)

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 訓練模型!
model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 9.6 改試試迴歸 (Regression) 範例

from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import BatchNormalization

# 9.6.1 載入資料集

(X_train, y_train), (X_test, y_test) = boston_housing.load_data()

X_train.shape

# (404, 13)

X_test.shape

# (102, 13)

X_train[0]

y_train[0]

# 9.6.2 神經網路的架構

model = Sequential()

model.add(Dense(32, input_dim=13, activation="relu"))
model.add(BatchNormalization())

model.add(Dense(16, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(1, activation="linear"))

model.summary()

# 9.6.3 編譯、訓練模型

model.compile(loss="mean_squared_error", optimizer="adam")

model.fit(
    X_train,
    y_train,
    batch_size=8,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
)

# 9.6.4 實際進行預測

X_test[42]

y_test[42]

model.predict(np.reshape(X_test[42], [1, 13]))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 9.7 用 TensorBoard 視覺化判讀訓練結果

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras import optimizers
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import TensorBoard  # new!

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 784).astype("float32")
X_test = X_test.reshape(10000, 784).astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)

# 規劃神經網路架構

model = Sequential()

model.add(Dense(64, activation="relu", input_shape=(784,)))
model.add(BatchNormalization())

model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())

model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.2))

model.add(Dense(10, activation="softmax"))

model.summary()

# 模型編譯

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 將模型訓練資訊輸出至本章範例資料集內的 logs 子資料夾

tensorboard = TensorBoard(
    log_dir="/content/drive/MyDrive/Colab Notebooks\F1383_Sample\Ch09\9_7\logs"
)  # 註：請記得依你存放的位置彈性修改路徑

# 9.7.1 在訓練中添加 TensorBoard callback

model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
    callbacks=[tensorboard],
)

# 9.7.2 在 Colab 啟動 TensorBoard
"""
%load_ext tensorboard
%tensorboard --logdir '/content/drive/MyDrive/Colab Notebooks\F1383_Sample\Ch09\9_7\logs'
Output hidden; open in https://colab.research.google.com to view.
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Ch10 機器視覺實戰演練：CNN (Convolutional Neural Network)
"""

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Flatten, Conv2D, MaxPooling2D  # new!

(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(60000, 28, 28, 1).astype("float32")
X_test = X_test.reshape(10000, 28, 28, 1).astype("float32")

X_train /= 255
X_test /= 255

n_classes = 10
y_train = to_categorical(y_train, n_classes)
y_test = to_categorical(y_test, n_classes)


model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation="relu", input_shape=(28, 28, 1)))

model.add(Conv2D(64, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())

model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(n_classes, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(
    X_train,
    y_train,
    batch_size=128,
    epochs=EPOCHS,
    verbose=1,
    validation_data=(X_test, y_test),
)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
# 10.4 進階的 CNN 技術 (用 tf.Keras 重現 AlexNet 與 VGGNet 架構)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization

""" NG module
# !pip install tflearn
import tflearn.datasets.oxflower17 as oxflower17
X, Y = oxflower17.load_data(one_hot=True)
Y[0]

# 10.4.2 CNN 範例 (一)：仿 AlexNet 經典模型

model = Sequential()

model.add(
    Conv2D(
        96,
        kernel_size=(11, 11),
        strides=(4, 4),
        activation="relu",
        input_shape=(224, 224, 3),
    )
)
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(256, kernel_size=(5, 5), activation="relu"))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(256, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(384, kernel_size=(3, 3), activation="relu"))
model.add(Conv2D(384, kernel_size=(3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(3, 3), strides=(2, 2)))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(4096, activation="tanh"))
model.add(Dropout(0.5))
model.add(Dense(4096, activation="tanh"))
model.add(Dropout(0.5))

model.add(Dense(17, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(
    X, Y, batch_size=64, epochs=EPOCHS, verbose=1, validation_split=0.1, shuffle=True
)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 10.4.3 CNN 範例 (二)：仿 VGGNet 經典模型

np.random.seed(42)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization

# from keras.callbacks import TensorBoard

""" NG module
# !pip install tflearn
import tflearn.datasets.oxflower17 as oxflower17
X, Y = oxflower17.load_data(one_hot=True)

model = Sequential()

model.add(Conv2D(64, 3, activation="relu", input_shape=(224, 224, 3)))
model.add(Conv2D(64, 3, activation="relu"))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization())

model.add(Conv2D(128, 3, activation="relu"))
model.add(Conv2D(128, 3, activation="relu"))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization())

model.add(Conv2D(256, 3, activation="relu"))
model.add(Conv2D(256, 3, activation="relu"))
model.add(Conv2D(256, 3, activation="relu"))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization())

model.add(Conv2D(512, 3, activation="relu"))
model.add(Conv2D(512, 3, activation="relu"))
model.add(Conv2D(512, 3, activation="relu"))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization())

model.add(Conv2D(512, 3, activation="relu"))
model.add(Conv2D(512, 3, activation="relu"))
model.add(Conv2D(512, 3, activation="relu"))
model.add(MaxPooling2D(2, 2))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dense(4096, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(4096, activation="relu"))
model.add(Dropout(0.5))

model.add(Dense(17, activation="softmax"))

model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

model.fit(
    X, Y, batch_size=64, epochs=EPOCHS, verbose=1, validation_split=0.1, shuffle=True
)  # callbacks=[tensorbrd])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
下載
https://storage.googleapis.com/tensorflow/keras-applications/vgg19/vgg19_weights_tf_dim_ordering_tf_kernels_notop.h5
放在
C:/Users/070601/.keras/models/之下
"""

# 10.6.3 遷移學習 (transfer learning)

from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 建立預訓練過的 VGG19 模型物件

vgg19 = VGG19(
    include_top=False, weights="imagenet", input_shape=(224, 224, 3), pooling=None
)

# 凍結 VGGNet 的神經層
for layer in vgg19.layers:
    layer.trainable = False

# 添加新的密集層
# 建立空的模型後, 把載入的 VGG19 模型的神經層加進去：
model = Sequential()
model.add(vgg19)

# 在 VGG19 神經層後面增加負責分類的新神經層：
model.add(Flatten(name="flattened"))
model.add(Dropout(0.5, name="dropout"))
model.add(Dense(2, activation="softmax", name="predictions"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

"""
熱狗堡資料集    Hot Dog - Not Hot Dog
https://www.kaggle.com/datasets/dansbecker/hot-dog-not-hot-dog/home
"""

# 使用 ImageDataGenerator 類別

# 建立兩個 ImageDataGenerator 物件：
train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    data_format="channels_last",
    rotation_range=30,
    horizontal_flip=True,
    fill_mode="reflect",
)

valid_datagen = ImageDataGenerator(rescale=1.0 / 255, data_format="channels_last")


# 定義訓練與驗證資料的生成器

# 執行此程式區塊前，請記得先執行最上面的程式區塊，在 Colab 內啟用 Google 雲端硬碟

# 設定批次量
batch_size = 32

# 定義訓練與驗證資料的生成器

train_generator = train_datagen.flow_from_directory(
    directory="D:/_git/vcs/_big_files/HotDog_NotHotDog/train",
    target_size=(224, 224),
    classes=["hot_dog", "not_hot_dog"],
    class_mode="categorical",
    batch_size=batch_size,
    shuffle=True,
    seed=42,
)

valid_generator = valid_datagen.flow_from_directory(
    directory="D:/_git/vcs/_big_files/HotDog_NotHotDog/test",
    target_size=(224, 224),
    classes=["hot_dog", "not_hot_dog"],
    class_mode="categorical",
    batch_size=batch_size,
    shuffle=True,
    seed=42,
)

""" NG 還沒設定檔案位置
# 註：由於神經網路的初始權重參數是隨機設定的, 參雜了隨機性, 因此底下 (或您重跑一次) 的結果不會與書中完全一樣, 但模型的能力是相近的
# 註：此模型執行時間較長，每週期約需 10 分鐘不等
model.fit(
    train_generator,
    steps_per_epoch=15,
    epochs=EPOCHS,
    validation_data=valid_generator,
    validation_steps=15,
)
"""

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


print("------------------------------")  # 30個
