
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#数据挖掘方法论──SEMMA模型训练使用流程" data-toc-modified-id="数据挖掘方法论──SEMMA模型训练使用流程-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>数据挖掘方法论──SEMMA模型训练使用流程</a></span></li><li><span><a href="#数据获取与导入的S（抽样）阶段。" data-toc-modified-id="数据获取与导入的S（抽样）阶段。-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>数据获取与导入的S（抽样）阶段。</a></span><ul class="toc-item"><li><span><a href="#规整数据集" data-toc-modified-id="规整数据集-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>规整数据集</a></span></li><li><span><a href="#筛选预测能力强的变量" data-toc-modified-id="筛选预测能力强的变量-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>筛选预测能力强的变量</a></span></li></ul></li><li><span><a href="#对每个变量的E（探索）阶段" data-toc-modified-id="对每个变量的E（探索）阶段-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>对每个变量的E（探索）阶段</a></span><ul class="toc-item"><li><span><a href="#对连续变量的统计探索" data-toc-modified-id="对连续变量的统计探索-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>对连续变量的统计探索</a></span></li><li><span><a href="#对分类变量的统计探索" data-toc-modified-id="对分类变量的统计探索-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>对分类变量的统计探索</a></span></li></ul></li><li><span><a href="#针对有问题的变量进行M（修改）的阶段" data-toc-modified-id="针对有问题的变量进行M（修改）的阶段-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>针对有问题的变量进行M（修改）的阶段</a></span><ul class="toc-item"><li><span><a href="#连续变量" data-toc-modified-id="连续变量-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>连续变量</a></span></li><li><span><a href="#分类变量" data-toc-modified-id="分类变量-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>分类变量</a></span></li><li><span><a href="#前向选择法筛选变量" data-toc-modified-id="前向选择法筛选变量-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>前向选择法筛选变量</a></span></li></ul></li><li><span><a href="#建立线性回归模型M（建模）阶段" data-toc-modified-id="建立线性回归模型M（建模）阶段-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>建立线性回归模型M（建模）阶段</a></span></li><li><span><a href="#模型验证A（验证）阶段" data-toc-modified-id="模型验证A（验证）阶段-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>模型验证A（验证）阶段</a></span><ul class="toc-item"><li><span><a href="#对线性回归模型进行评估" data-toc-modified-id="对线性回归模型进行评估-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>对线性回归模型进行评估</a></span></li><li><span><a href="#模型永久化" data-toc-modified-id="模型永久化-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>模型永久化</a></span></li></ul></li></ul></div>

# 本代码案例为 **两阶段精准营销模型** 中的 **构造客户价值预测模型** 部分
# 
# # 数据挖掘方法论──SEMMA模型训练使用流程
# 
# - Sample──数据取样
# 
# - Explore──数据特征探索、分析和予处理
# 
# - Modify──问题明确化、数据调整和技术选择
# 
# - Model──模型的研发、知识的发现
# 
# - Assess──模型和知识的综合解释和评价

# 此处采用线性回归对捐款数额（TargetD）进行建模，建模流程同上一节类似。

# # 数据获取与导入的S（抽样）阶段。
# 
# ## 规整数据集

# In[65]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
os.chdir(r"D:\Python_book\19Case\19_2Donations")



# In[66]:


# 创建一个列表，用来保存所有的建模数据清洗的相关信息
DATA_CLEAN = []


# In[67]:


model_data = pd.read_csv("donations2.csv").drop(["ID","TARGET_B"],1)
model_data.head()


# In[68]:


model_data.dtypes


# In[69]:


y = ["TARGET_D"]

var_c = ["GiftCnt36","GiftCntAll","GiftCntCard36","GiftCntCardAll","GiftTimeLast",
         "GiftTimeFirst","PromCnt12","PromCnt36","PromCntAll","PromCntCard12",
         "PromCntCard36","PromCntCardAll","StatusCatStarAll","DemAge",
         "DemMedHomeValue","DemPctVeterans","DemMedIncome","GiftAvgLast",
         "GiftAvg36","GiftAvgAll","GiftAvgCard36"]

var_d = ['DemGender', 'StatusCat96NK', 'DemCluster', 'DemHomeOwner']


# In[70]:


X = model_data[var_c + var_d]
Y = model_data[y]


# In[71]:


X.shape


# ## 筛选预测能力强的变量

# + 连续变量筛选-相关性

# In[72]:


corr_s = abs(model_data[y + var_c].corr(method = 'spearman'))
corr_s = pd.DataFrame(corr_s.iloc[0,:])

corr_p = abs(model_data[y + var_c].corr(method = 'pearson'))
corr_p = pd.DataFrame(corr_p.iloc[0,:])

