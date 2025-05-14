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
from sklearn.datasets import make_regression
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.metrics import adjusted_rand_score
from sklearn.metrics import completeness_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import v_measure_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LogisticRegressionCV
from sklearn.linear_model import HuberRegressor
from sklearn.cluster import KMeans  # k-means clustering
from sklearn.tree import DecisionTreeClassifier
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵
from matplotlib.colors import ListedColormap
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler  # Scaling
from sklearn import tree


def show():
    plt.show()
    pass


RATIO = 10

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear Regression and Regularization

N_samples = 25
x_min = -5
x_max = 5
x1 = np.linspace(x_min, x_max, N_samples * 5)
x = np.random.choice(x1, size=N_samples)
noise_std = 1
noise_mean = 0
noise_magnitude = 2

x1 = np.linspace(x_min, x_max, N_samples * 5)
x = np.random.choice(x1, size=N_samples)
y = 2 * x - 0.6 * x**2 + 0.2 * x**3 + 18 * np.sin(x)
y1 = 2 * x1 - 0.6 * x1**2 + 0.2 * x1**3 + 18 * np.sin(x1)
y = y + noise_magnitude * np.random.normal(
    loc=noise_mean, scale=noise_std, size=N_samples
)
plt.figure(figsize=(8, 5))
plt.plot(x1, y1, c="k", lw=2)
plt.scatter(x, y, edgecolors="k", c="yellow", s=60)
plt.grid(True)

show()

# return (x,y,x1,y1)

# Extract the data

# x,y,x1,y1 = p.result

from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# Machine learning (regression) model encapsulated within a function

lasso_eps = 0.01
lasso_nalpha = 20
lasso_iter = 3000
ridge_alphas = (0.001, 0.01, 0.1, 1)


def func_fit(model_type, test_size, degree):
    print("model_type :", model_type)
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
            PolynomialFeatures(degree, interaction_only=False), LinearRegression()
        )
    if model_type == "LASSO with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            LassoCV(eps=lasso_eps, n_alphas=lasso_nalpha, max_iter=lasso_iter, cv=5),
        )

    if model_type == "Ridge with CV":
        model = make_pipeline(
            PolynomialFeatures(degree, interaction_only=False),
            RidgeCV(alphas=ridge_alphas, cv=5),
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

    plt.subplot(121)
    plt.title("Test set performance")
    plt.xlabel("X-test")
    plt.ylabel("y-test")
    plt.scatter(X_test, y_test, edgecolors="k", c="blue", s=60)
    plt.scatter(X_test, test_pred, edgecolors="k", c="yellow", s=60)
    plt.grid(True)
    plt.legend(["Actual test values", "Predicted values"])
    plt.text(x=posx_test, y=posy_test, s="Test score: %.3f" % (test_score))

    plt.subplot(122)
    plt.title("Training set performance")
    plt.xlabel("X-train")
    plt.ylabel("y-train")
    plt.scatter(X_train, y_train, c="blue")
    plt.scatter(X_train, train_pred, c="yellow")
    plt.grid(True)
    plt.legend(["Actual training values", "Fitted values"])
    plt.text(x=posx_train, y=posy_train, s="Training score: %.3f" % (train_score))

    show()

    return (train_score, test_score)


test_size = 0.2
degree = 3

model_type = "Linear regression"
func_fit(model_type, test_size, degree)

model_type = "LASSO with CV"
func_fit(model_type, test_size, degree)

model_type = "Ridge with CV"
func_fit(model_type, test_size, degree)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

n_features = 8
n_cluster = 5
cluster_std = 1.5
n_samples = 1000

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

plt.figure(figsize=(16, 8))
for i in range(1, 29):
    print("i =", i)
    plt.subplot(7, 4, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=data1[1], edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)

show()

print("------------------------------")  # 30個

cc = df1.describe().transpose()
print(cc)

# How are the classes separated (boxplots)
plt.figure(figsize=(16, 8))

for i, c in enumerate(df1.columns):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df1[c], x=data1[1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Class", fontsize=15)
    plt.ylabel(c, fontsize=15)

show()

print("------------------------------")  # 30個

X = df1
# cc = X.head()
# print(cc)

y = data1[1]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("------------------------------")  # 30個

# Running k-means and computing inter-cluster distance score for various *k* values

km_scores = []
km_silhouette = []
vmeasure_score = []
for i in range(2, 12):
    print("i =", i)
    km = KMeans(n_clusters=i, random_state=0).fit(X_scaled)
    preds = km.predict(X_scaled)
    print("Score for number of cluster(s) {}: {}".format(i, km.score(X_scaled)))
    km_scores.append(-km.score(X_scaled))
    silhouette = silhouette_score(X_scaled, preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))
    v_measure = v_measure_score(y, preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i, v_measure))
    print("-" * 100)

plt.scatter(x=[i for i in range(2, 12)], y=km_scores, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("K-means score")
show()

print("------------------------------")  # 30個

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("V-measure score")
show()

print("------------------------------")  # 30個

km = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_scaled)
preds_km = km.predict(X_scaled)

plt.figure(figsize=(16, 8))
for i in range(1, 29):
    print("i =", i)
    plt.subplot(7, 4, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=preds_km, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)

show()

print("------------------------------")  # 30個

# Expectation-maximization (Gaussian Mixture Model)

from sklearn.mixture import GaussianMixture

gm_bic = []
gm_score = []
for i in range(2, 12):
    print("i =", i)
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

plt.scatter(x=[i for i in range(2, 12)], y=gm_bic, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Gaussian mixture BIC score")
show()

plt.scatter(x=[i for i in range(2, 12)], y=gm_score, s=150, edgecolor="k")
show()

print("------------------------------")  # 30個

gm = GaussianMixture(
    n_components=5,
    verbose=1,
    n_init=10,
    tol=1e-2,
    covariance_type="full",
    max_iter=1000,
).fit(X_scaled)

cc = gm.means_
print(cc)

cc = km.cluster_centers_
print(cc)

cc = gm.means_ / km.cluster_centers_
print(cc)

preds_gm = gm.predict(X_scaled)

km_rand_score = adjusted_rand_score(preds_km, y)

gm_rand_score = adjusted_rand_score(preds_gm, y)

print("Adjusted Rand score for k-means", km_rand_score)
print("Adjusted Rand score for Gaussian Mixture model", gm_rand_score)

cc = silhouette_score(X_scaled, preds_km)
print(cc)

cc = silhouette_score(X_scaled, preds_gm)
print(cc)

plt.figure(figsize=(16, 8))
for i in range(1, 29):
    print("i =", i)
    plt.subplot(7, 4, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=preds_gm, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)

show()

print("------------------------------")  # 30個

# PCA

n_prin_comp = 3

pca_partial = PCA(n_components=n_prin_comp, svd_solver="full")
pca_partial.fit(X_scaled)

pca_full = PCA(n_components=n_features, svd_solver="full")
pca_full.fit(X_scaled)

# How much variance is explained by principal components?

pca_explained_var = pca_full.explained_variance_ratio_
cum_explaiend_var = pca_explained_var.cumsum()
print(cum_explaiend_var)

plt.figure(figsize=(12, 5))
plt.bar(x=["PrComp" + str(i) for i in range(1, 9)], height=cum_explaiend_var, width=0.6)
plt.xticks(fontsize=14)
plt.hlines(y=0.8, xmin="PrComp1", xmax="PrComp8", linestyles="dashed", lw=3)
plt.text(x="PrComp1", y=0.82, s="80% variance explained", fontsize=15)

show()

print("------------------------------")  # 30個

# Transform the original variables in principal component space and create a DataFrame
X_pca = pca_partial.fit_transform(X_scaled)
df_pca = pd.DataFrame(
    data=X_pca, columns=["Principal_comp" + str(i) for i in range(1, n_prin_comp + 1)]
)

# Running k-means on the transformed features
km_scores = []
km_silhouette = []
vmeasure_score = []
for i in range(2, 12):
    print("i =", i)
    km = KMeans(n_clusters=i, random_state=0).fit(X_pca)
    preds = km.predict(X_pca)
    print("Score for number of cluster(s) {}: {}".format(i, km.score(X_pca)))
    km_scores.append(-km.score(X_pca))
    silhouette = silhouette_score(X_pca, preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))
    v_measure = v_measure_score(y, preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i, v_measure))
    print("-" * 100)

plt.scatter(x=[i for i in range(2, 12)], y=km_scores, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("K-means scores")
show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("V-measures scores")
show()

# K-means fitting with PCA-transformed data
km_pca = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_pca)
preds_km_pca = km_pca.predict(X_pca)

# Visualizing the clusters after running k-means on PCA-transformed features
col_pca_combi = list(combinations(df_pca.columns, 2))
num_pca_combi = len(col_pca_combi)

plt.figure(figsize=(16, 8))
for i in range(1, num_pca_combi + 1):
    print("i =", i)
    plt.subplot(int(num_pca_combi / 3) + 1, 3, i)
    dim1 = col_pca_combi[i - 1][0]
    dim2 = col_pca_combi[i - 1][1]
    plt.scatter(df_pca[dim1], df_pca[dim2], c=preds_km_pca, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)
show()

# ICA

from sklearn.decomposition import FastICA

n_ind_comp = 3
ica_partial = FastICA(n_components=n_ind_comp)
ica_partial.fit(X_scaled)

ica_full = FastICA(max_iter=1000)
ica_full.fit(X_scaled)

X_ica = ica_partial.fit_transform(X_scaled)
df_ica = pd.DataFrame(
    data=X_ica, columns=["Independent_comp" + str(i) for i in range(1, n_ind_comp + 1)]
)

# Running k-means on the independent features
km_scores = []
km_silhouette = []
vmeasure_score = []
for i in range(2, 12):
    print("i =", i)
    km = KMeans(n_clusters=i, random_state=0).fit(X_ica)
    preds = km.predict(X_ica)
    print("Score for number of cluster(s) {}: {}".format(i, km.score(X_ica)))
    km_scores.append(-km.score(X_ica))
    silhouette = silhouette_score(X_ica, preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))
    v_measure = v_measure_score(y, preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i, v_measure))
    print("-" * 100)

plt.scatter(x=[i for i in range(2, 12)], y=km_scores)
show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score)
show()

# K-means fitting with ICA-transformed data
km_ica = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_ica)
preds_km_ica = km_ica.predict(X_ica)

# Visualizing the clusters after running k-means on ICA-transformed features
col_ica_combi = list(combinations(df_ica.columns, 2))
num_ica_combi = len(col_ica_combi)

plt.figure(figsize=(16, 8))
for i in range(1, num_ica_combi + 1):
    print("i =", i)
    plt.subplot(int(num_ica_combi / 3) + 1, 3, i)
    dim1 = col_ica_combi[i - 1][0]
    dim2 = col_ica_combi[i - 1][1]
    plt.scatter(df_ica[dim1], df_ica[dim2], c=preds_km_ica, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)
show()

# Random Projection
from sklearn.random_projection import GaussianRandomProjection

n_random_comp = 3
random_proj = GaussianRandomProjection(n_components=n_random_comp)
X_random_proj = random_proj.fit_transform(X_scaled)
df_random_proj = pd.DataFrame(
    data=X_random_proj,
    columns=["Random_projection" + str(i) for i in range(1, n_random_comp + 1)],
)

# Running k-means on random projections

km_scores = []
km_silhouette = []
vmeasure_score = []
for i in range(2, 12):
    print("i =", i)
    km = KMeans(n_clusters=i, random_state=0).fit(X_random_proj)
    preds = km.predict(X_random_proj)
    print("Score for number of cluster(s) {}: {}".format(i, km.score(X_random_proj)))
    km_scores.append(-km.score(X_random_proj))
    silhouette = silhouette_score(X_random_proj, preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i, silhouette))
    v_measure = v_measure_score(y, preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i, v_measure))
    print("-" * 100)

plt.scatter(x=[i for i in range(2, 12)], y=km_scores)
show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score)
show()

# K-means fitting with random-projected data

km_random_proj = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_random_proj)
preds_km_random_proj = km_random_proj.predict(X_random_proj)

# Visualizing the clusters after running k-means on random-projected features

col_random_proj_combi = list(combinations(df_random_proj.columns, 2))
num_random_proj_combi = len(col_random_proj_combi)

