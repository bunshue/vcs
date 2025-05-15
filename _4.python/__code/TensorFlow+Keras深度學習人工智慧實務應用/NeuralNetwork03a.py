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

print("Keras_Mnist_Introduce")

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

print("Keras_Mnist_CNN")

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

print("Keras_Mnist_MLP_h256")

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

print("Keras_Mnist_MLP_h1000")

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data

mnist = input_data.read_data_sets("C:/_git/vcs/_4.python/ml/data/MNIST_data/", one_hot=True)

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

print("Keras_Mnist_MLP_h1000_DropOut")

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
    show()


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
    show()


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

print("Keras_Mnist_MLP_h1000_DropOut_h1000_DropOut")

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
    show()


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
    show()


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

print("Keras_Taianic_Introduce")


# 下載鐵達尼號旅客資料集

import urllib.request

url = "http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic3.xls"  # old
url = "https://hbiostat.org/data/repo/titanic3.xls"
filename = "tmp_titanic3.xls"
if not os.path.isfile(filename):
    result = urllib.request.urlretrieve(url, filename)
    print("downloaded:", result)

# 使用Pandas dataframe讀取資料並進行處理

all_df = pd.read_excel(filename)

print(all_df.shape)

# 1309筆資料, 14欄位

# 查看前2筆資料
cc = all_df[:2]
print(cc)


"""
1	2		3	4	5	6	7
pclass	survived	name	sex	age	sibsp	parch
8	9	10	11		12	13	14
ticket	fare	cabin	embarked	boat	body	home.dest
	
資料欄位包含:
艙等:pclass
是否生存:survival
姓名:name
性別:sex
年齡:age
手足、配偶也在船上數量:sibsp
雙親或子女也在船上數量:parch
車票號碼:ticket
旅客費用:fare
艙位號碼:cabin
登船港口embarked
"""

# 選取所需的欄位, 只抓取需要的欄位至dataframe
cols = [
    "survived",
    "name",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]
all_df = all_df[cols]


"""
資料欄位包含:
是否生存:survival
艙等:pclass
姓名:name
性別:sex
年齡:age
手足、配偶也在船上數量:sibsp
雙親或子女也在船上數量:parch
旅客費用:fare
登船港口embarked
"""

# 4) 開始資料處理
"""
姓名先移除，訓練時不需要
性別:sex，欄位為文字，將轉為0、1
年齡:age，為null值，將填入平均值
旅客費用:fare，為null值，將填入平均值
登船港口embarked(有3類C、Q、S)，用onehot encoding 轉換
"""


cc = all_df[:2]
print(cc)

# 找出含有null值的欄位
cc = all_df.isnull().sum()
print(cc)

# 將name欄位移除
df = all_df.drop(["name"], axis=1)
# axis=0，指删除index，因此删除columns时要指定axis=1

# 資料都填上平均值 把age為null值的欄位補上平均值
age_mean = df["age"].mean()

df["age"] = df["age"].fillna(age_mean)

# 把fare為null值的欄位補上平均值
fare_mean = df["fare"].mean()
df["fare"] = df["fare"].fillna(fare_mean)

# 性別欄位轉換 轉換性別為0,1 需要將文字轉成數字才能進行訓練
df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)

cc = df[:2]
print(cc)

# 用Onehot Enconding轉換
# 登船港口embarked 轉換
# data為要轉換的dataframe  columns為要轉換的欄位
x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

cc = x_OneHot_df[:2]
print(cc)

# 4) dataframe轉換為array 。之後資料處理需要用到
# 轉換為array

ndarray = x_OneHot_df.values

print(ndarray.shape)

# (1309, 10)

print(ndarray[:2])

# 擷取features 和 label

Label = ndarray[:, 0]
Features = ndarray[:, 1:]

# 5) features 標準化，標準化之後的數字。都介顧0–1之間

print(Features.shape)

print(Features[:2])

print(Label.shape)

print(Label[:2])

# 將array進行標準化  將特徵欄位進行標準化

from sklearn import preprocessing

minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))

scaledFeatures = minmax_scale.fit_transform(Features)

print(scaledFeatures[:2])  # 查看前兩筆資料

print(Label[:5])

# 6) 將資料80% 為訓練資料、20 % 為測試資料
# 將資料分為訓練資料與測試資料
# 使用隨機方式分類並顯示
msk = np.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]

print("total:", len(all_df), "train:", len(train_df), "test:", len(test_df))

# total: 1309 train: 1043 test: 266

# 7)預處理function


def PreprocessData(raw_df):
    df = raw_df.drop(["name"], axis=1)
    age_mean = df["age"].mean()
    df["age"] = df["age"].fillna(age_mean)
    fare_mean = df["fare"].mean()
    df["fare"] = df["fare"].fillna(fare_mean)
    df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

    ndarray = x_OneHot_df.values
    Features = ndarray[:, 1:]
    Label = ndarray[:, 0]

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures = minmax_scale.fit_transform(Features)

    return scaledFeatures, Label


# 8) 進行資料預處理

train_Features, train_Label = PreprocessData(train_df)
test_Features, test_Label = PreprocessData(test_df)

print(train_Features[:2])  # 訓練資料特徵欄位

print(train_Label[:2])  # 訓練資料標籤欄位

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Taianic_MLP")

from sklearn import preprocessing

np.random.seed(10)

filename = "tmp_titanic3.xls"

all_df = pd.read_excel(filename)

cols = [
    "survived",
    "name",
    "pclass",
    "sex",
    "age",
    "sibsp",
    "parch",
    "fare",
    "embarked",
]
all_df = all_df[cols]

msk = np.random.rand(len(all_df)) < 0.8
train_df = all_df[msk]
test_df = all_df[~msk]

print("total:", len(all_df), "train:", len(train_df), "test:", len(test_df))

# total: 1309 train: 1034 test: 275


def PreprocessData(raw_df):
    df = raw_df.drop(["name"], axis=1)
    age_mean = df["age"].mean()
    df["age"] = df["age"].fillna(age_mean)
    fare_mean = df["fare"].mean()
    df["fare"] = df["fare"].fillna(fare_mean)
    df["sex"] = df["sex"].map({"female": 0, "male": 1}).astype(int)
    x_OneHot_df = pd.get_dummies(data=df, columns=["embarked"])

    ndarray = x_OneHot_df.values
    Features = ndarray[:, 1:]
    Label = ndarray[:, 0]

    minmax_scale = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaledFeatures = minmax_scale.fit_transform(Features)

    return scaledFeatures, Label


train_Features, train_Label = PreprocessData(train_df)
test_Features, test_Label = PreprocessData(test_df)

# 3. Create Model

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()

model.add(Dense(units=40, input_dim=9, kernel_initializer="uniform", activation="relu"))

model.add(Dense(units=30, kernel_initializer="uniform", activation="relu"))

model.add(Dense(units=1, kernel_initializer="uniform", activation="sigmoid"))

# 4. Train model

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

