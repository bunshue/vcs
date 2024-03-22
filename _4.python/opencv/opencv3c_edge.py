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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"

# == Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0, 0.0, 1.0)  # In BGR format

# == Processing =======================================================================

# 圖片處理

# -- Read image -----------------------------------------------------------------------
image = cv2.imread(filename)  # 讀取本機圖片

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 圖片轉為灰階

plt.subplot(232)
plt.title("灰階")
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))

# -- Edge detection -------------------------------------------------------------------

edges = cv2.Canny(image_gray, CANNY_THRESH_1, CANNY_THRESH_2)

plt.subplot(234)
plt.title("Canny")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

edges = cv2.dilate(edges, None)

plt.subplot(235)
plt.title("Dilate")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

edges = cv2.erode(edges, None)

plt.subplot(236)
plt.title("Erode")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

plt.show()

# cv2存圖
# cv2.imwrite('person-masked.jpg', masked)

print("------------------------------------------------------------")  # 60個

# split image into channels
c_red, c_green, c_blue = cv2.split(image)

plt.imshow(cv2.cvtColor(c_red, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(c_green, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(c_blue, cv2.COLOR_BGR2RGB))
plt.show()

# merge with mask got on one of a previous steps
# img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))
# plt.imshow(img_a)
# plt.show()

# save to disk
# cv2.imwrite('image/girl_1.png', img_a*255)

# or the same using plt
# plt.imsave('image/girl_2.png', img_a)
# plt.imshow('image', masked)                                   # Displays red, saves blue

print("------------------------------------------------------------")  # 60個

# 直方圖二值化
# 不同模式的Threshold方法
# cv2.THRESH_BINARY
# cv2.THRESH_BINARY_INV
# cv2.THRESH_TRUNC
# cv2.THRESH_TOZERO
# cv2.THRESH_TOZERO_INV

import cv2  # 導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 讀取本機圖片, 直接轉成灰階

ret, th1 = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

plt.imshow(cv2.cvtColor(th1, cv2.COLOR_BGR2RGB))

plt.show()

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("th1")
plt.imshow(cv2.cvtColor(th1, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# 影像邊緣檢測Canny()函數

gray_image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 讀取本機圖片, 直接轉成灰階

blur_gray = cv2.GaussianBlur(gray_image, (3, 3), 0)  # 執行高斯模糊化
threshold_1 = 30  # 強邊緣strong edge
threshold_2 = 60  # 弱邊緣weak edge

edges = cv2.Canny(blur_gray, threshold_1, threshold_2)

plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))
plt.title("Canny")

plt.show()

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("Canny")
plt.imshow(cv2.cvtColor(edges, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

# 影像邊緣檢測Sobel()函數


def sobel(image):
    kernel_size = (3, 3)
    blur_image = cv2.GaussianBlur(image, kernel_size, 0)  # 執行高斯模糊化
    # 水平方向梯度
    x = cv2.Sobel(blur_image, cv2.CV_16S, 1, 0, kernel_size)
    abs_x = cv2.convertScaleAbs(x)
    # 垂直方向梯度
    y = cv2.Sobel(blur_image, cv2.CV_16S, 0, 1, kernel_size)
    abs_y = cv2.convertScaleAbs(y)
    # 合併兩個方向的梯度
    sobel_image = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)
    return sobel_image


gray_image = cv2.imread(filename)  # 讀取本機圖片

sobel_image = sobel(gray_image)

plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))
plt.title("Sobel")

plt.show()


plt.figure("影像處理", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("Sobel")
plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


# 各種邊緣檢測的方法

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

print("顯示 Sobel 效果 1")
sobelx = cv2.Sobel(image, -1, 1, 0)

plt.subplot(232)
plt.title("Sobel 效果 1")
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

print("顯示 Sobel 效果 2 x 方向")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8

plt.subplot(233)
plt.title("Sobel 效果 2 x 方向")
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

print("顯示 Sobel 效果 3 y 方向")
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)

plt.subplot(234)
plt.title("Sobel 效果 3 y 方向")
plt.imshow(cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

print("顯示 Sobel 效果 4 x-y 方向")
sobelxy = cv2.Sobel(image, cv2.CV_64F, 1, 1)
sobelxy = cv2.convertScaleAbs(sobelxy)

plt.subplot(235)
plt.title("Sobel 效果 4 x-y 方向")
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

print("------------------------------------------------------------")  # 60個

print("顯示 Sobel 效果 5 先x 再y 方向")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

plt.subplot(236)
plt.title("Sobel 效果 5 先x 再y 方向")
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("顯示 Sobel 效果 6")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
sobelxy11 = cv2.Sobel(image, cv2.CV_64F, 1, 1)
sobelxy11 = cv2.convertScaleAbs(sobelxy11)

plt.figure("", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Sobel xy")
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Sobel xy11")
plt.imshow(cv2.cvtColor(sobelxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("Scharr 效果 1")
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8

print("Scharr 效果 2")
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)

print("Scharr 效果 3")
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

plt.figure("Scharr", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("Scharr 效果 1")
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("Scharr 效果 2")
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("Scharr 效果 3")
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("Scharr 效果")
# scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 1)   #fail
scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 0)  # ok
scharrxy11 = cv2.convertScaleAbs(scharrxy11)  # 转回uint8

plt.figure("", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("Scharr 效果")
plt.imshow(cv2.cvtColor(scharrxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("顯示 Sobel 效果 1")
scharrx = cv2.Sobel(image, cv2.CV_64F, 1, 0, -1)
scharry = cv2.Sobel(image, cv2.CV_64F, 0, 1, -1)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv2.convertScaleAbs(scharry)

plt.figure("", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Sobel x")
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Sobel y")
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("顯示 Sobel 效果 2")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

plt.figure("", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Sobel xy")
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Scharr xy")
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/laplacian.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print("顯示 Laplacian 效果")
Laplacian = cv2.Laplacian(image, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)

plt.figure("Laplacian", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("Laplacian")
plt.imshow(cv2.cvtColor(Laplacian, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# 輸出邊緣和結構信息

image = cv2.imread("data/contours.bmp")

plt.figure("輸出邊緣和結構信息", figsize=(10, 6))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
o = cv2.drawContours(image, contours, -1, (0, 0, 255), 5)

plt.subplot(122)
plt.title("輸出邊緣和結構信息")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")

plt.figure("影像處理1", figsize=(10, 6))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 5)
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.title("輪廓 " + str(i + 1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/loc3.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image.shape, np.uint8)

mask = cv2.drawContours(mask, contours, -1, (255, 255, 255), -1)

loc = cv2.bitwise_and(image, mask)

plt.figure("影像處理2", figsize=(10, 6))

plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("mask")
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("location")
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/moments.bmp")

plt.figure("影像處理3", figsize=(10, 6))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, 255, 3)
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.title("輪廓 " + str(i + 1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

print("觀察各個輪廓的矩（moments）:")
for i in range(n):
    print("輪廓" + str(i) + "的矩:\n", cv2.moments(contours[i]))
print("觀察各個輪廓的面積:")
for i in range(n):
    print("輪廓" + str(i) + "的面積:%d" % cv2.moments(contours[i])["m00"])

plt.show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")

plt.figure("影像處理4", figsize=(10, 6))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    print("contours[" + str(i) + "]面積=", cv2.contourArea(contours[i]))
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.title("輪廓 " + str(i + 1))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個


# 篩選出大于特定大小的輪廓

image = cv2.imread("data/contours.bmp")

plt.figure("影像處理5", figsize=(10, 6))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    if cv2.contourArea(contours[i]) > 15000:
        # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
        index = "22" + str(i + 2)
        plt.subplot(int(index))
        plt.title("輪廓 " + str(i + 1))
        plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

# 篩選出大于特定大小的輪廓

# --------------讀取及顯示原始圖像--------------------
image = cv2.imread("data/contours0.bmp")
print("顯示原圖")
cv2.imshow("original", image)

# --------------獲取輪廓--------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------計算各個輪廓的長度和、平均長度--------------------
n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

cntLen = []  # 存儲各個輪廓的長度
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print("第" + str(i) + "個輪廓的長度:%d" % cntLen[i])
cntLenSum = np.sum(cntLen)  # 各個輪廓長度和
cntLenAvr = cntLenSum / n  # 各個輪廓長度平均值
print("各個輪廓的總長度為：%d" % cntLenSum)
print("各個輪廓的平均長度為：%d" % cntLenAvr)

# --------------顯示超過平均值的輪廓--------------------
contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        cv2.imshow("contours[" + str(i) + "]", contoursImg[i])

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cs1.bmp")
print("顯示原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
HuM1 = cv2.HuMoments(cv2.moments(gray)).flatten()

print("cv2.moments(gray)=\n", cv2.moments(gray))
print("\nHuM1=\n", HuM1)
print(
    "\ncv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']=%f+%f=%f\n"
    % (
        cv2.moments(gray)["nu20"],
        cv2.moments(gray)["nu02"],
        cv2.moments(gray)["nu20"] + cv2.moments(gray)["nu02"],
    )
)
print("HuM1[0]=", HuM1[0])
print(
    "\nHu[0]-(nu02+nu20)=",
    HuM1[0] - (cv2.moments(gray)["nu20"] + cv2.moments(gray)["nu02"]),
)

print("------------------------------------------------------------")  # 60個

# ----------------計算圖像1的Hu矩-------------------
image1 = cv2.imread("data/cs1.bmp")
print("顯示原圖")

gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()
# ----------------計算圖像2的Hu矩-------------------
image2 = cv2.imread("data/cs3.bmp")
print("顯示原圖")

gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()
# ----------------計算圖像3的Hu矩-------------------
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image3 = cv2.imread(filename)
print("顯示原圖")

gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

# ---------打印圖像1、圖像2、圖像3的特征值------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
print("cv2.moments(gray1)=\n", cv2.moments(gray1))
print("cv2.moments(gray2)=\n", cv2.moments(gray2))
print("cv2.moments(gray3)=\n", cv2.moments(gray3))
print("\nHuM1=\n", HuM1)
print("\nHuM2=\n", HuM2)
print("\nHuM3=\n", HuM3)

# ---------計算圖像1與圖像2、圖像3的Hu矩之差----------------
print("\nHuM1-HuM2=", HuM1 - HuM2)
print("\nHuM1-HuM3=", HuM1 - HuM3)

plt.figure("影像處理6", figsize=(16, 12))

plt.subplot(131)
plt.title("original1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("original2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("original3")
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# --------------讀取3幅原始圖像--------------------
image1 = cv2.imread("data/cs1.bmp")
image2 = cv2.imread("data/cs2.bmp")
image3 = cv2.imread("data/cc.bmp")

# ----------打印3幅原始圖像的shape屬性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)
# --------------色彩空間轉換--------------------
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
# -------------進行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0.0)
# --------------打印差值--------------------
print("相同圖像的matchShape=", ret0)
print("相似圖像的matchShape=", ret1)
print("不相似圖像的matchShape=", ret2)

# --------------顯示3幅原始圖像--------------------

plt.figure("影像處理7", figsize=(16, 12))

plt.subplot(131)
plt.title("original1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("original2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("original3")
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# ---------------讀取并顯示原始圖像------------------
image = cv2.imread("data/cc.bmp")
print("顯示原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# ---------------返回頂點及邊長------------------
x, y, w, h = cv2.boundingRect(contours[0])
print("頂點及長寬的點形式:")
print("x=", x)
print("y=", y)
print("w=", w)
print("h=", h)
# ---------------僅有一個返回值的情況------------------
rect = cv2.boundingRect(contours[0])
print("\n頂點及長寬的元組（tuple）形式：")
print("rect=", rect)

print("------------------------------------------------------------")  # 60個

# ---------------讀取并顯示原始圖像------------------
image = cv2.imread("data/cc.bmp")

print("顯示原圖")
cv2.imshow("original", image)

plt.figure("影像處理8", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv2.drawContours(image, [brcnt], -1, (0, 0, 255), 2)

# ---------------顯示矩形邊界------------------
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ---------------讀取并顯示原始圖像------------------
image = cv2.imread("data/cc.bmp")

print("顯示原圖")
cv2.imshow("original", image)

plt.figure("影像處理9", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

# ---------------顯示矩形邊界------------------
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")

cv2.imshow("original", image)

plt.figure("影像處理10", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rect = cv2.minAreaRect(contours[0])
print("返回值rect:\n", rect)
points = cv2.boxPoints(rect)
print("\n轉換后的points：\n", points)
points = np.int0(points)  # 取整
image = cv2.drawContours(image, [points], 0, (0, 0, 255), 2)

cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", image)

plt.figure("影像處理11", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(image, center, radius, (0, 0, 255), 2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")

plt.figure("影像處理12", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original", image)
ellipse = cv2.fitEllipse(contours[0])
print("ellipse=", ellipse)
cv2.ellipse(image, ellipse, (0, 255, 0), 3)
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")

cv2.imshow("original", image)

plt.figure("影像處理13", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rows, cols = image.shape[:2]
[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(image, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", image)

plt.figure("影像處理14", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area, trgl = cv2.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl:", trgl)
for i in range(0, 3):
    print("x")
    # cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), (255,255,255), 2)
cv2.imshow("result", image)

plt.subplot(122)
plt.title("result")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ----------------讀取并顯示原始圖像-------------------------------
image = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", image)

# ----------------獲取輪廓-------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ----------------epsilon=0.1*周長-------------------------------
adp = image.copy()
epsilon = 0.1 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.1", adp)

# ----------------epsilon=0.09*周長-------------------------------
adp = image.copy()
epsilon = 0.09 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.09", adp)

# ----------------epsilon=0.055*周長-------------------------------
adp = image.copy()
epsilon = 0.055 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.055", adp)

# ----------------epsilon=0.05*周長-------------------------------
adp = image.copy()
epsilon = 0.05 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.05", adp)

# ----------------epsilon=0.02*周長-------------------------------
adp = image.copy()
epsilon = 0.02 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)
cv2.imshow("result0.02", adp)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")
print("顯示原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])  # 返回坐標值
print("returnPoints為默認值True時返回值hull的值：\n", hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)  # 返回索引值
print("returnPoints為False時返回值hull的值：\n", hull2)

print("------------------------------------------------------------")  # 60個

# --------------讀取并繪製原始圖像------------------
o = cv2.imread("data/hand.bmp")
print("顯示原圖")
cv2.imshow("original", o)
# --------------提取輪廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------尋找凸包，得到凸包的角點------------------
hull = cv2.convexHull(contours[0])
# --------------繪製凸包------------------
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
# --------------顯示凸包------------------
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ----------------原圖--------------------------
img = cv2.imread("data/hand.bmp")
print("顯示原圖")
cv2.imshow("original", img)
# ----------------構造輪廓--------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# ----------------凸包--------------------------
cnt = contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print("defects=\n", defects)
# ----------------構造凸缺陷--------------------------
for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(img, start, end, [0, 0, 255], 2)
    cv2.circle(img, far, 5, [255, 0, 0], -1)
# ----------------顯示結果--------------------------
cv2.imshow("result", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")
print("顯示原圖")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# --------------凸包----------------------
image1 = o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, (0, 255, 0), 2)
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：", cv2.isContourConvex(hull))
cv2.imshow("result1", image1)
# ------------逼近多邊形--------------------
image2 = o.copy()
epsilon = 0.01 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, (0, 0, 255), 2)
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：", cv2.isContourConvex(approx))
cv2.imshow("result2", image2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ----------------原始圖像-------------------------
o = cv2.imread("data/cs.bmp")
print("顯示原圖")
cv2.imshow("original", o)
# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

""" fail
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)

#----------------內部點A的距離-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部點B的距離-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#------------正好處于邊緣上的點C的距離-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的
#----------------顯示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

# ----------------原始圖像-------------------------
o = cv2.imread("data/cs.bmp")
print("顯示原圖")
cv2.imshow("original", o)
# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])
""" fail
image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, (0, 255, 0), 2)
#----------------內部點A與多邊形的關系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'A',(300,150), font, 1,(0,255,0),3)
print("distA=",distA) 
#----------------外部點B與多邊形的關系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'B',(300,250), font, 1,(0,255,0),3)
print("distB=",distB) 
#----------------邊緣線上點C與多邊形的關系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112),False)  
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'C',(423,112), font, 1,(0,255,0),3)
print("distC=",distC) 
#print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的
#----------------顯示-------------------------
cv2.imshow("result",image)

cv2.waitKey()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

# -----------原始圖像o1邊緣--------------------
o1 = cv2.imread("data/cs.bmp")
print("顯示原圖")
cv2.imshow("original1", o1)

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
ret, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
# -----------原始圖像o2邊緣--------------------
o2 = cv2.imread("data/cs3.bmp")
print("顯示原圖")
cv2.imshow("original2", o2)

gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
ret, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]
# -----------原始圖像o3邊緣--------------------
o3 = cv2.imread("data/hand.bmp")
print("顯示原圖")
cv2.imshow("original3", o3)

gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)
ret, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt3 = contours3[0]
# -----------構造距離提取算子--------------------
sd = cv2.createShapeContextDistanceExtractor()
# -----------計算距離--------------------
d1 = sd.computeDistance(cnt1, cnt1)
print("自身距離d1=", d1)
d2 = sd.computeDistance(cnt1, cnt2)
print("旋轉縮放后距離d2=", d2)
d3 = sd.computeDistance(cnt1, cnt3)
print("不相似對象距離d3=", d3)
# -----------顯示距離--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# -----------讀取原始圖像--------------------
o1 = cv2.imread("data/cs.bmp")
print("顯示原圖")

o2 = cv2.imread("data/cs3.bmp")
print("顯示原圖")

o3 = cv2.imread("data/hand.bmp")
print("顯示原圖")

cv2.imshow("original1", o1)
cv2.imshow("original2", o2)
cv2.imshow("original3", o3)
# -----------色彩轉換--------------------
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)
# -----------閾值處理--------------------
ret, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
ret, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
ret, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)
# -----------提取輪廓--------------------
contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours3, hierarchy = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
# -----------構造距離提取算子--------------------
hd = cv2.createHausdorffDistanceExtractor()
# -----------計算距離--------------------
d1 = hd.computeDistance(cnt1, cnt1)
print("自身Hausdorff距離d1=", d1)
d2 = hd.computeDistance(cnt1, cnt2)
print("旋轉縮放后Hausdorff距離d2=", d2)
d3 = hd.computeDistance(cnt1, cnt3)
print("不相似對象Hausdorff距離d3=", d3)
# -----------顯示距離--------------------

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(o, (x, y), (x + w, y + h), (255, 255, 255), 3)

aspectRatio = float(w) / h
print(aspectRatio)
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cv2.rectangle(o, (x, y), (x + w, y + h), (255, 0, 0), 3)

rectArea = w * h
cntArea = cv2.contourArea(contours[0])
extend = float(cntArea) / rectArea
print(extend)
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cntArea = cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o, [hull], True, (0, 255, 0), 2)
solidity = float(cntArea) / hullArea
print(solidity)
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o, contours[0], -1, (0, 0, 255), 3)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4 * cntArea / np.pi)
print(equiDiameter)
cv2.circle(o, (100, 100), int(equiDiameter / 2), (0, 0, 255), 3)  # 展示等直徑大小的圓
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
ellipse = cv2.fitEllipse(contours[0])
retval = cv2.fitEllipse(contours[0])
print("單個返回值形式：")
print("retval=\n", retval)
(x, y), (MA, ma), angle = cv2.fitEllipse(contours[0])
print("三個返回值形式：")
print("(x,y)=(", x, y, ")")
print("(MA,ma)=(", MA, ma, ")")
print("angle=", angle)
cv2.ellipse(o, ellipse, (0, 0, 255), 2)
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ------------生成一個都是0值的a-------------------
a = np.zeros((5, 5), dtype=np.uint8)
# -------隨機將其中10個位置上的數值設置為1------------
# ---times控制次數
# ---i,j是隨機生成的行、列位置
# ---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1
# -------打印a，觀察a內值的情況-----------
print("a=\n", a)
# ------查找a內非零值的位置信息------------
loc = np.transpose(np.nonzero(a))
# -----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n", loc)

print("------------------------------------------------------------")  # 60個

# -----------------讀取原始圖像----------------------
o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)
# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)
cv2.imshow("mask1", mask1)
# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)
cv2.imshow("mask2", mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# ------------生成一個都是0值的a-------------------
a = np.zeros((5, 5), dtype=np.uint8)
# -------隨機將其中10個位置上的數值設置為1------------
# ---times控制次數
# ---i,j是隨機生成的行、列位置
# ---a[i,j]=1,將隨機挑選出來的位置上的值設置為1
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1
# -------打印a，觀察a內值的情況-----------
print("a=\n", a)
# ------查找a內非零值的位置信息------------
loc = cv2.findNonZero(a)
# -----將a內非零值的位置信息輸出------------
print("a內非零值位置:\n", loc)

print("------------------------------------------------------------")  # 60個

# -----------------讀取原始圖像----------------------
o = cv2.imread("data/cc.bmp")
print("顯示原圖")
cv2.imshow("original", o)
# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)
cv2.imshow("mask1", mask1)
# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)
cv2.imshow("mask2", mask2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/ct.png")
print("顯示原圖")
cv2.imshow("original", o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]  # coutours[0]、coutours[1]是左側字母R
# --------使用掩膜獲取感興趣區域的最值-----------------
# 需要注意minMaxLoc處理的對象為灰度圖像，本例中處理對象為灰度圖像gray
# 如果希望獲取彩色圖像的，需要提取各個通道，將每個通道獨立計算最值
mask = np.zeros(gray.shape, np.uint8)
mask = cv2.drawContours(mask, [cnt], -1, 255, -1)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(gray, mask=mask)
print("minVal=", minVal)
print("maxVal=", maxVal)
print("minLoc=", minLoc)
print("maxLoc=", maxLoc)
# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
masko = cv2.drawContours(masko, [cnt], -1, (255, 255, 255), -1)
loc = cv2.bitwise_and(o, masko)
cv2.imshow("mask", loc)
# 顯示灰度結果
# loc=cv2.bitwise_and(gray,mask)
# cv2.imshow("mask",loc)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# --------讀取并顯示原始圖像-----------------
o = cv2.imread("data/ct.png")
print("顯示原圖")
cv2.imshow("original", o)
# --------獲取輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]
# --------使用掩膜獲取感興趣區域的均值-----------------
mask = np.zeros(gray.shape, np.uint8)  # 構造mean所使用的掩膜，必須是單通道的
cv2.drawContours(mask, [cnt], 0, (255, 255, 255), -1)
meanVal = cv2.mean(o, mask=mask)  # mask是區域，所以必須是單通道的
print("meanVal=\n", meanVal)
# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
cv2.drawContours(masko, [cnt], -1, (255, 255, 255), -1)
loc = cv2.bitwise_and(o, masko)
cv2.imshow("mask", loc)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs.bmp")
print("顯示原圖")

# --------獲取并繪製輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(gray.shape, np.uint8)
cnt = contours[0]
cv2.drawContours(mask, [cnt], 0, 255, -1)
# --------計算極值-----------------
leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])
# --------計算極值-----------------
print("leftmost=", leftmost)
print("rightmost=", rightmost)
print("topmost=", topmost)
print("bottommost=", bottommost)
# --------繪製說明文字-----------------
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, "A", leftmost, font, 1, (0, 0, 255), 2)
cv2.putText(o, "B", rightmost, font, 1, (0, 0, 255), 2)
cv2.putText(o, "C", topmost, font, 1, (0, 0, 255), 2)
cv2.putText(o, "D", bottommost, font, 1, (0, 0, 255), 2)
# --------繪製圖像-----------------
cv2.imshow("result", o)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

print("------------------------------------------------------------")  # 60個

print("使用 cv2 顯示圖片")

image = cv2.imread(filename)  # 讀取本機圖片

cv2.imshow("Peony", image)  # 顯示圖片

print("在此等待任意鍵繼續, 繼續後刪除本視窗")
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("取兩圖的影像差異 diff")

filename1 = "C:/_git/vcs/_1.data/______test_files1/compare/compare1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/compare/compare2.jpg"

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

print("image1.shape內容 :", img1.shape)
print("image2.shape內容 :", img2.shape)


# 比較並顯示差異影像
diff = cv2.absdiff(img1, img2)

cv2.imshow("Difference", diff)

print("在此等待任意鍵繼續, 繼續後刪除本視窗")
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("疊合")

filename1 = "C:/_git/vcs/_1.data/______test_files1/ims02.bmp"
filename2 = "C:/_git/vcs/_1.data/______test_files1/ims03.bmp"

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)


blended = cv2.addWeighted(img1, 1, img2, 1, 0)

cv2.imshow("Surveyed", blended)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

img = cv2.imread(filename, -1)

print(img.shape)
print(img.shape[0])  # H
print(img.shape[1])  # W

print("將一些點數改為亂數點數")
for i in range(30):
    for j in range(img.shape[1] // 2):
        img[i][j] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("複製貼上圖片的一部分")

# Copy part of image
#          H        W
tag = img[100:200, 130:230]
img[20:120, 180:280] = tag

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

import os

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

cv2.namedWindow("Peony1")  # 使用預設
cv2.namedWindow("Peony2", cv2.WINDOW_NORMAL)  # 可以調整大小
img1 = cv2.imread(filename)  # 彩色讀取
img2 = cv2.imread(filename, 0)  # 灰色讀取
cv2.imshow("Peony1", img1)  # 顯示影像img1
cv2.imshow("Peony2", img2)  # 顯示影像img2
cv2.waitKey(3000)  # 等待3秒
cv2.destroyWindow("Peony1")  # 刪除Peony1
cv2.waitKey(3000)  # 等待3秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

cv2.namedWindow("Peony")  # 使用預設
img = cv2.imread(filename)  # 彩色讀取
cv2.imshow("Peony", img)  # 顯示影像img
cv2.imwrite("tmp_pic01.jpg", img)  # 將檔案寫入 tmp_pic01.jpg
cv2.waitKey(3000)  # 等待3秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # BGR 讀取
cv2.imshow("Peony", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

cv2.namedWindow("Peony")  # 使用預設
img = cv2.imread(filename)  # 彩色讀取
cv2.line(img, (10, 300), (250, 300), (255, 0, 0), 5)  # 輸出線條
cv2.rectangle(img, (20, 20), (240, 250), (0, 0, 255), 2)  # 輸出矩陣
cv2.putText(img, "Peony", (10, 250), cv2.FONT_ITALIC, 3, (255, 0, 0), 8)  # 輸出文字
cv2.imshow("Peony", img)  # 顯示影像img
cv2.waitKey(3000)  # 等待3秒
cv2.destroyAllWindows()  # 刪除所有視窗

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