plt.figure(figsize=(16, 8))
for i in range(1, num_random_proj_combi + 1):
    print("i =", i)
    plt.subplot(int(num_random_proj_combi / 3) + 1, 3, i)
    dim1 = col_random_proj_combi[i - 1][0]
    dim2 = col_random_proj_combi[i - 1][1]
    plt.scatter(
        df_random_proj[dim1],
        df_random_proj[dim2],
        c=preds_km_random_proj,
        edgecolor="k",
    )
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)
show()


def plot_cluster_rp(df_rp, preds_rp):
    # Plots clusters after running random projection
    plt.figure(figsize=(16, 8))
    for i in range(1, num_random_proj_combi + 1):
        print("i =", i)
        plt.subplot(int(num_random_proj_combi / 3) + 1, 3, i)
        dim1 = col_random_proj_combi[i - 1][0]
        dim2 = col_random_proj_combi[i - 1][1]
        plt.scatter(df_rp[dim1], df_rp[dim2], c=preds_rp, edgecolor="k")
        plt.xlabel(f"{dim1}", fontsize=13)
        plt.ylabel(f"{dim2}", fontsize=13)
    show()


# Running the random projections many times

rp_score = []
rp_silhouette = []
rp_vmeasure = []
for i in range(20):
    print("i =", i)
    random_proj = GaussianRandomProjection(n_components=n_random_comp)
    X_random_proj = random_proj.fit_transform(X_scaled)
    df_random_proj = pd.DataFrame(
        data=X_random_proj,
        columns=["Random_projection" + str(i) for i in range(1, n_random_comp + 1)],
    )

    km = KMeans(n_clusters=5, random_state=0).fit(X_random_proj)
    preds = km.predict(X_random_proj)
    print("Score for iteration {}: {}".format(i, km.score(X_random_proj)))
    rp_score.append(-km.score(X_random_proj))

    silhouette = silhouette_score(X_random_proj, preds)
    rp_silhouette.append(silhouette)
    print("Silhouette score for iteration {}: {}".format(i, silhouette))

    v_measure = v_measure_score(y, preds)
    rp_vmeasure.append(v_measure)
    print("V-measure score for iteration {}: {}".format(i, v_measure))
    print("-" * 100)

    plot_cluster_rp(df_random_proj, preds)


plt.scatter(x=[i for i in range(20)], y=rp_score)
show()

plt.scatter(x=[i for i in range(20)], y=rp_silhouette)
show()

plt.scatter(x=[i for i in range(20)], y=rp_vmeasure)
show()

# This kind of variation does not happen with PCA
pca_score = []
pca_silhouette = []
pca_vmeasure = []

for i in range(20):
    print("i =", i)
    pca_partial = PCA(n_components=n_prin_comp, svd_solver="full")
    X_pca = pca_partial.fit_transform(X_scaled)
    km = KMeans(n_clusters=5, random_state=0).fit(X_pca)
    preds = km.predict(X_pca)
    print("Score for iteration {}: {}".format(i, km.score(X_pca)))
    rp_score.append(-km.score(X_pca))
    silhouette = silhouette_score(X_pca, preds)
    rp_silhouette.append(silhouette)
    print("Silhouette score for iteration {}: {}".format(i, silhouette))
    v_measure = v_measure_score(y, preds)
    rp_vmeasure.append(v_measure)
    print("V-measure score for iteration {}: {}".format(i, v_measure))
    print("-" * 100)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Complexity and learning curve analysis for classification

# Synthetic data set from scikit-learn

sns.set_style("white")

X, y = datasets.make_hastie_10_2(n_samples=12000, random_state=1)

df = pd.DataFrame(data=X, columns=["X" + str(i) for i in range(1, 11)])
cc = df.head()
print(cc)

df["y"] = pd.Series(y)
cc = df.head()
print(cc)

# Basic visualizations

i = 1
plt.figure(figsize=(12, 8))
for c in df.columns[:-1]:
    plt.subplot(4, 3, i)
    plt.title(f"Histogram of variable {c}")
    plt.yticks()
    plt.xticks()
    plt.hist(df[c], bins=20, color="orange", edgecolor="k")
    i += 1
show()

i = 1
plt.figure(figsize=(12, 8))
for c in df.columns[:-1]:
    plt.subplot(4, 3, i)
    plt.title(f"Boxplot of {c}")
    plt.yticks()
    plt.xticks()
    sns.boxplot(y=df[c], x=df["y"])
    i += 1
show()

df_sample = df.sample(frac=0.01)
sns.set(style="ticks")

""" NG pairplot
g=sns.pairplot(df_sample,vars=["X1","X2","X3"],
               hue="y",markers=["o", "s"],
               diag_kind="kde",diag_kws=dict(shade=True),plot_kws=dict(s=100,alpha=0.75))
"""

X = df.drop("y", axis=1)
y = df["y"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# 資料分割
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.50)

cc = X_test.head()
print(cc)

cc = X_val.head()
print(cc)

# Show the shape of these sets

print("Shape of validation set:", X_val.shape)
print("Shape of test set:", X_test.shape)
print("Shape of training set:", X_train.shape)

# Decision Tree model
dtree = DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=5)

dtree.fit(X_train, y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.7088888888888889

# Varying hyperparameters
# Varying max_depth

val_acc_max_depth = []
val_f1_max_depth = []
train_acc_max_depth = []
train_f1_max_depth = []

val_range = (1, 81, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=i, min_samples_leaf=1)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_max_depth.append(acc_train)
    train_f1_max_depth.append(f1_train)
    val_acc_max_depth.append(acc_val)
    val_f1_max_depth.append(f1_val)

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_max_depth,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_max_depth, c="blue"
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Max depth of the decision tree")
plt.ylabel("Accuracy")
plt.ylim(0.5, 1.05)
show()

# Varying min_samples_leaf with max_depth = 20

val_acc_min_samples_leaf = []
val_f1_min_samples_leaf = []
train_acc_min_samples_leaf = []
train_f1_min_samples_leaf = []

val_range = (1, 41, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=i)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_min_samples_leaf.append(acc_train)
    train_f1_min_samples_leaf.append(f1_train)
    val_acc_min_samples_leaf.append(acc_val)
    val_f1_min_samples_leaf.append(f1_val)

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_min_samples_leaf,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_min_samples_leaf,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Minimum samples/leaf (max depth=20)")
plt.ylabel("Accuracy")
# plt.ylim(0.7,1.0)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=5)
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("y", axis=1)
    y_train_sampled = df_sampled["y"]
    # Fitting and Predictions
    dtree.fit(X_train_sampled, y_train_sampled)
    pred_train = dtree.predict(X_train_sampled)
    pred_val = dtree.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    if i % 10 == 0:
        print(f"aaa Done for: {i}% training set size")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.0)
show()

# Boosting algorithm model
from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(
    DecisionTreeClassifier(min_samples_leaf=2, max_depth=3),
    n_estimators=20,
    learning_rate=0.01,
)

adaboost.fit(X_train, y_train)

# Predictions and evaluation

predictions = adaboost.predict(X_val)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.7422222222222222

# Varying number of estimators

val_acc_num_trees = []
val_f1_num_trees = []
train_acc_num_trees = []
train_f1_num_trees = []
time_adaboost = []

val_range = (1, 152, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    t1 = time.time()
    # Fitting
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=2),
        n_estimators=i,
        learning_rate=0.2,
    )
    adaboost.fit(X_train, y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_num_trees.append(acc_train)
    train_f1_num_trees.append(f1_train)
    val_acc_num_trees.append(acc_val)
    val_f1_num_trees.append(f1_val)
    t2 = time.time()
    time_adaboost.append(t2 - t1)
    print(f"aaa Done for number of trees: {i}")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_num_trees,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_num_trees, c="blue"
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Accuracy")
plt.ylim(0.5, 1.05)
show()

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), time_adaboost, c="red"
)
# plt.plot(range(val_range[0],val_range[1],val_range[2]),val_acc_num_trees,c='blue')
# plt.legend(["Training","Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Model training time (seconds)")
# plt.ylim(0.7,1.05)
show()

# Tweaking the learning_rate of AdaBoostClassifier

val_acc_lr = []
val_f1_lr = []
train_acc_lr = []
train_f1_lr = []

val_range = (1, 21, 1)
print("val_range :", val_range)

lr_range = []
for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    lr = 0.1 * i
    lr_range.append(lr)
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=2),
        n_estimators=100,
        learning_rate=lr,
    )
    adaboost.fit(X_train, y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_lr.append(acc_train)
    train_f1_lr.append(f1_train)
    val_acc_lr.append(acc_val)
    val_f1_lr.append(f1_val)
    print(f"Done for learning rate: {lr}")


plt.plot(lr_range, train_acc_lr, c="red")
plt.plot(lr_range, val_acc_lr, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Learning rate of AdaBoostClassifier")
plt.ylabel("Accuracy")
# plt.ylim(0.7,1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Model
    percentage = i * 0.01
    adaboost = adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=20),
        n_estimators=20,
        learning_rate=0.5,
    )
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("y", axis=1)
    y_train_sampled = df_sampled["y"]
    # Fitting and prediction
    adaboost.fit(X_train_sampled, y_train_sampled)
    pred_train = adaboost.predict(X_train_sampled)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"bbb Done for: {i}% training set size")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.75,1.0)
show()

# SVM model

X_train_scaled = StandardScaler().fit_transform(X_train)
X_val_scaled = StandardScaler().fit_transform(X_val)

from sklearn.svm import SVC

svc_clf = SVC(kernel="poly", C=1, degree=2)

svc_clf.fit(X_train_scaled, y_train)

# Predictions and evaluation

predictions = svc_clf.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.9788888888888889

# Varying degree of polynomial kernel

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []

val_range = (1, 11, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    svc_clf = SVC(kernel="poly", C=0.01, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"bbb Done for number of degree: {i}")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_degree, c="red"
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_degree, c="blue"
)
plt.grid(True)
plt.legend(["Training", "Validation"])
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# But what if we put a penalty for misclassification? C = 10

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []

val_range = (1, 11, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    svc_clf = SVC(kernel="poly", C=10, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"ccc Done for number of degree: {i}")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_degree, c="red"
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_degree, c="blue"
)
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# Varying regularization parameter C

val_acc_C = []
val_f1_C = []
train_acc_C = []
train_f1_C = []
C_range = []

