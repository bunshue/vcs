"""
cv2.blur()             # 均值濾波器, 平均模糊
cv2.GaussianBlur()     # 高斯濾波器, 高斯模糊
cv2.bilateralFilter()  # 雙邊濾波器
cv2.boxFilter()        # 方框濾波器, 平均模糊
cv2.medianBlur()       # 中值濾波器
cv2.filter2D()         # 2D濾波核
"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個
# cv2.blur()             # 均值濾波器, 平均模糊
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

dst = cv2.blur(image, (5, 5))

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 1")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_blur_05 = cv2.blur(image, (5, 5))  # 指定區域單位為 (5, 5)
image_blur_30 = cv2.blur(image, (30, 30))  # 指定區域單位為 (30, 30)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 刪除影像雜訊_濾波

print("使用 均值濾波器.blur()")

image = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("image", image)

dst1 = cv2.blur(image, (3, 3))  # 使用 3x3 濾波核
dst2 = cv2.blur(image, (5, 5))  # 使用 5x5 濾波核
dst3 = cv2.blur(image, (7, 7))  # 使用 7x7 濾波核
dst4 = cv2.blur(image, (29, 29))  # 使用 29x29 濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)
cv2.imshow("dst 29 x 29", dst4)

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("blur 3X3")

plt.subplot(233)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("blur 5X5")

plt.subplot(234)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("blur 7X7")

plt.subplot(235)
plt.imshow(cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB))
plt.title("blur 29X29")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.boxFilter()        # 方框濾波器, 平均模糊
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_boxFilter = cv2.boxFilter(image, -1, (5, 5))
# image_boxFilter = cv2.boxFilter(image, -1, (5, 5), normalize=0)
# image_boxFilter = cv2.boxFilter(image, -1, (2, 2), normalize=0)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))
plt.title("boxFilter 效果 1")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 方框濾波器.boxFilter()")

image = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("image", image)

dst1 = cv2.boxFilter(image, -1, (2, 2), normalize=0)  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(image, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(image, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核

cv2.imshow("dst 2 x 2", dst1)
cv2.imshow("dst 3 x 3", dst2)
cv2.imshow("dst 5 x 5", dst3)


plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("boxFilter 2X2")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("boxFilter 3X3")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("boxFilter 5X5")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# cv2.medianBlur() ST       # 中值濾波器
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_medianBlur = cv2.medianBlur(image, 3)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_medianBlur, cv2.COLOR_BGR2RGB))
plt.title("medianBlur 效果 1")

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


image_test1 = cv2.imread("data/worm.jpg")  # 彩色讀取

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

image = np.ones((3, 3), np.float32) * 150
image[1, 1] = 20
print(f"原陣列 image = \n {image}")

dst = cv2.medianBlur(image, 3)
print(f"中值濾波後 dst = \n {dst}")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

image = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("image", image)

dst1 = cv2.medianBlur(image, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(image, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(image, 7)  # 使用邊長是 7 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("medianBlur 3X3")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("medianBlur 5X5")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("medianBlur 7X7")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


image = cv2.imread(filename)  # 彩色讀取
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

output1 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

image_gray2 = cv2.medianBlur(image_gray, 5)  # 模糊化
output2 = cv2.adaptiveThreshold(
    image_gray2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cv2.imshow("image1", output1)
cv2.imshow("image2", output2)

# 3圖

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename)  # 彩色讀取

image_medianBlur1 = cv2.medianBlur(image, 5)  # 模糊程度為 5
image_medianBlur2 = cv2.medianBlur(image, 25)  # 模糊程度為 25

cv2.imshow("image1", image_medianBlur1)
cv2.imshow("image2", image_medianBlur2)

# 3圖

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# cv2.medianBlur() SP       # 中值濾波器
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.GaussianBlur() ST     # 高斯濾波器, 高斯模糊
print("------------------------------------------------------------")  # 60個

filename = filename_barbara

image = cv2.imread(filename, 0)  # 灰階讀取

# 高斯模糊
image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Gaussian lowpass filter

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

kernel_size = (5, 5)  # 卷積的矩陣大小 ksize 指定區域單位 ( 必須是大於 1 的奇數 )
sigma = 0  # sigma值     sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
image_blur = cv2.GaussianBlur(image, kernel_size, 0)  # 執行高斯模糊化

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖, 有Noise")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖, 有Noise")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title("高斯模糊 GaussianBlur")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp"

image = cv2.imread(filename)  # 彩色讀取

image_blur = cv2.GaussianBlur(image, (55, 55), 0)  # 執行高斯模糊化

plt.figure(figsize=(12, 8))
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

filename = filename2
filename = filename_barbara

image = cv2.imread(filename, 0)  # 灰階讀取  # 讀成黑白, 一維
print(image.shape)

image = cv2.imread(filename)  # 彩色讀取  # 讀成彩色, 三維
print(image.shape)

image_blur = cv2.GaussianBlur(image, (5, 5), 0)  # 執行高斯模糊化

plt.figure(figsize=(12, 8))

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

image = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("image", image)

dst1 = cv2.GaussianBlur(image, (3, 3), 0, 0)  # 使用 3 x 3 的濾波核
dst2 = cv2.GaussianBlur(image, (5, 5), 0, 0)  # 使用 5 x 5 的濾波核
dst3 = cv2.GaussianBlur(image, (29, 29), 0, 0)  # 使用 29 x 29 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 15 x 15", dst3)

plt.figure(figsize=(12, 8))

plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur 3X3")

plt.subplot(223)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur 5X5")

plt.subplot(224)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur 29X29")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur()")

image = cv2.imread("data/border.jpg")  # 彩色讀取

dst1 = cv2.blur(image, (3, 3))  # 均值濾波器 - 3x3 濾波核
dst2 = cv2.blur(image, (7, 7))  # 均值濾波器 - 7x7 濾波核

dst3 = cv2.GaussianBlur(image, (3, 3), 0, 0)  # 高斯濾波器 - 3x3 的濾波核
dst4 = cv2.GaussianBlur(image, (7, 7), 0, 0)  # 高斯濾波器 - 7x7 的濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 7 x 7", dst2)
cv2.imshow("Gauss dst 3 x 3", dst3)
cv2.imshow("Gauss dst 7 x 7", dst4)

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(232)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))
plt.title("blur 3X3")

plt.subplot(233)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))
plt.title("blur 7X7")

plt.subplot(234)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur 3X3")

plt.subplot(235)
plt.imshow(cv2.cvtColor(dst4, cv2.COLOR_BGR2RGB))
plt.title("GaussianBlur 7X7")

show()

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename)  # 彩色讀取

image_GaussianBlur1 = cv2.GaussianBlur(image, (5, 5), 0)  # 指定區域單位為 (5, 5)
image_GaussianBlur2 = cv2.GaussianBlur(image, (25, 25), 0)  # 指定區域單位為 (25, 25)

cv2.imshow("image1", image_GaussianBlur1)
cv2.imshow("image2", image_GaussianBlur2)

# 3圖

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("高斯模糊, 邊緣模糊化")
"""
GaussianBlur() 高斯模糊 
使用 OpenCV 的 GaussianBlur() 方法，可以使用高斯分佈進行模糊化的計算，
指定模糊區域單位 ( 必須是大於 1 的奇數 ) 後就能產生不同程度的模糊效果

