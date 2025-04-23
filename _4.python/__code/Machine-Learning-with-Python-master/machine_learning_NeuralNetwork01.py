"""
machine_learning_NeuralNetwork01

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

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵
from sklearn.linear_model import LinearRegression  # 函數學習機
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear_Regression_Methods
"""
Linear regression with various methods

This is a very simple example of using two scipy tools for linear regression.

    Scipy.Polyfit
    Stats.linregress
    Optimize.curve_fit
    numpy.linalg.lstsq
    statsmodels.OLS
    Analytic solution using Moore-Penrose generalized inverse or simple multiplicative matrix inverse
    LinearRegression 線性迴歸機
"""
from scipy import stats
from scipy import optimize
import statsmodels.api as sm

# Generate random data of a sufficiently large size

# Sample data creation
# number of points
n = int(5e6)
t = np.linspace(-10, 10, n)
# parameters
a = 3.25
b = -6.5
x = np.polyval([a, b], t)
# add some noise
xn = x + 3 * np.random.randn(n)

# Draw few random sample points and plot

xvar = np.random.choice(t, size=20)
yvar = np.polyval([a, b], xvar) + 3 * np.random.randn(20)
plt.scatter(xvar, yvar, c="green", edgecolors="k")
plt.grid(True)
show()

# Method: Scipy.Polyfit

# Linear regressison -polyfit - polyfit can be used other orders polynomials
t1 = time.time()
(ar, br) = np.polyfit(t, xn, 1)
xr = np.polyval([ar, br], t)
# compute the mean square error
err = np.sqrt(sum((xr - xn) ** 2) / n)
t2 = time.time()
t_polyfit = float(t2 - t1)

print("Linear regression using polyfit")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))
print("Time taken: {} seconds".format(t_polyfit))

# Linear regression using polyfit
# parameters: a=3.25 b=-6.50, ms error= 3.000
# Time taken: 1.7698638439178467 seconds

# Method: Stats.linregress

# Linear regression using stats.linregress
t1 = time.time()
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
t2 = time.time()
t_linregress = float(t2 - t1)

print("Linear regression using stats.linregress")
print("a=%.2f b=%.2f, std error= %.3f, r^2 coefficient= %.3f" % (a_s, b_s, stderr, r))
print("Time taken: {} seconds".format(t_linregress))

# Linear regression using stats.linregress
# a=3.25 b=-6.50, std error= 0.000, r^2 coefficient= 0.987
# Time taken: 0.15017366409301758 seconds

# Method: Optimize.curve_fit


def flin(t, a, b):
    result = a * t + b
    return result


t1 = time.time()
p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")
t2 = time.time()
t_optimize_curve_fit = float(t2 - t1)

print("Linear regression using optimize.curve_fit")
print("parameters: a=%.2f b=%.2f" % (p1[0], p1[1]))
print("Time taken: {} seconds".format(t_optimize_curve_fit))

# Linear regression using optimize.curve_fit
# parameters: a=3.25 b=-6.50
# Time taken: 1.2034447193145752 seconds

# Method: numpy.linalg.lstsq

t1 = time.time()
A = np.vstack([t, np.ones(len(t))]).T
result = np.linalg.lstsq(A, xn)
ar, br = result[0]
err = np.sqrt(result[1] / len(xn))
t2 = time.time()
t_linalg_lstsq = float(t2 - t1)

print("Linear regression using numpy.linalg.lstsq")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))
print("Time taken: {} seconds".format(t_linalg_lstsq))

# Linear regression using numpy.linalg.lstsq
# parameters: a=3.25 b=-6.50, ms error= 3.000
# Time taken: 0.3698573112487793 seconds

# Method: Statsmodels.OLS

t1 = time.time()
t = sm.add_constant(t)
model = sm.OLS(x, t)
results = model.fit()
ar = results.params[1]
br = results.params[0]
t2 = time.time()
t_OLS = float(t2 - t1)

print("Linear regression using statsmodels.OLS")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_OLS))

# Linear regression using statsmodels.OLS
# parameters: a=3.25 b=-6.50
# Time taken: 0.9167804718017578 seconds

print(results.summary())

# Analytic solution using Moore-Penrose pseudoinverse

t1 = time.time()
mpinv = np.linalg.pinv(t)
result = mpinv.dot(x)
ar = result[1]
br = result[0]
t2 = time.time()
t_inv_matrix = float(t2 - t1)

print("Linear regression using Moore-Penrose inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_inv_matrix))

# Linear regression using Moore-Penrose inverse
# parameters: a=3.25 b=-6.50
# Time taken: 0.6019864082336426 seconds

# Analytic solution using simple multiplicative matrix inverse

t1 = time.time()
m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
ar = m[1]
br = m[0]
t2 = time.time()
t_simple_inv = float(t2 - t1)

print("Linear regression using simple inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_simple_inv))

# Linear regression using simple inverse
# parameters: a=3.25 b=-6.50
# Time taken: 0.13125276565551758 seconds

# 線性迴歸機

t1 = time.time()
lm = LinearRegression()  # 函數學習機
lm.fit(t, x)
ar = lm.coef_[1]
br = lm.intercept_
t2 = time.time()
t_sklearn_linear = float(t2 - t1)

print("Linear regression using LinearRegression 線性迴歸機")
print("parameters: a=%.2f b=%.2f" % (ar, br))
print("Time taken: {} seconds".format(t_sklearn_linear))

# Linear regression using LinearRegression 線性迴歸機
# parameters: a=3.25 b=-6.50
# Time taken: 0.5318112373352051 seconds

# Bucket all the execution times in a list and plot

times = [
    t_polyfit,
    t_linregress,
    t_optimize_curve_fit,
    t_linalg_lstsq,
    t_OLS,
    t_inv_matrix,
    t_simple_inv,
    t_sklearn_linear,
]

plt.figure(figsize=(20, 5))
plt.grid(True)
plt.bar(
    x=[l * 0.8 for l in range(8)],
    height=times,
    width=0.4,
    tick_label=[
        "Polyfit",
        "Stats.linregress",
        "Optimize.curve_fit",
        "numpy.linalg.lstsq",
        "statsmodels.OLS",
        "Moore-Penrose matrix inverse",
        "Simple matrix inverse",
        "sklearn.linear_model",
    ],
)
show()

n_min = 50000
n_max = int(1e7)
n_levels = 25
r = np.log10(n_max / n_min)
l = np.linspace(0, r, n_levels)
n_data = list((n_min * np.power(10, l)))
n_data = [int(n) for n in n_data]

# time_dict={'Polyfit':[],'Stats.lingress':[],'Optimize.curve_fit':[],'linalg.lstsq':[],'statsmodels.OLS':[],
#'Moore-Penrose matrix inverse':[],'Simple matrix inverse':[], 'sklearn.linear_model':[]}

l1 = [
    "Polyfit",
    "Stats.lingress",
    "Optimize.curve_fit",
    "linalg.lstsq",
    "statsmodels.OLS",
    "Moore-Penrose matrix inverse",
    "Simple matrix inverse",
    "sklearn.linear_model",
]
time_dict = {key: [] for key in l1}

from tqdm import tqdm

for i in tqdm(range(len(n_data))):
    t = np.linspace(-10, 10, n_data[i])
    # parameters
    a = 3.25
    b = -6.5
    x = np.polyval([a, b], t)
    # add some noise
    xn = x + 3 * np.random.randn(n_data[i])

    # Linear regressison -polyfit - polyfit can be used other orders polynomials
    t1 = time.time()
    (ar, br) = np.polyfit(t, xn, 1)
    t2 = time.time()
    t_polyfit = 1e3 * float(t2 - t1)
    time_dict["Polyfit"].append(t_polyfit)

    # Linear regression using stats.linregress
    t1 = time.time()
    (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)
    t2 = time.time()
    t_linregress = 1e3 * float(t2 - t1)
    time_dict["Stats.lingress"].append(t_linregress)

    # Linear regression using optimize.curve_fit
    t1 = time.time()
    p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")
    t2 = time.time()
    t_optimize_curve_fit = 1e3 * float(t2 - t1)
    time_dict["Optimize.curve_fit"].append(t_optimize_curve_fit)

    # Linear regression using np.linalg.lstsq (solving Ax=B equation system)
    t1 = time.time()
    A = np.vstack([t, np.ones(len(t))]).T
    result = np.linalg.lstsq(A, xn)
    ar, br = result[0]
    t2 = time.time()
    t_linalg_lstsq = 1e3 * float(t2 - t1)
    time_dict["linalg.lstsq"].append(t_linalg_lstsq)

    # Linear regression using statsmodels.OLS
    t1 = time.time()
    t = sm.add_constant(t)
    model = sm.OLS(x, t)
    results = model.fit()
    ar = results.params[1]
    br = results.params[0]
    t2 = time.time()
    t_OLS = 1e3 * float(t2 - t1)
    time_dict["statsmodels.OLS"].append(t_OLS)

    # Linear regression using Moore-Penrose pseudoinverse matrix
    t1 = time.time()
    mpinv = np.linalg.pinv(t)
    result = mpinv.dot(x)
    ar = result[1]
    br = result[0]
    t2 = time.time()
    t_mpinverse = 1e3 * float(t2 - t1)
    time_dict["Moore-Penrose matrix inverse"].append(t_mpinverse)

    # Linear regression using simple multiplicative inverse matrix
    t1 = time.time()
    m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
    ar = m[1]
    br = m[0]
    t2 = time.time()
    t_simple_inv = 1e3 * float(t2 - t1)
    time_dict["Simple matrix inverse"].append(t_simple_inv)

    # Linear regression using scikit-learn's linear_model
    t1 = time.time()
    lm = LinearRegression()  # 函數學習機
    lm.fit(t, x)
    ar = lm.coef_[1]
    br = lm.intercept_
    t2 = time.time()
    t_sklearn_linear = 1e3 * float(t2 - t1)
    time_dict["sklearn.linear_model"].append(t_sklearn_linear)

df = pd.DataFrame(data=time_dict)
print(df)

plt.figure(figsize=(15, 10))
for i in df.columns:
    plt.semilogx((n_data), df[i], lw=3)
plt.xticks([1e5, 2e5, 5e5, 1e6, 2e6, 5e6, 1e7])
plt.xlabel("\nSize of the data set (number of samples)")
plt.yticks()
plt.ylabel("Milliseconds needed for simple linear regression model fit")
plt.grid(True)
plt.legend([name for name in df.columns])

show()

a1 = df.iloc[n_levels - 1]

plt.figure(figsize=(20, 5))
plt.grid(True)
plt.bar(x=[l * 0.8 for l in range(8)], height=a1, width=0.4, tick_label=list(a1.index))
show()

sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Polynomial regression - linear and neural network

# Polynomial regression with linear models and neural network

N_points = 500  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 10  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 2  # Std.Dev of the Gaussian noise adder
ridge_alpha = tuple(
    [10 ** (x) for x in range(-3, 0, 1)]
)  # Alpha (regularization strength) of ridge regression
lasso_eps = 0.001
lasso_nalpha = 20
lasso_iter = 1000
degree_min = 2
degree_max = 8

x_smooth = np.array(np.linspace(x_min, x_max, 501))

# Linearly spaced sample points
X = np.array(np.linspace(x_min, x_max, N_points))

# Samples drawn from uniform random distribution
X_sample = x_min + np.random.rand(N_points) * (x_max - x_min)


def func(x):
    result = (20 * x + 3 * x**2 + 0.1 * x**3) * np.sin(x) * np.exp(-(1 / x_max) * x)
    return result


noise_x = np.random.normal(loc=noise_mean, scale=noise_sd, size=N_points)

y = func(X) + noise_x
y_sampled = func(X_sample) + noise_x

df = pd.DataFrame(data=X, columns=["X"])
df["Ideal y"] = df["X"].apply(func)
df["y"] = y
df["X_sampled"] = X_sample
df["y_sampled"] = y_sampled

cc = df.head()
print(cc)

# Plot the function(s), both the ideal characteristic and the observed output (with process and observation noise)

df.plot.scatter(
    "X",
    "Ideal y",
    title="Ideal y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="blue",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")

show()

df.plot.scatter(
    "X_sampled",
    y="y_sampled",
    title="Randomly sampled y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="orange",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")

show()

# Import scikit-learn librares and prepare train/test splits

from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

n_train = X_train.shape[0]

# Polynomial model with Ridge regularization (pipelined) with lineary spaced samples

linear_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    linear_sample_score.append(test_score)
    poly_degree.append(degree)
    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE))
    # plt.suptitle("Polynomial of degree {}".format(degree))
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

cc = linear_sample_score
print(cc)

# Modeling with randomly sampled data set

X_train, X_test, y_train, y_test = train_test_split(
    df["X_sampled"], df["y_sampled"], test_size=0.33
)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

random_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    random_sample_score.append(test_score)
    poly_degree.append(degree)

    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE))
    # plt.suptitle("Polynomial of degree {}".format(degree))
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

cc = random_sample_score
print(cc)

df_score = pd.DataFrame(
    data={
        "degree": [d for d in range(degree_min, degree_max + 1)],
        "Linear sample score": linear_sample_score,
        "Random sample score": random_sample_score,
    }
)
print(df_score)

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(df_score["degree"], df_score["Linear sample score"], lw=2)
plt.plot(df_score["degree"], df_score["Random sample score"], lw=2)
plt.xlabel("Model Complexity: Degree of polynomial")
plt.ylabel("Model Score: R^2 score on test set")
plt.legend()

show()

# Checking the regularization strength from the cross-validated model pipeline

m = model.steps[1][1]
print(m.alpha_)

# 0.0014941809717564625

# Neural network for regression

import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

learning_rate = 0.000001
training_epochs = 20000

n_input = 1  # Number of features
n_output = 1  # Regression output is a number only

n_hidden_layer = 35  # layer number of features

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)

"""
X_train=X_train.reshape(X_train.size,1)
y_train=y_train.reshape(y_train.size,1)
X_test=X_test.reshape(X_test.size,1)
y_test=y_test.reshape(y_test.size,1)
"""

from sklearn import preprocessing

X_scaled = preprocessing.scale(X_train)
y_scaled = preprocessing.scale(y_train)

# Weights and bias variable

# Store layers weight & bias as Variables classes in dictionaries
weights = {
    "hidden_layer": tf.Variable(tf.random_normal([n_input, n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_hidden_layer, n_output])),
}
biases = {
    "hidden_layer": tf.Variable(tf.random_normal([n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_output])),
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

# Gradient descent optimizer for training (backpropagation):

# Define loss and optimizer
cost = tf.reduce_sum(tf.squared_difference(ops, y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(
    cost
)

# TensorFlow Session for training and loss estimation

from tqdm import tqdm

# Initializing the variables
init = tf.global_variables_initializer()

# Empty lists for book-keeping purpose
epoch = 0
log_epoch = []
epoch_count = []
acc = []
loss_epoch = []

"""
# Launch the graph
with tf.Session() as sess:
    sess.run(init)    
    # Loop over epochs
    for epoch in tqdm(range(training_epochs)):
        # Run optimization process (backprop) and cost function (to get loss value)
        _,l=sess.run([optimizer,cost], feed_dict={x: X_scaled, y: y_scaled})
        loss_epoch.append(l) # Save the loss for every epoch        
        epoch_count.append(epoch+1) #Save the epoch count
       
        # print("Epoch {}/{} finished. Loss: {}, Accuracy: {}".format(epoch+1,training_epochs,round(l,4),round(accu,4)))
        #print("Epoch {}/{} finished. Loss: {}".format(epoch+1,training_epochs,round(l,4)))
    w=sess.run(weights)
    b = sess.run(biases)
    #layer_1 = tf.add(tf.matmul(X_test, w['hidden_layer']),b['hidden_layer'])
    #layer_1 = tf.nn.relu(layer_1)

    # Output layer with no activation
    #ops = tf.add(tf.matmul(layer_1, w['out']), b['out'])

