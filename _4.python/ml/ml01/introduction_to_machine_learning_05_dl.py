"""
introduction_to_machine_learning_05_dl

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

import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap

from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
Deep learning(DL)

convolutional neural networks (CNN卷積神經網路) - deep feed-forward neural networks (discussed today)
recurrent neural networks (RNN) - connections between nodes can go backward (used e.g. for speech recognition)
generative adversarial networks (GAN) - system of two neural networks competing with each other (one generates fake data and the other compare them with real data)
"""

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# Convolutional neural networks 卷積神經網路

from skimage import io
from scipy.signal import convolve2d

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Albert_Einstein_Head.jpg/220px-Albert_Einstein_Head.jpg"

# image = skimage.io.imread(filename, True)  # True:轉為灰階
img = io.imread(url, True)

# define first filter
filter01 = np.array([[0, 1, 0], [0, -2, 0], [0, 1, 0]])

# define first filter
filter02 = np.array([[0, 0, 0], [1, -2, 1], [0, 0, 0]])

# apply filters
out01 = convolve2d(img, filter01, mode="valid")
out02 = convolve2d(img, filter02, mode="same")

plt.subplot(131)
plt.title(img.shape)
plt.imshow(img, cmap="gray")

plt.subplot(132)
plt.title(out01.shape)
plt.imshow(out01, cmap="gray")

plt.subplot(133)
plt.title(out02.shape)
plt.imshow(out02, cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

from skimage.measure import block_reduce

images = [img]

# perform 5 poolings
for i in range(5):
    images.append(block_reduce(images[-1], (2, 2), np.max))

# plot them all
for i in range(6):
    plt.subplot(231 + i)
    plt.imshow(images[i], cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# CNN structure

# Deep MNIST
"""
    Last week we got about 92% accuracy on MNIST dataset
    Today we are going to do better with CNN
    First, lets load the data
"""

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()


"""
先將 tutorials
放在
C:/Users/070601/AppData/Local/Programs/Python/Python311/Lib/site-packages/tensorflow/examples
之下
"""

from tensorflow.examples.tutorials.mnist import input_data

# import tensorflow.examples.tutorials.mnist.input_data as input_data

# to avoid warnings printed in the notebook
# tf.logging.set_verbosity(tf.logging.ERROR)

# one hot -> label 0-9 -> 0...01, 0...10, ...
mnist = input_data.read_data_sets("/tmp/", one_hot=True)

# Create placeholders for tensors to fed

x = tf.placeholder(tf.float32, [None, 784])  # img -> 28x28 -> 784
y = tf.placeholder(tf.float32, [None, 10])  # 10 classes

# Build the network

# reshape to 28x28 image with 1 color channel
x_image = tf.reshape(x, [-1, 28, 28, 1])

##### The first convolution (conv1) with 32 filters 5x5 #####

# init weights randomly from normal distribution with bounds
W_conv1 = tf.Variable(tf.truncated_normal([5, 5, 1, 32], stddev=0.1))

# init bias with 0.1
b_conv1 = tf.Variable(tf.constant(0.1, shape=[32]))

# create convolution
# input tensor has 4 dimensions: [batch, height, width, channels]
# strides defines how to move in each dimension
# padding = "SAME" (zero padding) or "VALID" (no padding)
conv1 = tf.nn.conv2d(x_image, W_conv1, strides=[1, 1, 1, 1], padding="SAME")

# ReLU activation funtion
h_conv1 = tf.nn.relu(conv1 + b_conv1)

# pooling layer 2x2 with stride 2
h_pool1 = tf.nn.max_pool(
    h_conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME"
)

##### The second convolutional layer - maps 32 feature maps to 64 #####

W_conv2 = tf.Variable(tf.truncated_normal([5, 5, 32, 64], stddev=0.1))
b_conv2 = tf.Variable(tf.constant(0.1, shape=[64]))

# last pooling layer is an input for this layer
conv2 = tf.nn.conv2d(h_pool1, W_conv2, strides=[1, 1, 1, 1], padding="SAME")
h_conv2 = tf.nn.relu(conv2 + b_conv2)
h_pool2 = tf.nn.max_pool(
    h_conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME"
)

# Convolution is done with zero padding - preserves image size
# Each pooling downsamples by 2x
# 28x28 -> 14x14x32 -> 7x7x64

###### Fully connected layer maps above to 1024 features #####

W_fc1 = tf.Variable(tf.truncated_normal([7 * 7 * 64, 1024], stddev=0.1))
b_fc1 = tf.Variable(tf.constant(0.1, shape=[1024]))

# we need to reshape last layer
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])

# matmul - matrix multiplication
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

##### Dropout layer #####

# keep_prob controls no. of deactivated neurons
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

##### Output layer #####

# Map the 1024 features to 10 classes, one for each digit
W_fc2 = tf.Variable(tf.truncated_normal([1024, 10], stddev=0.1))
b_fc2 = tf.Variable(tf.constant(0.1, shape=[10]))

out = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# loss function
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=out)
)

# training step - using Adam SGD with initial learning rate 1e-4
# train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy) old
train_step = tf.compat.v1.train.AdamOptimizer(1e-4).minimize(cross_entropy)

