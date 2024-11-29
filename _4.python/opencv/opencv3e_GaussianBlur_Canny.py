"""

GaussianBlur

Canny


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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

image = cv2.imread(filename, 0)

# 高斯模糊
image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure("影像處理", figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

# Gaussian lowpass filter

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

kernel_size = (5, 5)  # 卷積的矩陣大小 ksize 指定區域單位 ( 必須是大於 1 的奇數 )
sigma = 0  # sigma值     sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
image_blur = cv2.GaussianBlur(image, kernel_size, 0)  # 執行高斯模糊化

plt.figure("GaussianBlur", figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖, 有Noise")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure("GaussianBlur", figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖, 有Noise")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp"
image = cv2.imread(filename)

image_blur = cv2.GaussianBlur(image, (55, 55), 0)  # 執行高斯模糊化

plt.figure("GaussianBlur", figsize=(8, 6))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur")

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 執行高斯模糊化


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)  # 執行高斯模糊化
    detected_edges = cv2.Canny(
        detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size
    )
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # 只需在原始图像的边缘添加一些颜色
    cv2.imshow("canny demo", dst)


original_img = cv2.imread("lena.png", 0)
# canny(): 边缘检测
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)  # 執行高斯模糊化
canny = cv2.Canny(img1, 50, 150)

print("------------------------------------------------------------")  # 60個

print("CannyThreshold")


def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0)  # 執行高斯模糊化
    detected_edges = cv2.Canny(
        detected_edges, lowThreshold, lowThreshold * ratio, apertureSize=kernel_size
    )
    dst = cv2.bitwise_and(img, img, mask=detected_edges)  # 只需在原始圖像的邊緣添加一些顏色
    cv2.imshow("canny demo", dst)


lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3
img = cv2.imread("data/lena.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("canny demo")
cv2.createTrackbar(
    "Min threshold", "canny demo", lowThreshold, max_lowThreshold, CannyThreshold
)

CannyThreshold(0)  # 初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("sharpening")


# 圖像銳化函數
def my_not_sharpen(image, k, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  # 執行高斯模糊化
    # 注意不能直接用減法，對于圖像格式結果為負時會自動加上256
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    # 兩個矩陣中有一個不是圖像格式，則結果就不會轉換為圖像格式
    sharpen_image = image + k * model
    sharpen_image = cv2.convertScaleAbs(sharpen_image)
    return sharpen_image


# 提取圖像邊界信息函數
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  # 執行高斯模糊化
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv2.convertScaleAbs(model)
    return model


original_image_lena = cv2.imread("data/lena.png", 0)

# 獲得圖像邊界信息
edge_image_lena = my_get_model(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_not_sharpen(original_image_lena, 3)

# 顯示結果
plt.subplot(131)
plt.title("原始圖像")
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title("邊緣檢測")
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title("非銳化")
plt.imshow(sharpen_image_lena)
plt.show()


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

# 原圖
image = cv2.imread(filename, 0)  # 讀成黑白, 一維
print(image.shape)
image = cv2.imread(filename)  # 讀成彩色, 三維
print(image.shape)

# 高斯模糊，Canny边缘检测需要的
image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure("影像處理", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("GaussianBlur")
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


"""
print("gaussion blur")

print('跑很久 skip')

#高斯濾波函數
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2*sigma**2)) / (2*math.pi*sigma**2)

#產生高斯濾波矩陣
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    #根據尺寸和sigma值計算高斯矩陣
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i-n, j-n, sigma)
    #將高斯矩陣歸一化
    blur_retric = blur_retric / blur_retric[0][0]
    #將高斯矩陣轉換為整數
    blur_retric = blur_retric.astype(np.uint32)
    #返回高斯矩陣
    return blur_retric

#計算灰度圖像的高斯濾波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    #計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    #條件語句為判斷模板對應的值是否超出邊界
                    if (i+ii-sizepart)<0 or (i+ii-sizepart)>=image.shape[0]:
                        pass
                    elif (j+jj-sizepart)<0 or (j+jj-sizepart)>=image.shape[1]:
                        pass
                    else:
                        data += image[i+ii-sizepart][j+jj-sizepart] * blur_retric[ii][jj]
            image[i][j] = data / n
            data = 0
    #返回變換后的圖像矩陣
    return image