val_range = (-8, 2, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    C = 2 ** (i)
    C_range.append(C)
    # Fitting
    svc_clf = SVC(kernel="poly", C=C, degree=2)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_C.append(acc_train)
    train_f1_C.append(f1_train)
    val_acc_C.append(acc_val)
    val_f1_C.append(f1_val)
    print(f"ddd111 Done for number of C: {2**(i)}")


plt.semilogx(C_range, train_acc_C, c="red")
plt.semilogx(C_range, val_acc_C, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Regularization/penalty parameter $C$")
plt.ylabel("Accuracy")
# plt.ylim(0.81,0.85)
show()

# Radial basis function (RBF) kernel - varying gamma

val_acc_gamma = []
val_f1_gamma = []
train_acc_gamma = []
train_f1_gamma = []
gamma_range = []

val_range = (-25, 10, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    gamma = 10 ** (i / 5.0)
    gamma_range.append(gamma)
    # Fitting9
    svc_clf = SVC(kernel="rbf", C=1, gamma=gamma)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_gamma.append(acc_train)
    train_f1_gamma.append(f1_train)
    val_acc_gamma.append(acc_val)
    val_f1_gamma.append(f1_val)
    print(f"aaa Done for gamma: {gamma}")


plt.semilogx(gamma_range, train_acc_gamma, c="red")
plt.semilogx(gamma_range, val_acc_gamma, c="blue")
plt.grid(True)
plt.legend(["Training", "Validation"])
plt.xticks()
plt.yticks()
plt.xlabel("Gamma of the SVM classifier RBF kernel")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    svc_clf = SVC(kernel="rbf", C=1, gamma=0.01)
    # Sampling (and scaling)
    df_sampled = df.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("y", axis=1)
    y_train_sampled = df_sampled["y"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    svc_clf.fit(X_train_sampled, y_train_sampled)
    pred_train = svc_clf.predict(X_train_sampled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    print(f"ccc Done for: {i}% training set size")

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.9, 1.0)
show()

# K-nearest neighbor model

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(3)

knn.fit(X_train_scaled, y_train)

predictions = knn.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.7255555555555555

# Varying number of neighbors

val_acc_k = []
val_f1_k = []
train_acc_k = []
train_f1_k = []

val_range = (1, 21, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    knn = KNeighborsClassifier(i)
    knn.fit(X_train_scaled, y_train)
    pred_train = knn.predict(X_train_scaled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_k.append(acc_train)
    train_f1_k.append(f1_train)
    val_acc_k.append(acc_val)
    val_f1_k.append(f1_val)
    print(f"eee Done for number of neighbors: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_k, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_k, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neighbors ($K$)")
plt.ylabel("Accuracy")
plt.ylim(0.5, 1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    knn = KNeighborsClassifier(10)
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("y", axis=1)
    y_train_sampled = df_sampled["y"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    knn.fit(X_train_sampled, y_train_sampled)
    pred_train = knn.predict(X_train_sampled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"ddd222 Done for: {i}% training set size")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.7,0.9)
# plt.xlim(0, 110)
show()

# Neural Networks (Multi-layer perceptron)

import keras

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

n_input = X_train_scaled.shape[0]
num_classes = len(y_train.unique())
input_dim = X_train_scaled.shape[1]

# Function to construct 2-hidden-layer Keras model


def make_NN_model(
    input_dim,
    num_classes,
    neuron_layer_1=20,
    neuron_layer_2=10,
    dropout_prob=0.25,
    activation_func="relu",
    learning_rate=0.01,
    optimizer="SGD",
):
    """
    Creates a 2-hidden-layer Keras Neural Network model by adding densely connected layers, \
    dropout layers, and an output layer with 'softmax' activation with appropriate number of nodes for classification
    """
    model = Sequential()
    model.add(
        Dense(neuron_layer_1, input_shape=(input_dim,), activation=activation_func)
    )
    model.add(Dropout(dropout_prob))
    model.add(Dense(neuron_layer_2, activation=activation_func))
    # model.add(Dense(50,activation='relu'))
    model.add(Dropout(dropout_prob))
    # Softmax activation for the last layer for classification
    model.add(Dense(1, activation="sigmoid"))

    if optimizer == "SGD":
        optimizer = keras.optimizers.SGD()  # lr=learning_rate)
    if optimizer == "Adam":
        optimizer = keras.optimizers.Adam()  # lr=learning_rate)
    if optimizer == "RMSprop":
        optimizer = keras.optimizers.RMSprop()  # lr=learning_rate)

    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])

    return model


# Function to run the NN model


def run_NN(
    model,
    X_train,
    y_train,
    X_val,
    y_val,
    num_epochs=200,
    batch_size=16,
    plot_loss=False,
    verbosity=0,
):
    # save best model as checkpointer
    from keras.callbacks import ModelCheckpoint

    checkpointer = ModelCheckpoint(
        filepath="model.weights.best.hdf5", verbose=verbosity, save_best_only=True
    )

    # train the model
    hist = model.fit(
        X_train,
        y_train,
        batch_size=batch_size,
        epochs=num_epochs,
        validation_data=(X_val, y_val),
        verbose=verbosity,
        shuffle=False,
    )

    if plot_loss:
        plt.plot(hist.history["acc"], color="red")
        plt.plot(hist.history["val_acc"], color="blue")
        plt.title("Training and validation set accuracy")
        plt.grid(True)
        plt.xlabel("Epochs")
        plt.legend(["Training", "Validation"])
        show()

    return hist


# Function to test the NN model


def test_NN(hist, X_test, y_test):
    """
    Test a NN model with test data set for accuracy
    hist: A History object generated by the Keras model fitting process
    """
    score = hist.model.evaluate(X_test, y_test, verbose=0)[1]
    return score


# Basic run of the neural network (using Adam optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.2,
    learning_rate=0.02,
    neuron_layer_1=20,
    neuron_layer_2=10,
    optimizer="Adam",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=256,
    num_epochs=500,
    plot_loss=True,
)


# Basic run of the neural network (using Stochastic Gradient Descent optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.2,
    learning_rate=0.02,
    neuron_layer_1=100,
    neuron_layer_2=50,
    optimizer="SGD",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=256,
    num_epochs=1000,
    plot_loss=True,
)


# Varying hyperparameters
# Number of neurons per layer

train_acc_n = []
val_acc_n = []

val_range = (10, 200, 10)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.1,
        learning_rate=0.02,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="SGD",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=100,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"fff Done for number of neurons (each hidden layer): {i}")

plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
# plt.ylim(0.0,0.9)
show()

# Learning rate

train_acc_lr = []
val_acc_lr = []

val_range = (-40, -10, 1)
print("val_range :", val_range)

lr_range = []
for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    t1 = time.time()
    lr = 10 ** (i / 10.0)
    lr_range.append(lr)
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.1,
        learning_rate=lr,
        neuron_layer_1=100,
        neuron_layer_2=100,
        optimizer="SGD",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=100,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_lr.append(acc_train)
    val_acc_lr.append(acc_val)
    t2 = time.time()
    print(f"Done for learning rate: {lr}. Time took {round((t2-t1),2)} seconds")

plt.plot(lr_range, train_acc_lr, c="red")
plt.plot(lr_range, val_acc_lr, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Learning rate")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# How to improve neural network performance?

model = Sequential()
model.add(Dense(100, input_shape=(input_dim,), activation="selu"))
model.add(Dropout(0.1))
model.add(Dense(100, activation="selu"))
model.add(Dropout(0.1))
model.add(Dense(50, activation="selu"))
model.add(Dropout(0.1))
# sigmoid activation for the last layer for classification
model.add(Dense(1, activation="sigmoid"))

# Optimizer
optimizer = keras.optimizers.Adam(lr=0.01)

model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])

print("檢視模型架構")
model.summary()  # 檢視模型架構

hist = run_NN(
    model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=256,
    num_epochs=100,
    plot_loss=True,
)

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    t1 = time.time()
    percentage = i * 0.01
    # Sampling
    df_sampled = df.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("y", axis=1)
    y_train_sampled = df_sampled["y"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.05,
        neuron_layer_1=100,
        neuron_layer_2=100,
        optimizer="SGD",
    )
    hist = run_NN(
        nn_model,
        X_train_sampled,
        y_train_sampled,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=100,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_sampled, y_train_sampled, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)

    t2 = time.time()
    print(f"eee Done for: {i}% training set size. Took {round((t2-t1),2)} seconds.")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
# plt.xlim(0, 110)
show()

# At the end, comparison of performance (accuracy) on test set and wall time

dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=10)
dtree.fit(X_train, y_train)
predictions = dtree.predict(X_test)
score_dt = accuracy_score(y_test, predictions)
print(score_dt)

from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(
    DecisionTreeClassifier(min_samples_leaf=20, max_depth=2),
    n_estimators=80,
    learning_rate=0.5,
)
adaboost.fit(X_train, y_train)
predictions = adaboost.predict(X_test)
score_adaboost = accuracy_score(y_test, predictions)
print(score_adaboost)

X_train_scaled = StandardScaler().fit_transform(X_train)
X_test_scaled = StandardScaler().fit_transform(X_test)

from sklearn.svm import SVC

svc_clf = SVC(kernel="rbf", C=1, gamma=0.05)
svc_clf.fit(X_train_scaled, y_train)
predictions = svc_clf.predict(X_test_scaled)
score_SVC = accuracy_score(y_test, predictions)
print(score_SVC)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(5)
knn.fit(X_train_scaled, y_train)
predictions = knn.predict(X_test_scaled)
score_KNN = accuracy_score(y_test, predictions)
print(score_KNN)

accuracy_scores = [0.79, 0.93, 0.97, 0.69, 0.45]
timing = [0.23, 2.72, 2.27, 0.667, 3.5]

plt.figure(figsize=(15, 5))
plt.title("Accuracy of the ML model")
plt.bar(
    x=[
        "Decision Tree with pruning",
        "AdaBoost",
        "Support vector machine",
        "k-nearest neighbor",
        "Multi-layer perceptron",
    ],
    height=accuracy_scores,
    width=0.5,
    color="red",
    edgecolor="k",
)
plt.xticks()
plt.yticks()
show()

plt.figure(figsize=(15, 5))
plt.title("Wall time of running the ML model")
plt.bar(
    x=[
        "Decision Tree with pruning",
        "AdaBoost",
        "Support vector machine",
        "k-nearest neighbor",
        "Multi-layer perceptron",
    ],
    height=timing,
    width=0.5,
    color="blue",
    edgecolor="k",
)
plt.xticks()
plt.yticks()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Complexity and learning curve analysis for classification

sns.set_style("white")

df = pd.read_csv("Datasets/loan_data.csv")

# Look at first 5 rows
# cc = df.head()
# print(cc)

# Basic descriptive statistics

# df.describe()

# One-hot encoding of categorical features

df_final = pd.get_dummies(df, ["purpose"], drop_first=True)
df_final = df_final.drop("credit.policy", axis=1)

# cc = df_final.shape
# print(cc)
# (9578, 18)

# Basic visualizations

i = 1
plt.figure(figsize=(12, 8))
for c in df.describe().columns[:-1]:
    plt.subplot(4, 3, i)
    plt.title(f"Histogram of {c}")
    plt.yticks()
    plt.xticks()
    plt.hist(df[c], bins=20, color="orange", edgecolor="k")
    i += 1
show()

""" plot NG
i=1
plt.figure(figsize=(16, 8))
for c in df_final.columns[:-1]:
    plt.subplot(6,3,i)
    plt.title(f"Boxplot of {c}")
    plt.yticks()
    plt.xticks()
    sns.boxplot(y=df_final[c],x=df_final['not.fully.paid'])
    i+=1
show()
"""

""" plot NG
sns.set(style="ticks", color_codes=True)
g=sns.pairplot(df_final,vars=["log.annual.inc","dti","fico","revol.bal"],
               plot_kws=dict(s=30, edgecolor="b", linewidth=1),
               hue="not.fully.paid",markers=["o", "s"],
               diag_kind="kde",diag_kws=dict(shade=True))
"""

X = df_final.drop("not.fully.paid", axis=1)
y = df["not.fully.paid"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# cc = X_train.head()
# print(cc)

# cc = y.head()
# print(cc)

# 資料分割
X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.50)

# cc = X_test.head()
# print(cc)

# cc = X_val.head()
# print(cc)

# Show the shape of these sets

print("Shape of validation set:", X_val.shape)
print("Shape of test set:", X_test.shape)
print("Shape of training set:", X_train.shape)

# Decision Tree model
dtree = DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=5)

dtree.fit(X_train, y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8058455114822547

# Varying hyperparameters: Pruning the tree

# Varying max_depth

val_acc_max_depth = []
val_f1_max_depth = []
train_acc_max_depth = []
train_f1_max_depth = []
for i in range(3, 21):
    print("i =", i)
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=i, min_samples_leaf=1)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_max_depth.append(acc_train)
    train_f1_max_depth.append(f1_train)
    val_acc_max_depth.append(acc_val)
    val_f1_max_depth.append(f1_val)

plt.plot(range(3, 21), train_acc_max_depth, c="red")
plt.plot(range(3, 21), val_acc_max_depth, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Max depth of the decision tree")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.0)
show()

# Varying min_samples_leaf with max_depth = 20

val_acc_min_samples_leaf = []
val_f1_min_samples_leaf = []
train_acc_min_samples_leaf = []
train_f1_min_samples_leaf = []

for i in range(1, 41):
    print("i =", i)
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=i)
    dtree.fit(X_train, y_train)
    pred_train = dtree.predict(X_train)
    pred_val = dtree.predict(X_val)
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    train_acc_min_samples_leaf.append(acc_train)
    train_f1_min_samples_leaf.append(f1_train)
    val_acc_min_samples_leaf.append(acc_val)
    val_f1_min_samples_leaf.append(f1_val)

plt.plot(range(1, 41), train_acc_min_samples_leaf, c="red")
plt.plot(range(1, 41), val_acc_min_samples_leaf, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Minimum samples/leaf (max depth=20)")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.0)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    dtree = DecisionTreeClassifier(criterion="gini", max_depth=20, min_samples_leaf=20)
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    # Fitting and Predictions
    dtree.fit(X_train_sampled, y_train_sampled)
    pred_train = dtree.predict(X_train_sampled)
    pred_val = dtree.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)
    if i % 10 == 0:
        print(f"fff Done for: {i}% training set size")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.0)
show()

# Boosting algorithm model

