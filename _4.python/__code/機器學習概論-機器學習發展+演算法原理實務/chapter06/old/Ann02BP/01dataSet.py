# -*- coding: GBK -*-
# Filename : 01dataSet.py

import numpy as np 
import operator
import Untils
import BackPropgation
from numpy import *
import matplotlib.pyplot as plt 

dataMat,classLabels = Untils.loadDataSet("student.txt")

# ����ͼ�Σ���άɢ��,�޷���
# Untils.drawScatter(dataMat)

# ����ͼ�Σ���άɢ��,�з���,�ʺ�ѵ����
# Untils.drawClassScatter(mat(dataMat),classLabels)

# �ϲ�������ά��matrix�������غϲ����Matrix
# ����������Ⱥ�˳��
# [m,n]=shape(dataMat)
# classMat = transpose(mat(classLabels))
# matMerge = Untils.mergMatrix(mat(dataMat),classMat)

# Ԫ�س˷�
# a = mat([1,1,1]) ;b = mat([2,2,2])
# print multiply(a,b)

# ����BackPropgation.dlogsig(hp,tau)
# A = mat([0,1,2]);
# print "A*(1-A)",multiply(A,(1-A))
