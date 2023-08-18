# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 10:13:31 2018

@author: 李立宗  lilizong@gmail.com
《opencv图穷匕见-python实现》 电子工业出版社
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
#读取样本（特征）图像的值
s='image\\'  #图像所在路径
num=100 #共有样本数量
row=240 #每个数字图像的行数
col=240 #每个数字图像的列数
a=np.zeros((num,row,col)) #用来存储所有样本的数值
#print(a.shape)
n=0 #用来存储当前图像的编号。
for i in range(0,10):
    for j in range(1,11):
        a[n,:,:]=cv2.imread(s+str(i)+'\\'+str(i)+'-'+str(j)+'.bmp',0)
        n=n+1

#提取样本图像的特征
feature=np.zeros((num,round(row/5),round(col/5))) #用来存储所有样本的特征值
#print(feature.shape)  #看看feature的shape长什么样子
#print(row)            #看看row的值，有多少个特征（100）个


for ni in range(0,num):
    for nr in range(0,row):
        for nc in range(0,col):
            if a[ni,nr,nc]==255:
                feature[ni,int(nr/5),int(nc/5)]+=1
f=feature   #简化变量名称
#将feature处理为单行形式
train = feature[:,:].reshape(-1,round(row/5)*round(col/5)).astype(np.float32) 
#print(train.shape)
#贴标签，需要注意range(0,100)不是range(0,101)
trainLabels = [int(i/10)  for i in range(0,100)]
trainLabels=np.asarray(trainLabels)
#print(*trainLabels)   #打印测试看看标签值
##读取图像值
o=cv2.imread('image\\test\\5.bmp',0) #读取待测图像
of=np.zeros((round(row/5),round(col/5))) #用来存储测试图像的特征值
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1

test=of.reshape(-1,round(row/5)*round(col/5)).astype(np.float32) 
#调用函数识别
knn=cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE, trainLabels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
print("当前随机数可以判定为类型：", result)
print("距离当前点最近的5个邻居是：", neighbours)
print("5个最近邻居的距离: ", dist)