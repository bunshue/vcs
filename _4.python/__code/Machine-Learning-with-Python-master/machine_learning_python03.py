"""
machine_learning_python03

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

# Mean-shift Clustering Technique

from sklearn.cluster import MeanShift
from sklearn import metrics

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.4, random_state=101
)

X.shape

# (300, 2)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

# Clustering

ms_model = MeanShift().fit(X)
cluster_centers = ms_model.cluster_centers_
labels = ms_model.labels_
n_clusters = len(cluster_centers)
labels = ms_model.labels_

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at:\n\n", cluster_centers)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=ms_model.labels_, s=75)
plt.grid(True)
plt.xticks()
plt.yticks()
show()

# Homogeneity

print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Homogeneity score: 0.940507302233

# Completeness

print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Completeness score: 0.940507302233

# Time complexity and model quality as the data size grows

from tqdm import tqdm

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_ms = []
homo_ms = []
complete_ms = []

for i in tqdm(n_samples):
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.4, random_state=101
    )
    t1 = time.time()
    ms_model = MeanShift().fit(X)
    t2 = time.time()
    t_ms.append(t2 - t1)
    homo_ms.append(metrics.homogeneity_score(labels_true, ms_model.labels_))
    complete_ms.append(metrics.completeness_score(labels_true, ms_model.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Mean Shift\n")
plt.scatter(n_samples, t_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size\n")
plt.scatter(n_samples, homo_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size\n")
plt.scatter(n_samples, complete_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_ms, "k--", lw=3)
plt.grid(True)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Completeness score")
show()

# How well the cluster detection works in the presence of noise?

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    ms_model = MeanShift().fit(X)
    n_clusters.append(len(ms_model.cluster_centers_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data\n")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks()
plt.ylabel("Number of clusters detected")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Principal Component Analysis (PCA)

df = pd.read_csv("./Datasets/wine.data.csv")
cc = df.head(10)
print(cc)

# Basic statistics

cc = df.iloc[:, 1:].describe()
print(cc)

# Boxplots by output labels/classes

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4))
    plt.title("{}\n".format(c))
    plt.xlabel("Wine Class")
    show()

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
plt.title("Scatter plot of two features showing the \ncorrelation and class seperation")
plt.xlabel("OD280/OD315 of diluted wines")
plt.ylabel("Flavanoids")
show()


def correlation_matrix(df):
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 12))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation\n")
    labels = df.columns
    ax1.set_xticklabels(labels)
    ax1.set_yticklabels(labels)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    show()


correlation_matrix(df)

# Principal Component Analysis
# Data scaling

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X = df.drop("Class", axis=1)
y = df["Class"]

X = scaler.fit_transform(X)

dfx = pd.DataFrame(data=X, columns=df.columns[1:])

cc = dfx.head(10)
print(cc)

cc = dfx.describe()
print(cc)

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
plt.title("Explained variance ratio of the \nfitted principal component vector\n")
plt.xlabel("Principal components")
plt.xticks([i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))])
plt.yticks()
plt.ylabel("Explained variance ratio")
show()

# Showing better class separation using principal components

dfx_trans = pca.transform(dfx)

# Put it in a data frame

dfx_trans = pd.DataFrame(data=dfx_trans)
cc = dfx_trans.head(10)
print(cc)

# Plot the first two columns of this transformed data set with the color set to original ground truth class label

plt.figure(figsize=(10, 6))
plt.scatter(
    dfx_trans[0], dfx_trans[1], c=df["Class"], edgecolors="k", alpha=0.75, s=150
)
plt.grid(True)
plt.title("Class separation using first two principal components\n")
plt.xlabel("Principal component-1")
plt.ylabel("Principal component-2")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Clustering metrics - alternatives to the elbow method

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs

n_features = 4
n_cluster = 5
cluster_std = 1.2
n_samples = 200

data1 = make_blobs(
    n_samples=n_samples,
    n_features=n_features,
    centers=n_cluster,
    cluster_std=cluster_std,
)

d1 = data1[0]

df1 = pd.DataFrame(
    data=d1, columns=["Feature_" + str(i) for i in range(1, n_features + 1)]
)
cc = df1.head()
print(cc)

from itertools import combinations

lst_vars = list(combinations(df1.columns, 2))

cc = len(lst_vars)
print(cc)

plt.figure(figsize=(15, 8))
for i in range(1, 7):
    plt.subplot(2, 3, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=data1[1], edgecolor="k", s=150)
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)
show()

# How are the classes separated (boxplots)

plt.figure(figsize=(16, 14))
for i, c in enumerate(df1.columns):
    plt.subplot(3, 2, i + 1)
    sns.boxplot(y=df1[c], x=data1[1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Class", fontsize=15)
    plt.ylabel(c, fontsize=15)
    # plt.show()
show()

# k-means clustering

from sklearn.cluster import KMeans

X = df1

cc = X.head()
print(cc)

y = data1[1]

# Scaling

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# Metrics

from sklearn.metrics import silhouette_score, davies_bouldin_score, v_measure_score

# Running k-means and computing inter-cluster distance score for various k values

km_scores = []
km_silhouette = []
vmeasure_score = []
db_score = []
for i in range(2, 12):
    km = KMeans(n_clusters=i, random_state=0).fit(X_scaled)
    preds = km.predict(X_scaled)

    print("Score for number of cluster(s) {}: {}".format(i, km.score(X_scaled)))
    km_scores.append(-km.score(X_scaled))

    silhouette = silhouette_score(X_scaled, preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))

    db = davies_bouldin_score(X_scaled, preds)
    db_score.append(db)
    print("Davies Bouldin score for number of cluster(s) {}: {}".format(i, db))

    v_measure = v_measure_score(y, preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i, v_measure))
    print("-" * 100)

plt.figure(figsize=(7, 4))
plt.title("The elbow method for determining number of clusters\n", fontsize=16)
plt.scatter(x=[i for i in range(2, 12)], y=km_scores, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Number of clusters", fontsize=14)
plt.ylabel("K-means score", fontsize=15)
plt.xticks([i for i in range(2, 12)], fontsize=14)
plt.yticks(fontsize=15)
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("V-measure score")
plt.show()

plt.figure(figsize=(7, 4))
plt.title(
    "The silhouette coefficient method \nfor determining number of clusters\n",
    fontsize=16,
)
plt.scatter(x=[i for i in range(2, 12)], y=km_silhouette, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Number of clusters", fontsize=14)
plt.ylabel("Silhouette score", fontsize=15)
plt.xticks([i for i in range(2, 12)], fontsize=14)
plt.yticks(fontsize=15)
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=db_score, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Davies-Bouldin score")
plt.show()

# Expectation-maximization (Gaussian Mixture Model)

from sklearn.mixture import GaussianMixture

gm_bic = []
gm_score = []
for i in range(2, 12):
    gm = GaussianMixture(n_components=i, n_init=10, tol=1e-3, max_iter=1000).fit(
        X_scaled
    )
    print("BIC for number of cluster(s) {}: {}".format(i, gm.bic(X_scaled)))
    print(
        "Log-likelihood score for number of cluster(s) {}: {}".format(
            i, gm.score(X_scaled)
        )
    )
    print("-" * 100)
    gm_bic.append(-gm.bic(X_scaled))
    gm_score.append(gm.score(X_scaled))

plt.figure(figsize=(7, 4))
plt.title(
    "The Gaussian Mixture model BIC \nfor determining number of clusters\n", fontsize=16
)
plt.scatter(x=[i for i in range(2, 12)], y=np.log(gm_bic), s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Number of clusters", fontsize=14)
plt.ylabel("Log of Gaussian mixture BIC score", fontsize=15)
plt.xticks([i for i in range(2, 12)], fontsize=14)
plt.yticks(fontsize=15)
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=gm_score, s=150, edgecolor="k")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Hierarchical Clustering

# Dendograms

# Clustering with a shopping trend data set

df = pd.read_csv("Datasets/Mall_Customers.csv")
cc = df.head(10)
print(cc)

cc = df.describe()
print(cc)

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

# So, is there a definitive correlation between annual income and spending score? - Apparently not

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

# How about correlation between age and spending score? - Apparently not

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

# Strategy

# Dendograms

X = df.iloc[:, [3, 4]].values

# Ward distance matrix

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

hc = AgglomerativeClustering(n_clusters=5, linkage="ward")
y_hc = hc.fit_predict(X)

# Plot the clusters and label customer types

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

# Affinity Propagation Clustering Technique

from sklearn.cluster import AffinityPropagation
from sklearn import metrics

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.5, random_state=0
)

X.shape

# (300, 2)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
plt.grid(True)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Clustering

# Compute Affinity Propagation
af_model = AffinityPropagation(preference=-50).fit(X)
cluster_centers_indices = af_model.cluster_centers_indices_
labels = af_model.labels_
n_clusters_ = len(cluster_centers_indices)

# Number of detected clusters and their centers

print("Number of clusters detected by the algorithm:", n_clusters_)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at:\n\n", X[cluster_centers_indices])

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=af_model.labels_, s=75)
plt.grid(True)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.show()

# Homogeneity

print("Homogeneity score:", metrics.homogeneity_score(labels_true, labels))

# Homogeneity score: 0.871559529839

# Completeness

print("Completeness score:", metrics.completeness_score(labels_true, labels))

# Completeness score: 0.871585975337

# Prediction

x_new = [0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

# New point (0.5,0.4) will belong to cluster 0

x_new = [-0.5, 0.4]
x_pred = af_model.predict([x_new])[0]

print("New point ({},{}) will belong to cluster {}".format(x_new[0], x_new[1], x_pred))

# New point (-0.5,0.4) will belong to cluster 2

# Time complexity and model quality as the data size grows

from tqdm import tqdm

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_aff = []
homo_aff = []
complete_aff = []

for i in tqdm(n_samples):
    X, labels_true = make_blobs(
        n_samples=i, centers=centers, cluster_std=0.5, random_state=0
    )
    t1 = time.time()
    af_model = AffinityPropagation(preference=-50, max_iter=50).fit(X)
    t2 = time.time()
    t_aff.append(t2 - t1)
    homo_aff.append(metrics.homogeneity_score(labels_true, af_model.labels_))
    complete_aff.append(metrics.completeness_score(labels_true, af_model.labels_))

plt.figure(figsize=(8, 5))
plt.title("Time complexity of Affinity Propagation\n", fontsize=20)
plt.scatter(n_samples, t_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_aff, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Time taken for model (sec)", fontsize=15)
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size\n", fontsize=20)
plt.scatter(n_samples, homo_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_aff, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Homogeneity score", fontsize=15)
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size\n", fontsize=20)
plt.scatter(n_samples, complete_aff, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_aff, "k--", lw=3)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Number of samples", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Completeness score", fontsize=15)
plt.show()

# How well the cluster detection works in the presence of noise? Can damping help?

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.5
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for low damping=0.5\n", fontsize=16)
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Noise std.dev", fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Number of clusters detected", fontsize=15)
plt.show()

# Detected number of clusters: [200, 67, 1, 68, 60, 3, 3, 3, 4, 4, 5, 6, 6, 7, 9, 9]

noise = [
    0.01,
    0.05,
    0.1,
    0.2,
    0.3,
    0.4,
    0.5,
    0.6,
    0.7,
    0.8,
    0.9,
    1.0,
    1.25,
    1.5,
    1.75,
    2.0,
]
n_clusters = []
for i in noise:
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(
        n_samples=200, centers=centers, cluster_std=i, random_state=101
    )
    af_model = AffinityPropagation(
        preference=-50, max_iter=500, convergence_iter=15, damping=0.9
    ).fit(X)
    n_clusters.append(len(af_model.cluster_centers_indices_))

print("Detected number of clusters:", n_clusters)
plt.figure(figsize=(8, 5))
plt.title("Cluster detection with noisy data for high damping=0.9\n", fontsize=16)
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.grid(True)
plt.xticks(fontsize=15)
plt.xlabel("Noise std.dev", fontsize=15)
plt.yticks([i for i in range(2, 10)], fontsize=15)
plt.ylabel("Number of clusters detected", fontsize=15)
plt.show()

# Detected number of clusters: [3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 6, 7]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# DBSCAN Clustering

from sklearn import cluster, datasets

n_samples = 1500
noisy_circles, circle_labels = datasets.make_circles(
    n_samples=n_samples, factor=0.5, noise=0.05
)
noisy_moons, moon_labels = datasets.make_moons(n_samples=n_samples, noise=0.1)

noisy_moons = np.array(noisy_moons)
noisy_circles = np.array(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1])
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1])
plt.show()

# Can k-means identify the right clusters?

km = cluster.KMeans(n_clusters=2)

km.fit(noisy_moons)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=km.labels_)
plt.show()

km.fit(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=km.labels_)
plt.show()

# How does DBSCAN perform?

dbs = cluster.DBSCAN(eps=0.1)

dbs.fit(noisy_moons)

plt.figure(figsize=(8, 5))
plt.title("Half-moon shaped data", fontsize=18)
plt.grid(True)
plt.scatter(noisy_moons[:, 0], noisy_moons[:, 1], c=dbs.labels_)
plt.show()

dbs.fit(noisy_circles)

plt.figure(figsize=(8, 5))
plt.title("Concentric circles of data points", fontsize=18)
plt.grid(True)
plt.scatter(noisy_circles[:, 0], noisy_circles[:, 1], c=dbs.labels_)
plt.show()

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
