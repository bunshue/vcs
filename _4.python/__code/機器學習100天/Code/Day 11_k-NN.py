# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#机器学习100天——第十一天：K近邻法（K-NN）
#第一步：导入相关库

#第二步：导入数据集

dataset = pd.read_csv('../datasets/Social_Network_Ads.csv')
print(dataset)


#为了方便理解，这里我们只取Age年龄和EstimatedSalary估计工资作为特征

X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

#第三步：将数据划分成训练集和测试集
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

#第四步：特征缩放
# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#第五步：使用K-NN对训练集数据进行训练
# Fitting K-NN to the Training set
#从sklearn的neighbors类中导入KNeighborsClassifier学习器

from sklearn.neighbors import KNeighborsClassifier

#设置好相关的参数 n_neighbors = 5(K值的选择，默认选择5)、 metric = 'minkowski'(距离度量的选择，这里选择的是闵氏距离(默认参数))、 p = 2 (距离度量metric的附属参数，只用于闵氏距离和带权重闵氏距离中p值的选择，p=1为曼哈顿距离， p=2为欧式距离。默认为2)

classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
           metric_params=None, n_jobs=1, n_neighbors=5, p=2,
           weights='uniform')

#第六步：对测试集进行预测
# Predicting the Test set results

y_pred = classifier.predict(X_test)
print(y_pred)


#第七步：生成混淆矩阵
# Making the Confusion Matrix
#混淆矩阵可以对一个分类器性能进行分析，由此可以计算出许多指标，例如：ROC曲线、正确率等

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
cm = confusion_matrix(y_test, y_pred)
print(cm)
print(classification_report(y_test, y_pred))

"""



[[64  4]
 [ 3 29]]

    预测值
    0   1
实0 64  4   
际1 3   29
值

预测集中的0总共有68个，1总共有32个。 在这个混淆矩阵中，实际有68个0，但K-NN预测出有67(64+3)个0，其中有3个实际上是1。 同时K-NN预测出有33(4+29)个1，其中4个实际上是0。


"""




