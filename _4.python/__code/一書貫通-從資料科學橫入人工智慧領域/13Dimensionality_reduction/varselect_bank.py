# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:04:38 2018

@author: changguozhen
"""
# In[66]:
import os
os.chdir(r"d:\test\13Dimensionality_reduction")
import pandas as pd
model_data = pd.read_csv("profile_bank.csv")
data = model_data.ix[ :,'CNT_TBM':'CNT_CSC']
k=3
alphaMax=5
alphastep=0.2
#%%
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.decomposition import SparsePCA
from functools import reduce
data = preprocessing.scale(data)
n_components = k
pca_n = list()

#%%
#%%
pca_model = SparsePCA(n_components=n_components, alpha=5)
pca_model.fit(data)
#%%
pca = pd.DataFrame(pca_model.components_).T
#%%
n = data.shape[1] - sum(sum(np.array(pca != 0)))

#%%
best_alpha=5
pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
pca_model.fit(data)
pca = pd.DataFrame(pca_model.components_).T
data = pd.DataFrame(data)
score = pd.DataFrame(pca_model.fit_transform(data))

#%%
r = []
R_square = []
for xk in range(data.shape[1]):  # xk输入变量个数
    for paj in range(n_components):  # paj主成分个数
        r.append(abs(np.corrcoef(data.iloc[:, xk], score.iloc[:, paj])[0, 1]))
        r_max1 = max(r)
        r.remove(r_max1)
        r.append(-2)
        r_max2 = max(r)
        R_square.append((1 - r_max1 ** 2) / (1 - r_max2 ** 2))

R=abs(pd.DataFrame(np.array(r).reshape((data.shape[1], n_components))))
R_square = abs(pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components))))
var_list = []
#print(R_square)
#%%  
for i in range(n_components):
    vmin = R_square[i].min()
    print(R_square[i])
    print(vmin)
    print(R_square[R_square[i] == min][i])
    var_list.append(R_square[R_square[i] == vmin][i].index[0])
#%%
news_ids =[]
for id in var_list:
    if id not in news_ids:
        news_ids.append(id)
print(news_ids)
orgdata = model_data.ix[ :,'CNT_TBM':'CNT_CSC']
data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]

#%%



# In[67]:
