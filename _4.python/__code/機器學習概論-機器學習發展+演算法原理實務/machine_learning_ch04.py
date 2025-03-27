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

# Recommand_Lib.py

from numpy import *
import operator
import scipy.spatial.distance as dist


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


# 随机生成聚类中心
def randCenters(dataSet, k):
    n = shape(dataSet)[1]
    clustercents = mat(zeros((k, n)))  # 初始化聚类中心矩阵:k*n
    for col in range(n):
        mincol = min(dataSet[:, col])
        maxcol = max(dataSet[:, col])
        # random.rand(k,1): 产生一个0~1之间的随机数向量：k,1表示产生k行1列的随机数
        clustercents[:, col] = mat(mincol + float(maxcol - mincol) * random.rand(k, 1))
    return clustercents


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
    plt.scatter(mydata.T[0], mydata.T[1], s=size, c=color, marker=mrkr)


# 根据聚类范围绘制散点图
def color_cluster(dataindx, dataSet, plt, k=4):
    index = 0
    datalen = len(dataindx)
    for indx in range(datalen):
        if int(dataindx[indx]) == 0:
            plt.scatter(dataSet[index, 0], dataSet[index, 1], c="blue", marker="o")
        elif int(dataindx[indx]) == 1:
            plt.scatter(dataSet[index, 0], dataSet[index, 1], c="green", marker="o")
        elif int(dataindx[indx]) == 2:
            plt.scatter(dataSet[index, 0], dataSet[index, 1], c="red", marker="o")
        elif int(dataindx[indx]) == 3:
            plt.scatter(dataSet[index, 0], dataSet[index, 1], c="cyan", marker="o")
        index += 1


# KMeans 主函数
def kMeans(dataSet, k, distMeas=distEclud, createCent=randCenters):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            distlist = [distMeas(centroids[j, :], dataSet[i, :]) for j in range(k)]
            minDist = min(distlist)
            minIndex = distlist.index(minDist)
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        for cent in range(k):  # recalculate centroids
            ptsInClust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssment


def biKmeans(dataSet, k, distMeas=distEclud):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]  # create a list with one centroid
    for j in range(m):  # calc initial Error
        clusterAssment[j, 1] = distMeas(mat(centroid0), dataSet[j, :]) ** 2
    while len(centList) < k:
        lowestSSE = inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[
                nonzero(clusterAssment[:, 0].A == i)[0], :
            ]  # get the data points currently in cluster i
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = sum(
                splitClustAss[:, 1]
            )  # compare the SSE to the currrent minimum
            sseNotSplit = sum(
                clusterAssment[nonzero(clusterAssment[:, 0].A != i)[0], 1]
            )
            print("sseSplit, and notSplit: ", sseSplit, sseNotSplit)
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(
            centList
        )  # change 1 to 3,4, or whatever
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
        print("the bestCentToSplit is: ", bestCentToSplit)
        print("the len of bestClustAss is: ", len(bestClustAss))
        centList[bestCentToSplit] = bestNewCents[0, :].tolist()[
            0
        ]  # replace a centroid with two best centroids
        centList.append(bestNewCents[1, :].tolist()[0])
        clusterAssment[
            nonzero(clusterAssment[:, 0].A == bestCentToSplit)[0], :
        ] = bestClustAss  # reassign new clusters, and SSE
    return mat(centList), clusterAssment


# dataSet 训练集
# testVect 测试集
# r=3 取前r个近似值
# rank=1,结果排序
# distCalc 相似度计算函数
def recommand(dataSet, testVect, r=3, rank=1, distCalc=cosSim):
    m, n = shape(dataSet)
    limit = min(m, n)
    if r > limit:
        r = limit
    U, S, VT = linalg.svd(dataSet.T)  # svd分解
    V = VT.T
    Ur = U[:, :r]  # 取前r个U,S,V值
    Sr = diag(S)[:r, :r]
    Vr = V[:, :r]
    testresult = testVect * Ur * linalg.inv(Sr)  # 计算User E的坐标值
    # 计算测试集与训练集每个记录的相似度
    resultarray = array([distCalc(testresult, vi) for vi in Vr])
    descindx = argsort(-resultarray)[:rank]  # 排序结果--降序
    return descindx, resultarray[descindx]  # 排序后的索引和值


