"""
Stochastic_grad_descent

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

# Classification using Stochastic Gradient Descent

# Stochastic gradient descent (SGD)

from sklearn.datasets import make_classification
from time import time
from sklearn.linear_model import SGDClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Train using various classifiers with increasing training set size

# SGDClassifier: Using hinge loss (support vector machine loss)

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
hinge_acc = []
hinge_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    hinge_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    hinge_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# SGDClassifier: Using log loss (logistic regression)

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
log_acc = []
log_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    log_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    log_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# SGDClassifier: Using perceptron loss/algorithm

sgd_class = SGDClassifier(
    alpha=0.001,
    loss="hinge",
    max_iter=100,
    tol=0.001,
    n_jobs=-1,
    early_stopping=True,
    n_iter_no_change=2,
)
perceptron_acc = []
perceptron_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    sgd_class.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    perceptron_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, sgd_class.predict(X_test))
    perceptron_acc.append(acc)
    print("Accuracy on the test set:", round(acc, 3))
    print()

# Random Forest classifier

rf = RandomForestClassifier(
    n_estimators=20, max_depth=5, min_samples_leaf=5, min_samples_split=10, n_jobs=-1
)
rf_acc = []
rf_time = []
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
for size in [int(10 ** (0.2 * i)) for i in range(15, 31)]:
    prob = make_classification(
        n_samples=size,
        n_features=50,
        n_informative=45,
        n_classes=2,
        class_sep=0.75,
        random_state=101,
    )
    X, y = prob
    X = scaler.fit_transform(X)
    print("Size of the problem: ", X.shape)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )
    t1 = time()
    rf.fit(X_train, y_train)
    t2 = time()
    t_delta = round(1e3 * (t2 - t1), 3)
    rf_time.append(t_delta)
    print(f"Took {t_delta} milliseconds")
    acc = accuracy_score(y_test, rf.predict(X_test))
    rf_acc.append(acc)
    print("Accuracy:", round(acc, 3))
    print()

# Plot


def plot_var(var, var_name):
    size = np.array([int(10 ** (0.2 * i)) for i in range(15, 31)])
    plt.figure(figsize=(8, 5))
    plt.title(f"{var_name} with training set size", fontsize=18)
    plt.semilogx(size * 0.7, var, marker="o", color="k", lw=3, markersize=12)
    plt.grid(True)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Training set size", fontsize=15)
    plt.ylabel("Training time (milliseconds)", fontsize=15)
    # show()


plot_var(hinge_time, "Hinge loss time")
plot_var(log_time, "Logistic loss time")
plot_var(perceptron_time, "Perceptron algorithm time")
plot_var(rf_time, "Random Forest time")
show()

plot_var(hinge_acc, "Hinge loss accuracy")
plot_var(log_acc, "Logistic loss accuracy")
plot_var(perceptron_acc, "Perceptron algorithm accuracy")
plot_var(rf_acc, "Random Forest accuracy")
show()

# Observation
# While achieving similar accuracy level, the SGDClassifier estimator variants demonstrate faster training time as compared to the Random Forest classifier. The difference is not that significant at the low end of the training set size (< 100,000). But the difference becomes prominent for larger training set size.

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
