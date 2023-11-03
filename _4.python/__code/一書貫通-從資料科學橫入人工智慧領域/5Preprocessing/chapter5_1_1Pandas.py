
# coding: utf-8

# # 第5章 数据整合和数据清洗
# - pandas学习参考： [十分钟搞定pandas](http://www.cnblogs.com/chaosimple/p/4153083.html)

# ## 5.1　数据整合

# ### 5.1.1 行列操作 

# #### 1. 单列

# In[7]:

import pandas as pd
import numpy as np
sample = pd.DataFrame(np.random.randn(4, 5),
                     columns=['a','b','c','d','e'])
sample


# In[2]:

sample['a']


# In[3]:

sample.ix[:,'a']


# In[4]:

sample[['a']]


# #### 2. 选择多行和多列 

# In[8]:

sample.ix[0:2, 0:2]


# #### 3. 创建、删除列 

# In[10]:

sample['new_col1'] = sample['a'] - sample['b']
sample


# In[16]:

sample_new=sample.assign(new_col2 = sample['a'] - sample['b'],
                  new_col3 = sample['a'] + sample['b'])
sample_new


# In[24]:

sample.drop('a',axis=1)


# ### 5.1.2 条件查询

# In[25]:

sample =pd.DataFrame({'name':['Bob','Lindy','Mark',
                                     'Miki','Sully','Rose'],
						'score':[98,78,87,77,65,67],
						'group':[1,1,1,2,1,2],})
sample


# #### 1. 单条件 

# In[30]:

#sample.score > 70
sample[sample.score > 70]


# #### 2. 多条件

# In[32]:

sample[(sample.score > 70) & (sample.group ==1)]


# #### 3. 使用query

# In[33]:

#sample.query('score > 90')
sample.query('(group ==2) |(group == 1)')


# #### 4. 其他

# In[34]:

sample[sample['score'].between(70,80,inclusive=True)]


# In[35]:

sample[sample['name'].isin(['Bob','Lindy'])]


# In[36]:

sample[sample['name'].str.contains('[M]+')]


# ### 5.1.3 横向连接

# In[37]:

df1 = pd.DataFrame({'id':[1,2,3],
                    'col1':['a','b','c']})
df2 = pd.DataFrame({'id':[4,3],
                    'col2':['d','e']})


# #### 1. 内连接

# In[38]:

df1.merge(df2,how='inner',left_on='id',right_on='id')


# #### 2. 外连接

# In[40]:

df1.merge(df2,how='left',on='id')


# #### 3. 行索引连接

# In[41]:

df1 = pd.DataFrame({'id1':[1,2,3],
                    'col1':['a','b','c']},
                  index = [1,2,3])
df2 = pd.DataFrame({'id2':[1,2,3],
                    'col2':['aa','bb','cc']},
                  index = [1,3,2])


# In[42]:

pd.concat([df1,df2],axis=1)
#df1.join(df2)


# ### 5.1.4 纵向合并

# In[43]:

df1 = pd.DataFrame({'id':[1,1,1,2,3,4,6],
                    'col':['a','a','b','c','v','e','q']})
df2 = pd.DataFrame({'id':[1,2,3,3,5],
                    'col':['x','y','z','v','w']})


# In[44]:

pd.concat([df1,df2],ignore_index=True,axis=0)


# In[45]:

pd.concat([df1,df2],ignore_index=True).drop_duplicates()


# In[46]:

df3 = df1.rename(columns = {'col':'new_col'})


# In[47]:

pd.concat([df1,df3],ignore_index=True).drop_duplicates()


# ### 5.1.5 排序

# #### 1. 排序

# In[50]:

sample=pd.DataFrame({'name':['Bob','Lindy','Mark','Miki','Sully','Rose'],'score':[98,78,87,77,77,np.nan],'group':[1,1,1,2,1,2],})


# In[51]:

sample


# In[52]:

sample.sort_values('score',ascending=False,na_position='last')


# In[53]:

sample.sort_values(['group','score'])


# ### 5.1.6 分组汇总

# In[8]:

sample = pd.read_csv(r'D:\Python_book\5Preprocessing\sample.csv', encoding='gbk')
sample.head()


# In[9]:

sample.groupby('class') [['math']].max()


# In[10]:

sample.groupby(['grade','class'])[['math']].mean()


# In[11]:

sample.groupby(['grade'])['math','chinese'].mean()


# In[12]:

sample.groupby('class')['math'].agg(['mean','min','max'])


# In[14]:

df = sample.groupby(['grade','class'])['math','chinese'].agg(['min','max'])
df


# ### 5.1.7 拆分、堆叠列

# In[19]:

table = pd.DataFrame({'cust_id':[10001,10001,10002,10002,10003],
                      'type':['Normal','Special_offer',\
                              'Normal','Special_offer','Special_offer'],
                      'Monetary':[3608,420,1894,3503,4567]})


# In[24]:

pd.pivot_table(table,index='cust_id',columns='type',values='Monetary')


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


# ### 5.1.8 赋值与条件赋值

# #### 1. 赋值

# In[29]:

sample = pd.DataFrame({'name':['Bob','Lindy','Mark',
		 'Miki','Sully','Rose'],
		'score':[99,78,999,77,77,np.nan],
		'group':[1,1,1,2,1,2],})


# In[30]:

sample.score.replace(999,np.nan)


# In[32]:

sample.replace({'score':{999:np.nan},
                'name':{'Bob':np.nan}})


# #### 2. 条件赋值

# In[33]:

def transform(row):
    if row['group'] == 1:
        return ('class1')
    elif row['group'] == 2:
        return ('class2')  
sample.apply(transform,axis=1)  


# In[34]:

sample.assign(class_n = sample.apply(transform,axis=1))


# In[35]:

sample = sample.copy()
sample.loc[sample.group==1,'class_n']='class1'
sample.loc[sample.group==2,'class_n']='class2'


# In[ ]:




