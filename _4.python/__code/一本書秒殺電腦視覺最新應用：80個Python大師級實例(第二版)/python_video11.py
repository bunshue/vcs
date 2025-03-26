"""


"""
print("------------------------------------------------------------")  # 60個

import cv2

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#FLANN.py

"""
基于FLANN的匹配器(FLANN based Matcher)
FLANN代表近似最近邻居的快速库。它代表一组经过优化的算法，用于大数据集中的快速最近邻搜索以及高维特征。
"""

import cv2 as cv
from matplotlib import pyplot as plt

queryImage=cv.imread("template_adjust.jpg",0)
trainingImage=cv.imread("target.jpg",0)#读取要匹配的灰度照片
sift=cv.xfeatures2d.SIFT_create()#创建sift检测器
kp1, des1 = sift.detectAndCompute(queryImage,None)
kp2, des2 = sift.detectAndCompute(trainingImage,None)
#设置Flannde参数
FLANN_INDEX_KDTREE=0
indexParams=dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
searchParams= dict(checks=50)
flann=cv.FlannBasedMatcher(indexParams,searchParams)
matches=flann.knnMatch(des1,des2,k=2)
#设置好初始匹配值
matchesMask=[[0,0] for i in range (len(matches))]
for i, (m,n) in enumerate(matches):
	if m.distance< 0.5*n.distance: #舍弃小于0.5的匹配结果
		matchesMask[i]=[1,0]
#给特征点和匹配的线定义颜色
drawParams=dict(matchColor=(0,0,255),singlePointColor=(255,0,0),matchesMask=matchesMask,flags=0) 
#画出匹配的结果
resultimage=cv.drawMatchesKnn(queryImage,kp1,trainingImage,kp2,matches,None,**drawParams) 

plt.imshow(resultimage,),plt.show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# FLANN_positioning.py

#基于FLANN的匹配器(FLANN based Matcher)定位图片

import numpy as np
import cv2
from matplotlib import pyplot as plt
 
MIN_MATCH_COUNT = 10 #设置最低特征点匹配数量为10
template = cv2.imread('template_adjust.jpg',0) # queryImage
target = cv2.imread('target.jpg',0) # trainImage
# Initiate SIFT detector创建sift检测器
sift = cv2.xfeatures2d.SIFT_create()
# 使用SIFT查找关键字和描述符
kp1, des1 = sift.detectAndCompute(template,None)
kp2, des2 = sift.detectAndCompute(target,None)
#创建设置FLANN匹配
FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks = 50)
flann = cv2.FlannBasedMatcher(index_params, search_params)
matches = flann.knnMatch(des1,des2,k=2)
# 根据Lowe's比率测试保存所有的匹配项
good = []
#舍弃大于0.7的匹配
for m,n in matches:
    if m.distance < 0.7*n.distance:
        good.append(m)
if len(good)>MIN_MATCH_COUNT:
    # 获取关键点的坐标
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
    #计算变换矩阵和MASK
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
    matchesMask = mask.ravel().tolist()
    h,w = template.shape
    # 使用得到的变换矩阵对原图像的四个角进行变换，获得在目标图像上对应的坐标
    pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
    dst = cv2.perspectiveTransform(pts,M)
    cv2.polylines(target,[np.int32(dst)],True,0,2, cv2.LINE_AA)
else:
    print( "没有找到足够的匹配项 - %d/%d" % (len(good),MIN_MATCH_COUNT))
    matchesMask = None
draw_params = dict(matchColor=(0,255,0), 
                   singlePointColor=None,
                   matchesMask=matchesMask, 
                   flags=2)
result = cv2.drawMatches(template,kp1,target,kp2,good,None,**draw_params)
plt.imshow(result, 'gray')
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Multi_objective_matching.py

#opencv模板匹配----多目标匹配

import cv2
import numpy as np

red = (0, 0, 255)
linewidth = 3

#读取目标图片
target = cv2.imread("target.jpg")

#读取模板图片
template = cv2.imread("template.jpg")

#获得模板图片的高宽尺寸
theight, twidth = template.shape[:2]
#执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
#归一化处理
#寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
"""绘制矩形边框，将匹配区域标注出来
min_loc：矩形定点
min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
(0,0,225)：矩形的边框颜色；2：矩形边框宽度"""
cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)
#匹配值转换为字符串
#对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
#对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
strmin_val = str(min_val)
#初始化位置参数
temp_loc = min_loc
other_loc = min_loc
numOfloc = 1
#第一次筛选----规定匹配阈值，将满足阈值的从result中提取出来
#对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法设置匹配阈值为0.01
threshold = 0.01
loc = np.where(result<threshold)
#遍历提取出来的位置
for other_loc in zip(*loc[::-1]):
    #第二次筛选----将位置偏移小于5个像素的结果舍去
    if (temp_loc[0]+5<other_loc[0])or(temp_loc[1]+5<other_loc[1]):
        numOfloc = numOfloc + 1
        temp_loc = other_loc
        cv2.rectangle(target,other_loc,(other_loc[0]+twidth,other_loc[1]+theight),(0,0,225),2)
str_numOfloc = str(numOfloc)

#显示结果,并将匹配值显示在标题栏上
strText = "MatchResult----MatchingValue="+strmin_val+"----NumberOfPosition="+str_numOfloc

print('匹配值 :', strmin_val)

cv2.imshow(strText,target)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

#Single_target_matching.py

#opencv模板匹配----单目标匹配

import cv2

red = (0, 0, 255)
linewidth = 3

#读取目标图片
target = cv2.imread("target.jpg")

#读取模板图片
template = cv2.imread("template.jpg")

#获得模板图片的高宽尺寸
theight, twidth = template.shape[:2]
#执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
result = cv2.matchTemplate(target,template,cv2.TM_SQDIFF_NORMED)
#归一化处理
cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )
#寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#匹配值转换为字符串
#对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
#对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
strmin_val = str(min_val)

#绘制矩形边框，将匹配区域标注出来
#min_loc：矩形定点
#(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高

cv2.rectangle(target,min_loc,(min_loc[0]+twidth,min_loc[1]+theight), red, linewidth)

#显示结果,并将匹配值显示在标题栏上
strText = "MatchResult----MatchingValue=" + strmin_val

print('匹配值 :', strmin_val)

cv2.imshow(strText, target)
cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

