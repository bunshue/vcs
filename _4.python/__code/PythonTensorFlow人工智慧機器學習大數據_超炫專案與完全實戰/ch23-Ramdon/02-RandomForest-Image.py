#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

from sklearn.ensemble import RandomForestClassifier

import numpy as np
from sklearn.datasets import make_classification

X, Y = make_classification(n_samples=10,
                           n_features=3,
                           n_informative=2,
                           n_redundant=0,
                           random_state=0,
                           shuffle=True)

model = RandomForestClassifier(n_estimators=100, max_depth=10,
                             random_state=2)
model.fit(X, Y)
print(model.feature_importances_)
print(model.predict([[0,0,0]]))
estimator = model.estimators_[5]

from sklearn.tree import export_graphviz
export_graphviz(estimator, out_file='tree.dot',
                feature_names = ["A","B","C"],
                class_names = ["0","1"],
                rounded = True, proportion = False,
                precision = 2, filled = True)