layer1=np.matmul(X_test,w['hidden_layer'])+b['hidden_layer']
layer1_out = np.maximum(layer1,0)
yhat = np.matmul(layer1_out,w['out'])+b['out']

print(yhat-y_test)

plt.plot(epoch_count,loss_epoch)

show()
"""

# Keras

print(X_scaled.shape)

from keras.models import Sequential

from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation

from keras.optimizers import SGD

# from keras.utils import np_utils

# Building the model
model = Sequential()
model.add(Dense(25, activation="linear", input_dim=1))
# model.add(Dropout(.2))
model.add(Dense(25, activation="linear"))
# model.add(Dropout(.1))
model.add(Dense(25, activation="linear"))
model.add(Dense(25, activation="linear"))
model.add(Dense(1, activation="linear"))

# Compiling the model
# sgd = SGD(lr=0.001, decay=0, momentum=0.9, nesterov=True)
sgd = SGD(momentum=0.9, nesterov=True)
model.compile(loss="mean_squared_error", optimizer="sgd")

# NG
# print("檢視模型架構")
# model.summary()  # 檢視模型架構

""" NG

model.fit(X_scaled, y_scaled, epochs=2000, verbose=0)

score = model.evaluate(X_test, y_test)
print(score)

yhat=model.predict(X_test)

