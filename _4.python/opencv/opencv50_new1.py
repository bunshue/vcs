"""
opencv 集合

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

print("------------------------------------------------------------")  # 60個
'''
print('練習組合成一張大圖 picasa效果')

filename1 = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename2 = "C:/_git/vcs/_4.python/_data/bear.jpg"
filename3 = "C:/_git/vcs/_4.python/_data/panda.jpg"

ratio = 3

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)
image3 = cv2.imread(filename3)
print(image1.shape)

image1 = cv2.resize(image1, (image1.shape[1]//ratio, image1.shape[0]//ratio))
image2 = cv2.resize(image2, (image2.shape[1]//ratio, image2.shape[0]//ratio))
image3 = cv2.resize(image3, (image3.shape[1]//ratio, image3.shape[0]//ratio))
print(image1.shape)

output = np.zeros((768, 1024, 3), dtype='uint8')         # 設定合成的影像為一張全黑的畫布

x_st = 50
y_st = 50
w, h = image1.shape[1], image1.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image1[0:h, 0:w]      # 設定 output 的某個區域為即時影像 img 的某區域


x_st = 300
y_st = 200
w, h = image2.shape[1], image2.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image2[0:h, 0:w]      # 設定 output 的某個區域為即時影像 img 的某區域


x_st = 150
y_st = 300
w, h = image3.shape[1], image3.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image3[0:h, 0:w]      # 設定 output 的某個區域為即時影像 img 的某區域


plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()



"""

    img = cv2.flip(img, 1)                        # 翻轉影像，使其如同鏡子
    img = img[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

"""

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/_data/picture_mix1.bmp"
filename2 = "C:/_git/vcs/_4.python/_data/picture_mix2.bmp"

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)

print("兩圖直接相加")
result1 = image1 + image2

print("兩圖用cv相加")
result2 = cv2.add(image1, image2)

print("兩圖做alpha疊加")
result3 = cv2.addWeighted(image1, 0.7, image2, 0.3, 0)

plt.figure(
    num="相加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("兩圖直接相加")
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("兩圖用cv相加")
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("兩圖做alpha疊加")
plt.imshow(cv2.cvtColor(result3, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp"
lena = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dollar.bmp"
dollar = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="疊加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

print("兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之")
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[160:340, 200:300] = add

plt.subplot(133)
plt.title("兩圖擷取某塊做alpha疊加, 再貼回原圖")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
image1 = cv2.imread(filename)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

print(image1.shape)
print(image2.shape)

# 建立mask
mask = np.zeros(image1.shape[:2], np.uint8)
bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (50, 50, 400, 400)
cv2.grabCut(image1, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

image3 = image1 * mask2[:, :, np.newaxis]
image4 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)

plt.figure(
    num="new06",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.imshow(image2)

plt.subplot(222)
plt.imshow(mask)

plt.subplot(223)
plt.imshow(mask2)

plt.subplot(224)
plt.imshow(image4)

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
o = cv2.imread(filename)

image2 = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2], np.uint8)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)
cv2.grabCut(o, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)

mask2 = cv2.imread("images/mask.png", 0)
mask2Show = cv2.imread("images/mask.png", -1)

m2rgb = cv2.cvtColor(mask2Show, cv2.COLOR_BGR2RGB)
mask[mask2 == 0] = 0
mask[mask2 == 255] = 1
mask, bgd, fgd = cv2.grabCut(o, mask, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")
ogc = o * mask[:, :, np.newaxis]
ogc = cv2.cvtColor(ogc, cv2.COLOR_BGR2RGB)

plt.figure(
    num="new07",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(m2rgb)

plt.subplot(122)
plt.imshow(ogc)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
o = cv2.imread(filename)

image2 = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)

mask2 = np.zeros(o.shape[:2], np.uint8)
mask2[30:512, 50:400] = 3
mask2[50:300, 150:200] = 1
cv2.grabCut(o, mask2, None, bgd, fgd, 5, cv2.GC_INIT_WITH_MASK)
mask2 = np.where((mask2 == 2) | (mask2 == 0), 0, 1).astype("uint8")
ogc = o * mask2[:, :, np.newaxis]
ogc = cv2.cvtColor(ogc, cv2.COLOR_BGR2RGB)

plt.figure(
    num="new08",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(image2)

plt.subplot(122)
plt.imshow(ogc)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename, 0)

image2 = image.copy()
template = cv2.imread("images/temp.bmp", 0)
th, tw = template.shape[::]
image = image2.copy()
rv = cv2.matchTemplate(image, template, cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

# 矩形之左上點
topLeft = minLoc
# 矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(image, topLeft, bottomRight, 255, 2)

plt.figure(
    num="Matching Result 1",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(rv, cmap="gray")
plt.title("Matching Result")

plt.subplot(122)
plt.imshow(image, cmap="gray")
plt.title("Detected Point")

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename, 0)

image2 = image.copy()
template = cv2.imread("images/temp.bmp", 0)

tw, th = template.shape[::-1]
image = image2.copy()
rv = cv2.matchTemplate(image, template, cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)

# 矩形之左上點
topLeft = maxLoc
# 矩形之右下點
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(image, topLeft, bottomRight, 255, 2)

plt.figure(
    num="Matching Result 2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(rv, cmap="gray")
plt.title("Matching Result")

plt.subplot(122)
plt.imshow(image, cmap="gray")
plt.title("Detected Point")

plt.show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("images/lena4.bmp", 0)
template = cv2.imread("images/lena4Temp.bmp", 0)

w, h = template.shape[::-1]
res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(image, pt, (pt[0] + w, pt[1] + h), 255, 1)

plt.figure(
    num="Image",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.imshow(image, cmap="gray")

plt.show()
'''
print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
image = cv2.imread(filename)

H, W, D = image.shape

x = 50
y = 50
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("move")
plt.imshow(cv2.cvtColor(move, cv2.COLOR_BGR2RGB))

plt.suptitle('影像移動')
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename)

H, W, D = image.shape

p1 = np.float32([[0, 0], [W - 1, 0], [0, H - 1]])
p2 = np.float32([[0, H * 0.33], [W * 0.85, H * 0.25], [W * 0.15, H * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(image, M, (W, H))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("AffineTransform")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.suptitle("AffineTransform")
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/demo.bmp"
image = cv2.imread(filename)

H, W, D = image.shape

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure(
    num="new11",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

# Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename)

print("filter2D 效果")
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure(
    num="new26 filter2D 效果",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("filter2D 效果")
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"
image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)  # 水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)  # 垂直值一樣, 偵測垂直的邊緣

print("filter2D 效果")

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure(
    num="new27",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Prewitt_horizon")
# 躺平的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Prewitt_vertical")
# 直放的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個


def saltpepper(image, n):
    m = int((image.shape[0] * image.shape[1]) * n)
    for a in range(m):
        i = int(np.random.random() * image.shape[1])
        j = int(np.random.random() * image.shape[0])
        if image.ndim == 2:
            image[j, i] = 255
        elif image.ndim == 3:
            image[j, i, 0] = 255
            image[j, i, 1] = 255
            image[j, i, 2] = 255
    for b in range(m):
        i = int(np.random.random() * image.shape[1])
        j = int(np.random.random() * image.shape[0])
        if image.ndim == 2:
            image[j, i] = 0
        elif image.ndim == 3:
            image[j, i, 0] = 0
            image[j, i, 1] = 0
            image[j, i, 2] = 0
    return image


# 上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image0 = cv2.imread(filename)
image = cv2.imread(filename)

print("saltpepper 效果")
saltImage = saltpepper(image, 0.02)

plt.figure(
    num="new28 saltpepper 效果",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("saltpepper 效果")
plt.imshow(cv2.cvtColor(saltImage, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename)

threshold = 127
print("二值化")

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t, rst = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
# t, rst = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY_INV)
# t, rst = cv2.threshold(image, threshold, 255, cv2.THRESH_TRUNC)
# t, rst = cv2.threshold(image, threshold, 255, cv2.THRESH_TOZERO_INV)
# t, rst = cv2.threshold(image, threshold, 255, cv2.THRESH_TOZERO)

plt.figure(
    num="new29 二值化",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("二值化圖, 閥值 = " + str(threshold) + ", 小於變全黑, 大於變全白")
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg"
image = cv2.imread(filename, 0)

t1, thd = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
athdMEAN = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 5
)
athdGAUS = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 5
)

plt.figure(
    num="new30",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("thd")
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("athdMEAN")
plt.imshow(cv2.cvtColor(athdMEAN, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("athdGAUS")
plt.imshow(cv2.cvtColor(athdGAUS, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp"
image = cv2.imread(filename, 0)

t1, thd = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(
    num="new31",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("thd")
plt.imshow(cv2.cvtColor(thd, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("otsu")
plt.imshow(cv2.cvtColor(otsu, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

print("原圖 彩色")
image = cv2.imread(filename)

print("原圖 彩色 轉 灰階1通道")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print("gray.shape=", gray.shape)

print("灰階 轉 BGR3通道")
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
print("rgb.shape=", rgb.shape)

plt.figure(
    num="new32 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖 彩色")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("灰階1通道")
plt.imshow(cv2.cvtColor(gray, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("BGR3通道")
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
image = cv2.imread(filename)

print("原圖 BGR 轉 RGB")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(
    num="new33 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖 B-G-R OK")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("原圖 BGR 轉 RGB NG")
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"
image = cv2.imread(filename)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
v[:, :] = 255
newHSV = cv2.merge([h, s, v])
art = cv2.cvtColor(newHSV, cv2.COLOR_HSV2BGR)

plt.figure(
    num="new35 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("art")
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
image = cv2.imread(filename)

bgra = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra)
a[:, :] = 125
bgra125 = cv2.merge([b, g, r, a])
a[:, :] = 0
bgra0 = cv2.merge([b, g, r, a])

plt.figure(
    num="new36 影像處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("bgra")
plt.imshow(cv2.cvtColor(bgra, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("bgra125")
plt.imshow(cv2.cvtColor(bgra125, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("bgra0")
plt.imshow(cv2.cvtColor(bgra0, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename, 0)

plt.figure(
    num="new37 修改一部份資料",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("修改一部份資料 1")
for i in range(20, 60):  # y
    for j in range(20, 100):  # x
        image[i, j] = 255

print("修改一部份資料 2")
# 測試讀取、修改單個像素值
print("讀取像素點image.item(3,2)=", image.item(3, 2))
image.itemset((3, 2), 255)
print("修改後像素點image.item(3,2)=", image.item(3, 2))
# 測試修改一個區域的像素值
for i in range(100, 200):  # y
    for j in range(20, 60):  # x
        image.itemset((i, j), 220)

plt.subplot(222)
plt.title("修改後的圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("------------------------------")  # 30個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
image = cv2.imread(filename)

plt.subplot(223)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("讀取image[0,0]=", image[0, 0])
print("讀取image[0,0,0]=", image[0, 0, 0])
print("讀取image[0,0,1]=", image[0, 0, 1])
print("讀取image[0,0,2]=", image[0, 0, 2])
print("讀取image[50,0]=", image[50, 0])
print("讀取image[100,0]=", image[100, 0])
# 區域1
for i in range(0, 50):
    for j in range(0, 100):
        for k in range(0, 3):
            image[i, j, k] = 255  # 白色
# 區域2
for i in range(50, 100):
    for j in range(0, 100):
        image[i, j] = [128, 128, 128]  # 灰色
# 區域3
for i in range(100, 150):
    for j in range(0, 100):
        image[i, j] = 0  # 黑色
# 區域4
print("讀取image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("讀取image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("讀取image.item(0, 0, 2) = ", image.item(0, 0, 2))
for i in range(200, 250):
    for j in range(0, 100):
        for k in range(0, 3):
            image.itemset((i, j, k), 255)  # 白色

print("修改後image.item(0, 0, 0) = ", image.item(0, 0, 0))
print("修改後image.item(0, 0, 1) = ", image.item(0, 0, 1))
print("修改後image.item(0, 0, 2) = ", image.item(0, 0, 2))
print("修改後image[0, 0] = ", image[0, 0])
print("修改後image[0, 0, 0] = ", image[0, 0, 0])
print("修改後image[0, 0, 1] = ", image[0, 0, 1])
print("修改後image[0, 0, 2] = ", image[0, 0, 2])
print("修改後image[50, 0] = ", image[50, 0])
print("修改後image[100, 0] = ", image[100, 0])

plt.subplot(224)
plt.title("修改後的圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
a = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="new38 擷取一塊處理",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print("擷取一塊出來, 並顯示之")
face = a[200:400, 200:380]  # h, w

plt.subplot(232)
plt.title("擷取一塊出來")
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))

print("將其中一塊亂碼化, 並顯示之")
x_st = 50
y_st = 50
w = 100
h = 180
face = np.random.randint(0, 256, (h, w, 3))
a[y_st : y_st + h, x_st : x_st + w] = face

plt.subplot(233)
plt.title("將其中一塊亂碼化")
plt.imshow(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))

print("------------------------------")  # 30個

# A圖
filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp"
lena = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)

# A圖抓一塊貼到B圖上
plt.subplot(234)
plt.title("原圖")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

# B圖
filename2 = "C:/_git/vcs/_4.python/_data/picture1.jpg"
peony = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

plt.subplot(235)
plt.title("原圖")
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

print("A圖抓一塊貼到B圖上")
face = lena[220:400, 250:350]
peony[160:340, 200:300] = face

plt.subplot(236)
plt.title("顯示修改後的圖")
plt.imshow(cv2.cvtColor(peony, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

print("裁剪圖片a")

image = cv2.imread(r"images/sample.jpg")

H = image.shape[0]
W = image.shape[1]
print("H * W =", image.shape)
print("H =", H)
print("W =", W)

print("裁剪圖片b")

# image_cut = image[0:(H * 2 // 3), 0:(W * 2 // 3)]
image_cut = image[0 : (H * 1 // 2), 0 : (W * 1 // 2)]
print(image_cut.shape)

plt.imshow(cv2.cvtColor(image_cut, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("圖片翻轉 原圖")

image = cv2.imread(r"images/sample.jpg")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print("圖片翻轉 效果")

image_flip = cv2.flip(image, -999)
image_flip2 = cv2.flip(image, -88)

plt.imshow(cv2.cvtColor(image_flip, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("圖片色彩空間的轉換")

image = cv2.imread(r"images/sample.jpg")
image_convert = cv2.cvtColor(image, cv2.COLOR_BGR2Lab)
plt.imshow(cv2.cvtColor(image_convert, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

# OpenCV 進階圖片處理功能

print("圖片的二值化處理")
image = cv2.imread(r"images/sample.jpg")
thr, image_binary = cv2.threshold(image, 192, 255, cv2.THRESH_TOZERO)

plt.imshow(cv2.cvtColor(image_binary, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("去除圖片的雜訊 原圖")

image2 = cv2.imread(r"images/sample2.jpg")

plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.show()

print("去除圖片的雜訊 效果")

image2_denoised = cv2.fastNlMeansDenoisingColored(image2, h=5)

plt.imshow(cv2.cvtColor(image2_denoised, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("absolute")

def my_laplace_sharpen(image, my_type="small"):
    result = np.zeros(image.shape, dtype=np.int64)
    # 確定拉普拉斯模板的形式
    if my_type == "small":
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i + ii - 1) < 0 or (i + ii - 1) >= image.shape[0]:
                        pass
                    elif (j + jj - 1) < 0 or (j + jj - 1) >= image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i + ii - 1][j + jj - 1] * my_model[ii][jj]
    return result


original_image_test1 = cv2.imread("data/lena.png", 0)


def my_laplace_result_add_abs(image, model):
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            if model[i][j] < 0:
                model[i][j] = 0
            if model[i][j] > 255:
                model[i][j] = 255
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result


# 調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type="big")

# 繪制結果
fig = plt.figure(
    num="new39",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

fig.add_subplot(121)
plt.title("原始圖像")
plt.imshow(original_image_test1)
fig.add_subplot(122)
plt.title("銳化濾波")
plt.imshow(my_laplace_result_add_abs(original_image_test1, result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("createCLAHE_image")

image = cv2.imread("data/building.png", 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(cl1, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("equalizeHist_image")

image = cv2.imread("data/wu_2.png", 0)
equ = cv2.equalizeHist(image)  # 只能傳入灰度圖
res = np.hstack((image, equ))  # 圖像列拼接（用于顯示）

# 繪製結果
fig = plt.figure(
    num="equalizeHist_image",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("gradient")

# 輸入圖像，輸出提取的邊緣信息
def my_sobel_sharpen(image):
    result_x = np.zeros(image.shape, dtype=np.int64)
    result_y = np.zeros(image.shape, dtype=np.int64)
    result = np.zeros(image.shape, dtype=np.int64)
    # 確定拉普拉斯模板的形式
    my_model_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    my_model_y = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i + ii - 1) < 0 or (i + ii - 1) >= image.shape[0]:
                        pass
                    elif (j + jj - 1) < 0 or (j + jj - 1) >= image.shape[1]:
                        pass
                    else:
                        result_x[i][j] += (
                            image[i + ii - 1][j + jj - 1] * my_model_x[ii][jj]
                        )
                        result_y[i][j] += (
                            image[i + ii - 1][j + jj - 1] * my_model_y[ii][jj]
                        )
            result[i][j] = abs(result_x[i][j]) + abs(result_y[i][j])
            if result[i][j] > 255:
                result[i][j] = 255
    return result


# 將邊緣信息按一定比例加到原始圖像上
def my_result_add(image, model, k):
    result = image + k * model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result


original_image_lena = cv2.imread("data/lena.png", 0)

# 獲得圖像邊界信息
edge_image_lena = my_sobel_sharpen(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_result_add(original_image_lena, edge_image_lena, -0.5)

# 繪製結果
fig = plt.figure(
    num="gradient",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原始圖像")
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title("邊緣檢測")
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title("梯度處理")
plt.imshow(sharpen_image_lena)

plt.show()

print("------------------------------------------------------------")  # 60個

print("imaeg_laplace")

original_image_test1 = cv2.imread("data/lena.png", 0)

# 用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result


def my_laplace_sharpen(image, my_type="small"):
    result = np.zeros(image.shape, dtype=np.int64)
    # 確定拉普拉斯模板的形式
    if my_type == "small":
        my_model = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    else:
        my_model = np.array([[1, 1, 1], [1, -8, 1], [1, 1, 1]])
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(3):
                for jj in range(3):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i + ii - 1) < 0 or (i + ii - 1) >= image.shape[0]:
                        pass
                    elif (j + jj - 1) < 0 or (j + jj - 1) >= image.shape[1]:
                        pass
                    else:
                        result[i][j] += image[i + ii - 1][j + jj - 1] * my_model[ii][jj]
    return result


# 將計算結果限制為正值
def my_show_edge(model):
    # 這里一定要用copy函數，不然會改變原來數組的值
    mid_model = model.copy()
    for i in range(mid_model.shape[0]):
        for j in range(mid_model.shape[1]):
            if mid_model[i][j] < 0:
                mid_model[i][j] = 0
            if mid_model[i][j] > 255:
                mid_model[i][j] = 255
    return mid_model


# 調用自定義函數
result = my_laplace_sharpen(original_image_test1, my_type="big")

# 繪製結果
fig = plt.figure(
    num="new40",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

fig.add_subplot(131)
plt.title("原始圖像")
plt.imshow(original_image_test1)
fig.add_subplot(132)
plt.title("邊緣檢測")
plt.imshow(my_show_edge(result))
fig.add_subplot(133)
plt.title("銳化處理")
plt.imshow(my_laplace_result_add(original_image_test1, result))
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")

from matplotlib import pyplot as plt


# 用原始圖像減去拉普拉斯模板直接計算得到的邊緣信息
def my_laplace_result_add(image, model):
    result = image - model
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            if result[i][j] > 255:
                result[i][j] = 255
            if result[i][j] < 0:
                result[i][j] = 0
    return result


original_image_test1 = cv2.imread("data/lena.png", 0)
# 函數中的參數ddepth為輸出圖像的深度，也就是每個像素點是多少位的。
# CV_16S表示16位有符號數
computer_result = cv2.Laplacian(original_image_test1, ksize=3, ddepth=cv2.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_fft")

Fs = 1200
# 采樣頻率
Ts = 1 / Fs
# 采樣區間
x = np.arange(0, 1, Ts)  # 時間向量，1200個
y = 5 * np.sin(2 * np.pi * 600 * x)
N = 1200
frq = np.arange(N)  # 頻率數1200個數
half_x = frq[range(int(N / 2))]  # 取一半區間
fft_y = np.fft.fft(y)
abs_y = np.abs(fft_y)  # 取復數的絕對值，即復數的模(雙邊頻譜)
angle_y = 180 * np.angle(fft_y) / np.pi  # 取復數的弧度,并換算成角度
gui_y = abs_y / N  # 歸一化處理（雙邊頻譜）
gui_half_y = gui_y[range(int(N / 2))]  # 由于對稱性，只取一半區間（單邊頻譜）

# 繪製結果
fig = plt.figure(
    num="image_fft",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 畫出原始波形的前50個點
plt.subplot(231)
plt.plot(frq[0:50], y[0:50])
plt.title("原始波形")
# 畫出雙邊未求絕對值的振幅譜
plt.subplot(232)
plt.plot(frq, fft_y, "black")
plt.title("雙邊振幅譜(未求振幅絕對值)")
# 畫出雙邊求絕對值的振幅譜
plt.subplot(233)
plt.plot(frq, abs_y, "r")
plt.title("雙邊振幅譜(未歸一化)")
# 畫出雙邊相位譜
plt.subplot(234)
plt.plot(frq[0:50], angle_y[0:50], "violet")
plt.title("雙邊相位譜(未歸一化)")
# 畫出雙邊振幅譜(歸一化)
plt.subplot(235)
plt.plot(frq, gui_y, "g")
plt.title("雙邊振幅譜(歸一化)")

# 畫出單邊振幅譜(歸一化)
plt.subplot(236)
plt.plot(half_x, gui_half_y, "blue")
plt.title("單邊振幅譜(歸一化)")
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

image = plt.imread("data/castle3.jpg")

# 根據公式轉成灰度圖
image = 0.2126 * image[:, :, 0] + 0.7152 * image[:, :, 1] + 0.0722 * image[:, :, 2]

# 繪製結果
fig = plt.figure(
    num="image_fft2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 顯示原圖
plt.subplot(231)
plt.imshow(image, "gray")
plt.title("原始圖像")
# 進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)

plt.subplot(232)
plt.imshow(np.abs(fft2), "gray")
plt.title("二維傅里葉變換")
# 將圖像變換的原點移動到頻域矩形的中心，并顯示效果
shift2center = np.fft.fftshift(fft2)

plt.subplot(233)
plt.imshow(np.abs(shift2center), "gray")
plt.title("頻域矩形的中心")
# 對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(fft2))

plt.subplot(235)
plt.imshow(log_fft2, "gray")
plt.title("傅立葉變換對數變換")
# 對中心化后的結果進行對數變換，并顯示結果
log_shift2center = np.log(1 + np.abs(shift2center))

plt.subplot(236)
plt.imshow(log_shift2center, "gray")
plt.title("中心化的對數變化")

plt.show()

print("------------------------------------------------------------")  # 60個

print("magnitude_spectrum")

image = cv2.imread("data/lena.png", 0)
dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# 繪製結果
fig = plt.figure(
    num="magnitude_spectrum",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121), plt.imshow(image, cmap="gray")
plt.title("原始圖像")

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("級頻譜")

plt.show()

print("------------------------------------------------------------")  # 60個

print("optimize")


def ComputeMinLevel(hist, pnum):
    index = np.add.accumulate(hist)
    return np.argwhere(index > pnum * 8.3 * 0.01)[0][0]


def ComputeMaxLevel(hist, pnum):
    hist_0 = hist[::-1]
    Iter_sum = np.add.accumulate(hist_0)
    index = np.argwhere(Iter_sum > (pnum * 2.2 * 0.01))[0][0]
    return 255 - index


def LinearMap(minlevel, maxlevel):
    if minlevel >= maxlevel:
        return []
    else:
        index = np.array(list(range(256)))
        screenNum = np.where(index < minlevel, 0, index)
        screenNum = np.where(screenNum > maxlevel, 255, screenNum)
        for i in range(len(screenNum)):
            if screenNum[i] > 0 and screenNum[i] < 255:
                screenNum[i] = (i - minlevel) / (maxlevel - minlevel) * 255
        return screenNum


def CreateNewImg(image):
    h, w, d = image.shape
    newimage = np.zeros([h, w, d])
    for i in range(d):
        imagehist = np.bincount(image[:, :, i].reshape(1, -1)[0])
        minlevel = ComputeMinLevel(imagehist, h * w)
        maxlevel = ComputeMaxLevel(imagehist, h * w)
        screenNum = LinearMap(minlevel, maxlevel)
        if screenNum.size == 0:
            continue
        for j in range(h):
            newimage[j, :, i] = screenNum[image[j, :, i]]
    return newimage


image = cv2.imread("data/building.png")
newimage = CreateNewImg(image)
cv2.imshow("原始圖像", image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

cv2.imshow("去霧后圖像", newimage / 255)
""" 不能用
plt.imshow(cv2.cvtColor(newimage / 255, cv2.COLOR_BGR2RGB))
plt.show()
"""

print("------------------------------------------------------------")  # 60個

print("兩圖相減")

filename1 = "data/_compare/compare1.jpg"
filename2 = "data/_compare/compare2.jpg"

image1 = cv2.imread(filename1)
image2 = cv2.imread(filename2)

# image3 = math.fabs(image1-image2)
image3 = image1 - image2

fig = plt.figure(
    num="兩圖相減",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減")

plt.show()

print("------------------------------------------------------------")  # 60個

"""

彩色影像轉HSV(RGB to HSV 或 BGR to HSV)

HSV簡單介紹分別為：
色相(H)：色彩的顏色名稱，如紅色、黃色等。
飽和度(S)：色彩的純度，越高色彩越純，低則逐漸變灰，數值為0-100%。
明度(V)：亮度，數值為0-100%。

使用 cv2.cvtColor 轉換顏色空間時，第二個參數與HSV相關的有：
cv2.COLOR_BGR2HSV
cv2.COLOR_HSV2BGR
cv2.COLOR_RGB2HSV
cv2.COLOR_HSV2RGB

opencv 預設的排列方式為BGR，而不是RGB

所以這邊使用的是 cv2.COLOR_BGR2HSV

當然實際上使用時不會只是單純RGB轉換成HSV就結束了，
通常會去針對HSV顏色區間去作後續的處理

範例. 物件偵測 - 找出綠色的物體

彩色轉HSV常見的應用可能有物件偵測，去背處理(排除綠色的背景)，
以下就來示範如何找出圖片中綠色的水果，類似的應用可能有找出草地的背景，

"""
image = cv2.imread("data/fruit.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

fig = plt.figure(
    num="彩色影像轉HSV",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))
plt.title("轉HSV")

lower_green = np.array([35, 43, 46])  # 綠色下限
upper_green = np.array([77, 255, 255])  # 綠色上限
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(133)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title("抓出綠色的部分")

plt.show()

print("------------------------------------------------------------")  # 60個


def salt_pepper_noise(image, fraction, salt_vs_pepper):
    img = np.copy(image)
    size = img.size
    num_salt = np.ceil(fraction * size * salt_vs_pepper).astype("int")
    num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype("int")
    row, column = img.shape

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_pepper)
    y = np.random.randint(0, row - 1, num_pepper)
    img[y, x] = 0  # 撒上胡椒

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_salt)
    y = np.random.randint(0, row - 1, num_salt)
    img[y, x] = 255  # 撒上鹽
    return img


fraction = 0.1  # 雜訊佔圖的比例
salt_vs_pepper = 0.5  # 鹽與胡椒的比例

filename = "C:/_git/vcs/_4.python/_data/tiger.jpg"
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
noisy = salt_pepper_noise(img, fraction, salt_vs_pepper)

plt.imshow(cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB))
plt.title("胡椒(黑)鹽(白)效果")

plt.show()

# 黑點就好比胡椒，白點就像是鹽，這種加上雜訊的方式，就稱為椒鹽雜訊（Salt & Pepper Noise）

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
print("image_dft2")

print('跑不出來 skip')

PI = 3.141591265

image = plt.imread('data/castle3.jpg')
#根據公式轉成灰度圖
image = 0.2126 * image[:,:,0] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,2]

#顯示原圖
plt.subplot(131),plt.imshow(image,'gray'),plt.title('original')

#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(132),plt.imshow(log_fft2,'gray'),plt.title('log_fft2')

h , w = image.shape
#生成一個同樣大小的復數矩陣
F = np.zeros([h,w],'complex128')
for u in range(h):
    for v in range(w):
        res = 0
        for x in range(h):
            for y in range(w):
                res += image[x,y] * np.exp(-1.j * 2 * PI * (u * x / h + v * y / w))
        F[u,v] = res

log_F = np.log(1 + np.abs(F))
plt.subplot(133)
plt.imshow(log_F,'gray')
plt.title('log_F')
"""


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 偽寫入
# cv2.imwrite("tmp_bgra.png", bgra)
# cv2.imwrite("tmp_bgra125.png", bgra125)
# cv2.imwrite("tmp_bgra0.png", bgra0)

print("------------------------------------------------------------")  # 60個

# 直接改寫image的內容
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename)

for i in range(20, 80):
    image[i, 180] = [0, 0, 255]  # 紅色一點

#     H          x
image[10:100, 200:290] = [0, 0, 255]  # 紅色 一塊 90X90

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


