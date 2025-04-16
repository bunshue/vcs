"""
Ridge(


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


from math import sin, cos, pi, exp


def get_dataset(N=20, sigma=0.1):
    """Generate N training samples"""
    # X is a set of random points from [-1, 1]
    X = 2 * np.random.sample(N) - 1
    # Y are corresponding target values (with noise included)
    Y = np.array([sin(pi * x) + np.random.normal(0, sigma) for x in X])

    return X, Y


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
mnist = input_data.read_data_sets("./tmp_mnist/", one_hot=True)

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

print("無 GPU 跳過")
"""
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

show()
# test accuracy 0.9915

iterations = np.linspace(0, nof_iterations, nof_iterations // test_every)

plt.xlabel("Iteration")
plt.ylabel("Accuracy")

plt.plot(iterations, train_accuracy, label="Training accuracy")
plt.plot(iterations, valid_accuracy, label="Valid accuracy")

plt.legend()
show()
"""
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

"""
sugar不能用 import theano 失敗

"""

"""
Neural Network
    Artificial neural network (in particular deep NN) is the most popular machine learning method these days
    They are inspired by human brains (at least initially)
    Artifical neuron is a mathematical function
    Neurons are connected with each other (kind of synapses)
    Usually connections have some weights
    Today, feedforward neural networks (multilayer perceptrons) will be discussed
    However, before we go there, lets start with linear and logistic regression
"""

# just to overwrite default colab style
plt.style.use("default")
plt.style.use("seaborn-talk")

# Linear regression

N = 100  # number of samples

a = 0.50  # slope
b = 0.50  # y-intercept
s = 0.25  # sigma

### GENERATE SAMPLES ###

X = 10.0 * np.random.sample(N)  # features
Y = [(a * X[i] + b) + np.random.normal(0, s) for i in range(N)]  # targets

### PLOT SAMPLES ###

plt.xlabel("Feature")
plt.ylabel("Target")
plt.scatter(X, Y, marker=".")
show()

print("------------------------------------------------------------")  # 60個

#!pip install theano

import theano
import theano.tensor as T

x = T.vector("x")  # feature vector
y = T.vector("y")  # target vector

# weights initialized randomly
# a = theano.shared(np.random.randn(), name = 'w')
# b = theano.shared(np.random.randn(), name = 'b')

# initial weights by hand for demonstration (random may be to close)
a = theano.shared(-0.5, name="w")
b = theano.shared(1.0, name="b")


pred = T.dot(x, a) + b  # hyphothesis
cost = T.sum(T.pow(pred - y, 2)) / N  # cost function
grad_a, grad_b = T.grad(cost, [a, b])  # gradients

# And finally, we define gradient descent method (which also returns the value of the cost function)

alpha = 0.005  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((a, a - alpha * grad_a), (b, b - alpha * grad_b)),
)

# Each training step involves the full cycle on training data (epoch)

n_epochs = 1000  # number of training steps / epochs
costs = []  # to keep track on the value of cost function on each step
weights = []  # to store few set of weights

keep = (0, 10, 100, 500, 1000)  # save result for some epochs passed

for i in range(n_epochs + 1):
    if i in keep:
        weights.append((a.get_value(), b.get_value()))

    costs.append(train(X, Y))

# Finally, we can visualize the results

plt.figure(figsize=(10, 15))
n_rows = 3
n_cols = 2

for i, (a_, b_) in enumerate(weights):
    plt.subplot(n_rows, n_cols, i + 1)

    plt.title("Epoch %i: y = %.2f x + %.2f" % (keep[i], a_, b_))
    plt.xlabel("Feature")
    plt.ylabel("Target")

    x_ = np.arange(0, 10, 0.1)

    plt.plot(x_, a_ * x_ + b_, color="C1")
    plt.scatter(X, Y, marker=".")


plt.subplot(n_rows, n_cols, len(weights) + 1)
plt.title("Cost function")
plt.xlabel("Epoch")
plt.ylabel("L")
plt.ylim([0, 0.2])

plt.plot(range(len(costs)), costs)

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# Logistic regression

p_ = np.arange(0.01, 0.99, 0.01)

plt.title("Logit function")
plt.xlabel("p")
plt.ylabel("$\ln(p/(1-p))$")

plt.plot(p_, np.log(p_ / (1 - p_)))
show()

print("------------------------------------------------------------")  # 60個

x_ = np.arange(-10, 10, 0.1)

plt.title("Logistic function")
plt.xlabel("x")
plt.ylabel("$1/(1 + e^{-x})$")

plt.plot(x_, 1 / (1 + np.exp(-x_)))
show()

print("------------------------------------------------------------")  # 60個

# Cost function

N = 50  # number of students per class

X = np.concatenate((np.random.random((N)) * 35, 30 + np.random.random((N)) * 25))

Y = np.concatenate(([0] * N, [1] * N))

plt.xlabel("Study time [h]")
plt.ylabel("Success")

plt.scatter(X, Y)
show()

print("------------------------------------------------------------")  # 60個

# Once again lets use theano

import theano
import theano.tensor as T

x = T.vector("x")  # feature vector
y = T.vector("y")  # target vector

a = theano.shared(np.random.randn(), name="w")  # weights initialized randomly
b = theano.shared(np.random.randn(), name="b")

hypo = 1 / (1 + T.exp(-T.dot(x, a) - b))  # hyphothesis
xent = -y * T.log(hypo) - (1 - y) * T.log(1 - hypo)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_a, grad_b = T.grad(cost, [a, b])  # gradients

alpha = 0.01  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((a, a - alpha * grad_a), (b, b - alpha * grad_b)),
)

print("------------------------------------------------------------")  # 60個

x_min = min(X)
x_max = max(X)

s = lambda x: (x - x_min) / (x_max - x_min)  # scale

# Now, we train the model on normalized data

n_epochs = 1000

[train(s(X), Y) for _ in range(n_epochs)]

plt.xlabel("Study time [h]")
plt.ylabel("Success")

plt.scatter(X, Y)

h_ = np.arange(0, 60, 0.01)

plt.plot(h_, 1 / (1 + np.exp(-s(h_) * a.get_value() - b.get_value())), "C1")

plt.plot([0, 60], [0.5, 0.5], "C2--")
show()

print("------------------------------------------------------------")  # 60個

# Multinominal logistic regression

# Logit approach


def grade(init_know, study_time):
    """Arbitrary grading system."""
    score = np.random.normal(init_know + 2 * study_time, 5)

    if score > 90:
        return 3  # bdb
    elif score > 70:
        return 2  # db
    elif score > 50:
        return 1  # dst
    else:
        return 0  # ndst


# The training set

N = 1000  # number of students

X = np.random.sample((N, 2)) * [100, 50]
Y = np.array([grade(*student) for student in X], dtype="int32")

plt.xlabel("Initial knowledge")
plt.ylabel("Study time")

for student, g in zip(X, Y):
    plt.scatter(*student, color="C" + str(g), marker=".")
show()

# Data preparation

X_train = np.multiply(X, np.array([1 / 100, 1 / 50]))

# Lets add 1 for bias term to the dataset

X_train = np.hstack((np.ones((N, 1)), X_train))

# How does it look?

print("Original:", X[:5], "Preprocessed:", X_train[:5], sep="\n\n")

# Training
# The implementation of MLR in theano

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vectors
y = T.ivector("y")  # target vector

W = theano.shared(np.random.randn(3, 4))  # weight matrix (2 features + bias,
#                4 possible outcomes)

hypo = T.nnet.softmax(T.dot(x, W))  # hyphothesis
cost = -T.mean(T.log(hypo)[T.arange(y.shape[0]), y])  # cost function
grad_W = T.grad(cost=cost, wrt=W)  # gradients

alpha = 0.5  # learning rate

# define a training step
train = theano.function(inputs=[x, y], outputs=cost, updates=[(W, W - alpha * grad_W)])

# predict a class label
predict = theano.function(inputs=[x], outputs=T.argmax(hypo, axis=1))

# The training process on normalized data

n_epochs = 10000
acc_train = []  # accuracy on training dataset

for _ in range(n_epochs):
    # do a single step of gradient descent
    train(X_train, Y)
    # calculate accuracy with current set of weights
    acc_train.append((Y == predict(X_train)).sum() / Y.shape[0])

plt.xlabel("Epoch")
plt.ylabel("Cost")

plt.plot(range(len(acc_train)), acc_train)
show()

print("------------------------------------------------------------")  # 60個

# Validation
# First we need unseen data for testing

# another set of students
X_test = np.random.sample((N, 2)) * [100, 50]
Y_test = np.array([grade(*student) for student in X_test], dtype="int32")

# normalize and add bias
X_test_normalized = np.multiply(X_test, np.array([1 / 100, 1 / 50]))
X_test_normalized = np.hstack((np.ones((N, 1)), X_test_normalized))

# To predict a grade we use the function predict defined earlier

Y_pred = predict(X_test_normalized)

# We can visualize the prediction

plt.xlabel("Initial knowledge")
plt.ylabel("Study time")

for student, g in zip(X_test, Y_pred):
    plt.scatter(*student, color="C" + str(g), marker=".")
show()

print("------------------------------------------------------------")  # 60個

# 計算準確率

cc = (Y_test == Y_pred).sum() / Y_test.shape[0]
print(cc)

# Softmax visualization

softmax = theano.function(inputs=[x], outputs=hypo)

probs = softmax(X_test_normalized)

print(probs.shape)

# (1000, 4)

# We can plot each class separately

from mpl_toolkits.mplot3d import Axes3D

grades = ("ndst", "dst", "db", "bdb")

for i in range(4):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("Initial knowledge", labelpad=20)
    ax.set_ylabel("Study time", labelpad=20)

    ax.set_title("Grade: " + grades[i])

    ax.scatter(X_test.T[0], X_test.T[1], probs.T[i], marker=".")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Neural Networks
    Here are some helpful functions to draw neural networks
"""

radius = 0.3

arrow_kwargs = dict(head_width=0.05, fc="black")


def draw_connecting_arrow(ax, circ1, rad1, circ2, rad2):
    theta = np.arctan2(circ2[1] - circ1[1], circ2[0] - circ1[0])

    starting_point = (circ1[0] + rad1 * np.cos(theta), circ1[1] + rad1 * np.sin(theta))

    length = (
        circ2[0] - circ1[0] - (rad1 + 1.4 * rad2) * np.cos(theta),
        circ2[1] - circ1[1] - (rad1 + 1.4 * rad2) * np.sin(theta),
    )

    ax.arrow(starting_point[0], starting_point[1], length[0], length[1], **arrow_kwargs)


def draw_circle(ax, center, radius):
    circ = plt.Circle(center, radius, fill=False, lw=2)
    ax.add_patch(circ)


def draw_net(input_size, output_size, hidden_layers=[], w=6, h=4):
    # Draw a network
    x = 0  # initial layer position

    ax = plt.subplot()
    ax.set_aspect("equal")
    ax.axis("off")

    ax.set_xlim([-2, -2 + w])
    ax.set_ylim([-h / 2, h / 2 + 1])

    # set y position
    y_input = np.arange(-(input_size - 1) / 2, (input_size + 1) / 2, 1)
    y_output = np.arange(-(output_size - 1) / 2, (output_size + 1) / 2, 1)
    y_hidden = [np.arange(-(n - 1) / 2, (n + 1) / 2, 1) for n in hidden_layers]

    # draw input layer
    plt.text(x, h / 2 + 0.5, "Input\nLayer", ha="center", va="top")

    for i, y in enumerate(y_input):
        draw_circle(ax, (x, y), radius)
        ax.text(
            x - 0.9,
            y,
            "$x_%i$" % (input_size - 1 - i),
            ha="right",
            va="center",
        )
        draw_connecting_arrow(ax, (x - 0.9, y), 0.1, (x, y), radius)

    last_layer = y_input  # last layer y positions

    # draw hidden layers
    for ys in y_hidden:
        # shift x
        x += 2
        plt.text(x, h / 2 + 0.5, "Hidden\nLayer", ha="center", va="top")

        # draw neurons for each hidden layer
        for i, y1 in enumerate(ys):
            draw_circle(ax, (x, y1), radius)

            # connect a neuron with all neurons from previous layer
            if i != len(ys) - 1:  # skip bias
                for y2 in last_layer:
                    draw_connecting_arrow(ax, (x - 2, y2), radius, (x, y1), radius)

        # update last layer
        last_layer = ys

    x += 2  # update position for output layer

    # draw output layer
    plt.text(x, h / 2 + 0.5, "Output\nLayer", ha="center", va="top")

    for i, y1 in enumerate(y_output):
        draw_circle(ax, (x, y1), radius)
        ax.text(x + 0.8, y1, "Output", ha="left", va="center")
        draw_connecting_arrow(ax, (x, y1), radius, (x + 0.8, y1), 0.1)

        # connect each output neuron with all neurons from previous layer
        for y2 in last_layer:
            draw_connecting_arrow(ax, (x - 2, y2), radius, (x, y1), radius)
    show()


draw_net(3, 1)


def binary_step(x):
    return 0 if x < 0 else 1


def logistic(x):
    return 1 / (1 + math.exp(-x))


def tanh(x):
    return math.tanh(x)


def relu(x):
    return 0 if x < 0 else x


x = np.linspace(-5, 5, 100)

bs = [binary_step(x_) for x_ in x]
lf = [logistic(x_) for x_ in x]
th = [tanh(x_) for x_ in x]
re = [relu(x_) for x_ in x]

_, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))

