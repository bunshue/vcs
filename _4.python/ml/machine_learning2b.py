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
    # print(recordlist)
    return np.mat(recordlist)  # 返回转换后的矩阵形式
    # 逐行遍历 		# 结果按分隔符分割为行向量
    # recordlist = [map(eval, row.split(delimiter)) for row in rowlist if row.strip()]
    # return np.mat(recordlist)  # 返回转换后的矩阵形式


def createPlot(inTree):
    fig = plt.figure(1, facecolor="white")
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
    # createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    plotTree(inTree, (0.5, 1.0), "")
    show()


""" old
def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
    plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
    show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# import scipy.spatial.distance.cdist as dist

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


# 余弦相似度
def cosSim(vecA, vecB):
    return (
        np.dot(vecA, vecB.T) / ((np.linalg.norm(vecA) * np.linalg.norm(vecB)) + eps)
    )[0, 0]


# Jaccard距离
# def distJaccard(vecA, vecB):
# 	temp = mat([array(vecA.tolist()[0]),array(vecB.tolist()[0])])
# 	return dist.pdist(temp,'jaccard')


# 绘制散点图
def drawScatter1(plt, mydata, size=20, color="blue", mrkr="o"):
    m, n = np.shape(mydata)
    if m > n and m > 2:
        plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)
    else:
        plt.scatter(mydata[0], mydata[1], s=size, c=color, marker=mrkr)


# 绘制散点图
def drawScatter2(plt, mydata, size=20, color="blue", mrkr="o"):
    plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)


# 绘制分类点
def drawScatterbyLabel1(plt, Input):
    # print("原始資料 :\n", Input, sep="")
    m, n = np.shape(Input)
    # print("shape :", m, n)
    target = Input[:, -1]
    # print("目標 :\n", target, sep="")
    for i in range(m):
        if target[i] == 0:
            plt.scatter(Input[i, 0], Input[i, 1], c="blue", marker="o")
        else:
            plt.scatter(Input[i, 0], Input[i, 1], c="red", marker="s")


# 硬限幅函数
def hardlim(dataSet):
    dataSet[np.nonzero(dataSet.A > 0)[0]] = 1
    dataSet[np.nonzero(dataSet.A <= 0)[0]] = 0
    return dataSet


# Logistic函数
def logistic(wTx):
    return 1.0 / (1.0 + np.exp(-wTx))


# 分类函数
def classifier(testData, weights):
    prob = logistic(sum(testData * weights))  # 求取概率--判别算法
    if prob > 0.5:
        return 1.0  # prob>0.5 返回为1
    else:
        return 0.0  # prob<=0.5 返回为0


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

print("treePlotter2.py")

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if (
            type(secondDict[key]).__name__ == "dict"
        ):  # test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if (
            type(secondDict[key]).__name__ == "dict"
        ):  # test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(
        nodeTxt,
        xy=parentPt,
        xycoords="axes fraction",
        xytext=centerPt,
        textcoords="axes fraction",
        va="center",
        ha="center",
        bbox=nodeType,
        arrowprops=arrow_args,
    )


def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(
    myTree, parentPt, nodeTxt
):  # if the first key tells you what feat was split on
    numLeafs = getNumLeafs(myTree)  # this determines the x width of this tree
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]  # the text label for this node should be this
    cntrPt = (
        plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW,
        plotTree.yOff,
    )
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if (
            type(secondDict[key]).__name__ == "dict"
        ):  # test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key], cntrPt, str(key))  # recursion
        else:  # it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


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

print("Recommand_Lib.py")

import operator
import scipy.spatial.distance as dist


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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("svdRec.py")


def loadExData():
    return [
        [0, 0, 0, 2, 2],
        [0, 0, 0, 3, 3],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [2, 2, 2, 0, 0],
        [5, 5, 5, 0, 0],
        [1, 1, 1, 0, 0],
    ]


def loadReData():
    return [
        [4, 4, 0, 2, 2],
        [4, 0, 0, 3, 3],
        [4, 0, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [2, 2, 2, 0, 0],
        [5, 5, 5, 0, 0],
        [1, 1, 1, 0, 0],
    ]


def loadExData2():
    return [
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
        [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0],
    ]


# 欧氏距离：
# 二维空间的欧氏距离公式：sqrt((x1-x2)^2+(y1-y2)^2)
def ecludSim(inA, inB):
    return 1.0 / (1.0 + np.linalg.norm(inA - inB))


# 皮尔逊相似度：corrcoef相关系数:衡量X与Y线性相关程度,其绝对值越大,则表明X与Y相关度越高。
# E((X-EX)(Y-EY))/sqrt(D(X)D(Y))
def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


# 夹角余弦：计算空间内两点之间的夹角余弦
# 两个n维样本点a(x11,x12,…,x1n)和b(x21,x22,…,x2n)的夹角余弦
# cos(theta) = a*b/(|a|*|b|)
def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = np.linalg.norm(inA) * np.linalg.norm(inB)
    return 0.5 + 0.5 * (num / denom)


# 标准相似度计算方法下的用户估计值
def standEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]  # 列数
    simTotal = 0.0
    ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user, j]  # 数据集第user行第j列的元素值
        if userRating == 0:
            continue  # 跳过未评估项目
        # logical_and:矩阵逐个元素运行逻辑与,返回值为每个元素的True,False
        # dataMat[:,item].A>0: 第item列中大于0的元素
        # dataMat[:,j].A: 第j列中大于0的元素
        # overLap: dataMat[:,item],dataMat[:,j]中同时都大于0的那个元素的行下标
        overLap = nonzero(logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0))[0]
        # 计算相似度
        if len(overLap) == 0:
            similarity = 0
        else:
            similarity = simMeas(
                dataMat[overLap, item], dataMat[overLap, j]
            )  # 计算overLap矩阵的相似度
        # print "第%d列和第%d列的相似度是: %f" %(item, j, similarity)
        # 累计总相似度
        simTotal += similarity
        # ratSimTotal = 相似度*元素值
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0  # 如果总相似度为0，返回0
    # 返回相似度*元素值/总相似度
    else:
        # print "ratSimTotal:",ratSimTotal
        # print "simTotal:",simTotal
        return ratSimTotal / simTotal


# 使用svd进行估计
def svdEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    # svd相似性计算的核心
    U, Sigma, VT = np.linalg.svd(dataMat)  # 计算矩阵的奇异值分解
    # Sig4 = np.mat(eye(4)*Sigma[:4]) # 取Svd特征值的前4个构成对角阵
    # xformedItems = dataMat.T * U[:,:4] * Sig4.I  # 创建变换后的项目矩阵create transformed items
    V = VT.T  # V是dataMat的相似矩阵
    xformedItems = V[:, :4]
    # print "xformedItems:",xformedItems
    # 逐列遍历数据集
    for j in range(n):
        userRating = dataMat[user, j]  # 未评级用户为0,因此不会计算。其他的均有值
        # print "userRating:",userRating
        # 跳过未评级的项目
        if userRating == 0 or j == item:
            continue
        # 使用指定的计算公式计算向量间的相似度
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)  # 相似度计算公式
        # print "待评估%d列和第%d列的相似度是: %f" % (item, j, similarity)
        simTotal += similarity  # 计算累计总相似度
        ratSimTotal += similarity * userRating  # ratSim = 相似度*项目评估值
    if simTotal == 0:
        return 0
    else:
        return ratSimTotal / simTotal


# 产生推荐结果的主方法
# simMeas取值:cosSim, pearsSim, ecludSim
# estMethod取值:standEst,svdEst
# user 用户项目矩阵中进行评估的行下标
# N=3返回前3项
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=svdEst):
    unratedItems = nonzero(dataMat[user, :].A == 0)[1]  # 查找未评级的项目--即用户--项目矩阵中user行对应的零值
    # print "unratedItems:",unratedItems
    # unratedItems: 未评估的项目--项目矩阵中user行对应零值的列下标
    if len(unratedItems) == 0:
        return "已经对所有项目评级"
    # 初始化项目积分数据类型,是一个二维矩阵
    # 元素1:item;元素2:评分值
    itemScores = []
    # 循环进行评估:将每个未评估项目于已评估比较，计算相似度
    # 本例中未评估项目取值1,2
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)  # 使用评估方法对数据评估，返回评估积分
        itemScores.append((item, estimatedScore))  # 并在项目积分内加入项目和对应的评估积分
    # 返回排好序的项目和积分，N=3返回前3项
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]


""" no file
print("testRecomm01.py")

