"""
cv2.blur()             # 均值濾波器, 平均模糊
cv2.GaussianBlur()     # 高斯濾波器, 高斯模糊
cv2.bilateralFilter()  # 雙邊濾波器
cv2.boxFilter()        # 平均模糊
cv2.medianBlur()       # 中值濾波器
cv2.filter2D()         # 2D濾波核
"""

import cv2

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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("blur 效果 1")
r = cv2.blur(image, (5, 5))

plt.figure("blur 效果", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("blur 效果 1")
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("blur 效果 2")
image_blur_05 = cv2.blur(image, (5, 5))
image_blur_30 = cv2.blur(image, (30, 30))

plt.figure("blur 效果", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("blur 效果 2")
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("blur 效果 2")
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"

img = cv2.imread(filename)
output1 = cv2.blur(img, (5, 5))  # 指定區域單位為 (5, 5)
output2 = cv2.blur(img, (25, 25))  # 指定區域單位為 (25, 25)

cv2.imshow("image1", output1)
cv2.imshow("image2", output2)

cv2.waitKey(0)  # 按下任意鍵停止
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 刪除影像雜訊_濾波
print("------------------------------------------------------------")  # 60個

filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("使用 均值濾波器.blur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (3, 3))  # 使用 3x3 濾波核
dst2 = cv2.blur(src, (5, 5))  # 使用 5x5 濾波核
dst3 = cv2.blur(src, (7, 7))  # 使用 7x7 濾波核
dst4 = cv2.blur(src, (29, 29))  # 使用 29x29 濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)
cv2.imshow("dst 29 x 29", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.boxFilter() ST
print("------------------------------------------------------------")  # 60個


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("boxFilter 效果 1")
image_boxFilter = cv2.boxFilter(image, -1, (5, 5))

plt.figure("new20 boxFilter 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 1")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("boxFilter 效果 2")
image_boxFilter = cv2.boxFilter(image, -1, (5, 5), normalize=0)

plt.figure("new21 boxFilter 效果 2", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 2")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("boxFilter 效果 3")
image_boxFilter = cv2.boxFilter(image, -1, (2, 2), normalize=0)

plt.figure("new22 boxFilter 效果 3", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 3")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 方框濾波器.boxFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.boxFilter(src, -1, (2, 2), normalize=0)  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(src, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(src, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核

cv2.imshow("dst 2 x 2", dst1)
cv2.imshow("dst 3 x 3", dst2)
cv2.imshow("dst 5 x 5", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.medianBlur() ST
print("------------------------------------------------------------")  # 60個


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("medianBlur 效果 1")
image_medianBlur = cv2.medianBlur(image, 3)

plt.figure("new23 medianBlur 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("medianBlur 效果 1")
plt.imshow(cv2.cvtColor(image_medianBlur, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("median 跑一陣子")


def get_median(data):
    data.sort()
    half = len(data) // 2
    return data[half]


# 計算灰度圖像的中值濾波
def my_median_blur_gray(image, size):
    data = []
    sizepart = int(size / 2)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    # 首先判斷所以是否超出范圍，也可以事先對圖像進行零填充
                    if (i + ii - sizepart) < 0 or (i + ii - sizepart) >= image.shape[0]:
                        pass
                    elif (j + jj - sizepart) < 0 or (j + jj - sizepart) >= image.shape[
                        1
                    ]:
                        pass
                    else:
                        data.append(image[i + ii - sizepart][j + jj - sizepart])
            # 取每個區域內的中位數
            image[i][j] = int(get_median(data))
            data = []
    return image


# 計算彩色圖像的中值濾波
def my_median_blur_RGB(image, size):
    (b, r, g) = cv2.split(image)
    blur_b = my_median_blur_gray(b, size)
    blur_r = my_median_blur_gray(r, size)
    blur_g = my_median_blur_gray(g, size)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result


image_test1 = cv2.imread("data/worm.jpg")
# 調用自定義函數
my_image_blur_median = my_median_blur_RGB(image_test1, 5)
# 調用庫函數
computer_image_blur_median = cv2.medianBlur(image_test1, 5)
fig = plt.figure("new41")
fig.add_subplot(131)
plt.title("原圖")
plt.imshow(image_test1)
fig.add_subplot(132)
plt.title("自定義函數濾波")
plt.imshow(my_image_blur_median)
fig.add_subplot(133)
plt.title("庫函數濾波")
plt.imshow(computer_image_blur_median)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = np.ones((3, 3), np.float32) * 150
src[1, 1] = 20
print(f"原陣列 src = \n {src}")

dst = cv2.medianBlur(src, 3)
print(f"中值濾波後 dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.medianBlur(src, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(src, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(src, 7)  # 使用邊長是 7 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
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
show()

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
show()

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
show()

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
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

# 原圖
image = cv2.imread(filename, 0)  # 讀成黑白, 一維
print(image.shape)

image = cv2.imread(filename)  # 讀成彩色, 三維
print(image.shape)

image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure("影像處理", figsize=(16, 12))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 高斯濾波器.GaussianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 使用 3 x 3 的濾波核
dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)  # 使用 5 x 5 的濾波核
dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)  # 使用 29 x 29 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 15 x 15", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur()")

src = cv2.imread("data/border.jpg")

dst1 = cv2.blur(src, (3, 3))  # 均值濾波器 - 3x3 濾波核
dst2 = cv2.blur(src, (7, 7))  # 均值濾波器 - 7x7 濾波核

dst3 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 高斯濾波器 - 3x3 的濾波核
dst4 = cv2.GaussianBlur(src, (7, 7), 0, 0)  # 高斯濾波器 - 7x7 的濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 7 x 7", dst2)
cv2.imshow("Gauss dst 3 x 3", dst3)
cv2.imshow("Gauss dst 7 x 7", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur() / 雙邊濾波器.bilateralFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (15, 15))  # 均值濾波器
dst2 = cv2.GaussianBlur(src, (15, 15), 0, 0)  # 高斯濾波器
dst2 = cv2.bilateralFilter(src, 15, 100, 100)  # 雙邊濾波器

cv2.imshow("blur", dst1)
cv2.imshow("GaussianBlur", dst1)
cv2.imshow("bilateralFilter", dst2)

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個
# bilateralFilter ST
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("bilateralFilter 效果 1")
image_bilateralFilter = cv2.bilateralFilter(image, 25, 100, 100)

plt.figure("new24 bilateralFilter 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("bilateralFilter 效果 1")
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp"
image = cv2.imread(filename)

print("bilateralFilter 效果 2")
image_bilateralFilter = cv2.bilateralFilter(image, 55, 100, 100)

plt.figure("new25 bilateralFilter 效果 2", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("bilateralFilter 效果 2")
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

show()


print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)

cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.imshow("image3", output3)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# bilateralFilter SP
print("------------------------------------------------------------")  # 60個

print("使用 2D濾波核.filter2D()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(src, -1, kernel)  # 自定義濾波器
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()

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

show()
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

show()

print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

