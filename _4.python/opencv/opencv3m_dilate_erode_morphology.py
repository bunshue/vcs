"""
opencv 集合


cv2.dilate()
cv2.erode()
cv2.morphologyEx()


dilate 擴大 膨脹
erode 侵蝕
morphology 形態學 構詞學



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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/kernel.bmp"
o = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("dilate 擴大 膨脹 效果")
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59, 59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (59, 59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (59, 59))
dst1 = cv2.dilate(o, kernel1)
dst2 = cv2.dilate(o, kernel2)
dst3 = cv2.dilate(o, kernel3)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(o, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("dilate 擴大 膨脹 效果")
plt.imshow(cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("dilate 擴大 膨脹 效果")
plt.imshow(cv2.cvtColor(dst2, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("dilate 擴大 膨脹 效果")
plt.imshow(cv2.cvtColor(dst3, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


print("morphology 形態學")

original_img0 = cv2.imread("data/lena.png")
original_img = cv2.imread("data/lena.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義矩形結構元素
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)  # 頂帽運算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel)  # 黒帽運算

# 顯示圖像
cv2.imshow("original_img0", original_img0)
cv2.imshow("original_img", original_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("erode-dilate")

original_img = cv2.imread("data/flower.png")
res = cv2.resize(
    original_img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC
)  # 圖形太大了縮小一點
B, G, R = cv2.split(res)  # 獲取紅色通道
img = R
_, RedThresh = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
# OpenCV定義的結構矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
eroded = cv2.erode(RedThresh, kernel)  # 腐蝕圖像
dilated = cv2.dilate(RedThresh, kernel)  # 膨脹圖像

cv2.imshow("original_img", res)  # 原圖像
cv2.imshow("R_channel_img", img)  # 紅色通道圖
cv2.imshow("RedThresh", RedThresh)  # 紅色閾值圖像
cv2.imshow("Eroded Image", eroded)  # 顯示腐蝕后的圖像
cv2.imshow("Dilated Image", dilated)  # 顯示膨脹后的圖像

# NumPy定義的結構元素
NpKernel = np.uint8(np.ones((3, 3)))
Nperoded = cv2.erode(RedThresh, NpKernel)  # 腐蝕圖像

cv2.imshow("Eroded by NumPy kernel", Nperoded)  # 顯示腐蝕后的圖像
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("Canny")

image = cv2.imread("data/jianzhu.png", cv2.IMREAD_GRAYSCALE)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate_img = cv2.dilate(image, kernel)
erode_img = cv2.erode(image, kernel)

# 將兩幅圖像相減獲得邊；cv2.absdiff參數：(膨脹后的圖像，腐蝕后的圖像)
# 上面得到的結果是灰度圖，將其二值化以便觀察結果
# 反色，對二值圖每個像素取反

absdiff_img = cv2.absdiff(dilate_img, erode_img)
retval, threshold_img = cv2.threshold(absdiff_img, 40, 255, cv2.THRESH_BINARY)
result = cv2.bitwise_not(threshold_img)
cv2.imshow("jianzhu", image)
cv2.imshow("dilate_img", dilate_img)
cv2.imshow("erode_img", erode_img)
cv2.imshow("absdiff_img", absdiff_img)
cv2.imshow("threshold_img", threshold_img)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("bitwise")

original_img = cv2.imread("data/lena.png", 0)
gray_img = cv2.resize(
    original_img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC
)  # 圖形太大了縮小一點

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義矩形結構元素(核大小為3效果好)
TOPHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_TOPHAT, kernel)  # 頂帽運算
BLACKHAT_img = cv2.morphologyEx(gray_img, cv2.MORPH_BLACKHAT, kernel)  # 黒帽運算

bitwiseXor_gray = cv2.bitwise_xor(gray_img, TOPHAT_img)

# 顯示如下腐蝕后的圖像
cv2.imshow("gray_img", gray_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)
cv2.imshow("bitwiseXor_gray", bitwiseXor_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("absdiff")

image = cv2.imread("data/jianzhu.png", 0)
original_image = image.copy()
# 構造5×5的結構元素，分別為十字形、菱形、方形和X型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 構造方形結構元素
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

dilate_cross_img = cv2.dilate(image, cross)  # 使用cross膨脹圖像
erode_diamond_img = cv2.erode(dilate_cross_img, diamond)  # 使用菱形腐蝕圖像

dilate_x_img = cv2.dilate(image, x)  # 使用X膨脹原圖像
erode_square_img = cv2.erode(dilate_x_img, square)  # 使用方形腐蝕圖像

result = cv2.absdiff(erode_square_img, erode_diamond_img)  # 將兩幅閉運算的圖像相減獲得角
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)  # 使用閾值獲得二值圖

# 在原圖上用半徑為5的圓圈將點標出。
for j in range(result.size):
    y = int(j / result.shape[0])
    x = int(j % result.shape[0])
    if result[x, y] == 255:  # result[] 只能傳入整型
        cv2.circle(image, (y, x), 5, (255, 0, 0))

cv2.imshow("original_image", original_image)
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp"
filename = "C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png"

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image3 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image4 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure("", figsize=(16, 12))

print("dilate 擴大 膨脹 效果")

plt.subplot(221)
plt.title("原圖")
draw_line(image1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("dilate 擴大 膨脹 效果 1")
kernel = np.ones((20, 20), np.uint8)
dilation = cv2.dilate(image2, kernel)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("dilate 擴大 膨脹 效果 2")
kernel = np.ones((40, 40), np.uint8)
dilation = cv2.dilate(image3, kernel)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("dilate 擴大 膨脹 效果 3 加 iterations")
kernel = np.ones((10, 10), np.uint8)
dilation = cv2.dilate(image4, kernel, iterations=9)
draw_line(dilation)
plt.imshow(cv2.cvtColor(dilation, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域擴大、膨脹")
plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

plt.figure("", figsize=(16, 8))
plt.subplot(131)
plt.imshow(ishow)

plt.subplot(132)
plt.imshow(dist_transform)

plt.subplot(133)
plt.imshow(fore)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
bg = cv2.dilate(opening, kernel, iterations=3)
dist = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist, 0.7 * dist.max(), 255, 0)
fore = np.uint8(fore)
un = cv2.subtract(bg, fore)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.imshow(ishow)

plt.subplot(222)
plt.imshow(bg)

plt.subplot(223)
plt.imshow(fore)

plt.subplot(224)
plt.imshow(un)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
fore = np.uint8(fore)
ret, markers = cv2.connectedComponents(fore)
print(ret)

plt.figure("", figsize=(16, 8))
plt.subplot(131)
plt.imshow(ishow)

plt.subplot(132)
plt.imshow(fore)

plt.subplot(133)
plt.imshow(markers)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, fore = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
fore = np.uint8(fore)
ret, markers1 = cv2.connectedComponents(fore)
foreAdv = fore.copy()
unknown = cv2.subtract(sure_bg, foreAdv)
ret, markers2 = cv2.connectedComponents(foreAdv)
markers2 = markers2 + 1
markers2[unknown == 255] = 0

plt.figure("", figsize=(16, 8))
plt.subplot(121)
plt.imshow(markers1)

plt.subplot(122)
plt.imshow(markers2)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/water_coins.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ishow = img.copy()
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
sure_bg = cv2.dilate(opening, kernel, iterations=3)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0
markers = cv2.watershed(img, markers)
img[markers == -1] = [0, 255, 0]

plt.figure("", figsize=(16, 8))
plt.subplot(121)
plt.imshow(ishow)

plt.subplot(122)
plt.imshow(img)

plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

o = cv2.imread("images/rice.png", cv2.IMREAD_UNCHANGED)
k = np.ones((5, 5), np.uint8)
e = cv2.erode(o, k)
b = cv2.subtract(o, e)

plt.figure("", figsize=(16, 8))
plt.subplot(131)
plt.imshow(o)

plt.subplot(132)
plt.imshow(e)

plt.subplot(133)
plt.imshow(b)

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個


def draw_line(img):
    for i in range(8):
        cv2.line(img, (0, 100 * i), (700, 100 * i), (0, 0, 255), 2)  # 水平線
        cv2.line(img, (100 * i, 0), (100 * i, 700), (0, 0, 255), 2)  # 垂直線


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp"
filename = "C:/_git/vcs/_4.python/_data/opencv05_dilate_erode1.png"

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image3 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
image4 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure("erode 侵蝕 效果", figsize=(16, 12))

plt.subplot(221)
plt.title("原圖")
draw_line(image1)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 1")
kernel = np.ones((25, 25), np.uint8)
erosion = cv2.erode(image2, kernel)

plt.subplot(222)
plt.title("erode 侵蝕 效果 1")
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 2")
kernel = np.ones((25, 25), np.uint8)
erosion = cv2.erode(image3, kernel)

plt.subplot(223)
plt.title("erode 侵蝕 效果 2")
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 3 加 iterations")
kernel = np.ones((9, 9), np.uint8)
erosion = cv2.erode(image4, kernel, iterations=5)

plt.subplot(224)
plt.title("erode 侵蝕 效果 3")
draw_line(erosion)
plt.imshow(cv2.cvtColor(erosion, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域被侵蝕、縮小了")
plt.tight_layout()
plt.show()


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/opening.bmp"
img1 = cv2.imread(filename)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/opening2.bmp"
img2 = cv2.imread(filename)

print("morphologyEx 效果 1")
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_OPEN, k)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("morphologyEx 效果 1")
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("morphologyEx 效果 1")
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/closing.bmp"
img1 = cv2.imread(filename)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/closing2.bmp"
img2 = cv2.imread(filename)

print("morphologyEx 效果 2")
k = np.ones((10, 10), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k, iterations=3)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k, iterations=3)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("morphologyEx 效果 2")
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("morphologyEx 效果 2")
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/gradient.bmp"
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("morphologyEx 效果 3")
k = np.ones((5, 5), np.uint8)
r = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, k)

plt.figure("", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("morphologyEx 效果 3")
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/tophat.bmp"
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("morphologyEx 效果 4")
k = np.ones((5, 5), np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_TOPHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_TOPHAT, k)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("morphologyEx 效果 4")
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("morphologyEx 效果 4")
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/blackhat.bmp"
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image2 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("morphologyEx 效果 5")
k = np.ones((5, 5), np.uint8)
r1 = cv2.morphologyEx(image1, cv2.MORPH_BLACKHAT, k)
r2 = cv2.morphologyEx(image2, cv2.MORPH_BLACKHAT, k)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("morphologyEx 效果 5")
plt.imshow(cv2.cvtColor(r1, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("morphologyEx 效果 5")
plt.imshow(cv2.cvtColor(r2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print("------------------------------------------------------------")  # 60個

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print("kernel1 =\n", kernel1)
print("kernel2 =\n", kernel2)
print("kernel3 =\n", kernel3)


print("------------------------------------------------------------")  # 60個


print("defogging")


def zmMinFilterGray(src, r=7):
    # 最小值濾波，r是濾波器半徑
    return cv2.erode(src, np.ones((2 * r + 1, 2 * r + 1)))


def guidedfilter(I, p, r, eps):
    height, width = I.shape
    m_I = cv2.boxFilter(I, -1, (r, r))
    m_p = cv2.boxFilter(p, -1, (r, r))
    m_Ip = cv2.boxFilter(I * p, -1, (r, r))
    cov_Ip = m_Ip - m_I * m_p
    m_II = cv2.boxFilter(I * I, -1, (r, r))
    var_I = m_II - m_I * m_I

    a = cov_Ip / (var_I + eps)
    b = m_p - a * m_I
    m_a = cv2.boxFilter(a, -1, (r, r))
    m_b = cv2.boxFilter(b, -1, (r, r))
    return m_a * I + m_b


def Defog(m, r, eps, w, maxV1):  # 輸入rgb圖像，值范圍[0,1]
    # 計算大氣遮罩圖像V1和光照值A, V1 = 1-t/A
    V1 = np.min(m, 2)  # 得到暗通道圖像
    Dark_Channel = zmMinFilterGray(V1, 5)
    cv2.imshow("wu_Dark", Dark_Channel)  # 查看暗通道
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    V1 = guidedfilter(V1, Dark_Channel, r, eps)  # 使用引導濾波優化
    bins = 2000
    ht = np.histogram(V1, bins)  # 計算大氣光照A
    d = np.cumsum(ht[0]) / float(V1.size)
    for lmax in range(bins - 1, 0, -1):
        if d[lmax] <= 0.999:
            break
    A = np.mean(m, 2)[V1 >= ht[1][lmax]].max()
    V1 = np.minimum(V1 * w, maxV1)  # 對值范圍進行限制
    return V1, A


def deHaze(m, r=81, eps=0.001, w=0.95, maxV1=0.80, bGamma=False):
    Y = np.zeros(m.shape)
    Mask_img, A = Defog(m, r, eps, w, maxV1)  # 得到遮罩圖像和大氣光照

    for k in range(3):
        Y[:, :, k] = (m[:, :, k] - Mask_img) / (1 - Mask_img / A)  # 顏色校正
    Y = np.clip(Y, 0, 1)
    if bGamma:
        Y = Y ** (np.log(0.5) / np.log(Y.mean()))  # gamma校正,默認不進行該操作
    return Y


m = deHaze(cv2.imread("data/wu.jpg") / 255.0) * 255
cv2.imwrite("tmp_wu_2.png", m)

print("------------------------------------------------------------")  # 60個

print("Canny1")

original_img = cv2.imread("data/lena.png", 0)
# canny(): 邊緣檢測
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)  # 執行高斯模糊化
canny = cv2.Canny(img1, 50, 150)

# 形態學：邊緣檢測
_, Thr_img = cv2.threshold(
    original_img, 210, 255, cv2.THRESH_BINARY
)  # 設定紅色通道閾值210（閾值影響梯度運算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))  # 定義矩形結構元素
gradient = cv2.morphologyEx(Thr_img, cv2.MORPH_GRADIENT, kernel)  # 梯度

plt.subplot(131)
cv2.imshow("原始圖像", original_img)

plt.subplot(132)
cv2.imshow("梯度", gradient)

plt.subplot(133)
cv2.imshow("Canny函數", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

print("open-close")

original_img = cv2.imread("data/flower.png", 0)
gray_res = cv2.resize(
    original_img, None, fx=0.8, fy=0.8, interpolation=cv2.INTER_CUBIC
)  # 圖形太大了縮小一點
# B, G, img = cv2.split(res)
# _,RedThresh = cv2.threshold(img,160,255,cv2.THRESH_BINARY) #設定紅色通道閾值160（閾值影響開閉運算效果）
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義矩形結構元素
# 閉運算1
closed1 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel, iterations=1)
# 閉運算2
closed2 = cv2.morphologyEx(gray_res, cv2.MORPH_CLOSE, kernel, iterations=3)
# 開運算1
opened1 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel, iterations=1)
# 開運算2
opened2 = cv2.morphologyEx(gray_res, cv2.MORPH_OPEN, kernel, iterations=3)
# 梯度
gradient = cv2.morphologyEx(gray_res, cv2.MORPH_GRADIENT, kernel)

# 顯示如下腐蝕后的圖像
cv2.imshow("gray_res", gray_res)
cv2.imshow("Close1", closed1)
cv2.imshow("Close2", closed2)
cv2.imshow("Open1", opened1)
cv2.imshow("Open2", opened2)
cv2.imshow("gradient", gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