# For convenience we define a method to measure accuracy

# argmax returns the index of the heighest index in a tensor
# equal returns True / False if prediction is equal/not equal to true label
# cast would convert True/False to 1/0, so we can calculate the average
correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

# 必須使用 GPU
# Make sure we are running on GPU
device_name = tf.test.gpu_device_name()

print("device_name :", device_name)

if device_name != "/device:GPU:0":
    raise SystemError("無 GPU")
print("Found GPU at: {}".format(device_name))

# Found GPU at: /device:GPU:0

# Finally we can train the network on MNIST dataset

# to use GPU through Colaboratory
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

nof_iterations = 20000  # number of training steps
test_every = 1000  # calculate accuracy every test_every step
batch_size = 32  # traning batch size
acc_batch = 2048  # the size of a subset used to measure accuracy

train_accuracy = []
valid_accuracy = []

with tf.Session(config=config) as sess:
    # initialize weights and biases
    sess.run(tf.global_variables_initializer())

    for i in range(nof_iterations):
        # take mini batch from MNIST dataset
        batch = mnist.train.next_batch(batch_size)

        # every test_every iterations save current accuracy scores
        if i % test_every == 0:
            # for testing we do not want dropout neurons - keep_prob = 1
            # to save time we calculate accuracy on a subset of data

            train_batch = mnist.train.next_batch(acc_batch)
            train_accuracy.append(
                accuracy.eval(
                    feed_dict={x: train_batch[0], y: train_batch[1], keep_prob: 1.0}
                )
            )

            test_batch = mnist.test.next_batch(acc_batch)
            valid_accuracy.append(
                accuracy.eval(
                    feed_dict={x: test_batch[0], y: test_batch[1], keep_prob: 1.0}
                )
            )

        # run training step with 50% neurons deactivated
        train_step.run(feed_dict={x: batch[0], y: batch[1], keep_prob: 0.5})

    # calculate the accuracy on the whole testing dataset
    print(
        "test accuracy %g"
        % accuracy.eval(
            feed_dict={x: mnist.test.images, y: mnist.test.labels, keep_prob: 1.0}
        )
    )

# test accuracy 0.9915

iterations = np.linspace(0, nof_iterations, nof_iterations // test_every)

plt.xlabel("Iteration")
plt.ylabel("Accuracy")

plt.plot(iterations, train_accuracy, label="Training accuracy")
plt.plot(iterations, valid_accuracy, label="Valid accuracy")

plt.legend()
show()

print("------------------------------------------------------------")  # 60個

# Batch normalization

# BN layer

# Data augmentation

# Flipping

from skimage import io
from scipy.signal import convolve2d

url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Albert_Einstein_Head.jpg/220px-Albert_Einstein_Head.jpg"

# image = skimage.io.imread(filename, True)  # True:轉為灰階
img = io.imread(url, True)


img_flip_x = np.flip(img, axis=1)
img_flip_y = np.flip(img, axis=0)
img_flip_xy = np.flip(img_flip_y, axis=1)

plt.subplot(221)
plt.title("original")
plt.imshow(img, cmap="gray")

plt.subplot(222)
plt.title("x-flip")
plt.imshow(img_flip_x, cmap="gray")

plt.subplot(223)
plt.title("y-flip")
plt.imshow(img_flip_y, cmap="gray")

plt.subplot(224)
plt.title("xy-flip")
plt.imshow(img_flip_xy, cmap="gray")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# Rotation

from scipy.ndimage.interpolation import rotate

for i, angle in enumerate((30, 60, 90, 120)):
    img_rot = rotate(img, angle=angle)
    plt.subplot(221 + i)
    plt.title("angle = {}".format(angle))
    plt.imshow(img_rot, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Translation

from scipy.ndimage.interpolation import shift

for i, (dx, dy) in enumerate(((30, 30), (60, 60), (-30, -30), (-60, -60))):
    img_trans = shift(img, (dx, dy))
    plt.subplot(221 + i)
    plt.title("dx, dy = {}, {}".format(dx, dy))
    plt.imshow(img_trans, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Scaling

from skimage.transform import rescale

for i, scale in enumerate((1.0, 0.9, 0.8, 0.7)):
    img_scaled = rescale(img, scale).copy()
    img_scaled = np.pad(
        img_scaled, (img.shape[0] - img_scaled.shape[0]) // 2, mode="constant"
    )
    plt.subplot(221 + i)
    plt.title("scale = {}".format(scale))
    plt.imshow(img_scaled, cmap="gray")

plt.tight_layout()

show()

print("------------------------------------------------------------")  # 60個

# Noise

# salt and pepper noise
for i, prob in enumerate((0.05, 0.10, 0.15, 0.20)):
    img_noised = img.copy()
    rnd = np.random.rand(img.shape[0], img.shape[1])
    img_noised[rnd < prob] = 0  # pepper
    img_noised[rnd > 1 - prob] = 1  # salt
    plt.subplot(221 + i)
    plt.title("prob = {}".format(prob))
    plt.imshow(img_noised, cmap="gray")

plt.tight_layout()
show()

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


print("------------------------------------------------------------")  # 60個