print(yhat)

plt.scatter(yhat,y_test)

show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Regularized polynomial regression with linear and random sampling

# Global variables for the program

N_points = 41  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 10  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 2  # Std.Dev of the Gaussian noise adder
ridge_alpha = tuple(
    [10 ** (x) for x in range(-3, 0, 1)]
)  # Alpha (regularization strength) of ridge regression
lasso_eps = 0.001
lasso_nalpha = 20
lasso_iter = 1000
degree_min = 2
degree_max = 8

x_smooth = np.array(np.linspace(x_min, x_max, 1001))

# Linearly spaced sample points
X = np.array(np.linspace(x_min, x_max, N_points))

# Samples drawn from uniform random distribution
X_sample = x_min + np.random.rand(N_points) * (x_max - x_min)


def func(x):
    result = x**2 * np.sin(x) * np.exp(-(1 / x_max) * x)
    return result


noise_x = np.random.normal(loc=noise_mean, scale=noise_sd, size=N_points)

y = func(X) + noise_x
y_sampled = func(X_sample) + noise_x

df = pd.DataFrame(data=X, columns=["X"])
df["Ideal y"] = df["X"].apply(func)
df["y"] = y
df["X_sampled"] = X_sample
df["y_sampled"] = y_sampled

cc = df.head()
print(cc)

