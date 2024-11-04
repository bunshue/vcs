
# coding: utf-8

# # KNN

# * 加载数据集

# In[ ]:


get_ipython().magic('matplotlib inline')
import os
import numpy as np
from scipy import stats
import pandas as pd
import sklearn.cross_validation as cross_validation
import matplotlib.pyplot as plt

os.chdir(r'D:\Python_book\11KNNNB')
pd.set_option('display.max_columns', None)


# In[ ]:


orgData = pd.read_csv('date_data2.csv')
orgData.describe()


# * 选取自变量

# In[ ]:


X = orgData.ix[:, :4]
Y = orgData[['Dated']]
X.head()


# * 极值标准化

# In[ ]:


from sklearn import preprocessing

min_max_scaler = preprocessing.MinMaxScaler()
X_scaled = min_max_scaler.fit_transform(X)
X_scaled[1:5]


# * 划分训练集和测试集

# In[ ]:


train_data, test_data, train_target, test_target = cross_validation.train_test_split(
    X_scaled, Y, test_size=0.2, train_size=0.8, random_state=123)   #划分训练集和测试集


# 上述过程有没有问题？

# * 建模

# In[ ]:


from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)  # 默认欧氏距离
model.fit(train_data, train_target.values.flatten())
test_est = model.predict(test_data)


# * 验证

# In[ ]:


import sklearn.metrics as metrics

print(metrics.confusion_matrix(test_target, test_est, labels=[0, 1]))  # 混淆矩阵
print(metrics.classification_report(test_target, test_est))


# In[ ]:


model.score(test_data, test_target)


# * 选择k值

# In[ ]:


for k in range(1, 30):
    k_model = KNeighborsClassifier(n_neighbors=k)
    k_model.fit(train_data, train_target.values.flatten())
    score = k_model.score(test_data, test_target)
    print(k, '\t', score)


# * 交叉验证选择k值

# In[ ]:


from sklearn.grid_search import ParameterGrid
from sklearn.grid_search import GridSearchCV 
from sklearn.cross_validation import KFold

n_samples = len(train_data)
kf = KFold(n=n_samples, n_folds=3)
grid = {'n_neighbors':[1,2,3,4,5,6,7,8,9]}
estimator = KNeighborsClassifier()
gridSearchCV = GridSearchCV(estimator, grid, cv=kf)
gridSearchCV.fit(train_data, train_target.values.flatten())
gridSearchCV.grid_scores_


# In[ ]:


gridSearchCV.best_params_


# In[ ]:


best = gridSearchCV.best_estimator_ 
best.score(test_data, test_target)
# 练习：试一试哪些参数会影响结果
###################################################################################################
#%%