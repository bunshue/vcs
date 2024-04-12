"""
OpenCV 畫圖

cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.polylines

cv2.putText()

cv之繪圖之順序
建立畫布
直線	.line
矩形	.rectangle
圓形	.circle
橢圓形	.ellipse
多邊形	.polylines
文字	.putText

未指明line_width就是1點

"""

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

print('建立畫布(黑色)')
W = 640
H = 480
# 快速產生 WxH，每個項目為 [0,0,0] 的三維陣列
image = np.zeros((H, W,3), dtype='uint8')
#image = np.zeros((H, W,3), np.uint8)
#image = np.ones((H,W,3), np.uint8)*255  # 白色背景

print('畫直線')
color = (0, 0, 255) #B G R
line_width = 10
x1, y1 = 50, 50
x2, y2 = 250, 50
#畫直線 起 終 色 寬
cv2.line(image, (x1, y1), (x2, y2), color, line_width)
cv2.line(image, (x1, y1), (x2, y2), 30)  #無color, 黑色線 1 點
cv2.line(image, (x1, y1+30), (x2, y2+30), (0, 255, 0), 15, lineType=cv2.LINE_AA)

print('畫箭頭')
#畫箭頭 起 終 色 寬
cv2.arrowedLine(image,(x1, y1+60),(x2, y2+60),(0,0,255),5)

print('畫矩形 空心')
color = (0, 0, 255) #B G R
line_width = 5
#畫矩形 左上 右下 色 寬
w, h = 150, 100
#矩形之左上點
x1, y1 = 50, 150
#矩形之右下點
x2, y2 = x1+w, y1+h
cv2.rectangle(image,(x1,y1),(x2,y2),color, line_width)

print('畫矩形 實心')
color = (0, 255, 0) #B G R
line_width = -1
#畫矩形 左上 右下 色 寬(-1, 填滿)
w, h = 150, 100
#矩形之左上點
x1, y1 = 50, 270
#矩形之右下點
x2, y2 = x1+w, y1+h
cv2.rectangle(image,(x1,y1),(x2,y2),color, line_width)#線條寬度為負數 代表實心

print('畫圓形 空心')
cx, cy = 360, 60  # 圓心
radius = 50  # 半徑
color = (0, 255, 255) # 顏色
linewidth = 2 # 線寬
cv2.circle(image, (cx, cy), radius, color, linewidth)  # 繪製圓形

print('畫圓形 實心')
linewidth = -1 #線寬 負值代表實心
cv2.circle(image,(cx, cy), radius // 2, color, linewidth)  # 設定 -1

print('畫橢圓形')
cx, cy = 530, 60  # 橢心
AA, BB = 100, 50  # 長軸 短軸
angle = 0  # 順時鐘旋轉角度
color = (0, 0, 255)
linewidth = 5 #線條寬度, 負數代表實心

#畫橢圓              中心  長軸 短軸 旋轉  開始 結束角度 顏色 線寬
cv2.ellipse(image, (cx, cy), (AA, BB), angle, 0, 360, color, linewidth) #空心
cv2.ellipse(image, (cx, cy), (AA//2, BB//2), angle, 0, 360, color, -1)  #實心
cv2.ellipse(image, (530, 120), (100, 50),0,0,180,255,-1)#藍色半橢圓

print('# 改一塊顏色')
image[400:450, 50:100] = [0,0,255]

print('畫多邊形')

#設定頂點座標
x_st, y_st = 350, 200
dd = 50
px1, py1 = x_st, y_st
px2, py2 = x_st-dd, y_st+dd
px3, py3 = x_st-dd, y_st+dd*2
px4, py4 = x_st, y_st+dd*3
px5, py5 = x_st+dd, y_st+dd*2
px6, py6 = x_st+dd, y_st+dd

pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6]])
#pts = np.array([[px1, py1], [px2, py2], [px3, py3], [px4, py4], [px5, py5], [px6, py6]], np.int32)

cv2.polylines(image, [pts], True, (255, 0, 0), 2)   #True表示封口
#True: 頭尾相連, False: 頭尾不相連

print('畫多邊形')
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(0,255,255))

