"""
machine_learning2c_svd2

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

# 输入数据：用户-菜肴
# 行：用户，列：菜肴
# 数字表示用户对菜肴的喜好评分1-5,0表示未品尝该菜
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
    # corrcoef()返回的是2*2的对称矩阵,索引[0][1]或者[1][0]都行
    # 并将值范围[-1,1]归一化到[0,1]
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


# 夹角余弦：计算空间内两点之间的夹角余弦
# 两个n维样本点a(x11,x12,…,x1n)和b(x21,x22,…,x2n)的夹角余弦
# cos(theta) = a*b/(|a|*|b|)
def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = np.linalg.norm(inA) * np.linalg.norm(inB)
    # 将余弦夹角值[-1,1]归一化到[0,1]
    return 0.5 + 0.5 * (num / denom)


# 标准相似度计算方法下的用户估计值
def standEst(dataMat, user, simMeas, item):
    n = np.shape(dataMat)[1]  # 列数
    simTotal = 0.0
    ratSimTotal = 0.0

    # 遍历所有物品
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
    # 归一化预测评分
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
