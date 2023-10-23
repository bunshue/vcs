# -*- coding: utf-8 -*-
# Filename : Kohonen.py

import operator
import Untils
from numpy import *
import matplotlib.pyplot as plt

# ��һ�����ݼ�
def mapMinMax(dataMat):
	ymin = -1; ymax = 1
	m,n = shape(dataMat)
	rtnMat = mat(zeros((m,n)))
	for i in range(n):
		xmin = dataMat[:,i].min()
		xmax = dataMat[:,i].max()
		rtnMat[:,i] = (ymax-ymin)*(dataMat[:,i]-xmin)/(xmax-xmin) + ymin;		
	return rtnMat;
	
# ������������֮��ľ���:����һ���ԳƵ�n*n����	
def distM(matA,matB):
	ma,na = shape(matA);
	mb,nb = shape(matB);
	rtnmat= zeros((ma,nb))
	for i in range(ma):
		for j in range(nb):
			rtnmat[i,j] = sqrt(sum(power(matA[i,:] - matB[:,j].transpose(),2)))
	return 	rtnmat

# ���㷨	
def kohonen(dataMat,M=2,N=2,ITER = 200):
	dm,dn = shape(dataMat)
	# ��һ������
	normDataset = mapMinMax(dataMat)
	# ����
	# ѧϰ��
	rate1max=0.8; rate1min=0.05
	# ѧϰ�뾶
	r1max=3; r1min=0.8
  
	## ���繹��
	Inum = 2;	K=M*N          #Kohonen�ܽڵ���  
   
	# Kohonen��ڵ�����
	k=0;
	jdpx = mat(zeros((K,2)));
	for i in range(M):
		for j in range(N):
			jdpx[k,:]=[i,j]
			k=k+1;
	
	# Ȩֵ��ʼ��
	w1 = random.rand(Inum,K); #��һ��Ȩֵ
  
	## �������
	for i in range(ITER):  	
		#����Ӧѧϰ�ʺ���Ӧ�뾶
		rate1 = rate1max-(i+1)/float(ITER)*(rate1max-rate1min)
		r = r1max-(i+1)/float(ITER)*(r1max-r1min)
		# �����ȡһ������
		k = random.randint(0,dm) # ��������������,���������ֵ
		myndSet = normDataset[k,:] #xx
			
		# �������Žڵ㣺������С���������ֵ
		minIndx= (distM(myndSet,w1)).argmin()
		d1 = ceil(minIndx/M)
		d2 = mod(minIndx,M)
		distMat = distM(mat([d1,d2]),jdpx.transpose())
		nodelindx = (distMat<r).nonzero()[1]
		for j in range(K):
			if sum(nodelindx==j):
				w1[:,j] = w1[:,j]+rate1*(myndSet.tolist()[0]-w1[:,j])
  
	# ѧϰ�׶�
	classLabel = range(dm)
	for i in range(dm):
		classLabel[i] = distM(normDataset[i,:],w1).argmin()

  # ��������ǩ
	return mat(classLabel)		