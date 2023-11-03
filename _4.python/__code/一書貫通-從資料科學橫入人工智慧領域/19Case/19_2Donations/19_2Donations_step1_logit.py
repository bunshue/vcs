
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc" style="margin-top: 1em;"><ul class="toc-item"><li><span><a href="#数据挖掘方法论──SEMMA模型训练使用流程" data-toc-modified-id="数据挖掘方法论──SEMMA模型训练使用流程-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>数据挖掘方法论──SEMMA模型训练使用流程</a></span></li><li><span><a href="#数据获取与导入的S（抽样）阶段。" data-toc-modified-id="数据获取与导入的S（抽样）阶段。-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>数据获取与导入的S（抽样）阶段。</a></span><ul class="toc-item"><li><span><a href="#规整数据集" data-toc-modified-id="规整数据集-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>规整数据集</a></span></li><li><span><a href="#筛选预测能力强的变量" data-toc-modified-id="筛选预测能力强的变量-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>筛选预测能力强的变量</a></span></li><li><span><a href="#根据IV值筛选变量---分类变量" data-toc-modified-id="根据IV值筛选变量---分类变量-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>根据IV值筛选变量 - 分类变量</a></span></li><li><span><a href="#根据IV值筛选变量-连续变量" data-toc-modified-id="根据IV值筛选变量-连续变量-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>根据IV值筛选变量-连续变量</a></span></li></ul></li><li><span><a href="#针对每个变量的E（探索）阶段" data-toc-modified-id="针对每个变量的E（探索）阶段-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>针对每个变量的E（探索）阶段</a></span><ul class="toc-item"><li><span><a href="#对连续变量的统计探索" data-toc-modified-id="对连续变量的统计探索-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>对连续变量的统计探索</a></span></li><li><span><a href="#对分类变量的统计探索" data-toc-modified-id="对分类变量的统计探索-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>对分类变量的统计探索</a></span></li></ul></li><li><span><a href="#针对有问题的变量进行修改的M（修改）阶段" data-toc-modified-id="针对有问题的变量进行修改的M（修改）阶段-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>针对有问题的变量进行修改的M（修改）阶段</a></span><ul class="toc-item"><li><span><a href="#将连续变量的错误值改为缺失值" data-toc-modified-id="将连续变量的错误值改为缺失值-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>将连续变量的错误值改为缺失值</a></span></li><li><span><a href="#将连续变量的缺失值用中位数填补" data-toc-modified-id="将连续变量的缺失值用中位数填补-4.2"><span class="toc-item-num">4.2&nbsp;&nbsp;</span>将连续变量的缺失值用中位数填补</a></span></li><li><span><a href="#对分类水平过多的变量进行合并（或概化）" data-toc-modified-id="对分类水平过多的变量进行合并（或概化）-4.3"><span class="toc-item-num">4.3&nbsp;&nbsp;</span>对分类水平过多的变量进行合并（或概化）</a></span></li><li><span><a href="#解释变量分布转换" data-toc-modified-id="解释变量分布转换-4.4"><span class="toc-item-num">4.4&nbsp;&nbsp;</span>解释变量分布转换</a></span></li><li><span><a href="#变量压缩" data-toc-modified-id="变量压缩-4.5"><span class="toc-item-num">4.5&nbsp;&nbsp;</span>变量压缩</a></span></li></ul></li><li><span><a href="#建立逻辑回归模型M（建模）阶段" data-toc-modified-id="建立逻辑回归模型M（建模）阶段-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>建立逻辑回归模型M（建模）阶段</a></span><ul class="toc-item"><li><span><a href="#分成训练集和测试集，比例为6:4" data-toc-modified-id="分成训练集和测试集，比例为6:4-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>分成训练集和测试集，比例为6:4</a></span></li><li><span><a href="#模型训练" data-toc-modified-id="模型训练-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>模型训练</a></span></li></ul></li><li><span><a href="#模型验证A（验证）阶段" data-toc-modified-id="模型验证A（验证）阶段-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>模型验证A（验证）阶段</a></span><ul class="toc-item"><li><span><a href="#对逻辑回归模型进行评估" data-toc-modified-id="对逻辑回归模型进行评估-6.1"><span class="toc-item-num">6.1&nbsp;&nbsp;</span>对逻辑回归模型进行评估</a></span></li><li><span><a href="#构建神经网络并评估" data-toc-modified-id="构建神经网络并评估-6.2"><span class="toc-item-num">6.2&nbsp;&nbsp;</span>构建神经网络并评估</a></span></li><li><span><a href="#模型永久化" data-toc-modified-id="模型永久化-6.3"><span class="toc-item-num">6.3&nbsp;&nbsp;</span>模型永久化</a></span></li></ul></li></ul></div>

