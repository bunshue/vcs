
# coding: utf-8

# # 时间数据重采样

# ## resample

# In[1]:


import pandas as pd
import numpy as np

date_rng = pd.date_range('20170101', periods=100, freq='D')
ser_obj = pd.Series(range(len(date_rng)), index=date_rng)
print(ser_obj.head(10))


# In[2]:


# 统计每个月的数据总和
resample_month_sum = ser_obj.resample('M').sum()
# 统计每个月的数据平均
resample_month_mean = ser_obj.resample('M').mean()

print('按月求和：', resample_month_sum)
print('按月求均值：', resample_month_mean)


# ## 降采样

# In[3]:


# 将数据聚合到5天的频率
five_day_sum_sample = ser_obj.resample('5D').sum()
five_day_mean_sample = ser_obj.resample('5D').mean()
five_day_ohlc_sample = ser_obj.resample('5D').ohlc()

print('降采样，sum')
print(five_day_sum_sample)


# In[4]:


print('降采样，mean')
print(five_day_mean_sample)


# In[6]:


# 使用groupby降采样
print(ser_obj.groupby(lambda x: x.month).sum())


# In[7]:


print(ser_obj.groupby(lambda x: x.weekday).sum())


# ## 升采样

# In[16]:


df = pd.DataFrame(np.random.randn(5, 3),
                 index=pd.date_range('20170101', periods=5, freq='W-MON'),
                 columns=['S1', 'S2', 'S3'])
print(df)


# In[18]:


# 直接重采样会产生空值
print(df.resample('D').asfreq())


# In[21]:


#ffill
print(df.resample('D').ffill(2))


# In[20]:


print(df.resample('D').bfill())


# In[23]:


print(df.resample('D').fillna('ffill'))


# In[24]:


print(df.resample('D').interpolate('linear'))

#%%
