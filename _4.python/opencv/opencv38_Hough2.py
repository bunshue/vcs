"""
霍夫變換

HoughLines
HoughLinesP
HoughCircles

"""

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

img = cv2.imread('images/jianzhu.png') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
#hough变换
lines = cv2.HoughLines(edges,1,np.pi/180,180)
lines1 = lines[:,0,:]#提取为为二维
for rho,theta in lines1[:]: 
	a = np.cos(theta)
	b = np.sin(theta)
	x0 = a*rho
	y0 = b*rho
	x1 = int(x0 + 1000*(-b))
	y1 = int(y0 + 1000*(a))
	x2 = int(x0 - 1000*(-b))
	y2 = int(y0 - 1000*(a)) 
	cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])
plt.show()

print('------------------------------------------------------------')	#60個

lane = cv2.imread('images/lane.jpg')
# 高斯模糊，Canny边缘检测需要的
lane = cv2.GaussianBlur(lane, (5, 5), 0)    #執行高斯模糊化
# 进行边缘检测，减少图像空间中需要检测的点数量
lane = cv2.Canny(lane, 50, 150)
cv2.imshow("lane", lane)
cv2.waitKey()

rho = 1  # 距离分辨率
theta = np.pi / 180  # 角度分辨率
threshold = 10  # 霍夫空间中多少个曲线相交才算作正式交点
min_line_len = 10  # 最少多少个像素点才构成一条直线
max_line_gap = 50  # 线段之间的最大间隔像素
lines = cv2.HoughLinesP(lane, rho, theta, threshold, maxLineGap=max_line_gap)
line_img = np.zeros_like(lane)
for line in lines:
    for x1, y1, x2, y2 in line:
        cv2.line(line_img, (x1, y1), (x2, y2), 255, 1)

cv2.imshow("line_img", line_img)

cv2.waitKey()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/4.png', 0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,
                            param1=100,param2=30,minRadius=100,maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # 画外圆
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # 画出圆心
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個

