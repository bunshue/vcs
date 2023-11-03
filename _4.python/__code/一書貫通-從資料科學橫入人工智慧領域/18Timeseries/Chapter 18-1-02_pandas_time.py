
# coding: utf-8

# # Pandas的时间序列处理 

# ## 创建

# In[2]:


from datetime import datetime
import pandas as pd
import numpy as np

# 指定index为datetime的list
date_list = [datetime(2017, 2, 18), datetime(2017, 2, 19), 
             datetime(2017, 2, 25), datetime(2017, 2, 26), 
             datetime(2017, 3, 4), datetime(2017, 3, 5)]
time_s = pd.Series(np.random.randn(6), index=date_list)
print(time_s)
print(type(time_s.index))


# In[3]:


# pd.date_range()
dates = pd.date_range('2017-02-18', # 起始日期
                      periods=5,    # 周期
                      freq='W-SAT') # 频率
print(dates)
print(pd.Series(np.random.randn(5), index=dates))


# ## 索引

# In[4]:


# 索引位置
print(time_s[0])


# In[5]:


# 索引值
print(time_s[datetime(2017, 2, 18)])


# In[6]:


# 可以被解析的日期字符串
print(time_s['2017/02/18'])


# In[7]:


# 按“年份”、“月份”索引
print(time_s['2017-2'])


# In[8]:


# 切片操作
print(time_s['2017-2-26':])


# ## 过滤
# 

# In[9]:


time_s.truncate(before='2017-2-25')


# In[10]:


time_s.truncate(after='2017-2-25')


# ## 生成日期范围

# In[11]:


# 传入开始、结束日期，默认生成的该时间段的时间点是按天计算的
date_index = pd.date_range('2017/02/18', '2017/03/18')
print(date_index)


# In[12]:


# 只传入开始或结束日期，还需要传入时间段
print(pd.date_range(start='2017/02/18', periods=10))


# In[13]:


print(pd.date_range(end='2017/03/18', periods=10))


# In[14]:


# 规范化时间戳 
print(pd.date_range(start='2017/02/18 12:13:14', periods=10))
print(pd.date_range(start='2017/02/18 12:13:14', periods=10, normalize=True))


# ## 频率与偏移量

# In[15]:


print(pd.date_range('2017/02/18', '2017/03/18', freq='2D'))


# In[16]:


# 偏移量通过加法连接
sum_offset = pd.tseries.offsets.Week(2) + pd.tseries.offsets.Hour(12)
print(sum_offset)

print(pd.date_range('2017/02/18', '2017/03/18', freq=sum_offset))


# ## 移动数据

# In[17]:


ts = pd.Series(np.random.randn(5), index=pd.date_range('20170218', periods=5, freq='W-SAT'))
print(ts)


# In[21]:


print(ts.shift(1,freq='2D'))
print(ts.shift(-1))


# In[19]:
