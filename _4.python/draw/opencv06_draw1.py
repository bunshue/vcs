
"""
OpenCV 畫圖

OpenCV 畫圖, 寫字集合


cv2.line()
cv2.circle()
cv2.rectangle()
cv2.ellipse()
cv2.putText()
cv2.polylines


"""

import cv2
import time

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

print('OpenCV 畫圖')
# 無底圖作畫
print('設定圖片大小')
W = 800
H = 600
BORDER = 100
#image = np.zeros((H, W, 3))
image = np.zeros((H, W, 3), dtype = np.uint8)

image[:] = (200, 200, 200)  #將所有點著色

"""
#有底圖作畫
filename = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
image = cv2.imread(filename)	#讀取本機圖片
"""

#-----------------------------------------------------------------------------
#cv2.namedWindow("plot")
#-----------------------------------------------------------------------------

print('畫直線')

color = (0, 0, 255) #B G R
line_width = 4

x1, y1 = 100, 100
x2, y2 = 500, 100

cv2.line(image, (x1, y1), (x2, y2), color, line_width)
cv2.line(image, (x1, y1+20), (x2, y2 + 20), line_width)  #無color, 黑色線 1 點

print('------------------------------------------------------------')	#60個

print('畫矩形')
x1, y1 = 100, 100
x2, y2 = 300, 200

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

print('------------------------------------------------------------')	#60個

n = 300
image = np.zeros((n+1,n+1,3), np.uint8)
image = cv2.line(image,(0,0),(n,n),(255,0,0),3)
image = cv2.line(image,(0,100),(n,100),(0,255,0),1)
image = cv2.line(image,(100,0),(100,n),(0,0,255),6)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
#plt.title('xxxx')
plt.show()

print('------------------------------------------------------------')	#60個

n = 300
image = np.ones((n,n,3), np.uint8)*255
image = cv2.rectangle(image,(50,50),(n-100,n-50),(0,0,255),-1)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
#plt.title('xxxx')
plt.show()

print('------------------------------------------------------------')	#60個

thickness=-1
mode=1
d=400
def draw_circle(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        a=np.random.randint(1,d-50)
        r=np.random.randint(1,d/5)
        angle = np.random.randint(0,361)
        color = np.random.randint(0,high = 256,size = (3,)).tolist()
        if mode==1:
            cv2.rectangle(img,(x,y),(a,a),color,thickness)
        elif mode==2:
            cv2.circle(img,(x,y),r,color,thickness)
        elif mode==3:
            cv2.line(img,(a,a),(x,y),color,3)  
        elif mode==4:
            cv2.ellipse(img, (x,y), (100,150), angle, 0, 360,color,thickness)                  
        elif mode==5:
            cv2.putText(img,'OpenCV',(0,round(d/2)), 
                        cv2.FONT_HERSHEY_SIMPLEX, 2,color,5)    
img=np.ones((d,d,3),np.uint8)*255
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)
while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(1)&0xFF
    if k==ord('r'):
        mode=1
    elif k==ord('c'):
        mode=2
    elif k==ord('l'):
        mode=3
    elif k==ord('e'):
        mode=4
    elif k==ord('t'):
        mode=5
    elif k==ord('f'):
        thickness=-1
    elif k==ord('u'):
        thickness=3
    elif k==27:
        break   

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

print('------------------------------------------------------------')	#60個
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
#繪製顯示系統當前時間
localtime = time.localtime()
text = time.strftime("%Y-%m-%d %I:%M:%S %p", localtime)
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
print('------------------------------------------------------------')	#60個
print('把圖片顯示出來')
cv2.imshow('OpenCV Draw Picture', image)
#-----------------------------------------------------------------------------
print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件
#-----------------------------------------------------------------------------

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,200),font, 3,(0,255,0),5)
cv2.imshow("demo19.7",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

d = 400
img = np.ones((d,d,3),dtype="uint8")*255
#生成白色背景
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(0,150),font, 3,(0,0,255),15)
cv2.putText(img,'OpenCV',(0,250),font, 3,(0,255,0),15,
            cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,True)
cv2.imshow("demo19.7",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

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


