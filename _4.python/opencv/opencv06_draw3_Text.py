"""
OpenCV 畫圖

OpenCV 畫圖, 寫字集合

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

import time

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

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

