"""
keras

"""

import keras

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

# 迭代次數
ITERATIONS = 50

print("------------------------------------------------------------")  # 60個

import tensorflow as tf

print(tf.__version__)
'''
print("------------------------------------------------------------")  # 60個

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer="sgd", loss="mean_squared_error")

# y = x
xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0], dtype=float)
ys = np.array([0.0, 1.0, 2.0, 5.0, 4.0, 5.0], dtype=float)
print(type(xs))
print(xs)
print(type(ys))
print(ys)

model.fit(xs, ys, epochs=ITERATIONS)

print("keras 預測")
xx = np.linspace(0.0, 10.0, 21)
yy = model.predict(xx)

"""
print(model.predict([2.5]))
print(model.predict([4.5]))
print(model.predict([6.0]))
print(model.predict([10.0]))
print(xx)
print(yy)
"""

x = np.linspace(0, 10, 100)
plt.plot(x, x, "b", lw=2, label="y = x")
plt.plot(xs, ys, "g-o", lw=1, ms=10, label="實驗點")
plt.scatter(xx, yy, c="red", marker="o", lw=4, label="預測點")

xmin, xmax, ymin, ymax = -1, 11, -1, 11
plt.axis([xmin, xmax, ymin, ymax])  # 設定各軸顯示範圍
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

"""
mnist 資料集 內容
assert x_train.shape == (60000, 28, 28)
assert x_test.shape == (10000, 28, 28)
assert y_train.shape == (60000,)
assert y_test.shape == (10000,)
"""
'''
print("------------------------------------------------------------")  # 60個

"""
import tensorflow as tf 
import tensorflow.examples.tutorials.mnist.input_data as input_data
 
mnist = input_data.read_data_sets('./database2/', one_hot=True)#相对路径
#tensorflow.contrib.learn.python.learn.datasets.mnist.DataSet
print(type(mnist))#<class 'tensorflow.contrib.learn.python.learn.datasets.base.Datasets'>
 
batch = mnist.train.next_batch(100)
print(type(batch))#<class 'tuple'>
 
x=mnist.train.images
y=mnist.train.labels
print(type(x),x.shape)#<class 'numpy.ndarray'> (55000, 784)
print(type(y),y.shape)#<class 'numpy.ndarray'> (55000, 10)
"""

print("------------------------------------------------------------")  # 60個

import keras

# from tensorflow import keras


def preprocess(labels, images):
    """
    最简单的预处理函数:
            转numpy为Tensor、分类问题需要处理label为one_hot编码、处理训练数据
    """
    # 把numpy数据转为Tensor
    labels = tf.cast(labels, dtype=tf.int32)
    # labels 转为one_hot编码
    labels = tf.one_hot(labels, depth=10)
    # 顺手归一化
    images = tf.cast(images, dtype=tf.float32) / 255
    return labels, images


# abs_path_to_dataset='H:/Leon/CODE/python_projects/master_ImRecognition/dataset/MNIST/database3/mnist.npz'
# (x, y), (x_test, y_test) = keras.datasets.mnist.load_data(path=abs_path_to_dataset)#绝对路径
(x, y), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
print(type(x), x.shape)  # <class 'numpy.ndarray'> (60000, 28, 28)
print(type(y), y.shape)  # <class 'numpy.ndarray'> (60000,)
db_train = tf.data.Dataset.from_tensor_slices((x, y))
print(
    db_train
)  # <DatasetV1Adapter shapes: ((28, 28), ()), types: (tf.uint8, tf.uint8)>
print(
    type(db_train)
)  # <class 'tensorflow.python.data.ops.dataset_ops.DatasetV1Adapter'>
db_train.shuffle(1000)
db_train.map(preprocess)
db_train.batch(64)
db_train.repeat(2)
print(
    type(db_train)
)  # <class 'tensorflow.python.data.ops.dataset_ops.DatasetV1Adapter'>
# print(db_train.output_shapes)#(TensorShape([Dimension(28), Dimension(28)]), TensorShape([]))


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