# 加载修正后数据
dataMat = file2matrix("ml_data/training.txt", "\t")
print(dataMat[0][0])
# 相似公式：夹角余弦
output1 = recommend(dataMat, 1)
print(output1)

# 相似公式：欧氏距离
# output2 = recommend(dataMat,1,simMeas=ecludSim)
# print(output2)

# 相似公式：相关系数
# output3 = recommend(dataMat,1,simMeas=pearsSim)
# print(output3)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("svdtest01.py")

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
# print "hU:",hU
# print "hV:",hV
sigma = np.sqrt(lamda)  # 特征值
print("sigma:", sigma)

Sigma = np.zeros([np.shape(A)[0], np.shape(A)[1]])
U, S, VT = np.linalg.svd(A)
# Sigma[:np.shape(A)[0], :np.shape(A)[0]] = np.diag(S)
# print(U)
print(S)
# print(VT)

# print(U*Sigma*VT)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("testRecommsvd.py")


# 夹角余弦，避免除0
def cosSim(inA, inB):
    denom = np.linalg.norm(inA) * np.linalg.norm(inB)
    return float(inA * inB.T) / (denom + eps)


# 加载修正后数据
A = np.mat(
    [[5, 5, 3, 0, 5, 5], [5, 0, 4, 0, 4, 4], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]]
)
new = np.mat([[5, 5, 0, 0, 0, 5]])