# Plot the function(s), both the ideal characteristic and the observed output (with process and observation noise)

df.plot.scatter(
    "X",
    "Ideal y",
    title="Ideal y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="blue",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")

show()

df.plot.scatter(
    "X_sampled",
    y="y_sampled",
    title="Randomly sampled y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="orange",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")

show()

df.plot.scatter(
    "X",
    y="y",
    title="Linearly sampled y",
    grid=True,
    edgecolors=(0, 0, 0),
    c="orange",
    s=40,
    figsize=(10, 5),
)
plt.plot(x_smooth, func(x_smooth), "k")

show()

# Import scikit-learn librares and prepare train/test splits

from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

# Polynomial model with Ridge regularization (pipelined) with lineary spaced samples


linear_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    linear_sample_score.append(test_score)
    poly_degree.append(degree)
    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE))
    # plt.suptitle("Polynomial of degree {}".format(degree))
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

print(linear_sample_score)

# Modeling with randomly sampled data set

X_train, X_test, y_train, y_test = train_test_split(
    df["X_sampled"], df["y_sampled"], test_size=0.33
)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

random_sample_score = []
poly_degree = []
for degree in range(degree_min, degree_max + 1):
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    y_pred = np.array(model.predict(X_train))
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
    test_score = model.score(X_test, y_test)
    random_sample_score.append(test_score)
    poly_degree.append(degree)

    print("Test score of model with degree {}: {}\n".format(degree, test_score))

    # plt.figure()
    # plt.title("RMSE: {}".format(RMSE))
    # plt.suptitle("Polynomial of degree {}".format(degree))
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