def my_kNN(testdata, trainSet, listClasses, k):
    dataSetSize = trainSet.shape[0]
    distances = array(zeros(dataSetSize))
    for indx in range(dataSetSize):
        distances[indx] = cosSim(testdata, trainSet[indx])
    sortedDistIndicies = argsort(-distances)
    classCount = {}
    for i in range(k):  # i = 0~(k-1)
        voteIlabel = listClasses[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(
        classCount.items(), key=operator.itemgetter(1), reverse=True
    )
    return sortedClassCount[0][0]


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# bikMeans_test.py

from numpy import *

# 从文件构建的数据集
dataMat = file2matrix("data04/4k2_far.txt", "\t")
dataSet = mat(dataMat[:, 1:])  # 转换为矩阵形式

k = 4  # 分类数
m = shape(dataSet)[0]
# 初始化第一个聚类中心: 每一列的均值
centroid0 = mean(dataSet, axis=0).tolist()[0]
centList = [centroid0]  # 把均值聚类中心加入中心表中
# 初始化聚类距离表,距离方差:
ClustDist = mat(zeros((m, 2)))
for j in range(m):
    ClustDist[j, 1] = distEclud(centroid0, dataSet[j, :]) ** 2

# 依次生成k个聚类中心
while len(centList) < k:
    lowestSSE = inf  # 初始化最小误差平方和。核心参数，这个值越小就说明聚类的效果越好。
    # 遍历cenList的每个向量
    # ----1. 使用ClustDist计算lowestSSE，以此确定:bestCentToSplit、bestNewCents、bestClustAss----#
    for i in range(len(centList)):
        ptsInCurrCluster = dataSet[nonzero(ClustDist[:, 0].A == i)[0], :]
        # 应用标准kMeans算法(k=2),将ptsInCurrCluster划分出两个聚类中心,以及对应的聚类距离表
        centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2)
        # 计算splitClustAss的距离平方和
        sseSplit = sum(splitClustAss[:, 1])
        # 计算ClustDist[ClustDist第1列!=i的距离平方和
        sseNotSplit = sum(ClustDist[nonzero(ClustDist[:, 0].A != i)[0], 1])
        if (
            sseSplit + sseNotSplit
        ) < lowestSSE:  # 算法公式: lowestSSE = sseSplit + sseNotSplit
            bestCentToSplit = i  # 确定聚类中心的最优分隔点
            bestNewCents = centroidMat  # 用新的聚类中心更新最优聚类中心
            bestClustAss = splitClustAss.copy()  # 深拷贝聚类距离表为最优聚类距离表
            lowestSSE = sseSplit + sseNotSplit  # 更新lowestSSE
    # 回到外循环
    # ----2. 计算新的ClustDist----#
    # 计算bestClustAss 分了两部分:
    # 第一部分为bestClustAss[bIndx0,0]赋值为聚类中心的索引
    bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
    # 第二部分 用最优分隔点的指定聚类中心索引
    bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentToSplit
    # 以上为计算bestClustAss
    # 更新ClustDist对应最优分隔点下标的距离，使距离值等于最优聚类距离对应的值
    # 以上为计算ClustDist

    # ----3. 用最优分隔点来重构聚类中心----#
    # 覆盖: bestNewCents[0,:].tolist()[0]附加到原有聚类中心的bestCentToSplit位置
    # 增加: 聚类中心增加一个新的bestNewCents[1,:].tolist()[0]向量
    centList[bestCentToSplit] = bestNewCents[0, :].tolist()[0]
    centList.append(bestNewCents[1, :].tolist()[0])
    ClustDist[nonzero(ClustDist[:, 0].A == bestCentToSplit)[0], :] = bestClustAss
    # 以上为计算centList
color_cluster(ClustDist[:, 0:1], dataSet, plt)
print("cenList:", mat(centList))
# print("ClustDist:", ClustDist)
# 绘制聚类中心图形
drawScatter(plt, mat(centList), size=60, color="red", mrkr="D")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# itemdf.py

from numpy import *

dataMat = mat(
    [
        [0.417, 0.0, 0.25, 0.333],
        [0.3, 0.4, 0.0, 0.3],
        [0.0, 0.0, 0.625, 0.375],
        [0.278, 0.222, 0.222, 0.278],
        [0.263, 0.211, 0.263, 0.263],
    ]
)
testSet = [0.334, 0.333, 0.0, 0.333]
classLabel = np.array(["B", "C", "D", "E", "F"])

print(my_kNN(testSet, dataMat, classLabel, 3))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# kMeans_test.py

