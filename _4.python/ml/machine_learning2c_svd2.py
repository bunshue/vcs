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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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
def loadExData0():
    return [
        [0, 0, 0, 2, 2],
        [0, 0, 0, 3, 3],
        [0, 0, 0, 1, 1],
        [1, 1, 1, 0, 0],
        [2, 2, 2, 0, 0],
        [5, 5, 5, 0, 0],
        [1, 1, 1, 0, 0],
    ]


def loadExData():
    return [
        [4, 4, 0, 2, 2],
        [4, 0, 0, 3, 3],
        [4, 0, 0, 1, 1],
        [1, 1, 1, 2, 0],
        [2, 2, 2, 0, 0],
        [1, 1, 1, 0, 0],
        [5, 5, 5, 0, 0],
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


def loadExData1():
    return [
        [2, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0],
        [3, 3, 4, 0, 3, 0, 0, 2, 2, 0, 0],
        [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0],
        [4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 4, 5, 0],
        [1, 1, 2, 1, 1, 2, 1, 0, 4, 5, 0],
    ]


# 基于欧氏距离的相似度：1/(1+欧氏距离)
def ecludSim(inA, inB):  # A,B两个样本向量
    # 库函数np.linalg.norm（）计算欧式距离
    return 1.0 / (1.0 + np.linalg.norm(inA - inB))


# 基于皮尔森相关系数的相似度：0.5+0.5*corrcoef()
def pearsSim(inA, inB):
    if len(inA) < 3:
        return 1.0
    # corrcoef()返回的是2*2的对称矩阵,索引[0][1]或者[1][0]都行
    # 并将值范围[-1,1]归一化到[0,1]
    return 0.5 + 0.5 * corrcoef(inA, inB, rowvar=0)[0][1]


# 基于余弦夹角的相似度
def cosSim(inA, inB):
    num = float(inA.T * inB)
    denom = np.linalg.norm(inA) * np.linalg.norm(inB)
    # 将余弦夹角值[-1,1]归一化到[0,1]
    return 0.5 + 0.5 * (num / denom)


# 基于物品相似度，计算用户对物品的评分估计值
# 输入：dataMat 用户数据
# user：用户编号（行）
# simMeas：相似度计算函数
# item:物品编号（列），用户待预测的物品
def standEst(dataMat, user, simMeas, item):
    # 数据矩阵列，即为物品数
    n = np.shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0

    # 遍历所有物品
    for j in range(n):
        # 用户user对j物品评分
        userRating = dataMat[user, j]
        # （1）若未对物品j评分，即userRating=0，不处理
        if userRating == 0:
            continue
        # （2）若对物品j评分：
        # 统计对物品item和物品j都评分的用户编号
        overLap = np.nonzero(
            np.logical_and(dataMat[:, item].A > 0, dataMat[:, j].A > 0)
        )[0]
        # （2.1）若没有用户同时对物品item和j评分，则两物品间相似度为0
        if len(overLap) == 0:
            similarity = 0
        # （2.2）若有用户同时对物品item和j评分，抽取出来，计算相似度
        else:
            similarity = simMeas(dataMat[overLap, item], dataMat[overLap, j])
        print("the %d and %d similarity is: %f" % (item, j, similarity))
        # 相似度求和
        simTotal += similarity
        # 预测用户user对物品item评分总和
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    # 归一化预测评分
    else:
        # print "ratSimTotal:",ratSimTotal
        # print "simTotal:",simTotal
        return ratSimTotal / simTotal


# 基于SVD的评分估计
# 输入：dataMat 用户数据
# user：用户编号（行）
# simMeas：相似度计算函数
# item:物品编号（列），用户待预测的物品
def svdEst(dataMat, user, simMeas, item):
    # 物品数
    n = np.shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    # SVD分解
    U, Sigma, VT = np.linalg.svd(dataMat)
    # 构建对角矩阵，取前3个奇异值
    # 3个额外算出来的，确保总能量>90%
    Sig3 = np.mat(np.eye(3) * Sigma[:3])
    # SVD降维，重构低维空间的物品#.I求逆
    xformedItems = dataMat.T * U[:, :3] * Sig3.I
    # 遍历所有物品
    for j in range(n):
        # 用户user对j物品评分
        userRating = dataMat[user, j]
        # 若未对物品j评分，即userRating=0，不处理
        if userRating == 0 or j == item:
            continue
        # 在低维空间计算物品j与物品item的相似度
        similarity = simMeas(xformedItems[item, :].T, xformedItems[j, :].T)
        print("the %d and %d similarity is: %f" % (item, j, similarity))
        # 相似度求和
        simTotal += similarity
        # 预测用户user对物品item评分总和
        ratSimTotal += similarity * userRating
    if simTotal == 0:
        return 0
    # 归一化预测评分
    else:
        return ratSimTotal / simTotal


# 基于物品相似度的推荐
# dataMat：  数据
# user：     用户编号
# N：       选择预测评分最高的N个结果
# simMeas：  相似度计算方法
# estMethod：用户对物品的预测估分方法
def recommend(dataMat, user, N=3, simMeas=cosSim, estMethod=standEst):
    # 找没有被用户user评分的物品
    unratedItems = np.nonzero(dataMat[user, :].A == 0)[1]
    # 若都评分则退出，不需要再推荐
    if len(unratedItems) == 0:
        return "you rated everything"
    itemScores = []
    # 遍历未评分的物品
    for item in unratedItems:
        # 预测用户user对为评分物品item的估分
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        # 存（物品编号，对应估分值）
        itemScores.append((item, estimatedScore))
    # 选择最高的估分结果
    return sorted(itemScores, key=lambda jj: jj[1], reverse=True)[:N]


"""
recommend() 用法
# 相似公式：夹角余弦
# output1 = recommend(dataMat, 1)

# 相似公式：欧氏距离
# output2 = recommend(dataMat,1,simMeas=ecludSim)

# 相似公式：相关系数
# output3 = recommend(dataMat,1,simMeas=pearsSim)
"""

# *****测试奇异值分解的结果：
data = [
    [1, 1, 1, 0, 0],
    [2, 2, 2, 0, 0],
    [1, 1, 1, 0, 0],
    [5, 5, 5, 0, 0],
    [1, 1, 0, 2, 2],
    [0, 0, 0, 3, 3],
    [0, 0, 0, 1, 1],
]
U, sigma, VT = np.linalg.svd(data)
print("sigma=", sigma)
print("U=", U)
print("VT=", VT)
# #低秩重构,取前3个奇异值
sigma3 = np.mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])
recondata = U[:, :3] * sigma3 * VT[:3, :]
print("recondata=")
print(recondata)