from sklearn.ensemble import AdaBoostClassifier

adaboost = AdaBoostClassifier(
    DecisionTreeClassifier(min_samples_leaf=2), n_estimators=20, learning_rate=0.01
)

adaboost.fit(X_train, y_train)

# Predictions and evaluation

predictions = adaboost.predict(X_val)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8322894919972165

# Varying number of estimators

val_acc_num_trees = []
val_f1_num_trees = []
train_acc_num_trees = []
train_f1_num_trees = []

val_range = (1, 53, 3)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=20),
        n_estimators=i,
        learning_rate=0.2,
    )
    adaboost.fit(X_train, y_train)
    pred_train = adaboost.predict(X_train)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_num_trees.append(acc_train)
    train_f1_num_trees.append(f1_train)
    val_acc_num_trees.append(acc_val)
    val_f1_num_trees.append(f1_val)
    print(f"ggg Done for number of trees: {i}")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_num_trees,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_num_trees, c="blue"
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Accuracy")
plt.ylim(0.7, 1.05)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Model
    percentage = i * 0.01
    adaboost = AdaBoostClassifier(
        DecisionTreeClassifier(min_samples_leaf=20, max_depth=20),
        n_estimators=20,
        learning_rate=0.2,
    )
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    # Fitting and prediction
    adaboost.fit(X_train_sampled, y_train_sampled)
    pred_train = adaboost.predict(X_train_sampled)
    pred_val = adaboost.predict(X_val)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"ggg Done for: {i}% training set size")

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.05)
show()

# SVM model

X_train_scaled = StandardScaler().fit_transform(X_train)
X_val_scaled = StandardScaler().fit_transform(X_val)

from sklearn.svm import SVC

svc_clf = SVC(kernel="poly", C=1, degree=2)

svc_clf.fit(X_train_scaled, y_train)

# Predictions and evaluation

predictions = svc_clf.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8350730688935282

# Varying degree of polynomial kernel

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []

val_range = (1, 11, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    svc_clf = SVC(kernel="poly", C=0.01, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"hhh Done for number of degree: {i}")

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_degree, c="red"
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_degree, c="blue"
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
plt.ylim(0.8, 0.9)
show()

# But what if we put a penalty for misclassification? C = 10

val_acc_degree = []
val_f1_degree = []
train_acc_degree = []
train_f1_degree = []

val_range = (1, 11, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    svc_clf = SVC(kernel="poly", C=1, degree=i)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_degree.append(acc_train)
    train_f1_degree.append(f1_train)
    val_acc_degree.append(acc_val)
    val_f1_degree.append(f1_val)
    print(f"iii Done for number of degree: {i}")

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_degree, c="red"
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_degree, c="blue"
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Degree of the SVM classifier kernel (polynomial)")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# Varying regularization parameter C (i.e. in the Lagrangian formulation of SVM)

val_acc_C = []
val_f1_C = []
train_acc_C = []
train_f1_C = []
C_range = []

val_range = (-8, 2, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    C = 2 ** (i)
    C_range.append(C)
    # Fitting
    svc_clf = SVC(kernel="poly", C=C, degree=2)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_C.append(acc_train)
    train_f1_C.append(f1_train)
    val_acc_C.append(acc_val)
    val_f1_C.append(f1_val)
    print(f"jjj Done for number of C: {2**(i)}")


plt.plot(C_range, train_acc_C, c="red")
plt.plot(C_range, val_acc_C, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Regularization/penalty parameter $C$")
plt.ylabel("Accuracy")
# plt.ylim(0.81,0.85)
show()

# Radial basis function (RBF) kernel - varying gamma

val_acc_gamma = []
val_f1_gamma = []
train_acc_gamma = []
train_f1_gamma = []
gamma_range = []

val_range = (-5, 2, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    gamma = 10 ** (i)
    gamma_range.append(gamma)
    # Fitting
    svc_clf = SVC(kernel="rbf", C=10, gamma=gamma)
    svc_clf.fit(X_train_scaled, y_train)
    pred_train = svc_clf.predict(X_train_scaled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_gamma.append(acc_train)
    train_f1_gamma.append(f1_train)
    val_acc_gamma.append(acc_val)
    val_f1_gamma.append(f1_val)
    print(f"bbb Done for gamma: {gamma}")


plt.semilogx(gamma_range, train_acc_gamma, c="red")
plt.semilogx(gamma_range, val_acc_gamma, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Gamma of the SVM classifier RBF kernel")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    svc_clf = SVC(kernel="poly", C=0.001, degree=2)
    # Sampling (and scaling)
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    svc_clf.fit(X_train_sampled, y_train_sampled)
    pred_train = svc_clf.predict(X_train_sampled)
    pred_val = svc_clf.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    print(f"hhh Done for: {i}% training set size")


plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.82, 0.86)
show()

# K-nearest neighbor model

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(3)

knn.fit(X_train_scaled, y_train)

predictions = knn.predict(X_val_scaled)

score1 = accuracy_score(y_val, predictions)
print(score1)

# 0.8058455114822547

# Varying number of neighbors

val_acc_k = []
val_f1_k = []
train_acc_k = []
train_f1_k = []

val_range = (1, 21, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    knn = KNeighborsClassifier(i)
    knn.fit(X_train_scaled, y_train)
    pred_train = knn.predict(X_train_scaled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train, pred_train)
    f1_train = f1_score(y_train, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_k.append(acc_train)
    train_f1_k.append(f1_train)
    val_acc_k.append(acc_val)
    val_f1_k.append(f1_val)
    print(f"kkk Done for number of neighbors: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_k, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_k, c="blue")
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neighbors ($K$)")
plt.ylabel("Accuracy")
# plt.ylim(0.81,0.85)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
val_f1_train_size = []
train_acc_train_size = []
train_f1_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    percentage = i * 0.01
    knn = KNeighborsClassifier(5)
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and prediction
    knn.fit(X_train_sampled, y_train_sampled)
    pred_train = knn.predict(X_train_sampled)
    pred_val = knn.predict(X_val_scaled)
    # Accuracy and F1 score
    acc_train = accuracy_score(y_train_sampled, pred_train)
    f1_train = f1_score(y_train_sampled, pred_train, average="micro")
    acc_val = accuracy_score(y_val, pred_val)
    f1_val = f1_score(y_val, pred_val, average="micro")
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    train_f1_train_size.append(f1_train)
    val_acc_train_size.append(acc_val)
    val_f1_train_size.append(f1_val)

    if i % 10 == 0:
        print(f"iii Done for: {i}% training set size")

plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    train_acc_train_size,
    c="red",
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2] * RATIO),
    val_acc_train_size,
    c="blue",
)
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.7, 0.9)
# plt.xlim(0, 110)
show()

# Neural Networks (Multi-layer perceptron)

import keras

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

n_input = X_train_scaled.shape[0]
num_classes = len(y_train.unique())
input_dim = X_train_scaled.shape[1]

# Function to construct 2-hidden-layer Keras model


def make_NN_model(
    input_dim,
    num_classes,
    neuron_layer_1=20,
    neuron_layer_2=10,
    dropout_prob=0.25,
    activation_func="relu",
    learning_rate=0.01,
    optimizer="SGD",
):
    """
    Creates a 2-hidden-layer Keras Neural Network model by adding densely connected layers, \
    dropout layers, and an output layer with 'softmax' activation with appropriate number of nodes for classification
    """
    model = Sequential()
    model.add(
        Dense(neuron_layer_1, input_shape=(input_dim,), activation=activation_func)
    )
    model.add(Dropout(dropout_prob))
    model.add(Dense(neuron_layer_2, activation=activation_func))
    # model.add(Dense(50,activation='relu'))
    model.add(Dropout(dropout_prob))
    # Softmax activation for the last layer for classification
    model.add(Dense(1, activation="sigmoid"))

    if optimizer == "SGD":
        optimizer = keras.optimizers.SGD(lr=learning_rate)
    if optimizer == "Adam":
        optimizer = keras.optimizers.Adam(lr=learning_rate)
    if optimizer == "RMSprop":
        optimizer = keras.optimizers.RMSprop(lr=learning_rate)

    model.compile(loss="binary_crossentropy", optimizer=optimizer, metrics=["accuracy"])

    return model


# Function to run the NN model


def run_NN(
    model,
    X_train,
    y_train,
    X_val,
    y_val,
    num_epochs=200,
    batch_size=16,
    plot_loss=False,
    verbosity=0,
):
    # save best model as checkpointer
    from keras.callbacks import ModelCheckpoint

    checkpointer = ModelCheckpoint(
        filepath="model.weights.best.hdf5", verbose=verbosity, save_best_only=True
    )

    # train the model
    hist = model.fit(
        X_train,
        y_train,
        batch_size=batch_size,
        epochs=num_epochs,
        validation_data=(X_val, y_val),
        verbose=verbosity,
        shuffle=False,
    )

    if plot_loss:
        plt.plot(hist.history["acc"], color="red")
        plt.plot(hist.history["val_acc"], color="blue")
        plt.title("Training and validation set accuracy")
        plt.grid(True)
        plt.xlabel("Epochs")
        plt.legend(["Training", "Validation"])
        show()

    return hist


# Function to test the NN model


def test_NN(hist, X_test, y_test):
    """
    Test a NN model with test data set for accuracy
    hist: A History object generated by the Keras model fitting process
    """
    score = hist.model.evaluate(X_test, y_test, verbose=0)[1]
    return score


# Basic run of the neural network (using Adam optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.0,
    learning_rate=0.0001,
    neuron_layer_1=10,
    neuron_layer_2=5,
    optimizer="Adam",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=64,
    num_epochs=25,
    plot_loss=True,
)


# Basic run of the neural network (using Stochastic Gradient Descent optimizer)

nn_model = make_NN_model(
    input_dim=input_dim,
    num_classes=num_classes,
    dropout_prob=0.0,
    learning_rate=0.0001,
    neuron_layer_1=10,
    neuron_layer_2=5,
    optimizer="SGD",
)

hist = run_NN(
    nn_model,
    X_train_scaled,
    y_train,
    X_val_scaled,
    y_val,
    verbosity=1,
    batch_size=64,
    num_epochs=25,
    plot_loss=True,
)


# Varying hyperparameter - number of neurons per layer? How many epochs should we run for?

# Running for num_epochs = 5

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=5,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"lll Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# Running for num_epochs = 10

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=10,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"mmm Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# Running for num_epochs = 25

train_acc_n = []
val_acc_n = []

val_range = (2, 21, 1)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    # Fitting
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=i,
        neuron_layer_2=i,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_scaled,
        y_train,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_scaled, y_train, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_n.append(acc_train)
    val_acc_n.append(acc_val)
    print(f"nnn Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_n, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of neurons per layer")
plt.ylabel("Accuracy")
plt.ylim(0.0, 0.9)
show()

# LEARNING CURVE: Varying training set size

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    percentage = i * 0.01
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.0001,
        neuron_layer_1=5,
        neuron_layer_2=5,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_sampled,
        y_train_sampled,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_sampled, y_train_sampled, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)

    print(f"jjj Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
# plt.xlim(0, 110)
show()

# To smooth out the dependence on training set size, can we tweak the learning rate?

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
print("val_range :", val_range)

for i in range(val_range[0], val_range[1], val_range[2] * RATIO):
    print("i =", i)
    percentage = i * 0.01
    # Sampling
    df_sampled = df_final.sample(frac=percentage)
    X_train_sampled = df_sampled.drop("not.fully.paid", axis=1)
    y_train_sampled = df_sampled["not.fully.paid"]
    X_train_sampled = StandardScaler().fit_transform(X_train_sampled)
    # Fitting and Predictions
    nn_model = make_NN_model(
        input_dim=input_dim,
        num_classes=num_classes,
        dropout_prob=0.0,
        learning_rate=0.001,
        neuron_layer_1=5,
        neuron_layer_2=5,
        optimizer="Adam",
    )
    hist = run_NN(
        nn_model,
        X_train_sampled,
        y_train_sampled,
        X_val_scaled,
        y_val,
        verbosity=0,
        batch_size=256,
        num_epochs=25,
        plot_loss=False,
    )
    # Accuracy score
    acc_train = hist.model.evaluate(X_train_sampled, y_train_sampled, verbose=0)[1]
    acc_val = hist.model.evaluate(X_val_scaled, y_val, verbose=0)[1]
    # Appending to the lists
    train_acc_train_size.append(acc_train)
    val_acc_train_size.append(acc_val)

    print(f"kkk Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2] * RATIO), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed (lr=0.001)")
plt.ylabel("Accuracy")
plt.ylim(0.5, 0.9)
# plt.xlim(0, 110)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Mean-shift Clustering Technique

from sklearn.cluster import MeanShift

centers = [[1, 1], [-1, -1], [1, -1]]

X, labels_true = make_blobs(
    n_samples=300, centers=centers, cluster_std=0.4, random_state=101
)

print(X.shape)
# (300, 2)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c="orange", s=75)
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

print("Number of clusters detected by the algorithm :", n_clusters)

# Number of clusters detected by the algorithm: 3

print("Cluster centers detected at :", cluster_centers)

plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], edgecolors="k", c=ms_model.labels_, s=75)
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

n_samples = [10, 20, 50, 100, 200, 500, 1000, 2000, 3000, 5000, 7500, 10000]
centers = [[1, 1], [-1, -1], [1, -1]]
t_ms = []
homo_ms = []
complete_ms = []

for i in n_samples:
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
plt.title("Time complexity of Mean Shift")
plt.scatter(n_samples, t_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_ms, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size")
plt.scatter(n_samples, homo_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_ms, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size")
plt.scatter(n_samples, complete_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, complete_ms, "k--", lw=3)
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
plt.title("Cluster detection with noisy data")
plt.scatter(noise, n_clusters, edgecolors="k", c="green", s=100)
plt.xticks()
plt.xlabel("Noise std.dev")
plt.yticks()
plt.ylabel("Number of clusters detected")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Principal Component Analysis (PCA)

df = pd.read_csv("./Datasets/wine.data.csv")
cc = df.head()
print(cc)

# Basic statistics

cc = df.iloc[:, 1:].describe()
print(cc)

# Boxplots by output labels/classes

for c in df.columns[1:]:
    df.boxplot(c, by="Class", figsize=(7, 4))
    plt.title("{}".format(c))
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

plt.title("Scatter plot of two features showing the \ncorrelation and class seperation")
plt.xlabel("OD280/OD315 of diluted wines")
plt.ylabel("Flavanoids")
show()


def correlation_matrix(df):
    from matplotlib import cm as cm

    fig = plt.figure(figsize=(16, 8))
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap("jet", 30)
    cax = ax1.imshow(df.corr(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title("Wine data set features correlation")
    labels = df.columns
    ax1.set_xticklabels(labels)
    ax1.set_yticklabels(labels)
    # Add colorbar, make sure to specify tick locations to match desired ticklabels
    fig.colorbar(cax, ticks=[0.1 * i for i in range(-11, 11)])
    show()


correlation_matrix(df)

# Principal Component Analysis, PCA

scaler = StandardScaler()

X = df.drop("Class", axis=1)
y = df["Class"]

X = scaler.fit_transform(X)

dfx = pd.DataFrame(data=X, columns=df.columns[1:])

cc = dfx.head()
print(cc)

cc = dfx.describe()
print(cc)

# PCA

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
plt.title("Explained variance ratio of the \nfitted principal component vector")
plt.xlabel("Principal components")
plt.xticks([i + 1 for i in range(len(dfx_pca.explained_variance_ratio_))])
plt.yticks()
plt.ylabel("Explained variance ratio")
show()

# Showing better class separation using principal components

dfx_trans = pca.transform(dfx)

# Put it in a data frame

dfx_trans = pd.DataFrame(data=dfx_trans)
cc = dfx_trans.head()
print(cc)

# Plot the first two columns of this transformed data set with the color set to original ground truth class label

plt.figure(figsize=(10, 6))
plt.scatter(
    dfx_trans[0], dfx_trans[1], c=df["Class"], edgecolors="k", alpha=0.75, s=150
)
plt.title("Class separation using first two principal components")
plt.xlabel("Principal component-1")
plt.ylabel("Principal component-2")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Clustering metrics - alternatives to the elbow method

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
    print("i =", i)
    plt.subplot(2, 3, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=data1[1], edgecolor="k", s=150)
    plt.xlabel(f"{dim1}")
    plt.ylabel(f"{dim2}")
show()

# How are the classes separated (boxplots)

plt.figure(figsize=(16, 8))
for i, c in enumerate(df1.columns):
    plt.subplot(3, 2, i + 1)
    sns.boxplot(y=df1[c], x=data1[1])
    plt.xticks()
    plt.yticks()
    plt.xlabel("Class")
    plt.ylabel(c)
    # show()
show()

X = df1

cc = X.head()
print(cc)

y = data1[1]

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# Running k-means and computing inter-cluster distance score for various k values

km_scores = []
km_silhouette = []
vmeasure_score = []
db_score = []
for i in range(2, 12):
    print("i =", i)
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
plt.title("The elbow method for determining number of clusters")
plt.scatter(x=[i for i in range(2, 12)], y=km_scores, s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("K-means score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.xlabel("V-measure score")
show()

plt.figure(figsize=(7, 4))
plt.title("The silhouette coefficient method \nfor determining number of clusters")
plt.scatter(x=[i for i in range(2, 12)], y=km_silhouette, s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("Silhouette score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
show()

plt.scatter(x=[i for i in range(2, 12)], y=db_score, s=150, edgecolor="k")
plt.xlabel("Davies-Bouldin score")
show()

# Expectation-maximization (Gaussian Mixture Model)

from sklearn.mixture import GaussianMixture

gm_bic = []
gm_score = []
for i in range(2, 12):
    print("i =", i)
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
plt.title("The Gaussian Mixture model BIC \nfor determining number of clusters")
plt.scatter(x=[i for i in range(2, 12)], y=np.log(gm_bic), s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("Log of Gaussian mixture BIC score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
show()

plt.scatter(x=[i for i in range(2, 12)], y=gm_score, s=150, edgecolor="k")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Hierarchical Clustering

# Dendograms

# Clustering with a shopping trend data set

df = pd.read_csv("Datasets/Mall_Customers.csv")
cc = df.head()
print(cc)

cc = df.describe()
print(cc)

plt.figure(figsize=(8, 5))
plt.title("Annual income distribution")
plt.xlabel("Annual income (k$)")
plt.hist(df["Annual Income (k$)"], color="orange", edgecolor="k")
show()

plt.figure(figsize=(8, 5))
plt.title("Spending Score distribution")
plt.xlabel("Spending Score (1-100)")
plt.hist(df["Spending Score (1-100)"], color="green", edgecolor="k")
show()

# So, is there a definitive correlation between annual income and spending score? - Apparently not

plt.figure(figsize=(8, 5))
plt.title("Annual Income and Spending Score correlation")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.scatter(
    df["Annual Income (k$)"],
    df["Spending Score (1-100)"],
    color="red",
    edgecolor="k",
    alpha=0.6,
    s=100,
)
show()

# How about correlation between age and spending score? - Apparently not

plt.figure(figsize=(8, 5))
plt.title("Age and Spending Score correlation")
plt.xlabel("Age")
plt.ylabel("Spending Score (1-100)")
plt.scatter(
    df["Age"],
    df["Spending Score (1-100)"],
    color="blue",
    edgecolor="k",
    alpha=0.6,
    s=100,
)
show()

# Strategy

# Dendograms

X = df.iloc[:, [3, 4]].values

# Ward distance matrix

import scipy.cluster.hierarchy as sch

plt.figure(figsize=(15, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
show()

# Optimal number of clusters

plt.figure(figsize=(15, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.hlines(y=190, xmin=0, xmax=2000, lw=3, linestyles="--")
plt.text(x=900, y=220, s="Horizontal line crossing 5 vertical lines")
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
show()

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
plt.title("Clustering of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.axhspan(ymin=60, ymax=100, xmin=0.4, xmax=0.96, alpha=0.3, color="yellow")
show()

wcss = []
for i in range(1, 16):
    print("i =", i)
    kmeans = KMeans(n_clusters=i, init="k-means++")
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

with plt.style.context(("fivethirtyeight")):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, 16), wcss)
    plt.title("The Elbow Method with k-means++")
    plt.xlabel("Number of clusters")
    plt.xticks()
    plt.ylabel("WCSS (within-cluster sums of squares)")
    plt.vlines(x=5, ymin=0, ymax=250000, linestyles="--")
    plt.text(
        x=5.5,
        y=110000,
        s="5 clusters seem optimal choice \nfrom the elbow position",
        fontsize=25,
        fontdict={"family": "Times New Roman"},
    )
    show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# machine_learning_Synthetic-Data-Generation1

# Synthetic Data Generation

# Regression problem generation

data1 = make_regression(
    n_samples=20,
    n_features=4,
    n_informative=2,
    n_targets=1,
    bias=0.0,
    effective_rank=None,
    tail_strength=0.5,
    noise=0.0,
    shuffle=True,
    coef=False,
    random_state=None,
)
df1 = pd.DataFrame(data1[0], columns=["x" + str(i) for i in range(1, 5)])
df1["y"] = data1[1]

cc = df1.head()
print(cc)

plt.figure(figsize=(15, 10))
for i in range(1, 5):
    print("i =", i)
    fit = np.polyfit(df1[df1.columns[i - 1]], df1["y"], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2, 2, i)
    plt.scatter(df1[df1.columns[i - 1]], df1["y"], s=200, c="orange", edgecolor="k")
    plt.plot(df1[df1.columns[i - 1]], fit_fn(df1[df1.columns[i - 1]]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Data with Gaussian noise

data2 = make_regression(
    n_samples=20,
    n_features=4,
    n_informative=2,
    n_targets=1,
    bias=0.0,
    effective_rank=None,
    tail_strength=0.5,
    noise=2.0,
    shuffle=True,
    coef=False,
    random_state=None,
)
df2 = pd.DataFrame(data2[0], columns=["x" + str(i) for i in range(1, 5)])
df2["y"] = data2[1]

plt.figure(figsize=(15, 10))
for i in range(1, 5):
    print("i =", i)
    fit = np.polyfit(df2[df2.columns[i - 1]], df2["y"], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(2, 2, i)
    plt.scatter(df2[df2.columns[i - 1]], df2["y"], s=200, c="orange", edgecolor="k")
    plt.plot(df2[df2.columns[i - 1]], fit_fn(df2[df2.columns[i - 1]]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Plot datasets with varying degree of noise

plt.figure(figsize=(15, 6))
df2 = pd.DataFrame(data=np.zeros((20, 1)))
for i in range(3):
    print("i =", i)
    data2 = make_regression(
        n_samples=20,
        n_features=1,
        n_informative=1,
        n_targets=1,
        bias=0.0,
        effective_rank=None,
        tail_strength=0.5,
        noise=i * 10,
        shuffle=True,
        coef=False,
        random_state=None,
    )
    df2["x" + str(i + 1)] = data2[0]
    df2["y" + str(i + 1)] = data2[1]

for i in range(3):
    print("i =", i)
    fit = np.polyfit(df2["x" + str(i + 1)], df2["y" + str(i + 1)], 1)
    fit_fn = np.poly1d(fit)
    plt.subplot(1, 3, i + 1)
    plt.scatter(
        df2["x" + str(i + 1)], df2["y" + str(i + 1)], s=200, c="orange", edgecolor="k"
    )
    plt.plot(df2["x" + str(i + 1)], fit_fn(df2["x" + str(i + 1)]), "b-", lw=3)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Classification problem generation

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=1.0,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

cc = df3.head()
print(cc)

from itertools import combinations

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making class separation easy by tweaking class_sep

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=3.0,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

from itertools import combinations

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making class separation hard by tweaking class_sep

data3 = make_classification(
    n_samples=20,
    n_features=4,
    n_informative=4,
    n_redundant=0,
    n_repeated=0,
    n_classes=2,
    n_clusters_per_class=1,
    weights=None,
    flip_y=0.01,
    class_sep=0.5,
    hypercube=True,
    shift=0.0,
    scale=1.0,
    shuffle=True,
    random_state=None,
)
df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
df3["y"] = data3[1]

from itertools import combinations

lst_var = list(combinations(df3.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df3[var1], df3[var2], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making data noisy by increasing flip_y

plt.figure(figsize=(18, 10))
for i in range(6):
    print("i =", i)
    data3 = make_classification(
        n_samples=20,
        n_features=4,
        n_informative=4,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=1,
        weights=None,
        flip_y=0.1 * i,
        class_sep=1.0,
        hypercube=True,
        shift=0.0,
        scale=1.0,
        shuffle=False,
        random_state=101,
    )
    df3 = pd.DataFrame(data3[0], columns=["x" + str(i) for i in range(1, 5)])
    df3["y"] = data3[1]
    plt.subplot(2, 3, i + 1)
    plt.title(f"Plot for flip_y={round(0.1*i,2)}")
    plt.scatter(df3["x1"], df3["x2"], s=200, c=df3["y"], edgecolor="k")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Plot datasets with varying degree of class separation

plt.figure(figsize=(18, 5))
df2 = pd.DataFrame(data=np.zeros((20, 1)))
for i in range(3):
    print("i =", i)
    data2 = make_classification(
        n_samples=20,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_repeated=0,
        n_classes=2,
        n_clusters_per_class=1,
        weights=None,
        flip_y=0,
        class_sep=i + 0.5,
        hypercube=True,
        shift=0.0,
        scale=1.0,
        shuffle=False,
        random_state=101,
    )
    df2["x" + str(i + 1) + "1"] = data2[0][:, 0]
    df2["x" + str(i + 1) + "2"] = data2[0][:, 1]
    df2["y" + str(i + 1)] = data2[1]

for i in range(3):
    print("i =", i)
    plt.subplot(1, 3, i + 1)
    plt.scatter(
        df2["x" + str(i + 1) + "1"],
        df2["x" + str(i + 1) + "2"],
        s=200,
        c=df2["y" + str(i + 1)],
        edgecolor="k",
    )
    plt.grid(True)

show()

print("------------------------------------------------------------")  # 60個

# Clustering problem generation

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=1.0,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making clusters compact and easily separable by tweaking cluster_std

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=0.3,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making clusters spread out and difficult to separate by tweaking cluster_std

data4 = make_blobs(
    n_samples=60,
    n_features=4,
    centers=3,
    cluster_std=2.5,
    center_box=(-5.0, 5.0),
    shuffle=True,
    random_state=None,
)
df4 = pd.DataFrame(data4[0], columns=["x" + str(i) for i in range(1, 5)])
df4["y"] = data4[1]

from itertools import combinations

lst_var = list(combinations(df4.columns[:-1], 2))
len_var = len(lst_var)
plt.figure(figsize=(18, 10))
for i in range(1, len_var + 1):
    print("i =", i)
    plt.subplot(2, math.ceil(len_var / 2), i)
    var1 = lst_var[i - 1][0]
    var2 = lst_var[i - 1][1]
    plt.scatter(df4[var1], df4[var2], s=200, c=df4["y"], edgecolor="k")
    plt.xlabel(var1)
    plt.ylabel(var2)
    plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making anisotropically distributed clustering problem

data5 = make_blobs(n_samples=50, n_features=2, centers=3, cluster_std=1.5)

transformation = [[0.5, -0.5], [-0.4, 0.8]]

data5_0 = np.dot(data5[0], transformation)
df5 = pd.DataFrame(data5_0, columns=["x" + str(i) for i in range(1, 3)])
df5["y"] = data5[1]

plt.figure(figsize=(8, 5))
plt.scatter(df5["x1"], df5["x2"], c=df5["y"], s=200, edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Making concentric circle clusters

data6 = make_circles(
    n_samples=50, shuffle=True, noise=None, random_state=None, factor=0.6
)
df6 = pd.DataFrame(data6[0], columns=["x" + str(i) for i in range(1, 3)])
df6["y"] = data6[1]

plt.figure(figsize=(8, 5))
plt.scatter(df6["x1"], df6["x2"], c=df6["y"], s=200, edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Introdue noise in the circle clusters

data6 = make_circles(
    n_samples=50, shuffle=True, noise=0.15, random_state=None, factor=0.6
)
df6 = pd.DataFrame(data6[0], columns=["x" + str(i) for i in range(1, 3)])
df6["y"] = data6[1]

plt.figure(figsize=(8, 5))
plt.scatter(df6["x1"], df6["x2"], c=df6["y"], s=200, edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Make moon shape clusters

data7 = make_moons(n_samples=50, shuffle=True, noise=None, random_state=None)
df7 = pd.DataFrame(data7[0], columns=["x" + str(i) for i in range(1, 3)])
df7["y"] = data7[1]

plt.figure(figsize=(8, 5))
plt.scatter(df7["x1"], df7["x2"], c=df7["y"], s=200, edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個

# Introduce noise in the moon-shaped clusters

data7 = make_moons(n_samples=50, shuffle=True, noise=0.1, random_state=None)
df7 = pd.DataFrame(data7[0], columns=["x" + str(i) for i in range(1, 3)])
df7["y"] = data7[1]

plt.figure(figsize=(8, 5))
plt.scatter(df7["x1"], df7["x2"], c=df7["y"], s=200, edgecolors="k")
plt.xlabel("x1")
plt.ylabel("x2")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Generate name, address, phone number, email etc. using pydbgen package

from pydbgen import pydbgen

generator = pydbgen.pydb()

# Generate a license-plate (US style)
cc = generator.license_plate()
print(cc)
# 'OKY-2318'

""" NG
# Generate few random names
cc = generator.gen_data_series(num=10,data_type='name')
print(cc)
"""

# Generate random phone numbers
cc = generator.simple_ph_num()
print(cc)

# '389-066-8154'
""" NG
cc = generator.gen_data_series(num=10,data_type='phone_number_full')
print(cc)
"""
# Generate a full data frame with random name, street address, SSN, email, date
""" NG
df10 = generator.gen_dataframe(fields=['name','street_address','ssn','email','date'])
print(df10)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
Synth_Time_series
"""

# machine_learning_Synth_Time_series

# Synthesizing time series data

# Functions


# cylinder bell funnel based on "Learning comprehensible descriptions of multivariate time series"
def generate_bell(length, amplitude, default_variance):
    bell = (
        np.random.normal(0, default_variance, length)
        + amplitude * np.arange(length) / length
    )
    return bell


def generate_funnel(length, amplitude, default_variance):
    funnel = (
        np.random.normal(0, default_variance, length)
        + amplitude * np.arange(length)[::-1] / length
    )
    return funnel


def generate_cylinder(length, amplitude, default_variance):
    cylinder = np.random.normal(0, default_variance, length) + amplitude
    return cylinder


std_generators = [generate_bell, generate_funnel, generate_cylinder]


def generate_pattern_data(
    length=100,
    avg_pattern_length=5,
    avg_amplitude=1,
    default_variance=1,
    variance_pattern_length=10,
    variance_amplitude=2,
    generators=std_generators,
    include_negatives=True,
):
    data = np.random.normal(0, default_variance, length)
    current_start = random.randint(0, avg_pattern_length)
    current_length = current_length = max(
        1, math.ceil(random.gauss(avg_pattern_length, variance_pattern_length))
    )

    while current_start + current_length < length:
        generator = random.choice(generators)
        current_amplitude = random.gauss(avg_amplitude, variance_amplitude)

        while current_length <= 0:
            current_length = -(current_length - 1)
        pattern = generator(current_length, current_amplitude, default_variance)

        if include_negatives and random.random() > 0.5:
            pattern = -1 * pattern

        data[current_start : current_start + current_length] = pattern

        current_start = (
            current_start + current_length + random.randint(0, avg_pattern_length)
        )
        current_length = max(
            1, math.ceil(random.gauss(avg_pattern_length, variance_pattern_length))
        )

    return np.array(data)


# Generate time series and plot

n_data = [50, 150, 500]
n_pattern_length = [5, 10, 20]

from itertools import product

config_ = list(product(n_data, n_pattern_length))

fig, axes = plt.subplots(nrows=3, ncols=3, figsize=(12, 9))
ax = axes.ravel()
i = 0
for n1, n2 in config_:
    data = generate_pattern_data(length=n1, avg_pattern_length=n2)
    ax[i].plot(data, color="k")
    ax[i].grid(True)
    i += 1
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Time-profiling

# Time-profiling Data Science code using cProfile

import cProfile

SIZE = 10_000_000
a = np.arange(SIZE)
b = np.random.normal(size=SIZE)

cProfile.run("a+b")

print("------------------------------")  # 60個

code = """SIZE = 10_000_000
a = np.arange(SIZE)
b = np.random.normal(size=SIZE)
a+b"""

print(code)

cProfile.run(code)

print("------------------------------")  # 60個


def add():
    SIZE = 10_000_000
    a = np.arange(SIZE)
    b = np.random.normal(size=SIZE)
    c = a + b


cProfile.run("add()")

print("------------------------------")  # 60個


def add(size):
    a = np.arange(size)
    b = np.random.normal(size=size)
    c = a + b


SIZE = 10_000_000
cProfile.run("add(SIZE)")

print("------------------------------")  # 60個

SIZE = 20_000_000
cProfile.run("add(SIZE)")

print("------------------------------")  # 60個


def ops(a, b):
    x1 = a + b
    x2 = a - b
    x3 = a * b
    x4 = a / b


cProfile.run("ops(a,b)")

print("------------------------------")  # 60個

import cProfile
import pstats

profiler = cProfile.Profile()
# Enable profiler
profiler.enable()
# Function execution
add(SIZE)
# Disable profiler
profiler.disable()
# pstats
stats = pstats.Stats(profiler)
# Print the total time and function calls
print("Total function calls:", stats.total_calls)
print("Total time (seconds):", stats.total_tt)

# Total function calls: 48
# Total time (seconds): 1.1839559

stats = pstats.Stats(profiler)
stats.print_stats()

type(stats)

# pstats.Stats

stats.total_tt

# 1.1839559

stats.fcn_list

size = [int(i * 1e6) for i in range(5, 26, 5)]
total_tt = []
for s in size:
    profiler = cProfile.Profile()
    profiler.enable()
    add(s)
    profiler.disable()
    stats = pstats.Stats(profiler)
    total_tt.append(round(stats.total_tt, 3))

total_tt

[0.274, 0.464, 0.706, 0.94, 1.187]

plt.figure(figsize=(6, 3), dpi=120)
plt.bar(
    x=[str(i) + "-million" for i in range(5, 26, 5)],
    height=total_tt,
    edgecolor="k",
    color="#2c75b0",
)
plt.xlabel("Array size")
plt.ylabel("Time taken (seconds)")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Timing-decorator-ML-optimization

from functools import wraps
from time import time, sleep
from sklearn.ensemble import RandomForestClassifier

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
    # 資料分割
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33)
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

cc = classifier_accuracy(log_model, x, y)
print(cc)
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
ax[0].set_title("Accuracy score with data size")
ax[0].set_xlabel("Data size")
ax[0].grid(True)
ax[1].scatter(SIZE, model_time, edgecolor="k", s=100)
ax[1].plot(SIZE, model_time)
ax[1].set_title("Training time (msec) with data size")
ax[1].set_xlabel("Data size")
ax[1].grid(True)
show()

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
ax[0].set_title("Accuracy score with Random Forest")
ax[0].set_xlabel("Number of trees")
ax[0].grid(True)
ax[1].scatter(num_trees, model_time, edgecolor="k", s=100)
ax[1].plot(num_trees, model_time)
ax[1].set_title("Training time (msec) with Random Forest")
ax[1].set_xlabel("Number of trees")
ax[1].grid(True)
show()

model_time = np.array(model_time)
model_acc = np.array(model_acc)
model_opt = model_acc + 1 / model_time

plt.figure(dpi=120)
plt.title("Model optimization with number of trees")
plt.plot(num_trees, model_opt)
plt.scatter(num_trees, model_opt, s=100, edgecolor="k")
plt.xlabel("Number of trees")
plt.grid(True)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# machine_learning_regression01

# Linear_Regression_Methods
# Linear regression with various methods
"""
This is a very simple example of using two scipy tools for linear regression.
    Scipy.Polyfit
    Stats.linregress
    Optimize.curve_fit
    numpy.linalg.lstsq
    statsmodels.OLS
    Analytic solution using Moore-Penrose generalized inverse or simple multiplicative matrix inverse
    sklearn.linear_model.LinearRegression
"""
from numpy import linspace, polyval, polyfit, sqrt  # , stats, randn, optimize
from scipy import stats, optimize
import statsmodels.api as sm

# Generate random data of a sufficiently large size

# Sample data creation
# number of points
n = int(5e6)
t = np.linspace(-10, 10, n)
# parameters
a = 3.25
b = -6.5
x = polyval([a, b], t)
# add some noise
xn = x + 3 * np.random.randn(n)

# Draw few random sample points and plot

xvar = np.random.choice(t, size=20)
yvar = polyval([a, b], xvar) + 3 * np.random.randn(20)
plt.scatter(xvar, yvar, c="green", edgecolors="k")
plt.grid(True)
show()

# Method: Scipy.Polyfit

# Linear regressison -polyfit - polyfit can be used other orders polynomials
(ar, br) = polyfit(t, xn, 1)
xr = polyval([ar, br], t)
# compute the mean square error
err = sqrt(sum((xr - xn) ** 2) / n)

print("Linear regression using polyfit")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))

# Method: Stats.linregress

# Linear regression using stats.linregress
(a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)

print("Linear regression using stats.linregress")
print("a=%.2f b=%.2f, std error= %.3f, r^2 coefficient= %.3f" % (a_s, b_s, stderr, r))

# Method: Optimize.curve_fit


def flin(t, a, b):
    result = a * t + b
    return result


p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")

print("Linear regression using optimize.curve_fit")
print("parameters: a=%.2f b=%.2f" % (p1[0], p1[1]))

# Method: numpy.linalg.lstsq

A = np.vstack([t, np.ones(len(t))]).T
result = np.linalg.lstsq(A, xn)
ar, br = result[0]
err = np.sqrt(result[1] / len(xn))

print("Linear regression using numpy.linalg.lstsq")
print("parameters: a=%.2f b=%.2f, ms error= %.3f" % (ar, br, err))

# Method: Statsmodels.OLS

t = sm.add_constant(t)
model = sm.OLS(x, t)
results = model.fit()
ar = results.params[1]
br = results.params[0]

print("Linear regression using statsmodels.OLS")
print("parameters: a=%.2f b=%.2f" % (ar, br))

print(results.summary())

# Analytic solution using Moore-Penrose pseudoinverse

mpinv = np.linalg.pinv(t)
result = mpinv.dot(x)
ar = result[1]
br = result[0]

print("Linear regression using Moore-Penrose inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))

# Analytic solution using simple multiplicative matrix inverse

m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
ar = m[1]
br = m[0]

print("Linear regression using simple inverse")
print("parameters: a=%.2f b=%.2f" % (ar, br))

# Method: sklearn.linear_model.LinearRegression

lm = LinearRegression()
lm.fit(t, x)
ar = lm.coef_[1]
br = lm.intercept_

print("Linear regression using sklearn.linear_model.LinearRegression")
print("parameters: a=%.2f b=%.2f" % (ar, br))

n_min = 50000
n_max = int(1e7)
n_levels = 25
r = np.log10(n_max / n_min)
l = np.linspace(0, r, n_levels)
n_data = list((n_min * np.power(10, l)))
n_data = [int(n) for n in n_data]

""" NG somewhere
for i in range(len(n_data)):
    print("i =", i)
    t = np.linspace(-10, 10, n_data[i])
    # parameters
    a = 3.25
    b = -6.5
    x = polyval([a, b], t)
    # add some noise
    xn = x + 3 * np.random.randn(n_data[i])

    # Linear regressison -polyfit - polyfit can be used other orders polynomials
    (ar, br) = polyfit(t, xn, 1)

    # Linear regression using stats.linregress
    (a_s, b_s, r, tt, stderr) = stats.linregress(t, xn)

    # Linear regression using optimize.curve_fit
    p1, _ = optimize.curve_fit(flin, xdata=t, ydata=xn, method="lm")

    # Linear regression using np.linalg.lstsq (solving Ax=B equation system)
    A = np.vstack([t, np.ones(len(t))]).T
    result = np.linalg.lstsq(A, xn)
    ar, br = result[0]

    # Linear regression using statsmodels.OLS
    t = sm.add_constant(t)
    model = sm.OLS(x, t)
    results = model.fit()
    ar = results.params[1]
    br = results.params[0]

    # Linear regression using Moore-Penrose pseudoinverse matrix
    mpinv = np.linalg.pinv(t)
    result = mpinv.dot(x)
    ar = result[1]
    br = result[0]

    # Linear regression using simple multiplicative inverse matrix
    m = np.dot((np.dot(np.linalg.inv(np.dot(t.T, t)), t.T)), x)
    ar = m[1]
    br = m[0]

    # Linear regression using scikit-learn's linear_model
    lm = LinearRegression()
    lm.fit(t, x)
    ar = lm.coef_[1]
    br = lm.intercept_
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear_Regression_Practice
# Linear Regrssion on US Housing Price

df = pd.read_csv("data/USA_Housing.csv")

cc = df.head()
print(cc)

# Check basic info on the data set

df.info(verbose=True)

# 'describe()' method to get the statistical summary of the various features of the data set

df.describe(percentiles=[0.1, 0.25, 0.5, 0.75, 0.9])

#'columns' method to get the names of the columns (features)

df.columns

# Basic plotting and visualization on the data set

# Pairplots using seaborn

sns.pairplot(df)
show()

# Distribution of price (the predicted quantity)

df["Price"].plot.hist(bins=25, figsize=(8, 4))

show()

df["Price"].plot.density()

show()

# Correlation matrix and heatmap

""" NG
df.corr()

plt.figure(figsize=(10,7))
sns.heatmap(df.corr(),annot=True,linewidths=2)

show()
"""

# Feature and variable sets

# Make a list of data frame column names

l_column = list(df.columns)  # Making a list out of column names
len_feature = len(l_column)  # Length of column vector list
l_column

# Put all the numerical features in X and Price in y, ignore Address which is string for linear regression

X = df[l_column[0 : len_feature - 2]]
y = df[l_column[len_feature - 2]]

print("Feature set size:", X.shape)
print("Variable set size:", y.shape)

cc = X.head()
print(cc)

cc = y.head()
print(cc)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

print("Training feature set size:", X_train.shape)
print("Test feature set size:", X_test.shape)
print("Training variable set size:", y_train.shape)
print("Test variable set size:", y_test.shape)

lm = LinearRegression()  # Creating a Linear Regression object 'lm'

# Fit the model on to the instantiated object itself

lm.fit(
    X_train, y_train
)  # Fit the linear model on to the 'lm' object itself i.e. no need to set this to another variable

# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)

# Check the intercept and coefficients and put them in a DataFrame

print("The intercept term of the linear model:", lm.intercept_)

# The intercept term of the linear model: -2631028.90175

print("The coefficients of the linear model:", lm.coef_)

# idict = {'Coefficients':lm.intercept_}
# idf = pd.DataFrame(data=idict,index=['Intercept'])
cdf = pd.DataFrame(data=lm.coef_, index=X_train.columns, columns=["Coefficients"])
# cdf=pd.concat([idf,cdf], axis=0)
cdf

# Calculation of standard errors and t-statistic for the coefficients

n = X_train.shape[0]
k = X_train.shape[1]
dfN = n - k
train_pred = lm.predict(X_train)
train_error = np.square(train_pred - y_train)
sum_error = np.sum(train_error)
se = [0, 0, 0, 0, 0]
for i in range(k):
    print("i =", i)
    r = sum_error / dfN
    r = r / np.sum(
        np.square(
            X_train[list(X_train.columns)[i]] - X_train[list(X_train.columns)[i]].mean()
        )
    )
    se[i] = np.sqrt(r)
cdf["Standard Error"] = se
cdf["t-statistic"] = cdf["Coefficients"] / cdf["Standard Error"]
cdf

print(
    "Therefore, features arranged in the order of importance for predicting the house price",
    "-" * 90,
    sep="",
)
l = list(cdf.sort_values("t-statistic", ascending=False).index)
print(" > \n".join(l))

l = list(cdf.index)

from matplotlib import gridspec

fig = plt.figure(figsize=(14, 8))

gs = gridspec.GridSpec(2, 3)
# f, ax = plt.subplots(nrows=1,ncols=len(l), sharey=True)
ax0 = plt.subplot(gs[0])
ax0.scatter(df[l[0]], df["Price"])
ax0.set_title(l[0] + " vs. Price", fontdict={"fontsize": 20})

ax1 = plt.subplot(gs[1])
ax1.scatter(df[l[1]], df["Price"])
ax1.set_title(l[1] + " vs. Price", fontdict={"fontsize": 20})

ax2 = plt.subplot(gs[2])
ax2.scatter(df[l[2]], df["Price"])
ax2.set_title(l[2] + " vs. Price", fontdict={"fontsize": 20})

ax3 = plt.subplot(gs[3])
ax3.scatter(df[l[3]], df["Price"])
ax3.set_title(l[3] + " vs. Price", fontdict={"fontsize": 20})

ax4 = plt.subplot(gs[4])
ax4.scatter(df[l[4]], df["Price"])
ax4.set_title(l[4] + " vs. Price", fontdict={"fontsize": 20})

show()

# R-square of the model fit

print("R-squared value of this fit:", round(metrics.r2_score(y_train, train_pred), 3))

# R-squared value of this fit: 0.917

# Prediction, error estimate, and regression evaluation matrices

# Prediction using the lm model

predictions = lm.predict(X_test)
print("Type of the predicted object:", type(predictions))
print("Size of the predicted object:", predictions.shape)

# Scatter plot of predicted price and y_test set to see if the data fall on a 45 degree straight line

plt.figure(figsize=(10, 7))
plt.title("Actual vs. predicted house prices")
plt.xlabel("Actual test set house prices")
plt.ylabel("Predicted house prices")
plt.scatter(x=y_test, y=predictions)

show()

# Plotting histogram of the residuals i.e. predicted errors (expect a normally distributed pattern)

plt.figure(figsize=(10, 7))
plt.title("Histogram of residuals to check for normality")
plt.xlabel("Residuals")
plt.ylabel("Kernel density")
sns.distplot([y_test - predictions])

show()

# Scatter plot of residuals and predicted values (Homoscedasticity)

plt.figure(figsize=(10, 7))
plt.title("Residuals vs. predicted values plot (Homoscedasticity)")
plt.xlabel("Predicted house prices")
plt.ylabel("Residuals")
plt.scatter(x=predictions, y=y_test - predictions)

show()

# Regression evaluation metrices

print("Mean absolute error (MAE):", metrics.mean_absolute_error(y_test, predictions))
print("Mean square error (MSE):", metrics.mean_squared_error(y_test, predictions))
print(
    "Root mean square error (RMSE):",
    np.sqrt(metrics.mean_squared_error(y_test, predictions)),
)

# R-square value

print(
    "R-squared value of predictions:", round(metrics.r2_score(y_test, predictions), 3)
)

# R-squared value of predictions: 0.919

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Linear regression as a statistical estimation problem

df = pd.read_csv("data/slump_test.csv", sep=",")

df.drop("No", axis=1, inplace=True)

cc = df.head()
print(cc)

print(df.shape)
# (103, 10)

"""
# Import MyLinearRegression from MLR and fit

from mlr.MLR import MyLinearRegression as mlr

m = mlr()

predictors = list(df.columns[:7])

print(predictors)

response = 'Compressive Strength (28-day)(Mpa)'

m.fit_dataframe(X=predictors,y=response,dataframe=df)

# Print all the coefficients and the intercept

m.coef_

m.intercept_

# 139.7814998489339

# Print metrics

print ("R-squared: ",m.r_squared())
print ("Adjusted R-squared: ",m.adj_r_squared())
print("MSE: ",m.mse())

# All metrics at once!

cc = m.print_metrics()
print(cc)

n = df.shape[0]
p = df.shape[1]-3

r2 = 1-(m.sse()/m.sst())
adjr2 = 1 - (m.sse()/m.sst())*((n-1)/(n-p-1))

print("R^2 from first principles:",round(r2,4))
print("Adjusted-R^2 from first principles:",round(adjr2,4))

#R^2 from first principles: 0.8968
#Adjusted-R^2 from first principles: 0.8892

#AIC and BIC

# AIC : Akaike information criterion
# BIC : Bayesian information criterion

# Residuals plots

m.fitted_vs_residual()

m.fitted_vs_features()

# Histogram and Q-Q plot of the standardized residuals

m.histogram_resid()

m.qqplot_resid()

# F-test of overall significance

cc = m.ftest()
print(cc)
# (117.98260528684814, 5.444633963386908e-44)

# Standard errors, t-statistic, p-values

print("Standard errors:",m.std_err())
print()
print("t-test values:",m.tvalues())
print()
print("P-values:",m.pvalues())

for i in range(7):
    print("i =", i)
    print(f"Predictor: {df.columns[i]}, Standard error: {m.std_err()[i+1]}, t-statistic: {m.tvalues()[i+1]}, p-value: {m.pvalues()[i+1]}")

# We can print the confidence interval of the regression coefficients directly

m.conf_int()[1:]

# If we change the statistical significance level to 0.01 from 0.05, then two more variables show range including zero

m.conf_int(alpha=0.01)[1:]

# Now, we can build a model removing those three variables who showed p-val > 0.05

m2 = mlr()

predictors = ['Cement', 'Fly ash', 'Water', 'Coarse Aggr.']

m2.fit_dataframe(X=predictors,y=response,dataframe=df)

print("Metrics of the old (full) model\n"+"-"*40)
m.print_metrics()

print("Metrics of the new (smaller) model\n"+"-"*40)
m2.print_metrics()

# We can also plot something called Cook's distance plot to see if there is any outliers in the data

m.cook_distance()

# We can plot the full pairwise scatterplots

m.pairplot()

# This may take a little time. Have patience...

# You can also use Seaborn library for visualization like pairplots and correlation heatmaps

sns.pairplot(data=df[df.columns[:7]])
show()

corr = np.corrcoef(df[df.columns[:7]],rowvar=False)
plt.figure(figsize=(10,10))
sns.heatmap(data=corr,linewidths=1,annot=True)
show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Robust linear regression

# Creating a regression problem using make_regression method

rng = np.random.RandomState(0)

X, y, coef = make_regression(
    n_samples=200, n_features=2, noise=4.0, coef=True, random_state=0
)

# Plot

fix, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].scatter(X[:, 0], y)
ax[0].grid(True)
ax[1].scatter(X[:, 1], y)
ax[1].grid(True)
show()

# Inserting random outliers in the data

X[:4] = rng.uniform(10, 20, (4, 2))
y[:4] = rng.uniform(100, 200, 4)

# Plot to show the inserted outliers

fix, ax = plt.subplots(1, 2, figsize=(10, 3))
ax[0].scatter(X[:, 0], y)
ax[0].grid(True)
ax[1].scatter(X[:, 1], y)
ax[1].grid(True)
show()

# Create a HuberRegressor object and fit

huber = HuberRegressor()

huber.fit(X, y)

cc = X[1].reshape(1, -1)
print(cc)

cc = huber.predict(X[1].reshape(1, -1))
print(cc)

# A simple linear regression fit for comparison

linear = LinearRegression()

linear.fit(X, y)

# Compare the estimated coefficients

print("True coefficients:", coef)
print("Huber coefficients:", huber.coef_)
print("Linear Regression coefficients:", linear.coef_)

fix, ax = plt.subplots(1, 2, figsize=(12, 3), sharey=True)
ax[0].barh(
    ["True coef", "Huber coef", "Linear fit coef"],
    width=[coef[0], huber.coef_[0], linear.coef_[0]],
)
ax[0].set_title("1st coefficients")
ax[1].barh(
    ["True coef", "Huber coef", "Linear fit coef"],
    width=[coef[1], huber.coef_[1], linear.coef_[1]],
)
ax[1].set_title("2nd coefficients")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Support vector regression

# A simple nonlinear function


def nonlinear(array):
    return (
        10 * array[:, 0] - np.exp(0.01 * array[:, 1] + np.log(1 + array[:, 2] ** 2))
    ) / (array[:, 3] ** 2 + 5)


# Generate features and target data for regression

n_samples = 200
n_features = 4

x = 5 * np.random.rand(n_samples, n_features)

y = nonlinear(x) + np.random.randn(n_samples)

y = y.reshape(n_samples, 1)

df = pd.DataFrame(data=np.hstack((x, y)), columns=["X1", "X2", "X3", "X4", "y"])

cc = df.head()
print(cc)

# Plotting the data

fig, ax = plt.subplots(2, 2, figsize=(10, 8))
ax = ax.ravel()
for i in range(4):
    print("i =", i)
    ax[i].scatter(df[df.columns[i]], df["y"], edgecolor="k", color="red", alpha=0.75)
    ax[i].set_title(f"{df.columns[i]} vs. y")
    ax[i].grid(True)
show()

X = df[["X1", "X2", "X3", "X4"]]
y = df["y"]

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Support vector regressor with linear kernel

from sklearn.svm import SVR

svr_linear = SVR(kernel="linear", gamma="scale", C=1.0, epsilon=0.1)
svr_linear.fit(X_train, y_train)

# Test score

svr_linear.score(X_test, y_test)

# 0.5039103904226544

# Linear regression as a baseline

linear = LinearRegression()

linear.fit(X_train, y_train)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None)

linear.score(X_test, y_test)

# 0.5131204583471316

# Support vector regressor with Gaussian (radial basis function) kernel

svr_rbf = SVR(kernel="rbf", gamma="scale", C=1.0, epsilon=0.1)
svr_rbf.fit(X_train, y_train)

svr_rbf.score(X_test, y_test)

# 0.6473177483091139

# So, clearly, the RBF kernel showed better accuracy on the test set

print(
    "RMSE for linear SVR:",
    np.sqrt(mean_squared_error(y_test, svr_linear.predict(X_test))),
)
print(
    "RMSE for RBF kernelized SVR:",
    np.sqrt(mean_squared_error(y_test, svr_rbf.predict(X_test))),
)

# We can do a grid search of hyperparameters (with 5-fold cross-validation) to see if the test/validation score be improved

from sklearn.model_selection import GridSearchCV

params = {"C": [0.01, 0.05, 0.1, 0.5, 1, 2, 5], "epsilon": [0.1, 0.2, 0.5, 1]}

grid = GridSearchCV(
    svr_rbf, param_grid=params, cv=5, scoring="r2", verbose=1, return_train_score=True
)

grid.fit(X_train, y_train)

# Fitting 5 folds for each of 28 candidates, totalling 140 fits

# Check which was deemed best estimator by the grid search

cc = grid.best_estimator_
print(cc)

# Fit that estimator to the data and see

svr_best = SVR(kernel="rbf", gamma="scale", C=5.0, epsilon=0.5)
svr_best.fit(X_train, y_train)

svr_best.score(X_test, y_test)

# 0.6776661577094625

print(
    "RMSE for RBF kernelized SVR:",
    np.sqrt(mean_squared_error(y_test, svr_best.predict(X_test))),
)

# RMSE for RBF kernelized SVR: 1.163125361525394

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Regression_Diagnostics

# Visual analytics and diagnostics of model fit for linear regression

import statsmodels.formula.api as sm

# The dataset path may be different in your situation. Please use the correct path
df = pd.read_excel("data/Concrete_Data.xls")

cc = df.head()
print(cc)

cc = df.describe().T
print(cc)

# Taking a peek at the relationship between the predicting variables and the response

for c in df.columns[:-1]:
    print(c)
    plt.figure(figsize=(8, 5))
    plt.title("{} vs. \nConcrete Compressive Strength".format(c))
    plt.scatter(
        x=df[c],
        y=df["Concrete compressive strength(MPa, megapascals) "],
        color="blue",
        edgecolor="k",
    )
    plt.grid(True)
    plt.xlabel(c)
    plt.ylabel("Concrete compressive strength\n(MPa, megapascals)")
    show()

# Creating a copy with suitable column names for processing with statsmodels.OLS()

df1 = df.copy()

df1.columns = ["Component" + str(i) for i in range(1, 8)] + ["Age"] + ["y"]

cc = df1.head()
print(cc)

# Pairwise scatter plots

from seaborn import pairplot

pairplot(df1)
show()

# Correlation matrix and heatmap to visually check for multicollinearity

corr = df1[:-1].corr()

print(corr)

from statsmodels.graphics.correlation import plot_corr

fig = plot_corr(corr, xnames=corr.columns)
show()

# Creating a formula string for using in the statsmodels.OLS()

formula_str = df1.columns[-1] + " ~ " + "+".join(df1.columns[:-1])

print(formula_str)

# "y ~ Component1+Component2+Component3+Component4+Component5+Component6+Component7+Age"

# Construct and fit the model. Print summary of the fitted model

model = sm.ols(formula=formula_str, data=df1)

fitted = model.fit()

print("檢視模型架構")
fitted.summary()  # 檢視模型架構

# A new Result dataframe: p-values and statistical significance of the features

df_result = pd.DataFrame()

df_result["pvalues"] = fitted.pvalues[1:]

df_result["Features"] = df.columns[:-1]

df_result.set_index("Features", inplace=True)


def yes_no(b):
    if b:
        return "Yes"
    else:
        return "No"


df_result["Statistically significant?"] = df_result["pvalues"].apply(yes_no)

print(df_result)

# Residuals vs. predicting variables plots

for c in df.columns[:-1]:
    print(c)
    plt.figure(figsize=(8, 5))
    plt.title("{} vs. \nModel residuals".format(c))
    plt.scatter(x=df[c], y=fitted.resid, color="blue", edgecolor="k")
    plt.grid(True)
    xmin = min(df[c])
    xmax = max(df[c])
    plt.hlines(y=0, xmin=xmin * 0.9, xmax=xmax * 1.1, color="red", linestyle="--", lw=3)
    plt.xlabel(c)
    plt.ylabel("Residuals")
    show()

# Residual plots show some bit of clustering but overall the assumptions linearity and independence seem to hold because the distribution seem random around the 0 axis.

# Fitted vs. residuals

plt.figure(figsize=(8, 5))
p = plt.scatter(x=fitted.fittedvalues, y=fitted.resid, edgecolor="k")
xmin = min(fitted.fittedvalues)
xmax = max(fitted.fittedvalues)
plt.hlines(y=0, xmin=xmin * 0.9, xmax=xmax * 1.1, color="red", linestyle="--", lw=3)
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Fitted vs. residuals plot")
plt.grid(True)
show()

# The fitted vs. residuals plot shows violation of the constant variance assumption - Heteroscedasticity.

# Histogram of normalized residuals

plt.figure(figsize=(8, 5))
plt.hist(fitted.resid_pearson, bins=20, edgecolor="k")
plt.ylabel("Count")
plt.xlabel("Normalized residuals")
plt.title("Histogram of normalized residuals")
show()

# Q-Q plot of the residuals

from statsmodels.graphics.gofplots import qqplot

plt.figure(figsize=(8, 5))
fig = qqplot(fitted.resid_pearson, line="45", fit="True")
plt.xticks()
plt.yticks()
plt.xlabel("Theoretical quantiles")
plt.ylabel("Sample quantiles")
plt.title("Q-Q plot of normalized residuals")
plt.grid(True)
show()

# The Q-Q plot (and the histogram above) shows that the normality assumption is satisfied pretty good

# Normality (Shapiro-Wilk) test of the residuals

from scipy.stats import shapiro

_, p = shapiro(fitted.resid)

if p < 0.01:
    print("The residuals seem to come from Gaussian process")
else:
    print("The normality assumption may not hold")

# The residuals seem to come from Gaussian process

# Cook"s distance (checking for outliers in residuals)

from statsmodels.stats.outliers_influence import OLSInfluence as influence

inf = influence(fitted)

(c, p) = inf.cooks_distance
plt.figure(figsize=(8, 5))
plt.title("Cook's distance plot for the residuals")
plt.stem(np.arange(len(c)), c, markerfmt=",")
plt.grid(True)
show()

# There are few data points with residuals being possible outliers

# Variance inflation factor

from statsmodels.stats.outliers_influence import variance_inflation_factor as vif

for i in range(len(df1.columns[:-1])):
    print("i =", i)
    v = vif(np.matrix(df1[:-1]), i)
    print("Variance inflation factor for {}: {}".format(df.columns[i], round(v, 2)))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Ridge/LASSO polynomial regression with linear and random sampling

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

from sklearn.ensemble import AdaBoostRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(df["X"], df["y"], test_size=0.2)

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
    print("Test score of model with degree {}: {}".format(degree, test_score))

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

print(linear_sample_score)

# 資料分割
X_train, X_test, y_train, y_test = train_test_split(
    df["X_sampled"], df["y_sampled"], test_size=0.2
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

    print("Test score of model with degree {}: {}".format(degree, test_score))

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


# Cehcking the regularization strength from the cross-validated model pipeline

m = model.steps[1][1]
print(m.alpha_)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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
