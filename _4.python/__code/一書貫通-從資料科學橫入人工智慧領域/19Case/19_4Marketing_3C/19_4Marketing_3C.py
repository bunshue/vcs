
# coding: utf-8

# |变量名|变量说明|
# |:--:|:--:|
# |ID	|数据库中每个人的ID|
# |target_flag|	是否购买过目标产品|
# |gender|	性别|
# |education	|教育背景|
# |home_value|	所住房屋的价值|
# |age	|年龄信息，以类似25-35分组表示|
# |buy_online	|有无网购记录|
# |mosaic_group	|根据居住区域归纳的描述消费心理的变量|
# |marital	|婚姻状态|
# |poc	|有无小孩|
# |occupation	|职业信息|
# |mortgage	|住房贷款信息|
# |home_owner	|所住房屋是否自有|
# |region	|所处地区信息|
# |new_car|	购买新车的可能性（1代表最可能）|
# |home_income|	家庭收入信息（A代表最低，L代表最高）|
# 

# In[1]:


import os
os.chdir(r'D:\Python_book\19Case\19_4Marketing_3C')
# os.getcwd()


# ### 读取数据，并对数据进行初步探索

# In[2]:


get_ipython().magic('matplotlib inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)


# In[3]:


train = pd.read_csv('response_data_train.csv', skipinitialspace=True)
test = pd.read_csv('response_data_test.csv', skipinitialspace=True)
print(train.shape)
print(test.shape)


# In[4]:


train.describe(include='all')


# In[5]:


cols = train.columns.tolist()
x_c = ['home_value', 'new_car']
x_d = list(set(cols) - set(x_c)); x_d.remove('target_flag')


# ### 数据预处理

# 编码同时填补缺失值

# In[6]:


def label_encoder(series):
    cat = series.value_counts(dropna=False)
    len_series = len(series)
    return {k:v for k, v in zip(cat.index, range(len_series))}


# In[7]:


for col in x_d:
    encoder = label_encoder(train[col])
    train[col].replace(encoder, inplace=True)  # Encode train
    test[col].replace(encoder, inplace=True)  # Encode test


# In[8]:


encoder = label_encoder(train.target_flag)
train.target_flag.replace(encoder, inplace=True)
test.target_flag.replace(encoder, inplace=True)


# WOE编码

# In[9]:


from woe import WoE

for col in x_d:
    woe = WoE(v_type='d', t_type='b')
    woe.fit(train[col], train.target_flag)
    train[col] = woe.transform(train[col])['woe']
    test[col] = woe.transform(test[col])['woe']

test.head()


# ### 建模

# 通过搜索参数网格，选择模型的最优超参

# In[10]:


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV

dt = DecisionTreeClassifier()
grid = {'max_leaf_nodes':np.arange(32, 64, 6),
        'min_samples_split':np.arange(50, 301, 50)}
cv = GridSearchCV(dt, grid, scoring='roc_auc', cv=4, n_jobs=-1)
cv.fit(train.ix[:, 1:], train['target_flag'])
#%%
print('best_score:%2.4f'  %cv.best_score_)
print('best_params: %s' %cv.best_params_)


# In[11]:


from sklearn.metrics import roc_auc_score, roc_curve

test_p = cv.predict_proba(test.ix[:, 1:])
print(roc_auc_score(test.target_flag, test_p[:, 1]))


# ### 通过筛选变量可以改善模型过拟合的情况

# 决策树生长中，每一步都会计算变量的重要性，最终能够汇总各变量对整个模型的重要性。因此自然会想到利用决策树本身计算的变量重要性进行变量筛选

# In[12]:


imp = cv.best_estimator_.feature_importances_
list(zip(train.ix[:, 1:].columns, imp))


# 去除部分重要性不高的变量

# In[13]:


train= train.drop(
    ['poc', 'home_owner', 'mortgage', 'region', 'home_income'], axis=1)
test = test.drop(
    ['poc', 'home_owner', 'mortgage', 'region', 'home_income'], axis=1)


# 重新拟合模型

# In[14]:


cv.fit(train.ix[:, 1:], train['target_flag'])

print('best_score:%2.4f'  %cv.best_score_)
print('best_params: %s' %cv.best_params_)


# 当去除了部分变量后，模型的表现有所提升

# In[15]:


train_p = cv.predict_proba(train.ix[:, 1:])
test_p = cv.predict_proba(test.ix[:, 1:])
print(roc_auc_score(test.target_flag, test_p[:, 1]))


# 可以通过绘制ROC曲线来观察模型过拟合的情况

# In[16]:


fpr_test, tpr_test, th_test = roc_curve(test.target_flag, test_p[:, 1])

fpr_train, tpr_train, th_train = roc_curve(train.target_flag, train_p[:, 1])

plt.figure(figsize=[4, 4])
plt.plot(fpr_test, tpr_test, 'b--')
plt.plot(fpr_train, tpr_train, 'r-')
plt.title('ROC curve')
plt.show()


# 可视化

# In[18]:


import pydotplus
from IPython.display import Image
import sklearn.tree as tree

dot_data = tree.export_graphviz(
    cv.best_estimator_, 
    out_file=None, 
    feature_names=train.columns[1:],
    max_depth=2,
    class_names=['0','1'],
    filled=True
) 
            
graph = pydotplus.graph_from_dot_data(dot_data)  
Image(graph.create_png()) 
# graph.write_pdf('response_decision_tree.pdf')


# In[19]:


from sklearn.tree import _tree

def tree_to_code(tree, feature_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]
    print("def tree({}):".format(", ".join(feature_names)))

    def recurse(node, depth):
        indent = "  " * depth
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return {}".format(indent, tree_.value[node]))

    recurse(0, 1)


# In[22]:


tree_to_code(cv.best_estimator_, train.columns[1:])


# 使用组合方法

# In[23]:


from sklearn.ensemble import GradientBoostingClassifier

gbc = GradientBoostingClassifier()
gbc.fit(train.ix[:, 1:], train.target_flag)
gbc_train_p = gbc.predict_proba(train.ix[:, 1:])
gbc_test_p = gbc.predict_proba(test.ix[:, 1:])
#%%
print(roc_auc_score(train.target_flag, gbc_train_p[:, 1]))
print(roc_auc_score(test.target_flag, gbc_test_p[:, 1]))

#%%
