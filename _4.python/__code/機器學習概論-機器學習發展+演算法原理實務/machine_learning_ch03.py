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
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *


def loadDataSet(fileName):  # general function to parse tab -delimited floats
    dataMat = []  # assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split("\t")
        fltLine = map(float, curLine)  # map all elements to float()
        dataMat.append(fltLine)
    return dataMat


# 二元切分数据集
def binSplitDataSet(dataSet, feature, value):
    # nonzero(dataSet[:,feature] > value)[0]: 数据集第feature列大于value(特征值)的行向量
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :][0]
    # nonzero(dataSet[:,feature] <= value)[0]: 数据集第feature列小于等于value(特征值)的行向量
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :][0]
    return mat0, mat1


# 回归树叶子节点
def regLeaf(dataSet):
    return mean(dataSet[:, -1])  # 返被回划分数据集最后一列的均值


# 回归方差
# 返回数据集最后1列的二阶中心距乘以划分数据集的行数
def regErr(dataSet):
    return var(dataSet[:, -1]) * shape(dataSet)[0]


# 选择最优分割点
# leafType:叶子节点算法函数
# errType:回归方差算法函数
# ops:允许的方差下降值,最小切分样本数
def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    tolS = ops[0]
    # 允许的方差下降值
    tolN = ops[1]  # 最小切分样本数
    # ---- 算法终止条件1开始 ----#
    splitdataSet = set(dataSet[:, -1].T.tolist()[0])
    if len(splitdataSet) == 1:
        return None, leafType(dataSet)  # 返回值: leafType(dataSet):树的叶子节点
    # ---- 算法终止条件1结束 ----#

    # ---- 计算dataSet各列的最优划分方差,划分列,划分值 ----#
    m, n = shape(dataSet)  # 返回数据集的行数和列数
    S = errType(dataSet)  # 计算整个数据集的回归方差,S
    # 初始化最优参数: 最大方差、最优划分列、最优划分值
    bestS = inf
    bestIndex = 0
    bestValue = 0
    # 按列遍历数据集前n-1列
    # featIndex: 第0~n-1列
    for featIndex in range(n - 1):
        # 遍历每列去重后的各个类型
        # splitVal:各列的每个类型
        for splitVal in set(dataSet[:, featIndex]):
            # 二元划分数据集:按划分列和划分值分隔dataSet
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            # mat0的行数 小于 tolN 或 mat1的行数 小于 tolN
            if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
                continue  # 终止后面的程序,进行下一次循环
            # mat0的回归方差+mat1的回归方差
            newS = errType(mat0) + errType(mat1)
            # 如果newS小于bestS
            if newS < bestS:
                bestIndex = featIndex  # 最优索引 <- 特征索引
                bestValue = splitVal  # 最优值 <- 分割值
                bestS = newS  # bestS <- newS
    # ---- DataSet的最优划分参数：方差、划分列、划分值计算结束 ----#

    # ---- 算法终止条件2开始:返回的是值节点类型 ----#
    # 如果(S - bestS) 小于 1
    if (S - bestS) < tolS:
        # print "stop 2"
        # 返回值: feat==None,leafType(dataSet):数据集标签集的均值
        return None, leafType(dataSet)
    # ---- 算法终止条件2结束 ----#

    # ---- 算法终止条件3开始 ----#
    # 二元划分数据集:按划分列和划分值分隔dataSet
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    # mat0的行数小于 tolN 或 mat1的行数小于tolN
    if (shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
        # print "stop 3"
        return None, leafType(dataSet)
    # ---- 算法终止条件3结束 ----#
    # 算法终止的前3个条件的划分列为None,说明为叶子节点,本枝分类树划分结束

    # ---- 算法终止条件4开始:返回的是子树节点类型 ----#
    # print "stop 4"
    # 返回最优特征的划分列和划分值,但回归树还需递归划分
    return bestIndex, bestValue
    # ---- 算法终止条件4结束 ----#


# 创建分类回归树
# dataSet: 数据集矩阵
# leafType:叶子节点算法函数指针
# errType:回归方差算法函数指针
# ops: 允许的方差下降值,最小切分样本数--算法停止条件
def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1, 4)):
    # 选择最优划分: feat: 划分列, val: 划分值
    # 传递 叶子节点算法函数指针,回归方差算法函数指针,允许的方差下降值,最小切分样本数
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    # 停止条件:如果feat为空,算法停止, 返回叶子节点值
    if feat == None:
        return val
    retTree = {}
    retTree["spInd"] = feat  # 把划分列特征放入创建的树中
    retTree["spVal"] = val  # 把划分值放入创建的树中
    # 因为是面向过程的编程，判断树的节点级输出有些麻烦,增加调试信息：
    # 输出节点一级的信息,连续输出多少个就有多少层
    # 本算法为先左后右的递归，所以首先输出的是left node，当node输出中断后，才为另一侧的node
    # print "node:",retTree
    # 以划分列和元素为分割点二分数据集:dataSet被分为左右两部分：lSet:左子树集合, rSet:右子树集合
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    # 递归生成子树
    retTree["left"] = createTree(lSet, leafType, errType, ops)
    retTree["right"] = createTree(rSet, leafType, errType, ops)

    return retTree


