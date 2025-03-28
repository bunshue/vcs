"""
machine_learning_ch02

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# from common1 import *
import scipy
import sklearn.linear_model
from sklearn import datasets
from sklearn.datasets import make_blobs  # 集群資料集
from sklearn.datasets import make_moons
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split  # 資料分割 => 訓練資料 + 測試資料
from sklearn import metrics
from sklearn.decomposition import PCA
from sklearn.decomposition import KernelPCA  # KernelPCA 萃取特徵

from matplotlib.colors import ListedColormap
from sklearn.preprocessing import MinMaxScaler
from sklearn import tree


def show():
    # plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lassoReg.py

from numpy import *


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1  # get number of fields
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


# 矩阵标准化
def normData(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    xMeans = mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, k):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = shape(wMatT)
    for i in range(m):
        ax.plot(k, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(0, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet("data07/ridgedata2.txt")
# 数据矩阵转换
xMat, yMat = normData(xArr, yArr)
m, n = shape(xMat)
eps = 0.005  # 迭代步长变化
numIt = 1000  # 迭代次数

returnMat = zeros((numIt, n))  # 返回矩阵
ws = zeros((n, 1))  # 初始化ws为全零向量
wsTest = ws.copy()
wsMax = ws.copy()
for i in range(numIt):
    lowestError = inf
    # 初始化lowestError为无穷大
    for j in range(n):  # n 为特征向量的维度
        for sign in [-1, 1]:  # sign:信号量 取值为-1和1
            wsTest = ws.copy()
            wsTest[j] += eps * sign  # 信号量乘以步进值
            yTest = xMat * wsTest  # xMat乘以wsTest为特征向量
            rssE = ((yMat.A - yTest.A) ** 2).sum()  # 误差计算公式 # .A返回自身数据的一个引用(不进行拷贝)
            if rssE < lowestError:  # 判别最小误差
                lowestError = rssE  # 更新最小误差值
                wsMax = wsTest  # 更新wsMax
    ws = wsMax.copy()
    returnMat[i, :] = ws.T
print(returnMat)

# 绘制图形
# lasso
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(returnMat)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# leastSquare.py

from numpy import *
import operator


def loadDataSet(fileName):
    X = []
    Y = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append(float(curLine[0]))
        Y.append(float(curLine[-1]))
    return X, Y


# 绘制图形
def plotscatter(Xmat, Ymat, a, b, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    Xmat.sort()  # 对Xmat各元素进行排序
    yhat = [a * float(xi) + b for xi in Xmat]  # 计算预测值
    plt.plot(Xmat, yhat, "r")  # 绘制回归线
    show()


# 数据文件名
Xmat, Ymat = loadDataSet("data07/regdataset.txt")
meanX = mean(Xmat)  # 原始数据集的均值
meanY = mean(Ymat)
dX = Xmat - meanX  # 各元素与均值的差
dY = Ymat - meanY
# 手工计算：
# sumXY = 0; SqX = 0
# for i in range(len(dX)):
# 	sumXY += double(dX[i])*double(dY[i])
# 	SqX += double(dX[i])**2
sumXY = vdot(dX, dY)  # 返回两个向量的点乘 multiply
SqX = sum(power(dX, 2))  # 向量的平方：(X-meanX)^2

# 计算斜率和截距
a = sumXY / SqX
b = meanY - a * meanX
print(a, b)
# 绘制图形
plotscatter(Xmat, Ymat, a, b, plt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_k.py

from numpy import *


def scatterplot(k, x1, x2):  # 绘制图形
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x1)
    ax1.plot(x2)
    plt.title("k=" + str(k))
    show()


def logistic_map(k, init):
    maxIter = 100  # 最大迭代数
    x = list(range(maxIter))
    x[0] = init
    for i in list(range(maxIter - 1)):
        x[i + 1] = k * x[i] * (1.0 - x[i])
    return x


x1 = logistic_map(3.6, 0.1)
x2 = logistic_map(3.6, 0.9)
scatterplot(3.6, x1, x2)

"""
x1 = logistic_map(3.5,0.1)
x2 = logistic_map(3.5,0.9)
scatterplot(3.5,x1,x2)	
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# logistic_map.py

from numpy import *


def scatterplot(k,wMat):# 绘制图形
	fig = plt.figure();	ax = fig.add_subplot(111) 
	m,n=shape(wMat)
	for i in range(m): #逐列描点
		ax.scatter(mat(k),wMat[:,i],s=0.1,marker=".")
	show()
	
maxIter =1000 # 最大迭代数和系数分辨率区间
k= linspace(2.1,4.0,maxIter) # logisitic区间
klen = len(k)
xMat =mat(zeros((klen,maxIter)))  # 初始化结果矩阵
x = 1.0/float(maxIter)
for i in range(klen) :   # 沿系数方向循环
	for j in range(maxIter):  
		x = float(k[i])*x*(1.0-x) # 变量迭代
		xMat[i,j]=x
