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
# dst_canny = cv2.Canny(image, 50, 100)  # minVal=50, maxVal=100

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("Canny 1")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("Canny 2")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("Canny 3")

show()

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


# 輸出邊緣和結構信息

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure("輸出邊緣和結構信息", figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

o = cv2.drawContours(image, contours, -1, RED, 5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("輸出邊緣和結構信息")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(
    binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 5)
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/loc3.jpg")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(image.shape, np.uint8)

mask = cv2.drawContours(mask, contours, -1, WHITE, -1)

loc = cv2.bitwise_and(image, mask)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_BGR2RGB))
plt.title("mask")

plt.subplot(133)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("location")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/moments.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

print("觀察各個輪廓的矩（moments）:")
for i in range(n):
    print("輪廓" + str(i) + "的矩:\n", cv2.moments(contours[i]))
print("觀察各個輪廓的面積:")
for i in range(n):
    print("輪廓" + str(i) + "的面積:%d" % cv2.moments(contours[i])["m00"])

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    print("contours[" + str(i) + "]面積=", cv2.contourArea(contours[i]))
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
    index = "22" + str(i + 2)
    plt.subplot(int(index))
    plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
    plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 篩選出大于特定大小的輪廓

image = cv2.imread("data/contours.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(
    gray,
    thresh,
    maxval,
)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)  # 獲取輪廓個數
print("總共找到", n, "個輪廓")

contoursImg = []
for i in range(n):
    temp = np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    if cv2.contourArea(contours[i]) > 15000:
        # cv2.imshow("contours[" + str(i) + "]", contoursImg[i])
        index = "22" + str(i + 2)
        plt.subplot(int(index))
        plt.imshow(cv2.cvtColor(contoursImg[i], cv2.COLOR_BGR2RGB))
        plt.title("輪廓 " + str(i + 1))

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cs1.bmp")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

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
print("------------------------------------------------------------")  # 60個

# ----------------計算圖像1的Hu矩-------------------
image1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()

# ----------------計算圖像2的Hu矩-------------------
image2 = cv2.imread("data/cs3.bmp")  # 彩色讀取
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()

# ----------------計算圖像3的Hu矩-------------------
filename = filename_lena_gray

image3 = cv2.imread(filename)  # 彩色讀取
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階
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

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("original1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("original2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("original3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Opencv之利用matchshape算子实现简单的形状匹配
"""
使用OpenCV的matchShape算子进行形状匹配。
通过将待识别图像和模板图像转换为灰度并进行阈值处理，然后找到轮廓，
最后通过比较轮廓的Hu不变矩来确定匹配度。匹配分值越小，轮廓越相似。
matchShapes函数适用于识别大物体的形状，但对纹理复杂的图像识别率较低。
"""

# --------------讀取3幅原始圖像--------------------
image1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
image2 = cv2.imread("data/cs2.bmp")  # 彩色讀取
image3 = cv2.imread("data/cc.bmp")  # 彩色讀取

# ----------打印3幅原始圖像的shape屬性值-------------
print("image1.shape=", image1.shape)
print("image2.shape=", image2.shape)
print("image3.shape=", image3.shape)

# --------------色彩空間轉換--------------------
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# -------------進行Hu矩匹配--------------------
ret0 = cv2.matchShapes(gray1, gray1, 1, 0.0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0.0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0.0)

# --------------打印差值--------------------
print("相同圖像的matchShape=", ret0)
print("相似圖像的matchShape=", ret1)
print("不相似圖像的matchShape=", ret2)

# --------------顯示3幅原始圖像--------------------
plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("original1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("original2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("original3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("opencv 輪廓比對")

img_patterns = cv2.imread("data/patterns.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

patterns, _ = cv2.findContours(img_patterns, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_targets = cv2.imread("data/targets.png", cv2.IMREAD_GRAYSCALE)  # 灰階讀取

targets, _ = cv2.findContours(img_targets, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

patterns = [pattern - np.min(pattern, 0, keepdims=True) for pattern in patterns]
targets = [target - np.min(target, 0, keepdims=True) for target in targets]

patterns_simple = [cv2.approxPolyDP(pattern, 5, True) for pattern in patterns]
targets_simple = [cv2.approxPolyDP(target, 8, True) for target in targets]


for method in [1, 2, 3]:
    method_str = "CONTOURS_MATCH_I{}".format(method)
    method = getattr(cv2, method_str)
    scores = [
        cv2.matchShapes(targets_simple[0], patterns_simple[pidx], method, 0)
        for pidx in range(5)
    ]
    print(method_str, ", ".join("{: 8.4f}".format(score) for score in scores))

# CV_CONTOURS_MATCH_I1  11.3737,   0.3456,   0.0289,   1.0495,   0.0020
# CV_CONTOURS_MATCH_I2   4.8051,   2.2220,   0.0179,   0.3624,   0.0013
# CV_CONTOURS_MATCH_I3   0.9164,   0.4778,   0.0225,   0.4552,   0.0016

# %figonly=使用`matchShapes()`比較由`approxPolyDP()`近似之後的輪廓
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_aspect("equal")

width = 180
for tidx, (target, target_simple) in enumerate(zip(targets, targets_simple)):
    scores = []
    texts = []
    for pidx, (pattern, pattern_simple) in enumerate(zip(patterns, patterns_simple)):
        index = np.s_[:, 0, :]
        pattern2 = pattern[index]
        target2 = target[index]
        pattern_simple2 = pattern_simple[index]
        target_simple2 = target_simple[index]

        x0 = pidx * width + width
        y0 = tidx * width + width

        if tidx == 0:
            pattern_poly = plt.Polygon(pattern2 + [x0, 0], color="black", alpha=0.6)
            ax.add_patch(pattern_poly)
            text = ax.text(x0 + width * 0.3, -50, str(pidx), fontsize=14, ha="center")
        if pidx == 0:
            target_poly = plt.Polygon(target2 + [0, y0], color="g", alpha=0.6)
            ax.add_patch(target_poly)
            text = ax.text(-50, y0 + width * 0.3, str(tidx), fontsize=14, ha="center")

        pattern_simple_poly = plt.Polygon(
            pattern_simple2 + [x0, 0], facecolor="none", alpha=0.6
        )
        ax.add_patch(pattern_simple_poly)
        target_simple_poly = plt.Polygon(
            target_simple2 + [0, y0], facecolor="none", alpha=0.6
        )
        ax.add_patch(target_simple_poly)

        score = cv2.matchShapes(target_simple, pattern_simple, cv2.CONTOURS_MATCH_I3, 0)
        text = ax.text(
            x0 + width * 0.3,
            y0 + width * 0.2,
            "{:5.4f}".format(score),
            ha="center",
            va="center",
            fontsize=16,
        )
        scores.append(score)
        texts.append(text)
    best_index = np.argmin(scores)
    texts[best_index].set_color("red")

ax.relim()
ax.set_axis_off()
ax.autoscale()

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x + w, y]], [[x + w, y + h]], [[x, y + h]]])
cv2.drawContours(image, [brcnt], -1, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ---------------提取圖像輪廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ---------------構造矩形邊界------------------
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(image, (x, y), (x + w, y + h), RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("顯示矩形邊界")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
(x, y), radius = cv2.minEnclosingCircle(contours[0])
center = (int(x), int(y))
radius = int(radius)
cv2.circle(image, center, radius, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("圓圈圈出來")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

ellipse = cv2.fitEllipse(contours[0])
print("ellipse=", ellipse)
cv2.ellipse(image, ellipse, GREEN, 3)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("橢圓形圈出來")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
rows, cols = image.shape[:2]
[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int((-x * vy / vx) + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(image, (cols - 1, righty), (0, lefty), GREEN, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("直線貫通")

show()

print("------------------------------------------------------------")  # 60個

# some NG
image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area, trgl = cv2.minEnclosingTriangle(contours[0])
print("area=", area)
print("trgl:", trgl)
for i in range(0, 3):
    print("x")
    # cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), WHITE, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ----------------獲取輪廓-------------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# ----------------epsilon=0.1*周長-------------------------------
adp = image.copy()
epsilon = 0.1 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(232)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.1")

# ----------------epsilon=0.09*周長-------------------------------
adp = image.copy()
epsilon = 0.09 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(233)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.09")

# ----------------epsilon=0.055*周長-------------------------------
adp = image.copy()
epsilon = 0.055 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(234)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.055")

# ----------------epsilon=0.05*周長-------------------------------
adp = image.copy()
epsilon = 0.05 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(235)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.05")

# ----------------epsilon=0.02*周長-------------------------------
adp = image.copy()
epsilon = 0.02 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], 0, RED, 2)

plt.subplot(236)
plt.imshow(cv2.cvtColor(adp, cv2.COLOR_BGR2RGB))
plt.title("result0.02")

show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/contours.bmp")  # 彩色讀取

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])  # 返回坐標值
print("returnPoints為默認值True時返回值hull的值：\n", hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)  # 返回索引值
print("returnPoints為False時返回值hull的值：\n", hull2)

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# --------------提取輪廓------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# --------------尋找凸包，得到凸包的角點------------------
hull = cv2.convexHull(contours[0])
# --------------繪製凸包------------------
cv2.polylines(o, [hull], True, GREEN, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("顯示凸包")

show()

print("------------------------------------------------------------")  # 60個

# ----------------原圖--------------------------
img = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# ----------------構造輪廓--------------------------
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
    cv2.line(img, start, end, RED, 2)
    cv2.circle(img, far, 5, BLUE, -1)

plt.subplot(122)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("顯示結果")
show()

print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# --------------凸包----------------------
image1 = o.copy()
hull = cv2.convexHull(contours[0])
cv2.polylines(image1, [hull], True, GREEN, 2)
print("使用函數cv2.convexHull()構造的多邊形是否是凸包：", cv2.isContourConvex(hull))

plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("result1")

# ------------逼近多邊形--------------------
image2 = o.copy()
epsilon = 0.01 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
image2 = cv2.drawContours(image2, [approx], 0, RED, 2)
print("使用函數cv2.approxPolyDP()構造的多邊形是否是凸包：", cv2.isContourConvex(approx))

plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("result2")

show()

print("------------------------------------------------------------")  # 60個

# ----------------原始圖像-------------------------
o = cv2.imread("data/cs1.bmp")  # 彩色讀取

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)

# ----------------內部點A的距離-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)
# ----------------外部點B的距離-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)
# ------------正好處于邊緣上的點C的距離-----------------
distC = cv2.pointPolygonTest(hull, (423, 112), True)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的


plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("邊緣")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs1.bmp")  # 彩色讀取

# ----------------獲取凸包------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
hull = cv2.convexHull(contours[0])

image = cv2.imread("data/cs1.bmp", 0)  # 灰階讀取

image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.polylines(image, [hull], True, GREEN, 2)
# ----------------內部點A與多邊形的關系-------------------------
distA = cv2.pointPolygonTest(hull, (300, 150), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "A", (300, 150), font, 1, GREEN, 3)
print("distA=", distA)
# ----------------外部點B與多邊形的關系-------------------------
distB = cv2.pointPolygonTest(hull, (300, 250), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "B", (300, 250), font, 1, GREEN, 3)
print("distB=", distB)
# ----------------邊緣線上點C與多邊形的關系----------------------
distC = cv2.pointPolygonTest(hull, (423, 112), False)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, "C", (423, 112), font, 1, GREEN, 3)
print("distC=", distC)
# print(hull)   #測試邊緣到底在哪里，然后再使用確定位置的

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("邊緣")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# -----------原始圖像o1邊緣--------------------
o1 = cv2.imread("data/cs1.bmp")  # 彩色讀取

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours1, hierarchy = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt1 = contours1[0]

# -----------原始圖像o2邊緣--------------------
o2 = cv2.imread("data/cs3.bmp")  # 彩色讀取

gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours2, hierarchy = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt2 = contours2[0]

# -----------原始圖像o3邊緣--------------------
o3 = cv2.imread("data/hand.bmp")  # 彩色讀取

gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(o2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(o3, cv2.COLOR_BGR2RGB))
plt.title("原圖3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o1 = cv2.imread("data/cs1.bmp")  # 彩色讀取
o2 = cv2.imread("data/cs3.bmp")  # 彩色讀取
o3 = cv2.imread("data/hand.bmp")  # 彩色讀取

# -----------色彩轉換--------------------
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)  # 轉灰階
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)  # 轉灰階

# -----------閾值處理--------------------

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary1 = cv2.threshold(gray1, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary2 = cv2.threshold(gray2, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理
ret, binary3 = cv2.threshold(gray3, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(o2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(o3, cv2.COLOR_BGR2RGB))
plt.title("原圖3")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.rectangle(o, (x, y), (x + w, y + h), WHITE, 3)

aspectRatio = float(w) / h
print(aspectRatio)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
x, y, w, h = cv2.boundingRect(contours[0])
cv2.drawContours(o, contours[0], -1, RED, 3)
cv2.rectangle(o, (x, y), (x + w, y + h), BLUE, 3)

rectArea = w * h
cntArea = cv2.contourArea(contours[0])
extend = float(cntArea) / rectArea
print(extend)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/hand.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(o, contours[0], -1, RED, 3)
cntArea = cv2.contourArea(contours[0])
hull = cv2.convexHull(contours[0])
hullArea = cv2.contourArea(hull)
cv2.polylines(o, [hull], True, GREEN, 2)
solidity = float(cntArea) / hullArea
print(solidity)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(o, contours[0], -1, RED, 3)
cntArea = cv2.contourArea(contours[0])
equiDiameter = np.sqrt(4 * cntArea / np.pi)
print(equiDiameter)
cv2.circle(o, (100, 100), int(equiDiameter / 2), RED, 3)  # 展示等直徑大小的圓

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cc.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
cv2.ellipse(o, ellipse, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
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
o = cv2.imread("data/cc.bmp")  # 彩色讀取

# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = np.transpose(np.nonzero(mask1))
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = np.transpose(np.nonzero(mask2))
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))
plt.title("mask1")

plt.subplot(133)
plt.imshow(cv2.cvtColor(mask2, cv2.COLOR_BGR2RGB))
plt.title("mask2")

show()

print("------------------------------------------------------------")  # 60個
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

o = cv2.imread("data/cc.bmp")  # 彩色讀取

# -----------------獲取輪廓------------------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

# -----------------繪製空心輪廓------------------------
mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], 0, 255, 2)
pixelpoints1 = cv2.findNonZero(mask1)
print("pixelpoints1.shape=", pixelpoints1.shape)
print("pixelpoints1=\n", pixelpoints1)

# -----------------繪製實心輪廓---------------------
mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], 0, 255, -1)
pixelpoints2 = cv2.findNonZero(mask2)
print("pixelpoints2.shape=", pixelpoints2.shape)
print("pixelpoints2=\n", pixelpoints2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(mask1, cv2.COLOR_BGR2RGB))
plt.title("mask1")

plt.subplot(133)
plt.imshow(cv2.cvtColor(mask2, cv2.COLOR_BGR2RGB))
plt.title("mask2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/ct.png")  # 彩色讀取

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
masko = cv2.drawContours(masko, [cnt], -1, WHITE, -1)
loc = cv2.bitwise_and(o, masko)

# 顯示灰度結果
# loc=cv2.bitwise_and(gray,mask)
# cv2.imshow("mask",loc)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/ct.png")  # 彩色讀取

# --------獲取輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[2]
# --------使用掩膜獲取感興趣區域的均值-----------------
mask = np.zeros(gray.shape, np.uint8)  # 構造mean所使用的掩膜，必須是單通道的
cv2.drawContours(mask, [cnt], 0, WHITE, -1)
meanVal = cv2.mean(o, mask=mask)  # mask是區域，所以必須是單通道的
print("meanVal=\n", meanVal)
# --------使用掩膜獲取感興趣區域并顯示-----------------
masko = np.zeros(o.shape, np.uint8)
cv2.drawContours(masko, [cnt], -1, WHITE, -1)
loc = cv2.bitwise_and(o, masko)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(loc, cv2.COLOR_BGR2RGB))
plt.title("mask")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