# 判断是否为树,验证输入数据是否为字典
def isTree(obj):
    return type(obj).__name__ == "dict"


# 计算树叶子节点的均值
def getMean(tree):
    # 左、右子树递归至叶子节点处
    if isTree(tree["right"]):
        tree["right"] = getMean(tree["right"])
    if isTree(tree["left"]):
        tree["left"] = getMean(tree["left"])
    # 返回叶子节点的均值
    return (tree["left"] + tree["right"]) / 2.0


# 树的后剪枝
# testData: 测试集
def prune(tree, testData):
    if shape(testData)[0] == 0:
        return getMean(tree)  # 如果没有测试数据输入,运行getMean,程序退出
    # 如果左、右子节点是树
    if isTree(tree["right"]) or isTree(tree["left"]):
        # 对测试集按划分列和树的划分值进行二元分割
        lSet, rSet = binSplitDataSet(testData, tree["spInd"], tree["spVal"])
    if isTree(tree["left"]):
        tree["left"] = prune(tree["left"], lSet)  # 如果左节点是树，对测试集递归剪枝
    if isTree(tree["right"]):
        tree["right"] = prune(tree["right"], rSet)  # 如果右节点是树，对测试集递归剪枝
    # 如果左右节点都不是树
    if not isTree(tree["left"]) and not isTree(tree["right"]):
        lSet, rSet = binSplitDataSet(
            testData, tree["spInd"], tree["spVal"]
        )  # 对测试集按划分列和划分值进行二元分割
        # 计算左右子树的方差
        errorNoMerge = sum(power(lSet[:, -1] - tree["left"], 2)) + sum(
            power(rSet[:, -1] - tree["right"], 2)
        )
        # 执行合并：树节点均值
        treeMean = (tree["left"] + tree["right"]) / 2.0
        # 计算合并的方差
        errorMerge = sum(power(testData[:, -1] - treeMean, 2))
        # 如果合并后的方差小于不合并方差
        if errorMerge < errorNoMerge:
            # print "merging"
            return treeMean  # 返回节点均值,执行合并
        else:
            return tree  # 否则直接返回,不进行合并
    else:
        return tree


# 将模型数据格式化为线性函数的自变量X,因变量Y
def linearSolve(dataSet):  # helper function used in two places
    m, n = shape(dataSet)
    X = mat(ones((m, n)))
    Y = mat(ones((m, 1)))  # 初始化全X,Y
    X[:, 1:n] = dataSet[:, 0 : n - 1]
    Y = dataSet[:, -1]  # 为 X,Y 赋值
    xTx = X.T * X
    if linalg.det(xTx) == 0.0:
        raise NameError(
            "This matrix is singular, cannot do inverse,\n\
        try increasing the second value of ops"
        )
    ws = xTx.I * (X.T * Y)  # 产生截距和斜率矩阵
    return ws, X, Y  # 返回X,Y和线性回归的系数


