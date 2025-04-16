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

# Random Forest Regression

from sklearn.datasets import make_regression

# What is make_regression method?

n_samples = 100  # Number of samples
n_features = 6  # Number of features
n_informative = (
    3  # Number of informative features i.e. actual features which influence the output
)

X, y, coef = make_regression(
    n_samples=n_samples,
    n_features=n_features,
    n_informative=n_informative,
    random_state=None,
    shuffle=False,
    noise=20,
    coef=True,
)

# Make a data frame and create basic visualizations

df1 = pd.DataFrame(data=X, columns=["X" + str(i) for i in range(1, n_features + 1)])
df2 = pd.DataFrame(data=y, columns=["y"])
df = pd.concat([df1, df2], axis=1)
df.head(10)

# Scatter plots

with plt.style.context(("seaborn-dark")):
    for i, col in enumerate(df.columns[:-1]):
        plt.figure(figsize=(6, 4))
        plt.grid(True)
        plt.xlabel("Feature:" + col, fontsize=12)
        plt.ylabel("Output: y", fontsize=12)
        plt.scatter(df[col], df["y"], c="red", s=50, alpha=0.6)
        show()

# Histograms of the feature space

with plt.style.context(("fivethirtyeight")):
    for i, col in enumerate(df.columns[:-1]):
        plt.figure(figsize=(6, 4))
        plt.grid(True)
        plt.xlabel("Feature:" + col, fontsize=12)
        plt.ylabel("Output: y", fontsize=12)
        plt.hist(df[col], alpha=0.6, facecolor="g")
        show()

# How will a Decision Tree regressor do?

from sklearn import tree

tree_model = tree.DecisionTreeRegressor(max_depth=5, random_state=None)
tree_model.fit(X, y)

print("Relative importance of the features: ", tree_model.feature_importances_)
with plt.style.context("dark_background"):
    plt.figure(figsize=(10, 7))
    plt.grid(True)
    plt.yticks(range(n_features + 1, 1, -1), df.columns[:-1], fontsize=20)
    plt.xlabel("Relative (normalized) importance of parameters", fontsize=15)
    plt.ylabel("Features\n", fontsize=20)
    plt.barh(
        range(n_features + 1, 1, -1), width=tree_model.feature_importances_, height=0.5
    )
    show()

# Relative importance of the features:  [ 0.06896493  0.35741588  0.54578154  0.0230699   0.          0.00476775]

print("Regression coefficient:", tree_model.score(X, y))

# Regression coefficient: 0.95695111153

# Random Forest Regressor

from sklearn.ensemble import RandomForestRegressor

# 隨機森林演算法, 用 sklearn 裡的 RandomForestRegressor 來做隨機森林演算法
# 使用 100 棵 決策樹

# model = RandomForestRegressor(max_depth=5, random_state=None,max_features='auto',max_leaf_nodes=5,n_estimators=100)
model = RandomForestRegressor(n_estimators=100, random_state=9487)  # 隨機森林函數學習機

model.fit(X, y)

# Print the relative importance of the features

print("Relative importance of the features: ", model.feature_importances_)
with plt.style.context("dark_background"):
    plt.figure(figsize=(10, 7))
    plt.grid(True)
    plt.yticks(range(n_features + 1, 1, -1), df.columns[:-1], fontsize=20)
    plt.xlabel("Relative (normalized) importance of parameters", fontsize=15)
    plt.ylabel("Features\n", fontsize=20)
    plt.barh(range(n_features + 1, 1, -1), width=model.feature_importances_, height=0.5)
    show()

# Relative importance of the features:  [ 0.03456204  0.46959355  0.49500136  0.          0.          0.00084305]

print("Regression coefficient:", model.score(X, y))

# Regression coefficient: 0.811794737752

# Benchmark to statsmodel (ordinary least-square solution by exact analytic method)

import statsmodels.api as sm

Xs = sm.add_constant(X)
stat_model = sm.OLS(y, Xs)
stat_result = stat_model.fit()

print("檢視模型架構")
stat_result.summary()  # 檢視模型架構

# Make arrays of regression coefficients estimated by the models

rf_coef = np.array(coef)
stat_coef = np.array(stat_result.params[1:])

df_coef = pd.DataFrame(
    data=[rf_coef, stat_coef],
    columns=df.columns[:-1],
    index=["True Regressors", "OLS method estimation"],
)
df_coef

# Show the relative importance of regressors side by side

df_importance = pd.DataFrame(
    data=[
        model.feature_importances_,
        stat_result.tvalues[1:] / sum(stat_result.tvalues[1:]),
    ],
    columns=df.columns[:-1],
    index=["RF Regressor relative importance", "OLS method normalized t-statistic"],
)
df_importance

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
