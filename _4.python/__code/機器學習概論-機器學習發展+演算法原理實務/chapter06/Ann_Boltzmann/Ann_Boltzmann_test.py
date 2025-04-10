# testBoltzmann01.py

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

def show():
    plt.show()
    pass

print("------------------------------------------------------------")  # 60個

import operator
import copy
import Untils
import Boltzmann
from numpy import *

print("------------------------------------------------------------")  # 60個
'''
dataSet = Untils.loadDataSet("cities.txt")
#dataSet = Untils.loadDataSet("dataSet25.txt")
cityPosition = mat(dataSet)
m, n = shape(cityPosition)
pn = m
# 将城市的坐标矩阵转换为邻接矩阵（城市间距离矩阵）
dist = Boltzmann.distM(cityPosition, cityPosition.T)

# 初始化
MAX_ITER = 2000  # 1000-2000
MAX_M = m
Lambda = 0.97
T0 = 1000
# 100-1000
# 构造一个初始可行解
x0 = arange(m)
random.shuffle(x0)
#
T = T0
iteration = 0
x = x0
# 路径变量
xx = x0.tolist()
# 每个路径
di = []
di.append(Boltzmann.pathLen(dist, x0))  # 每个路径对应的距离
k = 0
# 路径计数

# 外循环
while iteration <= MAX_ITER:
    # 内循环迭代器
    m = 0
    # 内循环
    while m <= MAX_M:
        # 产生新路径
        newx = Boltzmann.changePath(x)
        # 计算距离
        oldl = Boltzmann.pathLen(dist, x)
        newl = Boltzmann.pathLen(dist, newx)
        if oldl > newl:  # 如果新路径优于原路径，选择新路径作为下一状态
            x = newx
            xx.append(x)  # xx[n,:] = x
            di.append(newl)  # di[n] = newl
            k += 1
        else:  # 如果新路径比原路径差，则执行概率操作
            tmp = random.rand()
            sigmod = exp(-(newl - oldl) / T)
            if tmp < sigmod:
                x = newx
                xx.append(x)  # xx[n,:] = x
                di.append(newl)  # di[n]= newl
                k += 1
        m += 1  # 内循环次数加1
    # 内循环
    iteration += 1  # 外循环次数加1
    T = T * Lambda  # 降温

# 计算最优值
bestd = min(di)
indx = argmin(di)
bestx = xx[indx]
print("循环迭代", k, "次")
print("最优解:", bestd)
print("最佳路线:", bestx)

# 优化前城市图,路径图
Untils.drawScatter(cityPosition, flag=False)
Untils.drawPath(range(m - 1), cityPosition)

# 显示优化后城市图,路径图
Untils.drawScatter(cityPosition, flag=False)
Untils.drawPath(bestx, cityPosition, color="r")

# 绘制误差趋势线
x0 = range(len(di))
Untils.TrendLine(x0, di)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testBoltzmann01.py

import operator
import copy
import Untils
import Boltzmann
from numpy import *

dataSet = Untils.loadDataSet("dataSet25.txt")
cityPosition = mat(dataSet)
m, n = shape(cityPosition)
bestx, di = Boltzmann.boltzmann(cityPosition, MAX_ITER=2000, T0=100)


# 优化前城市图,路径图
Untils.drawScatter(cityPosition, flag=False)
Untils.drawPath(range(m), cityPosition)

# 显示优化后城市图,路径图
Untils.drawScatter(cityPosition, flag=False)
Untils.drawPath(bestx, cityPosition, color="r")

# 绘制误差趋势线
x0 = range(len(di))
Untils.TrendLine(x0, di)
'''
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# showCityPath.py

import operator
import copy
import Untils
from numpy import *


# 加载数据文件
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split("\t")) - 1
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split("\t")
        lineArr.append(float(curLine[0]))
        lineArr.append(float(curLine[1]))
        dataMat.append(lineArr)
    return dataMat


# 绘制二维数据集坐标散点图:无分类
# 适用于 List 和 Matrix
def drawScatter(dataMat, plt):
    px = (dataMat[:, 0]).tolist()
    py = (dataMat[:, 1]).tolist()
    plt.scatter(px, py, c="green", marker="o", s=60)
    i = 65
    for x, y in zip(px, py):
        plt.annotate(
            str(chr(i)) + "(" + str(int(x[0])) + "," + str(int(y[0])) + ")",
            xy=(x[0] + 40, y[0]),
            color="black",
            fontsize=10,
        )
        i += 1


def drawPath(Seq, dataMat, plt, color="b"):
    m, n = shape(dataMat)
    px = (dataMat[Seq, 0]).tolist()
    py = (dataMat[Seq, 1]).tolist()
    px.append(px[0])
    py.append(py[0])
    plt.plot(px, py, color)


dataSet = loadDataSet("dataSet25.txt")
cityPosition = mat(dataSet)
m, n = shape(cityPosition)


# 优化前城市图,路径图
drawScatter(cityPosition, plt)
"""
drawPath(range(m),cityPosition,plt) 
"""
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# dataSet.py

import operator
import Untils
import Boltzmann
from numpy import *

# 载入数据
dataSet = Untils.loadDataSet("dataset.txt")
cityPosition = mat(dataSet)
m, n = shape(cityPosition)

# 随机数
tmp = random.rand()
print(tmp)

# 不重复的随机数
path = mat(zeros((m, m)))
tmp = arange(m)
for i in range(m):
    random.shuffle(tmp)
    path[i, :] = tmp
# print(path)

# 绘制数据散点图
# Untils.drawScatter(dataSet)

# 将城市的坐标矩阵转换为邻接矩阵（城市间距离矩阵）
dist = Boltzmann.distM(cityPosition, cityPosition.T)

path = arange(m)
# print(Boltzmann.pathLen(dist,path))

# sort
a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
a.sort()
# print(a)
x1 = 3
x2 = 5
# print(a[x1:x2])
# print(x2-x1)

a = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
b = a
c = a
a[2:8] = b[3:9] + []
print(a)
print(b)
print(c)
# 改变路径
newPath = Boltzmann.changePath(path.tolist())
# print(newPath)

b = []
b.append(3.14)
b.append(5.78)
# print(b)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testBoltzmann01.py

import operator
import copy
import Untils
from BMNet import *
from numpy import *

bmNet = BoltzmannNet()
bmNet.loadDataSet("dataSet25.txt")
bmNet.train()
print("循环迭代", bmNet.iteration, "次")
print("最优解:", bmNet.bestdist)
print("最佳路线:", bmNet.bestpath)

# 显示优化后城市图,路径图
bmNet.drawScatter(plt)
bmNet.drawPath(plt)
show()

# 绘制误差算法收敛曲线
bmNet.TrendLine(plt)
show()

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

