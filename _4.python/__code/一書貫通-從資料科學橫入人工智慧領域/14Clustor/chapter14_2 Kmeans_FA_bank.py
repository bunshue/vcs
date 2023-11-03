
# coding: utf-8

# # 第十四讲-2 K-means聚类分析 

# ### 第一步：手动测试主成分数量

# - 1、引入数据
import os
os.chdir(r"D:\Python_book\14Clustor")

# In[1]:


import pandas as pd
model_data = pd.read_csv("profile_bank.csv")
data = model_data.loc[ :,'CNT_TBM':'CNT_CSC']
data.head()


# - 2、查看相关系数矩阵，判定做变量降维的必要性（非必须）

# In[2]:


corr_matrix = data.corr(method='pearson')
#corr_matrix = corr_matrix.abs()
corr_matrix


# - 3、做主成分之前，进行中心标准化

# In[3]:


from sklearn import preprocessing
data = preprocessing.scale(data)


# - 4、使用sklearn的主成分分析，用于判断保留主成分的数量

# In[4]:


from sklearn.decomposition import PCA
'''说明：1、第一次的n_components参数应该设的大一点
   说明：2、观察explained_variance_ratio_和explained_variance_的取值变化，建议explained_variance_ratio_累积大于0.85，explained_variance_需要保留的最后一个主成分大于0.8，
'''
pca=PCA(n_components=3)
newData=pca.fit(data)
print(pca.explained_variance_)
print(pca.explained_variance_ratio_)


# In[5]:


'''通过主成分在每个变量上的权重的绝对值大小，确定每个主成分的代表性
'''
pd.DataFrame(pca.components_).T


# ### 第二步：根据主成分分析确定需要保留的主成分数量，进行因子分析

# - 1、导入包，并对输入的数据进行主成分提取。为保险起见，data需要进行中心标准化

# In[6]:


from fa_kit import FactorAnalysis
from fa_kit import plotting as fa_plotting
fa = FactorAnalysis.load_data_samples(
        data,
        preproc_demean=True,
        preproc_scale=True
        )
fa.extract_components()


# - 2、设定提取主成分的方式。默认为“broken_stick”方法，建议使用“top_n”法

# In[7]:


fa.find_comps_to_retain(method='top_n',num_keep=3)


# - 3、通过最大方差法进行因子旋转

# In[8]:


fa.rotate_components(method='varimax')
fa_plotting.graph_summary(fa)


# - 说明：可以通过第三张图观看每个因子在每个变量上的权重，权重越高，代表性越强

# - 4、获取因子得分

# In[12]:


pd.DataFrame(fa.comps["rot"])


# In[13]:


import numpy as np
fas = pd.DataFrame(fa.comps["rot"])
data = pd.DataFrame(data)
score = pd.DataFrame(np.dot(data, fas))


# ### 第三步：根据因子得分进行数据分析

# In[14]:


fa_scores=score.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
fa_scores.head()


# ### 第四步：使用因子得分进行k-means聚类

# ### 4.1 k-means聚类的第一种方式：不进行变量分布的正态转换--用于寻找异常值

# - 1、查看变量的偏度

# In[15]:


var = ["ATM_POS","TBM","CSC"]
skew_var = {}
for i in var:
    skew_var[i]=abs(fa_scores[i].skew())
    skew=pd.Series(skew_var).sort_values(ascending=False)
skew


# - 2、进行k-means聚类

# In[16]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3) #MiniBatchKMeans()分批处理
#kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result=kmeans.fit(fa_scores)
#print(result)


# - 3、对分类结果进行解读

# In[17]:


model_data_l=model_data.join(pd.DataFrame(result.labels_))
model_data_l=model_data_l.rename(columns={0: "clustor"})
model_data_l.head()



# In[18]:


import matplotlib
get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind = 'pie') 


# ### 4.2 k-means聚类的第二种方式：进行变量分布的正态转换--用于客户细分

# - 1、进行变量分布的正态转换

# In[19]:


import numpy as np
from sklearn import preprocessing
quantile_transformer = preprocessing.QuantileTransformer(output_distribution='normal', random_state=0)
fa_scores_trans=quantile_transformer.fit_transform(fa_scores)
fa_scores_trans=pd.DataFrame(fa_scores_trans)
fa_scores_trans=fa_scores_trans.rename(columns={0: "ATM_POS", 1: "TBM", 2: "CSC"})
fa_scores_trans.head()


# In[20]:


var = ["ATM_POS","TBM","CSC"]
skew_var = {}
for i in var:
    skew_var[i]=abs(fa_scores_trans[i].skew())
    skew=pd.Series(skew_var).sort_values(ascending=False)
skew


# - 2、进行k-means聚类

# In[21]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3) #MiniBatchKMeans()分批处理
#kmeans = cluster.KMeans(n_clusters=3, init='random', n_init=1)
result=kmeans.fit(fa_scores_trans)
#print(result)


# - 3、对分类结果进行解读

# In[22]:


model_data_l=model_data.join(pd.DataFrame(result.labels_))
model_data_l=model_data_l.rename(columns={0: "clustor"})
model_data_l.head()


# In[23]:


import matplotlib
get_ipython().magic('matplotlib inline')
model_data_l.clustor.value_counts().plot(kind = 'pie') 


# In[31]:


from sklearn import tree

clf = tree.DecisionTreeClassifier(criterion='gini', max_depth=3, min_samples_split=100, min_samples_leaf=100, random_state=12345)  # 当前支持计算信息增益和GINI
clf.fit(model_data, result.labels_)


# In[48]:


import pydotplus
from IPython.display import Image
import sklearn.tree as tree

dot_data = tree.export_graphviz(clf, 
                                out_file=None, 
                                feature_names=model_data.columns,  
                                class_names=['0','1','2'],
                                filled=True) 


# In[49]:


graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png()) 

#%%
