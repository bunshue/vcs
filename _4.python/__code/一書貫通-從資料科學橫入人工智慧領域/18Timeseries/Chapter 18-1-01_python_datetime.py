
# coding: utf-8

# # Python的日期和时间处理 

# ## datetime模块

# In[1]:


from datetime import datetime


# In[2]:


now = datetime.now()
print(now)


# In[3]:


print('年: {}, 月: {}, 日: {}'.format(now.year, now.month, now.day))


# In[4]:


diff = datetime(2017, 3, 4, 17) - datetime(2017, 2, 18, 15)
print(type(diff))
print(diff)
print('经历了{}天, {}秒。'.format(diff.days, diff.seconds))


# ## 字符串和datetime转换
# 

# ### datetime -> str

# In[5]:


# str()
dt_obj = datetime(2017, 3, 4)
str_obj = str(dt_obj)
print(type(str_obj))
print(str_obj)


# In[6]:


# datetime.strftime()
str_obj2 = dt_obj.strftime('%d-%m-%Y')
print(str_obj2)


# ### str -> datetime

# In[7]:


# strptime
dt_str = '2017-02-18'
dt_obj2 = datetime.strptime(dt_str, '%Y-%m-%d')
print(type(dt_obj2))
print(dt_obj2)


# In[8]:


# dateutil.parser.parse
from dateutil.parser import parse
dt_str2 = '2017/02/18'
dt_obj3 = parse(dt_str2)
print(type(dt_obj3))
print(dt_obj3)


# In[9]:


# pd.to_datetime
import pandas as pd
s_obj = pd.Series(['2017/02/18', '2017/02/19', '2017-02-25', '2017-02-26'], name='course_time')
print(s_obj)


# In[10]:


s_obj2 = pd.to_datetime(s_obj)
print(s_obj2)


# In[11]:


# 处理缺失值
s_obj3 = pd.Series(['2017/02/18', '2017/02/19', '2017-02-25', '2017-02-26'] + [None], 
                   name='course_time')
print(s_obj3)


# In[12]:


s_obj4 = pd.to_datetime(s_obj3)
print(s_obj4) # NAT-> Not a Time

#%%
