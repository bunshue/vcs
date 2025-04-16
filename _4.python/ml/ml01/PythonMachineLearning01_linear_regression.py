"""
PythonMachineLearning-master 01

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
import statsmodels.api as sm
from sklearn import tree
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from matplotlib.colors import ListedColormap
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from scipy import stats
from scipy import optimize


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Interactive Machine Learning Demo

from ipywidgets import interact, interactive, IntSlider, Layout, interact_manual
import ipywidgets as widgets
from IPython.display import display

# Linear Regression and Regularization

N_samples = 25
x_min = -5
x_max = 5
x1 = np.linspace(x_min, x_max, N_samples * 5)
x = np.random.choice(x1, size=N_samples)
noise_std = 1
noise_mean = 0
noise_magnitude = 2

# Function definitions (ideal fitting function and actual data generating function with noise)


def func_gen(N_samples, x_min, x_max, noise_magnitude, noise_sd, noise_mean):
    x1 = np.linspace(x_min, x_max, N_samples * 5)
    x = np.random.choice(x1, size=N_samples)
    y = 2 * x - 0.6 * x**2 + 0.2 * x**3 + 18 * np.sin(x)
    y1 = 2 * x1 - 0.6 * x1**2 + 0.2 * x1**3 + 18 * np.sin(x1)
    y = y + noise_magnitude * np.random.normal(
        loc=noise_mean, scale=noise_sd, size=N_samples
    )
    plt.figure(figsize=(8, 5))
    plt.plot(x1, y1, c="k", lw=2)
    plt.scatter(x, y, edgecolors="k", c="yellow", s=60)
    plt.grid(True)
    show()
    return (x, y, x1, y1)


# Call the 'interactive' widget with the data generating function, which also plots the data real-time

p = interactive(
    func_gen,
    N_samples={"Low (50 samples)": 50, "High (200 samples)": 200},
    x_min=(-5, 0, 1),
    x_max=(0, 5, 1),
    noise_magnitude=(0, 5, 1),
    noise_sd=(0.1, 1, 0.1),
    noise_mean=(-2, 2, 0.5),
)
display(p)

# Extract the data

# NG x,y,x1,y1 = p.result

lasso_eps = 0.01
lasso_nalpha = 20
lasso_iter = 3000
ridge_alphas = (0.001, 0.01, 0.1, 1)


def func_fit(model_type, test_size, degree):
    # 資料分割
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

    t1 = np.min(X_test)
    t2 = np.max(X_test)
    t3 = np.min(y_test)
    t4 = np.max(y_test)

    t5 = np.min(X_train)
    t6 = np.max(X_train)
    t7 = np.min(y_train)
    t8 = np.max(y_train)

    posx_test = t1 + (t2 - t1) * 0.7
    posx_train = t5 + (t6 - t5) * 0.7
    posy_test = t3 + (t4 - t3) * 0.2
    posy_train = t7 + (t8 - t7) * 0.2

    if model_type == "Linear regression":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            LinearRegression(normalize=True),
        )
    if model_type == "LASSO with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            LassoCV(
                eps=lasso_eps,
                n_alphas=lasso_nalpha,
                max_iter=lasso_iter,
                normalize=True,
                cv=5,
            ),
        )

    if model_type == "Ridge with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            RidgeCV(alphas=ridge_alphas, normalize=True, cv=5),
        )

    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    model.fit(X_train, y_train)

    train_pred = np.array(model.predict(X_train))
    train_score = model.score(X_train, y_train)

    test_pred = np.array(model.predict(X_test))
    test_score = model.score(X_test, y_test)

    RMSE_test = np.sqrt(np.mean(np.square(test_pred - y_test)))
    RMSE_train = np.sqrt(np.mean(np.square(train_pred - y_train)))

    print("Test score: {}, Training score: {}".format(test_score, train_score))

    print("RMSE Test: {}, RMSE train: {}".format(RMSE_test, RMSE_train))

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.title("Test set performance\n", fontsize=16)
    plt.xlabel("X-test", fontsize=13)
    plt.ylabel("y-test", fontsize=13)
    plt.scatter(X_test, y_test, edgecolors="k", c="blue", s=60)
    plt.scatter(X_test, test_pred, edgecolors="k", c="yellow", s=60)
    plt.grid(True)
    plt.legend(["Actual test values", "Predicted values"])
    plt.text(x=posx_test, y=posy_test, s="Test score: %.3f" % (test_score), fontsize=15)

    plt.subplot(1, 2, 2)
    plt.title("Training set performance\n", fontsize=16)
    plt.xlabel("X-train", fontsize=13)
    plt.ylabel("y-train", fontsize=13)
    plt.scatter(X_train, y_train, c="blue")
    plt.scatter(X_train, train_pred, c="yellow")
    plt.grid(True)
    plt.legend(["Actual training values", "Fitted values"])
    plt.text(
        x=posx_train,
        y=posy_train,
        s="Training score: %.3f" % (train_score),
        fontsize=15,
    )

    show()

    return (train_score, test_score)


# Run the encapsulated ML function with ipywidget interactive

style = {"description_width": "initial"}
# Continuous_update = False for IntSlider control to stop continuous model evaluation while the slider is being dragged
m = interactive(
    func_fit,
    model_type=widgets.RadioButtons(
        options=["Linear regression", "LASSO with CV", "Ridge with CV"],
        description="Choose Model",
        style=style,
        layout=Layout(width="250px"),
    ),
    test_size=widgets.Dropdown(
        options={
            "10% of data": 0.1,
            "20% of data": 0.2,
            "30% of data": 0.3,
            "40% of data": 0.4,
            "50% of data": 0.5,
        },
        description="Test set size",
        style=style,
    ),
    degree=widgets.IntSlider(
        min=1,
        max=10,
        step=1,
        description="Polynomial degree",
        stye=style,
        continuous_update=False,
    ),
)

# Set the height of the control.children[-1] so that the output does not jump and flicker
output = m.children[-1]
output.layout.height = "350px"

# Display the control
display(m)

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
