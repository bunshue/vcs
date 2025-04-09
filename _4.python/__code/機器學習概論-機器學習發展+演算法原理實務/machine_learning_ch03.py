"""
machine_learning_ch03

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
    # plt.show()
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

print("common_libs.py")

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


# 绘制分类点
def drawScatterbyLabel2(plt, Input):
    m, n = np.shape(Input)
    target = Input[:, -1]
    for i in range(m):
        if target[i] == 1:
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


def buildMat(dataSet):
    m, n = np.shape(dataSet)
    dataMat = np.zeros((m, n))
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
    xMat = np.mat(np.ones((len(xArr), 2)))
    yMat = np.mat(np.ones((len(yArr), 1)))
    xMat[:, 1:] = (np.mat(xArr).T)[:, 0:]
    yMat[:, 0:] = (np.mat(yArr).T)[:, 0:]
    xTx = xMat.T * xMat
    if np.linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T * yMat)
    return ws


def loadDataSet1(fileName):  # general function to parse tab -delimited floats
    dataMat = []  # assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(float, curLine)  # map all elements to float()
        dataMat.append(fltLine)
    return dataMat


def loadDataSet2(fileName):
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


def loadDataSet3(fileName):
    X = []
    Y = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append(float(curLine[0]))
        Y.append(float(curLine[-1]))
    return X, Y


def loadDataSet4(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1
    X = []
    Y = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        X.append([float(curLine[i]) for i in range(numFeat)])
        Y.append(float(curLine[-1]))
    return X, Y


def plotscatter1(Xmat, Ymat, a, b, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    Xmat.sort()  # 对Xmat各元素进行排序
    yhat = [a * float(xi) + b for xi in Xmat]  # 计算预测值
    plt.plot(Xmat, yhat, "r")  # 绘制回归线
    show()


def plotscatter2(Xmat, Ymat, a, b, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    Xmat.sort()  # 对Xmat各元素进行排序
    yhat = [a * float(xi) + b for xi in Xmat]  # 计算预测值
    plt.plot(Xmat, yhat, "r")  # 绘制回归线
    show()
    return yhat


def plotscatter3(Xmat, Ymat, yHat, plt):
    fig = plt.figure()
    ax = fig.add_subplot(111)  # 绘制图形位置
    ax.scatter(Xmat, Ymat, c="blue", marker="o")  # 绘制散点图
    plt.plot(Xmat, yHat, "r")  # 绘制散点图
    show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("classReg.py")

fileName = "data03/ex0.txt"
dataSet = loadDataSet1(fileName)
# 转换为矩阵
dataSet = np.mat(dataSet)

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

print("trees2.py")

import operator


# 创建数据集
def createDataSet():
    # 无需浮出水面,脚蹼,是否是鱼类
    dataSet = [[1, 1, "yes"], [1, 1, "yes"], [1, 0, "no"], [0, 1, "no"], [0, 1, "no"]]
    labels = ["no surfacing", "flippers"]  # [无需浮出水面,脚蹼]
    # change to discrete values
    return dataSet, labels


# 分隔数据集：删除特征轴所在的数据列，返回剩余的数据集
# dataSet：数据集
# axis：特征轴
# value：特征轴的取值
def splitDataSet(dataSet, axis, value):
    # 初始化划分后的数据集:list
    retDataSet = []
    # 遍历数据集中所有行
    for featVec in dataSet:
        # 如果featVec[axis]取值等于value
        if featVec[axis] == value:
            # 从数据集中删除掉特征轴所在列
            reducedFeatVec = featVec[:axis]  # list操作 提取0~(axis-1)的元素
            # print "reducedFeatVec1:",reducedFeatVec
            reducedFeatVec.extend(featVec[axis + 1 :])  # list操作 将特征轴（列）之后的元素加回
            # print "reducedFeatVec2:",reducedFeatVec
            # 把删除特征轴的划分数据附加到返回矩阵中
            retDataSet.append(reducedFeatVec)
            # print "retDataSet:",retDataSet
    # 返回划分后的特征矩阵
    return retDataSet


# 存储树到文件
def storeTree(inputTree, filename):
    fw = open(filename, "w")
    pickle.dump(inputTree, fw)
    fw.close()


# 从文件抓取树
def grabTree(filename):
    fr = open(filename)
    return pickle.load(fr)


print("classify01.py")

import copy

dataSet, labels = createDataSet()
print(dataSet, labels)
treelabels = copy.deepcopy(labels)


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

print("test1.py")


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]  # list操作 提取0~(axis-1)的元素
            reducedFeatVec.extend(featVec[axis + 1 :])  # list操作 将特征轴（列）之后的元素加回
            retDataSet.append(reducedFeatVec)
    # 返回划分后的特征矩阵
    return retDataSet


# P1=128.0/384.0
# P2=256.0/384.0
P1 = 257.0 / 384.0
P2 = 127.0 / 384.0
Ip1p2 = -P1 * np.log2(P1) - P2 * np.log2(P2)
print(Ip1p2)

mylist = [1, 0, 1, 0, 1, 0, 0]
items = dict([(mylist.count(i), i) for i in mylist])
print(items[max(items.keys())])
dataset = [[1, 0], [0, 1], [1, 0]]
numEntries = len(dataset)  # 得到数据集行数
labelCounts = {}  # 初始化类别标签	for featVec in dataset: # 这段代码计算了数据集中各个特征向量的和
for featVec in dataset:
    currentLabel = featVec[-1]
    if currentLabel not in labelCounts.keys():
        labelCounts[currentLabel] = 0
    labelCounts[currentLabel] += 1
print(labelCounts)
cateList = [data[-1] for data in dataset]  # 从数据集中得到类别标签
items = dict([(cateList.count(i), i) for i in cateList])  # 得到类别为key，出现次数value的字典
print(items)

print(splitDataSet(dataset, 0, 0))

P1 = 640.0 / 1024.0
P2 = 384.0 / 1024.0
Ip1p2 = -P1 * np.log2(P1) - P2 * np.log2(P2)
print(Ip1p2)
print(0.9544 - 0.6877)

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

print("bikMeans_test.py")

# 从文件构建的数据集
dataMat = file2matrix("data04/4k2_far.txt", "\t")

print(dataMat)

dataSet = np.mat(dataMat[:, 1:])  # 转换为矩阵形式

print(dataSet)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("kMeans_test.py")

# 从文件构建的数据集
dataMat = file2matrix("data04/4k2_far.txt", "\t")
dataSet = np.mat(dataMat[:, 1:])  # 转换为矩阵形式
# dataSet = file2matrix("data04/testSet.txt","\t")

k = 4  # 外部指定1,2,3... 通过观察数据集有4个聚类中心
m = np.shape(dataSet)[0]  # 返回矩阵的行数

# 本算法核心数据结构:行数与数据集相同
# 列1：数据集对应的聚类中心,列2:数据集行向量到聚类中心的距离
ClustDist = np.mat(np.zeros((m, 2)))

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

eps = 1.0e-6
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

eps = 1.0e-6
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

eps = 1.0e-6


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

print("data.py")

Input = file2matrix("data05/testSet.txt", "\t")
m, n = np.shape(Input)
print(m, n)
newdata = np.zeros((m, 3))
newdata[:, :2] = Input[:, :2]
newdata[:, 2:2] = Input[:, 3:3]
print(newdata[:100, :])

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("gradient_test.py")

# 输入数据
Input = file2matrix("data05/testSet.txt", "\t")
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

print("log_evalue_weight.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 按分类绘制散点图
drawScatterbyLabel1(plt, Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)

# print dataMat

# 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = np.ones((n, 1))  # 初始化权重向量
weightlist = []

# 主程序
for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
# 绘制训练后超平面
X = np.linspace(-5, 5, 100)
Ylist = []
lenw = len(weightlist)
for indx in range(lenw):
    if indx % 20 == 0:  # 每20次输出一次分类超平面
        weight = weightlist[indx]
        Y = -(np.double(weight[0]) + X * (np.double(weight[1]))) / np.double(weight[2])
        plt.plot(X, Y)
        # 分类超平面注释
        plt.annotate("hplane:" + str(indx), xy=(X[99], Y[99]))
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("log_evalue_weight2.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)

# print dataMat

# 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = np.ones((n, 1))  # 初始化权重向量
weightlist = []

# 主程序

for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
weightmat = np.mat(np.zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = np.linspace(0, steps, steps)
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("log_evalue_weight3.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)

# print dataMat

# 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = np.ones((n, 1))  # 初始化权重向量
weightlist = []

# 主程序
for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(211)
axes2 = plt.subplot(212)
weightmat = np.mat(np.zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = np.linspace(0, steps, steps)
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("log_evalue_weight4.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)

# print dataMat

# 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = np.ones((n, 1))  # 初始化权重向量
weightlist = []

# 主程序
for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors
    weightlist.append(weights)

print(weights)  # 输出训练后的权重
fig = plt.figure()
axes1 = plt.subplot(311)
axes2 = plt.subplot(312)
axes3 = plt.subplot(313)
weightmat = np.mat(np.zeros((steps, n)))
i = 0
for weight in weightlist:
    weightmat[i, :] = weight.T
    i += 1
X = np.linspace(0, steps, steps)
# 输出前10个点的截距变化
axes1.plot(X, weightmat[:, 0], color="blue", linewidth=1, linestyle="-")
axes1.set_ylabel("weight[0]")
axes2.plot(X, weightmat[:, 1], color="red", linewidth=1, linestyle="-")
axes2.set_ylabel("weight[1]")
axes3.plot(X, weightmat[:, 2], color="green", linewidth=1, linestyle="-")
axes3.set_ylabel("weight[2]")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("logistic_test.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 按分类绘制散点图
drawScatterbyLabel1(plt, Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)
print(dataMat[:10, :])

# 定义步长和迭代次数
alpha = 0.001  # 步长
steps = 500  # 迭代次数
weights = np.ones((n, 1))  # 初始化权重向量

# 主程序
for k in range(steps):
    gradient = dataMat * np.mat(weights)  # 梯度
    output = logistic(gradient)  # logistic函数
    errors = target - output  # 计算误差
    weights = weights + alpha * dataMat.T * errors

print(weights)  # 输出训练后的权重
# 绘制训练后超平面
X = np.linspace(-7, 7, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(np.double(weights[0]) + X * (np.double(weights[1]))) / np.double(weights[2])
plt.plot(X, Y)
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

print("stoc_evalue_alpha.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = np.ones(n)  # 初始化权重向量

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
        # del dataIndex[randIndex]  # 从数据集中删除选取的随机索引

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("stoc_evalue_weight.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = np.ones(n)  # 初始化权重向量

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
        # del dataIndex[randIndex]  # 从数据集中删除选取的随机索引
    weightlist.append(weights)

lenwl = len(weightlist)
weightmat = np.zeros((lenwl, n))
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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("stoc_evalue_weight2.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

dataMat = buildMat(Input)

# 4. 定义迭代次数
steps = 500  # 迭代次数
weights = np.ones(n)  # 初始化权重向量

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
        # del dataIndex[randIndex]  # 从数据集中删除选取的随机索引
    weightlist.append(weights)

lenwl = len(weightlist)
weightmat = np.zeros((lenwl, n))
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

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("stoc_test.py")

Input = file2matrix("data05/testSet.txt", "\t")
target = Input[:, -1]  # 获取分类标签列表
[m, n] = np.shape(Input)

# 按分类绘制散点图
drawScatterbyLabel1(plt, Input)

# 构建b+x 系数矩阵：b这里默认为1
dataMat = buildMat(Input)

# print dataMat

# 定义步长和迭代次数
steps = 500  # 迭代次数
weights = np.ones(n)  # 初始化权重向量

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
        # del dataIndex[randIndex]  # 从数据集中删除选取的随机索引

print(weights)  # 输出训练后的权重
weights = weights.tolist()[0]
# 6. 绘制训练后超平面
X = np.linspace(-5, 5, 100)
# y=w*x+b: b:weights[0]/weights[2]; w:weights[1]/weights[2]
Y = -(np.double(weights[0]) + X * (np.double(weights[1]))) / np.double(weights[2])
plt.plot(X, Y)
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import copy

# 输入数据
Input = file2matrix("data05/test.txt", "\t")
target = Input[:, 0].copy()
Input[:, 0] = Input[:, 2].copy()
Input[:, 2] = target.copy()
[m, n] = np.shape(Input)

print(m)
print(n)

# 按分类绘制散点图
drawScatterbyLabel2(plt, Input)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("lassoReg.py")


# 矩阵标准化
def normData(xArr, yArr):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat, 0)
    xMeans = np.mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = np.var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, k):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = np.shape(wMatT)
    for i in range(m):
        ax.plot(k, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(0, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet2("data07/ridgedata2.txt")
# 数据矩阵转换
xMat, yMat = normData(xArr, yArr)
m, n = np.shape(xMat)
eps = 0.005  # 迭代步长变化
numIt = 1000  # 迭代次数

returnMat = np.zeros((numIt, n))  # 返回矩阵
ws = np.zeros((n, 1))  # 初始化ws为全零向量
wsTest = ws.copy()
wsMax = ws.copy()
for i in range(numIt):
    lowestError = np.inf
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

print("leastSquare.py")

# 数据文件名
Xmat, Ymat = loadDataSet3("data07/regdataset.txt")
meanX = np.mean(Xmat)  # 原始数据集的均值
meanY = np.mean(Ymat)
dX = Xmat - meanX  # 各元素与均值的差
dY = Ymat - meanY
# 手工计算：
# sumXY = 0; SqX = 0
# for i in range(len(dX)):
# 	sumXY += np.double(dX[i])*np.double(dY[i])
# 	SqX += np.double(dX[i])**2
sumXY = np.vdot(dX, dY)  # 返回两个向量的点乘 multiply
SqX = sum(np.power(dX, 2))  # 向量的平方：(X-meanX)^2

# 计算斜率和截距
a = sumXY / SqX
b = meanY - a * meanX
print(a, b)
# 绘制图形
plotscatter1(Xmat, Ymat, a, b, plt)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("logistic_k.py")


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


x1 = logistic_map(3.5, 0.1)
x2 = logistic_map(3.5, 0.9)
scatterplot(3.5, x1, x2)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("logistic_map.py")


def scatterplot(k, wMat):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    m, n = np.shape(wMat)
    for i in range(m):  # 逐列描点
        ax.scatter(np.mat(k), wMat[:, i], s=0.1, marker=".")
    show()


maxIter = 1000  # 最大迭代数和系数分辨率区间
k = np.linspace(2.1, 4.0, maxIter)  # logisitic区间
klen = len(k)
xMat = np.mat(np.zeros((klen, maxIter)))  # 初始化结果矩阵
x = 1.0 / float(maxIter)
for i in range(klen):  # 沿系数方向循环
    for j in range(maxIter):
        x = float(k[i]) * x * (1.0 - x)  # 变量迭代
        xMat[i, j] = x

# 绘制图形
print(k.shape)
print(xMat.shape)
# NG scatterplot(k, xMat)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("multilinear.py")

# 岭回归函数


# 矩阵标准化
def normData(xMat, yMat):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat, 0)
    xMeans = np.mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = np.var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = np.shape(wMatT)
    for i in range(m):
        ax.plot(wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(i, wMatT[i, 0]), color="black")
    show()


def Multicollinear(xMat):
    features = xMat.T
    m, n = np.shape(features)
    for i in range(m):
        if i == (m - 1):
            print(i, ":", 0)
            print(np.corrcoef(features[i], features[0]))
        else:
            print(i, ":", i + 1)
            print(np.corrcoef(features[i], features[i + 1]))


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet2("data07/ridgedata.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集
Multicollinear(xMat)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("normalequation.py")


# 数据矩阵,分类标签
xArr, yArr = loadDataSet3("data07/regdataset.txt")
# 生成X坐标列
m = len(xArr)
Xmat = np.mat(np.ones((m, 2)))
for i in range(m):
    Xmat[i, 1] = xArr[i]
Ymat = np.mat(yArr).T  # 转换为y列

xTx = Xmat.T * Xmat  # 矩阵左乘自身的转置

ws = []
if np.linalg.det(xTx) != 0.0:
    # 计算直线的斜率和截距
    # 矩阵正规方程组公式:inv(X.T*X)*X.T*Y
    ws = xTx.I * (Xmat.T * Ymat)
else:
    print("This matrix is singular, cannot do inverse")
    sys.exit(0)  # 退出程序
print("ws:", ws)


# NG yHat = plotscatter2(Xmat[:,1],Ymat,ws[1,0],ws[0,0],plt)

# 计算相关系数:
# NG print(np.corrcoef(yHat, Ymat.T))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("rbfNettest.py")

# 数据矩阵,分类标签
xArr, yArr = loadDataSet4("data07/nolinear.txt")
# 局部加权线性回归算法：回归线矩阵

# RBF函数的平滑系数
miu = 0.02
k = 0.03

# 数据集坐标数组转换为矩阵
xMat = np.mat(xArr)
yMat = np.mat(yArr).T
testArr = xArr  # 测试数组
m, n = np.shape(xArr)  # xArr的行数
yHat = np.zeros(m)  # yHat是y的预测值,yHat的数据是y的回归线矩阵
for i in range(m):
    weights = np.mat(np.eye(m))
    for j in range(m):
        diffMat = testArr[i] - xMat[j, :]
        # 利用高斯核函数计算权重矩阵,计算后的权重是一个对角阵
        weights[j, j] = np.exp(diffMat * diffMat.T / (-miu * k**2))
    xTx = xMat.T * (weights * xMat)  # 矩阵左乘自身的转置
    if np.linalg.det(xTx) != 0.0:
        ws = xTx.I * (xMat.T * (weights * yMat))
        yHat[i] = testArr[i] * ws  # 计算回归线坐标矩阵
    else:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)  # 退出程序


# NG plotscatter3(xMat[:,1],yMat,yHat,plt) # 绘制图形

# 计算相关系数:
# NG print(np.corrcoef(yHat,yMat.T))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("rbm.py")

from scipy import sparse as S
from scipy.sparse.csr import csr_matrix


def normalize(x):
    V = x.copy()
    V -= x.min(axis=1).reshape(x.shape[0], 1)
    V /= V.max(axis=1).reshape(x.shape[0], 1)
    return V


def sigmoid(x):
    # return x*(x > 0)
    # return np.tanh(x)
    return 1.0 / (1 + np.exp(-x))


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
            self.W = np.random.uniform(-0.1, 0.1, (n_visible, n_hidden)) / np.sqrt(
                n_visible + n_hidden
            )
            self.W = np.insert(self.W, 0, 0, axis=1)
            self.W = np.insert(self.W, 0, 0, axis=0)
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
            bias = S.csr_matrix(np.ones((Input.shape[0], 1)))
            csr = S.hstack([bias, Input]).tocsr()
        else:
            csr = np.insert(Input, 0, 1, 1)
        for epoch in range(max_epochs):
            idx = np.arange(csr.shape[0])
            np.random.shuffle(idx)
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
            total_change = np.sum(np.abs(w_update))
            self.W += self.momentum * self.last_change + w_update
            self.W *= self.weight_decay

            self.last_change = w_update

            RMSE = np.mean((csr[idx] - self.V_state) ** 2) ** 0.5
            self.Errors.append(RMSE)
            self.epoch += 1
            # print("Epoch %s: RMSE = %s; ||W||: %6.1f; Sum Update: %f" % (self.epoch, RMSE, np.sum(np.abs(self.W)), total_change))
        return self

    def learning_curve(self):
        plt.ion()
        # plt.figure()
        E = np.array(self.Errors)
        E = pd.DataFrame(E)
        plt.plot(E.rolling(50).mean()[50:])
        show()

    def activate(self, X):
        if X.shape[1] != self.W.shape[0]:
            if isinstance(X, S.csr_matrix):
                bias = S.csr_matrix(np.ones((X.shape[0], 1)))
                csr = S.hstack([bias, X]).tocsr()
            else:
                csr = np.insert(X, 0, 1, 1)
        else:
            csr = X
        p = sigmoid(csr.dot(self.W))
        p[:, 0] = 1.0
        return p

    def sample(self, H, addBias=True):
        if H.shape[1] == self.W.shape[0]:
            if isinstance(H, S.csr_matrix):
                bias = S.csr_matrix(np.ones((H.shape[0], 1)))
                csr = S.hstack([bias, H]).tocsr()
            else:
                csr = np.insert(H, 0, 1, 1)
        else:
            csr = H
        p = sigmoid(csr.dot(self.W.T))
        p[:, 0] = 1
        return p


data = np.random.uniform(0, 1, (100, 10))
rbm = RBM(10, 15)
rbm.fit(data, 1000)
rbm.learning_curve()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("ridgeReg.py")

# 岭回归函数


# 矩阵标准化
def normData(xArr, yArr):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat, 0)
    xMeans = np.mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = np.var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, k):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = np.shape(wMatT)
    for i in range(m):
        ax.plot(k, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(0, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet2("data07/ridgedata.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集

Knum = 30  # 确定lam的范围exp(-10~20)
# 初始化30行,8列的全0矩阵
wMat = np.zeros((Knum, np.shape(xMat)[1]))
klist = np.zeros((Knum, 1))
for i in range(Knum):
    k = float(i) / 500.0  # 算法的目的是确定k的取值
    klist[i] = k
    xTx = xMat.T * xMat
    denom = xTx + np.eye(np.shape(xMat)[1]) * k
    if np.linalg.det(denom) == 0.0:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)
    ws = denom.I * (xMat.T * yMat)
    wMat[i, :] = ws.T
print(klist)
scatterplot(klist, klist)  # k值的变化
scatterplot(wMat, klist)  # 岭回归

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("ridgeRegtest1.py")

# 岭回归函数


# 矩阵标准化
def normData(xMat, yMat):
    xMat = np.mat(xArr)
    yMat = np.mat(yArr).T
    yMean = np.mean(yMat, 0)
    xMeans = np.mean(xMat, 0)
    ynorm = yMat - yMean
    xVar = np.var(xMat, 0)
    xnorm = (xMat - xMeans) / xVar
    return xnorm, ynorm


def scatterplot(wMat, logk):  # 绘制图形
    fig = plt.figure()
    ax = fig.add_subplot(111)
    wMatT = wMat.T
    m, n = np.shape(wMatT)
    for i in range(m):
        ax.plot(logk, wMatT[i, :])
        ax.annotate("feature[" + str(i) + "]", xy=(i, wMatT[i, 0]), color="black")
    show()


# 前8列为xArr,后1列为yArr
xArr, yArr = loadDataSet2("data07/ridgedata2.txt")
xMat, yMat = normData(xArr, yArr)  # 标准化数据集

Knum = 100  # 确定lam的范围exp(-10~20)
# 初始化30行,8列的全0矩阵
wMat = np.zeros((Knum, np.shape(xMat)[1]))
klist = np.zeros((Knum, 1))
for i in range(Knum):
    k = i / 1000.0  # 算法的目的是确定k的取值
    klist[i] = k
    xTx = xMat.T * xMat
    denom = xTx + np.eye(np.shape(xMat)[1]) * k
    if np.linalg.det(denom) == 0.0:
        print("This matrix is singular, cannot do inverse")
        sys.exit(0)
    ws = denom.I * (xMat.T * yMat)
    wMat[i, :] = ws.T
print(klist)
scatterplot(klist, klist)  # k值的变化
scatterplot(wMat, klist)  # 岭回归

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

# list 轉 matrix
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
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
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


print("------------------------------------------------------------")  # 60個

print("------------------------------")  # 60個
