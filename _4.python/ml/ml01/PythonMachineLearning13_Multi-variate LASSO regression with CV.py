"""
Multi-variate LASSO regression with CV

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

# Multi-variate Rregression Metamodel with DOE based on random sampling

# Generate random (equivalent to Latin Hypercube sampling done in Optislang) feature vectors

X = np.array(10 * np.random.randn(37, 5))

df = pd.DataFrame(X, columns=["Feature" + str(l) for l in range(1, 6)])

cc = df.head()
print(cc)

# Plot the random distributions of input features

for i in df.columns:
    df.hist(i, bins=5, xlabelsize=15, ylabelsize=15, figsize=(8, 6))
show()


df["y"] = (
    5 * df["Feature1"] ** 2
    + 13 * df["Feature2"]
    + 0.1 * df["Feature3"] ** 2 * df["Feature1"]
    + 2 * df["Feature4"] * df["Feature5"]
    + 0.1 * df["Feature5"] ** 3
    + 0.8 * df["Feature1"] * df["Feature4"] * df["Feature5"]
    + 30 * np.random.normal(loc=5, scale=2)
)

cc = df.head()
print(cc)

# Plot single-variable scatterplots

for i in df.columns:
    df.plot.scatter(i, "y", edgecolors=(0, 0, 0), s=50, c="g", grid=True)
show()

# Standard linear regression

linear_model = sklearn.linear_model.LinearRegression()  # 函數學習機

X_linear = df.drop("y", axis=1)
y_linear = df["y"]

linear_model.fit(X_linear, y_linear)

y_pred_linear = linear_model.predict(X_linear)

# R-square of simple linear fit is very bad, coefficients have no meaning i.e. we did not 'learn' the function

RMSE_linear = np.sqrt(np.sum(np.square(y_pred_linear - y_linear)))

print("Root-mean-square error of linear model:", RMSE_linear)

# Root-mean-square error of linear model: 4838.87696595

coeff_linear = pd.DataFrame(
    linear_model.coef_,
    index=df.drop("y", axis=1).columns,
    columns=["Linear model coefficients"],
)
print(coeff_linear)

print("R2 value of linear model:", linear_model.score(X_linear, y_linear))

# R2 value of linear model: 0.347548929728

plt.figure(figsize=(12, 8))
plt.xlabel("Predicted value with linear fit", fontsize=20)
plt.ylabel("Actual y-values", fontsize=20)
plt.grid(1)
plt.scatter(y_pred_linear, y_linear, edgecolors=(0, 0, 0), lw=2, s=80)
plt.plot(y_pred_linear, y_pred_linear, "k--", lw=2)
show()

# Create polynomial features

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(3, include_bias=False)

X_poly = poly.fit_transform(X)
X_poly_feature_name = poly.get_feature_names_out(
    ["Feature" + str(l) for l in range(1, 6)]
)
print(X_poly_feature_name)
print(len(X_poly_feature_name))

df_poly = pd.DataFrame(X_poly, columns=X_poly_feature_name)
cc = df_poly.head()
print(cc)

df_poly["y"] = df["y"]
cc = df_poly.head()
print(cc)

X_train = df_poly.drop("y", axis=1)
y_train = df_poly["y"]

# Polynomial model without regularization and cross-validation

poly = sklearn.linear_model.LinearRegression()  # 函數學習機

model_poly = poly.fit(X_train, y_train)
y_poly = poly.predict(X_train)
RMSE_poly = np.sqrt(np.sum(np.square(y_poly - y_train)))
print("Root-mean-square error of simple polynomial model:", RMSE_poly)

# Root-mean-square error of simple polynomial model: 1.89910302223e-11

coeff_poly = pd.DataFrame(
    model_poly.coef_,
    index=df_poly.drop("y", axis=1).columns,
    columns=["Coefficients polynomial model"],
)
print(coeff_poly)

print("R2 value of simple polynomial model:", model_poly.score(X_train, y_train))

# R2 value of simple polynomial model: 1.0

# Metamodel (Optislang style :) - polynomial model with cross-validation and LASSO regularization

from sklearn.linear_model import LassoCV

model1 = LassoCV(cv=10, verbose=0, eps=0.001, n_alphas=100, tol=0.0001, max_iter=5000)

model1.fit(X_train, y_train)

y_pred1 = np.array(model1.predict(X_train))

RMSE_1 = np.sqrt(np.sum(np.square(y_pred1 - y_train)))
print("Root-mean-square error of Metamodel:", RMSE_1)

# Root-mean-square error of Metamodel: 10.6254345131

coeff1 = pd.DataFrame(
    model1.coef_,
    index=df_poly.drop("y", axis=1).columns,
    columns=["Coefficients Metamodel"],
)
print(coeff1)

cc = model1.score(X_train, y_train)
print(cc)

# 0.99999685404731742

print(model1.alpha_)

# 0.11791796322572394

# Printing only the non-zero coefficients of the metamodel

cc = coeff1[coeff1["Coefficients Metamodel"] != 0]
print(cc)

plt.figure(figsize=(12, 8))
plt.xlabel("Predicted value with Metamodel", fontsize=20)
plt.ylabel("Actual y-values", fontsize=20)
plt.grid(1)
plt.scatter(y_pred1, y_train, edgecolors=(0, 0, 0), lw=2, s=80)
plt.plot(y_pred1, y_pred1, "k--", lw=2)
show()

# Display results
m_log_alphas = -np.log10(model1.alphas_)

plt.figure()
ymin, ymax = 2300, 3800
plt.plot(m_log_alphas, model1.mse_path_, ":")
plt.plot(
    m_log_alphas,
    model1.mse_path_.mean(axis=-1),
    "k",
    label="Average across the folds",
    linewidth=2,
)
plt.axvline(
    -np.log10(model1.alpha_), linestyle="--", color="k", label="alpha: CV estimate"
)
plt.legend()

plt.xlabel("-log(alpha)")
plt.ylabel("Mean square error")
plt.axis("tight")
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
