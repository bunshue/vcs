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

# 刪除影像雜訊_濾波

print("使用 均值濾波器.blur()")

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"

image = cv2.imread(filename)  # 彩色讀取

image_blur_05 = cv2.blur(image, (5, 5))  # 使用 5x5 濾波核
image_blur_15 = cv2.blur(image, (15, 15))  # 使用 15x15 濾波核
image_blur_30 = cv2.blur(image, (30, 30))  # 使用 30x30 濾波核

plt.figure(figsize=(10, 8))
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(222)
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 5X5")

plt.subplot(223)
plt.imshow(cv2.cvtColor(image_blur_15, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 15X15")

plt.subplot(224)
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))
plt.title("blur 效果 30X30")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# cv2.boxFilter()        # 方框濾波器, 平均模糊
print("------------------------------------------------------------")  # 60個

print("使用 方框濾波器.boxFilter()")

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"
image = cv2.imread(filename)  # 彩色讀取

dst1 = cv2.boxFilter(image, -1, (2, 2))  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(image, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(image, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核

plt.figure(figsize=(10, 8))
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

filename = "C:/_git/vcs/_4.python/opencv/data/lena_noise.png"
image = cv2.imread(filename2)  # 彩色讀取
image = cv2.imread(filename)  # 彩色讀取

computer_image_blur_median = cv2.medianBlur(image, 5)

plt.figure(figsize=(12, 8))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(122)
plt.imshow(cv2.cvtColor(computer_image_blur_median, cv2.COLOR_BGR2RGB))
plt.title("medianBlur 效果")
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

dst1 = cv2.medianBlur(image, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(image, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(image, 7)  # 使用邊長是 7 的濾波核

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

print("cv2.floodFill() 填充 2")
"""
有些特殊的卷积核可以表示成一个列矢量和一个行矢量的乘积，
这时只需要将原始图像按 顺序与这两个矢量进行卷积，
所得到的最终结果和直接与卷积核进行卷积的结果相同。
对于较大的卷积核能大幅度地提高 计算速度。

OpenCV提供了 sep5()来进行这种分步卷积，调用参数如下：
sepFilter2D(src, ddepth, kernelX, kernelY[, dst[, anchor[, delta[, borderType]]]])
比较filter2D()和sepFilter2D() 的计算速度：
"""

img = np.random.rand(10, 10)
img = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)  # 灰階讀取

row = cv2.getGaussianKernel(7, -1)
col = cv2.getGaussianKernel(5, -1)

kernel = np.dot(col[:], row[:].T)

img2 = cv2.filter2D(img, -1, kernel)
img3 = cv2.sepFilter2D(img, -1, row, col)
print("error=", np.max(np.abs(img2[:] - img3[:])))

plt.subplot(131)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("原圖")

plt.subplot(132)
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("img2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(img3, cv2.COLOR_BGR2RGB))
plt.title("img3")

show()

"""
OpenCV提供了一些高级函数数来直接完成与某种特定卷积核的 卷积计算。

形态学运算
dilate
()对图像进行膨胀处理，而erode
()则对图像进行腐蚀处理。

mpiphologyEx()使用膨胀和收缩实现一些更高级的形态学处理。
这 些函数都可以对多值图像进行操作，对于多通道图像，它们将对每个通道进行相同的运算。

dilate()和erode()的调用参数相同：
dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]])

膨胀运算可以用下面的公式描述：
将结构元素kernel的锚点与原始图像中的每个像素(x,y)对齐之后，计算所有结构元素值不为0 的像素的最大值，写入目标图像的(x,y)像素点。而腐蚀运算则是计算所有结构元素不为0的像 素的最小值。
morphologyEx()的参数如下：
morphologyEx(src, op, kernel[, dst[, anchoriterationsborderType[, borderValue]]]]])
op参数，用于指定运算的类型。
moiphologyEx()的高级运算包括：
• MORPH_OPEN:开运算，可以用来区分两个靠得很近的区域。算法为先腐蚀再膨胀: dst=dilate(erode(src))
• MORPH_CLOSE:闭运算，可以用来连接两个靠得很近的区域。算法为先膨胀再腐蚀： dst=erode(dilate(src))
• MORPH_GRADIENT:形态梯度，能够找出图像区域的边缘。算法为膨胀减去腐蚀： dst=dilate(src)- erode(src)
• MORPH_TOPHAT:顶帽运算，算法为原始图像减去开运算：dst = src-open(src)。
• MORPH_BLACKHAT:黑帽运算，算法为闭运算减去原始图像：dst=close(src)-src。

    填充-floodFill

填充函数floodFill()在图像处理中经常用于标识或分离图像中的某些特定部分。它的调用方 式为:
floodFill(image, mask, seedPoint, newVal[, loDiff[, upDiff[, flags]]])
seedPoint参数为填充的起始点，为种子点； newVal参数为填充所使用的颜色值；loDiff和upDiff参数是填充的下限和上限容差；flags参数 是填充的算法标志。
填充从seedPoint指定的种子坐标开始，图像中与当前的填充区域颜色相近的点将被添加进 填充区域，从而逐步扩大填充区域，直到没有新的点能添加进填充区域为止。
颜色相近的判断 方法有两种：
    默认使用相邻点为基点进行判断。
•如果开启了 flags中的FL00DFILL_F1XED_RANGE标志位，则以种子点为基点进行判断。
假设图像中某个点(x,y)的颜色为C(x,y), C0为基点颜色，则下面的条件满足时，（x,y)将 被添加进填充区域：
C0 — loDiff < C(x，y) < C0 + hiDiff
此外还可以通过flags指定相邻点的定义：四连通或八连通。
当mask参数不为None时，它是一个宽和高比image都大两个像素的单通道8位图像
。image 图像中的像素(x,y)与mask中的(x + 1,y + 1)对应。填充只针对mask中的值为0的像素进行。 进行填充之后，mask中所有被填充的像素将被赋值为1。如果只希望修改mask,而不对原始图 像进行填充，可以开启flags标志中FLOODFTLL_MASK_ONLY。
#floodFill()的填充效果
"""
# 形態學運算
#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。
# 填充-floodFill
# 示範floodFill()的填充效果
#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。
# 去瑕疵-inpaint
#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。

coin_filename = "C:/_git/vcs/_4.python/opencv/data/morphology/coins.png"
img = cv2.imread(coin_filename)  # 彩色讀取
print("img.shape :", img.shape)

seed1 = 344, 188
seed2 = 152, 126
diff = (13, 13, 13)
h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(img, mask, seed1, BLACK, diff, diff, cv2.FLOODFILL_MASK_ONLY)
cv2.floodFill(img, None, seed2, RED, diff, diff)
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(~mask, cmap="gray")  # 灰階顯示
axes[1].imshow(img)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
# cv2.filter2D() SP         # 2D濾波核
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread("data/lena.png")  # 彩色讀取

computer_image_blur_gaussion = cv2.GaussianBlur(image, (5, 5), 0.75)  # 執行高斯模糊化

fig = plt.figure(figsize=(12, 8))

fig.add_subplot(121)
plt.title("原始圖像")
plt.imshow(image)

fig.add_subplot(122)
plt.title("高斯濾波器")
plt.imshow(computer_image_blur_gaussion)

show()

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
