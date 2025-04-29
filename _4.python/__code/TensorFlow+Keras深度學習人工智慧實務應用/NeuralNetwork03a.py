"""
TensorFlow+Keras深度學習人工智慧實務應用

http://www.drmaster.com.tw/download/example/MP21710_example.zip

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

import sklearn
import tensorflow as tf
from sklearn import datasets
from sklearn.cluster import KMeans  # 聚類方法, K-平均演算法
from sklearn.cluster import MeanShift  # 均值偏移_聚類演算法
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.metrics import accuracy_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 1. 全连接mnist数字识别
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()
x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255
y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)
model = Sequential()
model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)
model.add(Dropout(0.5))
model.add(Dense(units=1000, kernel_initializer="normal", activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))
print(model.summary())
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)
"""
show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])
prediction = model.predict_classes(x_Test)
plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)
# pd.crosstab(y_test_label,prediction,rownames=['label'],
#             colnames=['predict'])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 2. cnn on mnist


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()
x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28, 1).astype("float32")
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype("float32")
x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255
y_TrainOneHot = tf.keras.utils.to_categorical(y_Train)
y_TestOneHot = tf.keras.utils.to_categorical(y_Test)
model = Sequential()
model.add(
    Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=36, kernel_size=(5, 5), padding="same", activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
print(model.summary())
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
train_history = model.fit(
    x=x_Train4D_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=300,
    verbose=2,
)
"""
show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_Test4D_normalize, y_TestOneHot)
print(scores[1])
prediction = model.predict_classes(x_Test4D_normalize)
pd.crosstab(y_Test, prediction, rownames=["label"], colnames=["predict"])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 3. cnn on cifar10

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",prediction=" + str(prediction[idx])
        ax.set_title(title)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


from keras.datasets import cifar10
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import ZeroPadding2D


(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()
x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0
y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)
model = Sequential()
model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)
model.add(Dropout(rate=0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(rate=0.25))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dropout(rate=0.25))
model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 久
train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)
show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")
scores = model.evaluate(x_img_train_normalize, y_label_train_OneHot, verbose=0)
print(scores[1])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 5.1 建立Computational Graph

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

# 建立 const

ts_c = tf.constant(2, name="ts_c")

print(ts_c)

# <tf.Tensor 'ts_c:0' shape=() dtype=int32>

# 建立 Variable

ts_x = tf.Variable(ts_c + 5, name="ts_x")

print(ts_x)

# <tf.Variable 'ts_x:0' shape=() dtype=int32_ref>

# 5.2 建立Session執行Computational Graph

init = tf.global_variables_initializer()

ts_c = 2

ts_x = 7

# --------------------------------------

# Session open close

# import tensorflow as tf
ts_c = tf.constant(2, name="ts_c")
ts_x = tf.Variable(ts_c + 5, name="ts_x")

sess = tf.Session()
init = tf.global_variables_initializer()

sess.close()

# With語法開啟Session

ts_c = tf.constant(2, name="ts_c")
ts_x = tf.Variable(ts_c + 5, name="ts_x")
with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# --------------------------------------

# Create dim 1 tensor

ts_X = tf.Variable([0.4, 0.2, 0.4])

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# Create dim 2 tensor

ts_X = tf.Variable([[0.4, 0.2, 0.4]])

with tf.Session() as sess:
    init = tf.global_variables_initializer()
    sess.run(init)

# shape: (1, 3)

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])

with tf.Session() as sess:
    init = tf.global_variables_initializer()

# matmul

X = tf.Variable([[1.0, 1.0, 1.0]])

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])

XW = tf.matmul(X, W)

with tf.Session() as sess:
    init = tf.global_variables_initializer()

tf.add

b = tf.Variable([[0.1, 0.2]])
XW = tf.Variable([[-1.3, 0.4]])

Sum = XW + b
with tf.Session() as sess:
    init = tf.global_variables_initializer()

X = tf.Variable([[1.0, 1.0, 1.0]])

W = tf.Variable([[-0.5, -0.2], [-0.3, 0.4], [-0.5, 0.2]])


b = tf.Variable([[0.1, 0.2]])

XWb = tf.matmul(X, W) + b


with tf.Session() as sess:
    init = tf.global_variables_initializer()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

size = 500
W = tf.random_normal([size, size], name="W")
X = tf.random_normal([size, size], name="X")
mul = tf.matmul(W, X, name="mul")
sum_result = tf.reduce_sum(mul, name="sum")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_Introduce

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

print("train data=", len(x_train_image))
print(" test data=", len(x_test_image))

# train data= 60000
# test data= 10000

print("x_train_image:", x_train_image.shape)
print("y_train_label:", y_train_label.shape)

# x_train_image: (60000, 28, 28)
# y_train_label: (60000,)


def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap="binary")
    show()


plot_image(x_train_image[0])

print(y_train_label[0])
# 5


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_train_image, y_train_label, [], 0, 10)

print("x_test_image:", x_test_image.shape)
print("y_test_label:", y_test_label.shape)

# x_test_image: (10000, 28, 28)
# y_test_label: (10000,)

plot_images_labels_prediction(x_test_image, y_test_label, [], 0, 10)

# 將images進行預處理

print("x_train_image:", x_train_image.shape)
print("y_train_label:", y_train_label.shape)

# x_train_image: (60000, 28, 28)
# y_train_label: (60000,)

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

print("x_train:", x_Train.shape)
print("x_test:", x_Test.shape)

# x_train: (60000, 784)
# x_test: (10000, 784)

print(x_train_image[0])

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

print(x_Train_normalize[0])

# one hot encode outputs

print(y_train_label[:5])

y_TrainOneHot = tf.keras.utils.to_categorical(y_train_label)
y_TestOneHot = tf.keras.utils.to_categorical(y_test_label)

print(y_TrainOneHot[:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_CNN

from keras.datasets import mnist

# from tensorflow.keras.utils import to_categorical

np.random.seed(10)

# 資料預處理

(x_Train, y_Train), (x_Test, y_Test) = mnist.load_data()

x_Train4D = x_Train.reshape(x_Train.shape[0], 28, 28, 1).astype("float32")
x_Test4D = x_Test.reshape(x_Test.shape[0], 28, 28, 1).astype("float32")

x_Train4D_normalize = x_Train4D / 255
x_Test4D_normalize = x_Test4D / 255

y_TrainOneHot = tf.keras.utils.to_categorical(y_Train)
y_TestOneHot = tf.keras.utils.to_categorical(y_Test)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D

model = Sequential()

model.add(
    Conv2D(
        filters=16,
        kernel_size=(5, 5),
        padding="same",
        input_shape=(28, 28, 1),
        activation="relu",
    )
)

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(filters=36, kernel_size=(5, 5), padding="same", activation="relu"))

model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(128, activation="relu"))

model.add(Dropout(0.5))

model.add(Dense(10, activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train4D_normalize,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=2,
    batch_size=300,
    verbose=2,
)

print(type(train_history))
print(train_history)

print(train_history.history.keys())

# summarize history for accuracy
plt.plot(train_history.history["accuracy"])
plt.plot(train_history.history["val_accuracy"])
plt.title("model accuracy")
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
show()

# summarize history for loss
plt.plot(train_history.history["loss"])
plt.plot(train_history.history["val_loss"])
plt.title("model loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper left")
show()


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率
# 久
print("aaaaaaa 久")
scores = model.evaluate(x_Test4D_normalize, y_TestOneHot)
print(scores[1])

print("bbbbbbb 久")
# 預測結果
# prediction = model.predict_classes(x_Test4D_normalize) # old
predict_x = model.predict(x_Test4D_normalize)
prediction = np.argmax(predict_x, axis=1)

print("ccccccc")

# 9888/10000 [============================>.] - ETA: 0s

cc = prediction[:10]
print(cc)

# array([7, 2, 1, 0, 4, 1, 4, 9, 5, 9], dtype=int64)

# 查看預測結果


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        ax.set_title(
            "label=" + str(labels[idx]) + ",predict=" + str(prediction[idx]),
            fontsize=10,
        )

        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


print("ddddd")

plot_images_labels_prediction(x_Test, y_Test, prediction, idx=0)

# confusion matrix

cc = pd.crosstab(y_Test, prediction, rownames=["label"], colnames=["predict"])
print(cc)

df = pd.DataFrame({"label": y_Test, "predict": prediction})

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h256

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()

model.add(
    Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=2,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])

# 進行預測

# prediction=model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)

print(prediction)


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=0)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
print(df[:2])

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets(
    "C:/_git/vcs/_4.python/ml/data/MNIST_data/", one_hot=True
)

print(
    "train images     :", mnist.train.images.shape, "labels:", mnist.train.labels.shape
)
print(
    "validation images:",
    mnist.validation.images.shape,
    " labels:",
    mnist.validation.labels.shape,
)
print("test images      :", mnist.test.images.shape, "labels:", mnist.test.labels.shape)


# 建立模型
def layer(output_dim, input_dim, inputs, activation=None):
    W = tf.Variable(tf.random_normal([input_dim, output_dim]))
    b = tf.Variable(tf.random_normal([1, output_dim]))
    XWb = tf.matmul(inputs, W) + b
    if activation is None:
        outputs = XWb
    else:
        outputs = activation(XWb)
    return outputs


# 建立輸入層 x

import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

tf.disable_v2_behavior()

x = tf.placeholder("float", [None, 784])

# 建立隱藏層h1

h1 = layer(output_dim=1000, input_dim=784, inputs=x, activation=tf.nn.relu)

# 建立輸出層

y_predict = layer(output_dim=10, input_dim=1000, inputs=h1, activation=None)

# 建立訓練資料label真實值 placeholder

y_label = tf.placeholder("float", [None, 10])

# 定義訓練方式

loss_function = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(logits=y_predict, labels=y_label)
)

optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss_function)

# 定義評估模型的準確率

# 計算每一筆資料是否正確預測

correct_prediction = tf.equal(tf.argmax(y_label, 1), tf.argmax(y_predict, 1))

# 將計算預測正確結果，加總平均

accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 開始訓練

trainEpochs = 15
batchSize = 100
totalBatchs = int(mnist.train.num_examples / batchSize)
epoch_list = []
accuracy_list = []
loss_list = []
from time import time

startTime = time()
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for epoch in range(trainEpochs):
    for i in range(totalBatchs):
        batch_x, batch_y = mnist.train.next_batch(batchSize)
        sess.run(optimizer, feed_dict={x: batch_x, y_label: batch_y})

    loss, acc = sess.run(
        [loss_function, accuracy],
        feed_dict={x: mnist.validation.images, y_label: mnist.validation.labels},
    )

    epoch_list.append(epoch)
    loss_list.append(loss)
    accuracy_list.append(acc)

    print(
        "Train Epoch:",
        "%02d" % (epoch + 1),
        "Loss=",
        "{:.9f}".format(loss),
        " Accuracy=",
        acc,
    )

duration = time() - startTime
print("Train Finished takes:", duration)

fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.plot(epoch_list, loss_list, label="loss")
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["loss"], loc="upper left")
show()

plt.plot(epoch_list, accuracy_list, label="accuracy")
fig = plt.gcf()
fig.set_size_inches(4, 2)
plt.ylim(0.8, 1)
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend()
show()

# 評估模型準確率

print(
    "Accuracy:",
    sess.run(accuracy, feed_dict={x: mnist.test.images, y_label: mnist.test.labels}),
)

# Accuracy: 0.9577

# 進行預測

prediction_result = sess.run(tf.argmax(y_predict, 1), feed_dict={x: mnist.test.images})

cc = prediction_result[:10]
print(cc)

# array([7, 2, 1, 0, 4, 1, 8, 9, 4, 9])


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)

        ax.imshow(np.reshape(images[idx], (28, 28)), cmap="binary")

        title = "label=" + str(np.argmax(labels[idx]))
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    show()


plot_images_labels_prediction(
    mnist.test.images, mnist.test.labels, prediction_result, 0
)

y_predict_Onehot = sess.run(y_predict, feed_dict={x: mnist.test.images})

cc = y_predict_Onehot[8]
print(cc)

# sess.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000_DropOut

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

# 將「輸入層」與「隱藏層」加入模型

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dropout(0.5))

# 將「輸出層」加入模型

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

# 久
scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print("accuracy=", scores[1])

# accuracy= 0.9808

# 進行預測

# prediction = model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)

print(prediction)

# array([7, 2, 1, ..., 4, 5, 6], dtype=int64)


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
cc = df[:2]
print(cc)

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Mnist_MLP_h1000_DropOut_h1000_DropOut

np.random.seed(10)

from keras.datasets import mnist

(x_train_image, y_train_label), (x_test_image, y_test_label) = mnist.load_data()

x_Train = x_train_image.reshape(60000, 784).astype("float32")
x_Test = x_test_image.reshape(10000, 784).astype("float32")

x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255

y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
y_Test_OneHot = tf.keras.utils.to_categorical(y_test_label)

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

# 將「輸入層」與「隱藏層1」加入模型

model.add(
    Dense(units=1000, input_dim=784, kernel_initializer="normal", activation="relu")
)

model.add(Dropout(0.5))

# 將「隱藏層2」加入模型

model.add(Dense(units=1000, kernel_initializer="normal", activation="relu"))

model.add(Dropout(0.5))

# 將「輸出層」加入模型

model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))

print(model.summary())

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x=x_Train_normalize,
    y=y_Train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=200,
    verbose=2,
)

# 以圖形顯示訓練過程


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_Test_normalize, y_Test_OneHot)
print()
print("accuracy=", scores[1])

# accuracy= 0.9802

# 進行預測
# prediction = model.predict_classes(x_Test) # old
predict_x = model.predict(x_Test)
prediction = np.argmax(predict_x, axis=1)
print(prediction)


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "label=" + str(labels[idx])
        if len(prediction) > 0:
            title += ",predict=" + str(prediction[idx])

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340)

# confusion matrix

cc = pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"])

print(cc)

df = pd.DataFrame({"label": y_test_label, "predict": prediction})
cc = df[:2]
print(cc)

cc = df[(df.label == 5) & (df.predict == 3)]
print(cc)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=340, num=1)

plot_images_labels_prediction(x_test_image, y_test_label, prediction, idx=1289, num=1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Keras_Taianic_Introduce

"""
# 下載鐵達尼號旅客資料集

import urllib.request
import os

url="http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls"
filepath="tmp_titanic3.xls"
if not os.path.isfile(filepath):
    result=urllib.request.urlretrieve(url,filepath)
    print('downloaded:',result)


downloaded: ('data/titanic3.xls', <http.client.HTTPMessage object at 0x0000012D1CE78940>)

使用Pandas dataframe讀取資料並進行處理

import numpy
import pandas as pd

all_df = pd.read_excel(filepath)

all_df[:2]

	pclass 	survived 	name 	sex 	age 	sibsp 	parch 	ticket 	fare 	cabin 	embarked 	boat 	body 	home.dest
0 	1 	1 	Allen, Miss. Elisabeth Walton 	female 	29.0000 	0 	0 	24160 	211.3375 	B5 	S 	2 	NaN 	St Louis, MO
1 	1 	1 	Allison, Master. Hudson Trevor 	male 	0.9167 	1 	2 	113781 	151.5500 	C22 C26 	S 	11 	NaN 	Montreal, PQ / Chesterville, ON

cols=['survived','name','pclass' ,'sex', 'age', 'sibsp',
      'parch', 'fare', 'embarked']
all_df=all_df[cols]

all_df[:2]

	survived 	name 	pclass 	sex 	age 	sibsp 	parch 	fare 	embarked
0 	1 	Allen, Miss. Elisabeth Walton 	1 	female 	29.0000 	0 	0 	211.3375 	S
1 	1 	Allison, Master. Hudson Trevor 	1 	male 	0.9167 	1 	2 	151.5500 	S

all_df.isnull().sum()

survived      0
name          0
pclass        0
sex           0
age         263
sibsp         0
parch         0
fare          1
embarked      2
dtype: int64

df=all_df.drop(['name'], axis=1)

age_mean = df['age'].mean()
df['age'] = df['age'].fillna(age_mean)

fare_mean = df['fare'].mean()
df['fare'] = df['fare'].fillna(fare_mean)

df['sex']= df['sex'].map({'female':0, 'male': 1}).astype(int)

df[:2]

	survived 	pclass 	sex 	age 	sibsp 	parch 	fare 	embarked
0 	1 	1 	0 	29.0000 	0 	0 	211.3375 	S
1 	1 	1 	1 	0.9167 	1 	2 	151.5500 	S

x_OneHot_df = pd.get_dummies(data=df,columns=["embarked" ])

x_OneHot_df[:2]

	survived 	pclass 	sex 	age 	sibsp 	parch 	fare 	embarked_C 	embarked_Q 	embarked_S
0 	1 	1 	0 	29.0000 	0 	0 	211.3375 	0 	0 	1
1 	1 	1 	1 	0.9167 	1 	2 	151.5500 	0 	0 	1
轉換為array

ndarray = x_OneHot_df.values

ndarray.shape

(1309, 10)

ndarray[:2]

array([[   1.    ,    1.    ,    0.    ,   29.    ,    0.    ,    0.    ,
         211.3375,    0.    ,    0.    ,    1.    ],
       [   1.    ,    1.    ,    1.    ,    0.9167,    1.    ,    2.    ,
         151.55  ,    0.    ,    0.    ,    1.    ]])

Label = ndarray[:,0]
Features = ndarray[:,1:]

 

Features.shape

(1309, 9)

Features[:2]

array([[   1.    ,    0.    ,   29.    ,    0.    ,    0.    ,  211.3375,
           0.    ,    0.    ,    1.    ],
       [   1.    ,    1.    ,    0.9167,    1.    ,    2.    ,  151.55  ,
           0.    ,    0.    ,    1.    ]])

Label.shape

(1309,)

Label[:2]

array([ 1.,  1.])

將array進行標準化

from sklearn import preprocessing

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

scaledFeatures=minmax_scale.fit_transform(Features)

scaledFeatures[:2]

array([[ 0.        ,  0.        ,  0.36116884,  0.        ,  0.        ,
         0.41250333,  0.        ,  0.        ,  1.        ],
       [ 0.        ,  1.        ,  0.00939458,  0.125     ,  0.22222222,
         0.2958059 ,  0.        ,  0.        ,  1.        ]])

Label[:5]

array([ 1.,  1.,  0.,  0.,  0.])

將資料分為訓練資料與測試資料

msk = numpy.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]

