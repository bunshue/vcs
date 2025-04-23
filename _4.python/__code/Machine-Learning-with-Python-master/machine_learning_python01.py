"""
machine_learning_python01

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


"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Linear Regression and Regularization

N_samples = 25
x_min = -5
x_max = 5
x1= np.linspace(x_min,x_max,N_samples*5)
x= np.random.choice(x1,size=N_samples)
noise_std=1
noise_mean=0
noise_magnitude = 2

x1= np.linspace(x_min,x_max,N_samples*5)
x= np.random.choice(x1,size=N_samples)
y=2*x-0.6*x**2+0.2*x**3+18*np.sin(x)
y1=2*x1-0.6*x1**2+0.2*x1**3+18*np.sin(x1)
y= y+noise_magnitude*np.random.normal(loc=noise_mean,scale=noise_std,size=N_samples)
plt.figure(figsize=(8,5))
plt.plot(x1,y1,c='k',lw=2)
plt.scatter(x,y,edgecolors='k',c='yellow',s=60)
plt.grid(True)

show()

#return (x,y,x1,y1)

# Extract the data

# x,y,x1,y1 = p.result

# Load scikit-learn libraries

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

# Machine learning (regression) model encapsulated within a function

lasso_eps = 0.01
lasso_nalpha=20
lasso_iter=3000
ridge_alphas = (0.001,0.01,0.1,1)

def func_fit(model_type,test_size,degree):
    X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=test_size,random_state=55)
    
    t1=np.min(X_test)
    t2=np.max(X_test)
    t3=np.min(y_test)
    t4=np.max(y_test)
    
    t5=np.min(X_train)
    t6=np.max(X_train)
    t7=np.min(y_train)
    t8=np.max(y_train)
    
    posx_test=t1+(t2-t1)*0.7
    posx_train=t5+(t6-t5)*0.7
    posy_test=t3+(t4-t3)*0.2
    posy_train=t7+(t8-t7)*0.2
    
    if (model_type=='Linear regression'):
        model = make_pipeline(PolynomialFeatures(degree,interaction_only=False), 
                          LinearRegression())
    if (model_type=='LASSO with CV'):    
        model = make_pipeline(PolynomialFeatures(degree,interaction_only=False), 
                              LassoCV(eps=lasso_eps,n_alphas=lasso_nalpha,max_iter=lasso_iter,cv=5))
        
    if (model_type=='Ridge with CV'):    
        model = make_pipeline(PolynomialFeatures(degree,interaction_only=False), 
                              RidgeCV(alphas=ridge_alphas,cv=5))
    
    X_train=X_train.reshape(-1,1)
    X_test=X_test.reshape(-1,1)
    
    model.fit(X_train,y_train)
    
    train_pred = np.array(model.predict(X_train))
    train_score = model.score(X_train,y_train)
    
    test_pred = np.array(model.predict(X_test))
    test_score = model.score(X_test,y_test)
    
    RMSE_test=np.sqrt(np.mean(np.square(test_pred-y_test)))
    RMSE_train=np.sqrt(np.mean(np.square(train_pred-y_train)))
    
    print("Test score: {}, Training score: {}".format(test_score,train_score))
    
    print("RMSE Test: {}, RMSE train: {}".format(RMSE_test,RMSE_train))
    
    plt.figure(figsize=(12,4))
    
    plt.subplot(1,2,1)
    plt.title("Test set performance\n",fontsize=16)
    plt.xlabel("X-test",fontsize=13)
    plt.ylabel("y-test",fontsize=13)
    plt.scatter(X_test,y_test,edgecolors='k',c='blue',s=60)
    plt.scatter(X_test,test_pred,edgecolors='k',c='yellow',s=60)
    plt.grid(True)
    plt.legend(['Actual test values','Predicted values'])
    plt.text(x=posx_test,y=posy_test,s='Test score: %.3f'%(test_score),fontsize=15)
    
    plt.subplot(1,2,2)
    plt.title("Training set performance\n",fontsize=16)
    plt.xlabel("X-train",fontsize=13)
    plt.ylabel("y-train",fontsize=13)
    plt.scatter(X_train,y_train,c='blue')
    plt.scatter(X_train,train_pred,c='yellow')
    plt.grid(True)
    plt.legend(['Actual training values','Fitted values'])
    plt.text(x=posx_train,y=posy_train,s='Training score: %.3f'%(train_score),fontsize=15)
    
    plt.show()
       
    return (train_score,test_score)    


model_type='Linear regression'
model_type='LASSO with CV'
model_type='Ridge with CV'

test_size = 0.2
degree = 3

func_fit(model_type,test_size,degree)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs

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

plt.figure(figsize=(21, 35))
for i in range(1, 29):
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
plt.figure(figsize=(21, 15))

for i, c in enumerate(df1.columns):
    plt.subplot(3, 3, i + 1)
    sns.boxplot(y=df1[c], x=data1[1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Class", fontsize=15)
    plt.ylabel(c, fontsize=15)

show()

print("------------------------------")  # 30個

# k-means clustering
from sklearn.cluster import KMeans

X = df1
# X.head()
y = data1[1]

# Scaling
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

print("------------------------------")  # 30個

# Metrics
from sklearn.metrics import (
    silhouette_score,
    adjusted_rand_score,
    completeness_score,
    v_measure_score,
)

# Running k-means and computing inter-cluster distance score for various *k* values

km_scores = []
km_silhouette = []
vmeasure_score = []
for i in range(2, 12):
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
plt.show()

print("------------------------------")  # 30個

km = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_scaled)
preds_km = km.predict(X_scaled)
plt.figure(figsize=(21, 35))
for i in range(1, 29):
    plt.subplot(7, 4, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=preds_km, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)

plt.show()

print("------------------------------")  # 30個

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

plt.scatter(x=[i for i in range(2, 12)], y=gm_bic, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("Gaussian mixture BIC score")
plt.show()


plt.scatter(x=[i for i in range(2, 12)], y=gm_score, s=150, edgecolor="k")
plt.show()


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

plt.figure(figsize=(21, 35))
for i in range(1, 29):
    plt.subplot(7, 4, i)
    dim1 = lst_vars[i - 1][0]
    dim2 = lst_vars[i - 1][1]
    plt.scatter(df1[dim1], df1[dim2], c=preds_gm, edgecolor="k")
    plt.xlabel(f"{dim1}", fontsize=13)
    plt.ylabel(f"{dim2}", fontsize=13)
plt.show()

print("------------------------------")  # 30個

# PCA
from sklearn.decomposition import PCA

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
plt.show()

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
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.grid(True)
plt.xlabel("V-measures scores")
plt.show()

# K-means fitting with PCA-transformed data
km_pca = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_pca)
preds_km_pca = km_pca.predict(X_pca)

# Visualizing the clusters after running k-means on PCA-transformed features
col_pca_combi = list(combinations(df_pca.columns, 2))
num_pca_combi = len(col_pca_combi)

plt.figure(figsize=(21, 20))
for i in range(1, num_pca_combi + 1):
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
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score)
plt.show()

# K-means fitting with ICA-transformed data
km_ica = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_ica)
preds_km_ica = km_ica.predict(X_ica)

# Visualizing the clusters after running k-means on ICA-transformed features
col_ica_combi = list(combinations(df_ica.columns, 2))
num_ica_combi = len(col_ica_combi)

plt.figure(figsize=(21, 20))
for i in range(1, num_ica_combi + 1):
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
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score)
plt.show()

# K-means fitting with random-projected data

km_random_proj = KMeans(n_clusters=5, n_init=10, max_iter=500).fit(X=X_random_proj)
preds_km_random_proj = km_random_proj.predict(X_random_proj)

# Visualizing the clusters after running k-means on random-projected features

col_random_proj_combi = list(combinations(df_random_proj.columns, 2))
num_random_proj_combi = len(col_random_proj_combi)

plt.figure(figsize=(21, 20))
for i in range(1, num_random_proj_combi + 1):
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
plt.show()


def plot_cluster_rp(df_rp, preds_rp):
    """
    Plots clusters after running random projection
    """
    plt.figure(figsize=(21, 12))
    for i in range(1, num_random_proj_combi + 1):
        plt.subplot(int(num_random_proj_combi / 3) + 1, 3, i)
        dim1 = col_random_proj_combi[i - 1][0]
        dim2 = col_random_proj_combi[i - 1][1]
        plt.scatter(df_rp[dim1], df_rp[dim2], c=preds_rp, edgecolor="k")
        plt.xlabel(f"{dim1}", fontsize=13)
        plt.ylabel(f"{dim2}", fontsize=13)
    plt.show()


# Running the random projections many times

rp_score = []
rp_silhouette = []
rp_vmeasure = []
for i in range(20):
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
plt.show()

plt.scatter(x=[i for i in range(20)], y=rp_silhouette)
plt.show()

plt.scatter(x=[i for i in range(20)], y=rp_vmeasure)
plt.show()

# This kind of variation does not happen with PCA
pca_score = []
pca_silhouette = []
pca_vmeasure = []
for i in range(20):
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

from sklearn import datasets

X, y = datasets.make_hastie_10_2(n_samples=12000, random_state=1)

df = pd.DataFrame(data=X, columns=["X" + str(i) for i in range(1, 11)])
cc = df.head()
print(cc)

df["y"] = pd.Series(y)
cc = df.head()
print(cc)

# Basic visualizations

i = 1
plt.figure(figsize=(20, 20))
for c in df.columns[:-1]:
    plt.subplot(4, 3, i)
    plt.title(f"Histogram of variable {c}")
    plt.yticks()
    plt.xticks()
    plt.hist(df[c], bins=20, color="orange", edgecolor="k")
    i += 1
show()

i = 1
plt.figure(figsize=(20, 20))
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
# Test/train/validation split

X = df.drop("y", axis=1)
y = df["y"]

# First divide train and test data in 70:30 ratio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# Then further divide the test set in 50:50 ratio into validation set and test set

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

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=5)

dtree.fit(X_train, y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

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
for i in range(val_range[0], val_range[1], val_range[2]):
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

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_max_depth, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_max_depth, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    range(val_range[0], val_range[1], val_range[2]), train_acc_min_samples_leaf, c="red"
)
plt.plot(
    range(val_range[0], val_range[1], val_range[2]), val_acc_min_samples_leaf, c="blue"
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of trees: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_num_trees, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_num_trees, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Number of trees in the meta-estimator")
plt.ylabel("Accuracy")
plt.ylim(0.5, 1.05)
show()

plt.plot(range(val_range[0], val_range[1], val_range[2]), time_adaboost, c="red")
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
lr_range = []
for i in range(val_range[0], val_range[1], val_range[2]):
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.75,1.0)
show()

# SVM model
# Scaling the data using StandardScaler

from sklearn.preprocessing import StandardScaler

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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of degree: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of degree: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of C: {2**(i)}")


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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for gamma: {gamma}")


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
for i in range(val_range[0], val_range[1], val_range[2]):
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

    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neighbors: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_k, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_k, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.7,0.9)
plt.xlim(0, 110)
show()

# Neural Networks (Multi-layer perceptron)

import keras

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout

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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
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
lr_range = []
for i in range(val_range[0], val_range[1], val_range[2]):
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for: {i}% training set size. Took {round((t2-t1),2)} seconds.")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
plt.xlim(0, 110)
show()

# At the end, comparison of performance (accuracy) on test set and wall time

from sklearn.tree import DecisionTreeClassifier

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
# df.head()

# Basic descriptive statistics

# df.describe()

# One-hot encoding of categorical features

df_final = pd.get_dummies(df, ["purpose"], drop_first=True)
df_final = df_final.drop("credit.policy", axis=1)

# df_final.shape
# (9578, 18)

# Basic visualizations

i = 1
plt.figure(figsize=(20, 20))
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
plt.figure(figsize=(20,33))
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

# Test/train/validation split

X = df_final.drop("not.fully.paid", axis=1)
y = df["not.fully.paid"]

# First divide train and test data in 70:30 ratio

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

# X_train.head(10)

# y.head()

# Then further divide the test set in 50:50 ratio into validation set and test set

X_test, X_val, y_test, y_val = train_test_split(X_test, y_test, test_size=0.50)

# X_test.head()

# X_val.head()

# Show the shape of these sets

print("Shape of validation set:", X_val.shape)
print("Shape of test set:", X_test.shape)
print("Shape of training set:", X_train.shape)

# Decision Tree model

from sklearn.tree import DecisionTreeClassifier

dtree = DecisionTreeClassifier(criterion="gini", max_depth=10, min_samples_leaf=5)

dtree.fit(X_train, y_train)

# Predictions and evaluation

predictions = dtree.predict(X_val)

from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score

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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of trees: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_num_trees, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_num_trees, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks()
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.75, 1.05)
show()

# SVM model

# Scaling the data using StandardScaler

from sklearn.preprocessing import StandardScaler

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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of degree: {i}")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of degree: {i}")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_degree, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_degree, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of C: {2**(i)}")


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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for gamma: {gamma}")


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
for i in range(val_range[0], val_range[1], val_range[2]):
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

    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neighbors: {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_k, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_k, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
        print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
plt.ylim(0.7, 0.9)
plt.xlim(0, 110)
show()

# Neural Networks (Multi-layer perceptron)

import keras

# from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout

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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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
    print(f"Done for number of neurons (each hidden layer): {i}")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_n, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_n, c="blue")
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
for i in range(val_range[0], val_range[1], val_range[2]):
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

    print(f"Done for: {i}% training set size")


plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed")
plt.ylabel("Accuracy")
# plt.ylim(0.8,0.9)
plt.xlim(0, 110)
show()

# To smooth out the dependence on training set size, can we tweak the learning rate?

val_acc_train_size = []
train_acc_train_size = []

val_range = (10, 101, 5)
for i in range(val_range[0], val_range[1], val_range[2]):
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

    print(f"Done for: {i}% training set size")

plt.plot(range(val_range[0], val_range[1], val_range[2]), train_acc_train_size, c="red")
plt.plot(range(val_range[0], val_range[1], val_range[2]), val_acc_train_size, c="blue")
plt.legend(["Training", "Validation"])
plt.grid(True)
plt.xticks(np.arange(0, 110, step=10))
plt.yticks()
plt.xlabel("Percentage of training data fed (lr=0.001)")
plt.ylabel("Accuracy")
plt.ylim(0.5, 0.9)
plt.xlim(0, 110)
show()

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
plt.title("Time complexity of Mean Shift\n")
plt.scatter(n_samples, t_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, t_ms, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Time taken for model (sec)")
show()

plt.figure(figsize=(8, 5))
plt.title("Homogeneity score with data set size\n")
plt.scatter(n_samples, homo_ms, edgecolors="k", c="green", s=100)
plt.plot(n_samples, homo_ms, "k--", lw=3)
plt.xticks()
plt.xlabel("Number of samples")
plt.yticks()
plt.ylabel("Homogeneity score")
show()

plt.figure(figsize=(8, 5))
plt.title("Completeness score with data set size\n")
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
plt.title("Cluster detection with noisy data\n")
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
    plt.xlabel(f"{dim1}")
    plt.ylabel(f"{dim2}")
show()

# How are the classes separated (boxplots)

plt.figure(figsize=(16, 14))
for i, c in enumerate(df1.columns):
    plt.subplot(3, 2, i + 1)
    sns.boxplot(y=df1[c], x=data1[1])
    plt.xticks()
    plt.yticks()
    plt.xlabel("Class")
    plt.ylabel(c)
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
plt.title("The elbow method for determining number of clusters\n")
plt.scatter(x=[i for i in range(2, 12)], y=km_scores, s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("K-means score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=vmeasure_score, s=150, edgecolor="k")
plt.xlabel("V-measure score")
plt.show()

plt.figure(figsize=(7, 4))
plt.title("The silhouette coefficient method \nfor determining number of clusters")
plt.scatter(x=[i for i in range(2, 12)], y=km_silhouette, s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("Silhouette score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
plt.show()

plt.scatter(x=[i for i in range(2, 12)], y=db_score, s=150, edgecolor="k")
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
plt.title("The Gaussian Mixture model BIC \nfor determining number of clusters\n")
plt.scatter(x=[i for i in range(2, 12)], y=np.log(gm_bic), s=150, edgecolor="k")
plt.xlabel("Number of clusters")
plt.ylabel("Log of Gaussian mixture BIC score")
plt.xticks([i for i in range(2, 12)])
plt.yticks()
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
plt.title("Annual income distribution")
plt.xlabel("Annual income (k$)")
plt.hist(df["Annual Income (k$)"], color="orange", edgecolor="k")
plt.show()

plt.figure(figsize=(8, 5))
plt.title("Spending Score distribution")
plt.xlabel("Spending Score (1-100)")
plt.hist(df["Spending Score (1-100)"], color="green", edgecolor="k")
plt.show()

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
plt.show()

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
dendrogram = sch.dendrogram(sch.linkage(X, method="ward"))
plt.show()

# Optimal number of clusters

plt.figure(figsize=(15, 6))
plt.title("Dendrogram")
plt.xlabel("Customers")
plt.ylabel("Euclidean distances")
plt.hlines(y=190, xmin=0, xmax=2000, lw=3, linestyles="--")
plt.text(x=900, y=220, s="Horizontal line crossing 5 vertical lines")
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
plt.title("Clustering of customers")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
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
    plt.show()

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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 30個
