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
"""
# 01loadimg.py

from numpy import *
import cv2

win_name = 'mypicture' #窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow( win_name , cv2.WINDOW_NORMAL)
img = cv2.imread( 'snapshot0001.jpg',0) #0 黑白图片；1 原色图片
cv2.imshow(win_name ,img) # 显示图片
cv2.waitKey(0)
cv2.destroyAllWindows() # 销毁创建的对象
# 保存图片
# cv2.imwrite("paulwalker.mono.pgm", img)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 02opencvmatplotlib.py

from numpy import *
import cv2

# 读取图片
img = cv2.imread( 'paulwalker.mono.pgm' , 0) #黑白图片
plt.imshow(img, cmap = 'gray' , interpolation = 'bicubic' )
plt.xticks([]), plt. yticks([]) # 隐藏 X Y 坐标
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03drawrectangle.py

from numpy import *
import cv2

# Create a black image
img=zeros((512,512,3))
# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色:( 255,0,0)，宽度:2
cv2.line(img,(0,0),(511,511),( 255,0,0),2)
cv2.imshow('image' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04drawGeometry.py

from numpy import *
import cv2
img=zeros(( 512, 512, 3))
cv2.rectangle(img,( 384, 0),( 510, 128),( 0, 255, 0), 3) #矩形
cv2.circle(img,( 447, 63), 63, ( 0, 0, 255), - 1) #圆
cv2.ellipse(img,( 256, 256),( 100, 50), 0, 0, 360, 255, -1) #椭圆
#画多边形
pts=array([[10,5],[ 20,30],[70,20],[50,10]])
cv2.polylines(img,[pts],True,(0,255,255),1)
#写入文字
font=cv2.FONT_HERSHEY_SIMPLEX
cv2. putText(img, 'OpenCV' ,( 10, 500), font, 4,( 255, 255, 255), 2)
cv2.imshow('image' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05drawcirlcle.py

from numpy import *
import cv2

img=zeros(( 512, 512, 3))
# 绘制圆：圆心(255, 255), 半径60, 颜色( 0, 255, 255), 像素1
cv2.circle(img,(255, 150), 60, ( 0, 255, 255), 2) #圆
# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100  
# 360表示整个椭圆；颜色 0, 255, 255；像素2；
cv2.ellipse(img,(255, 350),(100, 50), 0, 0, 360, (255,255,0), 2) #椭圆
cv2.imshow('image' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Adaboost is short for Adaptive Boosting

from numpy import *
import copy


def loadDataSet(fileName):
    recordlist = []
    print(fileName)
    fp = open(fileName, "r")
    content = fp.read()
    fp.close()
    rowlist = content.splitlines()
    recordlist = [map(eval, row.split("\t")) for row in rowlist if row.strip()]
    dataSet = mat(recordlist)[:, :-1]
    labels = mat(recordlist)[:, -1].T
    return dataSet, labels


# dataMat:数据集,
# Column: 第几列
# threshVal:阈值
# threshSymb:分类分隔符,lt,gt符号
def splitDataSet(dataMat, Column, threshVal, operator):
    retArray = ones((shape(dataMat)[0], 1))  # 与数据集行数相同的全1向量
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
    dataMat = mat(dataSet)
    labelMat = mat(labellist).T
    m, n = shape(dataMat)  # 数据集行、列数
    numSteps = 10.0
    # 迭代步数
    bestFeat = {}
    # 最优项列
    bestClass = mat(zeros((m, 1)))  # 最优预测分类
    minError = inf  # 初始化最小误差为无穷大
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
                errSet = mat(ones((m, 1)))  # 初始化误差集为一个全1向量
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
    m = shape(dataSet)[0]
    D = mat(ones((m, 1)) / m)  # 初始化D为平均权重
    aggClassSet = mat(zeros((m, 1)))
    for i in range(numIt):
        bestFeat, error, EstClass = decisionTree(dataSet, labellist, D)
        alpha = float(
            0.5 * log((1.0 - error) / max(error, 1e-16))
        )  # alpha计算公式，1e-16避免除0
        bestFeat["alpha"] = alpha
        weakClassSet.append(bestFeat)  # 以数组形式存储弱分类器
        # 算法核心：D--权重修改公式：D*exp((+-)alpha)/sum(D)（Logistic）
        # +-号取决于是否错分，+正确划分，-错误划分
        wtx = multiply(-1 * alpha * mat(labellist).T, EstClass)  # 矩阵对应元素相乘:multiply矩阵点积
        D = multiply(D, exp(wtx))  # 为下次迭代计算新的D
        D = D / D.sum()
        aggClassSet += alpha * EstClass  # 累计预测类：
        # 如果 x>0 sign(x)=1; x<0 sign(x)=-1
        # 计算所有分类器的训练误差--累计误差
        totalErr = multiply(sign(aggClassSet) != mat(labellist).T, ones((m, 1)))
        errorRate = totalErr.sum() / m  # 计算总误差率
        if errorRate == 0.0:
            break  # 如果为0，分类完毕 跳出循环
    return weakClassSet, aggClassSet


# Ada分类器
def adaClassify(datToClass, classdictList):
    dataMat = mat(datToClass)  # do stuff similar to last aggClassSet in adaBoostTrainDS
    m = shape(dataMat)[0]
    aggClassSet = mat(zeros((m, 1)))
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
    numPosClas = sum(array(labellist) == 1.0)
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
    plt.show()
    print("the Area Under the Curve is: ", ySum * xStep)


# adaboost_traincase
# testAdaboost2.py

from numpy import *

# 导入训练集
dataArr, labelArr = loadDataSet("train.dat")

print("dataArr")
print(dataArr)

print("labelArr")
print(labelArr)

""" NG
weakClassArr, aggClassEst = adaBoostTrain(dataArr, labelArr, numIt=10)  # 训练分类器
print("weakClassArr:", weakClassArr)  # 输出弱分类器
# plotROC(aggClassEst.T, labelArr) # 绘制ROC曲线
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *
import cv2

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
img = cv2.imread("snapshot0001.jpg", 0)  # 0 黑白图片；1 原色图片
cv2.imshow(win_name, img)  # 显示图片
cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁创建的对象
# 保存图片
# cv2.imwrite("paulwalker.mono.pgm", img)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *
import cv2
from matplotlib import pyplot as plt

