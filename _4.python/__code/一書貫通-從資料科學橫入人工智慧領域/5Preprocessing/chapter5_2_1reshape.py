
# coding: utf-8

# # 第5章 数据整合和数据清洗
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# ### 5.1.1 行列操作 

# #### 1. 单列

# In[7]:

import pandas as pd
import numpy as np
#%%

# ### 拆分、堆叠列

# In[3]:
table = pd.DataFrame({'cust_id':[10001,10001,10002,10002,10003],
                      'type':['Normal','Special_offer',\
                              'Normal','Special_offer','Special_offer'],
                      'Monetary':[3608,420,1894,3503,4567]})


# In[4]:

table


# In[24]:

result=pd.pivot_table(table,index='cust_id',columns='type',values='Monetary')


# In[25]:

pd.pivot_table(table,index='cust_id',columns='type',values='Monetary',
        fill_value=0,aggfunc='sum')


# In[27]:

table1 = pd.pivot_table(table,index='cust_id',
                        columns='type',
                        values='Monetary',
                        fill_value=0,
                        aggfunc=np.sum).reset_index()
table1


# In[28]:

pd.melt(table1,
	id_vars='cust_id',
value_vars=['Normal','Special_offer'],
value_name='Monetary',
var_name='TYPE')



# In[ ]:
####################################################################################################

# coding: utf-8

# # 第5章3 RFM
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ### 1. 导入数据

# In[5]:

import pandas as pd
import numpy as np
trad_flow = pd.read_csv(r'D:\Python_Training\script_Python\5Preprocessing\RFM_TRAD_FLOW.csv', encoding='gbk')
trad_flow.head(10)


# ### 2.计算 RFM

# In[6]:

M=trad_flow.groupby(['cumid','type'])[['amount']].sum()


# In[7]:

M_trans=pd.pivot_table(M,index='cumid',columns='type',values='amount')


# In[8]:

F=trad_flow.groupby(['cumid','type'])[['transID']].count()
F.head()


# In[9]:

F_trans=pd.pivot_table(F,index='cumid',columns='type',values='transID')
F_trans.head()


# In[10]:

R=trad_flow.groupby(['cumid','type'])[['time']].max()
R.head()


# In[11]:

#R_trans=pd.pivot_table(R,index='cumid',columns='type',values='time')
#R_trans.head()


# ### 3.衡量客户对打折商品的偏好

# In[12]:

M_trans['Special_offer']= M_trans['Special_offer'].fillna(0)


# In[13]:

M_trans['spe_ratio']=M_trans['Special_offer']/(M_trans['Special_offer']+M_trans['Normal'])
M_rank=M_trans.sort_values('spe_ratio',ascending=False,na_position='last').head()


# In[16]:

M_rank['spe_ratio_group'] = pd.qcut( M_rank['spe_ratio'], 4) # 这里以age_oldest_tr字段等宽分为4段
M_rank.head()


# In[ ]:








