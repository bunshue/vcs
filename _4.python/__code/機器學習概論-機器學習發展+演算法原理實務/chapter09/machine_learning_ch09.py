"""
machine_learning_ch09

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

# eigencog_face.py

from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")
"""NG
ef.compute()
E = []
X = np.mat(np.zeros((10, 10304)))
for i in range(16):
    X = ef.Mat[i * 10 : (i + 1) * 10, :].copy()
    # X = ef.normalize(X.mean(axis =0),0,255)
    X = X.mean(axis=0)
    imgs = X.reshape(112, 92)
    E.append(imgs)
ef.subplot(title="AT&T Eigen Facedatabase", images=E)
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# eigencog_test.py

from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")
""" NG
ef.compute()
# 创建测试集
testImg = ef.X[30]
print("实际值 =", ef.y[30], "->", "预测值 =", ef.predict(testImg))
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Adaboost is short for Adaptive Boosting

import copy


def loadDataSet(fileName):
    recordlist = []
    print(fileName)
    fp = open(fileName, "r")
    # fp = open(fileName, "rb")
    content = fp.read()
    fp.close()
    rowlist = content.splitlines()
    recordlist = [map(eval, row.split("\t")) for row in rowlist if row.strip()]
    dataSet = np.mat(recordlist)[:, :-1]
    labels = np.mat(recordlist)[:, -1].T
    return dataSet, labels


# dataMat:数据集,
# Column: 第几列
# threshVal:阈值
# threshSymb:分类分隔符,lt,gt符号
def splitDataSet(dataMat, Column, threshVal, operator):
    retArray = np.ones((np.shape(dataMat)[0], 1))  # 与数据集行数相同的全1向量
    if operator == "lt":  # '小于'
        retArray[dataMat[:, Column] <= threshVal] = -1.0
    else:  # '大于'
        retArray[dataMat[:, Column] > threshVal] = -1.0
    return retArray  # 预测结果


# 单层决策树生成函数: 以最小误差作为衡量标准找到最优列,不等于符号(大于,小于),阈值和重估的分类标签
# dataSet: 数据集
# labellist: 类别标签
# D: 列向量每个元素的平均权重:1/总元素数
def decisionTree(dataSet, labellist, D):
    dataMat = np.mat(dataSet)
    labelMat = np.mat(labellist).T
    m, n = np.shape(dataMat)  # 数据集行、列数
    numSteps = 10.0
    # 迭代步数
    bestFeat = {}
    # 最优项列
    bestClass = np.mat(np.zeros((m, 1)))  # 最优预测分类
    minError = np.inf  # 初始化最小误差为无穷大
    for i in range(n):  # 按列迭代
        rangeMin = dataMat[:, i].min()
        # 最小值
        rangeMax = dataMat[:, i].max()
        # 最大值
        print("rangeMax :", rangeMax)
        print("rangeMin :", rangeMin)
        print("numSteps :", numSteps)  # 10.0
        stepSize = (rangeMax - rangeMin) / numSteps  # 步长 = (最大值-最小值)/步长数
        for j in range(-1, int(numSteps) + 1):  # 对每个步长数迭代: -1~(numSteps)
            threshVal = rangeMin + float(j) * stepSize  # 计算域值:(最小值+迭代步数*步长数)
            for operator in ["lt", "gt"]:  # operator 操作符，取值为两个: lt小于,gt大于--分类分隔符
                # 调用 splitDataSet方法,小于,大于
                predictedVals = splitDataSet(dataMat, i, threshVal, operator)
                errSet = np.mat(np.ones((m, 1)))  # 初始化误差集为一个全1向量
                errSet[predictedVals == labelMat] = 0  # 误差集：列向量的预测值 == 类别标签则赋值为0
                weightedError = D.T * errSet  # 权重误差 = D*误差数组:权重误差是个标量
                if weightedError < minError:
                    minError = weightedError  # 更新最小误差为权重误差
                    bestClass = predictedVals.copy()  # 最优预测类
                    bestFeat["dim"] = i  # 最优列
                    bestFeat["thresh"] = threshVal  # 最优阈值
                    bestFeat["oper"] = operator  # 最优分隔符号(大于或小于号)
    return bestFeat, minError, bestClass


# 基于单层分类器的ADABOOST训练过程
# 通过修改D的值调整弱分类器的权重
# dataSet:数据集
# labellist:分类标签
# numIt:迭代次数
def adaBoostTrain(dataSet, labellist, numIt=40):
    weakClassSet = []  # 初始化弱分类器
    m = np.shape(dataSet)[0]
    D = np.mat(np.ones((m, 1)) / m)  # 初始化D为平均权重
    aggClassSet = np.mat(np.zeros((m, 1)))
    for i in range(numIt):
        bestFeat, error, EstClass = decisionTree(dataSet, labellist, D)
        alpha = float(
            0.5 * log((1.0 - error) / max(error, 1e-16))
        )  # alpha计算公式，1e-16避免除0
        bestFeat["alpha"] = alpha
        weakClassSet.append(bestFeat)  # 以数组形式存储弱分类器
        # 算法核心：D--权重修改公式：D*exp((+-)alpha)/sum(D)（Logistic）
        # +-号取决于是否错分，+正确划分，-错误划分
        wtx = np.multiply(
            -1 * alpha * np.mat(labellist).T, EstClass
        )  # 矩阵对应元素相乘:multiply矩阵点积
        D = np.multiply(D, exp(wtx))  # 为下次迭代计算新的D
        D = D / D.sum()
        aggClassSet += alpha * EstClass  # 累计预测类：
        # 如果 x>0 sign(x)=1; x<0 sign(x)=-1
        # 计算所有分类器的训练误差--累计误差
        totalErr = multiply(sign(aggClassSet) != np.mat(labellist).T, np.ones((m, 1)))
        errorRate = totalErr.sum() / m  # 计算总误差率
        if errorRate == 0.0:
            break  # 如果为0，分类完毕 跳出循环
    return weakClassSet, aggClassSet


# Ada分类器
def adaClassify(datToClass, classdictList):
    dataMat = np.mat(
        datToClass
    )  # do stuff similar to last aggClassSet in adaBoostTrainDS
    m = np.shape(dataMat)[0]
    aggClassSet = np.mat(np.zeros((m, 1)))
    for i in range(len(classdictList)):
        EstClass = splitDataSet(
            dataMat,
            classdictList[i]["dim"],
            classdictList[i]["thresh"],
            classdictList[i]["oper"],
        )
        aggClassSet += classdictList[i]["alpha"] * EstClass
    return sign(aggClassSet)


def plotROC(predStrengths, labellist):
    cur = (1.0, 1.0)  # cursor
    ySum = 0.0  # variable to calculate AUC
    numPosClas = sum(np.array(labellist) == 1.0)
    yStep = 1 / float(numPosClas)
    xStep = 1 / float(len(labellist) - numPosClas)
    sortedIndicies = predStrengths.argsort()  # get sorted index, it's reverse
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    # loop through all the values, drawing a line segment at each point
    for index in sortedIndicies.tolist()[0]:
        if labellist[index] == 1.0:
            delX = 0
            delY = yStep
        else:
            delX = xStep
            delY = 0
            ySum += cur[1]
        ax.plot([cur[0], cur[0] - delX], [cur[1], cur[1] - delY], c="b")
        cur = (cur[0] - delX, cur[1] - delY)
    ax.plot([0, 1], [0, 1], "b--")
    plt.xlabel("False positive rate")
    plt.ylabel("True positive rate")
    plt.title("ROC curve for AdaBoost horse colic detection system")
    ax.axis([0, 1, 0, 1])
    show()
    print("the Area Under the Curve is: ", ySum * xStep)


# adaboost_traincase
# testAdaboost2.py

# 导入训练集
dataArr, labelArr = loadDataSet("train.dat")

print("dataArr")
print(dataArr)

print("labelArr")
print(labelArr)

weakClassArr, aggClassEst = adaBoostTrain(dataArr, labelArr, numIt=10)  # 训练分类器
print("weakClassArr:", weakClassArr)  # 输出弱分类器
# plotROC(aggClassEst.T, labelArr) # 绘制ROC曲线

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# adaboost_traincase.py

# 导入训练集
dataArr, labelArr = loadDataSet("train.dat")

weakClassArr, aggClassEst = adaBoostTrain(dataArr, labelArr, numIt=10)  # 训练分类器
print("weakClassArr:", weakClassArr)  # 输出弱分类器
# plotROC(aggClassEst.T, labelArr) # 绘制ROC曲线

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testcase.py

# 导入训练集
dataArr, labelArr = loadDataSet("horseColicTraining.txt")
# 训练分类器
weakClassArr, aggClassEst = adaBoostTrain(dataArr, labelArr, numIt=10)
print("weakClassArr:", weakClassArr)
# print "aggClassEst:",aggClassEst
# 绘制ROC曲线
plotROC(aggClassEst.T, labelArr)

# 导入测试集
testArr, testLabelArr = loadDataSet("horseColicTest.txt")
ClassEst100 = adaClassify(testArr, weakClassArr)  # 用学习好的分类器进行分类
errArr = np.mat(np.ones((67, 1)))
totalError = errArr[ClassEst100 != np.mat(testLabelArr).T].sum()
print("totalError:", totalError)


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