"""
pts = np.array([[150,50],[250,100],[150,250],[50,100]])   # 產生座標陣列
#畫多邊形 空心
cv2.polylines(image,[pts],True,(0,0,255),5)   # 繪製多邊形

#畫多邊形 實心
cv2.fillPoly(image,[pts],(0,0,255))
"""

cv2.imshow('OpenCV Draw 1', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print('建立畫布(黑色)')
W = 640
H = 480
# 快速產生 WxH，每個項目為 [0,0,0] 的三維陣列
image = np.zeros((H, W,3), dtype='uint8')

#寫字1
text = 'Hello'
x_st, y_st = 450, 400
fontFace = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 2.5
color = (0,0,255)
thickness = 5
lineType = cv2.LINE_AA
cv2.putText(image, text, (x_st, y_st), fontFace, fontScale, color, thickness, lineType)

# 寫字2
text = 'Hello'
x_st, y_st = 450, 400+50
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
color = (0,0,255)
thickness = 1
lineType = cv2.LINE_AA
cv2.putText(image, text, (x_st, y_st), font, 1, color, thickness, lineType)

#寫字3
from PIL import ImageFont, ImageDraw, Image    # 載入 PIL 相關函式庫
x_st, y_st = 450, 200
#font_filename = 'NotoSansTC-Regular.otf'          # 設定字型路徑
font = ImageFont.truetype(font_filename, 50)      # 設定字型與文字大小
imagePil = Image.fromarray(image)                # 將 image 轉換成 PIL 影像
draw = ImageDraw.Draw(imagePil)                # 準備開始畫畫
draw.text((x_st, y_st), '大家好～\n嘿嘿嘿～', fill=(255, 255, 0), font=font)  # 畫入文字，\n 表示換行
image = np.array(imagePil)                       # 將 PIL 影像轉換成 numpy 陣列












cv2.imshow('OpenCV Draw 2', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



print('------------------------------------------------------------')	#60個

print('建立畫布(白色)')
W, H = 1200, 800
image = np.ones((H,W,3),dtype="uint8")*255  # 白色背景

font=cv2.FONT_HERSHEY_SIMPLEX

x_st, y_st = 0, 100
cv2.putText(image,'OpenCV 1',(x_st, y_st),font, 3,(0,0,255),15)
y_st += 80
cv2.putText(image,'OpenCV 2',(x_st, y_st),font, 3,(0,255,0),5)
y_st += 80
cv2.putText(image,'OpenCV 3',(x_st, y_st),font, 3,(0,0,255),15)
y_st += 80
cv2.putText(image,'OpenCV 4',(x_st, y_st),font, 3,(0,255,0),15, cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,True)

font = cv2.FONT_HERSHEY_SIMPLEX
y_st += 80
cv2.putText(image,'OpenCV 5',(x_st, y_st), font, 4,(255,0,255),2,cv2.LINE_AA)

font=cv2.FONT_HERSHEY_SIMPLEX
y_st += 80
cv2.putText(image,'OpenCV 6',(x_st, y_st), font, 1,(0,255,0),3)

font = cv2.FONT_HERSHEY_SIMPLEX
y_st += 80
cv2.putText(image, 'OpenCV 7', (x_st, y_st), font, 6, (255, 255, 0), 10, cv2.LINE_AA)

cv2.imshow("OpenCV Draw 3",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

W = 512 + 200
H = 512

#建立 512x512 的黑色畫布
image = np.zeros((H, W, 3), dtype = np.uint8)  #H, W
#用(B, G, R) = (255, 255, 255): 白色填滿畫布
image.fill(255) #將這個矩陣全部填入255 => 白色
#image[:] = [48, 213, 254]#將這個矩陣全部填入指定顏色
# Fill image with gray color(set each pixel to gray)
#image[:] = (128, 128, 128)

print('------------------------------------------------------------')	#60個

font = cv2.FONT_HERSHEY_SIMPLEX
line_type = cv2.LINE_AA #文字線條樣式

#畫字時, 起點是左下角

print('畫字')
text = 'Hello, World!'
x_st = 20
y_st = 80
font_size = 1 #文字縮放比例
color = (0, 0, 255) #B G R
line_width = 1
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width)
y_st += 30
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)

print('------------------------------------------------------------')	#60個

text = "ABCDEFGHIJK"
x_st = 20
y_st = 40
font_size = 1 #文字縮放比例
color = (0, 255, 0) #B G R
line_width = 1
cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)