from numpy import *
import operator

# 从文件构建的数据集
dataMat = file2matrix("data04/4k2_far.txt", "\t")
dataSet = mat(dataMat[:, 1:])  # 转换为矩阵形式
# dataSet = file2matrix("data04/testSet.txt","\t")

k = 4  # 外部指定1,2,3... 通过观察数据集有4个聚类中心
m = shape(dataSet)[0]  # 返回矩阵的行数

# 本算法核心数据结构:行数与数据集相同
# 列1：数据集对应的聚类中心,列2:数据集行向量到聚类中心的距离
ClustDist = mat(zeros((m, 2)))

# 随机生成一个数据集的聚类中心:本例为2*4的矩阵
# 确保该聚类中心位于min(dataMat[:,j]),max(dataMat[:,j])之间
clustercents = randCenters(dataSet, k)

flag = True  # 初始化标志位,迭代开始
counter = []
# 计数器

# 循环迭代直至终止条件为False
# 算法停止的条件：dataSet的所有向量都能找到某个聚类中心,到此中心的距离均小于其他k-1个中心的距离
while flag:
    flag = False  # 预置标志位为False

    # ---- 1. 构建ClustDist： 遍历DataSet数据集,计算DataSet每行与聚类的最小欧式距离 ----#
    #     将此结果赋值ClustDist=[minIndex,minDist]
    for i in range(m):
        # 遍历k个聚类中心,获取最短距离
        distlist = [distEclud(clustercents[j, :], dataSet[i, :]) for j in range(k)]
        minDist = min(distlist)
        minIndex = distlist.index(minDist)

        if ClustDist[i, 0] != minIndex:  # 找到了一个新聚类中心
            flag = True  # 重置标志位为True，继续迭代

        # 将minIndex和minDist**2赋予ClustDist第i行
        # 含义是数据集i行对应的聚类中心为minIndex,最短距离为minDist
        ClustDist[i, :] = minIndex, minDist

    # ---- 2.如果执行到此处，说明还有需要更新clustercents值: 循环变量为cent(0~k-1)----#
    # 1.用聚类中心cent切分为ClustDist，返回dataSet的行索引
    # 并以此从dataSet中提取对应的行向量构成新的ptsInClust
    # 计算分隔后ptsInClust各列的均值，以此更新聚类中心clustercents的各项值
    for cent in range(k):
        # 从ClustDist的第一列中筛选出等于cent值的行下标
        dInx = nonzero(ClustDist[:, 0].A == cent)[0]
        # 从dataSet中提取行下标==dInx构成一个新数据集
        ptsInClust = dataSet[dInx]
        # 计算ptsInClust各列的均值: mean(ptsInClust, axis=0):axis=0 按列计算
        clustercents[cent, :] = mean(ptsInClust, axis=0)

# 返回计算完成的聚类中心
print("clustercents:\n", clustercents)

# 输出生成的ClustDist：对应的聚类中心(列1),到聚类中心的距离(列2),行与dataSet一一对应
# print ClustDist[:,0:1]
color_cluster(ClustDist[:, 0:1], dataSet, plt)
# 绘制聚类中心
drawScatter(plt, clustercents, size=60, color="red", mrkr="D")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# scikit_kMeans.py

from sklearn.cluster import KMeans

k = 4
dataSet = file2matrix("data04/4k2_far.txt", "\t")
dataMat = mat(dataSet[:, 1:])  # 转换为矩阵形式

kmeans = KMeans(init="k-means++", n_clusters=4)
kmeans.fit(dataMat)

