"""
machine_learning2b

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
import pickle
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# 数据文件转矩阵
# path: 数据文件路径
# delimiter: 文件分隔符
def file2matrix(path, delimiter):
    print("開啟檔案 :", path)
    recordlist = []
    fp = open(path, "r", encoding="utf8")  # 读取文件内容
    content = fp.read()
    fp.close()
    # print("content")
    # print(content)
    rowlist = content.splitlines()  # 按行转换为一维表
    # print("rowlist :", rowlist)
    recordlist = []
    for idx in range(len(rowlist)):
        cc = rowlist[idx].split(delimiter)
        for i in range(len(cc)):
            cc[i] = float(cc[i])
        recordlist.append(cc)
    return np.mat(recordlist)  # 返回转换后的矩阵形式


def createPlot(inTree):
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
    # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses

    show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import scipy.spatial.distance.cdist as dist
import scipy.spatial.distance as dist

# 欧氏距离
eps = 1.0e-6


def distEclud(vecA, vecB):
    return np.linalg.norm(vecA - vecB) + eps


# 相关系数
def distCorrcoef(vecA, vecB):
    return np.corrcoef(vecA, vecB, rowvar=0)[0][1]


# Jaccard距离
def distJaccard(vecA, vecB):
    temp = np.mat([np.array(vecA.tolist()[0]), np.array(vecB.tolist()[0])])
    return dist.pdist(temp, "jaccard")


# Jaccard距离
def distJaccard(vecA, vecB):
    temp = np.mat([np.array(vecA.tolist()[0]), np.array(vecB.tolist()[0])])
    return dist.pdist(temp, "jaccard")


# 余弦相似度
def cosSim(vecA, vecB):
    return (
        np.dot(vecA, vecB.T) / ((np.linalg.norm(vecA) * np.linalg.norm(vecB)) + eps)
    )[0, 0]


# 绘制散点图
def drawScatter1(plt, mydata, size=20, color="blue", mrkr="o"):
    m, n = np.shape(mydata)
    if m > n and m > 2:
        plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)
    else:
        plt.scatter(mydata[0], mydata[1], s=size, c=color, marker=mrkr)


def buildMat(dataSet):
    m, n = np.shape(dataSet)
    dataMat = np.zeros((m, n))
    dataMat[:, 0] = 1
    dataMat[:, 1:] = dataSet[:, :-1]
    return dataMat


def loadDataSet1(filename):  # general function to parse tab -delimited floats
    dataMat = []  # assume last column is target value
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(float, curLine)  # map all elements to float()
        dataMat.append(fltLine)
    return dataMat


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("builddataset.py")

labels = ["年龄", "收入", "学生", "信誉"]
dataset = [
    [0, 0, 0, 0, "no"],
    [0, 0, 0, 1, "no"],
    [0, 1, 0, 0, "no"],
    [0, 2, 1, 0, "yes"],
    [0, 1, 1, 1, "yes"],
    [1, 0, 0, 0, "yes"],
    [1, 2, 1, 1, "yes"],
    [1, 1, 0, 1, "yes"],
    [1, 0, 1, 0, "yes"],
    [2, 1, 0, 0, "yes"],
    [2, 2, 1, 0, "yes"],
    [2, 2, 1, 1, "no"],
    [2, 1, 1, 0, "yes"],
    [2, 1, 0, 1, "no"],
]
numlist = [64, 64, 128, 64, 64, 128, 64, 32, 32, 60, 64, 64, 132, 64]
print(np.mat(dataset).T)
datalines = []

for element, num in zip(dataset, numlist):
    liststr = ""
    for cell in element:
        liststr += str(cell) + "\t"
    liststr = liststr[:-1]
    for i in range(num):
        datalines.append(liststr)

fp = open("tmp_dataset.dat", "w")
fp.write("\n".join(datalines))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("classify07.py")

from sklearn.tree import DecisionTreeRegressor


# Create a random dataset
def plotfigure(X, X_test, y, y_pred):
    plt.figure()
    plt.scatter(X, y, c="k", label="data")
    plt.plot(X_test, y_pred, c="r", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    show()


x = np.linspace(-5, 5, 200)
siny = np.sin(x)  # 给出y与x的基本关系
X = np.mat(x).T
y = siny + np.random.rand(1, len(siny)) * 1.5  # 加入噪声的点集
y = y.tolist()[0]

# Fit regression model
clf = DecisionTreeRegressor(max_depth=4)

""" NG
clf.fit(X, y)