# 本代码案例为 **两阶段精准营销模型** 中的 **构造营销响应模型** 部分
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
# 
# # 数据获取与导入的S（抽样）阶段。
# 
# ## 规整数据集

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#需要把woe所在的目录"D:\Python_book\19Case\19_2Donations"设置到python工作目录，
#设置方式为Tools->PYTHONPATH manager 
from woe import WoE # 从本地导入
import os
os.chdir(r"D:\Python_book\19Case\19_2Donations")


# In[2]:
# 创建一个列表，用来保存所有的建模数据清洗的相关信息
DATA_CLEAN = []
# In[3]:
model_data = pd.read_csv("donations2.csv").drop(["ID","TARGET_D"],1)
model_data.head()
# In[4]:
model_data.dtypes

# In[5]:
# 目标变量
y = 'TARGET_B'

# 连续变量
var_c = ["GiftCnt36","GiftCntAll","GiftCntCard36",
         "GiftCntCardAll","GiftTimeLast","GiftTimeFirst",
         "PromCnt12","PromCnt36","PromCntAll",
         "PromCntCard12","PromCntCard36","PromCntCardAll",
         "StatusCatStarAll","DemAge","DemMedHomeValue",
         "DemPctVeterans","DemMedIncome","GiftAvgLast",
         "GiftAvg36","GiftAvgAll","GiftAvgCard36"]

# 分类变量
var_d = ['StatusCat96NK', 'DemHomeOwner', 'DemGender', 'DemCluster']
# In[6]:
X = model_data[var_c + var_d].copy()

Y = model_data[y].copy()


# ## 筛选预测能力强的变量

# **WoE类参数说明**:
# + **qnt_num**:int,等频分箱个数,默认16
# + **min_block_size**:int,最小观测数目，默认16
# + **spec_values**:dict,若为分类自变量，指派替换值
# + **v_type**:str,自变量类型,分类:‘d’,连续变量:‘c’，默认'c'
# + **bins**:list,预定义的连续变量分箱区间
# + **t_type**:str,目标变量类型,二分类:‘b’,连续变量:‘c’，默认'b'

# **WoE类重要方法**:
# 
# + **plot**:绘制WOE图
# + **transform**:转换数据为WOE数据
# + **fit_transform**:转换数据为WOE数据
# + **optimize**:连续变量使用最优分箱

# **WoE类重要属性**:
# + **bins**:分箱结果汇总
# + **iv**:变量的信息价值

# ## 根据IV值筛选变量 - 分类变量

# In[7]:
iv_d = {}
for i in var_d:
    iv_d[i] = WoE(v_type='d').fit(X[i].copy(), Y.copy()).iv

pd.Series(iv_d).sort_values(ascending = False)


# In[8]:


# 保留iv值较高的分类变量
var_d_s = ['StatusCat96NK', 'DemCluster']


# ## 根据IV值筛选变量-连续变量

# In[9]:


iv_c = {}
for i in var_c:
    iv_c[i] = WoE(v_type='c',t_type='b',qnt_num=3).fit(X[i],Y).iv 

sort_iv_c = pd.Series(iv_c).sort_values(ascending=False)
sort_iv_c


# In[10]:


# 以 2% 作为选取变量的阈值
var_c_s = list(sort_iv_c[sort_iv_c > 0.02].index)
var_c_s
# In[11]:
X = model_data[var_c_s + var_d_s].copy()
Y = model_data[y].copy()


# # 针对每个变量的E（探索）阶段

# ## 对连续变量的统计探索

# In[12]:


X[var_c_s].describe().T


# In[13]:


# 利用众数减去中位数的差值除以四分位距来查找是否有可能存在异常值
abs((X[var_c_s].mode().iloc[0,] - X[var_c_s].median()) /
    (X[var_c_s].quantile(0.75) - X[var_c_s].quantile(0.25)))


# In[14]:
# 对嫌疑最大的几个变量进行可视化分析
plt.hist(X["PromCntAll"], bins=20);

# ## 对分类变量的统计探索
#查看是否分类过多
# In[15]:
X["StatusCat96NK"].value_counts()

# In[16]:
len(X["DemCluster"].value_counts())

