"""
opencv 集合 新進2

"""

import cv2

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def show():
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


print("------------------------------------------------------------")  # 60個

# 01loadimg.py

import cv2

win_name = "mypicture"  # 窗口名称
# cv2.WINDOW_NORMAL:可以手动调整窗口大小
cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
img = cv2.imread(filename, 0)  # 0 黑白图片；1 原色图片
cv2.imshow(win_name, img)  # 显示图片
cv2.waitKey(0)
cv2.destroyAllWindows()  # 销毁创建的对象

cv2.imwrite("tmp_picture1.mono.pgm", img)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 02opencvmatplotlib.py

import cv2

# 读取图片
img = cv2.imread("tmp_picture1.mono.pgm", 0)  # 黑白图片
plt.imshow(img, cmap="gray", interpolation="bicubic")
plt.xticks([]), plt.yticks([])  # 隐藏 X Y 坐标
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 03drawrectangle.py

import cv2

# Create a black image
img = np.zeros((512, 512, 3))
# Draw a diagonal blue line with thickness of 5 px
# 起点:(0,0),终点:(511,511)，颜色:( 255,0,0)，宽度:2
cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 04drawGeometry.py

import cv2

img = np.zeros((512, 512, 3))
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)  # 矩形
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)  # 圆
cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, 255, -1)  # 椭圆
# 画多边形
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]])
cv2.polylines(img, [pts], True, (0, 255, 255), 1)
# 写入文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 2)
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 05drawcirlcle.py

import cv2

img = np.zeros((512, 512, 3))
# 绘制圆：圆心(255, 255), 半径60, 颜色( 0, 255, 255), 像素1
cv2.circle(img, (255, 150), 60, (0, 255, 255), 2)  # 圆
# 绘制椭圆
# 中心点的位置(255, 255), 短半径50,长半径100
# 360表示整个椭圆；颜色 0, 255, 255；像素2；
cv2.ellipse(img, (255, 350), (100, 50), 0, 0, 360, (255, 255, 0), 2)  # 椭圆
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# haar_face_detect.py

import cv2

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_alt_tree.xml"
picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 识别输入图片中的人脸对象.返回对象的矩形尺寸
# 函数原型detectMultiScale(gray, 1.2,3,CV_HAAR_SCALE_IMAGE,Size(30, 30))
# gray需要识别的图片
# 1.2：表示每次图像尺寸减小的比例
# 3：表示每一个目标至少要被检测到4次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸)
# CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(30, 30)为目标的最小最大尺寸
# faces：表示检测到的人脸目标序列
faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("_tmp_face1.jpg", img)  # 存圖

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# lbp_face_detect.py

import cv2

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/lbpcascades/lbpcascade_frontalface.xml"

picture_filename = "C:/_git/vcs/_4.python/opencv/data/_face/face06.jpg"

face_cascade = cv2.CascadeClassifier(xml_filename)

img = cv2.imread(picture_filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
for x, y, w, h in faces:
    img2 = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 4)
    roi_gray = gray[y : y + h, x : x + w]
    roi_color = img[y : y + h, x : x + w]

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imwrite("_tmp_face2.jpg", img)  # 存圖

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()