#計算彩色圖像的高斯濾波
def my_gaussion_blur_RGB(image, size, sigma):
    (b ,r, g) = cv2.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result

image_test1 = cv2.imread('data/lena.png')
#進行高斯濾波器比較
my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
computer_image_blur_gaussion = cv2.GaussianBlur(image_test1, (5, 5), 0.75)  #執行高斯模糊化

fig = plt.figure(figsize = (20, 15))

fig.add_subplot(131)
plt.title('原始圖像')
plt.imshow(image_test1)

fig.add_subplot(132)
plt.title('自定義高斯濾波器')
plt.imshow(my_image_blur_gaussion)

fig.add_subplot(133)
plt.title('庫高斯濾波器')
plt.imshow(computer_image_blur_gaussion)

plt.show()
"""
print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
output1 = cv2.adaptiveThreshold(
    img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
img_gray2 = cv2.medianBlur(img_gray, 5)  # 模糊化
output2 = cv2.adaptiveThreshold(
    img_gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.GaussianBlur(img, (5, 5), 0)  # 指定區域單位為 (5, 5)
output2 = cv2.GaussianBlur(img, (25, 25), 0)  # 指定區域單位為 (25, 25)
cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.medianBlur(img, 5)  # 模糊程度為 5
output2 = cv2.medianBlur(img, 25)  # 模糊程度為 25
cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("高斯模糊, 邊緣模糊化")
"""
GaussianBlur() 高斯模糊 
使用 OpenCV 的 GaussianBlur() 方法，可以使用高斯分佈進行模糊化的計算，
指定模糊區域單位 ( 必須是大於 1 的奇數 ) 後就能產生不同程度的模糊效果

cv2.GaussianBlur(img, ksize, sigmaX, sigmaY)
# img 來源影像
# ksize 指定區域單位 ( 必須是大於 1 的奇數 )
# sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
"""
num_bins = 256  # 直方圖顯示時的束數

L = 256
image0 = np.zeros((L * 3, L * 3, 1), dtype="uint8")  # 建立 黑色畫布

cv2.rectangle(image0, (L, 0), (L * 2, L * 3), (255, 255, 255), -1)

W, H, sigmaX, sigmaY = 101, 101, 0, 0  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊

num_bins = 256  # 直方圖顯示時的束數

plt.figure(figsize=(10, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖Gaussian模糊")

plt.subplot(223)
plt.title("調整 W, H")
plt.plot(image0[200, :].ravel(), "k")

W, H, sigmaX, sigmaY = 101, 101, 0, 0  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "r")

W, H, sigmaX, sigmaY = 201, 201, 0, 0  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "g")

W, H, sigmaX, sigmaY = 301, 301, 0, 0  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "b")

plt.subplot(224)
plt.title("調整 sigmaX, sigmaY")
plt.plot(image0[200, :].ravel(), "k")

W, H, sigmaX, sigmaY = 101, 101, 0, 0  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "r")

W, H, sigmaX, sigmaY = 101, 101, 100, 100  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "g")

W, H, sigmaX, sigmaY = 101, 101, 200, 200  # W, H 必須為單數
image1 = cv2.GaussianBlur(image0, (W, H), sigmaX, sigmaY)  # 進行高斯模糊
plt.plot(image1[200, :].ravel(), "b")

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Canny")
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

image = cv2.imread(filename, 0)

plt.figure("影像處理", figsize=(8, 6))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

# 高斯模糊，Canny边缘检测需要的
image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

# 进行边缘检测，减少图像空间中需要检测的点数量
image_canny = cv2.Canny(image_blur, 50, 150)

plt.subplot(122)
plt.title("Canny")
plt.imshow(cv2.cvtColor(image_canny, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

image_canny1 = cv2.Canny(image, 128, 200)
image_canny2 = cv2.Canny(image, 32, 128)

plt.figure("影像處理", figsize=(8, 6))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("Canny 1")
plt.imshow(cv2.cvtColor(image_canny1, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Canny 2")
plt.imshow(cv2.cvtColor(image_canny2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
