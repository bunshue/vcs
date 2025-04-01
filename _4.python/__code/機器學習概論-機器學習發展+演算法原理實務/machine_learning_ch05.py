"""
machine_learning_ch05

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
    plt.show()
    pass

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# common_libs.py

from numpy import *
import operator

# import scipy.spatial.distance.cdist as dist


def savefile(savepath, content):
    fp = open(savepath, "wb")
    fp.write(content)
    fp.close()


# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 文件分隔符
def file2matrix(path, delimiter):
    recordlist = []
    fp = open(path, "rb")  # 读取文件内容
    content = fp.read()
    fp.close()
    rowlist = content.splitlines()  # 按行转换为一维表
    # 逐行遍历 		# 结果按分隔符分割为行向量
    recordlist = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    return mat(recordlist)  # 返回转换后的矩阵形式


# 欧氏距离
eps = 1.0e-6


def distEclud(vecA, vecB):
    return linalg.norm(vecA - vecB) + eps


# 相关系数
def distCorrcoef(vecA, vecB):
    return corrcoef(vecA, vecB, rowvar=0)[0][1]


# Jaccard距离
# def distJaccard(vecA, vecB):
# 	temp = mat([array(vecA.tolist()[0]),array(vecB.tolist()[0])])
# 	return dist.pdist(temp,'jaccard')
# 余弦相似度
def cosSim(vecA, vecB):
    return (dot(vecA, vecB.T) / ((linalg.norm(vecA) * linalg.norm(vecB)) + eps))[0, 0]


# 绘制散点图
def drawScatter(plt, mydata, size=20, color="blue", mrkr="o"):
    m, n = shape(mydata)
    if m > n and m > 2:
        plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)
    else:
        plt.scatter(mydata[0], mydata[1], s=size, c=color, marker=mrkr)


# 绘制分类点
def drawScatterbyLabel(plt, Input):
    m, n = shape(Input)
    target = Input[:, -1]
    for i in range(m):
        if target[i] == 0:
            plt.scatter(Input[i, 0], Input[i, 1], c="blue", marker="o")
        else:
            plt.scatter(Input[i, 0], Input[i, 1], c="red", marker="s")


# 硬限幅函数
def hardlim(dataSet):
    dataSet[nonzero(dataSet.A > 0)[0]] = 1
    dataSet[nonzero(dataSet.A <= 0)[0]] = 0
    return dataSet


# Logistic函数
def logistic(wTx):
    return 1.0 / (1.0 + exp(-wTx))


def buildMat(dataSet):
    m, n = shape(dataSet)
    dataMat = zeros((m, n))
    dataMat[:, 0] = 1
    dataMat[:, 1:] = dataSet[:, :-1]
    return dataMat


# 分类函数
def classifier(testData, weights):
    prob = logistic(sum(testData * weights))  # 求取概率--判别算法
    if prob > 0.5:
        return 1.0  # prob>0.5 返回为1
    else:
        return 0.0  # prob<=0.5 返回为0


# 最小二乘回归，用于测试
def standRegres(xArr, yArr):
    xMat = mat(ones((len(xArr), 2)))
    yMat = mat(ones((len(yArr), 1)))
    xMat[:, 1:] = (mat(xArr).T)[:, 0:]
    yMat[:, 0:] = (mat(yArr).T)[:, 0:]
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# data.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
m, n = shape(Input)
print(m, n)
newdata = zeros((m, 3))
newdata[:, :2] = Input[:, :2]
newdata[:, 2:2] = Input[:, 3:3]
print(newdata[:100, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# gradient_test.py

import operator
from numpy import *

# 输入数据
Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 按分类绘制散点图
drawScatterbyLabel(plt, Input)

# 构建x+b 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
print(dataMat)
alpha = 0.001  # 步长
steps = 500  # 迭代次数

weights = ones((n, 1))  # 初始化权重向量
# 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = hardlim(gradient)  # 硬限幅函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors

print(weights)  # 输出权重

X = np.linspace(-5, 5, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(double(weights[0]) + X * (double(weights[1]))) / double(weights[2])
plt.plot(X, Y)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# iterate_test.py

from numpy import *

# 求解原方程
A = mat([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
b = mat([20, 33, 36])
result = linalg.solve(A, b.T)
print(result)

# 迭代求原方程组的解：x(k+1)=B0*x(k)+f
B0 = mat(
    [
        [0.0, 3.0 / 8.0, -2.0 / 8.0],
        [-4.0 / 11.0, 0.0, 1.0 / 11.0],
        [-6.0 / 12.0, -3.0 / 12.0, 0.0],
    ]
)
m, n = shape(B0)
f = mat([[20.0 / 8.0], [33.0 / 11.0], [36.0 / 12.0]])

error = 1.0e-6  # 误差阈值
steps = 100  # 迭代次数
xk = zeros((n, 1))  # 初始化 xk=x0
errorlist = []  # 记录逐次逼近的误差列表
for k in range(steps):  # 主程序
    xk_1 = xk  # 上一次的xk
    xk = B0 * xk + f  # 本次xk
    errorlist.append(linalg.norm(xk - xk_1))  # 计算并存储误差
    if errorlist[-1] < error:  # 判断误差是否小于阈值
        print(k + 1)  # 输出迭代次数
        break
print(xk)  # 输出计算结果
# 绘制误差收敛散点图
matpts = zeros((2, k + 1))
matpts[0] = linspace(1, k + 1, k + 1)
matpts[1] = array(errorlist)
drawScatter(plt, matpts)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# log_evalue_weight.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 2.按分类绘制散点图
drawScatterbyLabel(plt, Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print dataMat
# 4. 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = ones((n, 1))  # 初始化权重向量
weightlist = []
# 5. 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
# 6. 绘制训练后超平面
X = np.linspace(-5, 5, 100)
Ylist = []
lenw = len(weightlist)
for indx in range(lenw):
    if indx % 20 == 0:  # 每20次输出一次分类超平面
        weight = weightlist[indx]
        Y = -(double(weight[0]) + X * (double(weight[1]))) / double(weight[2])
        plt.plot(X, Y)
        # 分类超平面注释
        plt.annotate("hplane:" + str(indx), xy=(X[99], Y[99]))
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# log_evalue_weight2.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print dataMat
# 4. 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = ones((n, 1))  # 初始化权重向量
weightlist = []
# 5. 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
weightmat = mat(zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = linspace(0, steps, steps)
# 输出前10个点的截距变化
axes1.plot(
    X[0:10],
    -weightmat[0:10, 0] / weightmat[0:10, 2],
    color="blue",
    linewidth=1,
    linestyle="-",
)
axes2.plot(
    X[10:],
    -weightmat[10:, 0] / weightmat[10:, 2],
    color="blue",
    linewidth=1,
    linestyle="-",
)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# log_evalue_weight3.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print dataMat
# 4. 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = ones((n, 1))  # 初始化权重向量
weightlist = []
# 5. 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
weightmat = mat(zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = linspace(0, steps, steps)
# 输出前10个点的截距变化
axes1.plot(
    X[0:10],
    -weightmat[0:10, 1] / weightmat[0:10, 2],
    color="blue",
    linewidth=1,
    linestyle="-",
)
axes2.plot(
    X[10:],
    -weightmat[10:, 1] / weightmat[10:, 2],
    color="blue",
    linewidth=1,
    linestyle="-",
)

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# log_evalue_weight4.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print dataMat
# 4. 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = ones((n, 1))  # 初始化权重向量
weightlist = []
# 5. 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(311)
axes2 = plt.subplot(312)
axes3 = plt.subplot(313)
weightmat = mat(zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = linspace(0, steps, steps)
# 输出前10个点的截距变化
axes1.plot(X, weightmat[:, 0], color="blue", linewidth=1, linestyle="-")
axes1.set_ylabel("weight[0]")
axes2.plot(X, weightmat[:, 1], color="red", linewidth=1, linestyle="-")
axes2.set_ylabel("weight[1]")
axes3.plot(X, weightmat[:, 2], color="green", linewidth=1, linestyle="-")
axes3.set_ylabel("weight[2]")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_test.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)
# 2.按分类绘制散点图
drawScatterbyLabel(plt, Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
print(dataMat[:10, :])
# 4. 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = ones((n, 1))  # 初始化权重向量
# 5. 主程序
for k in range(steps):
    gradient = dataMat * mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors

print(weights)  # 输出训练后的权重
# 6. 绘制训练后超平面
X = np.linspace(-7, 7, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(double(weights[0]) + X * (double(weights[1]))) / double(weights[2])
plt.plot(X, Y)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# logistic_test2.py

import operator
from numpy import *

weights = mat([[4.12414349], [0.48007329], [-0.6168482]])
testdata = mat([-0.147324, 2.874846])
m, n = shape(testdata)
testmat = zeros((m, n + 1))
testmat[:, 0] = 1
testmat[:, 1:] = testdata
print(classifier(testmat, weights))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# plotGD.py

import matplotlib
import matplotlib.cm as cm
import matplotlib.mlab as mlab

leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

matplotlib.rcParams["xtick.direction"] = "out"
matplotlib.rcParams["ytick.direction"] = "out"

delta = 0.025  # 步长
x = np.arange(-2.0, 2.0, delta)  # x轴取值
y = np.arange(-2.0, 2.0, delta)  # y轴取值
X, Y = np.meshgrid(x, y)  # 绘制网格图
Z1 = -((X - 1) ** 2)
Z2 = -(Y**2)
# Z1 = mlab.bivariate_normal(X, Y, 1.0, 1.0, 0.0, 0.0)
# Z2 = mlab.bivariate_normal(X, Y, 1.5, 0.5, 1, 1)
# difference of Gaussians
Z = 1.0 * (Z2 + Z1) + 5.0  # 计算获取Z轴取值


plt.figure()
CS = plt.contour(X, Y, Z)
# 绘制点到点之间的箭头
plt.annotate(
    "",
    xy=(0.05, 0.05),
    xycoords="axes fraction",
    xytext=(0.2, 0.2),
    textcoords="axes fraction",
    va="center",
    ha="center",
    bbox=leafNode,
    arrowprops=arrow_args,
)
plt.text(-1.9, -1.8, "P0")  # P0点位置
plt.annotate(
    "",
    xy=(0.2, 0.2),
    xycoords="axes fraction",
    xytext=(0.35, 0.3),
    textcoords="axes fraction",
    va="center",
    ha="center",
    bbox=leafNode,
    arrowprops=arrow_args,
)
plt.text(-1.35, -1.23, "P1")  # P1点位置
plt.annotate(
    "",
    xy=(0.35, 0.3),
    xycoords="axes fraction",
    xytext=(0.45, 0.35),
    textcoords="axes fraction",
    va="center",
    ha="center",
    bbox=leafNode,
    arrowprops=arrow_args,
)
plt.text(-0.7, -0.8, "P2")  # P2点位置
plt.text(-0.3, -0.6, "P3")  # P3点位置
plt.clabel(CS, inline=1, fontsize=10)
plt.title("Gradient Ascent")
plt.xlabel("x")
plt.ylabel("y")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stoc_evalue_alpha.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = ones(n)  # 初始化权重向量

alphalist = []
alphahlist = []
# 算法主程序:
# 1.对数据集的每个行向量进行m次随机抽取
# 2.对抽取之后的行向量应用动态步长
# 3.进行梯度计算
# 4.求得行向量的权值，合并为矩阵的权值
for j in range(steps):
    dataIndex = range(m)  # 以导入数据的行数m为个数产生索引向量:0~99
    for i in range(m):
        alpha = 2 / (1.0 + j + i) + 0.0001  # 动态修改alpha步长从4->0.016
        if j == 0:
            alphalist.append(alpha)
        if i == 0:
            alphahlist.append(alpha)
        randIndex = int(random.uniform(0, len(dataIndex)))  # 生成0~m之间随机索引
        vectSum = sum(dataMat[randIndex] * weights.T)  # 计算dataMat随机索引与权重的点积和
        grad = logistic(vectSum)  # 计算点积和的梯度
        errors = target[randIndex] - grad  # 计算误差
        weights = weights + alpha * errors * dataMat[randIndex]  # 计算行向量权重
        del dataIndex[randIndex]  # 从数据集中删除选取的随机索引

# print weights	# 输出训练后的权重
weights = weights.tolist()[0]
lenal = len(alphalist)
lenalh = len(alphahlist)
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
X1 = np.linspace(0, lenal, lenal)
X2 = np.linspace(0, lenalh, lenalh)
axes1.plot(X1, alphalist)
axes2.plot(X2, alphahlist)
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stoc_evalue_weight.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = ones(n)  # 初始化权重向量

weightlist = []
# 算法主程序:
# 1.对数据集的每个行向量进行m次随机抽取
# 2.对抽取之后的行向量应用动态步长
# 3.进行梯度计算
# 4.求得行向量的权值，合并为矩阵的权值
for j in range(steps):
    dataIndex = range(m)  # 以导入数据的行数m为个数产生索引向量:0~99
    for i in range(m):
        alpha = 2 / (1.0 + j + i) + 0.0001  # 动态修改alpha步长从4->0.016
        randIndex = int(random.uniform(0, len(dataIndex)))  # 生成0~m之间随机索引
        vectSum = sum(dataMat[randIndex] * weights.T)  # 计算dataMat随机索引与权重的点积和
        grad = logistic(vectSum)  # 计算点积和的梯度
        errors = target[randIndex] - grad  # 计算误差
        weights = weights + alpha * errors * dataMat[randIndex]  # 计算行向量权重
        del dataIndex[randIndex]  # 从数据集中删除选取的随机索引
    weightlist.append(weights)

lenwl = len(weightlist)
weightmat = zeros((lenwl, n))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight
    i += 1
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
X1 = np.linspace(0, lenwl, lenwl)
axes1.plot(X1, -weightmat[:, 0] / weightmat[:, 2])
# 截距
axes1.set_ylabel("Intercept")
axes2.plot(X1, -weightmat[:, 1] / weightmat[:, 2])
# 斜率
axes2.set_ylabel("Slope")
# 生成回归线
ws = standRegres(X1, -weightmat[:, 0] / weightmat[:, 2])
Y1 = ws[0, 0] + X1 * ws[1, 0]
axes1.plot(X1, Y1, color="red", linewidth=2, linestyle="-")
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stoc_evalue_weight2.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = ones(n)  # 初始化权重向量

weightlist = []
# 算法主程序:
# 1.对数据集的每个行向量进行m次随机抽取
# 2.对抽取之后的行向量应用动态步长
# 3.进行梯度计算
# 4.求得行向量的权值，合并为矩阵的权值
for j in range(steps):
    dataIndex = range(m)  # 以导入数据的行数m为个数产生索引向量:0~99
    for i in range(m):
        alpha = 2 / (1.0 + j + i) + 0.0001  # 动态修改alpha步长从4->0.016
        randIndex = int(random.uniform(0, len(dataIndex)))  # 生成0~m之间随机索引
        vectSum = sum(dataMat[randIndex] * weights.T)  # 计算dataMat随机索引与权重的点积和
        grad = logistic(vectSum)  # 计算点积和的梯度
        errors = target[randIndex] - grad  # 计算误差
        weights = weights + alpha * errors * dataMat[randIndex]  # 计算行向量权重
        del dataIndex[randIndex]  # 从数据集中删除选取的随机索引
    weightlist.append(weights)

lenwl = len(weightlist)
weightmat = zeros((lenwl, n))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight
    i += 1
fig = plt.figure()
axes1 = plt.subplot(311)
axes2 = plt.subplot(312)
axes3 = plt.subplot(313)
X1 = np.linspace(0, lenwl, lenwl)
axes1.plot(X1, weightmat[:, 0])
#
axes1.set_ylabel("weight[0]")
axes2.plot(X1, weightmat[:, 1])
#
axes2.set_ylabel("weight[1]")
axes3.plot(X1, weightmat[:, 2])
#
axes3.set_ylabel("weight[2]")

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# stoc_test.py

import operator
from numpy import *

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = shape(Input)

# 2.按分类绘制散点图
drawScatterbyLabel(plt, Input)

# 3.构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print dataMat
# 4. 定义步长和迭代次数
steps = 500  # 迭代次数
weights = ones(n)  # 初始化权重向量

# 算法主程序:
# 1.对数据集的每个行向量进行m次随机抽取
# 2.对抽取之后的行向量应用动态步长
# 3.进行梯度计算
# 4.求得行向量的权值，合并为矩阵的权值
for j in range(steps):
    dataIndex = range(m)  # 以导入数据的行数m为个数产生索引向量:0~99
    for i in range(m):
        alpha = 2 / (1.0 + j + i) + 0.0001  # 动态修改alpha步长从4->0.016
        randIndex = int(random.uniform(0, len(dataIndex)))  # 生成0~m之间随机索引
        vectSum = sum(dataMat[randIndex] * weights.T)  # 计算dataMat随机索引与权重的点积和
        grad = logistic(vectSum)  # 计算点积和的梯度
        errors = target[randIndex] - grad  # 计算误差
        weights = weights + alpha * errors * dataMat[randIndex]  # 计算行向量权重
        del dataIndex[randIndex]  # 从数据集中删除选取的随机索引

print(weights)  # 输出训练后的权重
weights = weights.tolist()[0]
# 6. 绘制训练后超平面
X = np.linspace(-5, 5, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(double(weights[0]) + X * (double(weights[1]))) / double(weights[2])
plt.plot(X, Y)
plt.show()

print("------------------------------------------------------------")  # 60個

'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *
import operator
import scipy.spatial.distance as dist


def savefile(savepath, content):
    fp = open(savepath, "w", encoding="UTF-8-sig")
    fp.write(content)
    fp.close()


# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 文件分隔符
def file2matrix(path, delimiter):
    print('ddddddddddddddddddd')
    recordlist = []
    fp = open(path, "r", encoding="UTF-8-sig")  # 读取文件内容
    content = fp.read()
    fp.close()
    rowlist = content.splitlines()  # 按行转换为一维表
    # 逐行遍历 		# 结果按分隔符分割为行向量
    recordlist = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    return mat(recordlist)  # 返回转换后的矩阵形式


# 欧氏距离
eps = 1.0e-6


def distEclud(vecA, vecB):
    return linalg.norm(vecA - vecB) + eps


# 相关系数
def distCorrcoef(vecA, vecB):
    return corrcoef(vecA, vecB, rowvar=0)[0][1]


# Jaccard距离
def distJaccard(vecA, vecB):
    temp = mat([array(vecA.tolist()[0]), array(vecB.tolist()[0])])
    return dist.pdist(temp, "jaccard")


# 余弦相似度
def cosSim(vecA, vecB):
    return (dot(vecA, vecB.T) / ((linalg.norm(vecA) * linalg.norm(vecB)) + eps))[0, 0]


# 绘制散点图
def drawScatter(plt, mydata, size=20, color="blue", mrkr="o"):
    m, n = shape(mydata)
    if m > n and m > 2:
        plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)
    else:
        plt.scatter(mydata[0], mydata[1], s=size, c=color, marker=mrkr)


# 绘制分类点
def drawScatterbyLabel(plt, Input):
    m, n = shape(Input)
    target = Input[:, -1]
    for i in range(m):
        if target[i] == 1:
            plt.scatter(Input[i, 0], Input[i, 1], c="blue", marker="o")
        else:
            plt.scatter(Input[i, 0], Input[i, 1], c="red", marker="s")


# 硬限幅函数
def hardlim(dataSet):
    dataSet[nonzero(dataSet.A > 0)[0]] = 1
    dataSet[nonzero(dataSet.A <= 0)[0]] = 0
    return dataSet


# Logistic函数
def logistic(wTx):
    return 1.0 / (1.0 + exp(-wTx))


def buildMat(dataSet):
    m, n = shape(dataSet)
    dataMat = zeros((m, n))
    dataMat[:, 0] = 1
    dataMat[:, 1:] = dataSet[:, :-1]
    return dataMat


# 分类函数
def classifier(testData, weights):
    prob = logistic(sum(testData * weights))  # 求取概率--判别算法
    if prob > 0.5:
        return 1.0  # prob>0.5 返回为1
    else:
        return 0.0  # prob<=0.5 返回为0


# 最小二乘回归，用于测试
def standRegres(xArr, yArr):
    xMat = mat(ones((len(xArr), 2)))
    yMat = mat(ones((len(yArr), 1)))
    xMat[:, 1:] = (mat(xArr).T)[:, 0:]
    yMat[:, 0:] = (mat(yArr).T)[:, 0:]
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import copy
from numpy import *

# 输入数据
Input = file2matrix("data05/test.txt", "\t")
target = Input[:, 0].copy()
Input[:, 0] = Input[:, 2].copy()
Input[:, 2] = target.copy()
[m, n] = shape(Input)


print(m)
print(n)


sys.exit()


# 按分类绘制散点图
drawScatterbyLabel(plt, Input)

plt.show()

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
