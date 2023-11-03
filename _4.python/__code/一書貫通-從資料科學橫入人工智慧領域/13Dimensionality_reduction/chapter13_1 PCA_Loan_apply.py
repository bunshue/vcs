# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 21:26:31 2018

@author: Ben
"""

# coding: utf-8
"""
X1 品格：指客户的名誉；
X2 能力：指客户的偿还能力；
X3 资本：指客户的财务实力和财务状况；
X4 担保：指对申请贷款项担保的覆盖程度；
X5 环境：指外部经济、政策环境对客户的影响
"""
# 一、主成分分析

# - 1、引入数据

# In[1]:


import pandas as pd
import os
os.chdir(r"D:\Python_book\13Dimensionality_reduction")
model_data = pd.read_csv("Loan_aply.csv",encoding='gbk')
model_data.head()


# In[2]:
data = model_data.loc[ :,'X1':]
data.head()

# - 2、查看相关系数矩阵，判定做变量降维的必要性（非必须）

# In[3]:
corr_matrix = data.corr(method='pearson')

# - 3、做主成分之前，进行中心标准化

# In[4]:
from sklearn import preprocessing
data = preprocessing.scale(data)
# - 4、使用sklearn的主成分分析，用于判断保留主成分的数量

# In[5]:
from sklearn.decomposition import PCA
'''说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
'''
pca=PCA(n_components=4)
pca.fit(data)
print(pca.explained_variance_)#建议保留1个主成分
print(pca.explained_variance_ratio_)#建议保留1个主成分
#%%
pca=PCA(n_components=1).fit(data)#综上,2个主成分
newdata=pca.fit_transform(data)
citi10_pca=model_data.join(pd.DataFrame(newdata))
# In[6]:
'''通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性
'''
pd.DataFrame(pca.components_).T
#%%