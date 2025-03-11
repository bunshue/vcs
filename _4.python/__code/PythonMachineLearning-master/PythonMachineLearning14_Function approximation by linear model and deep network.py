"""
Function approximation by linear model and deep network

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

# Function approximation with linear models and neural network

N_points = 75  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 15  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 10  # Std.Dev of the Gaussian noise adder

# Generate feature and output vector following a non-linear function


# Definition of the function with exponential and sinusoidal terms
def func_trans(x):
    result = (20 * x + 3 * x**2 + 0.1 * x**3) * np.sin(x) * np.exp(-0.1 * x)
    return result


# Definition of the function without exponential and sinusoidal terms i.e. just the polynomial
def func_poly(x):
    result = 20 * x + 3 * x**2 + 0.1 * x**3
    return result


# Densely spaced points for generating the ideal functional curve
x_smooth = np.array(np.linspace(x_min, x_max, 501))

# Use one of the following
y_smooth = func_trans(x_smooth)
# y_smooth = func_poly(x_smooth)

# Linearly spaced sample points
X = np.array(np.linspace(x_min, x_max, N_points))

# Added observational/measurement noise
noise_x = np.random.normal(loc=noise_mean, scale=noise_sd, size=N_points)

# Observed output after adding the noise
y = func_trans(X) + noise_x

# Store the values in a DataFrame
df = pd.DataFrame(data=X, columns=["X"])
df["Ideal y"] = df["X"].apply(func_trans)
df["y"] = y
cc = df.head()
print(cc)

# Plot the function(s), both the ideal characteristic and the observed output (with process and observation noise)

df.plot.scatter(
    "X",
    "y",
    title="True process and measured samples\n",
    grid=True,
    edgecolors=(0, 0, 0),
    c="blue",
    s=60,
    figsize=(10, 6),
)
plt.plot(x_smooth, y_smooth, "k")

show()

# Import scikit-learn librares and prepare train/test splits

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)

X_train = X_train.values.reshape(X_train.size, 1)
y_train = y_train.values.reshape(y_train.size, 1)
X_test = X_test.values.reshape(X_test.size, 1)
y_test = y_test.values.reshape(y_test.size, 1)

from sklearn import preprocessing

X_scaled = preprocessing.scale(X_train)
y_scaled = preprocessing.scale(y_train)

print(X_train.shape[0])

# Polynomial model with LASSO/Ridge regularization (pipelined) with lineary spaced samples

# Regression model parameters

# Alpha (regularization strength) of ridge regression
ridge_alpha = tuple([10 ** (x) for x in range(-3, 0, 1)])

# Regularization strength parameters of LASSO regression
lasso_eps = 0.0001
lasso_nalpha = 20
lasso_iter = 5000

# Min and max degree of polynomials features to consider
degree_min = 2
degree_max = 8

# Empty lists to store model data
linear_sample_score = []
poly_degree = []
rmse = []
t_linear = []

import time

# Iterate over increasing degree of polynomial complexity
for degree in range(degree_min, degree_max + 1):
    t1 = time.time()
    model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha, cv=5))
    # model = make_pipeline(PolynomialFeatures(degree), LassoCV(eps=lasso_eps,n_alphas=lasso_nalpha,
    #                                                              max_iter=lasso_iter,normalize=True,cv=5))
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    t2 = time.time()
    t = t2 - t1
    t_linear.append(t)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(test_pred - y_test)))
    test_score = model.score(X_test, y_test)
    linear_sample_score.append(test_score)
    rmse.append(RMSE)
    poly_degree.append(degree)
    # print("Test score of model with degree {}: {}\n".format(degree,test_score))

    plt.figure()
    plt.title(
        "Predicted vs. actual for polynomial of degree {}".format(degree), fontsize=15
    )
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(poly_degree, rmse, lw=3, c="red")
plt.xlabel("\nModel Complexity: Degree of polynomial", fontsize=20)
plt.ylabel("Root-mean-square error on test set", fontsize=15)

show()

df_score = pd.DataFrame(
    data={
        "degree": [d for d in range(degree_min, degree_max + 1)],
        "Linear sample score": linear_sample_score,
    }
)

t_linear = np.array(t_linear)
time_linear = np.sum(t_linear)

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(poly_degree, linear_sample_score, lw=3, c="red")
plt.xlabel("\nModel Complexity: Degree of polynomial", fontsize=20)
plt.ylabel("R^2 score on test set", fontsize=15)

show()

print("------------------------------------------------------------")  # 60個

# Neural network for regression

import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

# Neural network parameters

learning_rate = 0.00001
training_epochs = 100000

n_input = 1  # Number of features
n_output = 1  # Regression output is a number only

n_hidden_layer = 25  # number of neurons in the hidden layer

# Weights and bias variable

# Store layers weight & bias as Variables classes in dictionaries
weights = {
    "hidden_layer": tf.Variable(tf.random.normal([n_input, n_hidden_layer])),
    "out": tf.Variable(tf.random.normal([n_hidden_layer, n_output])),
}
biases = {
    "hidden_layer": tf.Variable(tf.random.normal([n_hidden_layer])),
    "out": tf.Variable(tf.random.normal([n_output])),
}

print("Shape of the weights tensor of hidden layer:", weights["hidden_layer"].shape)
print("Shape of the weights tensor of output layer:", weights["out"].shape)
print("--------------------------------------------------------")
print("Shape of the bias tensor of hidden layer:", biases["hidden_layer"].shape)
print("Shape of the bias tensor of output layer:", biases["out"].shape)


with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    w = sess.run(weights["hidden_layer"])
    b = sess.run(biases["hidden_layer"])
print(
    "Weight tensor initialized randomly\n---------------------------------------\n", w
)
print("Bias tensor initialized randomly\n---------------------------------------\n", b)
sess.close()

# Input data as placeholder

# tf Graph input
x = tf.placeholder("float32", [None, n_input])
y = tf.placeholder("float32", [None, n_output])

# Hidden and output layers definition (using TensorFlow mathematical functions)

# Hidden layer with RELU activation
layer_1 = tf.add(tf.matmul(x, weights["hidden_layer"]), biases["hidden_layer"])
layer_1 = tf.nn.relu(layer_1)

# Output layer with linear activation
ops = tf.add(tf.matmul(layer_1, weights["out"]), biases["out"])

# Define loss and optimizer
cost = tf.reduce_mean(tf.squared_difference(ops, y))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(
    learning_rate=learning_rate
).minimize(cost)

# TensorFlow Session for training and loss estimation

from tqdm import tqdm
import time

# Initializing the variables
init = tf.global_variables_initializer()

# Empty lists for book-keeping purpose
epoch = 0
log_epoch = []
epoch_count = []
acc = []
loss_epoch = []

# Launch the graph and time the session
t1 = time.time()
with tf.Session() as sess:
    sess.run(init)
    # Loop over epochs
    for epoch in tqdm(range(training_epochs)):
        # Run optimization process (backprop) and cost function (to get loss value)
        _, l = sess.run([optimizer, cost], feed_dict={x: X_train, y: y_train})
        loss_epoch.append(l)  # Save the loss for every epoch
        epoch_count.append(epoch + 1)  # Save the epoch count

        # print("Epoch {}/{} finished. Loss: {}, Accuracy: {}".format(epoch+1,training_epochs,round(l,4),round(accu,4)))
        # print("Epoch {}/{} finished. Loss: {}".format(epoch+1,training_epochs,round(l,4)))
    w = sess.run(weights)
    b = sess.run(biases)
    yhat = sess.run(ops, feed_dict={x: X_test})
t2 = time.time()

time_SNN = t2 - t1

# Plot loss function as training epochs progress

plt.plot(loss_epoch)

show()

# Calculate and print root-mean-squared error and R^2 value for the fit

# Total variance
SSt_SNN = np.sum(np.square(y_test - np.mean(y_test)))
# Residual sum of squares
SSr_SNN = np.sum(np.square(yhat - y_test))
# Root-mean-square error
RMSE_SNN = np.sqrt(np.sum(np.square(yhat - y_test)))
# R^2 coefficient
r2_SNN = 1 - (SSr_SNN / SSt_SNN)

print("RMSE error of the shallow neural network:", RMSE_SNN)
print("R^2 value of the shallow neural network:", r2_SNN)

# RMSE error of the shallow neural network: 779.363682123
# R^2 value of the shallow neural network: 0.142786064062

# Plot residuals plots

plt.figure(figsize=(10, 6))
plt.title(
    "Predicted vs. actual (test set) for shallow (1-hidden layer) neural network\n",
    fontsize=15,
)
plt.xlabel("Actual values (test set)")
plt.ylabel("Predicted values")
plt.scatter(y_test, yhat, edgecolors="k", s=100, c="green")
plt.grid(True)
plt.plot(y_test, y_test, "r", lw=2)

show()

plt.figure(figsize=(10, 6))
plt.scatter(yhat, y_test - yhat, edgecolors="k", s=100, c="red")
plt.title(
    "Residual vs. fitted values for shallow (1-hidden layer) neural network\n",
    fontsize=15,
)
plt.xlabel("\nFitted values", fontsize=15)
plt.ylabel(
    "Residuals: Difference between actual (test set)\n and predicted values",
    fontsize=15,
)
plt.grid(True)
plt.axhline(y=0, lw=2, c="red")

show()

# More hidden layers
# Hyperparameters and layers' variables

learning_rate = 0.00001
training_epochs = 35000

n_input = 1  # Number of features
n_output = 1  # Regression output is a number only

n_hidden_layer_1 = 25  # Hidden layer 1
n_hidden_layer_2 = 25  # Hidden layer 2

# Weights and bias variable

# Store layers weight & bias as Variables classes in dictionaries
weights = {
    "hidden_layer_1": tf.Variable(tf.random_normal([n_input, n_hidden_layer_1])),
    "hidden_layer_2": tf.Variable(
        tf.random_normal([n_hidden_layer_1, n_hidden_layer_2])
    ),
    "out": tf.Variable(tf.random_normal([n_hidden_layer_2, n_output])),
}
biases = {
    "hidden_layer_1": tf.Variable(tf.random_normal([n_hidden_layer_1])),
    "hidden_layer_2": tf.Variable(tf.random_normal([n_hidden_layer_2])),
    "out": tf.Variable(tf.random_normal([n_output])),
}

print("Shape of the weights tensor of hidden layer 1:", weights["hidden_layer_1"].shape)
print("Shape of the weights tensor of hidden layer 2:", weights["hidden_layer_2"].shape)
print("Shape of the weights tensor of output layer:", weights["out"].shape)
print("--------------------------------------------------------")
print("Shape of the bias tensor of hidden layer 1:", biases["hidden_layer_1"].shape)
print("Shape of the bias tensor of hidden layer 2:", biases["hidden_layer_2"].shape)
print("Shape of the bias tensor of output layer:", biases["out"].shape)

# Input data as placeholder

# tf Graph input
x = tf.placeholder("float32", [None, n_input])
y = tf.placeholder("float32", [None, n_output])

# Hidden and output layers definition (using TensorFlow mathematical functions)

# Hidden layer with RELU activation
layer_1 = tf.add(tf.matmul(x, weights["hidden_layer_1"]), biases["hidden_layer_1"])
layer_1 = tf.nn.relu(layer_1)

layer_2 = tf.add(
    tf.matmul(layer_1, weights["hidden_layer_2"]), biases["hidden_layer_2"]
)
layer_2 = tf.nn.relu(layer_2)

# Output layer with linear activation
ops = tf.add(tf.matmul(layer_2, weights["out"]), biases["out"])

# Gradient descent optimizer for training (backpropagation)

# Define loss and optimizer
cost = tf.reduce_mean(tf.squared_difference(ops, y))
optimizer = tf.compat.v1.train.GradientDescentOptimizer(
    learning_rate=learning_rate
).minimize(cost)

# TensorFlow Session for training and loss estimation

from tqdm import tqdm
import time

# Initializing the variables
init = tf.global_variables_initializer()

# Empty lists for book-keeping purpose
epoch = 0
log_epoch = []
epoch_count = []
acc = []
loss_epoch = []

# Launch the graph and time the session
t1 = time.time()
with tf.Session() as sess:
    sess.run(init)
    # Loop over epochs
    for epoch in tqdm(range(training_epochs)):
        # Run optimization process (backprop) and cost function (to get loss value)
        _, l = sess.run([optimizer, cost], feed_dict={x: X_train, y: y_train})
        loss_epoch.append(l)  # Save the loss for every epoch
        epoch_count.append(epoch + 1)  # Save the epoch count

        # print("Epoch {}/{} finished. Loss: {}, Accuracy: {}".format(epoch+1,training_epochs,round(l,4),round(accu,4)))
        # print("Epoch {}/{} finished. Loss: {}".format(epoch+1,training_epochs,round(l,4)))
    w = sess.run(weights)
    b = sess.run(biases)
    yhat = sess.run(ops, feed_dict={x: X_test})

t2 = time.time()
time_DNN = t2 - t1

# Plot loss function as training epochs progress

plt.plot(loss_epoch)

show()

# Calculate and print root-mean-squared error and R^2 value for the fit

# Total variance
SSt_DNN = np.sum(np.square(y_test - np.mean(y_test)))
# Residual sum of squares
SSr_DNN = np.sum(np.square(yhat - y_test))
# Root-mean-square error
RMSE_DNN = np.sqrt(np.sum(np.square(yhat - y_test)))
# R^2 coefficient
r2_DNN = 1 - (SSr_DNN / SSt_DNN)

print("RMSE error of the deep neural network:", RMSE_DNN)
print("R^2 value of the deep neural network:", r2_DNN)

# RMSE error of the deep neural network: 308.205336459
# R^2 value of the deep neural network: 0.86594309056

# Plot residuals plots

plt.figure(figsize=(10, 6))
plt.title(
    "Predicted vs. actual (test set) for deep (2-layer) neural network\n", fontsize=15
)
plt.xlabel("Actual values (test set)", fontsize=15)
plt.ylabel("Predicted values", fontsize=15)
plt.scatter(y_test, yhat, edgecolors="k", s=100, c="green")
plt.grid(True)
plt.plot(y_test, y_test, "r", lw=2)

show()

plt.figure(figsize=(10, 6))
plt.scatter(yhat, y_test - yhat, edgecolors="k", s=100, c="red")
plt.title("Residual vs. fitted values for deep (2-layer) neural network\n", fontsize=15)
plt.xlabel("\nFitted values", fontsize=15)
plt.ylabel(
    "Residuals: Difference between actual (test set)\n and predicted values",
    fontsize=15,
)
plt.grid(True)
plt.axhline(y=0, lw=2, c="red")

show()

plt.figure(figsize=(10, 6))
plt.title("Time taken for building/fitting models\n", fontsize=16)
plt.ylabel("Time taken to build model", fontsize=12)
plt.xlabel("Various types of models", fontsize=14)
plt.grid(True)
plt.bar(
    left=[1, 2, 3],
    height=[time_linear, time_SNN, time_DNN],
    align="center",
    tick_label=[
        "Linear model with regularization",
        "1-hidden layer NN",
        "2-hidden layer NN",
    ],
)

show()

plt.figure(figsize=(10, 6))
plt.title("$R^2$-fit values of the models\n", fontsize=16)
plt.ylabel("$R^2$-fit value achieved by the model", fontsize=12)
plt.xlabel("Various types of models", fontsize=14)
plt.grid(True)
plt.bar(
    left=[1, 2, 3],
    height=[max(linear_sample_score), r2_SNN, r2_DNN],
    align="center",
    tick_label=[
        "Linear model with regularization",
        "1-hidden layer NN",
        "2-hidden layer NN",
    ],
)

show()

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