"""
train_history = model.fit(
    x=train_Features,
    y=train_Label,
    validation_split=0.1,
    epochs=30,
    batch_size=30,
    verbose=2,
)

# 6. Print History


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

scores = model.evaluate(x=test_Features, y=test_Label)

print(scores[1])

# 預測資料
# 加入Jack & Rose資料

Jack = pd.Series([0, "Jack", 3, "male", 23, 1, 0, 5.0000, "S"])
Rose = pd.Series([1, "Rose", 1, "female", 20, 1, 0, 100.0000, "S"])

JR_df = pd.DataFrame(
    [list(Jack), list(Rose)],
    columns=[
        "survived",
        "name",
        "pclass",
        "sex",
        "age",
        "sibsp",
        "parch",
        "fare",
        "embarked",
    ],
)

all_df = pd.concat([all_df, JR_df])

print(all_df[-2:])

# 進行預測

all_Features, Label = PreprocessData(all_df)

all_probability = model.predict(all_Features)

cc = all_probability[:10]
print(cc)

pd = all_df
pd.insert(len(all_df.columns), "probability", all_probability)

# 預測Jack & Rose資料的生存機率

print(pd[-2:])

# 查看生存機率高，卻沒有存活

cc = pd[(pd["survived"] == 0) & (pd["probability"] > 0.9)]
print(cc)

print(pd[:5])
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Cifar_CNN-Introduce")

from keras.datasets import cifar10

np.random.seed(10)

# 資料準備

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train:", len(x_img_train))
print("test :", len(x_img_test))

print(x_img_train.shape)

print(y_label_train.shape)

print(x_img_test.shape)

print(x_img_test[0])

print(y_label_test.shape)

label_dict = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_train, y_label_train, [], 0)

print("x_img_test:", x_img_test.shape)
print("y_label_test :", y_label_test.shape)

# Image normalize

print(x_img_train[0][0][0])

# array([59, 62, 63], dtype=uint8)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

print(x_img_train_normalize[0][0][0])

# array([ 0.23137255,  0.24313726,  0.24705882], dtype=float32)

# 轉換label 為OneHot Encoding

print(y_label_train.shape)

# (50000, 1)

print(y_label_train[:5])

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_train_OneHot.shape)

print(y_label_train_OneHot[:5])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Cifar_CNN")

from keras.datasets import cifar10

np.random.seed(10)

# 資料準備

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", x_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", x_img_test.shape, " labels:", y_label_test.shape)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import ZeroPadding2D

model = Sequential()

# 卷積層1

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

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

model.add(Dropout(0.25))

model.add(MaxPooling2D(pool_size=(2, 2)))

# Step3	建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(rate=0.25))

model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModelnew1.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=128,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.7339

# 進行預測

prediction = model.predict_classes(x_img_test_normalize)

print(prediction[:10])

# 查看預測結果

label_dict = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_test, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(x_img_test_normalize)


def show_Predicted_Probability(y, prediction, x_img, Predicted_Probability, i):
    print("label:", label_dict[y[i][0]], "predict:", label_dict[prediction[i]])
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(x_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 0
)

show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 3
)

print("confusion matrix")

print(prediction.shape)

print(y_label_test.shape)

print(y_label_test)

print(y_label_test.reshape(-1))

print(label_dict)
cc = pd.crosstab(
    y_label_test.reshape(-1), prediction, rownames=["label"], colnames=["predict"]
)
print(cc)

print(label_dict)

# Save model to JSON

model_json = model.to_json()
with open("SaveModel/cifarCnnModelnew.json", "w") as json_file:
    json_file.write(model_json)

# Save Model to YAML

model_yaml = model.to_yaml()
with open("SaveModel/cifarCnnModelnew.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Cifar_CNN_Continue_Train")

from keras.datasets import cifar10

np.random.seed(10)

(x_img_train, y_label_train), (x_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", x_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", x_img_test.shape, " labels:", y_label_test.shape)

x_img_train_normalize = x_img_train.astype("float32") / 255.0
x_img_test_normalize = x_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

model = Sequential()

# 卷積層1

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

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))

model.add(Dropout(0.25))

model.add(MaxPooling2D(pool_size=(2, 2)))

# Step3	建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(rate=0.25))

model.add(Dense(1024, activation="relu"))
model.add(Dropout(rate=0.25))

model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModel.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 載入模型失敗!開始訓練一個新模型

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    x_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=1,
    batch_size=128,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.57869999999999999

# 進行預測

prediction = model.predict_classes(x_img_test_normalize)

print(prediction[:10])

# 查看預測結果

label_dict = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(x_img_test, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(x_img_test_normalize)


def show_Predicted_Probability(y, prediction, x_img, Predicted_Probability, i):
    print("label:", label_dict[y[i][0]], "predict:", label_dict[prediction[i]])
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(x_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 0
)

show_Predicted_Probability(
    y_label_test, prediction, x_img_test, Predicted_Probability, 3
)

print("confusion matrix")

print(prediction.shape)

print(y_label_test.shape)

print(y_label_test)

print(y_label_test.reshape(-1))

print(label_dict)
cc = pd.crosstab(
    y_label_test.reshape(-1), prediction, rownames=["label"], colnames=["predict"]
)

print(cc)

print(label_dict)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModel.h5")
print("Saved model to disk")

# Saved model to disk

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Cifar_CNN_Deeper_Conv3")

# Simple CNN model for the CIFAR-10 Dataset

from keras.datasets import cifar10

np.random.seed(10)

(X_img_train, y_label_train), (X_img_test, y_label_test) = cifar10.load_data()

print("train data:", "images:", X_img_train.shape, " labels:", y_label_train.shape)
print("test  data:", "images:", X_img_test.shape, " labels:", y_label_test.shape)

X_img_train_normalize = X_img_train.astype("float32") / 255.0
X_img_test_normalize = X_img_test.astype("float32") / 255.0

y_label_train_OneHot = tf.keras.utils.to_categorical(y_label_train)
y_label_test_OneHot = tf.keras.utils.to_categorical(y_label_test)

print(y_label_test_OneHot.shape)

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D, ZeroPadding2D

model = Sequential()

# 卷積層1與池化層1

model.add(
    Conv2D(
        filters=32,
        kernel_size=(3, 3),
        input_shape=(32, 32, 3),
        activation="relu",
        padding="same",
    )
)
model.add(Dropout(0.3))
model.add(Conv2D(filters=32, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 卷積層2與池化層2

model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=64, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 卷積層3與池化層3

model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(Dropout(0.3))
model.add(Conv2D(filters=128, kernel_size=(3, 3), activation="relu", padding="same"))
model.add(MaxPooling2D(pool_size=(2, 2)))

# 建立神經網路(平坦層、隱藏層、輸出層)

model.add(Flatten())
model.add(Dropout(0.3))
model.add(Dense(2500, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(1500, activation="relu"))
model.add(Dropout(0.3))
model.add(Dense(10, activation="softmax"))

print(model.summary())

# 載入之前訓練的模型

try:
    model.load_weights("SaveModel/cifarCnnModelnew.h5")
    print("載入模型成功!繼續訓練模型")
except:
    print("載入模型失敗!開始訓練一個新模型")

# 載入模型失敗!開始訓練一個新模型

# 訓練模型

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

train_history = model.fit(
    X_img_train_normalize,
    y_label_train_OneHot,
    validation_split=0.2,
    epochs=1,
    batch_size=300,
    verbose=1,
)


def show_train_history(train_acc, test_acc):
    plt.plot(train_history.history[train_acc])
    plt.plot(train_history.history[test_acc])
    plt.title("Train History")
    plt.ylabel("Accuracy")
    plt.xlabel("Epoch")
    plt.legend(["train", "test"], loc="upper left")
    plt.show()


show_train_history("accuracy", "val_accuracy")

show_train_history("loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(X_img_test_normalize, y_label_test_OneHot, verbose=0)
print(scores[1])

# 0.10000000000000001

# 進行預測

prediction = model.predict_classes(X_img_test_normalize)

print(prediction[:10])

label_dict = {
    0: "airplane",
    1: "automobile",
    2: "bird",
    3: "cat",
    4: "deer",
    5: "dog",
    6: "frog",
    7: "horse",
    8: "ship",
    9: "truck",
}


def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")

        title = str(i) + "," + label_dict[labels[i][0]]
        if len(prediction) > 0:
            title += "=>" + label_dict[prediction[i]]

        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_prediction(X_img_test_normalize, y_label_test, prediction, 0, 10)

# 查看預測機率

Predicted_Probability = model.predict(X_img_test_normalize)


def show_Predicted_Probability(X_img, Predicted_Probability, i):
    plt.figure(figsize=(2, 2))
    plt.imshow(np.reshape(X_img_test[i], (32, 32, 3)))
    plt.show()
    for j in range(10):
        print(label_dict[j] + " Probability:%1.9f" % (Predicted_Probability[i][j]))


show_Predicted_Probability(X_img_test, Predicted_Probability, 0)

show_Predicted_Probability(X_img_test, Predicted_Probability, 3)

# Save model to JSON

model_json = model.to_json()
with open("SaveModel/cifarCnnModelnew.json", "w") as json_file:
    json_file.write(model_json)

# Save Model to YAML

model_yaml = model.to_yaml()
with open("SaveModel/cifarCnnModelnew.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)

# Save Weight to h5

model.save_weights("SaveModel/cifarCnnModelnew.h5")
print("Saved model to disk")

# Saved model to disk

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Imdb_Introduce")

import urllib.request
import tarfile

url = "http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
filename = "D:/_git/vcs/_big_files/tmp_aclImdb_v1.tar.gz"
if not os.path.isfile(filename):
    result = urllib.request.urlretrieve(url, filename)
    print("downloaded:", result)

# downloaded: ('data/aclImdb_v1.tar.gz', <http.client.HTTPMessage object at 0x00000256F5C98DD8>)

"""
if not os.path.exists("data/aclImdb"):
    tfile = tarfile.open(filename, 'r:gz')
    result=tfile.extractall('data/')
