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

#from common1 import *
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

'''
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
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs

n_features = 8
n_cluster = 5
cluster_std = 1.5
n_samples = 1000

data1 = make_blobs(n_samples=n_samples,n_features=n_features,centers=n_cluster,cluster_std=cluster_std)
d1 = data1[0]
df1=pd.DataFrame(data=d1,columns=['Feature_'+str(i) for i in range(1,n_features+1)])
cc = df1.head()
print(cc)


from itertools import combinations

lst_vars=list(combinations(df1.columns,2))
cc = len(lst_vars)
print(cc)

plt.figure(figsize=(21,35))
for i in range(1,29):
    plt.subplot(7,4,i)
    dim1=lst_vars[i-1][0]
    dim2=lst_vars[i-1][1]
    plt.scatter(df1[dim1],df1[dim2],c=data1[1],edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)

show()

print("------------------------------")  # 30個

cc = df1.describe().transpose()
print(cc)

# How are the classes separated (boxplots)
plt.figure(figsize=(21,15))

for i,c in enumerate(df1.columns):
    plt.subplot(3,3,i+1)
    sns.boxplot(y=df1[c],x=data1[1])
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.xlabel("Class",fontsize=15)
    plt.ylabel(c,fontsize=15)

show()

print("------------------------------")  # 30個

# k-means clustering
from sklearn.cluster import KMeans
X=df1
#X.head()
y=data1[1]

#Scaling
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
X_scaled=scaler.fit_transform(X)

print("------------------------------")  # 30個

# Metrics
from sklearn.metrics import silhouette_score, adjusted_rand_score, completeness_score, v_measure_score

# Running k-means and computing inter-cluster distance score for various *k* values

km_scores= []
km_silhouette = []
vmeasure_score =[]
for i in range(2,12):
    km = KMeans(n_clusters=i, random_state=0).fit(X_scaled)
    preds = km.predict(X_scaled)
    print("Score for number of cluster(s) {}: {}".format(i,km.score(X_scaled)))
    km_scores.append(-km.score(X_scaled))
    silhouette = silhouette_score(X_scaled,preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i,silhouette))
    v_measure = v_measure_score(y,preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i,v_measure))
    print("-"*100)
    
plt.scatter(x=[i for i in range(2,12)],y=km_scores,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("K-means score")
show()

print("------------------------------")  # 30個

plt.scatter(x=[i for i in range(2,12)],y=vmeasure_score,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("V-measure score")
plt.show()

print("------------------------------")  # 30個

km = KMeans(n_clusters=5,n_init=10,max_iter=500).fit(X=X_scaled)
preds_km = km.predict(X_scaled)
plt.figure(figsize=(21,35))
for i in range(1,29):
    plt.subplot(7,4,i)
    dim1=lst_vars[i-1][0]
    dim2=lst_vars[i-1][1]
    plt.scatter(df1[dim1],df1[dim2],c=preds_km,edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)

plt.show()

print("------------------------------")  # 30個

# Expectation-maximization (Gaussian Mixture Model)

from sklearn.mixture import GaussianMixture

gm_bic= []
gm_score=[]
for i in range(2,12):
    gm = GaussianMixture(n_components=i,n_init=10,tol=1e-3,max_iter=1000).fit(X_scaled)
    print("BIC for number of cluster(s) {}: {}".format(i,gm.bic(X_scaled)))
    print("Log-likelihood score for number of cluster(s) {}: {}".format(i,gm.score(X_scaled)))
    print("-"*100)
    gm_bic.append(-gm.bic(X_scaled))
    gm_score.append(gm.score(X_scaled))

plt.scatter(x=[i for i in range(2,12)],y=gm_bic,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("Gaussian mixture BIC score")
plt.show()


plt.scatter(x=[i for i in range(2,12)],y=gm_score,s=150,edgecolor='k')
plt.show()


print("------------------------------")  # 30個

gm = GaussianMixture(n_components=5,verbose=1,n_init=10,tol=1e-2,covariance_type='full',max_iter=1000).fit(X_scaled)

cc = gm.means_
print(cc)

cc = km.cluster_centers_
print(cc)

cc = gm.means_/km.cluster_centers_
print(cc)

preds_gm=gm.predict(X_scaled)

km_rand_score = adjusted_rand_score(preds_km,y)

gm_rand_score = adjusted_rand_score(preds_gm,y)

print("Adjusted Rand score for k-means",km_rand_score)
print("Adjusted Rand score for Gaussian Mixture model",gm_rand_score)

cc = silhouette_score(X_scaled,preds_km)
print(cc)

cc = silhouette_score(X_scaled,preds_gm)
print(cc)

plt.figure(figsize=(21,35))
for i in range(1,29):
    plt.subplot(7,4,i)
    dim1=lst_vars[i-1][0]
    dim2=lst_vars[i-1][1]
    plt.scatter(df1[dim1],df1[dim2],c=preds_gm,edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)
plt.show()

print("------------------------------")  # 30個

# PCA
from sklearn.decomposition import PCA
n_prin_comp = 3

pca_partial = PCA(n_components=n_prin_comp,svd_solver='full')
pca_partial.fit(X_scaled)

pca_full = PCA(n_components=n_features,svd_solver='full')
pca_full.fit(X_scaled)

# How much variance is explained by principal components?

pca_explained_var = pca_full.explained_variance_ratio_
cum_explaiend_var = pca_explained_var.cumsum()
print(cum_explaiend_var)

plt.figure(figsize=(12,5))
plt.bar(x=['PrComp'+str(i) for i in range(1,9)],height=cum_explaiend_var,width=0.6)
plt.xticks(fontsize=14)
plt.hlines(y=0.8,xmin='PrComp1',xmax='PrComp8',linestyles='dashed',lw=3)
plt.text(x='PrComp1',y=0.82,s="80% variance explained",fontsize=15)
plt.show()

print("------------------------------")  # 30個

# Transform the original variables in principal component space and create a DataFrame
X_pca = pca_partial.fit_transform(X_scaled)
df_pca=pd.DataFrame(data=X_pca,columns=['Principal_comp'+str(i) for i in range(1,n_prin_comp+1)])

# Running k-means on the transformed features
km_scores= []
km_silhouette = []
vmeasure_score =[]
for i in range(2,12):
    km = KMeans(n_clusters=i, random_state=0).fit(X_pca)
    preds = km.predict(X_pca)
    print("Score for number of cluster(s) {}: {}".format(i,km.score(X_pca)))
    km_scores.append(-km.score(X_pca))
    silhouette = silhouette_score(X_pca,preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i,silhouette))
    v_measure = v_measure_score(y,preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i,v_measure))
    print("-"*100)

plt.scatter(x=[i for i in range(2,12)],y=km_scores,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("K-means scores")
plt.show()

plt.scatter(x=[i for i in range(2,12)],y=vmeasure_score,s=150,edgecolor='k')
plt.grid(True)
plt.xlabel("V-measures scores")
plt.show()

# K-means fitting with PCA-transformed data
km_pca = KMeans(n_clusters=5,n_init=10,max_iter=500).fit(X=X_pca)
preds_km_pca = km_pca.predict(X_pca)

# Visualizing the clusters after running k-means on PCA-transformed features
col_pca_combi=list(combinations(df_pca.columns,2))
num_pca_combi = len(col_pca_combi)

plt.figure(figsize=(21,20))
for i in range(1,num_pca_combi+1):
    plt.subplot(int(num_pca_combi/3)+1,3,i)
    dim1=col_pca_combi[i-1][0]
    dim2=col_pca_combi[i-1][1]
    plt.scatter(df_pca[dim1],df_pca[dim2],c=preds_km_pca,edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)
show()

# ICA

from sklearn.decomposition import FastICA
n_ind_comp = 3
ica_partial = FastICA(n_components=n_ind_comp)
ica_partial.fit(X_scaled)

ica_full = FastICA(max_iter=1000)
ica_full.fit(X_scaled)

X_ica = ica_partial.fit_transform(X_scaled)
df_ica=pd.DataFrame(data=X_ica,columns=['Independent_comp'+str(i) for i in range(1,n_ind_comp+1)])

# Running k-means on the independent features
km_scores= []
km_silhouette = []
vmeasure_score =[]
for i in range(2,12):
    km = KMeans(n_clusters=i, random_state=0).fit(X_ica)
    preds = km.predict(X_ica)
    print("Score for number of cluster(s) {}: {}".format(i,km.score(X_ica)))
    km_scores.append(-km.score(X_ica))
    silhouette = silhouette_score(X_ica,preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i,silhouette))
    v_measure = v_measure_score(y,preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i,v_measure))
    print("-"*100)

plt.scatter(x=[i for i in range(2,12)],y=km_scores)
plt.show()

plt.scatter(x=[i for i in range(2,12)],y=vmeasure_score)
plt.show()

# K-means fitting with ICA-transformed data
km_ica = KMeans(n_clusters=5,n_init=10,max_iter=500).fit(X=X_ica)
preds_km_ica = km_ica.predict(X_ica)

# Visualizing the clusters after running k-means on ICA-transformed features
col_ica_combi=list(combinations(df_ica.columns,2))
num_ica_combi = len(col_ica_combi)

plt.figure(figsize=(21,20))
for i in range(1,num_ica_combi+1):
    plt.subplot(int(num_ica_combi/3)+1,3,i)
    dim1=col_ica_combi[i-1][0]
    dim2=col_ica_combi[i-1][1]
    plt.scatter(df_ica[dim1],df_ica[dim2],c=preds_km_ica,edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)
show()

# Random Projection
from sklearn.random_projection import GaussianRandomProjection
n_random_comp = 3
random_proj = GaussianRandomProjection(n_components=n_random_comp)
X_random_proj = random_proj.fit_transform(X_scaled)
df_random_proj=pd.DataFrame(data=X_random_proj,columns=['Random_projection'+str(i) for i in range(1,n_random_comp+1)])

# Running k-means on random projections

km_scores= []
km_silhouette = []
vmeasure_score = []
for i in range(2,12):
    km = KMeans(n_clusters=i, random_state=0).fit(X_random_proj)
    preds = km.predict(X_random_proj)
    print("Score for number of cluster(s) {}: {}".format(i,km.score(X_random_proj)))
    km_scores.append(-km.score(X_random_proj))
    silhouette = silhouette_score(X_random_proj,preds)
    km_silhouette.append(silhouette)
    print("Silhouette score for number of cluster(s) {}: {}".format(i,silhouette))
    v_measure = v_measure_score(y,preds)
    vmeasure_score.append(v_measure)
    print("V-measure score for number of cluster(s) {}: {}".format(i,v_measure))
    print("-"*100)

plt.scatter(x=[i for i in range(2,12)],y=km_scores)
plt.show()

plt.scatter(x=[i for i in range(2,12)],y=vmeasure_score)
plt.show()

# K-means fitting with random-projected data

km_random_proj = KMeans(n_clusters=5,n_init=10,max_iter=500).fit(X=X_random_proj)
preds_km_random_proj = km_random_proj.predict(X_random_proj)

# Visualizing the clusters after running k-means on random-projected features

col_random_proj_combi=list(combinations(df_random_proj.columns,2))
num_random_proj_combi = len(col_random_proj_combi)

plt.figure(figsize=(21,20))
for i in range(1,num_random_proj_combi+1):
    plt.subplot(int(num_random_proj_combi/3)+1,3,i)
    dim1=col_random_proj_combi[i-1][0]
    dim2=col_random_proj_combi[i-1][1]
    plt.scatter(df_random_proj[dim1],df_random_proj[dim2],c=preds_km_random_proj,edgecolor='k')
    plt.xlabel(f"{dim1}",fontsize=13)
    plt.ylabel(f"{dim2}",fontsize=13)
plt.show()

def plot_cluster_rp(df_rp,preds_rp):
    """
    Plots clusters after running random projection
    """
    plt.figure(figsize=(21,12))
    for i in range(1,num_random_proj_combi+1):
        plt.subplot(int(num_random_proj_combi/3)+1,3,i)
        dim1=col_random_proj_combi[i-1][0]
        dim2=col_random_proj_combi[i-1][1]
        plt.scatter(df_rp[dim1],df_rp[dim2],c=preds_rp,edgecolor='k')
        plt.xlabel(f"{dim1}",fontsize=13)
        plt.ylabel(f"{dim2}",fontsize=13)
    plt.show()

# Running the random projections many times

rp_score= []
rp_silhouette = []
rp_vmeasure = []
for i in range(20):
    random_proj = GaussianRandomProjection(n_components=n_random_comp)
    X_random_proj = random_proj.fit_transform(X_scaled)
    df_random_proj=pd.DataFrame(data=X_random_proj,columns=['Random_projection'+str(i) for i in range(1,n_random_comp+1)])
    
    km = KMeans(n_clusters=5, random_state=0).fit(X_random_proj)
    preds = km.predict(X_random_proj)
    print("Score for iteration {}: {}".format(i,km.score(X_random_proj)))
    rp_score.append(-km.score(X_random_proj))
    
    silhouette = silhouette_score(X_random_proj,preds)
    rp_silhouette.append(silhouette)
    print("Silhouette score for iteration {}: {}".format(i,silhouette))
    
    v_measure = v_measure_score(y,preds)
    rp_vmeasure.append(v_measure)
    print("V-measure score for iteration {}: {}".format(i,v_measure))
    print("-"*100)
    
    plot_cluster_rp(df_random_proj,preds)


plt.scatter(x=[i for i in range(20)],y=rp_score)
plt.show()

plt.scatter(x=[i for i in range(20)],y=rp_silhouette)
plt.show()

plt.scatter(x=[i for i in range(20)],y=rp_vmeasure)
plt.show()

# This kind of variation does not happen with PCA
pca_score= []
pca_silhouette = []
pca_vmeasure = []
for i in range(20):
    pca_partial = PCA(n_components=n_prin_comp,svd_solver='full')
    X_pca=pca_partial.fit_transform(X_scaled)
    km = KMeans(n_clusters=5, random_state=0).fit(X_pca)
    preds = km.predict(X_pca)
    print("Score for iteration {}: {}".format(i,km.score(X_pca)))
    rp_score.append(-km.score(X_pca))
    silhouette = silhouette_score(X_pca,preds)
    rp_silhouette.append(silhouette)
    print("Silhouette score for iteration {}: {}".format(i,silhouette))
    v_measure = v_measure_score(y,preds)
    rp_vmeasure.append(v_measure)
    print("V-measure score for iteration {}: {}".format(i,v_measure))
    print("-"*100)


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