U, S, VT = np.linalg.svd(A.T)
V = VT.T
Sigma = np.diag(S)
r = 2  # 取前两个奇异值
# 近似后的U,S,V值
Ur = U[:, :r]
Sr = Sigma[:r, :r]
Vr = V[:, :r]
# 计算new的坐标值
newresult = new * Ur * np.linalg.inv(Sr)
print(newresult)

maxv = 0  # 最大的余弦值
maxi = 0  # 最大值的下标
indx = 0
# 计算最近似的结果
for vi in Vr:
    temp = cosSim(newresult, vi)
    if temp > maxv:
        maxv = temp
        maxi = indx
    indx += 1
print(maxv, maxi)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("testRecommsvd2.py")

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

print("gradient_test.py")

# 输入数据
Input = file2matrix("data2/testSet.txt", "\t")
# print("原始資料 :\n", Input, sep="")

target = Input[:, -1]  # 获取分类标签列表
# print("目標 :\n", target, sep="")

[m, n] = np.shape(Input)
# print("shape :", m, n)

# 按分类绘制散点图
drawScatterbyLabel1(plt, Input)

# 构建x+b 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
# print("dataMat :\n", dataMat, sep="")

alpha = 0.001  # 步长
steps = 500  # 迭代次数

weights = np.ones((n, 1))  # 初始化权重向量
# 主程序
for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = hardlim(gradient)  # 硬限幅函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors

print("輸出權重 :\n", weights, sep="")  # 输出权重

