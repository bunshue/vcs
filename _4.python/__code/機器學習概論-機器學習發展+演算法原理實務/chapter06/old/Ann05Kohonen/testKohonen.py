# -*- coding: utf-8 -*-
# Filename : testKohonen.py

import numpy as np 
import operator
import Untils
import Kohonen
from numpy import *
import matplotlib.pyplot as plt 

# �������������ļ�
dataSet = Untils.loadDataSet("dataset.txt");
dataMat = mat(dataSet)
dm,dn = shape(dataMat)
# ��һ������
normDataset = Kohonen.mapMinMax(dataMat)
# ����
# ѧϰ��
rate1max=0.8  #0.8
rate1min=0.05;
# ѧϰ�뾶
r1max=3;
r1min=0.8 #0.8

## ���繹��
Inum=2;
M=2;
N=2;
K=M*N;          #Kohonen�ܽڵ���  
 
# Kohonen��ڵ�����
k=0;
jdpx = mat(zeros((K,2)));
for i in range(M):
    for j in range(N):
        jdpx[k,:]=[i,j];
        k=k+1;

# Ȩֵ��ʼ��
w1 = random.rand(Inum,K); #��һ��Ȩֵ

## �������
ITER = 200
for i in range(ITER):
	
	#����Ӧѧϰ�ʺ���Ӧ�뾶
	rate1 = rate1max-(i+1)/float(ITER)*(rate1max-rate1min)
	r = r1max-(i+1)/float(ITER)*(r1max-r1min)
	# �����ȡһ������
	k = random.randint(0,dm) #��������������,���������ֵ
	myndSet = normDataset[k,:] #xx
		
	# �������Žڵ㣺������С���������ֵ
	minIndx= (Kohonen.distM(myndSet,w1)).argmin()
	d1 = ceil(minIndx/M)
	d2 = mod(minIndx,N)
	distMat = Kohonen.distM(mat([d1,d2]),jdpx.transpose())
	nodelindx = (distMat<r).nonzero()[1]
	for j in range(K):
		if sum(nodelindx==j):
			w1[:,j] = w1[:,j]+rate1*(myndSet.tolist()[0]-w1[:,j])

# ѧϰ�׶�
classLabel = range(dm);
for i in range(dm):
    classLabel[i] = Kohonen.distM(normDataset[i,:],w1).argmin()
# ȥ��
lst = unique(classLabel)
print lst
classLabel = mat(classLabel)
# ��ͼ
i = 0;
for cindx in lst:
	myclass = nonzero(classLabel==cindx)[1]	
	xx = dataMat[myclass].copy()
	if i ==0:
		plt.plot(xx[:,0],xx[:,1],'bo')
	if i ==1:
		plt.plot(xx[:,0],xx[:,1],'r*')
	if i ==2:
		plt.plot(xx[:,0],xx[:,1],'gD')			
	if i ==3:
		plt.plot(xx[:,0],xx[:,1],'c^')						
	i +=1			
plt.show()

    	