ax1.set_title("Binary step")
ax2.set_title("TanH")
ax3.set_title("Logistic")
ax4.set_title("ReLU")

ax1.plot(x, bs)
ax2.plot(x, lf)
ax3.plot(x, th)
ax4.plot(x, re)
show()

print("------------------------------------------------------------")  # 60個

# Neural networks

draw_net(3, 1, [5], w=9, h=6)

draw_net(3, 1, [5, 7, 9, 5], w=14, h=10)

draw_net(3, 4, [5, 7, 9, 5], w=14, h=10)

# Backpropagation

draw_net(3, 2, [3], w=9, h=4)

print("------------------------------------------------------------")  # 60個

# AND, OR vs XOR

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y_and = [0, 0, 0, 1]
Y_or = [0, 1, 1, 1]
Y_xor = [0, 1, 1, 0]

titles = ("AND", "OR", "XOR")

for i, Y in enumerate([Y_and, Y_or, Y_xor]):
    ax = plt.subplot(131 + i)

    ax.set_xlim([-0.5, 1.5])
    ax.set_ylim([-0.5, 1.5])

    ax.set_aspect("equal")

    plt.title(titles[i])
    plt.scatter(*zip(*X), c=Y)

    if i == 0:
        plt.plot([0, 1.5], [1.5, 0])
    elif i == 1:
        plt.plot([-0.5, 1], [1, -0.5])
    else:
        plt.text(0.5, 0.5, s="?", ha="center", va="center")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

