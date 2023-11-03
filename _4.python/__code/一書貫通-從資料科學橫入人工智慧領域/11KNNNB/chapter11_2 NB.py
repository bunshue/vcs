# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 22:18:35 2018

@author: Ben
"""

import os
import pandas as pd
import sklearn.cross_validation as cross_validation

os.chdir(r'D:\Python_book\11KNNNB')
pd.set_option('display.max_columns', None)


# In[ ]:


orgData = pd.read_csv('date_data2.csv')
# # 朴素贝叶斯

# In[ ]:


orgData.head()


# In[ ]:

Y = orgData[['Dated']]
orgData1 = orgData.ix[:, -3:]

orgData1.income_rank = orgData1.income_rank.astype('category')
orgData1.describe(include='all')


# In[ ]:


train_data1, test_data1, train_target1, test_target1 = cross_validation.train_test_split(
    orgData1, Y, test_size=0.3, train_size=0.7, random_state=123)


# - 建模

# In[ ]:


from sklearn.naive_bayes import BernoulliNB

NB = BernoulliNB(alpha=1)
NB.fit(train_data1, train_target1.values.flatten())
test_est1 = NB.predict(test_data1)


# - 验证

# In[ ]:
import sklearn.metrics as metrics

print(metrics.classification_report(test_target1, test_est1))


#%%