print(random_sample_score)

df_score = pd.DataFrame(
    data={
        "degree": [d for d in range(degree_min, degree_max + 1)],
        "Linear sample score": linear_sample_score,
        "Random sample score": random_sample_score,
    }
)
print(df_score)


plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(df_score["degree"], df_score["Linear sample score"], lw=2)
plt.plot(df_score["degree"], df_score["Random sample score"], lw=2)
plt.xlabel("Model Complexity: Degree of polynomial")
plt.ylabel("Model Score: R^2 score on test set")
plt.legend()

show()

# Checking the regularization strength from the cross-validated model pipeline

m = model.steps[1][1]
print(m.alpha_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Regularized polynomial regression with linear and random sampling - LOOP

# Ridge/LASSO polynomial regression with linear and random sampling

from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

N_points = 41  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 10  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 5  # Std.Dev of the Gaussian noise adder
ridge_alpha = tuple(
    [10 ** (x) for x in range(-4, 0, 1)]
)  # Alpha (regularization strength) of ridge regression
lasso_eps = 0.001
lasso_nalpha = 20
lasso_iter = 2000
degree_min = 2
degree_max = 8

# Generate feature and output vector following a non-linear function


def func(x):
    result = x**2 * np.sin(x) * np.exp(-(1 / x_max) * x)
    return result


noise_x = np.random.normal(loc=noise_mean, scale=noise_sd, size=N_points)

var_linear = []
var_random = []
mean_linear = []
mean_random = []
dfs = []

for i in range(50):
    # x_smooth = np.array(np.linspace(x_min,x_max,1001))
    # Linearly spaced sample points
    X = np.array(np.linspace(x_min, x_max, N_points))
    # Samples drawn from uniform random distribution
    X_sample = x_min + np.random.rand(N_points) * (x_max - x_min)
    # noise_x = np.random.normal(loc=noise_mean,scale=noise_sd,size=N_points)

    y = func(X) + noise_x
    y_sampled = func(X_sample) + noise_x

    df = pd.DataFrame(data=X, columns=["X"])
    df["Ideal y"] = df["X"].apply(func)
    df["y"] = y
    df["X_sampled"] = X_sample
    df["y_sampled"] = y_sampled

    X_train, X_test, y_train, y_test = train_test_split(
        df["X"], df["y"], test_size=0.33
    )
    X_train = X_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)

    linear_sample_score = []
    poly_degree = []
    for degree in range(degree_min, degree_max + 1):
        model = make_pipeline(
            PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha, cv=5)
        )
        # model = make_pipeline(PolynomialFeatures(degree), LassoCV(eps=lasso_eps,n_alphas=lasso_nalpha,
        # max_iter=lasso_iter,normalize=True,cv=5))
        # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
        model.fit(X_train, y_train)
        y_pred = np.array(model.predict(X_train))
        test_pred = np.array(model.predict(X_test))
        RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
        test_score = model.score(X_test, y_test)
        linear_sample_score.append(test_score)
        poly_degree.append(degree)

    var_linear.append(np.std(np.array(linear_sample_score)))
    mean_linear.append(np.mean(np.array(linear_sample_score)))

    # Modeling with randomly sampled data set
    X_train, X_test, y_train, y_test = train_test_split(
        df["X_sampled"], df["y_sampled"], test_size=0.33
    )
    X_train = X_train.values.reshape(-1, 1)
    X_test = X_test.values.reshape(-1, 1)

    random_sample_score = []
    poly_degree = []
    for degree in range(degree_min, degree_max + 1):
        model = make_pipeline(
            PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha, cv=5)
        )
        # model = make_pipeline(PolynomialFeatures(degree), LassoCV(eps=lasso_eps,n_alphas=lasso_nalpha,
        # max_iter=lasso_iter,normalize=True,cv=5))
        # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
        model.fit(X_train, y_train)
        y_pred = np.array(model.predict(X_train))
        test_pred = np.array(model.predict(X_test))
        RMSE = np.sqrt(np.sum(np.square(y_pred - y_train)))
        test_score = model.score(X_test, y_test)
        random_sample_score.append(test_score)
        poly_degree.append(degree)

    var_random.append(np.std(np.array(random_sample_score)))
    mean_random.append(np.mean(np.array(random_sample_score)))

    df_score = pd.DataFrame(
        data={
            "degree": [d for d in range(degree_min, degree_max + 1)],
            "Linear sample score": linear_sample_score,
            "Random sample score": random_sample_score,
        }
    )
    dfs.append(df_score)
    # print(df_score)
    # print("\n")
    print("Run # {} finished".format(i + 1))


