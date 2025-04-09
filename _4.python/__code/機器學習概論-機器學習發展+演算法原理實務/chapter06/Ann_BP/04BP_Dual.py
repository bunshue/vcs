# -*- coding: GBK -*-
# Filename :gradDecent.py

from numpy import *
import operator
import Untils
import BackPropgation
import matplotlib.pyplot as plt 

# BP������

# ���ݼ�: ��1:�ؾ� 1��2:x���� ��3:y����
dataMat,classLabels = BackPropgation.loadDataSet() # ��ʼ��ʱ��1��Ϊȫ1����
[m,n] = shape(dataMat) 
SampIn = mat(BackPropgation.normalize(mat(dataMat)).transpose())
expected = mat(classLabels)

# �������
eb = 0.01                   # ������� 
eta = 0.6                   # ѧϰ�� 
mc = 0.8                    # �������� 
maxiter = 1000              # ���������� 

# ��������

# ��ʼ������
nSampNum = m;  # ��������
nSampDim = 2;  # ����ά��
nHidden = 3;   # ��������Ԫ 
nOut = 1;      # �����

# ���������
# net_Hidden * 3 һ�д���һ��������ڵ�
w = 2*(random.rand(nHidden,nSampDim)-1/2)  
b = 2*(random.rand(nHidden,1)-1/2) 
wex = mat(Untils.mergMatrix(mat(w),mat(b)))

# ��������
W = 2*(random.rand(nOut,nHidden)-1/2) 
B = 2*(random.rand(nOut,1)-1/2) 
WEX = mat(Untils.mergMatrix(mat(W),mat(B)))

dWEXOld = [] ; dwexOld = [] # ��ʼ��Ȩֵ�м����
# ѵ��
iteration = 0;  
# ��ʼ��������
errRec = [];

for i in range(maxiter):   
    # �����ź����򴫲�
    hp = wex*SampIn
    tau = BackPropgation.logsig(hp)
    tauex  = Untils.mergMatrix(tau.transpose(), ones((nSampNum,1))).transpose()

    HM = WEX*tauex
    out = BackPropgation.logsig(HM)    
    
    err = expected - out 
    sse = BackPropgation.sumsqr(err) 
    errRec.append(sse)
    # �ж��Ƿ�����
    iteration = iteration + 1
        
    if sse <= eb:
        print "iteration:",i 
        break
     
    # ����źŷ��򴫲�
    # DELTA��deltaΪ�ֲ��ݶ�  
    DELTA = multiply(err,BackPropgation.dlogsig(HM,out))
    wDelta = W.transpose()*DELTA
    delta = multiply(wDelta,BackPropgation.dlogsig(hp,tau))
    dWEX = DELTA*tauex.transpose()
    dwex = delta*SampIn.transpose()        
    # ����Ȩֵ
    if i == 0:  
        WEX = WEX + eta * dWEX
        wex = wex + eta * dwex
    else :    
        WEX = WEX + (1 - mc)*eta*dWEX + mc * dWEXOld
        wex = wex + (1 - mc)*eta*dwex + mc * dwexOld
 
    dWEXOld = dWEX
    dwexOld = dwex 
    W  = WEX[:,0:nHidden]

# �����������
X = linspace(0,1000,1000)
Untils.TrendLine(X,errRec)
   