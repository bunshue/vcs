"""
Principal Component Analysis (PCA)


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

# Principal Component Analysis (PCA)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/wine.data.csv")
df.head(10)

# df.iloc[:,1:].describe()

# Boxplots by output labels/classes

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4), fontsize=14)
    plt.title("{}\n".format(c), fontsize=16)
    plt.xlabel("Wine Class", fontsize=16)
    plt.show()


plt.figure(figsize=(10, 6))
plt.scatter(
    df["OD280/OD315 of diluted wines"],
    df["Flavanoids"],
    c=df["Class"],
    edgecolors="k",
    alpha=0.75,
    s=150,
)
plt.grid(True)
plt.title(
    "Scatter plot of two features showing the \ncorrelation and class seperation",
    fontsize=15,
)
plt.xlabel("OD280/OD315 of diluted wines", fontsize=15)
plt.ylabel("Flavanoids", fontsize=15)
plt.show()

# Are the features independent? Plot co-variance matrix


def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation\n", fontsize=15)
    labels = df.columns
    ax1.set_xticklabels(labels, fontsize=9)
    ax1.set_yticklabels(labels, fontsize=9)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    plt.show()


cc = correlation_matrix(df)
print(cc)

# Principal Component Analysis
# Data scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X = df.drop("Class", axis=1)
y = df["Class"]

X = scaler.fit_transform(X)

dfx = pd.DataFrame(data=X, columns=df.columns[1:])

dfx.head(10)

dfx.describe()

# PCA class import and analysis

from sklearn.decomposition import PCA

pca = PCA(n_components=None)

dfx_pca = pca.fit(dfx)

# Plot the explained variance ratio

plt.figure(figsize=(10, 6))
plt.scatter(
    x=[i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))],
    y=dfx_pca.explained_variance_ratio_,
    s=200,
    alpha=0.75,
    c="orange",
    edgecolor="k",
)
plt.grid(True)
plt.title(
    "Explained variance ratio of the \nfitted principal component vector\n", fontsize=25
)
plt.xlabel("Principal components", fontsize=15)
plt.xticks([i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))], fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Explained variance ratio", fontsize=15)
plt.show()


dfx_trans = pca.transform(dfx)

# Put it in a data frame

dfx_trans = pd.DataFrame(data=dfx_trans)
dfx_trans.head(10)


plt.figure(figsize=(10, 6))
plt.scatter(
    dfx_trans[0], dfx_trans[1], c=df["Class"], edgecolors="k", alpha=0.75, s=150
)
plt.grid(True)
plt.title("Class separation using first two principal components\n", fontsize=20)
plt.xlabel("Principal component-1", fontsize=15)
plt.ylabel("Principal component-2", fontsize=15)
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