# 产生叶子节点的模型，并返回系数
def modelLeaf(dataSet):
    ws, X, Y = linearSolve(dataSet)
    return ws


# 返回线性模型的预测值与实际值的方差
def modelErr(dataSet):
    ws, X, Y = linearSolve(dataSet)
    yHat = X * ws
    return sum(power(Y - yHat, 2))


# 回归树评估: 返回树节点的浮点值
def regTreeEval(model, inDat):
    return float(model)


# 模型树评估:Y = X*model
# model为二维向量: 斜率,截距
def modelTreeEval(model, inDat):
    n = shape(inDat)[1]  # inDat的列数
    X = mat(ones((1, n + 1)))  # 全1矩阵,1行,n+1列
    X[:, 1 : n + 1] = inDat
    return float(X * model)  # Y = X*model


# 树预测
# tree:回归树，模型树
# inData:第i行的测试集向量
# modelEval:与树一致的评估函数
def treeForeCast(tree, inData, modelEval=regTreeEval):
    # 如果不是树直接返回评估结果
    if not isTree(tree):
        return modelEval(tree, inData)
    # 如果inData[划分列]的取值大于tree[划分值]
    if inData[tree["spInd"]] > tree["spVal"]:
        # 如果tree的左子树是一颗树,而不是叶子节点 递归调用本函数
        if isTree(tree["left"]):
            return treeForeCast(tree["left"], inData, modelEval)
        # 否则返回叶子节点对应评估函数的评估值
        else:
            return modelEval(tree["left"], inData)
    else:  # 如果inData[划分列]的取值小于等于tree[划分值]
        # 如果tree的右子树是一颗树,而不是叶子节点,递归调用本函数
        if isTree(tree["right"]):
            return treeForeCast(tree["right"], inData, modelEval)
        # 否则返回叶子节点对应评估函数的评估值
        else:
            return modelEval(tree["right"], inData)


# 创建预测
# tree: 回归树，模型树
# testData: 测试集
# modelEval: 评估函数 regTreeEval,modelTreeEval
def createForeCast(tree, testData, modelEval=regTreeEval):
    m = len(testData)
    yHat = mat(zeros((m, 1)))  # 初始化为全0向量,行数为m
    for i in range(m):
        yHat[i, 0] = treeForeCast(tree, mat(testData[i]), modelEval)
    return yHat


# 02classReg.py

from numpy import *
import treeExplore

# 主程序
# 加载数据集
fileName = "data03/ex0.txt"
dataSet = loadDataSet(fileName)
# 转换为矩阵
dataSet = mat(dataSet)

# 创建树
regTree = createTree(dataSet)
print("regTree:", regTree)

treeExplore.createPlot(regTree)  # 创建决策树图

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# builddataset.py

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

# trees2.py

"""
Created on Oct 12, 2010
Decision Tree Source Code for Machine Learning in Action Ch. 3
@author: Peter Harrington
"""
from math import log
import operator


# 创建数据集
def createDataSet():
    # 无需浮出水面,脚蹼,是否是鱼类
    dataSet = [[1, 1, "yes"], [1, 1, "yes"], [1, 0, "no"], [0, 1, "no"], [0, 1, "no"]]
    labels = ["no surfacing", "flippers"]  # [无需浮出水面,脚蹼]
    # change to discrete values
    return dataSet, labels


# 计算香农熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)  # 得到数据集行数
    labelCounts = {}  # 初始化类别标签
    # featVec是指特征向量
    # 这段代码计算了数据集中各个特征向量的和
    for featVec in dataSet:
        # featVec[-1]：数据集行中最后一个元素-特征向量：这里是yes no
        currentLabel = featVec[-1]
        # 如果当前的字典labelCounts没有currentLabel对应特征向量的键，在字典中加入新的特征向量这个键
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        # 在字典labelCounts中currentLabel对应特征向量的键值+1
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0  # 初始化香农熵
    # 计算香农熵
    for key in labelCounts:
        # 计算各个特征向量的概率：特征向量出现的次数/总记录数
        prob = float(labelCounts[key]) / numEntries
        # 香农熵：= - p*log2(p) --shannonEnt2 = -prob * log(prob,2)
        # 这里计算的是整个数据集累计的香农熵
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


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


