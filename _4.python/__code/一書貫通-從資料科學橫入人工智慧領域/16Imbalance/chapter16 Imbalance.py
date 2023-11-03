
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

import os
os.chdir(r"D:\Python_book\16Imbalance")

# In[2]:


train = pd.read_csv('imb_train.csv')
test = pd.read_csv('imb_test.csv')
train.head()


# In[3]:


y_train = train['cls']; X_train = train.ix[:, :'X5']
y_test = test['cls'];   X_test = test.ix[:, :'X5']

print('train_size: %s' %len(y_train),
     'test_size: %s' % len(y_test))


# In[4]:


plt.figure(figsize=[3, 2])
count_classes = pd.value_counts(y_train, sort=True)
count_classes.plot(kind='bar')
plt.show()


# In[6]:
#1、采用抽样的方法

from imblearn.over_sampling import RandomOverSampler, SMOTE
from imblearn.combine import SMOTETomek

ros = RandomOverSampler(random_state=0, ratio='auto') # 随机过采样
sos = SMOTE(random_state=0)      # SMOTE过采样
kos = SMOTETomek(random_state=0)  # 综合采样

X_ros, y_ros = ros.fit_sample(X_train, y_train)
X_sos, y_sos = sos.fit_sample(X_train, y_train)
X_kos, y_kos = kos.fit_sample(X_train, y_train)

#%%
print('ros: %s, sos:%s, kos:%s' %(len(y_ros), len(y_sos), len(y_kos)))


# In[7]:


y_ros.sum(), y_sos.sum(), y_kos.sum()


# In[8]:


from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

clf = DecisionTreeClassifier(criterion='gini', random_state=1234)
param_grid = {'max_depth':[3, 4, 5, 6], 'max_leaf_nodes':[4, 6, 8, 10, 12]}
cv = GridSearchCV(clf, param_grid=param_grid, scoring='f1')


# In[9]:


data = [[X_train, y_train],
        [X_ros, y_ros],
        [X_sos, y_sos],
        [X_kos, y_kos]]

for features, labels in data:
    cv.fit(features, labels)
    predict_test = cv.predict(X_test)
    
    print('auc:%.3f' %metrics.roc_auc_score(y_test, predict_test), 
          'recall:%.3f' %metrics.recall_score(y_test, predict_test),
          'precision:%.3f' %metrics.precision_score(y_test, predict_test))


# In[10]:

#2、采用改变样本权重的方法
param_grid2 = {'max_depth':[3, 4, 5, 6], 
               'max_leaf_nodes':[4, 6, 8, 10, 12], 
               'class_weight':[{0:1, 1:5}, {0:1, 1:10}, {0:1, 1:15}]}

cv2 = GridSearchCV(clf, param_grid=param_grid2, scoring='f1')


# In[11]:


cv2.fit(X_train, y_train)
predict_test2 = cv2.predict(X_test)

print('auc:%.3f' %metrics.roc_auc_score(y_test, predict_test2),
      'recall:%.3f' %metrics.recall_score(y_test, predict_test2),
      'precision:%.3f' %metrics.precision_score(y_test, predict_test2))


# In[11]:


cv2.best_params_

#%%