"""

from keras.datasets import imdb
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer
import re


def rm_tags(text):
    re_tag = re.compile(r"<[^>]+>")
    return re_tag.sub("", text)


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print("read", filetype, "files:", len(file_list))

    all_labels = [1] * 12500 + [0] * 12500

    all_texts = []
    for fi in file_list:
        with open(fi, encoding="utf8") as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")

# read train files: 25000

y_test, test_text = read_files("test")

# read test files: 25000

# 查看正面評價的影評

print(train_text[0])

print(y_train[0])

# 查看負面評價的影評

print(train_text[12499])

print(y_train[12499])

print("先讀取所有文章建立字典，限制字典的數量為nb_words=2000")

token = Tokenizer(num_words=2000)
token.fit_on_texts(train_text)

# Tokenizer屬性

# fit_on_texts 讀取多少文章

print(token.document_count)

# 25000

# manyu print(token.word_index)

# 將每一篇文章的文字轉換一連串的數字
# 只有在字典中的文字會轉換為數字

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

print(train_text[0])

print(x_train_seq[0])

# 讓轉換後的數字長度相同

# 文章內的文字，轉換為數字後，每一篇的文章地所產生的數字長度都不同，因為後需要進行類神經網路的訓練，所以每一篇文章所產生的數字長度必須相同
# 以下列程式碼為例maxlen=100，所以每一篇文章轉換為數字都必須為100
# bj6eji3t03g/ 2k

x_train = sequence.pad_sequences(x_train_seq, maxlen=100)
x_test = sequence.pad_sequences(x_test_seq, maxlen=100)

# 如果文章轉成數字大於0,pad_sequences處理後，會truncate前面的數字

print("before pad_sequences length=", len(x_train_seq[0]))
print(x_train_seq[0])

print("after pad_sequences length=", len(x_train[0]))
print(x_train[0])

# 如果文章轉成數字不足100,pad_sequences處理後，前面會加上0

print("before pad_sequences length=", len(x_train_seq[1]))
print(x_train_seq[1])

print("after pad_sequences length=", len(x_train[1]))
print(x_train[1])

# 資料預處理

token = Tokenizer(num_words=2000)
token.fit_on_texts(train_text)

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

x_train = sequence.pad_sequences(x_train_seq, maxlen=100)
x_test = sequence.pad_sequences(x_test_seq, maxlen=100)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Imdb_MLP")

from keras.datasets import imdb
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

np.random.seed(10)

import re

re_tag = re.compile(r"<[^>]+>")


def rm_tags(text):
    return re_tag.sub("", text)


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print("read", filetype, "files:", len(file_list))

    all_labels = [1] * 12500 + [0] * 12500

    all_texts = []

    for fi in file_list:
        with open(fi, encoding="utf8") as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")

# read train files: 25000

y_test, test_text = read_files("test")

# read test files: 25000

token = Tokenizer(num_words=2000)
token.fit_on_texts(train_text)

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

x_train = sequence.pad_sequences(x_train_seq, maxlen=100)
x_test = sequence.pad_sequences(x_test_seq, maxlen=100)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding

model = Sequential()

model.add(Embedding(output_dim=32, input_dim=2000, input_length=100))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(units=256, activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(units=1, activation="sigmoid"))

model.summary()

# 訓練模型

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

''' NG
train_history = model.fit(
    x_train, y_train, batch_size=100, epochs=10, verbose=2, validation_split=0.2
)


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


# Populating the interactive namespace from numpy and matplotlib

show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_test, y_test, verbose=1)
print(scores[1])

# 0.80288000000000004

# 預測機率

probility = model.predict(x_test)

print(probility[:10])

for p in probility[12500:12510]:
    print(p)

# 預測結果

predict = model.predict_classes(x_test)

print(predict[:10])

predict_classes = predict.reshape(-1)
print(predict_classes[:10])

# 查看預測結果

SentimentDict = {1: "正面的", 0: "負面的"}


def display_test_Sentiment(i):
    print(test_text[i])
    print(
        "標籤label:", SentimentDict[y_test[i]], "預測結果:", SentimentDict[predict_classes[i]]
    )


display_test_Sentiment(2)

"""
As a recreational golfer with some knowledge of the sport's history, I was pleased with Disney's sensitivity to the issues of class in golf in the early twentieth century. The movie depicted well the psychological battles that Harry Vardon fought within himself, from his childhood trauma of being evicted to his own inability to break that glass ceiling that prevents him from being accepted as an equal in English golf society. Likewise, the young Ouimet goes through his own class struggles, being a mere caddie in the eyes of the upper crust Americans who scoff at his attempts to rise above his standing. What I loved best, however, is how this theme of class is manifested in the characters of Ouimet's parents. His father is a working-class drone who sees the value of hard work but is intimidated by the upper class; his mother, however, recognizes her son's talent and desire and encourages him to pursue his dream of competing against those who think he is inferior.Finally, the golf scenes are well photographed. Although the course used in the movie was not the actual site of the historical tournament, the little liberties taken by Disney do not detract from the beauty of the film. There's one little Disney moment at the pool table; otherwise, the viewer does not really think Disney. The ending, as in "Miracle," is not some Disney creation, but one that only human history could have written.
標籤label: 正面的 預測結果: 正面的
"""

print(predict_classes[12500:12510])

display_test_Sentiment(12502)

"""
First of all I hate those moronic rappers, who could'nt act if they had a gun pressed against their foreheads. All they do is curse and shoot each other and acting like cliché'e version of gangsters.The movie doesn't take more than five minutes to explain what is going on before we're already at the warehouse There is not a single sympathetic character in this movie, except for the homeless guy, who is also the only one with half a brain.Bill Paxton and William Sadler are both hill billies and Sadlers character is just as much a villain as the gangsters. I did'nt like him right from the start.The movie is filled with pointless violence and Walter Hills specialty: people falling through windows with glass flying everywhere. There is pretty much no plot and it is a big problem when you root for no-one. Everybody dies, except from Paxton and the homeless guy and everybody get what they deserve.The only two black people that can act is the homeless guy and the junkie but they're actors by profession, not annoying ugly brain dead rappers.Stay away from this crap and watch 48 hours 1 and 2 instead. At lest they have characters you care about, a sense of humor and nothing but real actors in the cast.
標籤label: 負面的 預測結果: 負面的
"""

# 預測新的影評

input_text = """
Oh dear, oh dear, oh dear: where should I start folks. I had low expectations already because I hated each and every single trailer so far, but boy did Disney make a blunder here. I'm sure the film will still make a billion dollars - hey: if Transformers 11 can do it, why not Belle? - but this film kills every subtle beautiful little thing that had made the original special, and it does so already in the very early stages. It's like the dinosaur stampede scene in Jackson's King Kong: only with even worse CGI (and, well, kitchen devices instead of dinos).
The worst sin, though, is that everything (and I mean really EVERYTHING) looks fake. What's the point of making a live-action version of a beloved cartoon if you make every prop look like a prop? I know it's a fairy tale for kids, but even Belle's village looks like it had only recently been put there by a subpar production designer trying to copy the images from the cartoon. There is not a hint of authenticity here. Unlike in Jungle Book, where we got great looking CGI, this really is the by-the-numbers version and corporate filmmaking at its worst. Of course it's not really a "bad" film; those 200 million blockbusters rarely are (this isn't 'The Room' after all), but it's so infuriatingly generic and dull - and it didn't have to be. In the hands of a great director the potential for this film would have been huge.
Oh and one more thing: bad CGI wolves (who actually look even worse than the ones in Twilight) is one thing, and the kids probably won't care. But making one of the two lead characters - Beast - look equally bad is simply unforgivably stupid. No wonder Emma Watson seems to phone it in: she apparently had to act against an guy with a green-screen in the place where his face should have been. 
"""

input_seq = token.texts_to_sequences([input_text])

print(len(input_seq[0]))

# 285

pad_input_seq = sequence.pad_sequences(input_seq, maxlen=100)

print(len(pad_input_seq[0]))

predict_result = model.predict_classes(pad_input_seq)

print(predict_result[0][0])

SentimentDict[predict_result[0][0]]

# "負面的"


def predict_review(input_text):
    input_seq = token.texts_to_sequences([input_text])
    pad_input_seq = sequence.pad_sequences(input_seq, maxlen=100)
    predict_result = model.predict_classes(pad_input_seq)
    print(SentimentDict[predict_result[0][0]])


# http://www.imdb.com/title/tt2771200/
# http://www.imdb.com/title/tt2771200

predict_review(
    """
It's hard to believe that the same talented director who made the influential cult action classic The Road Warrior had anything to do with this disaster.
Road Warrior was raw, gritty, violent and uncompromising, and this movie is the exact opposite. It's like Road Warrior for kids who need constant action in their movies.
This is the movie. The good guys get into a fight with the bad guys, outrun them, they break down in their vehicle and fix it. Rinse and repeat. The second half of the movie is the first half again just done faster.
The Road Warrior may have been a simple premise but it made you feel something, even with it's opening narration before any action was even shown. And the supporting characters were given just enough time for each of them to be likable or relatable.
In this movie there is absolutely nothing and no one to care about. We're supposed to care about the characters because... well we should. George Miller just wants us to, and in one of the most cringe worthy moments Charlize Theron's character breaks down while dramatic music plays to try desperately to make us care.
Tom Hardy is pathetic as Max. One of the dullest leading men I've seen in a long time. There's not one single moment throughout the entire movie where he comes anywhere near reaching the same level of charisma Mel Gibson did in the role. Gibson made more of an impression just eating a tin of dog food. I'm still confused as to what accent Hardy was even trying to do.
I was amazed that Max has now become a cartoon character as well. Gibson's Max was a semi-realistic tough guy who hurt, bled, and nearly died several times. Now he survives car crashes and tornadoes with ease?
In the previous movies, fuel and guns and bullets were rare. Not anymore. It doesn't even seem Post-Apocalyptic. There's no sense of desperation anymore and everything is too glossy looking. And the main villain's super model looking wives with their perfect skin are about as convincing as apocalyptic survivors as Hardy's Australian accent is. They're so boring and one-dimensional, George Miller could have combined them all into one character and you wouldn't miss anyone.
Some of the green screen is very obvious and fake looking, and the CGI sandstorm is laughably bad. It wouldn't look out of place in a Pixar movie.
There's no tension, no real struggle, or any real dirt and grit that Road Warrior had. Everything George Miller got right with that masterpiece he gets completely wrong here. 
"""
)

# 負面的

predict_review(
    """
Sure, I'm a huge film snob who (on the surface) only likes artsy-fartsy foreign films from before the 60's, but that hasn't stopped me from loving Disney's Beauty & The Beast; in fact, it's probably my favorite American animated film and is easily Disney's finest work. It's beautiful, it's breathtaking, it's warm, it's hilarious, it's captivating, and, in Disney fashion, it's magical. When I learned that Disney would be remaking their classic films, B&TB was undeniably the best wrapped package. How could they go wrong?
Oh man, they went wrong.
First thing's first: this film is so flat. The directing was dull and uninteresting throughout the entire film and it honestly felt like one of the Twilight sequels...and then I looked it up and found out that, yes, director Bill Condon was the man behind Breaking Dawn parts 1 & 2. Every shot looks bored and uninterested, which contrasts heavily with the original animated film that was constantly popping with vibrancy. The script too is boring because it's almost a complete remake of the original, though I guess most people won't mind that.
Next: the CGI is horrid. Although I didn't care for The Jungle Book from last year, I could at least admit that the CGI was breathtaking. The same cant be said for this film. Characters like Lumière, Cogsworth, Mrs Potts, and most of the cursed appliances have very strange, lifeless faces that are pretty off putting to be looking at for such a long time. All of the sets too look artificial and fake, especially the town towards the beginning. However, the biggest offender is easily and infuriatingly the character that mattered most: The Beast. The CGI on the Beast's face is so distracting that it completely takes you out of the film. His eyes are completely devoid of soul, and his mouth is a gaping video game black hole of fiction. Klaus Kinski looked much better in the Faerie Tale Theatre episode of Beauty & The Beast, and that was a 1984 TV show episode. But do you know why it looked better? Because it was an actual face with actual eyes, not some video game computerized synthetic monstrosity. When will studios learn that practical effects will always top CGI?
Finally: wasted casting. Emma Watson is beautiful, but she's no Belle. She is completely devoid of the warmth and humanity that made the animated Belle so beloved. Instead, she is cold and heartless throughout most of the film. Kevin Kline is 100% wasted and does nothing except look old. Ian McKellan, Ewan McGregor, Emma Thompson, and even Dan Stevens as the Beast are very expendable and could've been played by anyone else. The only good characters are Gaston and LeFou, mostly because they are fun and played by actors who breathe new life into their original shapes. If anything, this film should've been about Gaston and LeFou, but that would never happen because that would mean Disney couldn't cater to blind nostalgic 90's kids.
Overall, this film is a complete bore. It could've been better if even the special effects were good, but the CGI in particular is horrendous. I'm all for Disney remaking their nostalgia- catering 90's films, but they need to be interesting. This film, sadly, is not. Even the Christmas sequel is better than this film because it's at least something. 
"""
)

# 負面的

predict_review(
    """
I was really looking forward to this film. Not only has Disney recently made excellent live-action versions of their animated masterpieces (Jungle Book, Cinderella), but the cast alone (Emma Watson, Ian McKellen, Kevin Kline) already seemed to make this one a sure hit. Well, not so much as it turns out.
Some of the animation is fantastic, but because characters like Cogsworth (the clock), Lumière (the candelabra) and Chip (the little tea cup) now look "realistic", they lose a lot of their animated predecessors' charm and actually even look kind of creepy at times. And ironically - unlike in the animated original - in this new realistic version they only have very limited facial expressions (which is a creative decision I can't for the life of me understand).
Even when it works: there can be too much of a good thing. The film is overstuffed with lush production design and cgi (which is often weirdly artificial looking though) but sadly lacking in charm and genuine emotion. If this were a music album, I'd say it is "over-produced" and in need of more soul and swing. The great voice talent in some cases actually seems wasted, because it drowns in a sea of visual effects that numbs all senses. The most crucial thing that didn't work for me, though, is the Beast. He just never looks convincing. The eyes somehow don't look like real eyes and they're always slightly off.
On the positive side, I really liked Gaston, and the actor who played him, Luke Evans, actually gave the perhaps most energized performance of all. Kevin Kline as Belle's father has little to do but to look fatherly and old, but he makes the most of his part. Speaking of Belle, now that I've seen the film, I think her role was miscast. I think someone like Rachel McAdams would actually have been a more natural, lively and perhaps a bit more feisty Belle than Emma Watson.
If you love the original, you might want to give this one a pass, it's really not that good (although at least the songs were OK). Also, I'd think twice before bringing small children; without cute animated faces, all those "realistic" looking creatures and devices can be rather frightening for a child. """
)

# 正面的

predict_review(
    """
