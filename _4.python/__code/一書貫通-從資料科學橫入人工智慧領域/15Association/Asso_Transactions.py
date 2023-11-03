
# coding: utf-8

# # 关联规则介绍

# In[ ]:


import pandas as pd
#from Apriori import *
#需要把Apriori所在的目录"D:\Python_book\15Association\myscripts1"设置到python工作目录，
#设置方式为Tools->PYTHONPATH manager 
import Apriori as apri
import matplotlib.pyplot as plt


# ## 数据载入

# 原数据为倒排表数据

# In[ ]:
#Transactions---自行车及周边物品的销售数据

inverted=pd.read_csv(r'D:\Python_book\15Association\Transactions.csv')
inverted.head()


# ## 数据转换

# 倒排表数据转换为相应的二维列表数据

# In[ ]:


idataset=apri.dataconvert(inverted,tidvar='OrderNumber',itemvar='Model',data_type = 'inverted')
idataset[:5]


# ## 关联规则

# 参数说明:
# 
# + minSupport:最小支持度阈值
# + minConf:最小置信度阈值
# + minlen:规则最小长度
# + maxlen:规则最大长度

# 这里，minSupport或minConf设定越低，产生的规则越多，计算量也就越大
# 
# 设定参数为:minSupport=0.05,minConf=0.5,minlen=1,maxlen=10

# In[ ]:


res = apri.arules(idataset,minSupport=0.01,minConf=0.1,minlen=1,maxlen=2)


# ## 产生关联规则

# + 规定提升度要大于1,并按照置信度进行排序

# In[ ]:


res.ix[res.lift>1,:].sort_values('support',ascending=False).head(20)


# ## 关联规则结果汇总

# In[ ]:


res.plot.scatter(3,4,c=5,figsize=(4,4))
plt.xlabel('support')
plt.ylabel('confidence')


#%%
#互补品
res.ix[res.lift>1,['lhs','rhs','lift']].sort_values('lift',ascending=False).head(20)
#%%
#互斥品
res.ix[res.lift<1,['lhs','rhs','lift']].sort_values('lift',ascending=True).head(20)

#%%
#如果一个新客户刚刚下但了Mountain-200这个产品,如果希望获得最高的营销响应率,那在他的付费成功页面上最应该推荐什么产品?
Mountain_200=res.loc[res.lhs==frozenset({'Mountain-200'}),:]

res.ix[res.lhs==frozenset({'Mountain-200'}),['rhs','support','confidence','lift']].sort_values('confidence',ascending=False).head(20)


#%%
#如果一个新客户刚刚下但了Mountain-200这个产品,如果希望最大化提升总体的产品销售额,那在他的付费成功页面上最应该推荐什么产品?
Mountain_200=res.loc[res.lhs==frozenset({'Mountain-200'}),:]

res.ix[res.lhs==frozenset({'Mountain-200'}),['rhs','support','confidence','lift']].sort_values('lift',ascending=False).head(20)




#%%
#如果希望推荐Sport-100 自行车，应该如何制定营销策略
Sport_100=res.loc[res.rhs==frozenset({'Sport-100'}),:]

res.ix[res.rhs==frozenset({'Sport-100'}),['lhs','support','confidence','lift']].sort_values('lift',ascending=False).head(20)




#%%




















