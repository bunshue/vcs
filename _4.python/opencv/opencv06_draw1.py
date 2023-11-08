'''
OpenCV 畫圖

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

import time

print('------------------------------------------------------------')	#60個

print('OpenCV 畫圖')
# 無底圖作畫
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), dtype = np.uint8)

image[:] = (128, 128, 128)  #將所有點著色

#有底圖作畫
filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
image = cv2.imread(filename)	#讀取本機圖片

#-----------------------------------------------------------------------------
#cv2.namedWindow("plot")
#-----------------------------------------------------------------------------
print('畫直線')
x1, y1 = 20, 20
x2, y2 = 300, 20

color = (0, 0, 255) #B G R
line_width = 4

cv2.line(image, (x1, y1), (x2, y2), color, line_width)
cv2.line(image, (x1, y1), (x2, y2 + 100), line_width)  #無color, 黑色線 1 點

print('------------------------------------------------------------')	#60個

print('畫矩形')
x1, y1 = 20, 40
x2, y2 = 300, 140

color = (0, 255, 0) #B G R
line_width = 2
#畫矩形, 空心 2
cv2.rectangle(image, (x1, y1), (x2, y2), color, line_width)

dy = 120
x1, y1 = x1, y1 + dy
x2, y2 = x2, y2 + dy
#畫矩形, 實心 -1
cv2.rectangle(image, (x1, y1), (x2, y2), (234, 151, 102), -1)#線條寬度為負數 代表實心

print('------------------------------------------------------------')	#60個
print('畫圓')
cx = int(W / 2)
cy = int(H / 2)
r = 100
color = (255, 255, 0)  #B G R
line_width = 2

#畫圓形, 空心 2
cv2.circle(image, (cx, cy), r, color, line_width)

#畫圓形, 實心 -1
color = (255, 255, 0)  #B G R
cv2.circle(image, (cx, cy), r // 3, color, -1)

print('------------------------------------------------------------')	#60個
print('畫橢圓')
cx = 200 #中心x
cy = 400 #中心y
a = 200 #長軸
b = 100 #短軸
angle = 0  #旋轉角度
color = (0, 0, 255)
linewidth = 5
linewidth = 5 #線條寬度, 負數代表實心
#畫橢圓              中心  長軸 短軸 旋轉  開始 結束角度 顏色 線寬
cv2.ellipse(image, (cx, cy), (a, b), angle, 0, 360, color, linewidth) #空心
cv2.ellipse(image, (cx, cy), (a//2, b//2), angle, 0, 360, color, -1)  #實心

print('------------------------------------------------------------')	#60個
print('畫多邊形')
px1 = int(W / 2)
py1 = 0
px2 = BORDER
py2 = BORDER
px3 = 0
py3 = int(H / 2)
px4 = BORDER
py4 = H - BORDER
px5 = int(W / 2)
py5 = H
px6 = W - BORDER
py6 = H - BORDER
px7 = W
py7 = int(H / 2)
px8 = W - BORDER
py8 = BORDER
pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6], [px7, py7], [px8, py8]])
cv2.polylines(image, [pts], True, (255, 255, 0), 2)   #True表示封口
#True: 頭尾相連, False: 頭尾不相連
#-----------------------------------------------------------------------------
'''
pts = np.array([[300, 300], [300, 340], [350,320]], np.int32)
cv2.polylines(image, [pts], True, (0, 255, 255), 2)
'''

#設定頂點座標
pts = np.array(((10, 5), (100, 100), (170, 120), (200, 50)))
#True:頭尾相連; False:頭尾不相連
cv2.polylines(image, [pts], True, (105, 105, 105), 2)

print('------------------------------------------------------------')	#60個
print('畫標示頁箋')

#用 putText 繪製物件偵測的標籤

def drawBoundingBox(img, bboxs):
    for box in bboxs:
        x1, y1, x2, y2 = (box['x1'], box['y1'], box['x2'], box['y2'])
        label = box['label']
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 6)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        thickness = 1
        labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
        _x1 = x1 # bottomleft x of text
        _y1 = y1 # bottomleft y of text
        _x2 = x1 + labelSize[0][0] # topright x of text
        _y2 = y1 - labelSize[0][1] # topright y of text
        cv2.rectangle(img, (_x1, _y1), (_x2, _y2), (0, 255, 0), cv2.FILLED) # text background
        cv2.putText(img, label, (x1, y1), fontFace, fontScale, (0, 0, 0), thickness)
    return img

bboxs = []
box = {}
box['label'] = 'object 1'
box['x1'] = 40
box['y1'] = 40
box['x2'] = 180
box['y2'] = 180
bboxs.append(box)
box2 = {'label' : 'object 2', 'x1' : 300, 'y1' : 200, 'x2' : 600, 'y2' : 440}
bboxs.append(box2)
drawBoundingBox(image, bboxs)

print('------------------------------------------------------------')	#60個

#-----------------------------------------------------------------------------
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)
#-----------------------------------------------------------------------------
print('存圖')
filename = 'C:/_git/vcs/_1.data/______test_files2/image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.bmp'
cv2.imwrite(filename, image)
#-----------------------------------------------------------------------------
print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------

