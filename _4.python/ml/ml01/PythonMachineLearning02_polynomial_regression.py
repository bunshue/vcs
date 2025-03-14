"""
PythonMachineLearning-master 01

Regularized polynomial regression with linear and random sampling

Ridge/LASSO polynomial regression with linear and random sampling
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
df.head()

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
plt.show()

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
plt.show()

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
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn.pipeline import make_pipeline

X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.33)
X_train = X_train.values.reshape(-1, 1)
X_test = X_test.values.reshape(-1, 1)

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
    # plt.title("RMSE: {}".format(RMSE),fontsize=10)
    # plt.suptitle("Polynomial of degree {}".format(degree),fontsize=15)
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title(
        "Predicted vs. actual for polynomial of degree {}".format(degree), fontsize=15
    )
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)

# Test score of model with degree 2: -0.04323708983722585
# Test score of model with degree 3: -0.04323708983722607
# Test score of model with degree 4: 0.09365803380879467
# Test score of model with degree 5: 0.2942094903725706
# Test score of model with degree 6: 0.5078727869614987
# Test score of model with degree 7: 0.6519272435828123
# Test score of model with degree 8: 0.6929923646710744

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
    # plt.title("RMSE: {}".format(RMSE),fontsize=10)
    # plt.suptitle("Polynomial of degree {}".format(degree),fontsize=15)
    # plt.xlabel("X training values")
    # plt.ylabel("Fitted and training values")
    # plt.scatter(X_train,y_pred)
    # plt.scatter(X_train,y_train)

    plt.figure()
    plt.title(
        "Predicted vs. actual for polynomial of degree {}".format(degree), fontsize=15
    )
    plt.xlabel("Actual values")
    plt.ylabel("Predicted values")
    plt.scatter(y_test, test_pred)
    plt.plot(y_test, y_test, "r", lw=2)
"""
Test score of model with degree 2: -0.12434801463459723
Test score of model with degree 3: -0.0769230959117706
Test score of model with degree 4: 0.6735234335237947
Test score of model with degree 5: 0.7969653226807432
Test score of model with degree 6: 0.8321225592878035
Test score of model with degree 7: 0.8124366657216142
Test score of model with degree 8: 0.7813750489160156
"""
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
plt.xlabel("Model Complexity: Degree of polynomial", fontsize=20)
plt.ylabel("Model Score: R^2 score on test set", fontsize=15)
plt.legend(fontsize=15)

plt.show()

# Checking the regularization strength from the cross-validated model pipeline

m = model.steps[1][1]
print(m.alpha_)

# 0.021486111550969477


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