# # 针对有问题的变量进行修改的M（修改）阶段

# ## 将连续变量的错误值改为缺失值

# In[17]:

# 本模型中筛选后的变量,没有发现无错误值

# ## 将连续变量的缺失值用中位数填补

# In[18]:


# 查看缺失比例
1 - (X.describe().T["count"]) / len(X)
# In[19]:
fill_GiftAvgCard36 = X.GiftAvgCard36.median()
X.GiftAvgCard36.fillna(value=fill_GiftAvgCard36, inplace=True)
# In[20]:
# 将填补修改信息保存至数据清洗信息当中.1
DATA_CLEAN.append({"fill_GiftAvgCard36":fill_GiftAvgCard36})

# ## 对分类水平过多的变量进行合并（或概化）

# In[21]:
var_d_s
# In[24]:


# 统计每个水平的对应目标变量的均值，和每个水平数量

DemCluster_grp = model_data[['DemCluster',
                             'TARGET_B']].groupby('DemCluster',as_index = False)

DemC_C = DemCluster_grp['TARGET_B'].agg({'mean' : 'mean',
                                                   'count':'count'}).sort_values("mean")


# In[25]:


# 将这些类别尽量以人数大致均等的方式以响应率为序归结为10个大类
DemC_C["count_cumsum"] = DemC_C["count"].cumsum()
DemC_C["new_DemCluster"] = DemC_C["count_cumsum"].apply(lambda x: x//(len(model_data)/10))
DemC_C["new_DemCluster"] = DemC_C["new_DemCluster"].astype(int)


# In[26]:


DemC_C.groupby("new_DemCluster")["count"].sum()


# In[27]:

# 将重编码信息保存至数据清洗信息当中.2
DemCluster_new_class = DemC_C[["DemCluster","new_DemCluster"]].set_index("DemCluster")
DATA_CLEAN.append(DemCluster_new_class.to_dict())


# 根据重编码替换原数据

# In[28]:


X["DemCluster"] = X["DemCluster"].map(DATA_CLEAN[1]['new_DemCluster'])


# In[29]:


X.head()


# In[30]:


X.DemCluster.value_counts()


# 对分类变量进行woe转换

# In[31]:


X_rep = X.copy()


# In[32]:
#以下是根据概化之后的分类变量进行Woe转换.
#目前有一个Scorecardpy的包可以实现自动化分箱，可以用来试用，但是还没有经过全面的测试，不可直接使用。

for i in var_d_s:
    X_rep[i+"_woe"] = WoE(v_type='d').fit_transform(X_rep[i],Y)


# In[33]:
# 将woe转换的过程保存.3、4
StatusCat96NK_woe = X_rep[["StatusCat96NK","StatusCat96NK_woe"]].drop_duplicates().set_index("StatusCat96NK").to_dict()
DemCluster_woe = X_rep[["DemCluster","DemCluster_woe"]].drop_duplicates().set_index("DemCluster").to_dict()

DATA_CLEAN.append(StatusCat96NK_woe)
DATA_CLEAN.append(DemCluster_woe)


# In[34]:


del X_rep["StatusCat96NK"]
del X_rep["DemCluster"]


# In[35]:
X_rep.rename(columns={"StatusCat96NK_woe":"StatusCat96NK","DemCluster_woe":"DemCluster"},inplace=True)


# 通过随机森林对变量的重要性进行筛选

# In[36]:
import sklearn.ensemble as ensemble
rfc = ensemble.RandomForestClassifier(criterion='entropy', n_estimators=3, max_features=0.5, min_samples_split=5)
rfc_model = rfc.fit(X_rep, Y)
rfc_model.feature_importances_
rfc_fi = pd.DataFrame()
rfc_fi["features"] = list(X.columns)
rfc_fi["importance"] = list(rfc_model.feature_importances_)
rfc_fi=rfc_fi.set_index("features",drop=True)
var_sort = rfc_fi.sort_values(by="importance",ascending=False)
var_sort.plot(kind="bar");


# In[37]:


# 以 2% 作为选取变量的阈值
var_x = list(var_sort.importance[var_sort.importance > 0.02].index)
var_x


# ## 解释变量分布转换

# 查看解释变量的分布情况

# In[38]:


for i in var_x:
    print(i)
    plt.hist(X_rep[i], bins=20)
    plt.show()


# In[39]:


skew_var_x = {}
for i in var_x:
    skew_var_x[i] = abs(X_rep[i].skew())
    
skew = pd.Series(skew_var_x).sort_values(ascending=False)
skew


# In[40]:


# 将偏度大于1的变量进行对数运算
var_x_ln = skew.index[skew > 1]
var_x_ln


# In[41]:


# 加入数据清洗.5
DATA_CLEAN.append({"val_x_ln":var_x_ln})


# In[42]:


for i in var_x_ln:
    if min(X_rep[i]) <= 0:
        X_rep[i] =np.log(X_rep[i] + abs(min(X_rep[i])) + 0.01)
    else:
        X_rep[i] =np.log(X_rep[i])


# In[43]:


skew_var_x = {}
for i in var_x:
    skew_var_x[i]=abs(X_rep[i].skew())

skew = pd.Series(skew_var_x).sort_values(ascending=False)
skew


# ## 变量压缩

# In[44]:
from sklearn import preprocessing
pcadata = preprocessing.scale(X_rep)
# - 4、使用sklearn的主成分分析，用于判断保留主成分的数量

# In[5]:
from sklearn.decomposition import PCA
'''
此处作主成分分析，主要是进行冗余变量的剔出，因此注意以下两个原则：
1、保留的变量个数尽量多，累积的explained_variance_ratio_尽量大，比如阈值设定为0.95
2、只剔出单位根非常小的变量，比如阈值设定为0.2
'''
pca=PCA(n_components=14)
pca.fit(pcadata)
print(pca.explained_variance_)#建议保留9个主成分
print(pca.explained_variance_ratio_)#建议保留8个主成分

#%%
from VarSelec import Var_Select


# In[45]:Var_Select(orgdata, k,alphaMin=10, alphaMax=20, alphastep=0.2)

X_rep_reduc = Var_Select(X_rep, k=8, alphaMin=0.1,alphaMax=200, alphastep=0.5)
X_rep_reduc.head()

#如果报best_alpha没有定义的错误，请扩大alphaMax的取值
# In[46]:


X_rep_reduc_corr=X_rep_reduc.corr()


# In[47]:


# 最后选择的变量为
list(X_rep_reduc.columns)


# In[48]:


# 添加清洗.6
DATA_CLEAN.append({"final_var":list(X_rep_reduc.columns)})


# In[49]:


assert len(DATA_CLEAN) == 6, "确保没有重复添加清洗需要的数据"


# In[50]:


X_rep_reduc.head()


# # 建立逻辑回归模型M（建模）阶段

# ## 分成训练集和测试集，比例为6:4

# In[51]:


import sklearn.model_selection as model_selection
ml_data = model_selection.train_test_split(X_rep_reduc, Y, test_size=0.3, random_state=0)
train_data, test_data, train_target, test_target = ml_data


# ## 模型训练

# - 使用全部变量进行logistic回归

# In[52]:


from sklearn import preprocessing
min_max_scaler = preprocessing.MinMaxScaler()

train_data = min_max_scaler.fit_transform(train_data)
test_data = min_max_scaler.fit_transform(test_data)
train_data


# In[53]:


import sklearn.linear_model as linear_model
logistic_model = linear_model.LogisticRegression(class_weight = None,
                                                 dual = False,
                                                 fit_intercept = True,
                                                 intercept_scaling = 1,
                                                 penalty = 'l1',
                                                 random_state = None,
                                                 tol = 0.001)


# In[54]:


from sklearn.model_selection import ParameterGrid, GridSearchCV

C = np.logspace(-3,0,20,base=10)

param_grid = {'C': C}

clf_cv = GridSearchCV(estimator=logistic_model, 
                      param_grid=param_grid, 
                      cv=5, 
                      scoring='roc_auc')

clf_cv.fit(train_data, train_target)


# In[55]:


logistic_model = linear_model.LogisticRegression(C=clf_cv.best_params_["C"],
                                                 class_weight=None,
                                                 dual=False,
                                                 fit_intercept=True,
                                                 intercept_scaling=1,
                                                 penalty='l1',
                                                 random_state=None,
                                                 tol=0.001)
logistic_model.fit(train_data, train_target)


# In[59]:


logistic_model.coef_#表明第一个变量被剔除
X_rep_reduc=X_rep_reduc.drop(["PromCntCardAll"],1)

# In[60]:


import statsmodels.api as sm
import statsmodels.formula.api as smf

model=X_rep_reduc.join(train_target)

formula = "TARGET_B ~ " + "+".join(X_rep_reduc)
lg_m = smf.glm(formula=formula, data=model, 
             family=sm.families.Binomial(sm.families.links.logit)).fit()
lg_m.summary()


# # 模型验证A（验证）阶段

# ## 对逻辑回归模型进行评估

# In[58]:


test_est = logistic_model.predict(test_data)
train_est = logistic_model.predict(train_data)


# In[59]:


test_est_p = logistic_model.predict_proba(test_data)[:,1]
train_est_p = logistic_model.predict_proba(train_data)[:,1]


# In[60]:
# - 目标样本和非目标样本的分数分布

# In[64]:


import seaborn as sns
red, blue = sns.color_palette("Set1",2)


# In[65]:


sns.kdeplot(test_est_p[test_target==1], shade=True, color=red)
sns.kdeplot(test_est_p[test_target==0], shade=True, color=blue)


# - ROC曲线

# In[66]:
import sklearn.metrics as metrics

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_est_p)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_est_p)
plt.figure(figsize=[6,6])
plt.plot(fpr_test, tpr_test, color=blue)
plt.plot(fpr_train, tpr_train, color=red)
plt.title('ROC curve')
print('AUC = %6.4f' %metrics.auc(fpr_test, tpr_test))