o = cv2.imread("data/cs1.bmp")  # 彩色讀取

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("原圖")

# --------獲取并繪製輪廓-----------------
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
cv2.putText(o, "A", leftmost, font, 1, RED, 2)
cv2.putText(o, "B", rightmost, font, 1, RED, 2)
cv2.putText(o, "C", topmost, font, 1, RED, 2)
cv2.putText(o, "D", bottommost, font, 1, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))
plt.title("result")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = filename1

print("取兩圖的影像差異 diff")

filename_diff1 = "C:/_git/vcs/_1.data/______test_files1/compare/compare1.jpg"
filename_diff2 = "C:/_git/vcs/_1.data/______test_files1/compare/compare2.jpg"

img1 = cv2.imread(filename_diff1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img2 = cv2.imread(filename_diff2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

print("image1.shape內容 :", img1.shape)
print("image2.shape內容 :", img2.shape)

# 比較並顯示差異影像
diff = cv2.absdiff(img1, img2)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(diff, cv2.COLOR_BGR2RGB))
plt.title("Difference")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("疊合")

filename_add1 = "C:/_git/vcs/_1.data/______test_files1/ims02.bmp"
filename_add2 = "C:/_git/vcs/_1.data/______test_files1/ims03.bmp"

img1 = cv2.imread(filename_add1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取
img2 = cv2.imread(filename_add2, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

blended = cv2.addWeighted(img1, 1, img2, 1, 0)

plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(blended, cv2.COLOR_BGR2RGB))
plt.title("疊合")

show()

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

img = cv2.imread(filename2)  # 彩色讀取

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉灰階

img = cv2.medianBlur(img, 7)  # 模糊化，去除雜訊
# Laplacian
output = cv2.Laplacian(img, -1, 1, 5)  # 偵測邊緣
# Sobel
output = cv2.Sobel(img, -1, 1, 1, 1, 7)  # 偵測邊緣
# Canny
output = cv2.Canny(img, 36, 36)  # 偵測邊緣

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image1 = cv2.imread(filename2)  # 彩色讀取

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉灰階

# image2 = cv2.cvtColor(image1, 6)  # 也可以用數字對照 6 表示轉換成灰階
# 套用 medianBlur() 中值模糊
image3 = cv2.medianBlur(image2, 7)  # 模糊化，去除雜訊 7, 25 彩色黑白皆可
image4 = cv2.Canny(image3, 36, 36)  # 偵測邊緣

# 套用自適應二值化黑白影像
image5 = cv2.adaptiveThreshold(
    image3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("轉成灰階")

plt.subplot(233)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("模糊化，去除雜訊")

plt.subplot(234)
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))
plt.title("偵測邊緣")

plt.subplot(235)
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))
plt.title("自適應二值化黑白影像")

plt.subplot(236)
plt.title("")

plt.suptitle("相加")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("準備使用Trackbar")


def do_trackbar_event1(val):
    print("數值 :", val, end=" ")


image = cv2.imread(filename2)
cv2.imshow("OpenCV", image)

cv2.createTrackbar("Threshold ", "OpenCV", 0, 100, do_trackbar_event1)
cv2.setTrackbarPos("Threshold ", "OpenCV", 50)  # 設定預設值

# 取得Trackbar數值
value = cv2.getTrackbarPos("Threshold ", "OpenCV")
do_trackbar_event1(value)  # 套用一次設定值

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

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

# 篩選出大于特定大小的輪廓

image = cv2.imread("data/contours0.bmp")  # 彩色讀取
cv2.imshow("original", image)

# --------------獲取輪廓--------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉灰階

thresh = 127  # 定義閾值, 閾值以上為全白255, 閾值以下為全黑0
ret, binary = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)  # 二值化處理

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
    contoursImg[i] = cv2.drawContours(contoursImg[i], contours, i, WHITE, 3)
    if cv2.arcLength(contours[i], True) > cntLenAvr:
        print(i)
        cv2.imshow("contours[" + str(i) + "]", contoursImg[i])

cv2.waitKey()
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