# Single neuron approach

draw_net(3, 1)

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vector
y = T.vector("y")  # target vector

w = theano.shared(np.random.randn(2), name="w")  # weights initialized randomly
b = theano.shared(np.random.randn(), name="b")  # bias term

hypo = 1 / (1 + T.exp(-T.dot(x, w) - b))  # hyphothesis
xent = -y * T.log(hypo) - (1 - y) * T.log(1 - hypo)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_w, grad_b = T.grad(cost, [w, b])  # gradients

alpha = 0.1  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((w, w - alpha * grad_w), (b, b - alpha * grad_b)),
)

predict = theano.function(inputs=[x], outputs=hypo)

# Train for all gates and save prediction

N = 1000

gates = ("AND", "OR", "XOR")
gates_pred = {}

for gate, data in zip(gates, (Y_and, Y_or, Y_xor)):
    # reset weights
    w.set_value(np.random.randn(2))
    b.set_value(np.random.randn())

    # train neuron
    [train(X, data) for _ in range(N)]
    gates_pred[gate] = predict(X)

# Let's see the result

for gate in gates:
    for i, (x1, x2) in enumerate(X):
        print("{} {} {} -> {}".format(x1, gate, x2, gates_pred[gate][i]))
    print()

# Neural network approach

draw_net(3, 1, [3], w=8)