# 从数据集中选择最优的特征
def chooseBestFeatureToSplit(dataSet):
    # 计算特征向量维，其中最后一列用于类别标签，因此要减去
    numFeatures = len(dataSet[0]) - 1  # 特征向量维数= 行向量维度-1
    baseEntropy = calcShannonEnt(dataSet)  # 基础熵：源数据的香农熵
    # print "baseEntropy:",baseEntropy
    bestInfoGain = 0.0
    # 初始化最优的信息增益
    bestFeature = -1  # 初始化最优的特征轴

    # 外循环：遍历数据集各列,计算最优特征轴
    # i 为数据集列索引：取值范围 0~(numFeatures-1)
    for i in range(numFeatures):
        # 抽取第i列的列向量
        featList = [example[i] for example in dataSet]

        uniqueVals = set(featList)  # 去重：该列的唯一值集
        newEntropy = 0.0  # 初始化该列的香农熵

        # 内循环：按列和唯一值计算香农熵
        for value in uniqueVals:
            # 按选定列i和唯一值分隔数据集--删除选定列，返回剩余的数据集
            subDataSet = splitDataSet(dataSet, i, value)
            # print "subDataSet:",subDataSet
            # 概率：prob= 子数据集的行数/源数据集的行数
            prob = len(subDataSet) / float(len(dataSet))
            # 新香农熵：子数据集的概率*子数据集的香农熵
            # print "prob * calcShannonEnt(subDataSet):",prob * calcShannonEnt(subDataSet)
            # 累计新香农熵：newEntropy
            newEntropy += prob * calcShannonEnt(subDataSet)
        # print "newEntropy:",newEntropy
        # 根据新香农熵与基础熵比较计算信息量的增益（本质是熵的减少，无序度的减少）
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:  # 如果信息增益>0;
            bestInfoGain = infoGain  # 用当前信息增益值替代之前的最优增益值
            bestFeature = i  # 重置最优特征为当前列
    return bestFeature


# 计算最多的类别标签
def majorityCnt(classList):
    # 初始化字典：
    # key: 类别标签；value: 数量
    classCount = {}
    # 迭代将classList的向量值赋予classCount中
    for vote in classList:
        # 如果vote不存在在字典classCount的键中, 就加入这个键
        if vote not in classCount.keys():
            classCount[vote] = 0
        # 对应vote的字典值+1
        classCount[vote] += 1
    # 对分类数按value重新排序
    # 该句是按字典值排序的固定用法
    # classCount.iteritems()：字典迭代器函数
    # key：排序参数 operator.itemgetter(1)：多级排序
    sortedClassCount = sorted(
        classCount.iteritems(), key=operator.itemgetter(1), reverse=True
    )
    # print "sortedClassCount:",sortedClassCount
    # 返回出现最多类别标签
    return sortedClassCount[0][0]


