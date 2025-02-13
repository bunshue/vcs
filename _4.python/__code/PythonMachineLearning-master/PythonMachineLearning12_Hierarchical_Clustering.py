"""
Hierarchical_Clustering

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

# Hierarchical Clustering

# Dendograms

# Clustering with a shopping trend data set

df = pd.read_csv("data/Mall_Customers.csv")
df.head(10)

df.describe()

plt.figure(figsize=(8, 5))
plt.title("Annual income distribution", fontsize=16)
plt.xlabel("Annual income (k$)", fontsize=14)
plt.grid(True)
plt.hist(df["Annual Income (k$)"], color="orange", edgecolor="k")
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Spending Score distribution", fontsize=16)
plt.xlabel("Spending Score (1-100)", fontsize=14)
plt.grid(True)
plt.hist(df["Spending Score (1-100)"], color="green", edgecolor="k")
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Annual Income and Spending Score correlation", fontsize=18)
plt.xlabel("Annual Income (k$)", fontsize=14)
plt.ylabel("Spending Score (1-100)", fontsize=14)
plt.grid(True)
plt.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    color="red",
    edgecolor="k",
    alpha=0.6,
    s=100,
)
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Age and Spending Score correlation", fontsize=18)
plt.xlabel("Age", fontsize=14)
plt.ylabel("Spending Score (1-100)", fontsize=14)
plt.grid(True)
plt.scatter(
    df["Age"],
    df["Spending Score (1-100)"],
    color="blue",
    edgecolor="k",
    alpha=0.6,
    s=100,
)
plt.show()

# Dendograms

X = df.iloc[:, [3, 4]].values

import scipy.cluster.hierarchy as sch

plt.figure(figsize=(15, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
# plt.grid(True)
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.show()

# Optimal number of clusters

plt.figure(figsize=(15, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.hlines(y=190, xmin=0, xmax=2000, lw=3, linestyles="--")
plt.text(x=900, y=220, s="Horizontal line crossing 5 vertical lines", fontsize=20)
# plt.grid(True)
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.show()

# Hierarchical Clustering

from sklearn.cluster import AgglomerativeClustering

# hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
hc = AgglomerativeClustering(n_clusters=5, linkage="ward")
y_hc = hc.fit_predict(X)

plt.figure(figsize=(12, 7))
plt.scatter(X[y_hc == 0, 0], X[y_hc == 0, 1], s=100, c="red", label="Careful")
plt.scatter(X[y_hc == 1, 0], X[y_hc == 1, 1], s=100, c="blue", label="Standard")
plt.scatter(X[y_hc == 2, 0], X[y_hc == 2, 1], s=100, c="green", label="Target group")
plt.scatter(X[y_hc == 3, 0], X[y_hc == 3, 1], s=100, c="orange", label="Careless")
plt.scatter(X[y_hc == 4, 0], X[y_hc == 4, 1], s=100, c="magenta", label="Sensible")
plt.title("Clustering of customers", fontsize=20)
plt.xlabel("Annual Income (k$)", fontsize=16)
plt.ylabel("Spending Score (1-100)", fontsize=16)
plt.legend(fontsize=16)
plt.grid(True)
plt.axhspan(ymin=60, ymax=100, xmin=0.4, xmax=0.96, alpha=0.3, color="yellow")
plt.show()

# Verifying the optimal number of clusters by k-means algorithm

from sklearn.cluster import KMeans

wcss = []
for i in range(1, 16):
    kmeans = KMeans(n_clusters=i, init="k-means++")
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

with plt.style.context(("fivethirtyeight")):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 16), wcss)
    plt.title("The Elbow Method with k-means++\n", fontsize=25)
    plt.xlabel("Number of clusters")
    plt.xticks(fontsize=20)
    plt.ylabel("WCSS (within-cluster sums of squares)")
    plt.vlines(x=5, ymin=0, ymax=250000, linestyles="--")
    plt.text(
        x=5.5,
        y=110000,
        s="5 clusters seem optimal choice \nfrom the elbow position",
        fontsize=25,
        fontdict={"family": "Times New Roman"},
    )
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
