#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"



import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# Load the diabetes dataset
iris = datasets.load_iris()


iris_X_train , iris_X_test , iris_y_train , iris_y_test = train_test_split(iris.data,iris.target,test_size=0.2)


knn = KNeighborsClassifier()


knn.fit(iris_X_train, iris_y_train)


print("預測",knn.predict(iris_X_test))
print("實際",iris_y_test)

print('準確率: %.2f' % knn.score(iris_X_test, iris_y_test))
