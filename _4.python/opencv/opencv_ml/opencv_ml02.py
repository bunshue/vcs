import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#读取样本（特征）图像的值
s='images\\'  #图像所在路径
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

#####计算当前待识别图像的特征值
o=cv2.imread('images\\test\\5.bmp',0) #读取待测图像
##读取图像值
of=np.zeros((round(row/5),round(col/5))) #用来存储测试图像的特征值
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1

###开始计算，数字识别，计算最近的times个数字是谁，判断结果
d=np.zeros(100)
for i in range(0,100):
    d[i]=np.sum((of-f[i,:,:])*(of-f[i,:,:]))
#print(d)
d=d.tolist()
temp=[]
Inf = max(d)
#print(Inf)
k=7
for i in range(k):
    temp.append(d.index(min(d)))
    d[d.index(min(d))]=Inf
#print(temp)   #看看都被识别为哪些特征值了。
 
temp=[i/10 for i in temp]
#也可以返回去，处理为array,使用函数处理，意思差不多。
#temp=np.array(temp)
#temp=np.trunc(temp/10)
#print(temp)
#数组r用来存储结果，r[0]表示k近邻中0的个数，r[n]K近邻中n的个数
r=np.zeros(10)
for i in temp:
    r[int(i)]+=1
#print(r)
print('当前的数字可能为:'+str(np.argmax(r)))

print('------------------------------------------------------------')	#60個

#用于训练的数据
#rand1数据位于(0,30)
rand1 = np.random.randint(0, 30, (20, 2)).astype(np.float32)
#rand2数据位于(70,100)
rand2 = np.random.randint(70, 100, (20, 2)).astype(np.float32)
#将rand1和rand2拼接为训练数据
trainData = np.vstack((rand1, rand2))
#数据标签，两类：0,1
#r1Label对应着rand1的标签，为类型0
r1Label=np.zeros((20,1)).astype(np.float32)
#r2Label对应着rand2的标签，为类型1
r2Label=np.ones((20,1)).astype(np.float32)
tdLable = np.vstack((r1Label, r2Label))
#使用绿色标注类型0
g = trainData[tdLable.ravel() == 0]
plt.scatter(g[:,0], g[:,1], 80, 'g', 'o')
#使用蓝色标注类型1
b = trainData[tdLable.ravel() == 1]
plt.scatter(b[:,0], b[:,1], 80, 'b', 's')

plt.show()
#test用于测试的随机数，该数在0到100之间
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:,0], test[:,1], 80, 'r', '*')
#调用OpenCV内的KNN，并训练
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, tdLable)
#使用KNN分类
ret, results, neighbours, dist = knn.findNearest(test, 5)
#显示处理结果
print("当前随机数可以判定为类型：", results)
print("距离当前点最近的5个邻居是：", neighbours)
print("5个最近邻居的距离: ", dist)
#可以观察一下显示，对比上述输出
plt.show()

print('------------------------------------------------------------')	#60個

#读取样本（特征）图像的值
s='images\\'  #图像所在路径
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
o=cv2.imread('images\\test\\5.bmp',0) #读取待测图像
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

print('------------------------------------------------------------')	#60個

