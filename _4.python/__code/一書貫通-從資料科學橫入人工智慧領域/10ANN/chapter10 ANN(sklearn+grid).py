import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
#os.chdir(r"D:\Python_book\10ANN")

churn = pd.read_csv('telecom_churn.csv', skipinitialspace=True)
churn.head()

# 划分训练集和测试集

from sklearn.model_selection import train_test_split

data = churn.iloc[:, 2:]
target = churn['churn']
train_data, test_data, train_target, test_target = train_test_split(
    data, target, test_size=0.2)

# 极差标准化

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(train_data)

scaled_train_data = scaler.transform(train_data)
scaled_test_data = scaler.transform(test_data)

from sklearn.neural_network import MLPClassifier  # 多層感知器分類器 函數學習機

mlp = MLPClassifier(hidden_layer_sizes=(10,), 
                    activation='logistic', alpha=0.1, max_iter=1000)  # 多層感知器分類器 函數學習機

mlp.fit(scaled_train_data, train_target)
mlp

# ### 预测
# 预测分类标签

train_predict = mlp.predict(scaled_train_data)
test_predict = mlp.predict(scaled_test_data)

# 预测概率

# 计算分别属于各类的概率，取标签为1的概率
train_proba = mlp.predict_proba(scaled_train_data)[:, 1]  
test_proba = mlp.predict_proba(scaled_test_data)[:, 1]

# ### 验证

from sklearn import metrics

print(metrics.confusion_matrix(test_target, test_predict, labels=[0, 1]))
print(metrics.classification_report(test_target, test_predict))

mlp.score(scaled_test_data, test_target) # Mean accuracy

fpr_test, tpr_test, th_test = metrics.roc_curve(test_target, test_proba)
fpr_train, tpr_train, th_train = metrics.roc_curve(train_target, train_proba)

plt.figure(figsize=[4, 4])
plt.plot(fpr_test, tpr_test, 'b-')
plt.plot(fpr_train, tpr_train, 'r-')
plt.title('ROC curve')
plt.show()

print('AUC = %6.4f' %metrics.auc(fpr_test, tpr_test))

from sklearn.model_selection import GridSearchCV
from sklearn import metrics

param_grid = {
    'hidden_layer_sizes':[(10, ), (15, ), (20, ), (5, 5)],
    'activation':['logistic', 'tanh', 'relu'], 
    'alpha':[0.001, 0.01, 0.1, 0.2, 0.4, 1, 10]
}

mlp = MLPClassifier(max_iter=1000)  # 多層感知器分類器 函數學習機

gcv = GridSearchCV(estimator=mlp, param_grid=param_grid, 
                   scoring='roc_auc', cv=4, n_jobs=-1)

gcv.fit(scaled_train_data, train_target)

gcv.best_score_

gcv.best_params_

gcv.best_estimator_

gcv.score(scaled_test_data, test_target) # Mean accuracy