corr_sp = pd.concat([corr_s,corr_p], axis = 1)
corr_sp.columns = ['spearman','pearson']


# In[73]:


corr_sp[(corr_sp['spearman'] <= 0.1) & (corr_sp['pearson'] <= 0.1)]


# In[74]:


var_c_s = set(var_c) - set(['PromCnt12','PromCnt36',
                            'PromCntCard12','DemAge',
                            'DemPctVeterans','DemMedIncome'])
var_c_s = list(var_c_s)


# In[10]:


var_c_s


# + 分类变量筛选-方差分析

# In[11]:


var_d


# In[12]:


import statsmodels.stats.anova as anova
from statsmodels.formula.api import ols


# In[13]:


for i in var_d:
    formula = "TARGET_D ~ " + str(i)
    print(anova.anova_lm(ols(formula,data = model_data[var_d+['TARGET_D']]).fit()))


# In[14]:


var_d_s = list(set(var_d) - set(["DemHomeOwner"]))
var_d_s


# # 对每个变量的E（探索）阶段

# ## 对连续变量的统计探索

# In[15]:


X = model_data[var_c_s + var_d_s].copy()
Y = model_data[y].copy()


# In[16]:


model_data[var_c_s+var_d_s].head()


# In[17]:


# 描述性统计分析
X[var_c_s].describe().T


# In[18]:


# 利用众数减去中位数的差值除以四分位距来查找是否有可能存在异常值
abs((X[var_c_s].mode().iloc[0,] - X[var_c_s].median()) /
    (X[var_c_s].quantile(0.75) - X[var_c_s].quantile(0.25)))

#%%
#发现以下两个变量最可疑
X["PromCntAll"].hist()
#%%
X["DemMedHomeValue"].hist()
X["DemMedHomeValue"].describe().T
# ## 对分类变量的统计探索

# In[19]:


X["DemGender"].value_counts()


# In[20]:


X["StatusCat96NK"].value_counts()#有的水平数量太少


# In[21]:


X["DemCluster"].value_counts()[:10]#有的水平数量太少


# # 针对有问题的变量进行M（修改）的阶段

# ## 连续变量
# 
# 将变量中错误值替换为缺失值，然后进行缺失值填补

# In[22]:


X['DemMedHomeValue'].replace(0, np.nan, inplace = True)


# In[23]:


# 查看缺失比例
1 - (X.describe().T["count"]) / len(X)


# In[24]:


GiftAvgCard36_fill = X["GiftAvgCard36"].median()
DemMedHomeValue_fill = X["DemMedHomeValue"].median()

X["GiftAvgCard36"].fillna(GiftAvgCard36_fill,inplace = True)
X["DemMedHomeValue"].fillna(DemMedHomeValue_fill,inplace = True)


# In[25]:


# fill erroe 1、2
DATA_CLEAN.append({"GiftAvgCard36_fill":GiftAvgCard36_fill})
DATA_CLEAN.append({"DemMedHomeValue_fill":DemMedHomeValue_fill})


# - 解释变量分布转换

# In[26]:


for i in var_c_s:
    print(i)
    plt.hist(X[i], bins=20)
    plt.show()


# In[27]:


skew_var_x = {}
for i in var_c_s:
    skew_var_x[i]=abs(X[i].skew())
    
skew = pd.Series(skew_var_x).sort_values(ascending=False)
skew


# In[28]:


# 将偏度大于1的变量进行对数运算


# In[29]:


var_x_ln = skew[skew >= 1].index
var_x_ln


# In[30]:


# 3
DATA_CLEAN.append({"var_x_ln":var_x_ln})


# In[31]:


for i in var_x_ln:
    if min(X[i]) <= 0:
        X[i] = np.log(X[i] + abs(min(X[i])) + 0.01)
    else:
        X[i] = np.log(X[i])


# In[32]:


skew_var_x = {}
for i in var_c_s:
    skew_var_x[i]=abs(X[i].skew())

skew = pd.Series(skew_var_x).sort_values(ascending=False)
skew


# ## 分类变量

# - 水平数过多的分类变量进行水平合并

# In[33]:


var_d_s


# In[34]:


# 统计每个水平的对应目标变量的均值，和每个水平数量

DemC_group = model_data[['DemCluster','TARGET_D']].groupby('DemCluster',
                                                           as_index = False)
DemC_C= DemC_group['TARGET_D'].agg({'mean' : 'mean',
                                    'count':'count',
                                    "median":"median"}).sort_values(["median","mean"])

