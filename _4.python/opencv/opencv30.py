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

img = cv2.imread('images/computer.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize = 3)
orgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
oShow=orgb.copy()
lines = cv2.HoughLines(edges,1,np.pi/180,140)
for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(orgb,(x1,y1),(x2,y2),(0,0,255),2)

plt.subplot(121)
plt.imshow(oShow)
plt.axis('off')

plt.subplot(122)
plt.imshow(orgb)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/computer.jpg', -1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,150,apertureSize =3)
orgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
oShow=orgb.copy()
lines = cv2.HoughLinesP(edges,1,np.pi/180,160,minLineLength=100,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(orgb,(x1,y1),(x2,y2),(255,255,255),2)

plt.subplot(121)
plt.imshow(oShow)
plt.axis('off')

plt.subplot(122)
plt.imshow(orgb)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/chess.jpg', 0)
imgo=cv2.imread('images/chess.jpg', -1)
o=cv2.cvtColor(imgo,cv2.COLOR_BGR2RGB)
oshow=o.copy()
img = cv2.medianBlur(img,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,param1=50,param2=30,minRadius=100,maxRadius=200)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(o,(i[0],i[1]),i[2],(255,0,0),12)
    cv2.circle(o,(i[0],i[1]),2,(255,0,0),12)

plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')

plt.subplot(122)
plt.imshow(o)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/chess.jpg', 0)
imgo=cv2.imread('images/chess.jpg', -1)
o=cv2.cvtColor(imgo,cv2.COLOR_BGR2RGB)
oshow=o.copy()
img = cv2.medianBlur(img,5)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    cv2.circle(o,(i[0],i[1]),i[2],(255,0,0),12)   #注意如果是白色，会显示满屏白色，不仔细分析还会以为程序错了呢
    cv2.circle(o,(i[0],i[1]),2,(255,0,0),12)

plt.subplot(121)
plt.imshow(oshow)
plt.axis('off')

plt.subplot(122)
plt.imshow(o)
plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個


