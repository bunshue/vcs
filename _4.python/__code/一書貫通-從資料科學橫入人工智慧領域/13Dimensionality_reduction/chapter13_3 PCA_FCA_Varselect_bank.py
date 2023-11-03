# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 23:26:04 2018

@author: Ben
"""


# coding: utf-8
"""
CNT_TBM 柜台交易次数	
CNT_ATM ATM机交易次数
CNT_POS POS机交易次数	
CNT_CSC 有偿服务次数

"""
# 一、主成分分析

# - 1、引入数据

# In[1]:


import pandas as pd
import os
os.chdir(r"D:\Python_book\13Dimensionality_reduction")
model_data = pd.read_csv("profile_bank.csv")
data = model_data.ix[ :,'CNT_TBM':'CNT_CSC']

# - 2、查看相关系数矩阵，判定做变量降维的必要性（非必须）

# In[3]:
corr_matrix = data.corr(method='pearson')
#corr_matrix = data.corr(method='spearman')

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
pca=PCA(n_components=3)
pca.fit(data)
print(pca.explained_variance_)#建议保留2个主成分
print(pca.explained_variance_ratio_)#建议保留3个主成分
#%%
pca=PCA(n_components=3).fit(data)#综上,2个主成分
newdata=pca.fit_transform(data)
# In[6]:
'''通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性
'''
pd.DataFrame(pca.components_).T
#第一个主成分在第3个变量权重差不多高 
#第二个主成分在第1个变量权重高,其余均低
#第三个主成分在第4个变量权重高,其余均低
#############################################################################################
#二、因子分析
#因子分析的概念很多，作为刚入门的人，我们可以认为因子分析是主成分分析的延续
# In[7]:
from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting
fa = FactorAnalysis.load_data_samples(
        data,
        preproc_demean=True,
        preproc_scale=True
        )
fa.extract_components()


# - 2、设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

# In[8]:
fa.find_comps_to_retain(method='top_n',num_keep=3)
# - 3、通过最大方差法进行因子旋转

# In[9]:
pd.DataFrame(fa.comps["rot"])#查看因子权重
fa.rotate_components(method='varimax')
fa_plotting.graph_summary(fa)
# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强


# - 4、获取因子得分

# In[19]:
#到目前还没有与PCA中fit_transform类似的函数，因此只能手工计算因子
#以下是矩阵相乘的方式计算因子：因子=原始数据（n*k）*权重矩阵(k*num_keep)
import numpy as np
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)#注意data数据需要标准化
fa_score = pd.DataFrame(np.dot(data, fas))

# ### 第三步：根据因子得分进行数据分析

# In[25]:


a=fa_score.rename(columns={0: "Gross", 1: "Avg"})
profile_bank_fa=model_data.join(a)


#%%
#############################################################################################
#三、变量筛选
# ### 以下是变量选择的完整函数
#基于SparsePCA的算法还不是很稳定,尤其是当数据本身保留几个变量都处于模棱两个的时候,
#该算法并不能达到人为调整的效果。而且并不能保证每次保留的变量是一致的（原因1、SparsePCA：本身就具有随机性；2、脚本中也随机抽样的），
#只能保证保留的变量是不相关的
#其特点只是比较省人力，可以自动化运行
# In[65]:


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
    


# In[66]:
import os
os.chdir(r"D:\Python_book\13Dimensionality_reduction")
import pandas as pd
model_data = pd.read_csv("profile_bank.csv")
data = model_data.ix[ :,'CNT_TBM':'CNT_CSC']


# In[67]:
Varseled_data=Var_Select(data,k=3,alphaMax=10)
#%%


















#%%
