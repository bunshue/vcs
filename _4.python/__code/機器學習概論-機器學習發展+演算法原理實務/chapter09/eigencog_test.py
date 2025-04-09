# -*- coding: utf-8 -*-

from numpy import *
import sys
import os
from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")
ef.compute()
# 创建测试集
testImg = ef.X[30]
print("实际值 =", ef.y[30], "->", "预测值 =", ef.predict(testImg))