DemC_C["count_cumsum"] = DemC_C["count"].cumsum()
DemC_C["new_DemCluster"] = DemC_C["count_cumsum"].apply(lambda x:
                                                        x//(len(model_data)/10)+1)
DemC_C["new_DemCluster"] = DemC_C["new_DemCluster"].astype(int)

DemC_C.head()


# In[35]:


# 将重编码信息保存至数据清洗信息当中.4

DemCluster_new_class = DemC_C[["DemCluster","new_DemCluster"]].set_index("DemCluster")
DATA_CLEAN.append(DemCluster_new_class.to_dict())


# 根据重编码替换原数据

# In[36]:


X["DemCluster"] = X["DemCluster"].map(DemCluster_new_class.to_dict()['new_DemCluster'])


# In[37]:


new_DemGender = {"F":1,"M":2,"U":3}

# 5
DATA_CLEAN.append({"new_DemGender":new_DemGender})

X['DemGender'] = X['DemGender'].map(new_DemGender)


# In[ ]:


StatusCat96NK_group = model_data[['StatusCat96NK','TARGET_D']].groupby('StatusCat96NK', as_index = False)
StatusCat96NK_class = StatusCat96NK_group['TARGET_D'].agg({'mean' : 'mean', 'count':'count',"median":"median"}).sort_values(["median","mean"])

StatusCat96NK_class


# In[40]:


new_StatusCat96NK = {"S":1,"A":2,"E":2,"N":2,"F":2,"L":2}

# 6
DATA_CLEAN.append({"new_StatusCat96NK":new_StatusCat96NK})

X['StatusCat96NK'] = X['StatusCat96NK'].map(new_StatusCat96NK)


# In[45]:


X.shape


# In[46]:


X.head()


# ***

# ##  前向选择法筛选变量

# In[47]:


import statsmodels.formula.api as smf
def forward_selected(data, response):
    """
    Linear model designed by forward selection.

    Parameters:
    -----------
    data : pandas DataFrame with all possible predictors and response

    response: string, name of response column in data

    Returns:
    --------
    model: an "optimal" fitted statsmodels linear model
           with an intercept
           selected by forward selection
           evaluated by adjusted R-squared
    """
    remaining = set(data.columns)
    remaining.remove(response)
    selected = []
    current_score, best_new_score = 0.0, 0.0
    while remaining and current_score == best_new_score:
        scores_with_candidates = []
        for candidate in remaining:
            formula = "{} ~ {} + 1".format(response,
                                           ' + '.join(selected + [candidate]))
            score = smf.ols(formula, data).fit().rsquared_adj
            scores_with_candidates.append((score, candidate))
        scores_with_candidates.sort()
        best_new_score, best_candidate = scores_with_candidates.pop()
        if current_score < best_new_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_new_score
    formula = "{} ~ {} + 1".format(response,
                                   ' + '.join(selected))
    model = smf.ols(formula, data).fit()
    return selected


# In[48]:


final_var = forward_selected(pd.concat([X[var_c_s+var_d_s],Y],axis = 1), 'TARGET_D')


# In[49]:


final_var


# In[50]:


# 7
DATA_CLEAN.append({"final_var":final_var})


# In[51]:


var_c_s = list(set(var_c_s)&set(final_var))
var_c_s


# In[52]:


var_d_s = list(set(var_d_s)&set(final_var))
var_d_s


# In[53]:


model_final = pd.concat([X[var_d_s + var_c_s],Y], axis = 1)
model_final.columns


# # 建立线性回归模型M（建模）阶段

# - 使用筛选出的变量进行线性回归

# In[60]:


import statsmodels.api as sm
from statsmodels.formula.api import ols

# fit our model with .fit() and show results
# we use statsmodels' formula API to invoke the syntax below,
# where we write out the formula using ~

X = model_final.iloc[:,:-1]
Y = model_final.iloc[:,-1]

formula = 'TARGET_D ~ ' + '+'.join(final_var)
    
donation_model = ols(formula,model_final).fit()
# summarize our model
print(donation_model.summary())


# # 模型验证A（验证）阶段

# ## 对线性回归模型进行评估

# 参照教材，可通过回归模型的统计汇总信息，对模型拟合程度，系数相关程度等进行评价，并重新调整。

# ## 模型永久化

# In[61]:


import pickle as pickle
with open(r'liner.model', 'wb') as model_file:
    pickle.dump(donation_model, model_file)


# In[62]:


assert len(DATA_CLEAN) == 7


# In[63]:


for i,j in enumerate(DATA_CLEAN):
    print(i,j.keys())


# In[64]:


with open(r'liner.dataclean', 'wb') as f:
    pickle.dump(DATA_CLEAN, f)

#%%
