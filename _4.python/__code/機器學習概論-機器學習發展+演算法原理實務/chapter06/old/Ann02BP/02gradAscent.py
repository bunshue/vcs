# -*- coding: GBK -*-
# Filename :gradDecent.py

from numpy import *
import operator
import Untils
import matplotlib.pyplot as plt 

# BP������

# ���ݼ�: ��1:�ؾ� 1;��2:x����; ��3:y����
dataMat,classLabels = Untils.loadDataSet("student.txt")
dataMat = mat(dataMat)
classMat= mat(classLabels)

# ���ݹ�һ��
dataMat = Untils.normalize(dataMat)

# �������ݼ�����ɢ��ͼ
Untils.drawClassScatter(dataMat,classLabels,False)
		
# m���� n����
m,n = shape(dataMat)
labelMat = classMat.transpose()
# ����
alpha = 0.001
# ��������
maxCycles = 500
#�������Էָ��� y=a*x+b: b:weights[0]; a:weights[1]/weights[2]
weights = ones((n,1))
# ����ع�ϵ�� weights
for k in range(maxCycles):
	# ͨ��sigmoid�������ؽ����h���ݶȼ���Ľ������һ��������
	# h = logRegres2.sigmoid(dataMatrix*weights)
	h = 1.0/(1+exp(-dataMat*weights))
	# ������:�����ǩ(0,1)-h
	error = (labelMat - h)  
	# �ع�ϵ��������Ȩ��
	weights = weights + alpha * dataMat.transpose()* error 
print weights	

# ���Ʒ�����ͼ��
Untils.ClassifyLine(-3,3,weights)
	
