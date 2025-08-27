"""


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

import sklearn
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

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

a = tf.constant(2)
b = tf.constant(3)

matrix1 = tf.constant([[3., 3.]])

matrix2 = tf.constant([[2.],[2.]])

product = tf.matmul(matrix1, matrix2)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear Regression in TensorFlow

import tensorflow as tf
import numpy
import matplotlib.pyplot as plt

import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

rng = numpy.random

# Parameters
learning_rate = 0.01
training_epochs = 2000
display_step = 50

# Training Data
train_X = numpy.asarray([3.3,4.4,5.5,6.71,6.93,4.168,9.779,6.182,7.59,2.167,7.042,10.791,5.313,7.997,5.654,9.27,3.1])
train_Y = numpy.asarray([1.7,2.76,2.09,3.19,1.694,1.573,3.366,2.596,2.53,1.221,2.827,3.465,1.65,2.904,2.42,2.94,1.3])
n_samples = train_X.shape[0]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''

# import tensorflow as tf
import tensorflow.compat.v1 as tf  # 強制使用tensorflow 1.0

import tensorflow_datasets

# mnist = tensorflow_datasets.load("/tmp/data/")

mnist_npz_filename = "D:/_git/vcs/_big_files/mnist.npz"

mnist = np.load(mnist_npz_filename)
x_train, y_train = mnist["x_train"], mnist["y_train"]
x_test, y_test = mnist["x_test"], mnist["y_test"]
mnist.close()


# Parameters
learning_rate = 0.01
training_epochs = 25
batch_size = 100
display_step = 1


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