cv2.GaussianBlur(image, ksize, sigmaX, sigmaY)
# image 來源影像
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

plt.figure(figsize=(12, 8))

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
# cv2.GaussianBlur() SP     # 高斯濾波器, 高斯模糊
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.bilateralFilter()  # 雙邊濾波器
print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur() / 雙邊濾波器.bilateralFilter()")

image = cv2.imread(filename2)  # 彩色讀取

cv2.imshow("image", image)

dst1 = cv2.blur(image, (15, 15))  # 均值濾波器
dst2 = cv2.GaussianBlur(image, (15, 15), 0, 0)  # 高斯濾波器
dst2 = cv2.bilateralFilter(image, 15, 100, 100)  # 雙邊濾波器

cv2.imshow("blur", dst1)
cv2.imshow("GaussianBlur", dst1)
cv2.imshow("bilateralFilter", dst2)

# 4圖

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_bilateralFilter = cv2.bilateralFilter(image, 25, 100, 100)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))
plt.title("bilateralFilter 效果 1")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp"

image = cv2.imread(filename)  # 彩色讀取

image_bilateralFilter = cv2.bilateralFilter(image, 55, 100, 100)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))
plt.title("bilateralFilter 效果 2")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename)  # 彩色讀取

image_bilateralFilter1 = cv2.bilateralFilter(image, 50, 0, 0)
image_bilateralFilter2 = cv2.bilateralFilter(image, 50, 50, 100)
image_bilateralFilter3 = cv2.bilateralFilter(image, 50, 100, 1000)

cv2.imshow("image1", image_bilateralFilter1)
cv2.imshow("image2", image_bilateralFilter2)
cv2.imshow("image3", image_bilateralFilter3)

# 4圖


cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
# bilateralFilter SP
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# cv2.filter2D() ST         # 2D濾波核
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename2)  # 彩色讀取

cv2.imshow("image", image)

kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(image, -1, kernel)  # 自定義濾波器
cv2.imshow("dst", dst)

# 2圖

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 圖形處理 二維卷積 使用filter2D()製作的各種圖形處理效果
用不同的卷积核可以得到 各种不同的图像处理效果。
OpenCV提供了 filter2D()来完成图像的卷积运算，调用方式如下：
filter2D(src, ddepth, kernel[, dst[, anchor[, delta[, borderType]]]])
    anchor参数指定卷积核的锚点位置，当它为默认值(-1，-1)时， 以卷积核的中心为锚点