df1 = pd.concat(dfs)

rand = []
lin = []
for i in range(degree_max + 1 - degree_min):
    rand.append(df1.loc[i]["Random sample score"].mean())
    lin.append(df1.loc[i]["Linear sample score"].mean())

plt.figure(figsize=(8, 5))
plt.plot(range(degree_min, degree_max + 1), lin)
plt.plot(range(degree_min, degree_max + 1), rand)
plt.xlabel("Model complexity (degree of polynomial)")
plt.ylabel("Model score on test set")
plt.legend(["Linear sampling method", "Random sampling method"])
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Function approximation by linear model and deep network

# Function approximation with linear models and neural network

# Global variables for the program

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

from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
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
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(poly_degree, rmse, lw=3, c="red")
plt.xlabel("\nModel Complexity: Degree of polynomial")
plt.ylabel("Root-mean-square error on test set")

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
plt.xlabel("\nModel Complexity: Degree of polynomial")
plt.ylabel("R^2 score on test set")

show()

# Neural network for regression
# Import and declaration of variables

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
    "hidden_layer": tf.Variable(tf.random_normal([n_input, n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_hidden_layer, n_output])),
}
biases = {
    "hidden_layer": tf.Variable(tf.random_normal([n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_output])),
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
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(
    cost
)

from tqdm import tqdm

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

# Plot residuals plots

plt.figure(figsize=(10, 6))
plt.title("Predicted vs. actual (test set) for shallow (1-hidden layer) neural network")
plt.xlabel("Actual values (test set)")
plt.ylabel("Predicted values")
plt.scatter(y_test, yhat, edgecolors="k", s=100, c="green")
plt.grid(True)
plt.plot(y_test, y_test, "r", lw=2)

show()

plt.figure(figsize=(10, 6))
plt.scatter(yhat, y_test - yhat, edgecolors="k", s=100, c="red")
plt.title("Residual vs. fitted values for shallow (1-hidden layer) neural network")
plt.xlabel("\nFitted values")
plt.ylabel("Residuals: Difference between actual (test set)\n and predicted values")
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
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(
    cost
)

# TensorFlow Session for training and loss estimation

from tqdm import tqdm

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

# Plot residuals plots

plt.figure(figsize=(10, 6))
plt.title("Predicted vs. actual (test set) for deep (2-layer) neural network")
plt.xlabel("Actual values (test set)")
plt.ylabel("Predicted values")
plt.scatter(y_test, yhat, edgecolors="k", s=100, c="green")
plt.grid(True)
plt.plot(y_test, y_test, "r", lw=2)

show()

plt.figure(figsize=(10, 6))
plt.scatter(yhat, y_test - yhat, edgecolors="k", s=100, c="red")
plt.title("Residual vs. fitted values for deep (2-layer) neural network")
plt.xlabel("\nFitted values")
plt.ylabel("Residuals: Difference between actual (test set)\n and predicted values")
plt.grid(True)
plt.axhline(y=0, lw=2, c="red")

show()

plt.figure(figsize=(10, 6))
plt.title("Time taken for building/fitting models")
plt.ylabel("Time taken to build model")
plt.xlabel("Various types of models")
plt.grid(True)
plt.bar(
    x=[1, 2, 3],
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
plt.title("$R^2$-fit values of the models")
plt.ylabel("$R^2$-fit value achieved by the model")
plt.xlabel("Various types of models")
plt.grid(True)
plt.bar(
    x=[1, 2, 3],
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

# Function approximation by linear model and deep network LOOP test

# Function approximation with linear models and neural network

# Global variables for the program

N_points = 100  # Number of points for constructing function
x_min = 1  # Min of the range of x (feature)
x_max = 25  # Max of the range of x (feature)
noise_mean = 0  # Mean of the Gaussian noise adder
noise_sd = 10  # Std.Dev of the Gaussian noise adder
test_set_fraction = 0.2


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
df["Sin_X"] = df["X"].apply(math.sin)
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

from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(
    df[["X", "Sin_X"]], df["y"], test_size=test_set_fraction
)

# X_train=X_train.reshape(X_train.size,1)
# y_train=y_train.reshape(y_train.size,1)
# X_test=X_test.reshape(X_test.size,1)
# y_test=y_test.reshape(y_test.size,1)

# X_train=X_train.reshape(-1,1)
# y_train=y_train.reshape(-1,1)
# X_test=X_test.reshape(-1,1)
# y_test=y_test.reshape(-1,1)

from sklearn import preprocessing

X_scaled = preprocessing.scale(X_train)
y_scaled = preprocessing.scale(y_train)

# Polynomial model with LASSO/Ridge regularization (pipelined) with lineary spaced samples

# Regression model parameters
ridge_alpha = tuple(
    [10 ** (x) for x in range(-3, 0, 1)]
)  # Alpha (regularization strength) of ridge regression
# Alpha (regularization strength) of LASSO regression
lasso_eps = 0.0001
lasso_nalpha = 20
lasso_iter = 5000

# Min and max degree of polynomials features to consider
degree_min = 2
degree_max = 8

linear_sample_score = []
poly_degree = []
rmse = []
t_linear = []
import time

for degree in range(degree_min, degree_max + 1):
    t1 = time.time()
    # model = make_pipeline(PolynomialFeatures(degree), RidgeCV(alphas=ridge_alpha,normalize=True,cv=5))
    model = make_pipeline(
        PolynomialFeatures(degree),
        LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
    )
    # model = make_pipeline(PolynomialFeatures(degree), LinearRegression(normalize=True))
    model.fit(X_train, y_train)
    t2 = time.time()
    t = t2 - t1
    t_linear.append(t)
    test_pred = np.array(model.predict(X_test))
    RMSE = np.sqrt(np.sum(np.square(test_pred - y_test)))
    test_score = model.score(X_test, y_test)
    linear_sample_score.append(test_score)
    rmse.append(RMSE)
    poly_degree.append(degree)
    # print("Test score of model with degree {}: {}\n".format(degree,test_score))

    plt.figure()
    plt.title("Predicted vs. actual for polynomial of degree {}".format(degree))
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
    show()

print(linear_sample_score)

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(poly_degree, rmse, lw=3, c="red")
plt.title("Model complexity (highest polynomial degree) vs. test score")
plt.xlabel("\nDegree of polynomial")
plt.ylabel("Root-mean-square error on test set")

show()

df_score = pd.DataFrame(
    data={
        "degree": [d for d in range(degree_min, degree_max + 1)],
        "Linear sample score": linear_sample_score,
    }
)

# Save the best R^2 score
r2_linear = max(linear_sample_score)
print("Best R^2 score for linear polynomial degree models:", r2_linear)

# Best R^2 score for linear polynomial degree models: 0.995693773025

plt.figure(figsize=(8, 5))
plt.grid(True)
plt.plot(poly_degree, linear_sample_score, lw=3, c="red")
plt.xlabel("\nModel Complexity: Degree of polynomial")
plt.ylabel("R^2 score on test set")

show()

# 1-hidden layer (Shallow) network

import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

learning_rate = 1e-6
training_epochs = 150000

n_input = 1  # Number of features
n_output = 1  # Regression output is a number only

n_hidden_layer = 100  # layer number of features

weights = {
    "hidden_layer": tf.Variable(tf.random_normal([n_input, n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_hidden_layer, n_output])),
}
biases = {
    "hidden_layer": tf.Variable(tf.random_normal([n_hidden_layer])),
    "out": tf.Variable(tf.random_normal([n_output])),
}

# tf Graph input
x = tf.placeholder("float32", [None, n_input])
y = tf.placeholder("float32", [None, n_output])

# Hidden layer with RELU activation
layer_1 = tf.add(tf.matmul(x, weights["hidden_layer"]), biases["hidden_layer"])
layer_1 = tf.sin(layer_1)

# Output layer with linear activation
ops = tf.add(tf.matmul(layer_1, weights["out"]), biases["out"])

# Define loss and optimizer
cost = tf.reduce_mean(tf.squared_difference(ops, y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(
    cost
)

from tqdm import tqdm

# Initializing the variables
init = tf.global_variables_initializer()

# Empty lists for book-keeping purpose
epoch = 0
log_epoch = []
epoch_count = []
acc = []
loss_epoch = []

X_train, X_test, y_train, y_test = train_test_split(
    df["X"], df["y"], test_size=test_set_fraction
)
"""
X_train=X_train.reshape(X_train.size,1)
y_train=y_train.reshape(y_train.size,1)
X_test=X_test.reshape(X_test.size,1)
y_test=y_test.reshape(y_test.size,1)
"""
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

plt.plot(loss_epoch)

show()

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

plt.figure(figsize=(10, 6))
plt.title("Predicted vs. actual (test set) for shallow (1-hidden layer) neural network")
plt.xlabel("Actual values (test set)")
plt.ylabel("Predicted values")
plt.scatter(y_test, yhat, edgecolors="k", s=100, c="green")
plt.grid(True)
plt.plot(y_test, y_test, "r", lw=2)

show()

# Deep Neural network for regression

import tensorflow as tf
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

learning_rate = 1e-6
training_epochs = 15000

n_input = 1  # Number of features
n_output = 1  # Regression output is a number only

n_hidden_layer_1 = 30  # Hidden layer 1
n_hidden_layer_2 = 30  # Hidden layer 2

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

# tf Graph input
x = tf.placeholder("float32", [None, n_input])
y = tf.placeholder("float32", [None, n_output])

# Hidden and output layers definition (using TensorFlow mathematical functions)

# Hidden layer with activation
layer_1 = tf.add(tf.matmul(x, weights["hidden_layer_1"]), biases["hidden_layer_1"])
layer_1 = tf.sin(layer_1)

layer_2 = tf.add(
    tf.matmul(layer_1, weights["hidden_layer_2"]), biases["hidden_layer_2"]
)
layer_2 = tf.nn.relu(layer_2)

# Output layer with linear activation
ops = tf.add(tf.matmul(layer_2, weights["out"]), biases["out"])

# Define loss and optimizer
cost = tf.reduce_mean(tf.squared_difference(ops, y))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(
    cost
)

# TensorFlow Session for training and loss estimation

from tqdm import tqdm

# Initializing the variables
init = tf.global_variables_initializer()

# Empty lists for book-keeping purpose
epoch = 0
log_epoch = []
epoch_count = []
acc = []
loss_epoch = []
r2_DNN = []
test_size = []

for i in range(5):
    X_train, X_test, y_train, y_test = train_test_split(
        df["X"], df["y"], test_size=test_set_fraction
    )

    X_train = X_train.reshape(X_train.size, 1)
    y_train = y_train.reshape(y_train.size, 1)
    X_test = X_test.reshape(X_test.size, 1)
    y_test = y_test.reshape(y_test.size, 1)
    # Launch the graph and time the session
    with tf.Session() as sess:
        sess.run(init)
        # Loop over epochs
        for epoch in tqdm(range(training_epochs)):
            # Run optimization process (backprop) and cost function (to get loss value)
            # r1 = int(epoch/10000)
            # learning_rate = learning_rate-r1*3e-6
            # optimizer = tf.train.GradientDescentOptimizer(learning_rate=learning_rate).minimize(cost)
            _, l = sess.run([optimizer, cost], feed_dict={x: X_train, y: y_train})

        yhat = sess.run(ops, feed_dict={x: X_test})

    # test_size.append(0.5-(i*0.04))
    # Total variance
    SSt_DNN = np.sum(np.square(y_test - np.mean(y_test)))
    # Residual sum of squares
    SSr_DNN = np.sum(np.square(yhat - y_test))
    # Root-mean-square error
    RMSE_DNN = np.sqrt(np.sum(np.square(yhat - y_test)))
    # R^2 coefficient
    r2 = 1 - (SSr_DNN / SSt_DNN)
    r2_DNN.append(r2)
    print("Run: {} finished. Score: {}".format(i + 1, r2))


# Plot R2 score corss-validation results

plt.figure(figsize=(10, 6))
plt.title("\nR2-score for cross-validation runs of \ndeep (2-layer) neural network")
plt.xlabel("\nCross-validation run with random test/train split #")
plt.ylabel("R2 score (test set)")
plt.scatter([i + 1 for i in range(5)], r2_DNN, edgecolors="k", s=100, c="green")
plt.grid(True)
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
