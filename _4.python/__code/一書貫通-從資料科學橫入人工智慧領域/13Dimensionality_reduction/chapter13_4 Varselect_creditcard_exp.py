# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:36:02 2018

@author: Ben
"""

def Var_Select(orgdata, k, alphaMax=10, alphastep=0.2):
    """
    orgdata-需要信息压缩的数据框
    k-预期最大需要保留的最大变量个数，实际保留数量不能多于这个数值
    alphaMax-SparsePCA算法惩罚项的最大值,一般要到5才会取得比较理想的结果
    alphastep-SparsePCA算法惩罚项递增的步长
    """
    #step1:当数据量过大时，为了减少不必要的耗时
    if orgdata.iloc[:,1].count()>5000:
        data = orgdata.sample(5000)
    else:
        data = orgdata
   #step2:引入所需要的包，并且对数据进行标准化
    from sklearn import preprocessing
    import pandas as pd
    import numpy as np
    from sklearn.decomposition import SparsePCA
    #from functools import reduce
    data = preprocessing.scale(data)
    n_components = k
    #pca_n = list()
    #step3:进行SparsePCA计算，选择合适的惩罚项alpha，当恰巧每个原始变量只在一个主成分上有权重时，停止循环
    for i in np.arange(0.1, alphaMax, alphastep):
        pca_model = SparsePCA(n_components=n_components, alpha=i)
        pca_model.fit(data)
        pca = pd.DataFrame(pca_model.components_).T
        n = data.shape[1] - sum(sum(np.array(pca != 0)))####计算系数不为0的数量
        if n == 0:
            global best_alpha
            best_alpha = i
            break        
    #step4:根据上一步得到的惩罚项的取值，估计SparsePCA，并得到稀疏主成分得分
    pca_model = SparsePCA(n_components=n_components, alpha=best_alpha)
    pca_model.fit(data)
    pca = pd.DataFrame(pca_model.components_).T
    data = pd.DataFrame(data)
    score = pd.DataFrame(pca_model.fit_transform(data))
    #step6:计算原始变量与主成分之间的1-R方值
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

    R_square = abs(pd.DataFrame(np.array(R_square).reshape((data.shape[1], n_components))))
    var_list = []
    #print(R_square)
   #step7:每个主成分中，选出原始变量的1-R方值最小的。
    for i in range(n_components):
        vmin = R_square[i].min()
        #print(R_square[i])
        #print(vmin)
        #print(R_square[R_square[i] == min][i])
        var_list.append(R_square[R_square[i] == vmin][i].index)
    
    news_ids =[]
    for id in var_list:
        if id not in news_ids:
            news_ids.append(id)
    print(news_ids)
    data_vc = orgdata.iloc[:, np.array(news_ids).reshape(len(news_ids))]
    return data_vc

#%%
import os
os.chdir(r"D:\Python_book\13Dimensionality_reduction")
import pandas as pd
model_data = pd.read_csv("creditcard_exp.csv")
model_data.head()
data = model_data.loc[ :,'gender':]


# In[67]:
Varseled_data=Var_Select(data,k=5)
#%%