Up front: I'm probably not the right audience for this film. I only went because I was invited, and I wouldn't have gone to check this one out otherwise.
Firstly, some of the production values are really beautiful and reminded me of the animated classic in a good way. Also, the voice cast for the clock and the kitchen devices are great.
Secondly, the actors, well... this may sound kind of harsh, but I've never seen Emma Watson act so stiff in a movie. Her performance is wooden, which is pretty bad considering she's supposed to be the heart of the film. Also, she probably won't start a singing career anytime soon.
Thirdly (and most importantly), Beast. That's where they really dropped the ball. Giving him a lifeless CGI face was an unforgivable mistake, and it's such a constant distraction that I could never really get into the movie.
Overall, I'm afraid I wouldn't recommend this movie, at least not to adults. I'm sure most kids would enjoy it though, and it's not really a bad film: just a very mediocre one. 6 stars out of 10. 
"""
)

# 負面的

predict_review(
    """
Full disclosure, I didn't think the first movie was as bad as it was made out to be. It wasn't good in almost any sense, but it was to be expected given the combination of source material, resources and constraints.
That said, this sequel is 20x better than the first. Having established the characters in the first movie, the actors seem to be able to act now comfortably in their parts. The story becomes much more nuanced with plenty of dynamics on the go.
SPOILERS from now on
Can they maintain a "vanilla" relationship? Is he going to become controlling again and ruin things? Will she let it get out of control and ruin things also or stay on it? Who is that stalky girl and what happened to her exactly? what about his mother? and that ex of his? Will something occur with her infatuated boss?
On top of all of this, I realised while watching that the series was never about a bizarre sadist control freak, it's actually about all men and the story of a woman trying to find the balance between accepting or desiring the dominant behaviour of the male archetype and maintaining strength and independence in such a relationship.
While of course the fact that he is rich, while possibly relating to the power struggle, looks like it is going to be more and more used for generating further drama. The romance is much more evident in this movie to/ 
"""
)

# 正面的

# serialize model to JSON

model_json = model.to_json()
with open("SaveModel/Imdb_RNN_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("SaveModel/Imdb_RNN_model.h5")
print("Saved model to disk")

# Saved model to disk
NG '''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Imdb_MLP_Large")

from keras.datasets import imdb
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

np.random.seed(10)

import re

re_tag = re.compile(r"<[^>]+>")


def rm_tags(text):
    return re_tag.sub("", text)


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print("read", filetype, "files:", len(file_list))

    all_labels = [1] * 12500 + [0] * 12500

    all_texts = []

    for fi in file_list:
        with open(fi, encoding="utf8") as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")

# read train files: 25000

y_test, test_text = read_files("test")

# read test files: 25000

# 先讀取所有文章建立字典，限制字典的數量為nb_words=3800

token = Tokenizer(num_words=3800)
token.fit_on_texts(train_text)

# 將文字轉為數字序列

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

# 截長補短，讓所有影評所產生的數字序列長度一樣

x_train = sequence.pad_sequences(x_train_seq, maxlen=380)
x_test = sequence.pad_sequences(x_test_seq, maxlen=380)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding

model = Sequential()

model.add(Embedding(output_dim=32, input_dim=3800, input_length=380))
model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(units=256, activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(units=1, activation="sigmoid"))

model.summary()

# 訓練模型

model.compile(
    loss="binary_crossentropy",
    # optimizer='rmsprop',
    optimizer="adam",
    metrics=["accuracy"],
)

''' NG
train_history = model.fit(
    x_train, y_train, batch_size=100, epochs=10, verbose=2, validation_split=0.2
)


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


# Populating the interactive namespace from numpy and matplotlib

show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_test, y_test, verbose=1)
print(scores[1])

# 0.84863999999999995

# 預測機率

probility = model.predict(x_test)

print(probility[:10])

for p in probility[12500:12510]:
    print(p)

# 預測結果

predict = model.predict_classes(x_test)

print(predict.shape)

predict_classes = predict.reshape(25000)
print(predict_classes)

# 查看預測結果

SentimentDict = {1: "正面的", 0: "負面的"}


def display_test_Sentiment(i):
    print(test_text[i])
    print(
        "標籤label:", SentimentDict[y_test[i]], "預測結果:", SentimentDict[predict_classes[i]]
    )


display_test_Sentiment(2)
"""
As a recreational golfer with some knowledge of the sport's history, I was pleased with Disney's sensitivity to the issues of class in golf in the early twentieth century. The movie depicted well the psychological battles that Harry Vardon fought within himself, from his childhood trauma of being evicted to his own inability to break that glass ceiling that prevents him from being accepted as an equal in English golf society. Likewise, the young Ouimet goes through his own class struggles, being a mere caddie in the eyes of the upper crust Americans who scoff at his attempts to rise above his standing. What I loved best, however, is how this theme of class is manifested in the characters of Ouimet's parents. His father is a working-class drone who sees the value of hard work but is intimidated by the upper class; his mother, however, recognizes her son's talent and desire and encourages him to pursue his dream of competing against those who think he is inferior.Finally, the golf scenes are well photographed. Although the course used in the movie was not the actual site of the historical tournament, the little liberties taken by Disney do not detract from the beauty of the film. There's one little Disney moment at the pool table; otherwise, the viewer does not really think Disney. The ending, as in "Miracle," is not some Disney creation, but one that only human history could have written.
標籤label: 正面的 預測結果: 正面的
"""
display_test_Sentiment(3)
"""
I saw this film in a sneak preview, and it is delightful. The cinematography is unusually creative, the acting is good, and the story is fabulous. If this movie does not do well, it won't be because it doesn't deserve to. Before this film, I didn't realize how charming Shia Lebouf could be. He does a marvelous, self-contained, job as the lead. There's something incredibly sweet about him, and it makes the movie even better. The other actors do a good job as well, and the film contains moments of really high suspense, more than one might expect from a movie about golf. Sports movies are a dime a dozen, but this one stands out. This is one I'd recommend to anyone.
標籤label: 正面的 預測結果: 正面的
"""
print(predict_classes[12500:12510])

display_test_Sentiment(12500)
"""
Once again Mr. Costner has dragged out a movie for far longer than necessary. Aside from the terrific sea rescue sequences, of which there are very few I just did not care about any of the characters. Most of us have ghosts in the closet, and Costner's character are realized early on, and then forgotten until much later, by which time I did not care. The character we should really care about is a very cocky, overconfident Ashton Kutcher. The problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a cluttered closet. His only obstacle appears to be winning over Costner. Finally when we are well past the half way point of this stinker, Costner tells us all about Kutcher's ghosts. We are told why Kutcher is driven to be the best with no prior inkling or foreshadowing. No magic here, it was all I could do to keep from turning it off an hour in.
標籤label: 負面的 預測結果: 負面的
"""

# 預測新的影評

input_text = """
Oh dear, oh dear, oh dear: where should I start folks. I had low expectations already because I hated each and every single trailer so far, but boy did Disney make a blunder here. I'm sure the film will still make a billion dollars - hey: if Transformers 11 can do it, why not Belle? - but this film kills every subtle beautiful little thing that had made the original special, and it does so already in the very early stages. It's like the dinosaur stampede scene in Jackson's King Kong: only with even worse CGI (and, well, kitchen devices instead of dinos).
The worst sin, though, is that everything (and I mean really EVERYTHING) looks fake. What's the point of making a live-action version of a beloved cartoon if you make every prop look like a prop? I know it's a fairy tale for kids, but even Belle's village looks like it had only recently been put there by a subpar production designer trying to copy the images from the cartoon. There is not a hint of authenticity here. Unlike in Jungle Book, where we got great looking CGI, this really is the by-the-numbers version and corporate filmmaking at its worst. Of course it's not really a "bad" film; those 200 million blockbusters rarely are (this isn't 'The Room' after all), but it's so infuriatingly generic and dull - and it didn't have to be. In the hands of a great director the potential for this film would have been huge.
Oh and one more thing: bad CGI wolves (who actually look even worse than the ones in Twilight) is one thing, and the kids probably won't care. But making one of the two lead characters - Beast - look equally bad is simply unforgivably stupid. No wonder Emma Watson seems to phone it in: she apparently had to act against an guy with a green-screen in the place where his face should have been. 
"""
input_seq = token.texts_to_sequences([input_text])

print(len(input_seq[0]))

# 297

pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)

print(len(pad_input_seq[0]))

# 380

predict_result = model.predict_classes(pad_input_seq)

print(predict_result)

print(predict_result[0][0])

SentimentDict[predict_result[0][0]]

# '負面的'


def predict_review(input_text):
    input_seq = token.texts_to_sequences([input_text])
    pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)
    predict_result = model.predict_classes(pad_input_seq)
    print(SentimentDict[predict_result[0][0]])


# http://www.imdb.com/title/tt2771200/
# http://www.imdb.com/title/tt2771200

predict_review(
    """
It's hard to believe that the same talented director who made the influential cult action classic The Road Warrior had anything to do with this disaster.
Road Warrior was raw, gritty, violent and uncompromising, and this movie is the exact opposite. It's like Road Warrior for kids who need constant action in their movies.
This is the movie. The good guys get into a fight with the bad guys, outrun them, they break down in their vehicle and fix it. Rinse and repeat. The second half of the movie is the first half again just done faster.
The Road Warrior may have been a simple premise but it made you feel something, even with it's opening narration before any action was even shown. And the supporting characters were given just enough time for each of them to be likable or relatable.
In this movie there is absolutely nothing and no one to care about. We're supposed to care about the characters because... well we should. George Miller just wants us to, and in one of the most cringe worthy moments Charlize Theron's character breaks down while dramatic music plays to try desperately to make us care.
Tom Hardy is pathetic as Max. One of the dullest leading men I've seen in a long time. There's not one single moment throughout the entire movie where he comes anywhere near reaching the same level of charisma Mel Gibson did in the role. Gibson made more of an impression just eating a tin of dog food. I'm still confused as to what accent Hardy was even trying to do.
I was amazed that Max has now become a cartoon character as well. Gibson's Max was a semi-realistic tough guy who hurt, bled, and nearly died several times. Now he survives car crashes and tornadoes with ease?
In the previous movies, fuel and guns and bullets were rare. Not anymore. It doesn't even seem Post-Apocalyptic. There's no sense of desperation anymore and everything is too glossy looking. And the main villain's super model looking wives with their perfect skin are about as convincing as apocalyptic survivors as Hardy's Australian accent is. They're so boring and one-dimensional, George Miller could have combined them all into one character and you wouldn't miss anyone.
Some of the green screen is very obvious and fake looking, and the CGI sandstorm is laughably bad. It wouldn't look out of place in a Pixar movie.
There's no tension, no real struggle, or any real dirt and grit that Road Warrior had. Everything George Miller got right with that masterpiece he gets completely wrong here. 
"""
)

# 正面的

predict_review(
    """
Sure, I'm a huge film snob who (on the surface) only likes artsy-fartsy foreign films from before the 60's, but that hasn't stopped me from loving Disney's Beauty & The Beast; in fact, it's probably my favorite American animated film and is easily Disney's finest work. It's beautiful, it's breathtaking, it's warm, it's hilarious, it's captivating, and, in Disney fashion, it's magical. When I learned that Disney would be remaking their classic films, B&TB was undeniably the best wrapped package. How could they go wrong?
Oh man, they went wrong.
First thing's first: this film is so flat. The directing was dull and uninteresting throughout the entire film and it honestly felt like one of the Twilight sequels...and then I looked it up and found out that, yes, director Bill Condon was the man behind Breaking Dawn parts 1 & 2. Every shot looks bored and uninterested, which contrasts heavily with the original animated film that was constantly popping with vibrancy. The script too is boring because it's almost a complete remake of the original, though I guess most people won't mind that.
Next: the CGI is horrid. Although I didn't care for The Jungle Book from last year, I could at least admit that the CGI was breathtaking. The same cant be said for this film. Characters like Lumière, Cogsworth, Mrs Potts, and most of the cursed appliances have very strange, lifeless faces that are pretty off putting to be looking at for such a long time. All of the sets too look artificial and fake, especially the town towards the beginning. However, the biggest offender is easily and infuriatingly the character that mattered most: The Beast. The CGI on the Beast's face is so distracting that it completely takes you out of the film. His eyes are completely devoid of soul, and his mouth is a gaping video game black hole of fiction. Klaus Kinski looked much better in the Faerie Tale Theatre episode of Beauty & The Beast, and that was a 1984 TV show episode. But do you know why it looked better? Because it was an actual face with actual eyes, not some video game computerized synthetic monstrosity. When will studios learn that practical effects will always top CGI?
Finally: wasted casting. Emma Watson is beautiful, but she's no Belle. She is completely devoid of the warmth and humanity that made the animated Belle so beloved. Instead, she is cold and heartless throughout most of the film. Kevin Kline is 100% wasted and does nothing except look old. Ian McKellan, Ewan McGregor, Emma Thompson, and even Dan Stevens as the Beast are very expendable and could've been played by anyone else. The only good characters are Gaston and LeFou, mostly because they are fun and played by actors who breathe new life into their original shapes. If anything, this film should've been about Gaston and LeFou, but that would never happen because that would mean Disney couldn't cater to blind nostalgic 90's kids.
Overall, this film is a complete bore. It could've been better if even the special effects were good, but the CGI in particular is horrendous. I'm all for Disney remaking their nostalgia- catering 90's films, but they need to be interesting. This film, sadly, is not. Even the Christmas sequel is better than this film because it's at least something. 
"""
)

# 負面的

predict_review(
    """
I was really looking forward to this film. Not only has Disney recently made excellent live-action versions of their animated masterpieces (Jungle Book, Cinderella), but the cast alone (Emma Watson, Ian McKellen, Kevin Kline) already seemed to make this one a sure hit. Well, not so much as it turns out.
Some of the animation is fantastic, but because characters like Cogsworth (the clock), Lumière (the candelabra) and Chip (the little tea cup) now look "realistic", they lose a lot of their animated predecessors' charm and actually even look kind of creepy at times. And ironically - unlike in the animated original - in this new realistic version they only have very limited facial expressions (which is a creative decision I can't for the life of me understand).
Even when it works: there can be too much of a good thing. The film is overstuffed with lush production design and cgi (which is often weirdly artificial looking though) but sadly lacking in charm and genuine emotion. If this were a music album, I'd say it is "over-produced" and in need of more soul and swing. The great voice talent in some cases actually seems wasted, because it drowns in a sea of visual effects that numbs all senses. The most crucial thing that didn't work for me, though, is the Beast. He just never looks convincing. The eyes somehow don't look like real eyes and they're always slightly off.
On the positive side, I really liked Gaston, and the actor who played him, Luke Evans, actually gave the perhaps most energized performance of all. Kevin Kline as Belle's father has little to do but to look fatherly and old, but he makes the most of his part. Speaking of Belle, now that I've seen the film, I think her role was miscast. I think someone like Rachel McAdams would actually have been a more natural, lively and perhaps a bit more feisty Belle than Emma Watson.
If you love the original, you might want to give this one a pass, it's really not that good (although at least the songs were OK). Also, I'd think twice before bringing small children; without cute animated faces, all those "realistic" looking creatures and devices can be rather frightening for a child. """
)

# 正面的

predict_review(
    """
Up front: I'm probably not the right audience for this film. I only went because I was invited, and I wouldn't have gone to check this one out otherwise.
Firstly, some of the production values are really beautiful and reminded me of the animated classic in a good way. Also, the voice cast for the clock and the kitchen devices are great.
Secondly, the actors, well... this may sound kind of harsh, but I've never seen Emma Watson act so stiff in a movie. Her performance is wooden, which is pretty bad considering she's supposed to be the heart of the film. Also, she probably won't start a singing career anytime soon.
Thirdly (and most importantly), Beast. That's where they really dropped the ball. Giving him a lifeless CGI face was an unforgivable mistake, and it's such a constant distraction that I could never really get into the movie.
Overall, I'm afraid I wouldn't recommend this movie, at least not to adults. I'm sure most kids would enjoy it though, and it's not really a bad film: just a very mediocre one. 6 stars out of 10. 
"""
)

# 負面的

predict_review(
    """
Full disclosure, I didn't think the first movie was as bad as it was made out to be. It wasn't good in almost any sense, but it was to be expected given the combination of source material, resources and constraints.
That said, this sequel is 20x better than the first. Having established the characters in the first movie, the actors seem to be able to act now comfortably in their parts. The story becomes much more nuanced with plenty of dynamics on the go.
SPOILERS from now on
Can they maintain a "vanilla" relationship? Is he going to become controlling again and ruin things? Will she let it get out of control and ruin things also or stay on it? Who is that stalky girl and what happened to her exactly? what about his mother? and that ex of his? Will something occur with her infatuated boss?
On top of all of this, I realised while watching that the series was never about a bizarre sadist control freak, it's actually about all men and the story of a woman trying to find the balance between accepting or desiring the dominant behaviour of the male archetype and maintaining strength and independence in such a relationship.
While of course the fact that he is rich, while possibly relating to the power struggle, looks like it is going to be more and more used for generating further drama. The romance is much more evident in this movie to/ 
"""
)

# 正面的

# serialize model to JSON

model_json = model.to_json()
with open("SaveModel/Imdb_RNN_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("SaveModel/Imdb_RNN_model.h5")
print("Saved model to disk")

# Saved model to disk
NG '''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Imdb_RNN")

from keras.datasets import imdb
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

import re

re_tag = re.compile(r"<[^>]+>")


def rm_tags(text):
    return re_tag.sub("", text)


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print("read", filetype, "files:", len(file_list))

    all_labels = [1] * 12500 + [0] * 12500

    all_texts = []

    for fi in file_list:
        with open(fi, encoding="utf8") as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")

# read train files: 25000

y_test, test_text = read_files("test")

# read test files: 25000

token = Tokenizer(num_words=3800)
token.fit_on_texts(train_text)

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

x_train = sequence.pad_sequences(x_train_seq, maxlen=380)
x_test = sequence.pad_sequences(x_test_seq, maxlen=380)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding

# from keras.layers.recurrent import SimpleRNN
from keras.layers import SimpleRNN

model = Sequential()

model.add(Embedding(output_dim=32, input_dim=3800, input_length=380))
model.add(Dropout(0.35))

model.add(SimpleRNN(units=16))

model.add(Dense(units=256, activation="relu"))
model.add(Dropout(0.35))

model.add(Dense(units=1, activation="sigmoid"))

model.summary()

# 訓練模型

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
''' NG
train_history = model.fit(
    x_train, y_train, batch_size=100, epochs=10, verbose=2, validation_split=0.2
)


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

scores = model.evaluate(x_test, y_test, verbose=1)
print(scores[1])

# 0.83443999999999996

# 預測機率

probility = model.predict(x_test)

print(probility[:10])


for p in probility[12500:12510]:
    print(p)

# 預測結果

predict = model.predict_classes(x_test)

print(predict[:10])

print(predict.shape)

# (25000, 1)

predict_classes = predict.reshape(25000)
print(predict_classes)

# array([1, 1, 1, ..., 0, 1, 1])

# 查看預測結果

SentimentDict = {1: "正面的", 0: "負面的"}


def display_test_Sentiment(i):
    print(test_text[i])
    print(
        "label真實值:",
        SentimentDict[y_test[i]],
        "預測結果:",
        SentimentDict[predict_classes[i]],
    )


display_test_Sentiment(2)
"""
As a recreational golfer with some knowledge of the sport's history, I was pleased with Disney's sensitivity to the issues of class in golf in the early twentieth century. The movie depicted well the psychological battles that Harry Vardon fought within himself, from his childhood trauma of being evicted to his own inability to break that glass ceiling that prevents him from being accepted as an equal in English golf society. Likewise, the young Ouimet goes through his own class struggles, being a mere caddie in the eyes of the upper crust Americans who scoff at his attempts to rise above his standing. What I loved best, however, is how this theme of class is manifested in the characters of Ouimet's parents. His father is a working-class drone who sees the value of hard work but is intimidated by the upper class; his mother, however, recognizes her son's talent and desire and encourages him to pursue his dream of competing against those who think he is inferior.Finally, the golf scenes are well photographed. Although the course used in the movie was not the actual site of the historical tournament, the little liberties taken by Disney do not detract from the beauty of the film. There's one little Disney moment at the pool table; otherwise, the viewer does not really think Disney. The ending, as in "Miracle," is not some Disney creation, but one that only human history could have written.
label真實值: 正面的 預測結果: 正面的
"""
display_test_Sentiment(3)
"""
I saw this film in a sneak preview, and it is delightful. The cinematography is unusually creative, the acting is good, and the story is fabulous. If this movie does not do well, it won't be because it doesn't deserve to. Before this film, I didn't realize how charming Shia Lebouf could be. He does a marvelous, self-contained, job as the lead. There's something incredibly sweet about him, and it makes the movie even better. The other actors do a good job as well, and the film contains moments of really high suspense, more than one might expect from a movie about golf. Sports movies are a dime a dozen, but this one stands out. This is one I'd recommend to anyone.
label真實值: 正面的 預測結果: 正面的
"""
print(predict_classes[12500:12510])

display_test_Sentiment(12502)
"""
First of all I hate those moronic rappers, who could'nt act if they had a gun pressed against their foreheads. All they do is curse and shoot each other and acting like cliché'e version of gangsters.The movie doesn't take more than five minutes to explain what is going on before we're already at the warehouse There is not a single sympathetic character in this movie, except for the homeless guy, who is also the only one with half a brain.Bill Paxton and William Sadler are both hill billies and Sadlers character is just as much a villain as the gangsters. I did'nt like him right from the start.The movie is filled with pointless violence and Walter Hills specialty: people falling through windows with glass flying everywhere. There is pretty much no plot and it is a big problem when you root for no-one. Everybody dies, except from Paxton and the homeless guy and everybody get what they deserve.The only two black people that can act is the homeless guy and the junkie but they're actors by profession, not annoying ugly brain dead rappers.Stay away from this crap and watch 48 hours 1 and 2 instead. At lest they have characters you care about, a sense of humor and nothing but real actors in the cast.
label真實值: 負面的 預測結果: 負面的
"""
# 預測新的影評

input_text = """
I can't vote because I have not watched this movie yet. I've been wanting to watch this movie since the time they announced making it which is about 2 years ago (!)
I was planning to go with the family to see the anticipated movie but my nieces had school exams at the opening time so we all decided to wait for the next weekend. I was utterly shocked to learn yesterday that they pulled the movie from the Kuwaiti theaters "temporarily" so that the outrageous censorship system can remove some unwanted scenes.
The controversial gay "moment" according to my online research is barely there, so I can't find any logical reason for all the fuss that's been going on. And it was bad enough when fanatics and haters tried (in vain) to kill the movie with low ratings and negative reviews even before it was in the cinemas and I'm pretty sure most of those trolls never got the chance to watch the movie at that time.
Based on the trailers, I think the movie is very promising and entertaining and you can't simply overlook the tremendous efforts made to bring this beloved tale to life. To knock down hundreds of people's obvious hard work with unprofessional critique and negative reviews just for the sake of hatred is unfathomable. I hope people won't judge a movie before having the experience of watching it in the first place.
Impatiently waiting for the Kuwaiti cinemas to bring back the movie... 
"""

input_seq = token.texts_to_sequences([input_text])

print(input_seq[0])

# [9, 187, 2310, 83, 9, 24, 20, 292, 10, 16, 242, 203, 73, 1780, 5, 102, 10, 16, 233, 1, 54, 32, 227, 8, 59, 6, 40, 237, 149, 592, 9, 12, 3599, 5, 136, 15, 1, 219, 5, 63, 1, 16, 17, 57, 65, 391, 29, 1, 632, 54, 34, 71, 28, 867, 5, 854, 14, 1, 372, 2488, 9, 12, 1247, 2407, 5, 848, 11, 32, 1907, 1, 16, 35, 1, 2257, 34, 11, 1, 3585, 1503, 66, 45, 135, 1, 3112, 989, 557, 1787, 5, 57, 2297, 6, 1196, 46, 34, 9, 187, 165, 97, 3683, 279, 14, 28, 1, 194, 73, 166, 19, 2, 8, 12, 75, 191, 50, 2, 799, 7, 5, 511, 1, 16, 15, 360, 2891, 2, 1560, 852, 56, 154, 8, 12, 7, 1, 2, 142, 180, 248, 87, 4, 144, 111, 184, 1, 577, 5, 102, 1, 16, 29, 11, 54, 444, 19, 1, 9, 100, 1, 16, 6, 51, 2428, 2, 438, 2, 21, 187, 327, 1, 3515, 2047, 89, 5, 717, 10, 2760, 782, 5, 109, 5, 3290, 176, 3097, 4, 2857, 573, 250, 153, 15, 2, 1560, 852, 39, 14, 1, 2107, 4, 3677, 6, 9, 436, 80, 524, 1918, 3, 16, 154, 256, 1, 581, 4, 145, 8, 7, 1, 82, 269, 1061, 14, 1, 5, 717, 141, 1, 16]

print(len(input_seq[0]))

# 223

pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)

print(len(pad_input_seq[0]))

# 380

predict_result = model.predict_classes(pad_input_seq)

print(predict_result)

print(array([[0]]))

predict_result[0][0]

# 0

SentimentDict[predict_result[0][0]]

# '負面的'


def predict_review(input_text):
    input_seq = token.texts_to_sequences([input_text])
    pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)
    predict_result = model.predict_classes(pad_input_seq)
    print(SentimentDict[predict_result[0][0]])


# http://www.imdb.com/title/tt2771200/
# http://www.imdb.com/title/tt2771200

predict_review(
    """
