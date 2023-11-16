#!/usr/bin/env python
# -*- coding=utf-8 -*-
__author__ = "柯博文老師 Powen Ko, www.powenko.com"

import numpy as np
from sklearn import tree
from sklearn.externals.six import StringIO
import pydot
from os import system

X=np.array([[180, 85],[174, 80],[170, 75],
      [167, 45],[158, 52],[155, 44]])
Y = np.array(['man', 'man','man','woman', 'woman',  'woman'])

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

tree.export_graphviz(clf,out_file='tree.dot')
