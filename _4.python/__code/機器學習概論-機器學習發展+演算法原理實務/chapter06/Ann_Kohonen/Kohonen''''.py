# -*- coding: utf-8 -*-
from numpy import *
import matplotlib.pyplot as plt
class Kohonen(object):
	def __init__(self):	
		self.lratemax=0.8;  # ���ѧϰ��	
		self.lratemin=0.05  # ��Сѧϰ��	
		self.rmax=5.0;      # ������뾶
		self.rmin=0.5       # ��С����뾶
		self.Steps = 1000    # ��������
		self.lratelist=[]
		self.rlist=[]
		self.w=[]
		self.M=2;	          # ��ά�����������
		self.N=2            # ��ά�����������
		self.dataMat=[]
		self.classLabel=[]
		
	def loadDataSet(self,fileName): # ���������ļ�
		numFeat = len(open(fileName).readline().split('\t')) - 1 
		fr = open(fileName)
		for line in fr.readlines():
			lineArr =[]
			curLine = line.strip().split('\t')
			lineArr.append(float(curLine[0]));
			lineArr.append(float(curLine[1]));
			self.dataMat.append(lineArr)
		self.dataMat = mat(self.dataMat)
		
	# ���ݱ�׼��(��һ��):		# ��׼��
	def normalize(self,dataMat):
		[m,n]=shape(dataMat)
		for i in xrange(n-1):
			dataMat[:,i] = (dataMat[:,i]-mean(dataMat[:,i]))/(std(dataMat[:,i])+1.0e-10)
		return dataMat	
	
	# ������������֮��ľ���--ŷ�Ͼ���	
	def distEclud(self,matA,matB):
		ma,na = shape(matA);
		mb,nb = shape(matB);
		rtnmat= zeros((ma,nb))
		for i in xrange(ma):
			for j in xrange(nb):
	 			rtnmat[i,j] = linalg.norm(matA[i,:]-matB[:,j].T) 
		return 	rtnmat
	# ѧϰ�ʺ�ѧϰ�뾶����	
	def ratecalc(self,indx):
		lrate = self.lratemax-(float(indx)+1.0)/float(self.Steps)*(self.lratemax-self.lratemin) 
		r = self.rmax-(float(indx)+1.0)/float(self.Steps)*(self.rmax-self.rmin)
		return lrate,r
	# ��ʼ���ڶ�������	
	def init_grid(self):
		k=0;# �����ڶ�������ģ��
		grid = mat(zeros((self.M*self.N ,2)));
		for i in xrange(self.M):
			for j in xrange(self.N):
				grid[k,:]=[i,j]
				k +=1;
		return grid		
# ���㷨	
	def train(self):
    #1 �������������
		dm,dn = shape(self.dataMat) 
		normDataset = self.normalize(self.dataMat) # ��һ������x
		#2 ������������
		grid = self.init_grid() # ��ʼ���ڶ���������� 
		#3 ��������֮���Ȩ������
		self.w = random.rand(dn,self.M*self.N); #�����ʼ��Ȩֵ w
		distM = self.distEclud   # ȷ�����빫ʽ
		#4 �������
		if self.Steps < 10*dm:	self.Steps = 10*dm   # �趨��С��������
		for i in xrange(self.Steps): 	
			lrate,r = self.ratecalc(i) # ����ѧϰ�ʺͷ���뾶
			self.lratelist.append(lrate);self.rlist.append(r)
			# ���������������������ȡһ������
			k = random.randint(0,dm) 
			mySample = normDataset[k,:] 	
	
			# �������Žڵ㣺������С���������ֵ
			minIndx= (distM(mySample,self.w)).argmin()
			d1 = ceil(minIndx/self.M)   # ������������ڵڶ�������е�λ��
			d2 = mod(minIndx,self.M)    
			distMat = distM(mat([d1,d2]),grid.T)
			nodelindx = (distMat<r).nonzero()[1] # ����ѧϰ�����ȡ���������ҽڵ�
			# ����Ȩ����
			for j in xrange(shape(self.w)[1]):
				if sum(nodelindx==j):
		 			self.w[:,j] = self.w[:,j]+lrate*(mySample[0]-self.w[:,j])
		# ��������ǩ
		self.classLabel = range(dm)
		for i in xrange(dm):
			self.classLabel[i] = distM(normDataset[i,:],self.w).argmin()
		self.classLabel = mat(self.classLabel)		
	
	def showCluster(self,plt):
		lst = unique(self.classLabel.tolist()[0]) # ȥ��
		# ��ͼ
		i = 0;
		for cindx in lst:
			myclass = nonzero(self.classLabel==cindx)[1]	
			xx = self.dataMat[myclass].copy()
			if i ==0:
				plt.plot(xx[:,0],xx[:,1],'bo')
			elif i ==1:
				plt.plot(xx[:,0],xx[:,1],'rd')
			elif i ==2:
				plt.plot(xx[:,0],xx[:,1],'gD')			
			elif i ==3:
				plt.plot(xx[:,0],xx[:,1],'c^')						
			i +=1			
		plt.show()
# ����������: �ɵ�����ɫ		
	def TrendLine(self,plt,mylist,color='r'):
		X = linspace(0,len(mylist),len(mylist))
		Y = mylist
		plt.plot(X,Y,color)
		plt.show()