# 读取图片
img = cv2.imread("paulwalker.mono.pgm", 0)  # 黑白图片
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # 隐藏 X Y 坐标
plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


from numpy import *
import cv2

# Create a black image
img = zeros((512, 512, 3))
# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色:( 255,0,0)，宽度:2
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *
import cv2

img = zeros((512, 512, 3))
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 矩形
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)  # 圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)  # 椭圆
# 画多边形
pts = array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, (0, 255, 255), 1)
# 写入文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from numpy import *
import cv2

img = zeros((512, 512, 3))
# 绘制圆：圆心(255, 255), 半径60, 颜色( 0, 255, 255), 像素1
cv2.circle(img, (255, 150), 60, (0, 255, 255), 2)  # 圆
# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100
# 360表示整个椭圆；颜色 0, 255, 255；像素2；
cv2.ellipse(img, (255, 350), (100, 50), 0, 0, 360, (255, 255, 0), 2)  # 椭圆
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# adaboost_traincase.py

from numpy import *
from adaboostlib import *

# 导入训练集
dataArr, labelArr = loadDataSet("train.dat")

weakClassArr, aggClassEst = adaBoostTrain(dataArr, labelArr, numIt=10)  # 训练分类器
print("weakClassArr:", weakClassArr)  # 输出弱分类器
# plotROC(aggClassEst.T, labelArr) # 绘制ROC曲线

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# eigencog_face.py

from numpy import *
from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")
ef.compute()
E = []
X = mat(zeros((10, 10304)))
for i in range(16):
    X = ef.Mat[i * 10 : (i + 1) * 10, :].copy()
    # X = ef.normalize(X.mean(axis =0),0,255)
    X = X.mean(axis=0)
    imgs = X.reshape(112, 92)
    E.append(imgs)
ef.subplot(title="AT&T Eigen Facedatabase", images=E)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# eigencog_test.py

from numpy import *
from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")
ef.compute()
# 创建测试集
testImg = ef.X[30]
print("实际值 =", ef.y[30], "->", "预测值 =", ef.predict(testImg))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

from numpy import *
import cv2

face_cascade = cv2.CascadeClassifier(
    "E:\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_alt_tree.xml"
)

img = cv2.imread("mypicture.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("paulwalker.head.jpg", img)  # 保存图片

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

from numpy import *
import cv2

face_cascade = cv2.CascadeClassifier(
    "E:\\opencv\\sources\\data\\lbpcascades\\lbpcascade_frontalface.xml"
)

img = cv2.imread("snapshot0001.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("paulwalker.head.jpg", img)  # 保存图片

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# testcase.py

from numpy import *
from adaboostlib import *

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
errArr = mat(ones((67, 1)))
totalError = errArr[ClassEst100 != mat(testLabelArr).T].sum()
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
