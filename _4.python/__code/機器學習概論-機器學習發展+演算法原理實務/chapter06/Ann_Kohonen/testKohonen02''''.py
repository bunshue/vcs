# -*- coding: utf-8 -*-
# Filename : testKohonen02.py

import numpy as np 
from Kohonen import *
from numpy import *
import matplotlib.pyplot as plt 
# �����Ԫ��ƽ��֮��
def errorfunc(inX):
	return sum(power(inX,2))*0.5
# �������������ļ�
SOMNet = Kohonen()
SOMNet.loadDataSet("dataset2.txt");
SOMNet.train()
print SOMNet.w
SOMNet.showCluster(plt)
SOMNet.TrendLine(plt,SOMNet.lratelist)
SOMNet.TrendLine(plt,SOMNet.rlist)