# 绘制图形
scatterplot(k,xMat)	
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# multilinear.py

from numpy import *


# 岭回归函数
# 加载数据集
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1  # get number of fields
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


# 矩阵标准化
def normData(xMat, yMat):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    xMeans = mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = shape(wMatT)
    for i in range(m):
        ax.plot(wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(i, wMatT[i, 0]), color="black")
    show()


def Multicollinear(xMat):
    features = xMat.T
    m, n = shape(features)
    for i in range(m):
        if i == (m - 1):
            print(i, ":", 0)
            print(corrcoef(features[i], features[0]))
        else:
            print(i, ":", i + 1)
            print(corrcoef(features[i], features[i + 1]))


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet("data07/ridgedata.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集
Multicollinear(xMat)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# normalequation.py

from numpy import *


def loadDataSet(fileName):
    X = []
    Y = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append(float(curLine[0]))
        Y.append(float(curLine[-1]))
    return X, Y


# 绘制图形
def plotscatter(Xmat, Ymat, a, b, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    Xmat.sort()  # 对Xmat各元素进行排序
    yhat = [a * float(xi) + b for xi in Xmat]  # 计算预测值
    plt.plot(Xmat, yhat, "r")  # 绘制回归线
    show()
    return yhat


# 数据矩阵,分类标签
xArr, yArr = loadDataSet("data07/regdataset.txt")
# 生成X坐标列
m = len(xArr)
Xmat = mat(ones((m, 2)))
for i in range(m):
    Xmat[i, 1] = xArr[i]
Ymat = mat(yArr).T  # 转换为y列

xTx = Xmat.T * Xmat  # 矩阵左乘自身的转置

ws = []
if linalg.det(xTx) != 0.0:
    # 计算直线的斜率和截距
    # 矩阵正规方程组公式:inv(X.T*X)*X.T*Y
    ws = xTx.I * (Xmat.T * Ymat)
else:
    print("This matrix is singular, cannot do inverse")
    sys.exit(0)  # 退出程序
print("ws:", ws)

"""
yHat = plotscatter(Xmat[:,1],Ymat,ws[1,0],ws[0,0],plt)

# 计算相关系数:
print(corrcoef(yHat,Ymat.T))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# rbfNettest.py

from numpy import *


def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1
    X = []
    Y = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append([float(curLine[i]) for i in range(numFeat)])
        Y.append(float(curLine[-1]))
    return X, Y


# 绘制图形
def plotscatter(Xmat, Ymat, yHat, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    plt.plot(Xmat, yHat, "r")  # 绘制散点图
    show()


# 数据矩阵,分类标签
xArr, yArr = loadDataSet("data07/nolinear.txt")
# 局部加权线性回归算法：回归线矩阵

# RBF函数的平滑系数
miu = 0.02
k = 0.03

# 数据集坐标数组转换为矩阵
xMat = mat(xArr)
yMat = mat(yArr).T
testArr = xArr  # 测试数组
m, n = shape(xArr)  # xArr的行数
yHat = zeros(m)  # yHat是y的预测值,yHat的数据是y的回归线矩阵
for i in range(m):
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testArr[i] - xMat[j, :]
        # 利用高斯核函数计算权重矩阵,计算后的权重是一个对角阵
        weights[j, j] = exp(diffMat * diffMat.T / (-miu * k**2))
    xTx = xMat.T * (weights * xMat)  # 矩阵左乘自身的转置
    if linalg.det(xTx) != 0.0:
        ws = xTx.I * (xMat.T * (weights * yMat))
        yHat[i] = testArr[i] * ws  # 计算回归线坐标矩阵
    else:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)  # 退出程序

"""
plotscatter(xMat[:,1],yMat,yHat,plt) # 绘制图形

# 计算相关系数:
print(corrcoef(yHat,yMat.T))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# rbm.py

import numpy
from scipy import sparse as S
from matplotlib import pyplot as plt
from scipy.sparse.csr import csr_matrix
import pandas


def normalize(x):
    V = x.copy()
    V -= x.min(axis=1).reshape(x.shape[0], 1)
    V /= V.max(axis=1).reshape(x.shape[0], 1)
    return V


def sigmoid(x):
    # return x*(x > 0)
    # return numpy.tanh(x)
    return 1.0 / (1 + numpy.exp(-x))


class RBM:
    def __init__(
        self,
        n_visible=None,
        n_hidden=None,
        W=None,
        learning_rate=0.1,
        weight_decay=1,
        cd_steps=1,
        momentum=0.5,
    ):
        if W == None:
            self.W = numpy.random.uniform(
                -0.1, 0.1, (n_visible, n_hidden)
            ) / numpy.sqrt(n_visible + n_hidden)
            self.W = numpy.insert(self.W, 0, 0, axis=1)
            self.W = numpy.insert(self.W, 0, 0, axis=0)
        else:
            self.W = W
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.last_change = 0
        self.last_update = 0
        self.cd_steps = cd_steps
        self.epoch = 0
        self.weight_decay = weight_decay
        self.Errors = []

    def fit(self, Input, max_epochs=1, batch_size=100):
        if isinstance(Input, S.csr_matrix):
            bias = S.csr_matrix(numpy.ones((Input.shape[0], 1)))
            csr = S.hstack([bias, Input]).tocsr()
        else:
            csr = numpy.insert(Input, 0, 1, 1)
        for epoch in range(max_epochs):
            idx = numpy.arange(csr.shape[0])
            numpy.random.shuffle(idx)
            idx = idx[:batch_size]

            self.V_state = csr[idx]
            self.H_state = self.activate(self.V_state)
            pos_associations = self.V_state.T.dot(self.H_state)

            for i in range(self.cd_steps):
                self.V_state = self.sample(self.H_state)
                self.H_state = self.activate(self.V_state)

            neg_associations = self.V_state.T.dot(self.H_state)
            self.V_state = self.sample(self.H_state)

            # Update weights.
            w_update = self.learning_rate * (
                (pos_associations - neg_associations) / batch_size
            )
            total_change = numpy.sum(numpy.abs(w_update))
            self.W += self.momentum * self.last_change + w_update
            self.W *= self.weight_decay

            self.last_change = w_update

            RMSE = numpy.mean((csr[idx] - self.V_state) ** 2) ** 0.5
            self.Errors.append(RMSE)
            self.epoch += 1
            # print("Epoch %s: RMSE = %s; ||W||: %6.1f; Sum Update: %f" % (self.epoch, RMSE, numpy.sum(numpy.abs(self.W)), total_change))
        return self

    def learning_curve(self):
        plt.ion()
        # plt.figure()
        E = numpy.array(self.Errors)
        E = pd.DataFrame(E)
        plt.plot(E.rolling(50).mean()[50:])
        show()

    def activate(self, X):
        if X.shape[1] != self.W.shape[0]:
            if isinstance(X, S.csr_matrix):
                bias = S.csr_matrix(numpy.ones((X.shape[0], 1)))
                csr = S.hstack([bias, X]).tocsr()
            else:
                csr = numpy.insert(X, 0, 1, 1)
        else:
            csr = X
        p = sigmoid(csr.dot(self.W))
        p[:, 0] = 1.0
        return p

    def sample(self, H, addBias=True):
        if H.shape[1] == self.W.shape[0]:
            if isinstance(H, S.csr_matrix):
                bias = S.csr_matrix(numpy.ones((H.shape[0], 1)))
                csr = S.hstack([bias, H]).tocsr()
            else:
                csr = numpy.insert(H, 0, 1, 1)
        else:
            csr = H
        p = sigmoid(csr.dot(self.W.T))
        p[:, 0] = 1
        return p


if __name__ == "__main__":
    data = numpy.random.uniform(0, 1, (100, 10))
    rbm = RBM(10, 15)
    rbm.fit(data, 1000)
    rbm.learning_curve()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ridgeReg.py

# -*- coding: utf-8  -*-
# Filename : 04ridgeTest.py

from numpy import *


# 岭回归函数
# 加载数据集
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1  # get number of fields
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


# 矩阵标准化
def normData(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    xMeans = mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, k):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = shape(wMatT)
    for i in range(m):
        ax.plot(k, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(0, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet("data07/ridgedata.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集

Knum = 30  # 确定lam的范围exp(-10~20)
# 初始化30行,8列的全0矩阵
wMat = zeros((Knum, shape(xMat)[1]))
klist = zeros((Knum, 1))
for i in range(Knum):
    k = float(i) / 500.0  # 算法的目的是确定k的取值
    klist[i] = k
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * k
    if linalg.det(denom) == 0.0:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)
    ws = denom.I * (xMat.T * yMat)
    wMat[i, :] = ws.T
print(klist)
scatterplot(klist, klist)  # k值的变化
scatterplot(wMat, klist)  # 岭回归

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# ridgeRegtest1.py

from numpy import *


# 岭回归函数
# 加载数据集
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1  # get number of fields
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat


# 矩阵标准化
def normData(xMat, yMat):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    yMean = mean(yMat, 0)
    xMeans = mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, logk):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = shape(wMatT)
    for i in range(m):
        ax.plot(logk, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(i, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet("data07/ridgedata2.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集

Knum = 100  # 确定lam的范围exp(-10~20)
# 初始化30行,8列的全0矩阵
wMat = zeros((Knum, shape(xMat)[1]))
klist = zeros((Knum, 1))
for i in range(Knum):
    k = i / 1000.0  # 算法的目的是确定k的取值
    klist[i] = k
    xTx = xMat.T * xMat
    denom = xTx + eye(shape(xMat)[1]) * k
    if linalg.det(denom) == 0.0:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)
    ws = denom.I * (xMat.T * yMat)
    wMat[i, :] = ws.T
print(klist)
scatterplot(klist, klist)  # k值的变化
scatterplot(wMat, klist)  # 岭回归


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