X = np.linspace(-5, 5, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(np.double(weights[0]) + X * (np.double(weights[1]))) / np.double(weights[2])
plt.plot(X, Y)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("iterate_test.py")

# 求解原方程
A = np.mat([[8, -3, 2], [4, 11, -1], [6, 3, 12]])
b = np.mat([20, 33, 36])
result = np.linalg.solve(A, b.T)
print(result)

# 迭代求原方程组的解：x(k+1)=B0*x(k)+f
B0 = np.mat(
    [
        [0.0, 3.0 / 8.0, -2.0 / 8.0],
        [-4.0 / 11.0, 0.0, 1.0 / 11.0],
        [-6.0 / 12.0, -3.0 / 12.0, 0.0],
    ]
)
m, n = np.shape(B0)
f = np.mat([[20.0 / 8.0], [33.0 / 11.0], [36.0 / 12.0]])

error = 1.0e-6  # 误差阈值
steps = 100  # 迭代次数
xk = np.zeros((n, 1))  # 初始化 xk=x0
errorlist = []  # 记录逐次逼近的误差列表
for k in range(steps):  # 主程序
    xk_1 = xk  # 上一次的xk
    xk = B0 * xk + f  # 本次xk
    errorlist.append(np.linalg.norm(xk - xk_1))  # 计算并存储误差
    if errorlist[-1] < error:  # 判断误差是否小于阈值
        print(k + 1)  # 输出迭代次数
        break
print(xk)  # 输出计算结果
# 绘制误差收敛散点图
matpts = np.zeros((2, k + 1))
matpts[0] = np.linspace(1, k + 1, k + 1)
matpts[1] = np.array(errorlist)
drawScatter2(plt, matpts)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("logistic_test2.py")

weights = np.mat([[4.12414349], [0.48007329], [-0.6168482]])
testdata = np.mat([-0.147324, 2.874846])
m, n = np.shape(testdata)
testmat = np.zeros((m, n + 1))
testmat[:, 0] = 1
testmat[:, 1:] = testdata
print(classifier(testmat, weights))

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

print("stoc_test.py")

Input = file2matrix("data2/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 按分类绘制散点图
drawScatterbyLabel1(plt, Input)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 保留 讀取檔案 ok
print("normalequation.py")


def loadDataSet3(filename):
    X = []
    Y = []
    fr = open(filename)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append(float(curLine[0]))
        Y.append(float(curLine[-1]))
    return X, Y


# 数据矩阵,分类标签
xArr, yArr = loadDataSet3("data2/regdataset.txt")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# hmm01.py

# 起始概率
startP = np.mat([0.63, 0.17, 0.20])
# 状态转移概率[i,j]:i(t),j(t+1)
stateP = np.mat([[0.5, 0.25, 0.25], [0.375, 0.125, 0.375], [0.125, 0.675, 0.375]])
# 发射（混合）概率
# 列向量：emitP[:,i] = 隐含层状态; emitP[j,:] = 显式层状态
emitP = np.mat([[0.6, 0.20, 0.05], [0.25, 0.25, 0.25], [0.05, 0.10, 0.50]])

# 计算概率：干旱－干燥－潮湿
# 初始化概率：干旱：startP*emitP
state1Emit = np.multiply(startP, emitP[:, 0].T)
print(state1Emit)
print("argmax:", state1Emit.argmax())

# 计算干燥的概率:
state2Emit = stateP * state1Emit.T
state2Emit = np.multiply(state2Emit, emitP[:, 1])
print(state2Emit.T)
print("argmax:", state2Emit.argmax())

# 计算潮湿的概率:
state3Emit = stateP * state2Emit
state3Emit = np.multiply(state3Emit, emitP[:, 2])
print(state3Emit.T)
print("argmax:", state3Emit.argmax())

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# hmm02.py

# 起始概率
startP = np.mat([0.63, 0.17, 0.20])
# 状态转移概率[i,j]:i(t),j(t+1)
stateP = np.mat([[0.5, 0.375, 0.125], [0.25, 0.125, 0.675], [0.25, 0.375, 0.375]])
# 发射（混合）概率
emitP = np.mat(
    [[0.6, 0.20, 0.15, 0.05], [0.25, 0.25, 0.25, 0.25], [0.05, 0.10, 0.35, 0.50]]
)

# 计算概率：干旱－干燥－潮湿
state1Emit = np.multiply(startP.T, emitP[:, 0])
print(state1Emit)
best = state1Emit.argmax()
print("max", state1Emit.max(), "path1:", state1Emit.argmax())

# 计算干燥的概率:
print(state1Emit[best], stateP)
state2Mat = np.multiply(state1Emit[best], stateP)
print(state2Mat)
state2Mat = np.dot(state2Mat, emitP[:, 1])
print("max", state2Mat.max(), "path1:", state2Mat.argmax())
"""
# 计算潮湿的概率:
state3Mat = np.multiply(state2Mat[best],stateP)
state3Mat = np.dot(state3Mat,emitP[:,1])
print("max",state3Mat.max(),"path1:",state3Mat.argmax())
"""

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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
