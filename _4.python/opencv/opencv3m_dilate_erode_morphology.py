"""
數學形態學
cv2.dilate()  # dilate 擴大 膨脹 白色變大
cv2.erode()  # erode 侵蝕 白色變小
cv2.morphologyEx()  # morphology 形態學 構詞學
"""

from opencv_common import *

print("------------------------------------------------------------")  # 60個


def draw_line(image):
    H = image.shape[0]
    W = image.shape[1]
    # print(image.shape, H // 100, W // 100)
    for i in range(H // 100 + 1):
        cv2.line(image, (0, 100 * i), (W, 100 * i), (0, 0, 100), 2)  # 畫線 水平線 R

    for i in range(W // 100 + 1):
        cv2.line(
            image, (100 * i, 0), (100 * i, H), (0, 100, 0), 2, lineType=cv2.LINE_AA
        )  # 畫線 垂直線 G


print("------------------------------------------------------------")  # 60個

print("dilate 擴大 膨脹 效果")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/kernel.bmp"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode2.png"

image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("定義矩形結構元素 kernel")
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59, 59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (59, 59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (59, 59))
# print("kernel1 =\n", kernel1)
# print("kernel2 =\n", kernel2)
# print("kernel3 =\n", kernel3)
image_dilate1 = cv2.dilate(image, kernel1)
image_dilate2 = cv2.dilate(image, kernel2)
image_dilate3 = cv2.dilate(image, kernel3)

plt.figure("", figsize=(16, 12))
plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("dilate 白色膨脹 方 MORPH_RECT")
plt.imshow(cv2.cvtColor(image_dilate1, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("dilate 白色膨脹 叉 MORPH_CROSS")
plt.imshow(cv2.cvtColor(image_dilate2, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("dilate 白色膨脹 橢 MORPH_ELLIPSE")
plt.imshow(cv2.cvtColor(image_dilate3, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域擴大、膨脹了")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

print("dilate 擴大 膨脹 效果")

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode2.png"

image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

print("定義矩形結構元素 kernel")
kernel1 = np.ones((3, 3), np.uint8)
kernel2 = np.ones((5, 5), np.uint8)
kernel3 = np.ones((7, 7), np.uint8)
image_dilate1 = cv2.dilate(image, kernel1)
image_dilate2 = cv2.dilate(image, kernel2)
image_dilate3 = cv2.dilate(image, kernel3, iterations=3)
draw_line(image_dilate1)
draw_line(image_dilate2)
draw_line(image_dilate3)

plt.figure("", figsize=(16, 12))

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title("dilate 擴大 膨脹 效果 1")
plt.imshow(cv2.cvtColor(image_dilate1, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title("dilate 擴大 膨脹 效果 2")
plt.imshow(cv2.cvtColor(image_dilate2, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title("dilate 擴大 膨脹 效果 3 加 iterations")
plt.imshow(cv2.cvtColor(image_dilate3, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域擴大、膨脹了")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode2.png"

image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure("erode 侵蝕 效果", figsize=(16, 12))

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 1")
kernel1 = np.ones((3, 3), np.uint8)
image_erosion1 = cv2.erode(image, kernel1)

plt.subplot(222)
plt.title("erode 侵蝕 效果 1")
draw_line(image_erosion1)
plt.imshow(cv2.cvtColor(image_erosion1, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 2")
kernel2 = np.ones((5, 5), np.uint8)
image_erosion2 = cv2.erode(image, kernel2)

plt.subplot(223)
plt.title("erode 侵蝕 效果 2")
draw_line(image_erosion2)
plt.imshow(cv2.cvtColor(image_erosion2, cv2.COLOR_BGR2RGB))

print("erode 侵蝕 效果 3 加 iterations")
kernel3 = np.ones((7, 7), np.uint8)
image_erosion3 = cv2.erode(image, kernel3, iterations=3)

plt.subplot(224)
plt.title("erode 侵蝕 效果 3")
draw_line(image_erosion3)
plt.imshow(cv2.cvtColor(image_erosion3, cv2.COLOR_BGR2RGB))

plt.suptitle("白色區域被侵蝕、縮小了")
plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個

print("erode-dilate")

filename = "data/flower.png"
filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"
# filename = "C:/_git/vcs/_4.python/_data/bear.jpg"
# filename = "C:/_git/vcs/_4.python/_data/panda.jpg"


original_img = cv2.imread(filename)

res = cv2.resize(
    original_img, None, fx=0.6, fy=0.6, interpolation=cv2.INTER_CUBIC
)  # 圖形太大了縮小一點
cv2.imshow("original_img", res)  # 原圖像

B, G, R = cv2.split(res)  # 獲取紅色通道

img = R

cv2.imshow("R_channel_img", img)  # 紅色通道圖

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
_, RedThresh = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)
cv2.imshow("RedThresh", RedThresh)  # 紅色閾值圖像

# OpenCV定義的結構矩形元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

eroded = cv2.erode(RedThresh, kernel)  # 腐蝕圖像
dilated = cv2.dilate(RedThresh, kernel)  # 膨脹圖像

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

print("morphology 形態學")

# original_img = cv2.imread("data/lena.png")
original_img = cv2.imread("data/lena.png", 0)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))  # 定義矩形結構元素
TOPHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_TOPHAT, kernel)  # 頂帽運算
BLACKHAT_img = cv2.morphologyEx(original_img, cv2.MORPH_BLACKHAT, kernel)  # 黒帽運算

cv2.imshow("original_img", original_img)
cv2.imshow("TOPHAT_img", TOPHAT_img)
cv2.imshow("BLACKHAT_img", BLACKHAT_img)

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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
show()

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

img = cv2.imread(filename)
cv2.imshow("image1", img)  # 原始影像

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (11, 11))

img = cv2.erode(img, kernel)  # 先侵蝕，將白色小圓點移除
cv2.imshow("image2", img)  # 侵蝕後的影像

img = cv2.dilate(img, kernel)  # 再膨脹，白色小點消失
cv2.imshow("image3", img)  # 膨脹後的影像

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology//dilate_erode1.png"

print("形態學處理 erode")

# 檔案 => cv2影像
I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 創建結構元
s = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 腐蝕圖像
r = cv2.erode(I, s)

# 顯示原圖和腐蝕後的結果
cv2.imshow("I", I)
cv2.imshow("erode", r)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("形態學處理 dilate")

""" fail
if __name__ =="__main__":
    #第一步：讀入圖像
    # 檔案 => cv2影像
    I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    #顯示原圖
    cv2.imshow("I",I)
    #結構元半徑,迭代次數
    r,i = 1,1
    MAX_R,MAX_I = 20,20
    #顯示膨脹效果的窗口
    cv2.namedWindow("dilate",1)
    def nothing(*arg):
        pass
    #調節結構元半徑
    cv2.createTrackbar("r","dilate",r,MAX_R,nothing)
    #調節迭代次數
    cv2.createTrackbar("i","dilate",i,MAX_I,nothing)
    while True:
        #得到當前的r值
        r = cv2.getTrackbarPos('r', 'dilate')
        #得到當前的i值
        i= cv2.getTrackbarPos('i','dilate')
        #創建結構元
        s = cv2.getStructuringElement(cv2.MORPH_GRADIENT,(2*r+1,2*r+1))
        #膨脹圖像
        d = cv2.erode(I,s,iterations=i)
        #顯示膨脹效果
        cv2.imshow("dilate",d)

        k = cv2.waitKey(1)
        if k == ESC:
            break
    cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個

print("形態學處理 open")

# 第一步：讀入圖像
# 檔案 => cv2影像
I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 創建結構元
s = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 腐蝕圖像
d = cv2.morphologyEx(I, cv2.MORPH_OPEN, s, iterations=1)

# 顯示原圖和腐蝕後的結果
cv2.imshow("I", I)
cv2.imshow("open", d)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# fail

print("形態學處理 mor")
print("按 ESC 離開")

# 第一步：讀入圖像
# 檔案 => cv2影像
I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cv2.imshow("I", I)

# 結構元半徑，迭代次數
r, i = 1, 1
MAX_R, MAX_I = 20, 20

# 顯示形態學處理的效果的窗口
cv2.namedWindow("morphology", 1)


def nothing(*arg):
    pass


# 調節結構元半徑
cv2.createTrackbar("r", "morphology", r, MAX_R, nothing)

# 調節迭代次數
cv2.createTrackbar("i", "morphology", i, MAX_I, nothing)

while True:
    # 得到當前的r值
    r = cv2.getTrackbarPos("r", "morphology")
    # 得到當前的i值
    i = cv2.getTrackbarPos("i", "morphology")

    # 創建結構元
    s = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * r + 1, 2 * r + 1))

    # 形態學處理
    d = cv2.morphologyEx(I, cv2.MORPH_GRADIENT, s, iterations=i)

    # 顯示效果
    cv2.imshow("morphology", d)

    k = cv2.waitKey(1)
    if k == ESC:
        break


cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("侵蝕(Erosion) 白色變小")

src = np.zeros((7, 7), np.uint8)
src[1:6, 1:6] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.erode(src, kernel)  # 腐蝕.erode
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Erosion = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("侵蝕(Erosion) 白色變小")

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/dilate_erode1.png"
filename = "dilate_erode2.png"
# filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

src = cv2.imread(filename)
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.erode(src, kerne2)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst2)

kerne3 = np.ones((7, 7), np.uint8)  # 建立7x7內核
dst3 = cv2.erode(src, kerne3)  # 腐蝕.erode
cv2.imshow("after erosion 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("膨脹(Dilate) 白色變大")

filename = "dilate_erode2.png"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

src = cv2.imread(filename)
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 3 x 3", dst1)

kerne2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.dilate(src, kerne2)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst2)

kerne3 = np.ones((7, 7), np.uint8)  # 建立7x7內核
dst3 = cv2.dilate(src, kerne3)  # 膨脹.dilate
cv2.imshow("after dilation 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = np.zeros((7, 7), np.uint8)
src[2:5, 2:5] = 1  # 建立前景影像
kernel = np.ones((3, 3), np.uint8)  # 建立內核
dst = cv2.dilate(src, kernel)  # 膨脹.dilate
print(f"src = \n {src}")
print(f"kernel = \n {kernel}")
print(f"Dilation = \n {dst}")

print("------------------------------------------------------------")  # 60個

filename = "dilate_erode2.png"

src = cv2.imread(filename)
cv2.imshow("src", src)

kernel1 = np.ones((3, 3), np.uint8)  # 建立3x3內核
dst1 = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel1)  # 開運算
cv2.imshow("after Opening 3 x 3", dst1)

kernel2 = np.ones((5, 5), np.uint8)  # 建立5x5內核
dst2 = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel2)  # 開運算
cv2.imshow("after Opening 5 x 5", dst2)

kernel3 = np.ones((7, 7), np.uint8)  # 建立7x7內核
dst3 = cv2.morphologyEx(src, cv2.MORPH_OPEN, kernel3)  # 開運算
cv2.imshow("after Opening 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "dilate_erode2.png"

src = cv2.imread(filename)
cv2.imshow("src", src)

kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核

mid = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 9 x 9", mid)

dst = cv2.dilate(mid, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 9 x 9", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/night.jpg")
cv2.imshow("src", src)

kernel = np.ones((9, 9), np.uint8)  # 建立9x9內核

mid = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 9 x 9", mid)

dst = cv2.erode(mid, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 9 x 9", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/k.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("after dilation 5 x 5", dst1)

dst2 = cv2.erode(src, kernel)  # 腐蝕.erode
cv2.imshow("after erosion 5 x 5", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/snowman.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_CLOSE, kernel)  # 閉運算
cv2.imshow("after Closing 11 x 11", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/k.jpg")
cv2.imshow("src", src)

kernel = np.ones((5, 5), np.uint8)  # 建立5x5內核

dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient
cv2.imshow("after morpological gradient", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/hole.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst = cv2.morphologyEx(src, cv2.MORPH_GRADIENT, kernel)  # gradient
cv2.imshow("after morpological gradient", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/btree.jpg")
cv2.imshow("src", src)

kernel = np.ones((3, 3), np.uint8)  # 建立3x3內核

dst = cv2.morphologyEx(src, cv2.MORPH_TOPHAT, kernel)  # 禮帽運算(tophat)
cv2.imshow("after tophat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/snowman.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # 黑帽運算(blackhat)
cv2.imshow("after blackhat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/excel.jpg")
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.uint8)  # 建立11x11內核

dst = cv2.morphologyEx(src, cv2.MORPH_BLACKHAT, kernel)  # 黑帽運算(blackhat)
cv2.imshow("after blackhat", dst)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
print(f"MORPH_RECT \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
print(f"MORPH_ELLIPSE \n {kernel}")
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
print(f"MORPH_CROSS \n {kernel}")

print("------------------------------------------------------------")  # 60個

src = cv2.imread("data/morphology/bw_circle.jpg")
cv2.imshow("src", src)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (39, 39))

dst1 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_RECT", dst1)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (39, 39))

dst2 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_ELLIPSE", dst2)

kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (39, 39))

dst3 = cv2.dilate(src, kernel)  # 膨脹.dilate
cv2.imshow("MORPH_CROSS", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(dst)
plt.title("距離變換影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(sure_fg)
plt.title("閾值化影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
kernel = np.ones((3, 3), np.uint8)

# 執行開運算 Opening
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.5 * dst.max(), 255, 0)  # 前景圖案

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(dst)
plt.title("距離變換影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(sure_fg)
plt.title("閾值化影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案

# 計算未知區域
# 影像計算 影像相減 cv2.subtract
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

plt.subplot(141)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(142)
plt.imshow(dst)
plt.title("距離變換影像")
plt.axis("off")

plt.subplot(143)
plt.imshow(sure_fg)
plt.title("閾值化影像")
plt.axis("off")

plt.subplot(144)
plt.imshow(unknown)
plt.title("未知區域")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案

# 計算未知區域
# 影像計算 影像相減 cv2.subtract
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 標記
ret, markers = cv2.connectedComponents(sure_fg)

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(unknown)
plt.title("未知區域")
plt.axis("off")

plt.subplot(133)
plt.imshow(markers)
plt.title("標記區")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案

# 計算未知區域
# 影像計算 影像相減 cv2.subtract
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 標記
ret, markers = cv2.connectedComponents(sure_fg)

# 先複製再標記修訂
sure_fg_copy = sure_fg.copy()
ret, markers_new = cv2.connectedComponents(sure_fg_copy)
markers_new += 1  # 標記修訂
markers_new[unknown == 255] = 0

plt.subplot(131)
plt.title("未知區域")
plt.imshow(unknown)
plt.axis("off")

plt.subplot(132)
plt.title("標記區")
plt.imshow(markers, cmap="jet")
plt.axis("off")

plt.subplot(133)
plt.title("標記修訂區")
plt.imshow(markers_new, cmap="jet")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/opencv/data/morphology/opencv_coin.jpg"

src = cv2.imread(filename, cv2.IMREAD_COLOR)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

rgb_src = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)

# 二值化
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# 執行開運算 Opening
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# 執行膨脹操作
sure_bg = cv2.dilate(opening, kernel, iterations=3)

# 獲得距離轉換函數結果
dst = cv2.distanceTransform(opening, cv2.DIST_L2, 5)

# 讀者也可以更改下列 0.7 為其他值, 會影響前景大小
ret, sure_fg = cv2.threshold(dst, 0.7 * dst.max(), 255, 0)  # 前景圖案

# 計算未知區域
# 影像計算 影像相減 cv2.subtract
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# 標記
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# 正式執行分水嶺函數
dst = rgb_src.copy()
markers = cv2.watershed(dst, markers)
dst[markers == -1] = [255, 0, 0]  # 使用紅色

plt.subplot(121)
plt.title("原圖")
plt.imshow(rgb_src)
plt.axis("off")

plt.subplot(122)
plt.title("分割結果")
plt.imshow(dst)
plt.axis("off")

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