# 创建决策树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]  # 抽取源数据集的决策标签列
    # 程序终止条件1
    # 统计第一个标签的数量：classList.count(classList[0])
    # 如果classList只有一种决策标签，停止划分，返回这个决策标签
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 程序终止条件2
    # 如果数据集的第一个决策标签只有一个
    # 返回最多的决策标签
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)

    # 算法核心：
    # 返回数据集的最优特征轴：这个特征轴的香农熵<数据集的香农熵
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # 获取最优的特征标签用于创建树
    bestFeatLabel = labels[bestFeat]
    # 构建决策树,树的结构：广义表的形式
    # key:最优特征轴标签; value: subTree
    myTree = {bestFeatLabel: {}}

    # 删除labels数组中对应的特征类别--即表示已经处理完成
    del labels[bestFeat]

    # 抽取最优特征轴的列向量
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)  # 去重

    for value in uniqueVals:
        subLabels = labels[:]  # 将删除后的特征类别集建立子类别集
        # print subLabels
        # 按最优特征轴和唯一值分隔数据集--删除特征轴的数据列，返回剩余的数据集
        splitDataset = splitDataSet(dataSet, bestFeat, value)
        # print splitDataset
        # 对分隔后的数据集按照子特征类别集递归--树的生长
        # 子树的数据结构: 键:唯一值; 值:类别标签或子树(递归返回)
        subTree = createTree(splitDataset, subLabels)
        # print "bestFeatLabel:",bestFeatLabel,"value:",value,"subTree:",subTree
        myTree[bestFeatLabel][value] = subTree

        # 对分隔后的数据集进行按照子特征类别集进行递归
        # myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)

    return myTree  # 返回生成后的决策树


# 分类器
def classify(inputTree, featLabels, testVec):
    firstStr = inputTree.keys()[0]  # 树根节点
    secondDict = inputTree[firstStr]  # value-子树结构或分类标签
    featIndex = featLabels.index(firstStr)  # 根节点在分类标签集中的位置
    key = testVec[featIndex]  # 测试集数组取值
    valueOfFeat = secondDict[key]  #
    # 判断 valueOfFeat 是否是 dict类型
    if isinstance(valueOfFeat, dict):
        classLabel = classify(valueOfFeat, featLabels, testVec)  # 递归分类
    else:
        classLabel = valueOfFeat
    return classLabel


# 存储树到文件
def storeTree(inputTree, filename):
    import pickle

    fw = open(filename, "w")
    pickle.dump(inputTree, fw)
    fw.close()


# 从文件抓取树
def grabTree(filename):
    import pickle

    fr = open(filename)
    return pickle.load(fr)


# classify01.py

from numpy import *
from math import log
import copy

dataSet, labels = createDataSet()
print(dataSet, labels)
treelabels = copy.deepcopy(labels)
myTree = createTree(dataSet, treelabels)
print(myTree)
testVec = [1, 0]

classLabel = classify(myTree, labels, testVec)
print("classLabel:", classLabel)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# treePlotter2.py

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


# if you do get a dictonary you know it's a tree, and the first element will be another dict


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


# def createPlot():
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     createPlot.ax1 = plt.subplot(111, frameon=False) #ticks for demo puropses
#     plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
#     plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
#     show()


def retrieveTree(i):
    listOfTrees = [
        {"no surfacing": {0: "no", 1: {"flippers": {0: "no", 1: "yes"}}}},
        {
            "no surfacing": {
                0: "no",
                1: {"flippers": {0: {"head": {0: "no", 1: "yes"}}, 1: "no"}},
            }
        },
    ]
    return listOfTrees[i]


# createPlot(thisTree)

print("------------------------------")  # 60個

# ID3DTree.py

from numpy import *
import copy
import pickle