# 输出生成的ClustDist：对应的聚类中心(列1),到聚类中心的距离(列2),行与dataSet一一对应
drawScatter(plt, dataMat, size=20, color="b", mrkr=".")
# 绘制聚类中心
drawScatter(plt, kmeans.cluster_centers_, size=60, color="red", mrkr="D")
show()
"""
colors = ['r', 'b', 'g','black']
for k , col in zip( range(k) , colors):
    members = (kmeans.labels_ == k )
    pl.plot( dataMat[members, 0] , dataMat[members,1] , 'w', markerfacecolor=col, marker='.')
    pl.plot(kmeans.cluster_centers_[k,0], kmeans.cluster_centers_[k,1], 'o', markerfacecolor=col,\
            markeredgecolor='k', markersize=10)
pl.show()
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# svdRec.py

from numpy import *
from numpy import linalg as la


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
    return 1.0 / (1.0 + la.norm(inA - inB))


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
    denom = la.norm(inA) * la.norm(inB)
    return 0.5 + 0.5 * (num / denom)


# 标准相似度计算方法下的用户估计值
def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]  # 列数
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
    n = shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    # svd相似性计算的核心
    U, Sigma, VT = la.svd(dataMat)  # 计算矩阵的奇异值分解
    # Sig4 = mat(eye(4)*Sigma[:4]) # 取Svd特征值的前4个构成对角阵
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


# 输出矩阵
def printMat(inMat, thresh=0.8):
    for i in range(32):
        for k in range(32):
            if float(inMat[i, k]) > thresh:
                print(
                    1,
                )
            else:
                print(
                    0,
                )
        print("")


# 图片压缩
def imgCompress(numSV=3, thresh=0.8, flag=True):
    myl = []
    for line in open("0_5.txt").readlines():
        newRow = []
        for i in range(32):
            newRow.append(int(line[i]))
        myl.append(newRow)
    myMat = mat(myl)
    print("****original matrix******")
    printMat(myMat, thresh)
    U, Sigma, VT = la.svd(myMat)
    print("U 行列数:", shape(U)[0], ",", shape(U)[1])
    print("Sigma:", Sigma)
    print("VT 行列数:", shape(VT)[0], ",", shape(VT)[1])
    if flag:
        SigRecon = mat(zeros((numSV, numSV)))
        for k in range(numSV):  # construct diagonal matrix from vector
            SigRecon[k, k] = Sigma[k]
        reconMat = U[:, :numSV] * SigRecon * VT[:numSV, :]
        print("****reconstructed matrix using %d singular values******" % numSV)
        printMat(reconMat, thresh)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# svdtest01.py

# Filename : testRecomm01.py

from numpy import *
import operator

eps = 1.0e-6
# 加载修正后数据
A = mat(
    [[5, 5, 3, 0, 5, 5], [5, 0, 4, 0, 4, 4], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]]
)

# 手工分解求矩阵的svd
U = A * A.T
lamda, hU = linalg.eig(U)  # hU:U特征向量
VT = A.T * A
eV, hVT = linalg.eig(VT)  # hVT:VT特征向量
hV = hVT.T
# print "hU:",hU
# print "hV:",hV
sigma = sqrt(lamda)  # 特征值
print("sigma:", sigma)


Sigma = np.zeros([shape(A)[0], shape(A)[1]])
U, S, VT = linalg.svd(A)
# Sigma[:shape(A)[0], :shape(A)[0]] = np.diag(S)
# print(U)
print(S)
# print(VT)

# print(U*Sigma*VT)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testRecomm01.py

from numpy import *
import operator

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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testRecommsvd.py

from numpy import *
import operator

eps = 1.0e-6


# 夹角余弦，避免除0
def cosSim(inA, inB):
    denom = linalg.norm(inA) * linalg.norm(inB)
    return float(inA * inB.T) / (denom + eps)


# 加载修正后数据
A = mat(
    [[5, 5, 3, 0, 5, 5], [5, 0, 4, 0, 4, 4], [0, 3, 0, 5, 4, 5], [5, 4, 3, 3, 5, 5]]
)
new = mat([[5, 5, 0, 0, 0, 5]])
U, S, VT = linalg.svd(A.T)
V = VT.T
Sigma = diag(S)
r = 2  # 取前两个奇异值
# 近似后的U,S,V值
Ur = U[:, :r]
Sr = Sigma[:r, :r]
Vr = V[:, :r]
# 计算new的坐标值
newresult = new * Ur * linalg.inv(Sr)
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

# testRecommsvd2.py

from numpy import *
import operator

# 加载修正后数据
A = mat(
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
new = mat([[1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]])
indx, resultarray = recommand(A, new, r=2, rank=2, distCalc=cosSim)
print(indx)
print(resultarray)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# userdf.py

from numpy import *

dataMat = mat(
    [
        [0.238, 0, 0.1905, 0.1905, 0.1905, 0.1905],
        [0, 0.177, 0, 0.294, 0.235, 0.294],
        [0.2, 0.16, 0.12, 0.12, 0.2, 0.2],
    ]
)
testSet = [0.2174, 0.2174, 0.1304, 0, 0.2174, 0.2174]
classLabel = np.array(["B", "C", "D"])
print(my_kNN(testSet, dataMat, classLabel, 3))

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
