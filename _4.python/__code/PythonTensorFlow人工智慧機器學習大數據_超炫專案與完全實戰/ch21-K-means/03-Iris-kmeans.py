#!/usr/bin/python
# -*- coding: utf-8 -*-



import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans
from sklearn import metrics

# Load the diabetes dataset
iris = datasets.load_iris()


iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(iris.data,iris.target,test_size=0.2)


# KMeans 演算法
kmeans  = KMeans(n_clusters = 3)
kmeans_fit =kmeans.fit(iris_X_train)




print("實際",iris_y_train)
print("預測",kmeans_fit.labels_)
#調整標籤的數字
iris_y_train[iris_y_train==1]=11
iris_y_train[iris_y_train==0]=1
iris_y_train[iris_y_train==11]=0
print("調整",iris_y_train)

score = metrics.accuracy_score(iris_y_train,kmeans.predict(iris_X_train))
print('準確率:{0:f}'.format(score))