As a fan of the original Disney film (Personally I feel it's their masterpiece) I was taken aback to the fact that a new version was in the making. Still excited I had high hopes for the film. Most of was shattered in the first 10 minutes. Campy acting with badly performed singing starts off a long journey holding hands with some of the worst CGI Hollywood have managed to but to screen in ages.
A film that is over 50% GCI, should focus on making that part believable, unfortunately for this film, it's far from that. It looks like the original film was ripped apart frame by frame and the beautiful hand-painted drawings have been replaced with digital caricatures. Besides CGI that is bad, it's mostly creepy. As the little teacup boy will give me nightmares for several nights to come. Emma Watson plays the same character as she always does, with very little acting effort and very little conviction as Belle. Although I can see why she was cast in the film based on merits, she is far from the right choice for the role. Dan Stevens does alright under as some motion captured dead-eyed Beast, but his performance feels flat as well. Luke Evans makes for a great pompous Gaston, but a character that has little depth doesn't really make for a great viewing experience. Josh Gad is a great comic relief just like the original movie's LeFou. Other than that, none of the cast stands out enough for me to remember them. Human or CHI creature. I was just bored through out the whole experience. And for a project costing $160 000 000, I can see why the PR department is pushing it so hard because they really need to get some cash back on this pile of wet stinky CGI-fur!
All and all, I might be bias from really loving Disney's first adaptation. That for me marks the high-point of all their work, perfectly combining the skills of their animators along with some CGI in a majestic blend. This film however is more like the bucket you wash off your paintbrush in, it has all the same colors, but muddled with water and to thin to make a captivating story from. The film is quite frankly not worth your time, you would be better off watching the original one more time. 
"""
)

# 正面的

predict_review(
    """
I was really looking forward to this film. Not only has Disney recently made excellent live-action versions of their animated masterpieces (Jungle Book, Cinderella), but the cast alone (Emma Watson, Ian McKellen, Kevin Kline) already seemed to make this one a sure hit. Well, not so much as it turns out.
Some of the animation is fantastic, but because characters like Cogsworth (the clock), Lumière (the candelabra) and Chip (the little tea cup) now look "realistic", they lose a lot of their animated predecessors' charm and actually even look kind of creepy at times. And ironically - unlike in the animated original - in this new realistic version they only have very limited facial expressions (which is a creative decision I can't for the life of me understand).
Even when it works: there can be too much of a good thing. The film is overstuffed with lush production design and cgi (which is often weirdly artificial looking though) but sadly lacking in charm and genuine emotion. If this were a music album, I'd say it is "over-produced" and in need of more soul and swing. The great voice talent in some cases actually seems wasted, because it drowns in a sea of visual effects that numbs all senses. The most crucial thing that didn't work for me, though, is the Beast. He just never looks convincing. The eyes somehow don't look like real eyes and they're always slightly off.
On the positive side, I really liked Gaston, and the actor who played him, Luke Evans, actually gave the perhaps most energized performance of all. Kevin Kline as Belle's father has little to do but to look fatherly and old, but he makes the most of his part. Speaking of Belle, now that I've seen the film, I think her role was miscast. I think someone like Rachel McAdams would actually have been a more natural, lively and perhaps a bit more feisty Belle than Emma Watson.
If you love the original, you might want to give this one a pass, it's really not that good (although at least the songs were OK). Also, I'd think twice before bringing small children; without cute animated faces, all those "realistic" looking creatures and devices can be rather frightening for a child. """
)

# 正面的

predict_review(
    """