# In[67]:


test_x_axis = np.arange(len(fpr_test))/float(len(fpr_test))
train_x_axis = np.arange(len(fpr_train))/float(len(fpr_train))
plt.figure(figsize=[6,6])
plt.plot(fpr_test, test_x_axis, color=blue)
plt.plot(tpr_test, test_x_axis, color=blue)
plt.plot(fpr_train, train_x_axis, color=red)
plt.plot(tpr_train, train_x_axis, color=red)
plt.title('KS curve')


# ## 构建神经网络并评估

# In[68]:


from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(train_data)

scaled_train_data = scaler.transform(train_data)
scaled_test_data = scaler.transform(test_data)


# In[69]:


from sklearn.neural_network import MLPClassifier

mlp = MLPClassifier(hidden_layer_sizes=(10,), 
                    activation='logistic', alpha=0.1, max_iter=1000)


# In[70]:


from sklearn.model_selection import GridSearchCV
from sklearn import metrics

param_grid = {
    'hidden_layer_sizes':[(10, ), (15, ), (20, ), (5, 5)],
    'activation':['logistic', 'tanh', 'relu'], 
    'alpha':[0.001, 0.01, 0.1, 0.2, 0.4, 1, 10]
}
mlp = MLPClassifier(max_iter=1000)
gcv = GridSearchCV(estimator=mlp, param_grid=param_grid, 
                   scoring='roc_auc', cv=4, n_jobs=-1)