print('total:',len(all_df),
      'train:',len(train_df),
      'test:',len(test_df))

total: 1309 train: 1043 test: 266

def PreprocessData(raw_df):
    df=raw_df.drop(['name'], axis=1)
    age_mean = df['age'].mean()
    df['age'] = df['age'].fillna(age_mean)
    fare_mean = df['fare'].mean()
    df['fare'] = df['fare'].fillna(fare_mean)
    df['sex']= df['sex'].map({'female':0, 'male': 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df,columns=["embarked" ])

    ndarray = x_OneHot_df.values
    Features = ndarray[:,1:]
    Label = ndarray[:,0]

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures=minmax_scale.fit_transform(Features)    
    
    return scaledFeatures,Label

train_Features,train_Label=PreprocessData(train_df)
test_Features,test_Label=PreprocessData(test_df)

train_Features[:2]

array([[ 0.        ,  0.        ,  0.36116884,  0.        ,  0.        ,
         0.41250333,  0.        ,  0.        ,  1.        ],
       [ 0.        ,  1.        ,  0.00939458,  0.125     ,  0.22222222,
         0.2958059 ,  0.        ,  0.        ,  1.        ]])

train_Label[:2]

array([ 1.,  1.])

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


"""
# from keras.utils import np_utils
# np_utils.to_categorical(y_Train)
改成
y_Train_OneHot = tf.keras.utils.to_categorical(y_train_label)
# from keras.utils import np_utils
# np_utils.to_categorical(y_Train)
"""


""" 解决 placeholder
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0
tf.disable_v2_behavior()

x = tf.placeholder("float", [None, 784])
"""