The original Beauty and the Beast was my favorite cartoon as a kid but it did have major plot holes. Why had no one else ever seen the castle or knew where it was? Didn't anyone miss the people who were cursed? All of that gets an explanation when the enchantress places her curse in the beginning. Why did Belle and her Father move to a small town? Her mother died and the father thought it as best to leave. I love the new songs and added lyrics to the originals. I like the way the cgi beast looks (just the face is CGi). I think Emma Watson is a perfect Belle who is outspoken, fearless, and different. The set design is perfect for the era in France.
I know a lot of people disagree but I found this remake with all its changes to be more enchanting, beautiful, and complete than the original 1991 movie. To each his own but I think everyone should see it for themselves. 
"""
)

# 正面的

predict_review(
    """
"Beauty and the Beast" was stunning and gorgeous. Beautifully and artfully performed. Dazzlingly colorful and charming. Fresh and lighthearted. Wonderfully and magically enthralling. I laughed, I cried, I floated along with the music, I bawled and bawled as the spellbinding elegance and splendor took me to another place and time. I was 5 years old again enjoying the Wonderful World of Magic that is Disney, as if for the first time. I will gladly spend my money over and over to see that magic unfold. I willingly and happily concede Emma Watson to be Belle, for this generation of children, instead of Hermione. She has earned her place as a Disney princess and I applaud everyone who had a part in this piece of magic. Truly, Disney knows how to make us all children again. 
"""
)

# 正面的

# serialize model to JSON

model_json = model.to_json()
with open("SaveModel/Imdb_RNN_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("SaveModel/Imdb_RNN_model.h5")
print("Saved model to disk")

# Saved model to disk

# [1.02,2.03,-1.2,2,2],[1,2.1,3,2.2,3.4,3.6]

# ([1.02, 2.03, -1.2, 2, 2], [1, 2.1, 3, 2.2, 3.4, 3.6])
NG '''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Keras_Imdb_LSTM")

from keras.datasets import imdb
from keras.preprocessing import sequence
from tensorflow.keras.preprocessing.text import Tokenizer

np.random.seed(10)

import re

re_tag = re.compile(r"<[^>]+>")


def rm_tags(text):
    return re_tag.sub("", text)


def read_files(filetype):
    path = "data/aclImdb/"
    file_list = []

    positive_path = path + filetype + "/pos/"
    for f in os.listdir(positive_path):
        file_list += [positive_path + f]

    negative_path = path + filetype + "/neg/"
    for f in os.listdir(negative_path):
        file_list += [negative_path + f]

    print("read", filetype, "files:", len(file_list))

    all_labels = [1] * 12500 + [0] * 12500

    all_texts = []

    for fi in file_list:
        with open(fi, encoding="utf8") as file_input:
            all_texts += [rm_tags(" ".join(file_input.readlines()))]

    return all_labels, all_texts


y_train, train_text = read_files("train")

# read train files: 25000

y_test, test_text = read_files("test")

# read test files: 25000

# 先讀取所有文章建立字典，限制字典的數量為nb_words=2000

token = Tokenizer(num_words=3800)
token.fit_on_texts(train_text)

# 將文字轉為數字序列

x_train_seq = token.texts_to_sequences(train_text)
x_test_seq = token.texts_to_sequences(test_text)

# 截長補短，讓所有影評所產生的數字序列長度一樣

x_train = sequence.pad_sequences(x_train_seq, maxlen=380)
x_test = sequence.pad_sequences(x_test_seq, maxlen=380)

# 建立模型

from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Embedding
from keras.layers import LSTM

model = Sequential()

model.add(Embedding(output_dim=32, input_dim=3800, input_length=380))
model.add(Dropout(0.2))

model.add(LSTM(32))

model.add(Dense(units=256, activation="relu"))
model.add(Dropout(0.2))

model.add(Dense(units=1, activation="sigmoid"))

model.summary()

# 訓練模型

model.compile(
    loss="binary_crossentropy",
    # optimizer='rmsprop',
    optimizer="adam",
    metrics=["accuracy"],
)

''' NG
train_history = model.fit(
    x_train, y_train, batch_size=100, epochs=10, verbose=2, validation_split=0.2
)


def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train History")
    plt.ylabel(train)
    plt.xlabel("Epoch")
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


# Populating the interactive namespace from numpy and matplotlib

show_train_history(train_history, "accuracy", "val_accuracy")

show_train_history(train_history, "loss", "val_loss")

# 評估模型準確率

scores = model.evaluate(x_test, y_test, verbose=1)
print(scores[1])

# 0.85792000000000002

# 預測機率

probility = model.predict(x_test)

print(probility[:10])

for p in probility[12500:12510]:
    print(p)

# 預測結果

predict = model.predict_classes(x_test)

print(predict.shape)

predict_classes = predict.reshape(25000)
print(predict_classes)

# 查看預測結果

SentimentDict = {1: "正面的", 0: "負面的"}


def display_test_Sentiment(i):
    print(test_text[i])
    print(
        "標籤label:", SentimentDict[y_test[i]], "預測結果:", SentimentDict[predict_classes[i]]
    )


display_test_Sentiment(2)
"""
As a recreational golfer with some knowledge of the sport's history, I was pleased with Disney's sensitivity to the issues of class in golf in the early twentieth century. The movie depicted well the psychological battles that Harry Vardon fought within himself, from his childhood trauma of being evicted to his own inability to break that glass ceiling that prevents him from being accepted as an equal in English golf society. Likewise, the young Ouimet goes through his own class struggles, being a mere caddie in the eyes of the upper crust Americans who scoff at his attempts to rise above his standing. What I loved best, however, is how this theme of class is manifested in the characters of Ouimet's parents. His father is a working-class drone who sees the value of hard work but is intimidated by the upper class; his mother, however, recognizes her son's talent and desire and encourages him to pursue his dream of competing against those who think he is inferior.Finally, the golf scenes are well photographed. Although the course used in the movie was not the actual site of the historical tournament, the little liberties taken by Disney do not detract from the beauty of the film. There's one little Disney moment at the pool table; otherwise, the viewer does not really think Disney. The ending, as in "Miracle," is not some Disney creation, but one that only human history could have written.
標籤label: 正面的 預測結果: 正面的
"""

display_test_Sentiment(3)

"""
I saw this film in a sneak preview, and it is delightful. The cinematography is unusually creative, the acting is good, and the story is fabulous. If this movie does not do well, it won't be because it doesn't deserve to. Before this film, I didn't realize how charming Shia Lebouf could be. He does a marvelous, self-contained, job as the lead. There's something incredibly sweet about him, and it makes the movie even better. The other actors do a good job as well, and the film contains moments of really high suspense, more than one might expect from a movie about golf. Sports movies are a dime a dozen, but this one stands out. This is one I'd recommend to anyone.
標籤label: 正面的 預測結果: 正面的
"""

print(predict_classes[12500:12510])

display_test_Sentiment(12500)

"""
Once again Mr. Costner has dragged out a movie for far longer than necessary. Aside from the terrific sea rescue sequences, of which there are very few I just did not care about any of the characters. Most of us have ghosts in the closet, and Costner's character are realized early on, and then forgotten until much later, by which time I did not care. The character we should really care about is a very cocky, overconfident Ashton Kutcher. The problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a cluttered closet. His only obstacle appears to be winning over Costner. Finally when we are well past the half way point of this stinker, Costner tells us all about Kutcher's ghosts. We are told why Kutcher is driven to be the best with no prior inkling or foreshadowing. No magic here, it was all I could do to keep from turning it off an hour in.
標籤label: 負面的 預測結果: 負面的
"""

# 預測新的影評

input_text = """
Oh dear, oh dear, oh dear: where should I start folks. I had low expectations already because I hated each and every single trailer so far, but boy did Disney make a blunder here. I'm sure the film will still make a billion dollars - hey: if Transformers 11 can do it, why not Belle? - but this film kills every subtle beautiful little thing that had made the original special, and it does so already in the very early stages. It's like the dinosaur stampede scene in Jackson's King Kong: only with even worse CGI (and, well, kitchen devices instead of dinos).
The worst sin, though, is that everything (and I mean really EVERYTHING) looks fake. What's the point of making a live-action version of a beloved cartoon if you make every prop look like a prop? I know it's a fairy tale for kids, but even Belle's village looks like it had only recently been put there by a subpar production designer trying to copy the images from the cartoon. There is not a hint of authenticity here. Unlike in Jungle Book, where we got great looking CGI, this really is the by-the-numbers version and corporate filmmaking at its worst. Of course it's not really a "bad" film; those 200 million blockbusters rarely are (this isn't 'The Room' after all), but it's so infuriatingly generic and dull - and it didn't have to be. In the hands of a great director the potential for this film would have been huge.
Oh and one more thing: bad CGI wolves (who actually look even worse than the ones in Twilight) is one thing, and the kids probably won't care. But making one of the two lead characters - Beast - look equally bad is simply unforgivably stupid. No wonder Emma Watson seems to phone it in: she apparently had to act against an guy with a green-screen in the place where his face should have been. 
"""

input_seq = token.texts_to_sequences([input_text])

print(len(input_seq[0]))

# 297

pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)

print(len(pad_input_seq[0]))

# 380

predict_result = model.predict_classes(pad_input_seq)

print(predict_result)

print(predict_result[0][0])

SentimentDict[predict_result[0][0]]

"負面的"


def predict_review(input_text):
    input_seq = token.texts_to_sequences([input_text])
    pad_input_seq = sequence.pad_sequences(input_seq, maxlen=380)
    predict_result = model.predict_classes(pad_input_seq)
    print(SentimentDict[predict_result[0][0]])


# http://www.imdb.com/title/tt2771200/
# http://www.imdb.com/title/tt2771200

predict_review(
    """
It's hard to believe that the same talented director who made the influential cult action classic The Road Warrior had anything to do with this disaster.
Road Warrior was raw, gritty, violent and uncompromising, and this movie is the exact opposite. It's like Road Warrior for kids who need constant action in their movies.
This is the movie. The good guys get into a fight with the bad guys, outrun them, they break down in their vehicle and fix it. Rinse and repeat. The second half of the movie is the first half again just done faster.
The Road Warrior may have been a simple premise but it made you feel something, even with it's opening narration before any action was even shown. And the supporting characters were given just enough time for each of them to be likable or relatable.
In this movie there is absolutely nothing and no one to care about. We're supposed to care about the characters because... well we should. George Miller just wants us to, and in one of the most cringe worthy moments Charlize Theron's character breaks down while dramatic music plays to try desperately to make us care.
Tom Hardy is pathetic as Max. One of the dullest leading men I've seen in a long time. There's not one single moment throughout the entire movie where he comes anywhere near reaching the same level of charisma Mel Gibson did in the role. Gibson made more of an impression just eating a tin of dog food. I'm still confused as to what accent Hardy was even trying to do.
I was amazed that Max has now become a cartoon character as well. Gibson's Max was a semi-realistic tough guy who hurt, bled, and nearly died several times. Now he survives car crashes and tornadoes with ease?
In the previous movies, fuel and guns and bullets were rare. Not anymore. It doesn't even seem Post-Apocalyptic. There's no sense of desperation anymore and everything is too glossy looking. And the main villain's super model looking wives with their perfect skin are about as convincing as apocalyptic survivors as Hardy's Australian accent is. They're so boring and one-dimensional, George Miller could have combined them all into one character and you wouldn't miss anyone.
Some of the green screen is very obvious and fake looking, and the CGI sandstorm is laughably bad. It wouldn't look out of place in a Pixar movie.
There's no tension, no real struggle, or any real dirt and grit that Road Warrior had. Everything George Miller got right with that masterpiece he gets completely wrong here. 
"""
)

# 負面的

predict_review(
    """
Sure, I'm a huge film snob who (on the surface) only likes artsy-fartsy foreign films from before the 60's, but that hasn't stopped me from loving Disney's Beauty & The Beast; in fact, it's probably my favorite American animated film and is easily Disney's finest work. It's beautiful, it's breathtaking, it's warm, it's hilarious, it's captivating, and, in Disney fashion, it's magical. When I learned that Disney would be remaking their classic films, B&TB was undeniably the best wrapped package. How could they go wrong?
Oh man, they went wrong.
First thing's first: this film is so flat. The directing was dull and uninteresting throughout the entire film and it honestly felt like one of the Twilight sequels...and then I looked it up and found out that, yes, director Bill Condon was the man behind Breaking Dawn parts 1 & 2. Every shot looks bored and uninterested, which contrasts heavily with the original animated film that was constantly popping with vibrancy. The script too is boring because it's almost a complete remake of the original, though I guess most people won't mind that.
Next: the CGI is horrid. Although I didn't care for The Jungle Book from last year, I could at least admit that the CGI was breathtaking. The same cant be said for this film. Characters like Lumière, Cogsworth, Mrs Potts, and most of the cursed appliances have very strange, lifeless faces that are pretty off putting to be looking at for such a long time. All of the sets too look artificial and fake, especially the town towards the beginning. However, the biggest offender is easily and infuriatingly the character that mattered most: The Beast. The CGI on the Beast's face is so distracting that it completely takes you out of the film. His eyes are completely devoid of soul, and his mouth is a gaping video game black hole of fiction. Klaus Kinski looked much better in the Faerie Tale Theatre episode of Beauty & The Beast, and that was a 1984 TV show episode. But do you know why it looked better? Because it was an actual face with actual eyes, not some video game computerized synthetic monstrosity. When will studios learn that practical effects will always top CGI?
Finally: wasted casting. Emma Watson is beautiful, but she's no Belle. She is completely devoid of the warmth and humanity that made the animated Belle so beloved. Instead, she is cold and heartless throughout most of the film. Kevin Kline is 100% wasted and does nothing except look old. Ian McKellan, Ewan McGregor, Emma Thompson, and even Dan Stevens as the Beast are very expendable and could've been played by anyone else. The only good characters are Gaston and LeFou, mostly because they are fun and played by actors who breathe new life into their original shapes. If anything, this film should've been about Gaston and LeFou, but that would never happen because that would mean Disney couldn't cater to blind nostalgic 90's kids.
Overall, this film is a complete bore. It could've been better if even the special effects were good, but the CGI in particular is horrendous. I'm all for Disney remaking their nostalgia- catering 90's films, but they need to be interesting. This film, sadly, is not. Even the Christmas sequel is better than this film because it's at least something. 
"""
)

# 負面的

predict_review(
    """
I was really looking forward to this film. Not only has Disney recently made excellent live-action versions of their animated masterpieces (Jungle Book, Cinderella), but the cast alone (Emma Watson, Ian McKellen, Kevin Kline) already seemed to make this one a sure hit. Well, not so much as it turns out.
Some of the animation is fantastic, but because characters like Cogsworth (the clock), Lumière (the candelabra) and Chip (the little tea cup) now look "realistic", they lose a lot of their animated predecessors' charm and actually even look kind of creepy at times. And ironically - unlike in the animated original - in this new realistic version they only have very limited facial expressions (which is a creative decision I can't for the life of me understand).
Even when it works: there can be too much of a good thing. The film is overstuffed with lush production design and cgi (which is often weirdly artificial looking though) but sadly lacking in charm and genuine emotion. If this were a music album, I'd say it is "over-produced" and in need of more soul and swing. The great voice talent in some cases actually seems wasted, because it drowns in a sea of visual effects that numbs all senses. The most crucial thing that didn't work for me, though, is the Beast. He just never looks convincing. The eyes somehow don't look like real eyes and they're always slightly off.
On the positive side, I really liked Gaston, and the actor who played him, Luke Evans, actually gave the perhaps most energized performance of all. Kevin Kline as Belle's father has little to do but to look fatherly and old, but he makes the most of his part. Speaking of Belle, now that I've seen the film, I think her role was miscast. I think someone like Rachel McAdams would actually have been a more natural, lively and perhaps a bit more feisty Belle than Emma Watson.
If you love the original, you might want to give this one a pass, it's really not that good (although at least the songs were OK). Also, I'd think twice before bringing small children; without cute animated faces, all those "realistic" looking creatures and devices can be rather frightening for a child. """
)

# 正面的

predict_review(
    """