import theano
import theano.tensor as T

x = T.matrix("x")  # feature vector
y = T.vector("y")  # target vector

# first layer's weights (including bias)
w1 = theano.shared(np.random.randn(3, 2), name="w1")
# second layer's weights (including bias)
w2 = theano.shared(np.random.randn(3), name="w2")

h = T.nnet.sigmoid(T.dot(x, w1[:2,]) + w1[2,])  # hidden layer
o = T.nnet.sigmoid(T.dot(h, w2[:2,]) + w2[2,])  # output layer

xent = -y * T.log(o) - (1 - y) * T.log(1 - o)  # cross-entropy loss function
cost = xent.sum()  # cost function
grad_w1, grad_w2 = T.grad(cost, [w1, w2])  # gradients

alpha = 0.1  # learning rate

# at each training step we update weights:
# w -> w - alpha * grad_w and b -> b - alpha * grad_b
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=((w1, w1 - alpha * grad_w1), (w2, w2 - alpha * grad_w2)),
)

predict = theano.function(inputs=[x], outputs=o)

# Train on XOR and print prediction

[train(X, Y_xor) for _ in range(10000)]
prediction = predict(X)

for i, (x1, x2) in enumerate(X):
    print("{} XOR {} -> {}".format(x1, x2, prediction[i]))