class ID3DTree(object):
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []

    def loadDataSet(self, path, labels):
        recordlist = []
        fp = open(path, "rb")  # 读取文件内容
        content = fp.read()
        fp.close()
        rowlist = content.splitlines()  # 按行转换为一维表
        recordlist = [row.split("\t") for row in rowlist if row.strip()]
        self.dataSet = recordlist
        self.labels = labels

    def train(self):
        labels = copy.deepcopy(self.labels)
        self.tree = self.buildTree(self.dataSet, labels)

    # 创建决策树主程序
    def buildTree(self, dataSet, labels):
        cateList = [data[-1] for data in dataSet]  # 抽取源数据集的决策标签列
        # 程序终止条件1	: 如果classList只有一种决策标签，停止划分，返回这个决策标签
        if cateList.count(cateList[0]) == len(cateList):
            return cateList[0]
        # 程序终止条件2: 如果数据集的第一个决策标签只有一个 返回这个决策标签
        if len(dataSet[0]) == 1:
            return self.maxCate(cateList)
        # 算法核心：
        bestFeat = self.getBestFeat(dataSet)  # 返回数据集的最优特征轴：
        bestFeatLabel = labels[bestFeat]
        tree = {bestFeatLabel: {}}
        del labels[bestFeat]
        # 抽取最优特征轴的列向量
        uniqueVals = set([data[bestFeat] for data in dataSet])  # 去重
        for value in uniqueVals:
            subLabels = labels[:]  # 将删除后的特征类别集建立子类别集
            splitDataset = self.splitDataSet(dataSet, bestFeat, value)  # 按最优特征列和值分割数据集
            subTree = self.buildTree(splitDataset, subLabels)  # 构建子树
            tree[bestFeatLabel][value] = subTree
        return tree

    def maxCate(self, catelist):  # 计算出现最多的类别标签
        items = dict([(catelist.count(i), i) for i in catelist])
        return items[max(items.keys())]

    def getBestFeat(self, dataSet):
        # 计算特征向量维，其中最后一列用于类别标签，因此要减去
        numFeatures = len(dataSet[0]) - 1  # 特征向量维数= 行向量维度-1
        baseEntropy = self.computeEntropy(dataSet)  # 基础熵：源数据的香农熵
        bestInfoGain = 0.0
        # 初始化最优的信息增益
        bestFeature = -1  # 初始化最优的特征轴
        # 外循环：遍历数据集各列,计算最优特征轴
        # i 为数据集列索引：取值范围 0~(numFeatures-1)
        for i in range(numFeatures):  # 抽取第i列的列向量
            uniqueVals = set([data[i] for data in dataSet])  # 去重：该列的唯一值集
            newEntropy = 0.0  # 初始化该列的香农熵
            for value in uniqueVals:  # 内循环：按列和唯一值计算香农熵
                subDataSet = self.splitDataSet(dataSet, i, value)  # 按选定列i和唯一值分隔数据集
                prob = len(subDataSet) / float(len(dataSet))
                newEntropy += prob * self.computeEntropy(subDataSet)
            infoGain = baseEntropy - newEntropy  # 计算最大增益
            if infoGain > bestInfoGain:  # 如果信息增益>0;
                bestInfoGain = infoGain  # 用当前信息增益值替代之前的最优增益值
                bestFeature = i  # 重置最优特征为当前列
        return bestFeature

    def computeEntropy(self, dataSet):  # 计算香农熵
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]  # 从数据集中得到类别标签
        items = dict(
            [(i, cateList.count(i)) for i in cateList]
        )  # 得到类别为key，出现次数value的字典
        infoEntropy = 0.0  # 初始化香农熵
        for key in items:  # 计算香农熵
            prob = float(items[key]) / datalen
            infoEntropy -= prob * math.log(
                prob, 2
            )  # 香农熵：= - p*log2(p) --infoEntropy = -prob * log(prob,2)
        return infoEntropy

    # 分隔数据集：删除特征轴所在的数据列，返回剩余的数据集
    # dataSet：数据集;	 axis：特征轴;	 value：特征轴的取值
    def splitDataSet(self, dataSet, axis, value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]  # list操作 提取0~(axis-1)的元素
                rFeatVec.extend(featVec[axis + 1 :])  # list操作 将特征轴（列）之后的元素加回
                rtnList.append(rFeatVec)
        return rtnList

    def predict(self, inputTree, featLabels, testVec):  # 分类器
        root = inputTree.keys()[0]  # 树根节点
        secondDict = inputTree[root]  # value-子树结构或分类标签
        featIndex = featLabels.index(root)  # 根节点在分类标签集中的位置
        key = testVec[featIndex]  # 测试集数组取值
        valueOfFeat = secondDict[key]  #
        if isinstance(valueOfFeat, dict):
            classLabel = self.predict(valueOfFeat, featLabels, testVec)  # 递归分类
        else:
            classLabel = valueOfFeat
        return classLabel

    # 存储树到文件
    def storeTree(self, inputTree, filename):
        fw = open(filename, "w")
        pickle.dump(inputTree, fw)
        fw.close()

    # 从文件抓取树
    def grabTree(self, filename):
        fr = open(filename)
        return pickle.load(fr)