Up front: I'm probably not the right audience for this film. I only went because I was invited, and I wouldn't have gone to check this one out otherwise.
Firstly, some of the production values are really beautiful and reminded me of the animated classic in a good way. Also, the voice cast for the clock and the kitchen devices are great.
Secondly, the actors, well... this may sound kind of harsh, but I've never seen Emma Watson act so stiff in a movie. Her performance is wooden, which is pretty bad considering she's supposed to be the heart of the film. Also, she probably won't start a singing career anytime soon.
Thirdly (and most importantly), Beast. That's where they really dropped the ball. Giving him a lifeless CGI face was an unforgivable mistake, and it's such a constant distraction that I could never really get into the movie.
Overall, I'm afraid I wouldn't recommend this movie, at least not to adults. I'm sure most kids would enjoy it though, and it's not really a bad film: just a very mediocre one. 6 stars out of 10. 
"""
)

# 負面的

predict_review(
    """
Full disclosure, I didn't think the first movie was as bad as it was made out to be. It wasn't good in almost any sense, but it was to be expected given the combination of source material, resources and constraints.
That said, this sequel is 20x better than the first. Having established the characters in the first movie, the actors seem to be able to act now comfortably in their parts. The story becomes much more nuanced with plenty of dynamics on the go.
SPOILERS from now on
Can they maintain a "vanilla" relationship? Is he going to become controlling again and ruin things? Will she let it get out of control and ruin things also or stay on it? Who is that stalky girl and what happened to her exactly? what about his mother? and that ex of his? Will something occur with her infatuated boss?
On top of all of this, I realised while watching that the series was never about a bizarre sadist control freak, it's actually about all men and the story of a woman trying to find the balance between accepting or desiring the dominant behaviour of the male archetype and maintaining strength and independence in such a relationship.
While of course the fact that he is rich, while possibly relating to the power struggle, looks like it is going to be more and more used for generating further drama. The romance is much more evident in this movie to/ 
"""
)

# 正面的

# serialize model to JSON

model_json = model.to_json()
with open("SaveModel/Imdb_RNN_model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("SaveModel/Imdb_RNN_model.h5")
print("Saved model to disk")

# Saved model to disk
NG '''
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
from tensorflow.keras.utils import to_categorical  # One-Hot Encoding
y_Train_OneHot = to_categorical(y_train_label)
"""


""" 解决 placeholder
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0
tf.disable_v2_behavior()

x = tf.placeholder("float", [None, 784])
"""