# Again the same, but with tensorflow

import tensorflow as tf

# x = T.matrix('x') # feature vector
# y = T.vector('y') # target vector
x = tf.placeholder(tf.float32, [4, 2])
y = tf.placeholder(tf.float32, [4, 1])

# w1 = theano.shared(np.random.randn(3,2), name = 'w1')
# w2 = theano.shared(np.random.randn(3), name = 'w2')
w1 = tf.Variable(tf.random_normal([3, 2]), name="w1")
w2 = tf.Variable(tf.random_normal([3, 1]), name="w2")

# h = T.nnet.sigmoid(T.dot(x, w1[:2,]) + w1[2,])
# o = T.nnet.sigmoid(T.dot(h, w2[:2,]) + w2[2,])
h = tf.sigmoid(tf.add(tf.matmul(x, w1[:2,]), w1[2,]))
o = tf.sigmoid(tf.add(tf.matmul(h, w2[:2,]), w2[2,]))

# xent = - y * tf.log(o) - (1 - y) * tf.log(1 - o)
xent = tf.losses.log_loss(y, o)
cost = tf.reduce_mean(xent)

opt = tf.train.GradientDescentOptimizer(0.1).minimize(cost)

init = tf.global_variables_initializer()

X = [[0, 0], [1, 0], [0, 1], [1, 1]]
Y_xor = [[0], [1], [1], [0]]

with tf.Session() as sess:
    sess.run(init)
    [sess.run(opt, feed_dict={x: X, y: Y_xor}) for _ in range(10000)]
    print(sess.run(o, feed_dict={x: X}))

# Simple regression with NN

# plot a sample
X, Y = get_dataset(100, 0.25)

draw_net(2, 1, [4], w=10)

print("最後一次出現 draw_net(")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

x = tf.placeholder(tf.float32, [None, 1])
y = tf.placeholder(tf.float32, [None, 1])

w1 = tf.Variable(tf.random_normal([1, 3]), name="w1")
w2 = tf.Variable(tf.random_normal([3, 1]), name="w2")

b1 = tf.Variable(tf.random_normal([3]), name="b1")
b2 = tf.Variable(tf.random_normal([1]), name="b2")

h = tf.nn.sigmoid(tf.add(tf.matmul(x, w1), b1))
o = tf.add(tf.matmul(h, w2), b2)

xent = tf.losses.mean_squared_error(y, o)
cost = tf.reduce_mean(xent)

opt = tf.train.GradientDescentOptimizer(0.25).minimize(cost)

init = tf.global_variables_initializer()

X, Y = get_dataset(100, 0.25)
x_ = np.arange(-10, 10, 0.1)

# We need to reshape out training data

X_train = np.reshape(X, (-1, 1))
Y_train = np.reshape(Y, (-1, 1))

print("Original", X[:5], Y[:5], sep="\n\n")
print("\nReshaped", X_train[:5], Y_train[:5], sep="\n\n")

# And we can train the model

X_test = np.arange(-1, 1, 0.01).reshape(-1, 1)

with tf.Session() as sess:
    sess.run(init)
    [sess.run(opt, feed_dict={x: X_train, y: Y_train}) for _ in range(10000)]
    prediction = sess.run(o, feed_dict={x: X_test})

plt.scatter(X_test, prediction, color="C2", label="NN")
plt.scatter(X, Y, color="C1", label="Data")
plt.plot(x_, np.sin(np.pi * x_), "C0--", label="Truth")

plt.legend()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
MNIST
    THE MNIST DATABASE of handwritten digits
    The MNIST database of handwritten digits, available from this page, has a training set of 60,000 examples, and a test set of 10,000 examples. It is a subset of a larger set available from NIST. The digits have been size-normalized and centered in a fixed-size image.
    It is a good database for people who want to try learning techniques and pattern recognition methods on real-world data while spending minimal efforts on preprocessing and formatting.
    We can grab MNIST dataset using tensorflow.examples.tutorials.mnist
