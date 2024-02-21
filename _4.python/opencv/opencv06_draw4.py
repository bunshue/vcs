'''
OpenCV 畫圖



cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.putText()
cv2.polylines


'''
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

print('OpenCV 畫圖')

#有底圖作畫
filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
image = cv2.imread(filename)	#讀取本機圖片

print('image.shape格式 :', type(image.shape))
print('image.shape內容 :', image.shape)

height = image.shape[0]    #高
width = image.shape[1]    #寬
d = image.shape[2]    #深
h, w, d = image.shape   #d為dimension d=3 全彩, d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)


image = cv2.line(image, (0, 0), (width, height), (255, 0, 0), 5)
image = cv2.line(image, (0, height), (width, 0), (0, 255, 0), 5)
image = cv2.rectangle(image, (100, 100), (200, 200), (128, 128, 128), 5)
image = cv2.rectangle(image, (0, 0), (width-10, height-10), (128, 128, 128), 5)

image = cv2.circle(image, (100, 100), 100, (0, 0, 255))
image = cv2.circle(image, (300, 300), 60, (0, 0, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
image = cv2.putText(image, 'OpenCV', (10, height - 100), font, 6, (0, 0, 255), 10, cv2.LINE_AA)

print('把圖片顯示出來')
cv2.imshow('image', image)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

def draw_line(image):
    H = image.shape[0]
    W = image.shape[1]
    print(image.shape)
    print(H//100)
    print(W//100)
    for i in range(H//100 + 1):
        cv2.line(image, (0, 100*i), (W, 100*i), (0, 0, 255), 2) #畫線 水平線 R

    for i in range(W//100 + 1):
        cv2.line(image, (100*i, 0), (100*i, H), (0, 255, 0), 2, lineType=cv2.LINE_AA) #畫線 垂直線 G

    #矩形之左上點
    p1x, p1y = 10, 10
    #矩形之右下點
    p2x, p2y = W-10, H-10
    cv2.rectangle(image,(p1x,p1y),(p2x,p2y),(255, 0, 0), 5)

    #矩形之左上點
    p1x, p1y = 10, 10
    #矩形之右下點
    p2x, p2y = W-10, H-10
    cv2.rectangle(image,(p1x,p1y),(p2x,p2y),(255, 0, 0), 5)


#有底圖作畫
filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
image = cv2.imread(filename)	#讀取本機圖片


draw_line(image)

"""
# 畫圓
center = (100, 100) #圓心
radius = 100 #半徑
color = (0, 255, 255) #顏色
linewidth = 2 #線寬
cv2.circle(image, center, radius, color,linewidth)

radius = 50
linewidth = -1 #線寬 負值代表實心
cv2.circle(image, center, radius, color,linewidth)
"""

"""
#畫橢圓 TBD
ellipse = (0,0,300,100)
cv2.ellipse(image,ellipse,(0,0,255),2)

cv2.ellipse(image,(256,256),(100,50),0,0,180,255,-1)
"""

print('畫多邊形')

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,255,255))

print('畫字')
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV',(100,100), font, 4,(255,255,255),2,cv2.LINE_AA)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)


print('把圖片顯示出來')
cv2.imshow('image', image)

cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

print('建立空白圖片')

import numpy as np
image = np.zeros((512,512,3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv2.line(image,(0,0),(511,511),(255,0,0),5)

print('把圖片顯示出來')
cv2.imshow('image', image)

cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



image = cv2.imread(filename)	#讀取本機圖片


"""

# 寫字
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(image, "AAAAAA", (10, 25), font, 1, (255, 0, 0), 1, cv2.LINE_AA)

# 畫線
cv2.line(image, (0,0), (200,200), (0, 255, 0), 5, lineType=cv2.LINE_AA)


cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
"""

