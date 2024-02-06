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


img = cv2.line(image, (0, 0), (width, height), (255, 0, 0), 5)
img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
img = cv2.rectangle(img, (0, 0), (width-10, height-10), (128, 128, 128), 5)

img = cv2.circle(img, (100, 100), 100, (0, 0, 255))
img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCV', (10, height - 100), font, 6, (0, 0, 255), 10, cv2.LINE_AA)

print('把圖片顯示出來')
cv2.imshow('image', img)