print('------------------------------------------------------------')	#60個

print('寫在正中央, 先量測字體大小')
text = 'Hello, World!'
x_st = 20
y_st = 200
font = cv2.FONT_HERSHEY_COMPLEX
font_size = 2 #文字縮放比例
color = (255, 0, 0) #B G R
line_width = 2
text_size = cv2.getTextSize(text, font, font_size, line_width)
print('字體大小 : ', text_size)
w = text_size[0][0]
h = text_size[0][1]
x_st = W // 2 - w // 2
y_st = H // 2 + h // 2
print(x_st, y_st)

cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)  #預設, False
#cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type, False)    #False: 從左上畫起
#cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type, True)     #True:  從左下畫起
cv2.rectangle(image, (x_st, y_st), (x_st + w, y_st - h), (0, 0, 255), 2)

print('------------------------------------------------------------')	#60個

fonts = [
    cv2.FONT_HERSHEY_SIMPLEX,
    cv2.FONT_HERSHEY_PLAIN,
    cv2.FONT_HERSHEY_DUPLEX,
    cv2.FONT_HERSHEY_COMPLEX,
    cv2.FONT_HERSHEY_TRIPLEX,
    cv2.FONT_HERSHEY_COMPLEX_SMALL,
    cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
    cv2.FONT_HERSHEY_SCRIPT_COMPLEX
]

text = 'OpenCV'
x_st = 450
y_st = 50
font_size = 2 #文字縮放比例
color = (0, 0, 0)   #B G R
line_width = 1
for font in fonts:
    cv2.putText(image, text, (x_st, y_st), font, font_size, color, line_width, line_type)
    y_st += 60
    
cv2.imshow('OpenCV Draw 4', image)
cv2.waitKey(0)
cv2.destroyAllWindows() #銷毀建立的物件

print('------------------------------------------------------------')	#60個

print('建立畫布(黑色)')

W, H = 800, 600
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), dtype = np.uint8)
image[:] = (200, 200, 200)  #將所有點著色

print('畫標示頁箋')

#用 putText 繪製物件偵測的標籤
def drawBoundingBox(image, bboxs):
    for box in bboxs:
        x1, y1, x2, y2 = (box['x1'], box['y1'], box['x2'], box['y2'])
        label = box['label']
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 6)
        fontFace = cv2.FONT_HERSHEY_COMPLEX
        fontScale = 0.5
        thickness = 1
        labelSize = cv2.getTextSize(label, fontFace, fontScale, thickness)
        _x1 = x1 # bottomleft x of text
        _y1 = y1 # bottomleft y of text
        _x2 = x1 + labelSize[0][0] # topright x of text
        _y2 = y1 - labelSize[0][1] # topright y of text
        cv2.rectangle(image, (_x1, _y1), (_x2, _y2), (0, 255, 0), cv2.FILLED) # text background
        cv2.putText(image, label, (x1, y1), fontFace, fontScale, (0, 0, 0), thickness)
    return image

def draw_line(image):
    H = image.shape[0]
    W = image.shape[1]
    print(image.shape)
    print(H//100)
    print(W//100)
    for i in range(H//100 + 1):
        cv2.line(image, (0, 100*i), (W, 100*i), (0, 0, 100), 2) #畫線 水平線 R

    for i in range(W//100 + 1):
        cv2.line(image, (100*i, 0), (100*i, H), (0, 100, 0), 2, lineType=cv2.LINE_AA) #畫線 垂直線 G
"""
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

draw_line(image)

cv2.imshow('OpenCV Draw 1', image)
cv2.waitKey(0)
cv2.destroyAllWindows() #銷毀建立的物件
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
#有底圖作畫
filename = 'C:/_git/vcs/_4.python/_data/elephant.jpg'
image = cv2.imread(filename)	#讀取本機圖片
"""

#cv2.namedWindow("plot")





print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