"""

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

from tensorflow.examples.tutorials.mnist import input_data

# to avoid warnings printed in the notebook
tf.logging.set_verbosity(tf.logging.ERROR)

# one hot -> label 0-9 -> 0...01, 0...10, ...
mnist = input_data.read_data_sets("./tmp_mnist/", one_hot=True)

print(mnist.train.images.shape)

# (55000, 784)

for i in range(4):
    plt.subplot(221 + i)

    # random training sample
    index = np.random.randint(len(mnist.train.images))

    # train.images contains images in a form of a vector
    # so we reshape it back to 28x28
    plt.imshow(mnist.train.images[index].reshape(28, 28), cmap="gray")

    # train.labels contains labels in one hot format
    plt.title(mnist.train.labels[index])

plt.tight_layout()
show()

x = tf.placeholder(tf.float32, [None, 784])  # img -> 28x28 -> 784
y = tf.placeholder(tf.float32, [None, 10])  # 10 classes

W = tf.Variable(tf.zeros([784, 10]))  # weights
b = tf.Variable(tf.zeros([10]))  # bias

out = tf.nn.softmax(tf.matmul(x, W) + b)

# Define the loss function and optimizer

cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(labels=y, logits=out)
)

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

# Train the model

# create a session
sess = tf.Session()
# initialize weights
sess.run(tf.global_variables_initializer())

for _ in range(10000):
    # here instead of updating weights after the whole training set
    # we use batch size 100 (more about that in the next section)
    batch_xs, batch_ys = mnist.train.next_batch(100)

    # train_step is minimizing cross_entropy with learning rate 0.5 using GD
    # we pass small batches to placeholders x and y
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})

# Validate the model

# argmax returns the index of the heighest index in a tensor
# equal returns True / False if prediction is equal/not equal to true label
# cast would convert True/False to 1/0, so we can calculate the average
correct_prediction = tf.equal(tf.argmax(out, 1), tf.argmax(y, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

print(sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels}))

sess.close()

# 0.9241

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import tensorflow as tf

# tensorflow2下使用tensorflow1的方法
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

# Gradient descent variations
# SGD on MNIST # stochastic gradient descent (SGD)

# create a session
sess = tf.Session()
# initialize weights
sess.run(tf.global_variables_initializer())

test_loss = []  # placeholder for loss value per iteration

for _ in range(10000):
    # SGD -> batch size = 1
    batch_xs, batch_ys = mnist.train.next_batch(1)
    # update weights
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    # calculate loss funtion on test samples
    loss = sess.run(
        cross_entropy, feed_dict={x: mnist.test.images, y: mnist.test.labels}
    )
    # save it
    test_loss.append(loss)

plt.plot(np.arange(0, 10000, 1), test_loss)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Regularization

# plot a sample
X, Y = get_dataset(50)

x_ = np.arange(-1, 1, 0.01)

plt.scatter(X, Y, color="C1")
plt.plot(x_, np.sin(np.pi * x_), "C0--")
show()

print("------------------------------")  # 30個

# Lets fit data to polynomial of order 20

N = 20  # polynomial order

# add powers of x
X_train = [[x**i for i in range(1, N)] for x in X]

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_train, Y)
show()

# And plot prediction together with training data

X_test = np.linspace(-1, 1, 100)
Y_test = reg.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

# It is clearly overfitted

print("------------------------------")  # 30個

# Lets do the same using Ridge regression

from sklearn.linear_model import Ridge

reg_l2 = Ridge(alpha=0.1)
reg_l2.fit(X_train, Y)

Y_test = reg_l2.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

print(reg.coef_)

print(reg_l2.coef_)

print("------------------------------")  # 30個

# Lets repeat the same for Lasso regression

from sklearn.linear_model import Lasso

reg_l1 = Lasso(alpha=0.001)
reg_l1.fit(X_train, Y)

Y_test = reg_l1.predict([[x**i for i in range(1, N)] for x in X_test])

plt.ylim([-1.5, 1.5])

plt.scatter(X, Y, color="C1")
plt.plot(X_test, Y_test, "C0")
show()

print(reg_l1.coef_)

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


print("------------------------------------------------------------")  # 60個