使用filter2D()制作的各种图像处理效果
"""
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
src = cv2.imread(filename3)  # 彩色讀取

kernel1_name = "低通濾波器"
kernel1 = np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) * 0.1
kernel2_name = "高通濾波器"
kernel2 = np.array([[0.0, -1, 0], [-1, 5, -1], [0, -1, 0]])
kernel3_name = "邊緣檢驗"
kernel3 = np.array([[-1.0, -1, -1], [-1, 8, -1], [-1, -1, -1]])

dst1 = cv2.filter2D(src, -1, kernel1)
dst2 = cv2.filter2D(src, -1, kernel2)
dst3 = cv2.filter2D(src, -1, kernel3)

plt.figure(figsize=(12, 5))

plt.subplot(131)
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel1_name)

plt.subplot(132)
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel2_name)

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))  # 先轉換成RGB再顯示
plt.title(kernel3_name)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

image = cv2.imread(filename_lena_gray)  # 彩色讀取

print("filter2D 效果")
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))
plt.title("filter2D 效果")

plt.suptitle("filter2D 效果")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename_barbara, cv2.COLOR_BGR2GRAY)  # 灰階讀取

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)  # 水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)  # 垂直值一樣, 偵測垂直的邊緣

print("filter2D 效果")

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure(figsize=(12, 8))

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))
plt.title("Prewitt_horizon")
# 躺平的書本的邊緣有被強調出來

plt.subplot(133)
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))
plt.title("Prewitt_vertical")
# 直放的書本的邊緣有被強調出來

show()


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# cv2.filter2D() SP         # 2D濾波核
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
print("gaussion blur")

print("跑很久 skip")


# 高斯濾波函數
def my_function_gaussion(x, y, sigma):
    return math.exp(-(x**2 + y**2) / (2 * sigma**2)) / (2 * math.pi * sigma**2)


# 產生高斯濾波矩陣
def my_get_gaussion_blur_retric(size, sigma):
    n = size // 2
    blur_retric = np.zeros([size, size])
    # 根據尺寸和sigma值計算高斯矩陣
    for i in range(size):
        for j in range(size):
            blur_retric[i][j] = my_function_gaussion(i - n, j - n, sigma)
    # 將高斯矩陣歸一化
    blur_retric = blur_retric / blur_retric[0][0]
    # 將高斯矩陣轉換為整數
    blur_retric = blur_retric.astype(np.uint32)
    # 返回高斯矩陣
    return blur_retric


# 計算灰度圖像的高斯濾波
def my_gaussion_blur_gray(image, size, sigma):
    blur_retric = my_get_gaussion_blur_retric(size, sigma)
    n = blur_retric.sum()
    sizepart = size // 2
    data = 0
    # 計算每個像素點在經過高斯模板變換后的值
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            for ii in range(size):
                for jj in range(size):
                    # 條件語句為判斷模板對應的值是否超出邊界
                    if (i + ii - sizepart) < 0 or (i + ii - sizepart) >= image.shape[0]:
                        pass
                    elif (j + jj - sizepart) < 0 or (j + jj - sizepart) >= image.shape[
                        1
                    ]:
                        pass
                    else:
                        data += (
                            image[i + ii - sizepart][j + jj - sizepart]
                            * blur_retric[ii][jj]
                        )
            image[i][j] = data / n
            data = 0
    # 返回變換后的圖像矩陣
    return image


# 計算彩色圖像的高斯濾波
def my_gaussion_blur_RGB(image, size, sigma):
    (b, r, g) = cv2.split(image)
    blur_b = my_gaussion_blur_gray(b, size, sigma)
    blur_r = my_gaussion_blur_gray(r, size, sigma)
    blur_g = my_gaussion_blur_gray(g, size, sigma)
    result = cv2.merge((blur_b, blur_r, blur_g))
    return result


image_test1 = cv2.imread("data/lena.png")  # 彩色讀取

# 進行高斯濾波器比較
my_image_blur_gaussion = my_gaussion_blur_RGB(image_test1, 5, 0.75)
computer_image_blur_gaussion = cv2.GaussianBlur(image_test1, (5, 5), 0.75)  # 執行高斯模糊化

fig = plt.figure(figsize=(12, 8))

fig.add_subplot(131)
plt.title("原始圖像")
plt.imshow(image_test1)

fig.add_subplot(132)
plt.title("自定義高斯濾波器")
plt.imshow(my_image_blur_gaussion)

fig.add_subplot(133)
plt.title("庫高斯濾波器")
plt.imshow(computer_image_blur_gaussion)

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("使用Trackbar OK")


def do_trackbar_event1(val):
    # print("數值 :", val, end=" ")
    if val > 0:
        dst = cv2.blur(image, (val, val))
        cv2.imshow("OpenCV", dst)
    else:
        cv2.imshow("OpenCV", image)


image = cv2.imread(filename2)  # 彩色讀取
cv2.imshow("OpenCV", image)

cv2.createTrackbar("Threshold ", "OpenCV", 0, 30, do_trackbar_event1)
cv2.setTrackbarPos("Threshold ", "OpenCV", 5)  # 設定預設值

# 取得Trackbar數值
value = cv2.getTrackbarPos("Threshold ", "OpenCV")
do_trackbar_event1(value)  # 套用一次設定值

while True:
    k = cv2.waitKey(1)
    if k == ESC:
        break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


blur = cv2.GaussianBlur(gray, (3, 3), 0)