# (2)*****基于物品相似度的推荐，未用到SVD
data = loadExData()
# data=loadExData2() #用的是loadExData2()
data = np.mat(data)
itemscores = recommend(data, 5)  # 对用户2推荐
print("recommend result:")
print(itemscores)

#  (3)*****svd 查看能量分布
data = loadExData2()
u, sigma, vT = np.linalg.svd(np.mat(data))
print("sigma=", sigma)
sigma2 = sigma**2
print("all energy=", sum(sigma2))  # 总能量
print("90% of all energy=", sum(sigma2) * 0.9)  # 总能量的90%
# sigma_len=len(sigma) #奇异值个数
# # for i in range(sigma_len)
print("energy of the first 2 Singular value=", sum(sigma2[:2]))  # 前几个奇异值能量求和
print("energy of the first 3 Singular value=", sum(sigma2[:3]))

#  (4)*****基于svd推荐：
data = loadExData2()
data = np.mat(data)
itemscores = recommend(data, 1, estMethod=svdEst)  # 对用户1推荐,余弦夹角
# 对用户1推荐，皮尔逊系数
# itemscores=recommend(data,1,estMethod=svdEst,simMeas=pearsSim)
print("recommend result:")
print(itemscores)


# *****SVD的调用，及sigma输出格式，如何取对角矩阵
data = [
    [1, 1, 1, 0, 0],
    [2, 2, 2, 0, 0],
    [1, 1, 1, 0, 0],
    [5, 5, 5, 0, 0],
    [1, 1, 0, 2, 2],
    [0, 0, 0, 3, 3],
    [0, 0, 0, 1, 1],
]

u, sigma, vT = np.linalg.svd(data)
print(sigma)
sig3 = np.mat([[sigma[0], 0, 0], [0, sigma[1], 0], [0, 0, sigma[2]]])
recondata = u[:, :3] * sig3 * vT[:3, :]
print("recondata=", recondata)

# *****基于物品相似度的推荐，未用到SVD
data = loadExData()  # 用的是loadExData()
# data=loadExData2() #用的是loadExData2()
data = np.mat(data)
itemscores = recommend(data, 2)  # 对用户2推荐
print("recommend result:")
print(itemscores)


# *****svd 查看能量分布
data = loadExData2()
u, sigma, vT = np.linalg.svd(np.mat(data))
print("sigma=", sigma)
sigma2 = sigma**2
print("all energy=", sum(sigma2))  # 总能量
print("90% of all energy=", sum(sigma2) * 0.9)  # 总能量的90%
print("energy of the first 2 Singular value=", sum(sigma2[:2]))  # 前几个奇异值能量求和
print("energy of the first 3 Singular value=", sum(sigma2[:3]))


# *****基于svd推荐：
data = loadExData2()
data = np.mat(data)
itemscores = recommend(data, 1, estMethod=svdEst)  # 对用户1推荐,余弦夹角
# 对用户1推荐，皮尔逊系数
# itemscores=recommend(data,1,estMethod=svdEst,simMeas=pearsSim)
print("recommend result:")
print(itemscores)


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
