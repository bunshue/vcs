
print('------------------------------------------------------------')	#60個

import cv2

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

#第1步 準備數據
# A等級的筆試、面試分數
a = np.random.randint(95, 100, (20, 2)).astype(np.float32)
# B等級的筆試、面試分數
b = np.random.randint(90, 95, (20, 2)).astype(np.float32)

#合并數據
data = np.vstack((a, b))
data = np.array(data,dtype = 'float32')

#第2步 建立分組標簽，0代表A等級，1代表B等級
#aLabel對應著a的標簽，為類型0-等級A
aLabel = np.zeros((20, 1))
#bLabel對應著b的標簽，為類型1-等級B
bLabel = np.ones((20, 1))
#合并標簽
label = np.vstack((aLabel, bLabel))
label = np.array(label, dtype = 'int32')

#第3步 訓練
# ml 機器學習模塊 SVM_create() 創建
svm = cv2.ml.SVM_create() 
# 屬性設置，直接采用默認值即可。
#svm.setType(cv2.ml.SVM_C_SVC) # svm type
#svm.setKernel(cv2.ml.SVM_LINEAR) # line
#svm.setC(0.01)
# 訓練
result = svm.train(data, cv2.ml.ROW_SAMPLE,label)

#第4步 預測
#生成兩個隨機的(筆試成績、面試成績)，可以用隨機數生成
test = np.vstack([[99, 90], [90, 99]]) #0-A級 1-B級
test = np.array(test, dtype = 'float32')
#預測
(p1, p2) = svm.predict(test)

#第5步 觀察結果
#可視化
plt.scatter(a[:, 0], a[:, 1], 80, 'g', 'o')
plt.scatter(b[:, 0], b[:, 1], 80, 'b', 's')
plt.scatter(test[:, 0], test[:, 1], 80, 'r', '*')
plt.show()

#打印原始測試數據test，預測結果
print(test)
print(p2)

print('------------------------------------------------------------')	#60個

#讀取樣本（特征）圖像的值
s='images\\'  #圖像所在路徑
num=100 #共有樣本數量
row=240 #每個數字圖像的行數
col=240 #每個數字圖像的列數
a=np.zeros((num,row,col)) #用來存儲所有樣本的數值
#print(a.shape)
n=0 #用來存儲當前圖像的編號。
for i in range(0,10):
    for j in range(1,11):
        a[n,:,:]=cv2.imread(s+str(i)+'\\'+str(i)+'-'+str(j)+'.bmp',0)
        n=n+1

#提取樣本圖像的特征
feature=np.zeros((num,round(row/5),round(col/5))) #用來存儲所有樣本的特征值
#print(feature.shape)  #看看feature的shape長什么樣子
#print(row)            #看看row的值，有多少個特征（100）個

for ni in range(0,num):
    for nr in range(0,row):
        for nc in range(0,col):
            if a[ni,nr,nc]==255:
                feature[ni,int(nr/5),int(nc/5)]+=1
f=feature   #簡化變量名稱

#####計算當前待識別圖像的特征值
o=cv2.imread('images\\test\\5.bmp',0) #讀取待測圖像
##讀取圖像值
of=np.zeros((round(row/5),round(col/5))) #用來存儲測試圖像的特征值
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1

###開始計算，數字識別，計算最近的times個數字是誰，判斷結果
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
#print(temp)   #看看都被識別為哪些特征值了。
 
temp=[i/10 for i in temp]
#也可以返回去，處理為array,使用函數處理，意思差不多。
#temp=np.array(temp)
#temp=np.trunc(temp/10)
#print(temp)
#數組r用來存儲結果，r[0]表示k近鄰中0的個數，r[n]K近鄰中n的個數
r=np.zeros(10)
for i in temp:
    r[int(i)]+=1
#print(r)
print('當前的數字可能為:'+str(np.argmax(r)))

print('------------------------------------------------------------')	#60個

#用于訓練的數據
#rand1數據位于(0,30)
rand1 = np.random.randint(0, 30, (20, 2)).astype(np.float32)
#rand2數據位于(70,100)
rand2 = np.random.randint(70, 100, (20, 2)).astype(np.float32)
#將rand1和rand2拼接為訓練數據
trainData = np.vstack((rand1, rand2))
#數據標簽，兩類：0,1
#r1Label對應著rand1的標簽，為類型0
r1Label=np.zeros((20,1)).astype(np.float32)
#r2Label對應著rand2的標簽，為類型1
r2Label=np.ones((20,1)).astype(np.float32)
tdLable = np.vstack((r1Label, r2Label))
#使用綠色標注類型0
g = trainData[tdLable.ravel() == 0]
plt.scatter(g[:,0], g[:,1], 80, 'g', 'o')
#使用藍色標注類型1
b = trainData[tdLable.ravel() == 1]
plt.scatter(b[:,0], b[:,1], 80, 'b', 's')

plt.show()
#test用于測試的隨機數，該數在0到100之間
test = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(test[:,0], test[:,1], 80, 'r', '*')
#調用OpenCV內的KNN，并訓練
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, tdLable)
#使用KNN分類
ret, results, neighbours, dist = knn.findNearest(test, 5)
#顯示處理結果
print("當前隨機數可以判定為類型：", results)
print("距離當前點最近的5個鄰居是：", neighbours)
print("5個最近鄰居的距離: ", dist)
#可以觀察一下顯示，對比上述輸出
plt.show()

