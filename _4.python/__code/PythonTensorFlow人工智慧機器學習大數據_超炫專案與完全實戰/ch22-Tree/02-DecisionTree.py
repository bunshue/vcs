#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])


clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
prediction = clf.predict([[173, 76]])
print(prediction)

#繪圖
plt.plot(X[:3,0], X[:3,1], 'yx' )
plt.plot(X[3:,0], X[3:,1], 'g.' )
plt.plot([173], [76], 'r^' )                                                                                       #綠色點
plt.ylabel('W')
plt.xlabel('H')
plt.legend(('man','woman'),  loc='upper left')
plt.show()