# Predict
X_test = np.arange(-5.0, 5.0, 0.05)[:, np.newaxis]
y_pred = clf.predict(X_test)

plotfigure(X, X_test, y, y_pred)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Recommand.py")

import operator


# dataSet 训练集
# testVect 测试集
# r=3 取前r个近似值
# rank=1,结果排序
# distCalc 相似度计算函数
def recommand(dataSet, testVect, r=3, rank=1, distCalc=cosSim):
    m, n = np.shape(dataSet)
    limit = min(m, n)
    if r > limit:
        r = limit
    U, S, VT = np.linalg.svd(dataSet.T)  # svd分解
    V = VT.T
    Ur = U[:, :r]  # 取前r个U,S,V值
    Sr = np.diag(S)[:r, :r]
    Vr = V[:, :r]
    testresult = testVect * Ur * np.linalg.inv(Sr)  # 计算User E的坐标值
    # 计算测试集与训练集每个记录的相似度
    resultarray = np.array([distCalc(testresult, vi) for vi in Vr])
    descindx = np.argsort(-resultarray)[:rank]  # 排序结果--降序
    return descindx, resultarray[descindx]  # 排序后的索引和值


# 加载修正后数据
A = np.mat(
    [
        [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
        [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
        [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
        [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
        [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
        [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
        [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
        [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
        [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
    ]
)
new = np.mat([[1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]])
indx, resultarray = recommand(A, new, r=2, rank=2, distCalc=cosSim)
print(indx)
print(resultarray)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("plotGD.py")

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# markovtest1.py

# 建立二維list
A = [[0.8, 0.2], [0.7, 0.3]]
print(type(A))

# 二維list 轉 np.matrix
A = np.mat(A)
print(type(A))

print(A)

A1 = A * A
print(A1)

A10 = A
for i in range(9):
    A10 = A10 * A
print(A10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# test01.py

# 1:1                            #3.6E                #1.3E-4
A11 = 3.9e-4 + 1.3e-5 + 5.0e-9 + 9.5e-8 + 4.7e-3 + 4.0e-4 + 7.0e-6 + 5.0e-4
print(A11)
# 1:0       #5.7E-6
A10 = 5.1e-5 + 7.0e-6 + 4.9e-7 + 9.4e-6 + 1.6e-3 + 1.7e-4 + 6.9e-4 + 1.3e-2
print(A10)
# 0:1
A01 = 5.8e-3 + 6.5e-4 + 2.9e-7 + 5.6e-6 + 6.1e-4 + 6.8e-5 + 4.8e-4 + 9.2e-3
print(A01)
# 0:0
A00 = 2.5e-3 + 2.8e-4 + 2.9e-5 + 5.5e-4 + 2.6e-4 + 2.9e-5 + 4.8e-2 + 9.1e-1
print(A00)
print(A11 + A10 + A01 + A00)
print(1 - (A11 + A10 + A01 + A00))

print(0.0060101 / (0.01681389 + 0.0060101))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 求解原方程
A = np.mat([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
b = np.mat([20, 33, 36])
result = np.linalg.solve(A, b.T)
print(result)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("建立字典的語法")

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")

print("decisionNode")
print(decisionNode)
print("leafNode")
print(leafNode)
print("arrow_args")
print(arrow_args)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("奇异值分解(SVD）")

# 加载修正后数据
A = np.mat(
    [[5, 5, 3, 0, 5, 5], [5, 0, 4, 0, 4, 4], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]]
)

# 手工分解求矩阵的svd
U = A * A.T
lamda, hU = np.linalg.eig(U)  # hU:U特征向量
VT = A.T * A
eV, hVT = np.linalg.eig(VT)  # hVT:VT特征向量
hV = hVT.T

print("hU:", hU)
print("hV:", hV)

sigma = np.sqrt(lamda)  # 特征值
print("sigma:", sigma)

Sigma = np.zeros([np.shape(A)[0], np.shape(A)[1]])
U, S, VT = np.linalg.svd(A)

# Sigma[:np.shape(A)[0], :np.shape(A)[0]] = np.diag(S)

print(U)
print(S)
print(VT)
print(U * Sigma * VT)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# Logistic函数
def logistic(wTx):
    return 1.0 / (1.0 + np.exp(-wTx))


X = np.linspace(-5, 5, 100)

Y = logistic(X)
plt.plot(X, Y)

show()

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
print("------------------------------------------------------------")  # 60個


print("------------------------------")  # 60個
