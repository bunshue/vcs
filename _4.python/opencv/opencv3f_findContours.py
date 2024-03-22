"""

cv2.findContours
cv2.drawContours


圖片邊緣檢測

圖片轉換成灰階Grayscale的部分，
利用Canny邊緣檢測使用多階段算法來檢測圖像中的各種邊緣。

OpenCV具有findContour()幫助從圖像中提取輪廓的功能。

再來就把所有輪廓繪製起來，最後show出圖片 利用imshow語法。


"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

# BGR
color = [
    (0, 0, 255),  # 紅色, Red
    (0, 255, 0),  # 草綠色, Lime
    (255, 0, 0),  # 藍色, Blue
    (0, 255, 255),  # 黃色, Yellow
    (255, 0, 255),  # 品紅色, Fuchsia Magenta
    (255, 255, 0),  # 青色或水色, Cyan / Aqua
    (0, 0, 0),  # 黑色, Black
    (255, 255, 255),  # 白色, White
    (0, 0, 128),  # 栗色, Maroon
    (0, 128, 128),  # 橄欖綠, Olive
    (0, 128, 0),  # 綠色, Green
    (128, 128, 0),  # 藍綠色, Teal
    (128, 0, 0),  # 藏青色, Navy
    (128, 0, 128),  # 紫色, Purple
    (192, 192, 192),  # 銀色, Silver
    (128, 128, 128),  # 灰色, Gray
]

print("------------------------------------------------------------")  # 60個

# coin.jpg用圖片先處理方法一
filename = "images/coin.jpg"

# opencv05_dilate_erode1.png用圖片先處理方法二
# filename = 'C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png'

# 讀圖片的方法一
cap = cv2.VideoCapture(filename)  # 用VideoCapture讀取本機圖片
ret, image1 = cap.read()

# 讀圖片的方法二
image1 = cv2.imread(filename)

# 轉灰階
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)


# 圖片先處理方法一
image1_gray = cv2.GaussianBlur(image1_gray, (13, 13), 0)  # 執行高斯模糊化
edged = cv2.Canny(image1_gray, 50, 150)
contours, hierarchy = cv2.findContours(
    edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)


"""
#圖片先處理方法二
ret,thresh = cv2.threshold(image1_gray,127,255,0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
"""

print(type(contours))
print(len(contours))
# print(contours)

image2 = image1.copy()

linewidth = 10  # 線寬
# linewidth = -1 #填充模式

# 一起畫
# index = -1 # 指名要繪製的輪廓, -1代表全部
# image2=cv2.drawContours(image2,contours,index,(0,0,255),linewidth)  # image2為三通道才能顯示輪廓, 用紅框標示出來

# 分開畫
length = len(contours)
for index in range(length):
    image2 = cv2.drawContours(
        image2, contours, index, color[index % 9], linewidth
    )  # image2為三通道才能顯示輪廓

plt.figure("drawContours", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("尋找 Contours")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "images/poly.png"

print("顯示圖片")
image = cv2.imread(filename)  # 讀取本機圖片

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(211)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

shape = image.shape
h = shape[0]  # 高
w = shape[1]  # 寬
h, w, d = image.shape  # d為dimension d=3 全彩 d=1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)
contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

RECT, HEXAGON = 0, 1

print("=== 處理前")
print("矩形點數量：{}".format(len(contours[RECT])))
print("六邊形點數量：{}".format(len(contours[HEXAGON])))

approx_rect = cv2.approxPolyDP(contours[RECT], 30, True)
approx_hex = cv2.approxPolyDP(contours[HEXAGON], 30, True)

print("=== 處理後")
print("矩形點數量：{}".format(len(approx_rect)))
cv2.drawContours(image, [approx_rect], -1, (0, 0, 255), 5)

print("六邊形點數量：{}".format(len(approx_hex)))
cv2.drawContours(image, [approx_hex], -1, (0, 0, 255), 5)
print(approx_hex)
for i in range(len(approx_hex)):
    print(approx_hex[i])

plt.subplot(212)
plt.title("image")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# 多邊形凹凸點計算

import cv2

filename = "data/star.png"

print("顯示圖片")
image = cv2.imread(filename)  # 讀取本機圖片

shape = image.shape
h = shape[0]  # 高
w = shape[1]  # 寬
h, w, d = image.shape  # d為dimension d = 3 全彩 d = 1 灰階
print("寬 = ", w, ", 高 = ", h, ", D = ", d)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 50, 150)
edged = cv2.dilate(edged, None, iterations=1)
contours, hierarchy = cv2.findContours(
    edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

cnt = contours[0]
cnt = cv2.approxPolyDP(cnt, 30, True)
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("凸點數量：{}".format(len(hull)))
print("凹點數量：{}".format(len(defects)))

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(image, start, end, (0, 255, 0), 2)
    cv2.circle(image, far, 5, (0, 0, 255), -1)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"

image = cv2.imread(filename)

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(232)
plt.title("gray")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

edged = cv2.Canny(gray, 30, 200)

plt.subplot(233)
plt.title("Canny Edges")
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

plt.subplot(234)
plt.title("Canny Edges After Contouring")
plt.imshow(cv2.cvtColor(edged, cv2.COLOR_BGR2RGB))

print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (255, 0, 0), 2)

plt.subplot(235)
plt.title("Contours")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
