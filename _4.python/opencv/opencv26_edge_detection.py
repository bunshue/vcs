"""
圖像邊緣檢測

影像梯度與邊緣偵測

邊緣檢測

cv2.Canny()
cv2.Sobel()
cv2.Scharr()
cv2.Laplacian()
比較
"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
# cv2.Canny() ST
# Canny 邊緣檢測
print("------------------------------------------------------------")  # 60個

print("使用Trackbar 做 Canny")


def do_trackbar_event1(val):
    global min_value, max_value
    min_value = val
    # print("數值 :", val, end=" ")
    dst = cv2.Canny(image, min_value, max_value)  # minVal=50, maxVal=100, typical
    cv2.imshow("OpenCV", dst)


def do_trackbar_event2(val):
    global min_value, max_value
    max_value = val
    # print("數值 :", val, end=" ")
    dst = cv2.Canny(image, min_value, max_value)  # minVal=50, maxVal=100, typical
    cv2.imshow("OpenCV", dst)


image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
# image = cv2.GaussianBlur(image, (3, 3), 0)  # 降低噪音
# image = cv2.GaussianBlur(image, (5, 5), 0)

cv2.imshow("OpenCV", image)

min_value, max_value = 40, 50
cv2.createTrackbar("min ", "OpenCV", 0, 100, do_trackbar_event1)
cv2.setTrackbarPos("min ", "OpenCV", 40)  # 設定預設值

cv2.createTrackbar("max ", "OpenCV", 0, 100, do_trackbar_event2)
cv2.setTrackbarPos("max ", "OpenCV", 50)  # 設定預設值

# 取得Trackbar數值
value1 = cv2.getTrackbarPos("min ", "OpenCV")
do_trackbar_event1(value1)  # 套用一次設定值

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("CannyThreshold")


def do_CannyThreshold(lowThreshold):
    # 高斯模糊，边缘检测需要的
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)
    detected_edges = cv2.Canny(
        detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size
    )
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # 只需在原始圖像的邊緣添加一些顏色
    cv2.imshow("OpenCV", dst)


lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3
img = cv2.imread(filename2)  # 彩色讀取
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階
cv2.namedWindow("OpenCV")
cv2.createTrackbar(
    "Min threshold", "OpenCV", lowThreshold, max_lowThreshold, do_CannyThreshold
)

do_CannyThreshold(0)  # 初始化

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
# image = cv2.GaussianBlur(image, (3, 3), 0)  # 降低噪音
# image = cv2.GaussianBlur(image, (5, 5), 0)

dst1 = cv2.Canny(image, 50, 100)  # minVal=50, maxVal=100
dst2 = cv2.Canny(image, 50, 200)  # minVal=50, maxVal=200
dst3 = cv2.Canny(image, 100, 200)
dst4 = cv2.Canny(image, 50, 150)
dst5 = cv2.Canny(image, 128, 200)
dst6 = cv2.Canny(image, 32, 128)

# 套用 medianBlur() 中值模糊
image3 = cv2.medianBlur(image, 7)  # 模糊化，去除雜訊 7, 25 彩色黑白皆可
image4 = cv2.Canny(image3, 36, 36)  # 偵測邊緣

plt.figure(figsize=(12, 10))
plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(332)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("灰階直接 Canny 1")

plt.subplot(333)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("灰階直接Canny 2")

plt.subplot(334)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("模糊化，去除雜訊")

plt.subplot(335)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("Canny 偵測邊緣")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Canny() SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Sobel() ST
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/edge_detection/map.jpg")  # 彩色讀取

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

dst = cv2.Sobel(image, -1, 1, 0)  # 計算 x 軸影像梯度

plt.subplot(232)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

dst = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值

plt.subplot(233)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

dst = cv2.Sobel(image, -1, 0, 1)  # 計算 y 軸影像梯度

plt.subplot(234)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

dst = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dst = cv2.convertScaleAbs(dst)  # 將負值轉正值

plt.subplot(235)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/edge_detection/map.jpg")  # 彩色讀取

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

dstx = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值

plt.subplot(222)
plt.imshow(cv2.cvtColor(dstx, cv2.COLOR_BGR2RGB))
plt.title("dstx")

dsty = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值

plt.subplot(223)
plt.imshow(cv2.cvtColor(dsty, cv2.COLOR_BGR2RGB))
plt.title("dsty")

dst = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst=dstx+dsty")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 影像邊緣檢測Sobel()函數

image = cv2.imread(filename2)  # 彩色讀取

kernel_size = (3, 3)

# 高斯模糊，边缘检测需要的
blur_image = cv2.GaussianBlur(image, kernel_size, 0)

# 水平方向梯度
x = cv2.Sobel(blur_image, cv2.CV_16S, 1, 0, kernel_size)
abs_x = cv2.convertScaleAbs(x)

# 垂直方向梯度
y = cv2.Sobel(blur_image, cv2.CV_16S, 0, 1, kernel_size)
abs_y = cv2.convertScaleAbs(y)

# 合併兩個方向的梯度
sobel_image = cv2.addWeighted(abs_x, 0.5, abs_y, 0.5, 0)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(sobel_image, cv2.COLOR_BGR2RGB))
plt.title("Sobel")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 Sobel() 灰階")

image = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# Sobel()函數
dstx = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值

dsty = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值

dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst_sobel, cv2.COLOR_BGR2RGB))
plt.title("Sobel")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 Sobel()")

image = cv2.imread("data/edge_detection/geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
image = cv2.GaussianBlur(image, (3, 3), 0)  # 降低噪音

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# Sobel()函數
dstx = cv2.Sobel(image, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值

dsty = cv2.Sobel(image, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值

dst_sobel = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst_sobel, cv2.COLOR_BGR2RGB))
plt.title("Sobel")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 各種邊緣檢測的方法

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

print("------------------------------")  # 30個

print("顯示 Sobel 效果 1")
sobelx = cv2.Sobel(image, -1, 1, 0)

plt.subplot(232)
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))
plt.title("Sobel 效果 1")

print("------------------------------")  # 30個

print("顯示 Sobel 效果 2 x 方向")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8

plt.subplot(233)
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))
plt.title("Sobel 效果 2 x 方向")

print("------------------------------")  # 30個

print("顯示 Sobel 效果 3 y 方向")
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)

plt.subplot(234)
plt.imshow(cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB))
plt.title("Sobel 效果 3 y 方向")

print("------------------------------")  # 30個

print("顯示 Sobel 效果 4 x-y 方向")
sobelxy = cv2.Sobel(image, cv2.CV_64F, 1, 1)
sobelxy = cv2.convertScaleAbs(sobelxy)

plt.subplot(235)
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))
plt.title("Sobel 效果 4 x-y 方向")

print("------------------------------")  # 30個

print("顯示 Sobel 效果 5 先x 再y 方向")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8

sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

plt.subplot(236)
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))
plt.title("Sobel 效果 5 先x 再y 方向")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = filename_lena_gray

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("顯示 Sobel 效果 6")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8

sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

sobelxy11 = cv2.Sobel(image, cv2.CV_64F, 1, 1)
sobelxy11 = cv2.convertScaleAbs(sobelxy11)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))
plt.title("Sobel xy")

plt.subplot(133)
plt.imshow(cv2.cvtColor(sobelxy11, cv2.COLOR_BGR2RGB))
plt.title("Sobel xy11")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("顯示 Sobel 效果 1")
scharrx = cv2.Sobel(image, cv2.CV_64F, 1, 0, -1)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8

scharry = cv2.Sobel(image, cv2.CV_64F, 0, 1, -1)
scharry = cv2.convertScaleAbs(scharry)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))
plt.title("Sobel x")

plt.subplot(133)
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))
plt.title("Sobel y")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = filename_lena_gray

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("顯示 Sobel 效果 2")
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)  # 转回uint8

sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
sobely = cv2.convertScaleAbs(sobely)

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8

scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)

scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))
plt.title("Sobel xy")

plt.subplot(133)
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))
plt.title("Scharr xy")

show()

print("------------------------------------------------------------")  # 60個
# cv2.Sobel() SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Scharr() ST
print("------------------------------------------------------------")  # 60個

print("使用 Scharr() 灰階")

image = cv2.imread(filename3, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
image = cv2.GaussianBlur(image, (3, 3), 0)  # 降低噪音

# Scharr()函數
dstx = cv2.Scharr(image, cv2.CV_32F, 1, 0)  # 計算 x 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)  # 將負值轉正值

dsty = cv2.Scharr(image, cv2.CV_32F, 0, 1)  # 計算 y 軸影像梯度
dsty = cv2.convertScaleAbs(dsty)  # 將負值轉正值

dst_scharr = cv2.addWeighted(dstx, 0.5, dsty, 0.5, 0)  # 影像融合

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dstx, cv2.COLOR_BGR2RGB))
plt.title("Scharr X")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dsty, cv2.COLOR_BGR2RGB))
plt.title("Scharr Y")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst_scharr, cv2.COLOR_BGR2RGB))
plt.title("Scharr")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("Scharr")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("Scharr 效果 1")
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8

print("Scharr 效果 2")
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)

print("Scharr 效果 3")
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)  # 转回uint8

scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)

scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))
plt.title("Scharr 效果 1")

plt.subplot(223)
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))
plt.title("Scharr 效果 2")

plt.subplot(224)
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))
plt.title("Scharr 效果 3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("Scharr 效果")
# scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 1)   #fail
scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 0)  # ok
scharrxy11 = cv2.convertScaleAbs(scharrxy11)  # 转回uint8

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(scharrxy11, cv2.COLOR_BGR2RGB))
plt.title("Scharr 效果")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Scharr() SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Laplacian() ST
print("------------------------------------------------------------")  # 60個

print("使用 Laplacian()")

image = cv2.imread("data/edge_detection/geneva.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
image = cv2.GaussianBlur(image, (3, 3), 0)  # 降低噪音

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# Laplacian()函數
dst_tmp = cv2.Laplacian(image, cv2.CV_32F, ksize=3)  # Laplacian邊緣影像
dst_lap = cv2.convertScaleAbs(dst_tmp)  # 將負值轉正值

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst_lap, cv2.COLOR_BGR2RGB))
plt.title("Laplacian")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/edge_detection/laplacian.jpg")  # 彩色讀取

dst_tmp = cv2.Laplacian(image, cv2.CV_32F)  # Laplacian邊緣影像
dst = cv2.convertScaleAbs(dst_tmp)  # 轉換為正值

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("dst")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/laplacian.bmp"

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("顯示 Laplacian 效果")
Laplacian = cv2.Laplacian(image, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(Laplacian, cv2.COLOR_BGR2RGB))
plt.title("Laplacian")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.Laplacian() SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# 比較 ST
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 比較 SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = filename1
img = cv2.imread(filename, -1)  # 彩色讀取?? -1 ??

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

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Image")
show()

print("複製貼上圖片的一部分")

# Copy part of image
#          H        W
tag = img[100:200, 130:230]
img[20:120, 180:280] = tag

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Image")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)  # 彩色讀取

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

image = cv2.medianBlur(image, 7)  # 模糊化，去除雜訊

# Laplacian
dst1 = cv2.Laplacian(image, -1, 1, 5)  # 偵測邊緣

# Sobel
dst2 = cv2.Sobel(image, -1, 1, 1, 1, 7)  # 偵測邊緣

# Canny
dst3 = cv2.Canny(image, 36, 36)  # 偵測邊緣

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("Laplacian")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("Sobel")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("Canny")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("梯度 Gradient")

image = cv2.imread(filename_lena_color, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

# 高斯模糊，边缘检测需要的
img1 = cv2.GaussianBlur(image, (3, 3), 0)

# 形態學：邊緣檢測
# 設定紅色通道閾值210（閾值影響梯度運算效果）
thresh = 210  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(image, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定義矩形結構元素
gradient = cv2.morphologyEx(binary, cv2.MORPH_GRADIENT, kernel)  # 梯度

cv2.imshow("Original", image)
cv2.imshow("Gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255

edge[edge > 255] = 255
edge = edge.astype(np.uint8)

edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))

edge = edge / np.max(edge)
edge = np.power(edge, 1)
edge *= 255
edge = edge.astype(np.uint8)

edge[edge > 255] = 255
edge = edge.astype(np.uint8)

threshEdge[threshEdge > 0] = 255
threshEdge[threshEdge <= 0] = 0
threshEdge = threshEdge.astype(np.uint8)

edge_binary[edge_binary > 0] = 255
edge_binary[edge_binary <= 0] = 0
edge_binary = edge_binary.astype(np.uint8)

edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = edge.astype(np.uint8)

edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = np.round(edge)
edge = edge.astype(np.uint8)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------")  # 30個