print('------------------------------------------------------------')	#60個

#讀取樣本（特征）圖像的值
s='images\\'  #圖像所在路徑
num=100 #共有樣本數量
row=240 #每個數字圖像的行數
col=240 #每個數字圖像的列數
a=np.zeros((num,row,col)) #用來存儲所有樣本的數值
#print(a.shape)
n=0 #用來存儲當前圖像的編號。
for i in range(0,10):
    for j in range(1,11):
        a[n,:,:]=cv2.imread(s+str(i)+'\\'+str(i)+'-'+str(j)+'.bmp',0)
        n=n+1

#提取樣本圖像的特征
feature=np.zeros((num,round(row/5),round(col/5))) #用來存儲所有樣本的特征值
#print(feature.shape)  #看看feature的shape長什么樣子
#print(row)            #看看row的值，有多少個特征（100）個


for ni in range(0,num):
    for nr in range(0,row):
        for nc in range(0,col):
            if a[ni,nr,nc]==255:
                feature[ni,int(nr/5),int(nc/5)]+=1
f=feature   #簡化變量名稱
#將feature處理為單行形式
train = feature[:,:].reshape(-1,round(row/5)*round(col/5)).astype(np.float32) 
#print(train.shape)
#貼標簽，需要注意range(0,100)不是range(0,101)
trainLabels = [int(i/10)  for i in range(0,100)]
trainLabels=np.asarray(trainLabels)
#print(*trainLabels)   #打印測試看看標簽值
##讀取圖像值
o=cv2.imread('images\\test\\5.bmp',0) #讀取待測圖像
of=np.zeros((round(row/5),round(col/5))) #用來存儲測試圖像的特征值
for nr in range(0,row):
    for nc in range(0,col):
        if o[nr,nc]==255:
            of[int(nr/5),int(nc/5)]+=1

test=of.reshape(-1,round(row/5)*round(col/5)).astype(np.float32) 
#調用函數識別
knn=cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE, trainLabels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
print("當前隨機數可以判定為類型：", result)
print("距離當前點最近的5個鄰居是：", neighbours)
print("5個最近鄰居的距離: ", dist)

print('------------------------------------------------------------')	#60個

#隨機生成兩組數組
#生成60粒直徑大小在[0,50]之間的xiaoMI
xiaoMI = np.random.randint(0,50,60)
#生成60粒直徑大小在[200,250]之間的daMI
daMI = np.random.randint(200,250,60)
#將xiaoMI和daMI組合為MI
MI = np.hstack((xiaoMI,daMI))
#使用reshape函數將其轉換為(120,1)
MI = MI.reshape((120,1))
#將MI的數據類型轉換為float32
MI = np.float32(MI)
#調用kmeans模塊
#設置參數criteria的值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#設置參數flags的值
flags = cv2.KMEANS_RANDOM_CENTERS
#調用函數kmeans
retval,bestLabels,centers = cv2.kmeans(MI,2,None,criteria,10,flags)
'''
#打印返回值
print(retval)
print(bestLabels)
print(centers)
'''
#獲取分類結果
XM = MI[bestLabels==0]
DM = MI[bestLabels==1]
#繪制分類結果
#繪制原始數據
plt.plot(XM,'ro')
plt.plot(DM,'bs')
#繪制中心點
plt.plot(centers[0],'rx')
plt.plot(centers[1],'bx')

plt.show()

print('------------------------------------------------------------')	#60個

#隨機生成兩組數值
#xiaomi組,長和寬的大小都在[0,20]
xiaomi = np.random.randint(0,20,(30,2))
#dami組,長和寬的大小都在[40,60]
dami = np.random.randint(40,60,(30,2))
#組合數據
MI = np.vstack((xiaomi,dami))
# 轉換為float32類型
MI = np.float32(MI)
# 調用kmeans模塊
#設置參數criteria值
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
#調用kmeans函數
ret,label,center=cv2.kmeans(MI,2,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
'''
#打印返回值
print(ret)
print(label)
print(center)
'''
# 根據kmeans處理結果，將數據分類，分為XM和DM兩大類
XM = MI[label.ravel()==0]
DM = MI[label.ravel()==1]
# 繪制分類結果數據及中心點
plt.scatter(XM[:,0],XM[:,1],c = 'g', marker = 's')
plt.scatter(DM[:,0],DM[:,1],c = 'r', marker = 'o')
plt.scatter(center[0,0],center[0,1],s = 200,c = 'b', marker = 'o')
plt.scatter(center[1,0],center[1,1],s = 200,c = 'b', marker = 's')
plt.xlabel('Height'),plt.ylabel('Width')

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
#讀取待處理圖像
img = cv2.imread(filename)
#使用reshape將一個RGB像素點值的三個值作為一個單元
data = img.reshape((-1,3))
#轉換為kmeans可以處理的類型
data = np.float32(data)
#調用kmeans模塊
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K =2
ret,label,center=cv2.kmeans(data,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# 轉換為uint8數據類型，將每個像素點值都賦值為當前組的中心點值
#將center的值轉換為uint8
center = np.uint8(center)
#使用center內的值替換原有像素點值
res1 = center[label.flatten()]
#使用reshape調整替換后圖像
res2 = res1.reshape((img.shape))
#顯示處理結果
plt.subplot(121)
plt.imshow(img)
plt.axis('off')
plt.subplot(122)
plt.imshow(res2)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

