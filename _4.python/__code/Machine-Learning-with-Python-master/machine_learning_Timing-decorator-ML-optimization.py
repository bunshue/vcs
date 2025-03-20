"""
Timing-decorator-ML-optimization

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

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Timing-decorator-ML-optimization

from functools import wraps
from time import time, sleep
import numpy as np, matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification, make_regression
from sklearn.model_selection import train_test_split

# Timing decorator with functools.wraps


def timing(func):
    @wraps(func)
    def wrap(*args, **kw):
        ts = time()
        result = func(*args, **kw)
        te = time()
        tdelta = round(1000 * (te - ts), 3)
        print(f"Function '{func.__name__}' took {tdelta} milliseconds to run")
        return result

    return wrap


@timing
def list_length(a):
    if isinstance(a, list):
        sleep(0.1)
        s = len(a)
        return s
    else:
        print("Argument is not a list")


list_length([1, 2, 3])


list_length(5)


def time_return(func):
    @wraps(func)
    def wrap(*args, **kw):
        ts = time()
        result = func(*args, **kw)
        te = time()
        tdelta = round(1000 * (te - ts), 3)
        return tdelta

    return wrap


@time_return
def numpy_matmul(a, b):
    return np.matmul(a, b)


SIZE = 1000
a = np.random.beta(1.0, 2.0, size=(SIZE, SIZE))
b = np.random.beta(1.0, 2.0, size=(SIZE, SIZE))
numpy_matmul(a, b)

# 16.48

SIZE = 2000
a = np.random.beta(1.0, 2.0, size=(SIZE, SIZE))
b = np.random.beta(1.0, 2.0, size=(SIZE, SIZE))
numpy_matmul(a, b)

# 111.301

SIZE = [500, 1000, 2000, 3000, 4000, 5000]
for s in SIZE:
    a = np.random.beta(1.0, 2.0, size=(s, s))
    b = np.random.beta(1.0, 2.0, size=(s, s))
    t = numpy_matmul(a, b)
    print(f"Matrix multiplication of size ({s}x{s}) took {t} milliseconds")

# Throwing an ML estimator into the mix


def time_estimator(func):
    @wraps(func)
    def wrap(*args, **kw):
        ts = time()
        result = func(*args, **kw)
        te = time()
        tdelta = round(1000 * (te - ts), 3)
        return (tdelta, result)

    return wrap


@time_estimator
def classifier_accuracy(estimator, x, y):
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.33, random_state=42
    )
    estimator.fit(X_train, y_train)
    score = estimator.score(X_test, y_test)
    return round(score, 3)


data = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=20,
    n_redundant=0,
    flip_y=0.05,
    class_sep=1.5,
)
x, y = data[0], data[1]

log_model = LogisticRegressionCV()

classifier_accuracy(log_model, x, y)

# (312.083, 0.836)

# Change the data and record execution time

SIZE = [1000 + 500 * i for i in range(21)]
log_model = LogisticRegressionCV()
model_time, model_acc = [], []

for s in SIZE:
    data = make_classification(
        n_samples=s,
        n_features=20,
        n_informative=20,
        n_redundant=0,
        flip_y=0.05,
        class_sep=1.5,
    )
    x, y = data[0], data[1]
    m_time, m_acc = classifier_accuracy(log_model, x, y)
    model_time.append(m_time)
    model_acc.append(m_acc)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(SIZE, model_acc, edgecolor="k", s=100)
ax[0].plot(SIZE, model_acc)
ax[0].set_title("Accuracy score with data size", fontsize=15)
ax[0].set_xlabel("Data size", fontsize=14)
ax[0].grid(True)
ax[1].scatter(SIZE, model_time, edgecolor="k", s=100)
ax[1].plot(SIZE, model_time)
ax[1].set_title("Training time (msec) with data size", fontsize=15)
ax[1].set_xlabel("Data size", fontsize=14)
ax[1].grid(True)
plt.show()

# Change the model and optimize

num_trees = [5 * x for x in range(1, 21)]
model_time, model_acc = [], []
data = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=20,
    n_redundant=0,
    flip_y=0.05,
    class_sep=1.0,
)
x, y = data[0], data[1]
for n in num_trees:
    rf_model = RandomForestClassifier(n_estimators=n)
    m_time, m_acc = classifier_accuracy(rf_model, x, y)
    model_time.append(m_time)
    model_acc.append(m_acc)

fig, ax = plt.subplots(1, 2, figsize=(12, 4))
ax[0].scatter(num_trees, model_acc, edgecolor="k", s=100)
ax[0].plot(num_trees, model_acc)
ax[0].set_title("Accuracy score with Random Forest", fontsize=15)
ax[0].set_xlabel("Number of trees", fontsize=14)
ax[0].grid(True)
ax[1].scatter(num_trees, model_time, edgecolor="k", s=100)
ax[1].plot(num_trees, model_time)
ax[1].set_title("Training time (msec) with Random Forest", fontsize=15)
ax[1].set_xlabel("Number of trees", fontsize=14)
ax[1].grid(True)
plt.show()

model_time = np.array(model_time)
model_acc = np.array(model_acc)
model_opt = model_acc + 1 / model_time

plt.figure(dpi=120)
plt.title("Model optimization with number of trees", fontsize=15)
plt.plot(num_trees, model_opt)
plt.scatter(num_trees, model_opt, s=100, edgecolor="k")
plt.xlabel("Number of trees", fontsize=14)
plt.grid(True)
plt.show()

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
