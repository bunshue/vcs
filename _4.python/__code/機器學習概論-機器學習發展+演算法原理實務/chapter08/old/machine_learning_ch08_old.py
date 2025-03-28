"""
machine_learning_ch08_old

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
from time import sleep


def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i, m):
    j = i  # we want to select any J not equal to i
    while j == i:
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    iter = 0
    while iter < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            fXi = (
                float(multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[i, :].T))
                + b
            )
            Ei = fXi - float(
                labelMat[i]
            )  # if checks if an example violates KKT conditions
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C)) or (
                (labelMat[i] * Ei > toler) and (alphas[i] > 0)
            ):
                j = selectJrand(i, m)
                fXj = (
                    float(
                        multiply(alphas, labelMat).T * (dataMatrix * dataMatrix[j, :].T)
                    )
                    + b
                )
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if labelMat[i] != labelMat[j]:
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L == H:
                    print("L==H")
                    continue
                eta = (
                    2.0 * dataMatrix[i, :] * dataMatrix[j, :].T
                    - dataMatrix[i, :] * dataMatrix[i, :].T
                    - dataMatrix[j, :] * dataMatrix[j, :].T
                )
                if eta >= 0:
                    print("eta>=0")
                    continue
                alphas[j] -= labelMat[j] * (Ei - Ej) / eta
                alphas[j] = clipAlpha(alphas[j], H, L)
                if abs(alphas[j] - alphaJold) < 0.00001:
                    print("j not moving enough")
                    continue
                alphas[i] += (
                    labelMat[j] * labelMat[i] * (alphaJold - alphas[j])
                )  # update i by the same amount as j
                # the update is in the oppostie direction
                b1 = (
                    b
                    - Ei
                    - labelMat[i]
                    * (alphas[i] - alphaIold)
                    * dataMatrix[i, :]
                    * dataMatrix[i, :].T
                    - labelMat[j]
                    * (alphas[j] - alphaJold)
                    * dataMatrix[i, :]
                    * dataMatrix[j, :].T
                )
                b2 = (
                    b
                    - Ej
                    - labelMat[i]
                    * (alphas[i] - alphaIold)
                    * dataMatrix[i, :]
                    * dataMatrix[j, :].T
                    - labelMat[j]
                    * (alphas[j] - alphaJold)
                    * dataMatrix[j, :]
                    * dataMatrix[j, :].T
                )
                if (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1 + b2) / 2.0
                alphaPairsChanged += 1
                print("iter: %d i:%d, pairs changed %d" % (iter, i, alphaPairsChanged))
        if alphaPairsChanged == 0:
            iter += 1
        else:
            iter = 0
        # print("iteration number: %d" % iter)
    return b, alphas


def kernelTrans(
    X, A, kTup
):  # calc the kernel or transform data to a higher dimensional space
    m, n = shape(X)
    K = mat(zeros((m, 1)))
    if kTup[0] == "lin":
        K = X * A.T  # linear kernel
    elif kTup[0] == "rbf":
        for j in range(m):
            deltaRow = X[j, :] - A
            K[j] = deltaRow * deltaRow.T
        K = exp(
            K / (-1 * kTup[1] ** 2)
        )  # divide in NumPy is element-wise not matrix like Matlab
    else:
        raise NameError("Houston We Have a Problem -- That Kernel is not recognized")
    return K


class optStruct:
    def __init__(
        self, dataMatIn, classLabels, C, toler, kTup
    ):  # Initialize the structure with the parameters
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))  # first column is valid flag
        self.K = mat(zeros((self.m, self.m)))
        for i in range(self.m):
            self.K[:, i] = kernelTrans(self.X, self.X[i, :], kTup)


def calcEk(oS, k):
    fXk = float(multiply(oS.alphas, oS.labelMat).T * oS.K[:, k] + oS.b)
    Ek = fXk - float(oS.labelMat[k])
    return Ek


def selectJ(i, oS, Ei):  # this is the second choice -heurstic, and calcs Ej
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCache[i] = [1, Ei]  # set valid #choose the alpha that gives the maximum delta E
    validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
    if (len(validEcacheList)) > 1:
        for (
            k
        ) in (
            validEcacheList
        ):  # loop through valid Ecache values and find the one that maximizes delta E
            if k == i:
                continue  # don't calc for i, waste of time
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if deltaE > maxDeltaE:
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:  # in this case (first time around) we don't have any valid eCache values
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej


def updateEk(oS, k):  # after any alpha has changed update the new value in the cache
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


def innerL(i, oS):
    Ei = calcEk(oS, i)
    if ((oS.labelMat[i] * Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or (
        (oS.labelMat[i] * Ei > oS.tol) and (oS.alphas[i] > 0)
    ):
        j, Ej = selectJ(i, oS, Ei)  # this has been changed from selectJrand
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if oS.labelMat[i] != oS.labelMat[j]:
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if L == H:
            print("L==H")
            return 0
        eta = 2.0 * oS.K[i, j] - oS.K[i, i] - oS.K[j, j]  # changed for kernel
        if eta >= 0:
            print("eta>=0")
            return 0
        oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        updateEk(oS, j)  # added this for the Ecache
        if abs(oS.alphas[j] - alphaJold) < 0.00001:
            print("j not moving enough")
            return 0
        oS.alphas[i] += (
            oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
        )  # update i by the same amount as j
        updateEk(
            oS, i
        )  # added this for the Ecache                    #the update is in the oppostie direction
        b1 = (
            oS.b
            - Ei
            - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, i]
            - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.K[i, j]
        )
        b2 = (
            oS.b
            - Ej
            - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.K[i, j]
            - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.K[j, j]
        )
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0
        return 1
    else:
        return 0


def smoP(dataMatIn, classLabels, C, toler, maxIter, kTup=("lin", 0)):  # full Platt SMO
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler, kTup)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:  # go over all
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
                print(
                    "fullSet, iter: %d i:%d, pairs changed %d"
                    % (iter, i, alphaPairsChanged)
                )
            iter += 1
        else:  # go over non-bound (railed) alphas
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                print(
                    "non-bound, iter: %d i:%d, pairs changed %d"
                    % (iter, i, alphaPairsChanged)
                )
            iter += 1
        if entireSet:
            entireSet = False  # toggle entire set loop
        elif alphaPairsChanged == 0:
            entireSet = True
        print("iteration number: %d" % iter)
    return oS.b, oS.alphas


def calcWs(alphas, dataArr, classLabels):
    X = mat(dataArr)
    labelMat = mat(classLabels).transpose()
    m, n = shape(X)
    w = zeros((n, 1))
    for i in range(m):
        w += multiply(alphas[i] * labelMat[i], X[i, :].T)
    return w


def testRbf(k1=1.3):
    dataArr, labelArr = loadDataSet("testSetRBF.txt")
    b, alphas = smoP(
        dataArr, labelArr, 200, 0.0001, 10000, ("rbf", k1)
    )  # C=200 important
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]  # get matrix of only support vectors
    labelSV = labelMat[svInd]
    print("there are %d Support Vectors" % shape(sVs)[0])
    m, n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], ("rbf", k1))
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the training error rate is: %f" % (float(errorCount) / m))
    dataArr, labelArr = loadDataSet("testSetRBF2.txt")
    errorCount = 0
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    m, n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], ("rbf", k1))
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the test error rate is: %f" % (float(errorCount) / m))


def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def loadImages(dirName):
    from os import listdir

    hwLabels = []
    trainingFileList = listdir(dirName)  # load the training set
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split(".")[0]  # take off .txt
        classNumStr = int(fileStr.split("_")[0])
        if classNumStr == 9:
            hwLabels.append(-1)
        else:
            hwLabels.append(1)
        trainingMat[i, :] = img2vector("%s/%s" % (dirName, fileNameStr))
    return trainingMat, hwLabels


def testDigits(kTup=("rbf", 10)):
    dataArr, labelArr = loadImages("trainingDigits")
    b, alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, kTup)
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print("there are %d Support Vectors" % shape(sVs)[0])
    m, n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the training error rate is: %f" % (float(errorCount) / m))
    dataArr, labelArr = loadImages("testDigits")
    errorCount = 0
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    m, n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTup)
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the test error rate is: %f" % (float(errorCount) / m))


"""#######********************************
Non-Kernel VErsions below
"""  #######********************************


class optStructK:
    def __init__(
        self, dataMatIn, classLabels, C, toler
    ):  # Initialize the structure with the parameters
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        self.eCache = mat(zeros((self.m, 2)))  # first column is valid flag


def calcEkK(oS, k):
    fXk = float(multiply(oS.alphas, oS.labelMat).T * (oS.X * oS.X[k, :].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek


def selectJK(i, oS, Ei):  # this is the second choice -heurstic, and calcs Ej
    maxK = -1
    maxDeltaE = 0
    Ej = 0
    oS.eCache[i] = [1, Ei]  # set valid #choose the alpha that gives the maximum delta E
    validEcacheList = nonzero(oS.eCache[:, 0].A)[0]
    if (len(validEcacheList)) > 1:
        for (
            k
        ) in (
            validEcacheList
        ):  # loop through valid Ecache values and find the one that maximizes delta E
            if k == i:
                continue  # don't calc for i, waste of time
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if deltaE > maxDeltaE:
                maxK = k
                maxDeltaE = deltaE
                Ej = Ek
        return maxK, Ej
    else:  # in this case (first time around) we don't have any valid eCache values
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej


def updateEkK(oS, k):  # after any alpha has changed update the new value in the cache
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1, Ek]


def innerLK(i, oS):
    Ei = calcEk(oS, i)
    if ((oS.labelMat[i] * Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or (
        (oS.labelMat[i] * Ei > oS.tol) and (oS.alphas[i] > 0)
    ):
        j, Ej = selectJ(i, oS, Ei)  # this has been changed from selectJrand
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if oS.labelMat[i] != oS.labelMat[j]:
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if L == H:
            print("L==H")
            return 0
        eta = (
            2.0 * oS.X[i, :] * oS.X[j, :].T
            - oS.X[i, :] * oS.X[i, :].T
            - oS.X[j, :] * oS.X[j, :].T
        )
        if eta >= 0:
            print("eta>=0")
            return 0
        oS.alphas[j] -= oS.labelMat[j] * (Ei - Ej) / eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        updateEk(oS, j)  # added this for the Ecache
        if abs(oS.alphas[j] - alphaJold) < 0.00001:
            print("j not moving enough")
            return 0
        oS.alphas[i] += (
            oS.labelMat[j] * oS.labelMat[i] * (alphaJold - oS.alphas[j])
        )  # update i by the same amount as j
        updateEk(
            oS, i
        )  # added this for the Ecache                    #the update is in the oppostie direction
        b1 = (
            oS.b
            - Ei
            - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[i, :].T
            - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[i, :] * oS.X[j, :].T
        )
        b2 = (
            oS.b
            - Ej
            - oS.labelMat[i] * (oS.alphas[i] - alphaIold) * oS.X[i, :] * oS.X[j, :].T
            - oS.labelMat[j] * (oS.alphas[j] - alphaJold) * oS.X[j, :] * oS.X[j, :].T
        )
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]):
            oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]):
            oS.b = b2
        else:
            oS.b = (b1 + b2) / 2.0
        return 1
    else:
        return 0


def smoPK(dataMatIn, classLabels, C, toler, maxIter):  # full Platt SMO
    oS = optStruct(mat(dataMatIn), mat(classLabels).transpose(), C, toler)
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iter < maxIter) and ((alphaPairsChanged > 0) or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:  # go over all
            for i in range(oS.m):
                alphaPairsChanged += innerL(i, oS)
                print(
                    "fullSet, iter: %d i:%d, pairs changed %d"
                    % (iter, i, alphaPairsChanged)
                )
            iter += 1
        else:  # go over non-bound (railed) alphas
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i, oS)
                print(
                    "non-bound, iter: %d i:%d, pairs changed %d"
                    % (iter, i, alphaPairsChanged)
                )
            iter += 1
        if entireSet:
            entireSet = False  # toggle entire set loop
        elif alphaPairsChanged == 0:
            entireSet = True
        print("iteration number: %d" % iter)
    return oS.b, oS.alphas


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 02PlattSMO.py

from numpy import *
import operator

dataArr, labelArr = loadDataSet("nolinear.txt")
# print labelArr
# 主 platt smo 函数
# 数据集:dataArr
# 类别标签:labelArr,
# 错分类系数C: 0.6,
# 容错率:0.001
# 迭代次数: 40
b, alphas = smoP(dataArr, labelArr, 0.6, 0.001, 200)
# 根据拉格朗日alphas乘子计算W向量
ws = calcWs(alphas, dataArr, labelArr)

print("b:", b)
print("alphas[alphas > 0]:", alphas[alphas > 0])

# 绘制散点图
mydata = mat(dataArr)
# 数据描点
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(mydata)):
    if alphas[i] != 0:  # KKT条件
        ax.scatter(mydata[i, 0], mydata[i, 1], c="green", marker="s")
    elif labelArr[i] == 1:
        ax.scatter(mydata[i, 0], mydata[i, 1], c="blue", marker="o")
    elif labelArr[i] == -1:
        ax.scatter(mydata[i, 0], mydata[i, 1], c="red", marker="o")
# 显示绘制的图形
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03svmRbf.py

from numpy import *
import operator

k1 = 1.3
# 加载训练集
dataArr, labelArr = loadDataSet("testSetRBF.txt")
# 使用Platt SMO分类
# 使用rbf非线性核函数
b, alphas = smoP(
    dataArr, labelArr, 200, 0.0001, 10000, ("rbf", k1)
)  # C=200 important
datMat = mat(dataArr)
labelMat = mat(labelArr).T
svInd = nonzero(alphas.A > 0)[0]
# 获取支持向量
sVs = datMat[svInd]  # get matrix of only support vectors
labelSV = labelMat[svInd]
# 输出支持向量的数量
print("there are %d Support Vectors" % shape(sVs)[0])
print(svInd)
m, n = shape(datMat)
errorCount = 0
# 计算训练错误率
for i in range(m):
    kernelEval = kernelTrans(sVs, datMat[i, :], ("rbf", k1))
    predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
    if sign(predict) != sign(labelArr[i]):
        errorCount += 1
print("the training error rate is: %f" % (float(errorCount) / m))

# 输出非线性分类图
mydata = mat(dataArr)
# 数据描点
fig = plt.figure()
ax = fig.add_subplot(111)
for i in range(len(mydata)):
    if alphas[i] != 0:  # KKT条件
        ax.scatter(mydata[i, 0], mydata[i, 1], c="green", marker="s")
    elif labelArr[i] == 1:
        ax.scatter(mydata[i, 0], mydata[i, 1], c="blue", marker="o")
    elif labelArr[i] == -1:
        ax.scatter(mydata[i, 0], mydata[i, 1], c="red", marker="o")
# 显示绘制的图形
plt.show()
# 加载测试集
dataArr, labelArr = loadDataSet("testSetRBF2.txt")
errorCount = 0
datMat = mat(dataArr)
labelMat = mat(labelArr).T
m, n = shape(datMat)
# 用核函数划分测试集
for i in range(m):
    kernelEval = kernelTrans(sVs, datMat[i, :], ("rbf", k1))
    predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
    if sign(predict) != sign(labelArr[i]):
        errorCount += 1
# 输出误差分类结果
print("the test error rate is: %f" % (float(errorCount) / m))

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
