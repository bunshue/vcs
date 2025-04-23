import numpy as np
import operator
import Untils
import Kohonen
from numpy import *
import matplotlib.pyplot as plt

# 加载坐标数据文件
dataSet = Untils.loadDataSet("dataset.txt")

dataMat = mat(dataSet)
print(dataMat)

normDataset = Kohonen.mapMinMax(dataMat)
print(normDataset)