print("------------------------------")  # 60個

# classify02.py

from numpy import *
from math import log
import copy

dtree = ID3DTree()
dtree.loadDataSet("dataset.dat", ["age", "revenue", "student", "credit"])
# dtree.loadDataSet("data/lenses.txt",['age','prescript','astigmatic','tearRate'])
dtree.train()
print(dtree.tree)
createPlot(dtree.tree)

print("------------------------------------------------------------")  # 60個
print("------------------------------")  # 60個

# classify03.py

from numpy import *
from math import log
import copy

dtree = ID3DTree()
dtree.loadDataSet("tmp_dataset.dat", ["age", "revenue", "student", "credit"])
dtree.train()

dtree.storeTree(dtree.tree, "tmp_data.tree")

mytree = dtree.grabTree("tmp_data.tree")
print(mytree)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# classify04.py

from numpy import *
from math import log
import copy

dtree = ID3DTree()

labels = ["age", "revenue", "student", "credit"]
vector = ["0", "1", "0", "0"]  # ['0','1','0','0','no']

mytree = dtree.grabTree("tmp_data.tree")
print("真实输出 ", "no", "->", "决策树输出", dtree.predict(mytree, labels, vector))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# C45DTree.py

from numpy import *
import copy
import pickle


class C45DTree(object):
    def __init__(self):
        self.tree = {}
        self.dataSet = []
        self.labels = []

    def loadDataSet(self, path, labels):
        recordlist = []
        fp = open(path, "rb")
        content = fp.read()
        fp.close()
        rowlist = content.splitlines()
        recordlist = [row.split("\t") for row in rowlist if row.strip()]
        self.dataSet = recordlist
        self.labels = labels

    def train(self):
        labels = copy.deepcopy(self.labels)
        self.tree = self.buildTree(self.dataSet, labels)

    def buildTree(self, dataSet, labels):
        cateList = [data[-1] for data in dataSet]
        if cateList.count(cateList[0]) == len(cateList):
            return cateList[0]
        if len(dataSet[0]) == 1:
            return self.maxCate(cateList)
        bestFeat, featValueList = self.getBestFeat(dataSet)
        bestFeatLabel = labels[bestFeat]
        tree = {bestFeatLabel: {}}
        del labels[bestFeat]
        for value in featValueList:
            subLabels = labels[:]
            splitDataset = self.splitDataSet(dataSet, bestFeat, value)
            subTree = self.buildTree(splitDataset, subLabels)
            tree[bestFeatLabel][value] = subTree
        return tree

    def maxCate(self, catelist):
        items = dict([(catelist.count(i), i) for i in catelist])
        return items[max(items.keys())]

    def getBestFeat(self, dataSet):
        Num_Feats = len(dataSet[0][:-1])
        totality = len(dataSet)
        BaseEntropy = self.computeEntropy(dataSet)
        ConditionEntropy = []  # 初始化条件熵
        slpitInfo = []  # for C4.5, calculate gain ratio
        allFeatVList = []
        for f in range(Num_Feats):
            featList = [example[f] for example in dataSet]
            [splitI, featureValueList] = self.computeSplitInfo(featList)
            allFeatVList.append(featureValueList)
            slpitInfo.append(splitI)
            resultGain = 0.0
            for value in featureValueList:
                subSet = self.splitDataSet(dataSet, f, value)
                appearNum = float(len(subSet))
                subEntropy = self.computeEntropy(subSet)
                resultGain += (appearNum / totality) * subEntropy
            ConditionEntropy.append(resultGain)  # 总条件熵
        infoGainArray = BaseEntropy * ones(Num_Feats) - array(ConditionEntropy)
        infoGainRatio = infoGainArray / array(slpitInfo)  # c4.5, info gain ratio
        bestFeatureIndex = argsort(-infoGainRatio)[0]
        return bestFeatureIndex, allFeatVList[bestFeatureIndex]

    def computeSplitInfo(self, featureVList):
        numEntries = len(featureVList)
        featureVauleSetList = list(set(featureVList))
        valueCounts = [featureVList.count(featVec) for featVec in featureVauleSetList]
        # caclulate shannonEnt
        pList = [float(item) / numEntries for item in valueCounts]
        lList = [item * math.log(item, 2) for item in pList]
        splitInfo = -sum(lList)
        return splitInfo, featureVauleSetList

    def computeEntropy(self, dataSet):
        datalen = float(len(dataSet))
        cateList = [data[-1] for data in dataSet]
        items = dict([(i, cateList.count(i)) for i in cateList])
        infoEntropy = 0.0
        for key in items:
            prob = float(items[key]) / datalen
            infoEntropy -= prob * math.log(prob, 2)
        return infoEntropy

    def splitDataSet(self, dataSet, axis, value):
        rtnList = []
        for featVec in dataSet:
            if featVec[axis] == value:
                rFeatVec = featVec[:axis]
                rFeatVec.extend(featVec[axis + 1 :])
                rtnList.append(rFeatVec)
        return rtnList

    # 树的后剪枝