gcv.fit(scaled_train_data, train_target)


# In[71]:


gcv.best_params_


# In[72]:


mlp = MLPClassifier(hidden_layer_sizes=gcv.best_params_["hidden_layer_sizes"], 
                    activation=gcv.best_params_["activation"], alpha=gcv.best_params_["alpha"], max_iter=1000)

mlp.fit(scaled_train_data, train_target)


# In[73]:


train_predict = mlp.predict(scaled_train_data)
test_predict = mlp.predict(scaled_test_data)


# In[74]:


train_proba = mlp.predict_proba(scaled_train_data)[:, 1]  
test_proba = mlp.predict_proba(scaled_test_data)[:, 1]


# In[75]:


from sklearn import metrics

print(metrics.confusion_matrix(test_target, test_predict, labels=[0, 1]))
print(metrics.classification_report(test_target, test_predict))


# In[76]:


fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_proba)

plt.figure(figsize=[4, 4])
plt.plot(fpr_test, tpr_test, 'b-')
plt.plot(fpr_train, tpr_train, 'r-')
plt.title('ROC curve')
plt.show()

print('AUC = %6.4f' %metrics.auc(fpr_test, tpr_test))

#发现神经网络没有提升效果，因此仍然保留逻辑回归模型
# ## 模型永久化

# In[77]:


import pickle as pickle


# In[78]:


# 使用with语句确保文件关闭
with open(r'logitic.model', 'wb') as f:
    pickle.dump(logistic_model, f)


# In[79]:


with open(r'logitic.model', 'rb') as f:
    model_load = pickle.load(f)


# In[80]:


test_est_load = model_load.predict(test_data)


# In[81]:


pd.crosstab(test_est_load,test_est)


# 把清洗过程中使用的数据也保存到文件当中

# In[82]:


with open(r'logitic.dataclean', 'wb') as f:
    pickle.dump(DATA_CLEAN, f)
#%%

