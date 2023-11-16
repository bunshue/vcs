#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"


from sklearn.ensemble import RandomForestClassifier

import numpy as np

X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])

RForest = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=2)
RForest.fit(X, Y)
print(RForest.predict([[180, 85]]))