# testData: 测试集
def prune(tree, testData):
    pass

    def predict(self, inputTree, featLabels, testVec):
        root = inputTree.keys()[0]
        secondDict = inputTree[root]
        featIndex = featLabels.index(root)
        key = testVec[featIndex]
        valueOfFeat = secondDict[key]  #
        if isinstance(valueOfFeat, dict):
            classLabel = self.predict(valueOfFeat, featLabels, testVec)
        else:
            classLabel = valueOfFeat
        return classLabel

    def storeTree(self, inputTree, filename):
        fw = open(filename, "w")
        pickle.dump(inputTree, fw)
        fw.close()

    def grabTree(self, filename):
        fr = open(filename)
        return pickle.load(fr)


print("------------------------------")  # 30個

# classify05.py

from numpy import *
from math import log

dtree = C45DTree()
dtree.loadDataSet("tmp_dataset.dat", ["age", "revenue", "student", "credit"])
dtree.train()
print(dtree.tree)
createPlot(dtree.tree)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# classify06.py

from numpy import *
from math import log

dtree = C45DTree()
labels = ["age", "revenue", "student", "credit"]

dtree.loadDataSet("tmp_dataset.dat", labels)
dtree.decisionTree()
vector = ["0", "1", "0", "0"]  # ['0','1','0','0','no']
print("真实输出 ", "no", "->", "决策树输出", dtree.predict(dtree.tree, labels, vector))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# classify07.py

from numpy import *
from sklearn.tree import DecisionTreeRegressor


# Create a random dataset
def plotfigure(X, X_test, y, yp):
    plt.figure()
    plt.scatter(X, y, c="k", label="data")
    plt.plot(X_test, yp, c="r", label="max_depth=5", linewidth=2)
    plt.xlabel("data")
    plt.ylabel("target")
    plt.title("Decision Tree Regression")
    plt.legend()
    show()


x = np.linspace(-5, 5, 200)
siny = np.sin(x)  # 给出y与x的基本关系
X = mat(x).T
y = siny + np.random.rand(1, len(siny)) * 1.5  # 加入噪声的点集
y = y.tolist()[0]
# Fit regression model
clf = DecisionTreeRegressor(max_depth=4)

clf.fit(X, y)

# Predict
X_test = np.arange(-5.0, 5.0, 0.05)[:, np.newaxis]
yp = clf.predict(X_test)

plotfigure(X, X_test, y, yp)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# test1.py

from numpy import *


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
Ip1p2 = -P1 * log2(P1) - P2 * log2(P2)
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
Ip1p2 = -P1 * log2(P1) - P2 * log2(P2)
print(Ip1p2)
print(0.9544 - 0.6877)

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

print("------------------------------")  # 60個
