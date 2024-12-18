"""
opencv 集合 新進

"""

import cv2

ESC = 27
SPACE = 32

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def show():
    # return
    plt.show()
    pass


def cvshow(title, image):
    # return
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()
    pass


print("------------------------------------------------------------")  # 60個

print("練習組合成一張大圖 picasa效果")

filename1 = "C:/_git/vcs/_4.python/_data/elephant.jpg"
filename2 = "C:/_git/vcs/_4.python/_data/bear.jpg"
filename3 = "C:/_git/vcs/_4.python/_data/panda.jpg"

ratio = 3

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

# 檔案 => cv2影像
image3 = cv2.imread(filename3)

print(image1.shape)

image1 = cv2.resize(image1, (image1.shape[1] // ratio, image1.shape[0] // ratio))
image2 = cv2.resize(image2, (image2.shape[1] // ratio, image2.shape[0] // ratio))
image3 = cv2.resize(image3, (image3.shape[1] // ratio, image3.shape[0] // ratio))
print(image1.shape)

output = np.zeros((768, 1024, 3), dtype="uint8")  # 設定合成的影像為一張全黑的畫布

x_st = 50
y_st = 50
w, h = image1.shape[1], image1.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image1[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 300
y_st = 200
w, h = image2.shape[1], image2.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image2[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 150
y_st = 300
w, h = image3.shape[1], image3.shape[0]
output[y_st : y_st + h, x_st : x_st + w] = image3[
    0:h, 0:w
]  # 設定 output 的某個區域為即時影像 image 的某區域

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

# 檔案 => cv2影像
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
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

# 檔案 => cv2影像
o = cv2.imread(filename)

image2 = cv2.cvtColor(o, cv2.COLOR_BGR2RGB)
mask = np.zeros(o.shape[:2], np.uint8)
bgd = np.zeros((1, 65), np.float64)
fgd = np.zeros((1, 65), np.float64)
rect = (50, 50, 400, 500)
cv2.grabCut(o, mask, rect, bgd, fgd, 5, cv2.GC_INIT_WITH_RECT)

# 檔案 => cv2影像
mask2 = cv2.imread("images/mask.png", 0)

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

image2 = image.copy()

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

image2 = image.copy()

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread("images/lena4.bmp", 0)

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
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

plt.suptitle("影像移動")
show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
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
show()

print("------------------------------------------------------------")  # 60個

filename = "data/PerspectiveTransform.jpg"
# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])

pts1 = np.float32([[200, 0], [300, 0], [100, 600], [200, 600]])
pts2 = np.float32([[100, 0], [200, 0], [100, 600], [200, 600]])


pts1 = np.float32([[100, 0], [600, 0], [0, 600], [500, 600]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])


M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("把歪圖拉正")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

show()

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


# 上面就是椒鹽噪聲函數，下面是使用方法，大家可以愉快的玩耍了
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image0 = cv2.imread(filename)

# 檔案 => cv2影像
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

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

# 檔案 => cv2影像
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
plt.title("HSV轉換")
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

print("去除圖片的雜訊 fastNlMeansDenoisingColored")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image2 = cv2.imread(filename)

plt.figure(figsize=(12, 8))

plt.subplot(121)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image2_denoised = cv2.fastNlMeansDenoisingColored(image2, h=5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2_denoised, cv2.COLOR_BGR2RGB))
plt.title("去除圖片的雜訊 fastNlMeansDenoisingColored")

show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

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


# 檔案 => cv2影像
# original_image_test1 = cv2.imread(filename, 0)

# 檔案 => cv2影像
original_image_test1 = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)


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
# plt.imshow(original_image_test1)
plt.imshow(cv2.cvtColor(original_image_test1, cv2.COLOR_BGR2RGB))

fig.add_subplot(122)
plt.title("銳化濾波")
plt.imshow(my_laplace_result_add_abs(original_image_test1, result))

show()

print("------------------------------------------------------------")  # 60個

print("對比度增強 CLAHE")
print("createCLAHE_image 生成自適應均衡化圖像")

# 自適應直方圖均衡化（Adaptive Histogram Equalization, AHE）
# 限制對比度 自適應直方圖均衡化(Contrast Limited Adaptive Histogram Equalization, CLAHE)

# 檔案 => cv2影像
image = cv2.imread("data/building.png", 0)
# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 創建 CLAHE  對象
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# 創建 CLAHE  對象
# clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(28, 28))

# 限制對比度的自適應閾值均衡化
cl1 = clahe.apply(image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

plt.imshow(cv2.cvtColor(cl1, cv2.COLOR_BGR2RGB))
show()

# 存圖以比較之
# cv2.imwrite('building.png', image)
# cv2.imwrite('building_clahe.png', cl1)

print("------------------------------------------------------------")  # 60個

print("gradient 邊緣檢測 梯度處理")


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


# 檔案 => cv2影像
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
# plt.imshow(original_image_lena)
plt.imshow(cv2.cvtColor(original_image_lena, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("邊緣檢測")
plt.imshow(edge_image_lena)

plt.subplot(133)
plt.title("梯度處理")
plt.imshow(sharpen_image_lena)

show()

print("------------------------------------------------------------")  # 60個

print("imaeg_laplace 邊緣檢測 銳化處理")

# 檔案 => cv2影像
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
plt.imshow(cv2.cvtColor(original_image_test1, cv2.COLOR_BGR2RGB))

fig.add_subplot(132)
plt.title("邊緣檢測")
plt.imshow(my_show_edge(result))

fig.add_subplot(133)
plt.title("銳化處理")
plt.imshow(my_laplace_result_add(original_image_test1, result))

show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")


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


# 檔案 => cv2影像
original_image_test1 = cv2.imread("data/lena.png", 0)

# 函數中的參數ddepth為輸出圖像的深度，也就是每個像素點是多少位的。
# CV_16S表示16位有符號數
computer_result = cv2.Laplacian(original_image_test1, ksize=3, ddepth=cv2.CV_16S)
plt.imshow(my_laplace_result_add(original_image_test1, computer_result))

show()

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


# 檔案 => cv2影像
image = cv2.imread("data/building.png")
print(image.shape)

newimage = CreateNewImg(image)
print(newimage.shape)

""" OK, 但無法用plt顯示
cv2.imshow("Original", image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
show()

#cv2.imshow("去霧后圖像", newimage / 255)
#cv2.imshow("Optimize", newimage / 255)
cv2.imshow("Optimize", newimage / 255)

#不能用
#plt.imshow(cv2.cvtColor(newimage / 255, cv2.COLOR_BGR2RGB))
#show()
"""
print("------------------------------------------------------------")  # 60個

print("Y對稱一張圖片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

D = 20
output = np.zeros((h + D * 2, w * 2 + D * 2, 3), dtype="uint8")  # 產生 2W x H 的黑色背景

image1 = image1[:h, :w]  # 取出 WxH 的影像 全部 也可只取部分

print("左右翻轉影像")
image12 = cv2.flip(image1, 1)

# 左半
output[D : h + D, D : w + D] = image1  # 將 output 左邊內容換成 image1
# 右半
output[D : h + D, w + D : w * 2 + D] = image12  # 將 output 右邊內容換成 image2

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

print("XY對稱一張圖片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename)

w = image1.shape[1]
h = image1.shape[0]

output = np.zeros((h * 2, w * 2, 3), dtype="uint8")  # 產生 2W x 2H 的黑色背景

img = image1[:h, :w]  # 取出 WxH 的影像 全部 也可只取部分
img2 = cv2.flip(img, 1)  # 左右翻轉
img3 = cv2.flip(img, 0)  # 上下翻轉
img4 = cv2.flip(img, -1)  # 上下左右翻轉

# 左上
output[:h, :w] = img
# 右上
output[:h, w : w * 2] = img2
# 左下
output[h : h * 2, :w] = img3
# 右下
output[h : h * 2, w : w * 2] = img4

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個
print("OpenCV_01")

# 檔案 => cv2影像
image = cv2.imread(filename)  # 預設為彩色 1號

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰階 2號

# 檔案 => cv2影像
image = cv2.imread(filename, 2)  # 也可使用數字代表模式

print(image.shape)  # 得到 shape
print(image.dtype)  # uint8

cvshow("image", image)

"""
# 檔案 => cv2影像
image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

# 檔案 => cv2影像
image2 = cv2.imread('test.png', cv2.IMREAD_UNCHANGED)

print(image1.shape)    # (400, 300, 3)  JPG 只有三個色版 BGR
print(image2.shape)    # (400, 300, 4)  PNG 四個色版 GRA

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

# 檔案 => cv2影像
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA 色彩模式

print(image.shape)                             # (400, 300, 4)  第三個數值變成 4
"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_03")

# 檔案 => cv2影像
image_b = cv2.imread(filename)

# 檔案 => cv2影像
image_g = cv2.imread(filename)

# 檔案 => cv2影像
image_r = cv2.imread(filename)

image_b[:, :, 1] = 0  # 將綠色設為 0
image_b[:, :, 2] = 0  # 將紅色設為 0
image_g[:, :, 0] = 0  # 將藍色設為 0
image_g[:, :, 2] = 0  # 將紅色設為 0
image_r[:, :, 0] = 0  # 將藍色設為 0
image_r[:, :, 1] = 0  # 將綠色設為 0

cvshow("image R", image_r)
cvshow("image G", image_g)
cvshow("image B", image_b)

print("------------------------------------------------------------")  # 60個
print("OpenCV_04")

# 檔案 => cv2影像
image = cv2.imread(filename)

print("原圖為彩色")
cvshow("image1", image)

print("彩色轉灰階")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_05")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("像素操作 底片效果 半張負片")

# 檔案 => cv2影像
image = cv2.imread(filename)

rows = image.shape[0]  # 取得高度的總像素
cols = image.shape[1]  # 取得寬度的總像素

for row in range(int(rows / 2)):  # 只取 rows 的一半 ( 使用 int 取整數 )
    for col in range(cols):
        image[row, col, 0] = 255 - image[row, col, 0]  # 255 - 藍色
        image[row, col, 1] = 255 - image[row, col, 1]  # 255 - 綠色
        image[row, col, 2] = 255 - image[row, col, 2]  # 255 - 紅色

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_06")

print("像素操作 全張負片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

image = 255 - image  # 使用 255 減去陣列中所有數值

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_07")

# 檔案 => cv2影像
image = cv2.imread(filename)

contrast = 200
brightness = 0
output = image * (contrast / 127 + 1) - contrast + brightness  # 轉換公式
# 轉換公式參考 https://stackoverflow.com/questions/50474302/how-do-i-adjust-brightness-contrast-and-vibrance-with-opencv-python

# 調整後的數值大多為浮點數，且可能會小於 0 或大於 255
# 為了保持像素色彩區間為 0～255 的整數，所以再使用 np.clip() 和 np.uint8() 進行轉換
output = np.clip(output, 0, 255)
output = np.uint8(output)

cvshow("image", output)

print("------------------------------------------------------------")  # 60個
print("OpenCV_08")

# 檔案 => cv2影像
image = cv2.imread(filename)

output = image  # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(image, output, alpha, beta)  # 套用 convertScaleAbs

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("OpenCV_11 三原色疊加")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"
filename3 = "C:/_git/vcs/_4.python/opencv/data/RGB_B.png"

# 檔案 => cv2影像
image_r = cv2.imread(filename1)

# 檔案 => cv2影像
image_g = cv2.imread(filename2)

# 檔案 => cv2影像
image_b = cv2.imread(filename3)

image = cv2.add(image_r, image_g)  # 疊加紅色和綠色
image = cv2.add(image, image_b)  # 疊加藍色

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

# 改用 製造數據 自己畫出來

w, h = 400, 400
image_r = np.zeros([h, w, 3])  # 黑色
image_g = np.zeros([h, w, 3])  # 黑色
image_b = np.zeros([h, w, 3])  # 黑色

radius = 100

cx, cy = 200, 150
color = (0, 0, 255)  # 紅
cv2.circle(image_r, (cx, cy), radius, color, -1)  # 繪製實心圓形

cx, cy = 150, 250
color = (0, 255, 0)  # 綠
cv2.circle(image_g, (cx, cy), radius, color, -1)  # 繪製實心圓形

cx, cy = 250, 250
color = (255, 0, 0)  # 藍
cv2.circle(image_b, (cx, cy), radius, color, -1)  # 繪製實心圓形


image = cv2.add(image_r, image_g)  # 疊加紅色和綠色
image = cv2.add(image, image_b)  # 疊加藍色

cvshow("RGB Model", image)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("OpenCV_14 漸層色")

w, h = 400, 400
image = np.zeros([h, w, 3])
for i in range(h):
    image[i, :, 1] = int(256 * i / 400)  # 從上往下填入綠色漸層

image = image.astype("float32") / 255  # 轉換內容類型

cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("OpenCV_17 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

# 檔案 => cv2影像
image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 開啟圖片

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

h = image.shape[0]  # 取得圖片高度
w = image.shape[1]  # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_18 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

# 檔案 => cv2影像
image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

h = image.shape[0]
w = image.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x] = [0, 255, 255, 255]  # 亮色改成黃色

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_19")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
bg = cv2.imread(filename1, cv2.IMREAD_UNCHANGED)  # 開啟背景圖

bg = cv2.cvtColor(bg, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA

# 檔案 => cv2影像
image = cv2.imread(filename2, cv2.IMREAD_UNCHANGED)  # 開啟悟空公仔圖

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA

h = image.shape[0]  # 取得圖片高度
w = image.shape[1]  # 取得圖片寬度

for x in range(w):
    for y in range(h):
        r = image[y, x, 2]  # 取得該像素的紅色值
        g = image[y, x, 1]  # 取得該像素的綠色值
        b = image[y, x, 0]  # 取得該像素的藍色值
        if r > 20 and r < 80 and g < 190 and g > 110 and b < 150 and b > 60:
            image[y, x] = bg[y, x]  # 如果在範圍內的顏色，換成背景圖的像素值


cvshow("image", bg)
cvshow("image", image)

print("------------------------------------------------------------")  # 60個

print("測試 cv2.floodFill()")


def floodFill(
    source, mask, seedPoint, newVal, loDiff, upDiff, flags=cv2.FLOODFILL_FIXED_RANGE
):
    result = source.copy()
    cv2.floodFill(
        result,
        mask=mask,
        seedPoint=seedPoint,
        newVal=newVal,
        loDiff=loDiff,
        upDiff=upDiff,
        flags=flags,
    )
    return result


# 檔案 => cv2影像
image = cv2.imread(filename)
h, w = image.shape[:2]  # 取得原始影像的長寬

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 製作 mask，長寬都要加上 2
image1 = floodFill(image, mask, (100, 10), red, (100, 100, 60), (100, 100, 100))

cvshow("image1", image1)

print("------------------------------")  # 30個

# 檔案 => cv2影像
image = cv2.imread(filename)
h, w = image.shape[:2]  # 取得原始影像的長寬

mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 全黑遮罩
mask = 255 - mask  # 變成全白遮罩
mask[0:100, 0:200] = 0  # 將左上角長方形變成黑色

# 只處理mask區域
image2 = floodFill(image, mask, (100, 10), red, (100, 100, 60), (200, 200, 200))

cvshow("image2", image2)

print("------------------------------------------------------------")  # 60個

print("測試 凸透鏡 效果")


def convex(src_image, raw, effect):
    col, row, channel = raw[:]  # 取得圖片資訊
    cx, cy, r = effect[:]  # 取得凸透鏡的範圍
    output = np.zeros([row, col, channel], dtype=np.uint8)  # 產生空白畫布
    for y in range(row):
        for x in range(col):
            d = ((x - cx) * (x - cx) + (y - cy) * (y - cy)) ** 0.5  # 計算每個點與中心點的距離
            if d <= r:
                nx = int((x - cx) * d / r + cx)  # 根據不同的位置，產生新的 nx，越靠近中心形變越大
                ny = int((y - cy) * d / r + cy)  # 根據不同的位置，產生新的 ny，越靠近中心形變越大
                output[y, x, :] = src_image[ny, nx, :]  # 產生新的圖
            else:
                output[y, x, :] = src_image[y, x, :]  # 如果在半徑範圍之外，原封不動複製過去
    return output


# 檔案 => cv2影像
image = cv2.imread(filename)
image = convex(image, (300, 400, 3), (150, 130, 100))  # 提交參數數值，進行凸透鏡效果

cvshow("image", image)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("OpenCV_32")

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

w = image1.shape[1]  # 讀取圖片寬度
h = image1.shape[0]  # 讀取圖片高度

for i in range(w):
    image1[:, i, 0] = image1[:, i, 0] * ((300 - i) / 300) + image2[:, i, 0] * (
        i / 300
    )  # 藍色按照比例混合
    image1[:, i, 1] = image1[:, i, 1] * ((300 - i) / 300) + image2[:, i, 1] * (
        i / 300
    )  # 紅色按照比例混合
    image1[:, i, 2] = image1[:, i, 2] * ((300 - i) / 300) + image2[:, i, 2] * (
        i / 300
    )  # 綠色按照比例混合

# cv2.imwrite('tmp_image.png', image1)

image = image1.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_33")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

# 檔案 => cv2影像
mona = cv2.imread(filename)

# 檔案 => cv2影像
logo = cv2.imread(
    logo_filename, cv2.IMREAD_UNCHANGED
)  # 使用 cv2.IMREAD_UNCHANGED 讀取 png，保留 alpha 色版

mona_w = mona.shape[1]  # 蒙娜麗莎寬度
mona_h = mona.shape[0]  # 蒙娜麗莎高度
logo_w = logo.shape[1]  # logo 寬度
logo_h = logo.shape[0]  # logo 高度
dh = int((mona_h - logo_h) / 2)  # 如果 logo 要垂直置中，和上方的距離
h = dh + logo_h  # 計算蒙娜麗莎裡，logo 所在的高度位置

# 透過迴圈，根據背景透明度，計算出該像素的顏色
for i in range(logo_w):
    mona[dh:h, i, 0] = mona[dh:h, i, 0] * (1 - logo[:, i, 3] / 255) + logo[:, i, 0] * (
        logo[:, i, 3] / 255
    )
    mona[dh:h, i, 1] = mona[dh:h, i, 1] * (1 - logo[:, i, 3] / 255) + logo[:, i, 1] * (
        logo[:, i, 3] / 255
    )
    mona[dh:h, i, 2] = mona[dh:h, i, 2] * (1 - logo[:, i, 3] / 255) + logo[:, i, 2] * (
        logo[:, i, 3] / 255
    )

# cv2.imwrite('tmp_image.png', mona)

image = mona.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

cvshow("image", image)

print("------------------------------------------------------------")  # 60個
print("OpenCV_38")

""" barcode

# 檔案 => cv2影像
image = cv2.imread("barcode.jpg")

def putText(x,y,text,color=(0,0,0)):
    global image
    #font_filename = 'NotoSansTC-Regular.otf'
    font = ImageFont.truetype(font_filename, 20)
    imagePil = Image.fromarray(image)
    draw = ImageDraw.Draw(imagePil)
    draw.text((x, y), text, fill=color, font=font)
    image = np.array(imagePil)

def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr,1,0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin,ymin,xmax,ymax)

barcode = cv2.barcode_BarcodeDetector()                   # 建立 BarCode 偵測器
ok, data, data_type, bbox = barcode.detectAndDecode(image)  # 偵測 BarCode
# 如果有 BarCode
if ok:
    # 依序取出所有 BarCode 內容
    for i in range(len(data)):
        box = boxSize(bbox[i])   # 取出座標
        text = data[i]           # 取出內容
        cv2.rectangle(image,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 繪製外框
        putText(box[0],box[3],text,color=(0,0,255))                     # 放入文字

cvshow("image", image)
"""
print("------------------------------------------------------------")  # 60個
print("OpenCV_40 按上下調整亮度 按左右調整對比度 按ESC離開")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)


# 定義調整亮度對比的函式
def adjust(i, c, b):
    output = i * (c / 100 + 1) - c + b  # 轉換公式
    output = np.clip(output, 0, 255)
    output = np.uint8(output)
    return output


contrast = 0  # 初始化要調整對比度的數值
brightness = 0  # 初始化要調整亮度的數值

cv2.imshow("ImageShow", image)

while True:
    keycode = cv2.waitKey(0)
    if keycode == 0:
        brightness = brightness + 5  # 按下鍵盤的「上」，增加亮度
    if keycode == 1:
        brightness = brightness - 5  # 按下鍵盤的「下」，減少亮度
    if keycode == 2:
        contrast = contrast - 5  # 按下鍵盤的「右」，增加對比度
    if keycode == 3:
        contrast = contrast + 5  # 按下鍵盤的「左」，減少對比度
    if keycode == 113:
        contrast, brightness = 0, 0  # 按下鍵盤的「q」，恢復預設值
    if keycode == 27:
        break
    show = image.copy()  # 複製原始圖片
    show = adjust(show, contrast, brightness)  # 根據亮度和對比度的調整值，輸出新的圖片
    cv2.imshow("ImageShow", show)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("三種二值化方法")

THRESHOLD = 127

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t1, thd = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY)

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

show()

print("------------------------------------------------------------")  # 60個

THRESHOLD = 127

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t1, thd = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY)
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

show()

print("------------------------------------------------------------")  # 60個

print("圖片的二值化處理, 要先轉成灰階, 再二值化")

THRESHOLD = 30
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
thr, image_binary = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TOZERO)
print(thr)

plt.imshow(cv2.cvtColor(image_binary, cv2.COLOR_BGR2RGB))
show()

print("------------------------------------------------------------")  # 60個

print("OpenCV_09 各種二值化")

THRESHOLD = 127

# 檔案 => cv2影像
image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

# 轉換前，都先將圖片轉換成灰階色彩
#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
ret, output1 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_BINARY
)  # 如果大於 THRESHOLD 就等於 255，反之等於 0。

ret, output2 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_BINARY_INV
)  # 如果大於 THRESHOLD 就等於 0，反之等於 255。

ret, output3 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TRUNC
)  # 如果大於 THRESHOLD 就等於 THRESHOLD，反之數值不變。

ret, output4 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TOZERO
)  # 如果大於 THRESHOLD 數值不變，反之數值等於 0。

ret, output5 = cv2.threshold(
    image_gray, THRESHOLD, 255, cv2.THRESH_TOZERO_INV
)  # 如果大於 THRESHOLD 等於 0，反之數值不變。

cvshow("image", image)
cvshow("image1", output1)
cvshow("image2", output2)
cvshow("image3", output3)
cvshow("image4", output4)
cvshow("image5", output5)

print("------------------------------------------------------------")  # 60個
print("OpenCV_10")

THRESHOLD = 127

# 檔案 => cv2影像
image = cv2.imread(filename)

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

# 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(image_gray, THRESHOLD, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
output3 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cvshow("image", image)
cvshow("image1", output1)
cvshow("image2", output2)
cvshow("image3", output3)

print("------------------------------------------------------------")  # 60個

print("共用函數------------------------------------------------------------")  # 60個

from scipy import signal


# sobel 邊緣檢測
def sobel(image, winSize):
    rows, cols = image.shape
    pascalSmoothKernel = pascalSmooth(winSize)
    pascalDiffKernel = pascalDiff(winSize)
    # --- 與水平方向的卷積核卷積 ----
    image_sobel_x = np.zeros(image.shape, np.float32)
    # 垂直方向上的平滑
    image_sobel_x = signal.convolve2d(
        image, pascalSmoothKernel.transpose(), mode="same"
    )
    # 水平方向上的差分
    image_sobel_x = signal.convolve2d(image_sobel_x, pascalDiffKernel, mode="same")
    # --- 與垂直方向上的卷積核卷積 ---
    image_sobel_y = np.zeros(image.shape, np.float32)
    # 水平方向上的平滑
    image_sobel_y = signal.convolve2d(image, pascalSmoothKernel, mode="same")
    # 垂直方向上的差分
    image_sobel_y = signal.convolve2d(
        image_sobel_y, pascalDiffKernel.transpose(), mode="same"
    )
    return (image_sobel_x, image_sobel_y)


# 二項式展開式的系數，即平滑系數
def pascalSmooth(n):
    pascalSmooth = np.zeros([1, n], np.float32)
    for i in range(n):
        pascalSmooth[0][i] = math.factorial(n - 1) / (
            math.factorial(i) * math.factorial(n - 1 - i)
        )
    return pascalSmooth


# 計算差分
def pascalDiff(n):
    pascalDiff = np.zeros([1, n], np.float32)
    pascalSmooth_previous = pascalSmooth(n - 1)
    for i in range(n):
        if i == 0:
            # 恒等於 1
            pascalDiff[0][i] = pascalSmooth_previous[0][i]
        elif i == n - 1:
            # 恒等於 -1
            pascalDiff[0][i] = -pascalSmooth_previous[0][i - 1]
        else:
            pascalDiff[0][i] = (
                pascalSmooth_previous[0][i] - pascalSmooth_previous[0][i - 1]
            )
    return pascalDiff


# 通過平滑系數和差分系數的卷積運算計算卷積核
def getSobelKernel(winSize):
    pascalSmoothKernel = pascalSmooth(winSize)
    pascalDiffKernel = pascalDiff(winSize)
    # 水平方向上的卷積核
    sobelKernel_x = signal.convolve2d(
        pascalSmoothKernel.transpose(), pascalDiffKernel, mode="full"
    )
    # 垂直方向上的卷積核
    sobelKernel_y = signal.convolve2d(
        pascalSmoothKernel, pascalDiffKernel.transpose(), mode="full"
    )
    return (sobelKernel_x, sobelKernel_y)


print("------------------------------------------------------------")  # 60個

print("測試 cv2.linearPolar")
print("空間變換 極座標變換 linearPolar_OpenCV3")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
src = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)

# 顯示原圖
cvshow("src", src)

# 圖像的極坐標變換
dst = cv2.linearPolar(src, (508, 503), 550, cv2.INTER_LINEAR)

# 顯示極坐標變化的結果
cvshow("dst", dst)

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("極座標變換")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

print("測試 cv2.logPolar")

print("空間變換 極座標變換 logPolar")

# 檔案 => cv2影像
src = cv2.imread(filename, cv2.IMREAD_ANYCOLOR)

# 顯示原圖
cvshow("src", src)

# 圖像的極坐標變換
M = 150
dst = cv2.logPolar(src, (508, 503), M, cv2.WARP_FILL_OUTLIERS)
# 顯示極坐標變化的結果
print(src.shape)
print(dst.shape)

cvshow("dst", dst)

print("------------------------------------------------------------")  # 60個

print("對比度增強2")


# 分段線性變換
def piecewiseLinear(image, point1, point2):
    # 確保 point1 在 point2的左下角
    x1, y1 = point1
    x2, y2 = point2
    # 0 - point1.x
    a1 = float(y1) / x1
    b1 = 0
    # point1.x - point2.x
    a2 = float(y2 - y1) / float(x2 - x1)
    b2 = y1 - a2 * x1
    print(a2)
    # point2.x - 255
    a3 = float(255 - y2) / (255 - x2)
    b3 = 255 - a3 * 255
    # 輸出圖像
    outPutImage = np.zeros(image.shape, np.uint8)
    # 圖像的寬高
    rows, cols = image.shape
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            if pixel <= x1:
                outPixel = a1 * pixel + b1
            elif pixel > x1 and pixel < x2:
                outPixel = a2 * pixel + b2
            else:
                outPixel = a3 * pixel + b3
            outPixel = round(outPixel)
            outPutImage[r][c] = outPixel
    return outPutImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

cvshow("image", image)

# 分段線性變換
outPutImage = piecewiseLinear(image, (100, 50), (150, 230))
cvshow("outPutImage", outPutImage)

# 顯示直方圖正規化後圖片的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = outPutImage.shape
histSeq = outPutImage.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強3 histNormalized")


# 直方圖正規化
# 1、若輸入是 8 位圖 ，一般設置 O_min = 0，O_max = 255
# 2、若輸入的是歸一化的圖像，一般設置 O_min = 0，O_max = 1
def histNormalized(InputImage, O_min=0, O_max=255):
    # 得到輸入圖像的最小灰度值
    I_min = np.min(InputImage)
    # 得到輸入圖像的最大灰度值
    I_max = np.max(InputImage)
    # 得到輸入圖像的寬高
    rows, cols = InputImage.shape
    # 輸出圖像
    OutputImage = np.zeros(InputImage.shape, np.float32)
    # 輸出圖像的映射
    cofficient = float(O_max - O_min) / float(I_max - I_min)
    for r in range(rows):
        for c in range(cols):
            OutputImage[r][c] = cofficient * (InputImage[r][c] - I_min) + O_min
    return OutputImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 直方圖正規化
histNormResult = histNormalized(image)
# 數據類型轉換，灰度級顯示
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
# 顯示直方圖正規化的圖片
cvshow("histNormlized", histNormResult)

"""
#如果輸入圖像是歸一化的圖像
image_0_1 = image/255.0
#直方圖正規化
histNormResult = histNormalized(image_0_1,0,1)
#保存結果
histNormResult = 255.0*histNormResult
histNormResult = np.round(histNormResult)
histNormResult = histNormResult.astype(np.uint8)
"""
# 顯示直方圖正規化後圖片的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = image.shape
histNormResultSeq = histNormResult.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histNormResultSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("對比度增強5 equalHist")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 直方圖均衡化
def equalHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 計算灰度直方圖
    grayHist = calcGrayHist(image)
    # 計算累積灰度直方圖
    zeroCumuMoment = np.zeros([256], np.uint32)
    for p in range(256):
        if p == 0:
            zeroCumuMoment[p] = grayHist[0]
        else:
            zeroCumuMoment[p] = zeroCumuMoment[p - 1] + grayHist[p]
    # 根據直方圖均衡化得到的輸入灰度級和輸出灰度級的映射
    outPut_q = np.zeros([256], np.uint8)
    cofficient = 256.0 / (rows * cols)
    for p in range(256):
        q = cofficient * float(zeroCumuMoment[p]) - 1
        if q >= 0:
            outPut_q[p] = math.floor(q)
        else:
            outPut_q[p] = 0
    # 得到直方圖均衡化後的圖像
    equalHistImage = np.zeros(image.shape, np.uint8)
    for r in range(rows):
        for c in range(cols):
            equalHistImage[r][c] = outPut_q[image[r][c]]
    return equalHistImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖像
cvshow("image", image)

# 直方圖均衡化
result = equalHist(image)
cvshow("equalHist", result)

# 直方圖均衡話後的灰度直方圖
# 組數
numberBins = 256
# 計算灰度直方圖
rows, cols = image.shape
histEqualResultSeq = result.reshape(
    [
        rows * cols,
    ]
)

histogram, bins, patch_image = plt.hist(
    histEqualResultSeq, numberBins, facecolor="black", histtype="bar"
)

plt.xlabel("灰階值 0~255")
plt.ylabel("統計點數")

# 設置坐標軸的范圍
y_maxValue = np.max(histogram)
plt.axis([0, 255, 0, y_maxValue])

show()

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣擴充/擴充邊界 copyMakeBorder")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image0 = cv2.imread(filename)

# 擴充邊界
top = 50
bottom = 100
left = 150
right = 200
image1 = cv2.copyMakeBorder(image0, top, bottom, left, right, cv2.BORDER_DEFAULT)

cvshow("image0", image0)
cvshow("image1", image1)

print("------------------------------------------------------------")  # 60個

from scipy import signal

print("圖像平滑 sameConv2d")

# 輸入矩陣
I = np.array([[1, 2], [3, 4]], np.float32)
# I 的高和寬
H1, W1 = I.shape[:2]
# 卷積核
K = np.array([[-1, -2], [2, 1]], np.float32)
# K 的高和寬
H2, W2 = K.shape[:2]
# 計算 full 卷積
c_full = signal.convolve2d(I, K, mode="full")
# 指定錨點的位置
kr, kc = 1, 0
# 根據錨點位置，從 full 卷積中截取得到 same 卷積
c_same = c_full[H2 - kr - 1 : H1 + H2 - kr - 1, W2 - kc - 1 : W1 + W2 - kc - 1]
print(c_same)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 sepConv")

from scipy import signal

kernel1 = np.array([[1, 2, 3]], np.float32)
kernel2 = np.array([[4], [5], [6]], np.float32)
# 計算兩個核的全卷積
kernel = signal.convolve2d(kernel1, kernel2, mode="full")

print("------------------------------------------------------------")  # 60個

print("圖像平滑 conv")

from scipy import signal

# 圖像矩陣
"""
I=np.array([[1,2,3,10,12],
            [32,43,12,4,190],
            [12,234,78,0,12],
            [43,90,32,8,90],
            [71,12,4,98,123]],np.float32)
"""
I = np.ones((10, 10), np.float32)
I[1:3, 3:5] = 5
I[3:5, 4:7] = 3

# 卷積核
"""
    kernel = np.array([[1,0,-1],
                   [1,0,-1],
                   [1,0,-1]])
"""

kernel1 = np.array([[1, 3, 4], [9, 10, 2], [-1, 10, 2]], np.float32)
kernel2 = np.array([[-1, 2, 3], [4, 5, 6], [10, 9, 10]], np.float32)
# kernel1 = np.array([[-1,2,3]],np.float32)
# kernel2 = np.array([[10],[43],[1]],np.float32)
kernel = signal.convolve2d(kernel1, kernel2, mode="full")
print(kernel)

# 第一種方式:直接進行卷積運算得到的結果
I_Kernel = signal.convolve2d(I, kernel, mode="same", boundary="symm", fillvalue=0)

# 第二種方式:用可分離卷積核性質得到的結果
I_kernel1 = signal.convolve2d(I, kernel1, mode="same", boundary="wrap", fillvalue=0)
I_kernel1_kernel2 = signal.convolve2d(
    I_kernel1, kernel2, mode="same", boundary="wrap", fillvalue=0
)

# print(I_Kernel)
print("*******************")
print(np.max(np.abs(I_Kernel - I_kernel1_kernel2)))
print("********************")
print(I_Kernel)
print(I_kernel1_kernel2)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 conv2")

from scipy import signal

# 圖像矩陣
I = np.array(
    [
        [1, 2, 3, 10, 12],
        [32, 43, 12, 4, 190],
        [12, 234, 78, 0, 12],
        [43, 90, 32, 8, 90],
        [71, 12, 4, 98, 123],
    ],
    np.float32,
)
# 卷積核
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
# full 卷積
fullConv = signal.convolve2d(I, kernel, mode="full", boundary="fill", fillvalue=0)
# same 卷積
sameConv = signal.convolve2d(I, kernel, mode="same", boundary="symm")
# valid 卷積
validConv = signal.convolve2d(I, kernel, mode="valid")
print(fullConv)
print(sameConv)
print(validConv)

print("------------------------------------------------------------")  # 60個

from scipy import signal

# 得到高斯平滑算子：
# getGaussKernel(sigma,H,W),使用過程中一般H和W一般為奇數，sigma大於零


def getGaussKernel(sigma, H, W):
    # 第一步：構建高斯矩陣gaussMatrix
    gaussMatrix = np.zeros([H, W], np.float32)
    # 得到中心點的位置
    cH = (H - 1) / 2
    cW = (W - 1) / 2
    # 計算1/(2*pi*sigma^2)
    coefficient = 1.0 / (2 * np.pi * math.pow(sigma, 2))
    #
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r - cH, 2) + math.pow(c - cW, 2)
            gaussMatrix[r][c] = coefficient * math.exp(
                -norm2 / (2 * math.pow(sigma, 2))
            )
    # 第二步：計算高斯矩陣的和
    sumGM = np.sum(gaussMatrix)
    # 第三步：歸一化，gaussMatrix/sumGM
    gaussKernel = gaussMatrix / sumGM
    return gaussKernel


gaussKernel = getGaussKernel(2, 3, 3)
print(gaussKernel)
# 高斯核gaussKernel是可分解的，可以分解為水平方向和垂直方向的卷積核
gaussKernel_x = getGaussKernel(2, 1, 3)
print(gaussKernel_x)
gaussKernel_y = getGaussKernel(2, 3, 1)
print(gaussKernel_y)

"""
水平方向和垂直方向的卷積核進行卷積運算,注意：mode='full',boundary = 'fill',fillvalue=0
這樣的參數設置，得到的結果才和gaussKernel完全相等，否則，邊界不相等
"""
gaussKernel_xy = signal.convolve2d(
    gaussKernel_x, gaussKernel_y, mode="full", boundary="fill", fillvalue=0
)
print(gaussKernel_xy)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 gaussBlur")

from scipy import signal


# 高斯平滑，返回的數據類型為浮點型
def gaussBlur(image, sigma, H, W, _boundary="fill", _fillvalue=0):
    # 構建HxW的高斯平滑算子
    # gaussKernelxy = getGaussKernel(sigma,H,W)
    # 圖像矩陣和高斯卷積核卷積
    # gaussBlur_xy = signal.convolve2d(image,gaussKernelxy,mode='same',boundary = _boundary,fillvalue=_fillvalue)
    # return gaussBlur_xy
    # 因為高斯核是可分解的，根據卷積的結合律
    # 先進行水平方向的卷積，然後再進行垂直方向的卷積
    gaussKenrnel_x = getGaussKernel(sigma, 1, W)
    gaussBlur_x = signal.convolve2d(
        image, gaussKenrnel_x, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    gaussKenrnel_y = getGaussKernel(sigma, H, 1)
    gaussBlur_xy = signal.convolve2d(
        gaussBlur_x,
        gaussKenrnel_y,
        mode="same",
        boundary=_boundary,
        fillvalue=_fillvalue,
    )
    return gaussBlur_xy


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

cvshow("image", image)

# 3 11 11 9 25 25
blurImage = gaussBlur(image, 5, 51, 51, "symm")
# 如果輸入的圖像是8位圖,輸出的
blurImage = np.round(blurImage)
blurImage = blurImage.astype(np.uint8)
cvshow("gaussBlur", blurImage)

# 如果輸入的圖像數據類型是浮點型，且像素值歸一到[0,1]
image_0_1 = image / 255.0
blurImage_0_1 = gaussBlur(image_0_1, 4, 5, 5, "symm")
# cvshow("gaussBlur-0-1",blurImage_0_1)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 fastMeanBlur")


# 圖像積分
def integral(image):
    rows, cols = image.shape
    # 行積分運算
    inteImageC = np.zeros((rows, cols), np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = image[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c - 1] + image[r][c]
    # 列積分運算
    inteImage = np.zeros(image.shape, np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r - 1][c] + inteImageC[r][c]
    # 為了在快速均值平滑使用中省去判斷邊界的問題
    # 上邊和左邊進行補零
    inteImage_0 = np.zeros((rows + 1, cols + 1), np.float32)
    inteImage_0[1 : rows + 1, 1 : cols + 1] = inteImage
    return inteImage_0


# 快速均值平滑：返回數組的數據類型是浮點型，winSize = ( 高，寬 )
def fastMeanBlur(image, winSize, borderType=cv2.BORDER_DEFAULT):
    halfH = (winSize[0] - 1) // 2
    halfW = (winSize[1] - 1) // 2
    ratio = 1.0 / (winSize[0] * winSize[1])
    # 邊緣擴充
    paddImage = cv2.copyMakeBorder(image, halfH, halfH, halfW, halfW, borderType)
    # 圖像積分
    paddIntegral = integral(paddImage)
    # 圖像的寬高
    rows, cols = image.shape
    # 均值濾波後的結果
    meanBlurImage = np.zeros(image.shape, np.float32)
    r, c = 0, 0
    for h in range(halfH, halfH + rows, 1):
        for w in range(halfW, halfW + cols, 1):
            meanBlurImage[r][c] = (
                paddIntegral[h + halfH + 1][w + halfW + 1]
                + paddIntegral[h - halfH][w - halfW]
                - paddIntegral[h + halfH + 1][w - halfW]
                - paddIntegral[h - halfH][w + halfW + 1]
            ) * ratio
            c += 1
        r += 1
        c = 0
    return meanBlurImage


filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 快速均值平滑
meanBlurImage = fastMeanBlur(image, (15, 15), cv2.BORDER_DEFAULT)

# 數據類型轉換
meanBlurImage = np.round(meanBlurImage)
meanBlurImage = meanBlurImage.astype(np.uint8)

cvshow("fastMeanBlur", meanBlurImage)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 medianBlur")


# 中值濾波
def medianBlur(image, winSize):
    # 圖像的寬高
    rows, cols = image.shape
    # 窗口的寬高，均為奇數
    winH, winW = winSize
    halfWinH = (winH - 1) // 2
    halfWinW = (winW - 1) // 2
    # 中值濾波後的輸出圖像
    medianBlurImage = np.zeros(image.shape, image.dtype)
    for r in range(rows):
        for c in range(cols):
            # 判斷邊界
            rTop = 0 if r - halfWinH < 0 else r - halfWinH
            rBottom = rows - 1 if r + halfWinH > rows - 1 else r + halfWinH
            cLeft = 0 if c - halfWinW < 0 else c - halfWinW
            cRight = cols - 1 if c + halfWinW > cols - 1 else c + halfWinW
            # 取中值的區域
            region = image[rTop : rBottom + 1, cLeft : cRight + 1]
            # 求中值
            medianBlurImage[r][c] = np.median(region)
    return medianBlurImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 中值濾波
medianBlurImage = medianBlur(image, (3, 3))

# 顯示中值濾波後的結果
cvshow("medianBlurImage", medianBlurImage)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 BFilter")


# 基於空間距離的權重因子 ( 和計算高斯算子的過程是一樣的 )
def getClosenessWeight(sigma_g, H, W):
    # 第一步：構建高斯矩陣gaussMatrix
    gaussMatrix = np.zeros([H, W], np.float32)
    # 得到中心點的位置
    cH = (H - 1) / 2
    cW = (W - 1) / 2
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r - cH, 2.0) + math.pow(c - cW, 2.0)
            gaussMatrix[r][c] = math.exp(-norm2 / (2 * math.pow(sigma_g, 2.0)))
    # 第二步：計算高斯矩陣的和
    sumGM = np.sum(gaussMatrix)
    # 第三步：歸一化，gaussMatrix/sumGM
    gaussMatrix = gaussMatrix / sumGM
    return gaussMatrix


# BilateralFiltering 雙邊濾波，返回的數據類型為浮點型
def bfltGray(image, winH, winW, sigma_g, sigma_d):
    # 構建空間距離的權重因子
    closenessWeight = getClosenessWeight(sigma_g, winH, winW)
    # 得到卷積核的中心點坐標
    halfWinH = (winH - 1) // 2
    halfWinW = (winW - 1) // 2
    # 圖像矩陣的行數和列數
    rows, cols = image.shape
    # 雙邊濾波後的結果
    bfltGrayImage = np.zeros(image.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            # 判斷邊界
            rTop = 0 if r - halfWinH < 0 else r - halfWinH
            rBottom = rows - 1 if r + halfWinH > rows - 1 else r + halfWinH
            cLeft = 0 if c - halfWinW < 0 else c - halfWinW
            cRight = cols - 1 if c + halfWinW > cols - 1 else c + halfWinW
            # 核作用的區域
            region = image[rTop : rBottom + 1, cLeft : cRight + 1]
            # 構建灰度值相似性的權重因子
            similarityWeightTemp = np.exp(
                -0.5 * pow(region - pixel, 2.0) / pow(sigma_d, 2.0)
            )  # 錯誤
            closenessWeightTemp = closenessWeight[
                rTop - r + halfWinH : rBottom - r + halfWinH + 1,
                cLeft - c + halfWinW : cRight - c + halfWinW + 1,
            ]
            # 兩個核相乘
            weightTemp = similarityWeightTemp * closenessWeightTemp
            weightTemp = weightTemp / np.sum(weightTemp)
            bfltGrayImage[r][c] = np.sum(region * weightTemp)
    return bfltGrayImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 雙邊濾波
image = image.astype(np.float32)
bfltImage = bfltGray(image, 21, 21, 30, 30)
bfltImage = bfltImage / 255.0
# 顯示雙邊濾波的結果
bfltImage = bfltImage.astype(np.float32)
cvshow("BilateralFiltering", bfltImage)

# 因為雙邊濾波返回的是數據類型是浮點型的,可以轉換為 8 位圖
# bfltImage = bfltImage*255.0
# bfltImage = np.round(bfltImage)
# bfltImage = bfltImage.astype(np.uint8)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("圖像平滑 BilateralFiltering")


# 基於空間距離的權重模板 ( 和計算高斯算子的過程是一樣的 )
def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    closeWeight = np.exp(
        -0.5 * (np.power(r, 2) + np.power(c, 2)) / math.pow(sigma_g, 2)
    )
    return closeWeight


# BilateralFiltering 雙邊濾波，返回的數據類型為浮點型
def bfltGray(I, H, W, sigma_g, sigma_d):
    # 構建空間距離的權重模板
    closenessWeight = getClosenessWeight(sigma_g, H, W)
    # 模板的中心點位置
    cH = (H - 1) // 2
    cW = (W - 1) // 2
    # 圖像矩陣的行數和列數
    rows, cols = I.shape
    # 雙邊濾波後的結果
    bfltGrayImage = np.zeros(I.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = I[r][c]
            # 判斷邊界
            rTop = 0 if r - cH < 0 else r - cH
            rBottom = rows - 1 if r + cH > rows - 1 else r + cH
            cLeft = 0 if c - cW < 0 else c - cW
            cRight = cols - 1 if c + cW > cols - 1 else c + cW
            # 權重模板作用的區域
            region = I[rTop : rBottom + 1, cLeft : cRight + 1]
            # 構建灰度值相似性的權重因子
            similarityWeightTemp = np.exp(
                -0.5 * np.power(region - pixel, 2.0) / math.pow(sigma_d, 2)
            )
            closenessWeightTemp = closenessWeight[
                rTop - r + cH : rBottom - r + cH + 1,
                cLeft - c + cW : cRight - c + cW + 1,
            ]
            # 兩個權重模板相乘
            weightTemp = similarityWeightTemp * closenessWeightTemp
            weightTemp = weightTemp / np.sum(weightTemp)
            bfltGrayImage[r][c] = np.sum(region * weightTemp)
    return bfltGrayImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 將灰度值歸一化
image = image / 255.0

# 雙邊濾波
bfltImage = bfltGray(image, 33, 33, 10, 0.8)

# 顯示雙邊濾波的結果
cvshow("BilateralFiltering", bfltImage)

bfltImage = bfltImage * 255.0
bfltImage = np.round(bfltImage)
bfltImage = bfltImage.astype(np.uint8)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 blfFilterColor")


# 基於空間距離的權重因子 ( 和計算高斯核的過程類似 )
def getClosenessWeight(sigma_d, H, W):
    # 構建距離權重因子
    closenessWeight = np.zeros([H, W], np.float32)
    # 得到中心點的位置
    cH = (H - 1) / 2
    cW = (W - 1) / 2
    for r in range(H):
        for c in range(W):
            norm2 = math.pow(r - cH, 2.0) + math.pow(c - cW, 2.0)
            closenessWeight[r][c] = math.exp(-norm2 / (2 * math.pow(sigma_d, 2.0)))
    return closenessWeight


# BilateralFiltering 雙邊濾波，返回的數據類型為浮點型
def blFilter(image, winH, winW, sigma_d, sigma_s):
    # 構建空間距離的權重因子
    closenessWeight = getClosenessWeight(sigma_d, winH, winW)
    # 得到卷積核的中心點坐標
    halfWinH = (winH - 1) // 2
    halfWinW = (winW - 1) // 2
    # 圖像矩陣的行數和列數
    rows, cols = image.shape
    # 雙邊濾波後的結果
    blfImage = np.zeros(image.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            pixel = image[r][c]
            # 判斷邊界
            rTop = 0 if r - halfWinH < 0 else r - halfWinH
            rBottom = rows - 1 if r + halfWinH > rows - 1 else r + halfWinH
            cLeft = 0 if c - halfWinW < 0 else c - halfWinW
            cRight = cols - 1 if c + halfWinW > cols - 1 else c + halfWinW
            # 核作用的區域
            region = image[rTop : rBottom + 1, cLeft : cRight + 1]
            # 構建灰度值相似性的權重因子
            similarityWeightTemp = np.exp(
                -0.5 * np.power(region - pixel, 2.0) / np.power(sigma_s, 2.0)
            )
            closenessWeightTemp = closenessWeight[
                rTop - r + halfWinH : rBottom - r + halfWinH + 1,
                cLeft - c + halfWinW : cRight - c + halfWinW + 1,
            ]
            # 兩個權重因子對應位置相乘
            weightTemp = similarityWeightTemp * closenessWeightTemp
            # 歸一化
            weightTemp = weightTemp / np.sum(weightTemp)
            blfImage[r][c] = np.sum(region * weightTemp)
    return blfImage


# 彩色雙邊濾波 返回的是浮點型
def blFilterColor(colorImage, winH, winW, sigma_d, sigma_s):
    # 分別對三個顏色通道進行雙邊濾波
    blfColorImage = np.zeros(colorImage.shape, np.float32)
    for c in range(3):
        blfColorImage[:, :, c] = blFilter(
            colorImage[:, :, c], winH, winW, sigma_d, sigma_s
        )
    return blfColorImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# 顯示原圖
cvshow("image", image)

# 彩色雙邊濾波
image = image.astype(np.float32)  # 注意首先轉換為浮點型
blfColorImage = blFilterColor(image, 27, 27, 100, 30)
# 顯示結果
blfColorImage = np.round(blfColorImage)
blfColorImage = blfColorImage.astype(np.uint8)
cvshow("blfFilterColor", blfColorImage)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 JointBilterFilter")


# 基於空間距離的權重模板 ( 和計算高斯算子的過程是一樣的 )
def getClosenessWeight(sigma_g, H, W):
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    closeWeight = np.exp(
        -0.5 * (np.power(r, 2.0) + np.power(c, 2.0)) / math.pow(sigma_g, 2.0)
    )
    return closeWeight


def jointBLF(I, H, W, sigma_g, sigma_d, borderType=cv2.BORDER_DEFAULT):
    # 構建空間距離的權重模板
    closenessWeight = getClosenessWeight(sigma_g, H, W)
    # 對 I 進行高斯平滑
    Ig = cv2.GaussianBlur(I, (W, H), sigma_g)  # 執行高斯模糊化
    # 模板的中心點位置
    cH = (H - 1) // 2
    cW = (W - 1) // 2
    # 對原圖和高斯平滑的結果擴充邊界
    Ip = cv2.copyMakeBorder(I, cH, cH, cW, cW, borderType)
    Igp = cv2.copyMakeBorder(Ig, cH, cH, cW, cW, borderType)
    # 圖像矩陣的行數和列數
    rows, cols = I.shape
    i, j = 0, 0
    # 聯合雙邊濾波結果
    jblf = np.zeros(I.shape, np.float64)
    for r in np.arange(cH, cH + rows, 1):
        for c in np.arange(cW, cW + cols, 1):
            # 當前位置的值
            pixel = Igp[r][c]
            # 當前位置的鄰域
            rTop, rBottom = r - cH, r + cH
            cLeft, cRight = c - cW, c + cW
            # 從 Igp 中截取該鄰域，用於構建相似性權重
            region = Igp[rTop : rBottom + 1, cLeft : cRight + 1]
            # 通過上述鄰域,構建該位置的相似性權重模板
            similarityWeight = np.exp(
                -0.5 * np.power(region - pixel, 2.0) / math.pow(sigma_d, 2.0)
            )
            # 相似性權重模板和空間距離權重模板形成
            weight = closenessWeight * similarityWeight
            # 將權重模板歸一化
            weight = weight / np.sum(weight)
            # 權重模板和鄰域對應位置相乘并求和
            jblf[i][j] = np.sum(Ip[rTop : rBottom + 1, cLeft : cRight + 1] * weight)
            j += 1
        j = 0
        i += 1
    return jblf


# 檔案 => cv2影像
I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 將 8 位圖轉換為 浮點型
fI = I.astype(np.float64)
# 聯合雙邊濾波，返回值的數據類型為浮點型
jblf = jointBLF(fI, 33, 33, 7, 2)
# 轉換為 8 位圖
jblf = np.round(jblf)
jblf = jblf.astype(np.uint8)
cvshow("jblf", jblf)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 fastGuidedFilter")


# 快速導向濾波，輸入的圖像數據類型為歸一到[0,1]的浮點型
# s屬於(0,1] ,
# 建議 r>=4, 1/r=<s<=4/r
def fastGuidedFilter(I, p, r, eps, s):
    # 輸入圖像的寬高
    rows, cols = I.shape
    # 縮小圖像
    small_I = cv2.resize(
        I,
        dsize=(int(round(s * cols)), int(round(s * rows))),
        interpolation=cv2.INTER_CUBIC,
    )
    small_p = cv2.resize(
        p,
        dsize=(int(round(s * cols)), int(round(s * rows))),
        interpolation=cv2.INTER_CUBIC,
    )
    # 縮放均值平滑的窗口半徑
    small_r = int(round(r * s))  # 確保是整型
    winSize = (2 * small_r + 1, 2 * small_r + 1)
    # small_I 的均值平滑
    mean_small_I = fastMeanBlur(small_I, winSize, cv2.BORDER_DEFAULT)
    # small_p 的均值平滑
    mean_small_p = fastMeanBlur(small_p, winSize, cv2.BORDER_DEFAULT)
    # small_I.*small_p 的均值平滑
    small_Ip = small_I * small_p
    mean_small_Ip = fastMeanBlur(small_Ip, winSize, cv2.BORDER_DEFAULT)
    # 協方差
    cov_small_Ip = mean_small_Ip - mean_small_I * mean_small_p
    mean_small_II = fastMeanBlur(small_I * small_I, winSize, cv2.BORDER_DEFAULT)
    # 方差
    var_small_I = mean_small_II - mean_small_I * mean_small_I
    small_a = cov_small_Ip / (var_small_I + eps)
    small_b = mean_small_p - small_a * mean_small_I
    # 對 small_a 和 small_b 進行均值平滑
    mean_small_a = fastMeanBlur(small_a, winSize, cv2.BORDER_DEFAULT)
    mean_small_b = fastMeanBlur(small_b, winSize, cv2.BORDER_DEFAULT)
    # 放大 small_a 和 small_b
    mean_a = cv2.resize(
        mean_small_a, dsize=(cols, rows), interpolation=cv2.INTER_LINEAR
    )
    mean_b = cv2.resize(
        mean_small_b, dsize=(cols, rows), interpolation=cv2.INTER_LINEAR
    )
    q = mean_a * I + mean_b
    return q


# 彩色快速導向濾波（平滑）
def fGFColorSmooth(I, r, eps, s):
    q_color = np.zeros(I.shape, np.float64)
    # 對每一個通道進行導向濾波
    for c in range(3):
        q_color[:, :, c] = fastGuidedFilter(I[:, :, c], I[:, :, c], r, eps, s)
    return q_color


# 細節增強
def fGFEnchance(I, r, eps, s):
    # 導向平滑處理
    qColor = fGFColorSmooth(I, r, eps, s)
    # 細節增強處理
    enchanced = (I - qColor) * 5 + qColor
    """
    for c in range(3):
        enchanced[:,:,c] = cv2.normalize(enchanced[:,:,c],alpha = 1,beta = 0,norm_type = cv2.NORM_MINMAX)
    """
    enchanced = cv2.normalize(enchanced, alpha=1, beta=0, norm_type=cv2.NORM_MINMAX)
    return enchanced


""" NG
# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_COLOR)

#顯示原圖
cvshow("image",image)

#快速導向濾波（彩色圖像平滑）
image_0_1 = image/255.0
result = fGFColorSmooth(image_0_1,5,pow(0.1,2.0),1.0/3)
cvshow("fastGuidedFilter",result)

#細節增強
enchanced = fGFEnchance(image_0_1,5,pow(0.2,2.0),1.0/3)
cvshow("fGFEnchance",enchanced)
"""
print("------------------------------------------------------------")  # 60個

print("圖像平滑 guidedFilter")


# 導向濾波
def guidedFilter(I, p, winSize, eps):
    # 輸入圖像的寬高
    rows, cols = I.shape
    # I 的均值平滑
    mean_I = fastMeanBlur(I, winSize, cv2.BORDER_DEFAULT)
    # p 的均值平滑
    mean_p = fastMeanBlur(p, winSize, cv2.BORDER_DEFAULT)
    # I.*p 的均值平滑
    Ip = I * p
    mean_Ip = fastMeanBlur(Ip, winSize, cv2.BORDER_DEFAULT)
    # 協方差
    cov_Ip = mean_Ip - mean_I * mean_p
    mean_II = fastMeanBlur(I * I, winSize, cv2.BORDER_DEFAULT)
    # 方差
    var_I = mean_II - mean_I * mean_I
    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I
    # 對 a 和 b進行均值平滑
    mean_a = fastMeanBlur(a, winSize, cv2.BORDER_DEFAULT)
    mean_b = fastMeanBlur(b, winSize, cv2.BORDER_DEFAULT)
    q = mean_a * I + mean_b
    return q


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 將圖像歸一化
image_0_1 = image / 255.0

# 顯示原圖
cvshow("image", image)

# 導向濾波
result = guidedFilter(image_0_1, image_0_1, (17, 17), pow(0.2, 2.0))
cvshow("guidedFilter", result)

# 保存導向濾波的結果
result = result * 255
result[result > 255] = 255
result = np.round(result)
result = result.astype(np.uint8)

print("------------------------------------------------------------")  # 60個

print("圖像平滑 guidedFilter_color")


# 導向濾波
def guidedFilter(I, p, winSize, eps):
    # 輸入圖像的寬高
    rows, cols = I.shape
    # I 的均值平滑
    mean_I = fastMeanBlur(I, winSize, cv2.BORDER_DEFAULT)
    # p 的均值平滑
    mean_p = fastMeanBlur(p, winSize, cv2.BORDER_DEFAULT)
    # I.*p 的均值平滑
    Ip = I * p
    mean_Ip = fastMeanBlur(Ip, winSize, cv2.BORDER_DEFAULT)
    # 協方差
    cov_Ip = mean_Ip - mean_I * mean_p
    mean_II = fastMeanBlur(I * I, winSize, cv2.BORDER_DEFAULT)
    # 方差
    var_I = mean_II - mean_I * mean_I
    a = cov_Ip / (var_I + eps)
    b = mean_p - a * mean_I
    # 對 a 和 b進行均值平滑
    mean_a = fastMeanBlur(a, winSize, cv2.BORDER_DEFAULT)
    mean_b = fastMeanBlur(b, winSize, cv2.BORDER_DEFAULT)
    q = mean_a * I + mean_b
    return q


filename1 = "C:/_git/vcs/_4.python/opencv/data/pic_brightness1.bmp"
filename2 = "C:/_git/vcs/_4.python/opencv/data/pic_brightness2.bmp"

# 檔案 => cv2影像
I = cv2.imread(filename1, cv2.IMREAD_COLOR)
p = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

# 將圖像歸一化
image_0_1 = I / 255.0
p = p / 255.0

# 顯示原圖
cvshow("image_0_1", image_0_1)

# 導向濾波
result = np.zeros(I.shape)
result[:, :, 0] = guidedFilter(
    image_0_1[:, :, 0], image_0_1[:, :, 0], (17, 17), pow(0.2, 2.0)
)
result[:, :, 1] = guidedFilter(
    image_0_1[:, :, 1], image_0_1[:, :, 1], (17, 17), pow(0.2, 2.0)
)
result[:, :, 2] = guidedFilter(
    image_0_1[:, :, 2], image_0_1[:, :, 2], (17, 17), pow(0.2, 2.0)
)
cvshow("guidedFilter", result)

# 保存導向濾波的結果
result = result * 255
result[result > 255] = 255
result = np.round(result)
result = result.astype(np.uint8)

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshold_OpenCV3")

src = np.array(
    [[123, 234, 68], [33, 51, 17], [48, 98, 234], [129, 89, 27], [45, 167, 134]],
    np.uint8,
)
# 手動設置閾值
the = 150
maxval = 255
dst = cv2.threshold(src, the, maxval, cv2.THRESH_BINARY)
# Otsu 閾值處理
otsuThe = 0
otsuThe, dst_Otsu = cv2.threshold(src, otsuThe, maxval, cv2.THRESH_OTSU)
print(otsuThe, dst_Otsu)
# TRIANGLE 閾值處理
triThe = 0
triThe, dst_tri = cv2.threshold(src, triThe, maxval, cv2.THRESH_TRIANGLE)
print(triThe, dst_tri)

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshTwoPeaks")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 返回閾值和二值圖
def threshTwoPeaks(image):
    # 計算回復直方圖
    histogram = calcGrayHist(image)
    # 找到灰度直方圖的最大峰值對應的灰度值
    maxLoc = np.where(histogram == np.max(histogram))
    firstPeak = maxLoc[0]
    print(maxLoc[0])
    # 尋找灰度直方圖的 " 第二個峰值 " 對應的灰度值
    measureDists = np.zeros([256], np.float32)
    for k in range(256):
        measureDists[k] = pow(k - firstPeak, 2) * histogram[k]
    maxLoc2 = np.where(measureDists == np.max(measureDists))
    secondPeak = maxLoc2[0]
    # 找到兩個峰值之間的最小值對應的灰度值，作為閾值
    thresh = 0
    if firstPeak > secondPeak:
        temp = histogram[int(secondPeak) : int(firstPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = secondPeak + minLoc[0] + 1
    else:
        temp = histogram[int(firstPeak) : int(secondPeak)]
        minLoc = np.where(temp == np.min(temp))
        thresh = firstPeak + minLoc[0] + 1
    # 找到閾值後進行閾值處理，得到二值圖
    threshImage_out = image.copy()
    threshImage_out[threshImage_out > thresh] = 255
    threshImage_out[threshImage_out <= thresh] = 0
    return (thresh, threshImage_out)


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

thresh, threshImage_out = threshTwoPeaks(image)
# 輸出直方圖技術得到的閾值
print(thresh)

# 顯示原圖和閾值化得到的二值圖
cvshow("image", image)

cvshow("threshTwoPeaks", threshImage_out)

print("------------------------------------------------------------")  # 60個

print("閾值分割 threshEntroy")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[image[r][c]] += 1
    return grayHist


# 熵閾值法
def threshEntroy(image):
    rows, cols = image.shape
    # 求灰度直方圖
    grayHist = calcGrayHist(image)
    # 歸一化灰度直方圖
    normGrayHist = grayHist / float(rows * cols)
    # 計算累加直方圖，也稱零階累加矩
    zeroCumuMoment = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[k] = normGrayHist[k]
        else:
            zeroCumuMoment[k] = zeroCumuMoment[k - 1] + normGrayHist[k]
    # 計算各個灰度級的熵
    entropy = np.zeros([256], np.float32)
    for k in range(256):
        if k == 0:
            if normGrayHist[k] == 0:
                entropy[k] = 0
            else:
                entropy[k] = -normGrayHist[k] * math.log10(normGrayHist[k])
        else:
            if normGrayHist[k] == 0:
                entropy[k] = entropy[k - 1]
            else:
                entropy[k] = entropy[k - 1] - normGrayHist[k] * math.log10(
                    normGrayHist[k]
                )
    # 找閾值
    fT = np.zeros([256], np.float32)
    ft1, ft2 = 0.0, 0.0
    totalEntroy = entropy[255]
    for k in range(255):
        # 找最大值
        maxFront = np.max(normGrayHist[0 : k + 1])
        maxBack = np.max(normGrayHist[k + 1 : 256])
        if (
            maxFront == 0
            or zeroCumuMoment[k] == 0
            or maxFront == 1
            or zeroCumuMoment[k] == 1
            or totalEntroy == 0
        ):
            ft1 = 0
        else:
            ft1 = (
                entropy[k]
                / totalEntroy
                * (math.log10(zeroCumuMoment[k]) / math.log10(maxFront))
            )
        if (
            maxBack == 0
            or 1 - zeroCumuMoment[k] == 0
            or maxBack == 1
            or 1 - zeroCumuMoment[k] == 1
        ):
            ft2 = 0
        else:
            if totalEntroy == 0:
                ft2 = math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack)
            else:
                ft2 = (1 - entropy[k] / totalEntroy) * (
                    math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack)
                )
        fT[k] = ft1 + ft2
    # 找最大值的索引，作為得到的閾值
    threshLoc = np.where(fT == np.max(fT))
    thresh = threshLoc[0][0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return (threshold, thresh)


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 閾值處理
threshold, thresh = threshEntroy(image)
# 顯示閾值後的二值化圖像
cvshow("threshEntroy", threshold)
print(thresh)

print("------------------------------------------------------------")  # 60個

print("閾值分割 otsu")


# 計算圖像灰度直方圖
def calcGrayHist(image):
    # 灰度圖像矩陣的寬高
    rows, cols = image.shape
    # 存儲灰度直方圖
    grayHist = np.zeros([1, 256], np.uint32)
    for r in range(rows):
        for c in range(cols):
            grayHist[0][image[r][c]] += 1
    return grayHist


def ostu(image):
    rows, cols = image.shape
    # 計算圖像的灰度直方圖
    grayHist = calcGrayHist(image)
    # 歸一化灰度直方圖
    uniformGrayHist = grayHist / float(rows * cols)
    # 計算零階累積矩和一階累積矩
    zeroCumuMoment = np.zeros([1, 256], np.float32)
    oneCumuMoment = np.zeros([1, 256], np.float32)
    for k in range(256):
        if k == 0:
            zeroCumuMoment[0][k] = uniformGrayHist[0][0]
            oneCumuMoment[0][k] = (k + 1) * uniformGrayHist[0][0]
        else:
            zeroCumuMoment[0][k] = zeroCumuMoment[0][k - 1] + uniformGrayHist[0][k]
            oneCumuMoment[0][k] = oneCumuMoment[0][k - 1] + k * uniformGrayHist[0][k]
    # 計算類間方差
    variance = np.zeros([1, 256], np.float32)
    for k in range(255):
        if zeroCumuMoment[0][k] == 0:
            variance[0][k] = 0
        else:
            variance[0][k] = math.pow(
                oneCumuMoment[0][255] * zeroCumuMoment[0][k] - oneCumuMoment[0][k], 2
            ) / (zeroCumuMoment[0][k] * (1.0 - zeroCumuMoment[0][k]))
    # 找到閾值
    threshLoc = np.where(variance[0][0:255] == np.max(variance[0][0:255]))
    thresh = threshLoc[0]
    # 閾值處理
    threshold = np.copy(image)
    threshold[threshold > thresh] = 255
    threshold[threshold <= thresh] = 0
    return threshold


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 閾值算法
ostu_threshold = ostu(image)

# 顯示閾值處理的結果
cvshow("ostu_threshold", ostu_threshold)

print("------------------------------------------------------------")  # 60個

print("閾值分割 adaptive")


# 圖像積分
def integral(image):
    rows, cols = image.shape
    # 行積分運算
    inteImageC = np.zeros(image.shape, np.float32)
    for r in range(rows):
        for c in range(cols):
            if c == 0:
                inteImageC[r][c] = image[r][c]
            else:
                inteImageC[r][c] = inteImageC[r][c - 1] + image[r][c]
    # 列積分運算
    inteImage = np.zeros(image.shape, np.float32)
    for c in range(cols):
        for r in range(rows):
            if r == 0:
                inteImage[r][c] = inteImageC[r][c]
            else:
                inteImage[r][c] = inteImage[r - 1][c] + inteImageC[r][c]
    return inteImage


# 閾值處理
def threshAdaptive(image, winSize, ratio):
    # 圖像的寬高
    rows, cols = image.shape
    # 窗口的寬高
    winH, winW = winSize
    h = (winH - 1) // 2
    w = (winW - 1) // 2
    # 閾值處理後的二值化圖像
    threshImage = np.zeros(image.shape, np.uint8)
    # 圖像的積分
    inteImage = integral(image)
    for r in range(rows):
        for c in range(cols):
            # top left
            tl_r = (r - h) if r - h > 0 else 0
            tl_c = (c - w) if c - w > 0 else 0
            # bottom right
            br_r = (r + h) if (r + h) < rows else rows - 1
            br_c = (c + w) if (c + w) < cols else cols - 1
            # 計算區域和
            regionSum = (
                inteImage[br_r][br_c]
                + inteImage[tl_r][tl_c]
                - inteImage[tl_r][br_c]
                - inteImage[br_r][tl_c]
            )
            count = (br_r - tl_r + 1) * (br_c - tl_c + 1)
            if image[r][c] * count < (1 - ratio) * regionSum:
                threshImage[r][c] = 0
            else:
                threshImage[r][c] = 255
    return threshImage


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

threshImage = threshAdaptive(image, (41, 41), 0.15)
# 顯示自適應閾值後二值化圖像
cvshow("threshImage", threshImage)

print("------------------------------------------------------------")  # 60個

print("閾值分割 adaptiveThresh")


def adaptiveThresh(I, winSize, ratio=0.15):
    # 第一步：對圖像矩陣進行均值平滑
    I_smooth = cv2.boxFilter(I, cv2.CV_32FC1, winSize)
    # I_smooth = cv2.medianBlur(I,winSize)
    # 第二步：原圖像矩陣與平滑結果做差
    out = I - (1.0 - ratio) * I_smooth
    # 第三步：對 out 進行全局閾值處理，差值大於等於零，輸出值為255，反之為零
    out[out >= 0] = 255
    out[out < 0] = 0
    out = out.astype(np.uint8)
    return out


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

out = adaptiveThresh(image, (31, 31), 0.15)
cvshow("out", out)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 roberts")

from scipy import signal


def roberts(I, _boundary="fill", _fillvalue=0):
    # 圖像的高、寬
    H1, W1 = I.shape[0:2]
    # 卷積核的尺寸
    H2, W2 = 2, 2
    # 卷積核 1 及 錨點的位置
    R1 = np.array([[1, 0], [0, -1]], np.float32)
    kr1, kc1 = 0, 0
    # 計算 fuLl 卷積
    IconR1 = signal.convolve2d(
        I, R1, mode="full", boundary=_boundary, fillvalue=_fillvalue
    )
    IconR1 = IconR1[H2 - kr1 - 1 : H1 + H2 - kr1 - 1, W2 - kc1 - 1 : W1 + W2 - kc1 - 1]
    # 卷積核2
    R2 = np.array([[0, 1], [-1, 0]], np.float32)
    # 先計算 full 卷積
    IconR2 = signal.convolve2d(
        I, R2, mode="full", boundary=_boundary, fillvalue=_fillvalue
    )
    # 錨點的位置
    kr2, kc2 = 0, 1
    # 根據錨點的位置，截取 full卷積，從而得到 same 卷積
    IconR2 = IconR2[H2 - kr2 - 1 : H1 + H2 - kr2 - 1, W2 - kc2 - 1 : W1 + W2 - kc2 - 1]
    return (IconR1, IconR2)


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 卷積，注意邊界擴充一般采用 " symm "
IconR1, IconR2 = roberts(image, "symm")

# 45度方向上的邊緣強度的灰度級顯示
IconR1 = np.abs(IconR1)
edge_45 = IconR1.astype(np.uint8)
cvshow("edge_45", edge_45)

# 135度方向上的邊緣強度
IconR2 = np.abs(IconR2)
edge_135 = IconR2.astype(np.uint8)
cvshow("edge_135", edge_135)

# 用平方和的開方衡量最後的輸出邊緣
edge = np.sqrt(np.power(IconR1, 2.0) + np.power(IconR2, 2.0))
edge = np.round(edge)
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
# 顯示邊緣
cvshow("edge", edge)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Marr_Hildreth 1")

from scipy import signal


# 構建 LoG 算子
def createLoGKernel(sigma, kSize):
    # LoG 算子的寬高，且兩者均為奇數
    winH, winW = kSize
    logKernel = np.zeros(kSize, np.float32)
    # 方差
    sigmaSquare = pow(sigma, 2.0)
    # LoG 算子的中心
    centerH = (winH - 1) / 2
    centerW = (winW - 1) / 2
    for r in range(winH):
        for c in range(winW):
            norm2 = pow(r - centerH, 2.0) + pow(c - centerW, 2.0)
            logKernel[r][c] = (
                1.0
                / sigmaSquare
                * (norm2 / sigmaSquare - 2)
                * math.exp(-norm2 / (2 * sigmaSquare))
            )
    return logKernel


# 零交叉點：方法1
def zero_cross_default(image_conv_log):
    zero_cross = np.zeros(image_conv_log.shape, np.uint8)
    rows, cols = image_conv_log.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # 左 / 右方向
            if image_conv_log[r][c - 1] * image_conv_log[r][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            # 上 / 下方向
            if image_conv_log[r - 1][c] * image_conv_log[r + 1][c] < 0:
                zero_cross[r][c] = 255
                continue
            # 左上 / 右下方向
            if image_conv_log[r - 1][c - 1] * image_conv_log[r + 1][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            # 右上 / 左下方向
            if image_conv_log[r - 1][c + 1] * image_conv_log[r + 1][c - 1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross


# 零交叉點：方法2
def zero_cross_mean(image_conv_log):
    zero_cross = np.zeros(image_conv_log.shape, np.uint8)
    # 存儲左上，右上，左下，右下方向
    fourMean = np.zeros(4, np.float32)
    rows, cols = image_conv_log.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # 左上方的均值
            leftTopMean = np.mean(image_conv_log[r - 1 : r + 1, c - 1 : c + 1])
            fourMean[0] = leftTopMean
            # 右上方的均值
            rightTopMean = np.mean(image_conv_log[r - 1 : r + 1, c : c + 2])
            fourMean[1] = rightTopMean
            # 左下方的均值
            leftBottomMean = np.mean(image_conv_log[r : r + 2, c - 1 : c + 1])
            fourMean[2] = leftBottomMean
            # 右下方的均值
            rightBottomMean = np.mean(image_conv_log[r : r + 2, c : c + 2])
            fourMean[3] = rightBottomMean
            if np.min(fourMean) * np.max(fourMean) < 0:
                zero_cross[r][c] = 255
    return zero_cross


# Marr_Hildreth 邊緣檢測算法
def Marr_Hildreth(image, loGSize, sigma, crossType="ZERO_CROSS_DEFAULT"):
    # 第一步：創建 LoG 算子
    loGKernel = createLoGKernel(sigma, loGSize)
    # 第二步：圖像與 LoG 算子的卷積
    image_conv_log = signal.convolve2d(image, loGKernel, "same", "symm")
    # 第三步：過零點
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(image_conv_log)
    elif crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(image_conv_log)
    else:
        print("no crossType")
    return zero_cross


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# Marr-Hilreth 邊緣檢測算法
result = Marr_Hildreth(image, (13, 13), 2, "ZERO_CROSS_MEAN")
result = 255 - result
cvshow("Marr-Hildreth", result)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Marr_Hildreth 2")

from scipy import signal


# 非歸一化的高斯卷積
def gaussConv(I, size, sigma):
    # 卷積核的高和寬
    H, W = size
    # 構造水平方向上非歸一化的高斯卷積核
    xr, xc = np.mgrid[0:1, 0:W]
    xc -= (W - 1) // 2
    xk = np.exp(-np.power(xc, 2.0) / (2.0 * pow(sigma, 2)))
    # I 與 xk 卷積
    I_xk = signal.convolve2d(I, xk, "same", "symm")
    # 構造垂直方向上的非歸一化的高斯卷積核
    yr, yc = np.mgrid[0:H, 0:1]
    yr -= (H - 1) // 2
    yk = np.exp(-np.power(yr, 2.0) / (2.0 * pow(sigma, 2.0)))
    # I_xk 與 yk 卷積
    I_xk_yk = signal.convolve2d(I_xk, yk, "same", "symm")
    I_xk_yk *= 1.0 / (2 * np.pi * pow(sigma, 2.0))
    return I_xk_yk


# 高斯差分
def DoG(I, size, sigma, k=1.1):
    # 標準差為 sigma 的非歸一化的高斯卷積
    Is = gaussConv(I, size, sigma)
    # 標準差為 k*sigma 的非歸一化高斯卷積
    Isk = gaussConv(I, size, k * sigma)
    # 兩個高斯卷積的差分
    doG = Isk - Is
    doG /= pow(sigma, 2.0) * (k - 1)
    return doG


# 零交叉點：方法1
def zero_cross_default(doG):
    zero_cross = np.zeros(doG.shape, np.uint8)
    rows, cols = doG.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # 左 / 右方向
            if doG[r][c - 1] * doG[r][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            # 上 / 下方向
            if doG[r - 1][c] * doG[r + 1][c] < 0:
                zero_cross[r][c] = 255
                continue
            # 左上 / 右下方向
            if doG[r - 1][c - 1] * doG[r + 1][c + 1] < 0:
                zero_cross[r][c] = 255
                continue
            # 右上 / 左下方向
            if doG[r - 1][c + 1] * doG[r + 1][c - 1] < 0:
                zero_cross[r][c] = 255
                continue
    return zero_cross


# 零交叉點：方法2
def zero_cross_mean(doG):
    zero_cross = np.zeros(doG.shape, np.uint8)
    # 存儲左上，右上，左下，右下方向
    fourMean = np.zeros(4, np.float32)
    rows, cols = doG.shape
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # 左上方的均值
            leftTopMean = np.mean(doG[r - 1 : r + 1, c - 1 : c + 1])
            fourMean[0] = leftTopMean
            # 右上方的均值
            rightTopMean = np.mean(doG[r - 1 : r + 1, c : c + 2])
            fourMean[1] = rightTopMean
            # 左下方的均值
            leftBottomMean = np.mean(doG[r : r + 2, c - 1 : c + 1])
            fourMean[2] = leftBottomMean
            # 右下方的均值
            rightBottomMean = np.mean(doG[r : r + 2, c : c + 2])
            fourMean[3] = rightBottomMean
            if np.min(fourMean) * np.max(fourMean) < 0:
                zero_cross[r][c] = 255
    return zero_cross


# Marr_Hildreth 邊緣檢測算法
def Marr_Hildreth(image, size, sigma, k=1.1, crossType="ZERO_CROSS_DEFAULT"):
    # 高斯差分
    doG = DoG(image, size, sigma, k)
    # 過零點
    if crossType == "ZERO_CROSS_DEFAULT":
        zero_cross = zero_cross_default(doG)
    elif crossType == "ZERO_CROSS_MEAN":
        zero_cross = zero_cross_mean(doG)
    else:
        print("no crossType")
    return zero_cross


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# Marr-Hilreth 邊緣檢測算法
result = Marr_Hildreth(image, (19, 19), 2, 1.1, "ZERO_CROSS_MEAN")
cvshow("Marr-Hildreth", result)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 prewitt")

from scipy import signal


# prewtt卷積
def prewitt(
    I,
    _boundary="symm",
):
    # 因為prewitt_X是可分離卷積核,根據卷積運算的結合律,可以分兩次小卷積核運算
    # 1：垂直方向的 " 均值平滑 "
    ones_y = np.array([[1], [1], [1]], np.float32)
    i_conv_pre_x = signal.convolve2d(I, ones_y, mode="same", boundary=_boundary)
    # 2：水平方向的差分
    diff_x = np.array([[1, 0, -1]], np.float32)
    i_conv_pre_x = signal.convolve2d(
        i_conv_pre_x, diff_x, mode="same", boundary=_boundary
    )
    # 因為prewitt_y是可分離卷積核，根據卷積運算的結合律，可以分兩次小卷積核運算
    # 1：水平方向的"均值平滑 "
    ones_x = np.array([[1, 1, 1]], np.float32)
    i_conv_pre_y = signal.convolve2d(I, ones_x, mode="same", boundary=_boundary)
    # 2：垂直方向的差分
    diff_y = np.array([[1], [0], [-1]], np.float32)
    i_conv_pre_y = signal.convolve2d(
        i_conv_pre_y, diff_y, mode="same", boundary=_boundary
    )
    return (i_conv_pre_x, i_conv_pre_y)


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"
filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 圖像矩陣 和 兩個 prewitt算子 的卷積
i_conv_pre_x, i_conv_pre_y = prewitt(image)

# 取絕對值,分別得到水平方向和垂直方向的邊緣強度
abs_i_conv_pre_x = np.abs(i_conv_pre_x)
abs_i_conv_pre_y = np.abs(i_conv_pre_y)

# 水平方向和垂直方向的邊緣強度的灰度級顯示
edge_x = abs_i_conv_pre_x.copy()
edge_y = abs_i_conv_pre_y.copy()
edge_x[edge_x > 255] = 255
edge_y[edge_y > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = edge_y.astype(np.uint8)

cvshow("edge_x", edge_x)

cvshow("edge_y", edge_y)

# 利用 abs_i_conv_pre_x 和 abs_i_conv_pre_y 求最終的邊緣強度
# 求邊緣強度，有多重方式，這里使用的是插值法
edge = 0.5 * abs_i_conv_pre_x + 0.5 * abs_i_conv_pre_y
# 邊緣強度的灰度級顯示
edge[edge > 255] = 255
edge = edge.astype(np.uint8)
cvshow("edge", edge)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 sobel")

from scipy import signal

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 得到卷積核
sobelKernel3 = getSobelKernel(3)
sobelKernel5 = getSobelKernel(5)
print(sobelKernel3)
print(sobelKernel5)

# 卷積
image_sobel_x, image_sobel_y = sobel(image, 3)
edge_x = np.abs(image_sobel_x)
edge_x[edge_x > 255] = 255
edge_x = edge_x.astype(np.uint8)
edge_y = np.abs(image_sobel_y)
edge_y[edge_y > 255] = 255
edge_y = edge_y.astype(np.uint8)


# 邊緣強度：兩個卷積結果對應位置的平方和
edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))
# 邊緣強度的灰度級顯示
edge[edge > 255] = 255
edge = np.round(edge)
edge = edge.astype(np.uint8)

cvshow("sobel edge", edge)

# 模擬素描
pencilSketch = edge.copy()
pencilSketch = 255 - pencilSketch
pencilSketch[pencilSketch < 80] = 80
cvshow("pencilSketch", pencilSketch)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 Sobel_normalize")

from scipy import signal

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 卷積
image_sobel_x, image_sobel_y = sobel(image, 7)
# 平方和開方的方式
edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))
# 邊緣強度的灰度級顯示
edge = edge / np.max(edge)
edge = np.power(edge, 0.8)
edge *= 255
edge = edge.astype(np.uint8)
cvshow("sobel edge", edge)

print("------------------------------------------------------------")  # 60個
print("邊緣檢測 canny")

# sobel邊緣檢測


# 邊緣檢測
# 非極大值抑制
def non_maximum_suppression_default(dx, dy):
    # 邊緣強度
    edgeMag = np.sqrt(np.power(dx, 2.0) + np.power(dy, 2.0))
    # 寬、高
    rows, cols = dx.shape
    # 梯度方向
    gradientDirection = np.zeros(dx.shape)
    # 邊緣強度非極大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # angle 的范圍 [0,180] [-180,0]
            angle = math.atan2(dy[r][c], dx[r][c]) / math.pi * 180
            gradientDirection[r][c] = angle
            # 左 / 右方向
            if abs(angle) < 22.5 or abs(angle) > 157.5:
                if (
                    edgeMag[r][c] > edgeMag[r][c - 1]
                    and edgeMag[r][c] > edgeMag[r][c + 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 左上 / 右下方向
            if angle >= 22.5 and angle < 67.5 or (-angle > 112.5 and -angle <= 157.5):
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c - 1]
                    and edgeMag[r][c] > edgeMag[r + 1][c + 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 上 / 下方向
            if (angle >= 67.5 and angle <= 112.5) or (
                angle >= -112.5 and angle <= -67.5
            ):
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c]
                    and edgeMag[r][c] > edgeMag[r + 1][c]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 右上 / 左下方向
            if (angle > 112.5 and angle <= 157.5) or (-angle >= 22.5 and -angle < 67.5):
                if (
                    edgeMag[r][c] > edgeMag[r - 1][c + 1]
                    and edgeMag[r][c] > edgeMag[r + 1][c - 1]
                ):
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup


# 非極大值抑制：插值比較
def non_maximum_suppression_Inter(dx, dy):
    # 邊緣強度
    edgeMag = np.sqrt(np.power(dx, 2.0) + np.power(dy, 2.0))
    # 寬、高
    rows, cols = dx.shape
    # 梯度方向
    gradientDirection = np.zeros(dx.shape)
    # 邊緣強度的非極大值抑制
    edgeMag_nonMaxSup = np.zeros(dx.shape)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if dy[r][c] == 0 and dx[r][c] == 0:
                continue
            # angle的范圍 [0,180],[-180,0]
            angle = math.atan2(dy[r][c], dx[r][c]) / math.pi * 180
            gradientDirection[r][c] = angle
            # 左上方和上方的插值 右下方和下方的插值
            if (angle > 45 and angle <= 90) or (angle > -135 and angle <= -90):
                ratio = dx[r][c] / dy[r][c]
                leftTop_top = (
                    ratio * edgeMag[r - 1][c - 1] + (1 - ratio) * edgeMag[r - 1][c]
                )
                rightBottom_bottom = (1 - ratio) * edgeMag[r + 1][c] + ratio * edgeMag[
                    r + 1
                ][c + 1]
                if edgeMag[r][c] > leftTop_top and edgeMag[r][c] > rightBottom_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 右上方和上方的插值 左下方和下方的插值
            if (angle > 90 and angle <= 135) or (angle > -90 and angle <= -45):
                ratio = abs(dx[r][c] / dy[r][c])
                rightTop_top = (
                    ratio * edgeMag[r - 1][c + 1] + (1 - ratio) * edgeMag[r - 1][c]
                )
                leftBottom_bottom = (
                    ratio * edgeMag[r + 1][c - 1] + (1 - ratio) * edgeMag[r + 1][c]
                )
                if edgeMag[r][c] > rightTop_top and edgeMag[r][c] > leftBottom_bottom:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 左上方和左方的插值 右下方和右方的插值
            if (angle >= 0 and angle <= 45) or (angle > -180 and angle <= -135):
                ratio = dy[r][c] / dx[r][c]
                rightBottom_right = (
                    ratio * edgeMag[r + 1][c + 1] + (1 - ratio) * edgeMag[r][c + 1]
                )
                leftTop_left = (
                    ratio * edgeMag[r - 1][c - 1] + (1 - ratio) * edgeMag[r][c - 1]
                )
                if edgeMag[r][c] > rightBottom_right and edgeMag[r][c] > leftTop_left:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
            # 右上方和右方的插值 左下方和左方的插值
            if (angle > 135 and angle <= 180) or (angle > -45 and angle <= 0):
                ratio = abs(dy[r][c] / dx[r][c])
                rightTop_right = (
                    ratio * edgeMag[r - 1][c + 1] + (1 - ratio) * edgeMag[r][c + 1]
                )
                leftBottom_left = (
                    ratio * edgeMag[r + 1][c - 1] + (1 - ratio) * edgeMag[r][c - 1]
                )
                if edgeMag[r][c] > rightTop_right and edgeMag[r][c] > leftBottom_left:
                    edgeMag_nonMaxSup[r][c] = edgeMag[r][c]
    return edgeMag_nonMaxSup


# 判斷一個點的坐標是否在圖像范圍內
def checkInRange(r, c, rows, cols):
    if r >= 0 and r < rows and c >= 0 and c < cols:
        return True
    else:
        return False


def trace(edgeMag_nonMaxSup, edge, lowerThresh, r, c, rows, cols):
    # 大於閾值為確定邊緣點
    if edge[r][c] == 0:
        edge[r][c] = 255
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (
                    checkInRange(r + i, c + j, rows, cols)
                    and edgeMag_nonMaxSup[r + i][c + j] >= lowerThresh
                ):
                    trace(
                        edgeMag_nonMaxSup, edge, lowerThresh, r + i, c + j, rows, cols
                    )


# 滯後閾值
def hysteresisThreshold(edge_nonMaxSup, lowerThresh, upperThresh):
    # 寬高
    rows, cols = edge_nonMaxSup.shape
    edge = np.zeros(edge_nonMaxSup.shape, np.uint8)
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # 大於高閾值，設置為確定邊緣點，而且以該點為起始點延長邊緣
            if edge_nonMaxSup[r][c] >= upperThresh:
                trace(edgeMag_nonMaxSup, edge, lowerThresh, r, c, rows, cols)
            # 小於低閾值，被剔除
            if edge_nonMaxSup[r][c] < lowerThresh:
                edge[r][c] = 0
    return edge


""" NG
if __name__ == "__main__":
    # 檔案 => cv2影像
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # ------- canny 邊緣檢測 -----------
    # 第一步： 基於 sobel 核的卷積
    image_sobel_x, image_sobel_y = sobel(image, 3)
    # 邊緣強度：兩個卷積結果對應位置的平方和
    edge = np.sqrt(np.power(image_sobel_x, 2.0) + np.power(image_sobel_y, 2.0))
    # 邊緣強度的灰度級顯示
    edge[edge > 255] = 255
    edge = edge.astype(np.uint8)
    cv2.imshow("sobel edge", edge)
    # 第二步：非極大值抑制
    edgeMag_nonMaxSup = non_maximum_suppression_default(image_sobel_x, image_sobel_y)
    edgeMag_nonMaxSup[edgeMag_nonMaxSup > 255] = 255
    edgeMag_nonMaxSup = edgeMag_nonMaxSup.astype(np.uint8)
    cv2.imshow("edgeMag_nonMaxSup", edgeMag_nonMaxSup)
    # 第三步：雙閾值滯後閾值處理，得到 canny 邊緣
    # 滯後閾值的目的就是最後決定處於高閾值和低閾值之間的是否為邊緣點
    edge = hysteresisThreshold(edgeMag_nonMaxSup, 60, 180)
    lowerThresh = 40
    upperThresh = 150
    cv2.imshow("canny", edge)
    # -------以下是為了單閾值與滯後閾值的結果比較 ------
    # 大於高閾值 設置為白色 為確定邊緣
    EDGE = 255
    # 小於低閾值的設置為黑色 表示不是邊緣，被剔除
    NOEDGE = 0
    # 而大於等於低閾值 小於高閾值的設置為灰色，標記為可能的邊緣
    POSSIBLE_EDGE = 128
    tempEdge = np.copy(edgeMag_nonMaxSup)
    rows, cols = tempEdge.shape
    for r in range(rows):
        for c in range(cols):
            if tempEdge[r][c] >= upperThresh:
                tempEdge[r][c] = EDGE
            elif tempEdge[r][c] < lowerThresh:
                tempEdge[r][c] = NOEDGE
            else:
                tempEdge[r][c] = POSSIBLE_EDGE
    cv2.imshow("tempEdge", tempEdge)
    lowEdge = np.copy(edgeMag_nonMaxSup)
    lowEdge[lowEdge > 60] = 255
    lowEdge[lowEdge < 60] = 0
    cv2.imshow("lowEdge", lowEdge)
    upperEdge = np.copy(edgeMag_nonMaxSup)
    upperEdge[upperEdge > 180] = 255
    upperEdge[upperEdge <= 180] = 0
    cv2.imshow("upperEdge", upperEdge)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個

print("邊緣檢測 laplacian")
from scipy import signal

# laplacian 邊緣檢測算法:
# laplacian(image,_boundary='fill',_fillvalue=0)
# 其中：邊緣處理的方式_boundary包括：'symm','wrap','fill',
# 且當__boundary='fill'時，填充值默認為零_fillvalue=0


def laplacian(image, _boundary="fill", _fillvalue=0):
    # 拉普拉斯卷積核
    # laplacianKernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)
    laplacianKernel = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]], np.float32)
    # 圖像矩陣和拉普拉斯算子卷積
    i_conv_lap = signal.convolve2d(
        image, laplacianKernel, mode="same", boundary=_boundary, fillvalue=_fillvalue
    )
    return i_conv_lap


if __name__ == "__main__":
    # 檔案 => cv2影像
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # 顯示原圖
    cvshow("image.jpg", image)

    # ----- 第一種情形 ------
    # 圖像矩陣和拉普拉斯核進行卷積，然後進行閾值處理
    i_conv_lap = laplacian(image, "symm")
    i_conv_lap_copy = np.copy(i_conv_lap)
    # i_conv_lap_copy[i_conv_lap_copy>0] = 255
    # i_conv_lap_copy[i_conv_lap_copy<=0] = 150
    i_conv_lap_copy = np.abs(i_conv_lap_copy)
    i_conv_lap_copy += 125
    i_conv_lap_copy[i_conv_lap_copy > 255] = 255
    i_conv_lap_copy = i_conv_lap_copy.astype(np.uint8)
    cvshow("i_conv_lap", i_conv_lap_copy)
    # 第五種情形

    # ---- 第二種情形 ------
    # 對卷積結果取絕對值
    i_conv_lap_abs = np.abs(i_conv_lap)
    i_conv_lap_abs = np.round(i_conv_lap_abs)
    i_conv_lap_abs[i_conv_lap_abs > 255] = 255
    i_conv_lap_abs = i_conv_lap_abs.astype(np.uint8)
    cvshow("i_conv_lap_abs", i_conv_lap_abs)
    # ---- 第三種情形 -----
    # 先對圖像進行高斯平滑，再進行拉普拉斯卷積，然後閾值處理
    imageBlur = gaussBlur(image, 3, 19, 19, "symm")
    imageBlur_conv_lap = laplacian(imageBlur, "symm")
    threshEdge = np.copy(imageBlur_conv_lap)
    threshEdge = np.abs(threshEdge)
    threshEdge[threshEdge > 255] = 255
    # threshEdge[threshEdge>0] = 255
    # threshEdge[threshEdge<=0] = 0
    threshEdge = threshEdge.astype(np.uint8)
    cvshow("threshEdge", threshEdge)
    # ---- 第四種情形 ----
    # 圖像抽象化
    rows, cols = imageBlur_conv_lap.shape
    imageAbstraction = np.copy(imageBlur_conv_lap)
    for r in range(rows):
        for c in range(cols):
            if imageAbstraction[r][c] > 0:
                imageAbstraction[r][c] = 1
            else:
                imageAbstraction[r][c] = 1 + math.tanh(imageAbstraction[r][c])
    cvshow("imageAbstraction", imageAbstraction)
    # 轉換為 8 位圖，保存結果
    imageAbstraction = 255 * imageAbstraction
    imageAbstraction = np.round(imageAbstraction)
    imageAbstraction = imageAbstraction.astype(np.uint8)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 LoG_edge")
from scipy import signal


# 構建 LoG 算子
def createLoGKernel(sigma, kSize):
    # LoG 算子的寬高，且兩者均為奇數
    winH, winW = kSize
    logKernel = np.zeros(kSize, np.float32)
    # 方差
    sigmaSquare = pow(sigma, 2.0)
    # LoG 算子的中心
    centerH = (winH - 1) / 2
    centerW = (winW - 1) / 2
    for r in range(winH):
        for c in range(winW):
            norm2 = pow(r - centerH, 2.0) + pow(c - centerW, 2.0)
            logKernel[r][c] = (
                1.0
                / sigmaSquare
                * (norm2 / sigmaSquare - 2)
                * math.exp(-norm2 / (2 * sigmaSquare))
            )
    return logKernel


# 高斯拉普拉斯卷積，一般取 _boundary = 'symm'
def LoG(image, sigma, kSize, _boundary="fill", _fillValue=0):
    # 構建 LoG 卷積核
    loGKernel = createLoGKernel(sigma, kSize)
    # 圖像與 LoG 卷積核卷積
    image_conv_log = signal.convolve2d(image, loGKernel, "same", boundary=_boundary)
    return image_conv_log


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 高斯拉普拉斯卷積
image_conv_log = LoG(image, 2, (13, 13), "symm")

# 邊緣的二值化顯示
edge_binary = np.copy(image_conv_log)
edge_binary[edge_binary >= 0] = 0
edge_binary[edge_binary < 0] = 255
edge_binary = edge_binary.astype(np.uint8)
cvshow("edge_binary", edge_binary)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 LoG")
from scipy import signal


def createLoGKernel(sigma, size):
    # LoG 算子的高和寬，且兩者均為奇數
    H, W = size
    r, c = np.mgrid[0:H:1, 0:W:1]
    r -= (H - 1) // 2
    c -= (W - 1) // 2
    # 方差
    sigma2 = pow(sigma, 2.0)
    # LoG 核
    norm2 = np.power(r, 2.0) + np.power(c, 2.0)
    # LoGKernel=1.0/sigma2*(norm2/sigma2 -2)*np.exp(-norm2/(2*sigma2))
    LoGKernel = (norm2 / sigma2 - 2) * np.exp(-norm2 / (2 * sigma2))
    return LoGKernel


def LoG(image, sigma, size, _boundary="symm"):
    # 構建 LoG 卷積核
    loGKernel = createLoGKernel(sigma, size)
    # 圖像與 LoG 卷積核卷積
    image_conv_log = signal.convolve2d(image, loGKernel, "same", boundary=_boundary)
    return image_conv_log


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 高斯拉普拉斯卷積
image_conv_log = LoG(image, 6, (37, 37), "symm")

# 邊緣的二值化顯示
edge_binary = np.copy(image_conv_log)
edge_binary[edge_binary > 0] = 255
edge_binary[edge_binary <= 0] = 0
edge_binary = edge_binary.astype(np.uint8)
cvshow("edge_binary", edge_binary)

print("------------------------------------------------------------")  # 60個

print("邊緣檢測 DoG")
from scipy import signal


# 非歸一化的高斯卷積
def gaussConv(I, size, sigma):
    H, W = size  # 卷積核的高和寬
    # 構造水平方向上非歸一化的高斯卷積核
    xr, xc = np.mgrid[0:1, 0:W]
    xc -= (W - 1) // 2
    xk = np.exp(-np.power(xc, 2.0) / (2.0 * pow(sigma, 2)))
    # I 與 xk 卷積
    I_xk = signal.convolve2d(I, xk, "same", "symm")
    # 構造垂直方向上的非歸一化的高斯卷積核
    yr, yc = np.mgrid[0:H, 0:1]
    yr -= (H - 1) // 2
    yk = np.exp(-np.power(yr, 2.0) / (2.0 * pow(sigma, 2.0)))
    # I_xk 與 yk 卷積
    I_xk_yk = signal.convolve2d(I_xk, yk, "same", "symm")
    I_xk_yk *= 1.0 / (2 * np.pi * pow(sigma, 2.0))
    return I_xk_yk


# 高斯差分
def DoG(I, size, sigma, k=1.1):
    # 標準差為 sigma 的非歸一化的高斯卷積
    Is = gaussConv(I, size, sigma)
    # 標準差為 k*sigma 的非歸一化高斯卷積
    Isk = gaussConv(I, size, k * sigma)
    # 兩個高斯卷積的差分
    doG = Isk - Is
    doG /= pow(sigma, 2.0) * (k - 1)
    return doG


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cvshow("image", image)

# 高斯差分邊緣檢測
sigma = 4
k = 0.9
size = (25, 25)
imageDoG = DoG(image, size, sigma, k)
# 二值化邊緣，對 imageDoG 閾值處理
edge = np.copy(imageDoG)
edge[edge > 0] = 255
edge[edge <= 0] = 0
edge = edge.astype(np.uint8)
cvshow("edge", edge)

# 圖像邊緣抽象化
asbstraction = -np.copy(imageDoG)
asbstraction = asbstraction.astype(np.float32)
asbstraction[asbstraction >= 0] = 1.0
asbstraction[asbstraction < 0] = 1.0 + np.tanh(asbstraction[asbstraction < 0])
cvshow("asbstraction", asbstraction)
asbstraction = asbstraction * 255
asbstraction = asbstraction.astype(np.uint8)

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 HTLine")

from mpl_toolkits.mplot3d import Axes3D


# 霍夫極坐標變換：直線檢測
def HTLine(image, stepTheta=1, stepRho=1):
    # 寬、高
    rows, cols = image.shape
    # 圖像中可能出現的最大垂線的長度
    L = round(math.sqrt(pow(rows - 1, 2.0) + pow(cols - 1, 2.0))) + 1
    # 初始化投票器
    numtheta = int(180.0 / stepTheta)
    numRho = int(2 * L / stepRho + 1)
    accumulator = np.zeros((numRho, numtheta), np.int32)
    # 建立字典
    accuDict = {}
    for k1 in range(numRho):
        for k2 in range(numtheta):
            accuDict[(k1, k2)] = []
    # 投票計數
    for y in range(rows):
        for x in range(cols):
            if image[y][x] == 255:  # 只對邊緣點做霍夫變換
                for m in range(numtheta):
                    # 對每一個角度，計算對應的 rho 值
                    rho = x * math.cos(stepTheta * m / 180.0 * math.pi) + y * math.sin(
                        stepTheta * m / 180.0 * math.pi
                    )
                    # 計算投票哪一個區域
                    n = int(round(rho + L) / stepRho)
                    # 投票加 1
                    accumulator[n, m] += 1
                    # 記錄該點
                    accuDict[(n, m)].append((x, y))
    return accumulator, accuDict


if __name__ == "__main__":
    # 輸入圖像
    # 檔案 => cv2影像
    I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    # canny 邊緣檢測
    edge = cv2.Canny(I, 50, 200)
    # 顯示二值化邊緣
    cvshow("edge", edge)
    # 霍夫直線檢測
    accumulator, accuDict = HTLine(edge, 1, 1)
    # 計數器的二維直方圖方式顯示
    rows, cols = accumulator.shape
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    X, Y = np.mgrid[0:rows:1, 0:cols:1]
    surf = ax.plot_wireframe(X, Y, accumulator, cstride=1, rstride=1, color="gray")
    ax.set_xlabel("$\\rho$")
    ax.set_ylabel("$\\theta$")
    ax.set_zlabel("accumulator")
    ax.set_zlim3d(0, np.max(accumulator))
    # 計數器的灰度級顯示
    grayAccu = accumulator / float(np.max(accumulator))
    grayAccu = 255 * grayAccu
    grayAccu = grayAccu.astype(np.uint8)
    # 只畫出投票數大於 60 直線
    voteThresh = 60
    for r in range(rows):
        for c in range(cols):
            if accumulator[r][c] > voteThresh:
                points = accuDict[(r, c)]
                cv2.line(I, points[0], points[len(points) - 1], (255), 2)
    cvshow("accumulator", grayAccu)

    # 顯示原圖
    cvshow("I", I)
    show()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 HTCircle")

""" 跑不完
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#標準霍夫圓檢測
def HTCircle (I,minR,maxR,voteThresh = 100):
    #寬、高
    H,W = I.shape
    #歸為整數
    minr = round(minR)+1
    maxr = round(maxR)+1
    #初始化三維的計數器
    r_num = int(maxr-minr+1)
    a_num = int(W-1+maxr+maxr+1)
    b_num = int(H-1+maxr+maxr+1)
    accumulator = np.zeros((r_num,b_num,a_num),np.int32)
    #投票計數
    for y in range(H):
        for x  in range(W):
           cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
 if(I[y][x] == 255):#只對邊緣點做霍夫變換
                for k in range(r_num):# r 變化的步長為 1 
                    for theta in np.linspace(0,360,360):
                        #計算對應的 a 和 b
                        a = x - (minr+k)*math.cos(theta/180.0*math.pi)
                        b = y - (minr+k)*math.sin(theta/180.0*math.pi)
                        #取整
                        a = int(round(a))
                        b = int(round(b))
                        #投票
                        accumulator[k,b,a]+=1
    #篩選投票數 大於 voteThresh的圓
    circles = []
    for k in range(r_num):
        for b in range(b_num):
            for a in range(a_num): 
                if(accumulator[k,b,a]>voteThresh):
                    circles.append((k+minr,b,a))
    return circles

# 檔案 => cv2影像
I = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)

#canny 邊緣檢測
edge = cv2.Canny(I,50,200)
cvshow("edge",edge)

#霍夫圓檢測
circles = HTCircle(edge,60,80,80)

#畫圓
for i in range(len(circles)):
    cv2.circle(I,(int(circles[i][2]),int(circles[i][1])),int(circles[i][0]),(255),2)
cvshow("I",I)
"""
print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 contours")

# 輸入圖像
# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(image.shape)

# 邊緣檢測或閾值分割的二值化
binaryImg = cv2.Canny(image, 50, 200)

# 尋找輪廓
contours, h = cv2.findContours(binaryImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 打印 contoures 的類型
print(type(contours))

# contours 是列表類型，打印每一元素的類型
print(type(contours[0]))

# 打印輪廓（點集）個數
print(len(contours))

# 對這些點集，求每一個點集最小
# 最小外包凸包
contoursImg = np.zeros(image.shape, np.uint8)
cv2.drawContours(contoursImg, contours, 7, 255, 3)  # 多點頭尾連線

circle = cv2.minEnclosingCircle(contours[7])
cv2.circle(contoursImg, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), 255, 2)

convexhull = cv2.convexHull(contours[7])
cv2.drawContours(contoursImg, contours, 7, 255, 3)  # 多點頭尾連線

for i in range(len(contours)):
    # ----- 最小外包圓 -------
    circle = cv2.minEnclosingCircle(contours[i])
    # 畫圓
    # cv2.circle(image,(int(circle[0][0]),int(circle[0][1])),int(circle[1]),255,2)
    # ---- 最小直立矩形 ----
    rect = cv2.boundingRect(contours[i])
    # cv2.rectangle(image,(rect[0],rect[1]),(rect[2],rect[3]),255,2)
    # ---- 最小外包的旋轉矩形 -----
    convexhull = cv2.convexHull(contours[i])

# 最小直立矩形
cvshow("image", image)

# 顯示輪廓
cvshow("contoursImg", contoursImg)

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合")

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# 第二步：邊緣檢測 或者 閾值處理 生成一張二值圖
image = cv2.GaussianBlur(image, (3, 3), 0.5)  # 高斯平滑處理    #執行高斯模糊化
binaryImg = cv2.Canny(image, 50, 200)
cvshow("binaryImg", binaryImg)

# 第三步：邊緣的輪廓，返回的 contours 是一個 list 列表
contours, h = cv2.findContours(binaryImg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 輪廓的數量
n = len(contours)
contoursImg = []
# 畫出找到的輪廓
for i in range(n):
    # 創建一個黑色畫布
    temp = np.zeros(binaryImg.shape, np.uint8)
    contoursImg.append(temp)
    # 在第 i 個黑色畫布上，畫第 i 個輪廓
    cv2.drawContours(contoursImg[i], contours, i, 255, 2)  # 多點頭尾連線
    cvshow("contour-" + str(i), contoursImg[i])

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("幾何形狀的檢測和擬合 findContours_OpenCV3")

# filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 第一步：閾值化，生成二值圖
# 圖像平滑
dst = cv2.GaussianBlur(image, (3, 3), 0.5)  # 執行高斯模糊化
# Otsu 閾值分割
OtsuThresh = 0
OtsuThresh, dst = cv2.threshold(dst, OtsuThresh, 255, cv2.THRESH_OTSU)
# --- 形態學開運算（ 消除細小白點 ）
# 創建結構元
s = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dst = cv2.morphologyEx(dst, cv2.MORPH_OPEN, s, iterations=2)

# 第二步：尋找二值圖的輪廓，返回值是一個元組，hc[1] 代表輪廓
hc = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = hc[1]
# 打印輪廓的屬性
print(len(contours))
print(type(contours))
print(contours)

# 第三步：畫出找到的輪廓并用多邊形擬合輪廓
# 輪廓的數量
n = len(hc[1])
print("n =", n)
# 將輪廓畫在該黑板上
print(image.shape)

contoursImg = np.zeros(image.shape, np.uint8)

""" NG
for i in range(n):
    # 畫出輪廓
    cv2.drawContours(contoursImg, contours, i, 255, 2)  #  多點頭尾連線
    # 畫出輪廓的最小外包圓
    circle = cv2.minEnclosingCircle(contours[i])
    cv2.circle(image, (int(circle[0][0]), int(circle[0][1])), int(circle[1]), 0, 5)
    # 多邊形逼近（注意與凸包區別）
    approxCurve = cv2.approxPolyDP(contours[i], 0.3, True)
    # 多邊形頂點個數
    k = approxCurve.shape[0]
    # 頂點連接，繪制多邊形
    for i in range(k - 1):
        cv2.line(
            image,
            (approxCurve[i, 0, 0], approxCurve[i, 0, 1]),
            (approxCurve[i + 1, 0, 0], approxCurve[i + 1, 0, 1]),
            0,
            5,
        )
    # 首尾相接
    cv2.line(
        image,
        (approxCurve[k - 1, 0, 0], approxCurve[k - 1, 0, 1]),
        (approxCurve[0, 0, 0], approxCurve[0, 0, 1]),
        0,
        5,
    )

# 顯示輪廓
cvshow("contours", contoursImg)

# 顯示擬合的多邊形
cvshow("dst", image)
"""
print("------------------------------------------------------------")  # 60個

print("將一彩圖做RGB分離")

filename = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_COLOR)

# 得到三個顏色通道
b = image[:, :, 0]
g = image[:, :, 1]
r = image[:, :, 2]

# 顯示三個顏色通道
cvshow("B", b)
cvshow("G", g)
cvshow("R", r)

# 8位圖轉換為 浮點型
fimage = image / 255.0
fb = fimage[:, :, 0]
fg = fimage[:, :, 1]
fr = fimage[:, :, 2]

# 顯示三個顏色
cvshow("f B", fb)
cvshow("f G", fg)
cvshow("f R", fr)

print("------------------------------------------------------------")  # 60個

img = cv2.resize(cv2.imread("images/soccer_practice.jpg", 0), (0, 0), fx=0.8, fy=0.8)
template = cv2.resize(cv2.imread("images/shoe.PNG", 0), (0, 0), fx=0.8, fy=0.8)
print(img.shape)
print(template.shape)
h, w = template.shape

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED,
]

for method in methods:
    print("matchTemplate, method = ", method)
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cvshow("Match", img2)

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

temp = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print(temp.shape)

tempHt, tempWd = temp.shape
print(tempHt, tempWd)

height, width = temp.shape[:2]

array = temp.reshape(1, -1)

print(array.shape)

EM_sum = np.double(np.sum(array[0]))
print(EM_sum)

square_arr = np.square(array[0])
EM2_sum = np.double(np.sum(square_arr))
print(EM2_sum)


product_array = temp.reshape(1, -1)
_sum = np.double(np.sum(product_array[0]))

print("------------------------------------------------------------")  # 60個

"""
#例外的寫法
img = cv2.imread('digits.png',0)
if img is None:
    raise Exception("we need the digits.png image from samples/data here !")
"""
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image0 = cv2.imread(filename)

image1 = cv2.cvtColor(image0, cv2.COLOR_BGR2GRAY)  # 灰階

_, image2 = cv2.threshold(image1, 120, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白

cvshow("image0", image0)
cvshow("image1", image1)
cvshow("image2", image2)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image0, cv2.COLOR_BGR2RGB))
plt.subplot(132)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.subplot(133)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

show()

print("------------------------------------------------------------")  # 60個

filename = "data/lena.jpg"
img = cv2.imread(filename)
print(type(img), img.shape, img.dtype)

cvshow("demo1", img)

print("------------------------------------------------------------")  # 60個

filename = "data/lena.jpg"
img = cv2.imread(filename)

cvshow("demo1", img)

print("------------------------------------------------------------")  # 60個

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)

print("------------------------------------------------------------")  # 60個

# 圖形型態

from matplotlib import cm
from itertools import product


def func(x, y):
    return (x + y) * np.exp(-5.0 * (x**2 + y**2))


y, x = np.mgrid[-1:1:100j, -1:1:100j]
z = func(x, y)
zabs = np.abs(z)
alpha = cm.ScalarMappable(cmap="gray").to_rgba(zabs)[:, :, 0].copy()
z1 = cm.ScalarMappable(cmap="gray").to_rgba(z)[:, :, 0].copy()
z4 = cm.ScalarMappable(cmap="jet").to_rgba(z)
z3 = z4[:, :, 2::-1].copy()
z4[:, :, -1] = alpha
z4[:, :, :3] = z3

for dtype, img in product(["uint8", "uint16"], [z1, z3, z4]):
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    img = (img * np.iinfo(dtype).max).astype(dtype)
    fn = "tmp_{}_{}.png".format(dtype, nchannel)
    cv2.imwrite(fn, img)

from glob import glob

files = glob("uint*.png")
flags = ["ANYCOLOR", "ANYDEPTH", "COLOR", "GRAYSCALE", "UNCHANGED"]


def f(fn, flag):
    _flag = getattr(cv2, "IMREAD_" + flag)
    img = cv2.imread(fn, _flag)
    nchannel = 1 if img.ndim == 2 else img.shape[2]
    return "{}, {}ch".format(img.dtype, nchannel)


# 圖形輸出

img = cv2.imread("data/lena.jpg")
for quality in [90, 60, 30]:
    cv2.imwrite(
        "tmp_lena_q{:02d}.jpg".format(quality), img, [cv2.IMWRITE_JPEG_QUALITY, quality]
    )

from matplotlib.cm import ScalarMappable


def func(x, y, a):
    return (x * x - y * y) * np.sin((x + y) / a) / (x * x + y * y)


def make_image(x, y, a, dtype="uint8"):
    z = func(x, y, a)
    img_rgba = ScalarMappable(cmap="jet").to_rgba(z)
    img = (img_rgba[:, :, 2::-1] * np.iinfo(dtype).max).astype(dtype)
    return img


y, x = np.ogrid[-10:10:250j, -10:10:500j]
img_8bit = make_image(x, y, 0.5, dtype="uint8")
img_16bit = make_image(x, y, 0.5, dtype="uint16")

cv2.imwrite("tmp_img_8bit.jpg", img_8bit)
cv2.imwrite("tmp_img_16bit.jpg", img_16bit)
cv2.imwrite("tmp_img_8bit.png", img_8bit)
cv2.imwrite("tmp_img_16bit.png", img_16bit)

# 位元組序列與圖形相互轉換

with open("tmp_img_8bit.png", "rb") as f:
    png_str = f.read()

png_data = np.frombuffer(png_str, np.uint8)
img = cv2.imdecode(png_data, cv2.IMREAD_UNCHANGED)
res, jpg_data = cv2.imencode(".jpg", img)
jpg_str = jpg_data.tobytes()

# %fig=使用`Image`將`imencode()`解碼的結果直接內嵌到Notebook中
res, jpg_data = cv2.imencode(".jpg", img_8bit)

from IPython.display import Image

Image(data=jpg_data.tobytes())

# 視訊輸出

def test_avi_output(fn, fourcc):
    # fourcc = cv2.FOURCC(*fourcc)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    vw = cv2.VideoWriter(fn, fourcc, 15, (500, 250), True)
    if not vw.isOpened():
        return
    for a in np.linspace(0.1, 2, 100):
        img = make_image(x, y, a)
        vw.write(img)
    vw.release()

test_avi_output("tmp_fmp4.avi", "fmp4")

from os import path

for quantizer in [1, 10, 20, 30, 40]:
    fn = "tmp_x264_q{:02d}.avi".format(quantizer)
    test_avi_output(fn, "x264")
    fsize = path.getsize(fn)
    print("quantizer = {:02d}, size = {:07d} bytes".format(quantizer, fsize))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 圖形處理
# 二維卷冊積

# %fig=使用filter2D()製作的各種圖形處理效果
src = cv2.imread("data/lena.jpg")

kernels = [
    ("低通濾波器", np.array([[1, 1, 1], [1, 2, 1], [1, 1, 1]]) * 0.1),
    ("高通濾波器", np.array([[0.0, -1, 0], [-1, 5, -1], [0, -1, 0]])),
    ("邊緣檢驗", np.array([[-1.0, -1, -1], [-1, 8, -1], [-1, -1, -1]])),
]

index = 0
fig, axes = plt.subplots(1, 3, figsize=(12, 4.3))
for ax, (name, kernel) in zip(axes, kernels):
    dst = cv2.filter2D(src, -1, kernel)
    # 由於matplotlib的彩色順序和OpenCV的順序相反
    ax.imshow(dst[:, :, ::-1])
    ax.set_title(name)
    ax.axis("off")
fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

img = np.random.rand(1000, 1000)

row = cv2.getGaussianKernel(7, -1)
col = cv2.getGaussianKernel(5, -1)

kernel = np.dot(col[:], row[:].T)

img2 = cv2.filter2D(img, -1, kernel)
img3 = cv2.sepFilter2D(img, -1, row, col)
print("error=", np.max(np.abs(img2[:] - img3[:])))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 形態學運算

#    scpy2.opencv.morphology_demo：示範OpenCV中的各種形態學運算。

# 填充-floodFill

# %fig=示範floodFill()的填充效果
img = cv2.imread("data/coins.png")
seed1 = 344, 188
seed2 = 152, 126
diff = (13, 13, 13)
h, w = img.shape[:2]
mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(img, mask, seed1, (0, 0, 0), diff, diff, cv2.FLOODFILL_MASK_ONLY)
cv2.floodFill(img, None, seed2, (0, 0, 255), diff, diff)

fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].imshow(~mask, cmap="gray")
axes[1].imshow(img)

show()

#    scpy2.opencv.floodfill_demo：示範填充函數floodFill()的各個參數的用法。
# 去瑕疵-inpaint
#    scpy2.opencv.inpaint_demo：示範inpaint()的用法，使用者用滑鼠繪制需要去瑕疵的區域，程式實時顯示運算結果。

print("------------------------------------------------------------")  # 60個

# 圖形變換
# 幾何變換

# %fig=對圖形進行仿射變換
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
src = np.array([[0, 0], [w - 1, 0], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 300], [873, 78], [161, 923]], dtype=np.float32)

m = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()

print("------------------------------")  # 30個

# %fig=對圖形進行透視變換
src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], dtype=np.float32)
dst = np.array([[300, 350], [800, 300], [900, 923], [161, 923]], dtype=np.float32)

m = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, m, (2 * w, 2 * h), borderValue=(255, 255, 255, 255))

fig, ax = plt.subplots(figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1)
ax.set_xlim(-5, w * 2 + 5)
ax.set_ylim(h * 2 + 5, -5)
ax.axis("off")
ax.imshow(result[:, :, ::-1])
ax.imshow(img[:, :, ::-1], alpha=0.4)
p = np.vstack((src, src[:1]))
ax.plot(p[:, 0], p[:, 1], "-o", alpha=0.5)

from matplotlib.patches import FancyArrowPatch

for p1, p2 in zip(src, dst):
    arrow = FancyArrowPatch(
        p1, p2, transform=ax.transData, color="gray", mutation_scale=10
    )
    ax.add_artist(arrow)

show()

print("------------------------------------------------------------")  # 60個

"""
    scpy2.opencv.warp_demo：仿射變換和透視變換的示範程式，
    可以透過滑鼠拖曳圖中藍色三角形和四邊形的頂點，
    進一步決定原始圖形各個頂角經由變換之後的座標。
"""

"""
#重映射-remap

mapy, mapx = np.mgrid[0:h * 3:3, 0:w * 2:2]
img2 = cv2.remap(img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
x, y = 12, 40 #用於驗證映射公式的座標點
assert np.all(img[mapy[y, x], mapx[y, x]] == img2[y, x])

#%fig=使用3D曲面和remap()對圖片進行變形
def make_surf_map(func, r, w, h, d0):
    #計算曲面函數func在[-r:r]範圍之上的值，並進行透視投影。
    #視點高度為曲面高度的d0倍+1
    y, x = np.ogrid[-r:r:h * 1j, -r:r:w * 1j]
    z = func(x, y) + 0 * (x + y)  
    d = d0 * np.ptp(z) + 1.0  
    map1 = x * (d - z) / d  
    map2 = y * (d - z) / d
    return (map1 / (2 * r) + 0.5) * w, (map2 / (2 * r) + 0.5) * h  

def make_func(expr_str):
    def f(x, y):
        return eval(expr_str, np.__dict__, locals())
    return f

def get_latex(expr_str):
    import sympy
    x, y = sympy.symbols("x, y")
    env = {"x": x, "y": y}
    expr = eval(expr_str, sympy.__dict__, env)
    return sympy.latex(expr)

settings = [
    ("sqrt(8 - x**2 - y**2)", 2, 1),
    ("sin(6*sqrt(x**2+y**2))", 10, 10),
    ("sin(sqrt(x**2+y**2))/sqrt(x**2+y**2)", 20, 0.5)
]
fig, axes = plt.subplots(1, len(settings), figsize=(12, 12.0 / len(settings)))

for ax, (expr, r, height) in zip(axes, settings):
    mapx, mapy = make_surf_map(make_func(expr), r, w, h, height)
    img2 = cv2.remap(
        img, mapx.astype("f32"), mapy.astype("f32"), cv2.INTER_LINEAR)
    ax.imshow(img2[:, :, ::-1])
    ax.axis("off")
    ax.set_title("${}$".format(get_latex(expr)))

fig.subplots_adjust(0, 0, 1, 1, 0.02, 0)

show()
"""
print("------------------------------------------------------------")  # 60個
"""
    scpy2.opencv.remap_demo：示範remap()的拖曳效果。
    在圖形上按住滑鼠左鍵進行拖曳，每次拖曳完成之後，都將修改原始圖形，
    可以按滑鼠右鍵取消上次的拖曳動作。
"""

# %fig=使用remap()實現圖形拖曳效果
img = cv2.imread("data/lena.jpg")
h, w = img.shape[:2]
gridy, gridx = np.mgrid[:h, :w]
tx, ty = 313, 316
sx, sy = 340, 332
r = 40.0
sigma = 20

mask = ((gridx - sx) ** 2 + (gridy - sy) ** 2) < r**2
offsetx = np.zeros((h, w))
offsety = np.zeros((h, w))
offsetx[mask] = tx - sx
offsety[mask] = ty - sy
offsetx_blur = cv2.GaussianBlur(offsetx, (0, 0), sigma)
offsety_blur = cv2.GaussianBlur(offsety, (0, 0), sigma)
img2 = cv2.remap(
    img,
    (offsetx_blur + gridx).astype("f4"),
    (offsety_blur + gridy).astype("f4"),
    cv2.INTER_LINEAR,
)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax.imshow(img2[:, :, ::-1])
circle = plt.Circle((tx, ty), r, fill=None, alpha=0.5, lw=2, ls="dashed")
ax.add_artist(circle)
circle = plt.Circle((sx, sy), r, fill=None, alpha=0.5, lw=2, color="black")
ax.add_artist(circle)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個

# 直方圖

# %fig=`data/lena.jpg`的三個通道的直方圖統計、通道0和通道2的二維直方圖統計
img = cv2.imread("data/lena.jpg")
fig, ax = plt.subplots(1, 2, figsize=(12, 5))
colors = ["blue", "green", "red"]

for i in range(3):
    hist, x = np.histogram(img[:, :, i].ravel(), bins=256, range=(0, 256))
    ax[0].plot(0.5 * (x[:-1] + x[1:]), hist, label=colors[i], color=colors[i])

ax[0].legend(loc="upper left")
ax[0].set_xlim(0, 256)
hist2, x2, y2 = np.histogram2d(
    img[:, :, 0].ravel(),
    img[:, :, 2].ravel(),
    bins=(100, 100),
    range=[(0, 256), (0, 256)],
)
ax[1].imshow(hist2, extent=(0, 256, 0, 256), origin="lower", cmap="gray")
ax[1].set_ylabel("blue")
ax[1].set_xlabel("red")

show()

print("------------------------------")  # 30個

result = cv2.calcHist(
    [img],
    channels=(0, 1, 2),
    mask=None,
    histSize=(30, 20, 10),
    ranges=(0, 256, 0, 256, 0, 256),
)
cc = result.shape
print(cc)

# (30, 20, 10)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直方圖反向映射

# %fig=使用calcBackProject()尋找圖形中橙子部分
img = cv2.imread("data/fruits_section.jpg")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

result = cv2.calcHist([img_hsv], [0, 1], None, [40, 40], [0, 256, 0, 256])

result /= np.max(result) / 255

img2 = cv2.imread("data/fruits.jpg")
img_hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

img_bp = cv2.calcBackProject(
    [img_hsv2], channels=[0, 1], hist=result, ranges=[0, 256, 0, 256], scale=1
)
_, img_th = cv2.threshold(img_bp, 180, 255, cv2.THRESH_BINARY)
struct = np.ones((3, 3), np.uint8)
img_mp = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, struct, iterations=5)

fig, axes = plt.subplots(2, 3, figsize=(9, 6))
fig.subplots_adjust(0, 0, 1, 1, 0.01, 0.01)
axes[0, 0].imshow(img[:, :, ::-1])
axes[0, 1].imshow(img2[:, :, ::-1])
axes[0, 2].imshow(result[:], cmap="gray")
axes[1, 0].imshow(img_bp[:], cmap="gray")
axes[1, 1].imshow(img_th[:], cmap="gray")
axes[1, 2].imshow(img_mp[:], cmap="gray")

for axe in axes.flat:
    axe.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 直方圖比對


def histogram_match(src, dst):
    res = np.zeros_like(dst)
    cdf_src = np.zeros((3, 256))
    cdf_dst = np.zeros((3, 256))
    cdf_res = np.zeros((3, 256))
    kw = dict(bins=256, range=(0, 256), normed=True)

    for ch in (0, 1, 2):
        hist_src, _ = np.histogram(src[:, :, ch], **kw)
        hist_dst, _ = np.histogram(dst[:, :, ch], **kw)
        cdf_src[ch] = np.cumsum(hist_src)
        cdf_dst[ch] = np.cumsum(hist_dst)
        index = np.searchsorted(cdf_src[ch], cdf_dst[ch], side="left")
        np.clip(index, 0, 255, out=index)
        res[:, :, ch] = index[dst[:, :, ch]]
        hist_res, _ = np.histogram(res[:, :, ch], **kw)
        cdf_res[ch] = np.cumsum(hist_res)

    return res, (cdf_src, cdf_dst, cdf_res)


src = cv2.imread("data/autumn.jpg")
dst = cv2.imread("data/summer.jpg")

res, cdfs = histogram_match(src, dst)

# %figonly=直方圖比對結果
fig = plt.figure(figsize=(10, 6))
fig.subplots_adjust(0, 0, 1, 1, 0, 0)
ax1 = plt.subplot2grid((5, 6), (0, 0), 3, 3)
ax2 = plt.subplot2grid((5, 6), (0, 3), 3, 3)
ax1.imshow(dst[:, :, ::-1])
ax2.imshow(res[:, :, ::-1])
ax1.axis("off")
ax2.axis("off")
axb = plt.subplot2grid((5, 6), (3, 0), 2, 2)
axg = plt.subplot2grid((5, 6), (3, 2), 2, 2)
axr = plt.subplot2grid((5, 6), (3, 4), 2, 2)

axg.set_yticklabels([])
axr.set_yticklabels([])

for ax, cdf in zip((axb, axg, axr), zip(*cdfs)):
    ax.plot(cdf[0], alpha=0.6, label="src", ls="--")
    ax.plot(cdf[1], alpha=0.6, label="dst", ls=":")
    ax.plot(cdf[2], alpha=0.6, label="res")
    ax.set_xlim(0, 256)
    ax.set_ylim(0, 1.1)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 用二元視覺圖形計算深度訊息

img_left = cv2.pyrDown(cv2.imread("data/aloeL.jpg"))
img_right = cv2.pyrDown(cv2.imread("data/aloeR.jpg"))

img_left = cv2.cvtColor(img_left, cv2.COLOR_BGR2RGB)
img_right = cv2.cvtColor(img_right, cv2.COLOR_BGR2RGB)

stereo_parameters = dict(
    SADWindowSize=5,
    numDisparities=192,
    preFilterCap=4,
    minDisparity=-24,
    uniquenessRatio=1,
    speckleWindowSize=150,
    speckleRange=2,
    disp12MaxDiff=10,
    fullDP=False,
    P1=600,
    P2=2400,
)

stereo = cv2.StereoSGBM(**stereo_parameters)
# NG disparity = stereo.compute(img_left, img_right).astype(np.float32) / 16

# %fig=用remap重疊左右兩幅圖形
h, w = img_left.shape[:2]
ygrid, xgrid = np.mgrid[:h, :w]
ygrid = ygrid.astype(np.float32)
xgrid = xgrid.astype(np.float32)
# NG res = cv2.remap(img_right, xgrid - disparity, ygrid, cv2.INTER_LINEAR)

fig, axes = plt.subplots(1, 3, figsize=(9, 3))
axes[0].imshow(img_left)
axes[0].imshow(img_right, alpha=0.5)
# axes[1].imshow(disparity, cmap="gray")
axes[2].imshow(img_left)
# axes[2].imshow(res, alpha=0.5)
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 圖形識別
# 用Hough變換檢驗直線和圓

# scpy2.opencv.hough_demo：霍夫變換示範程式，可透過界面調節函數的所有參數。

# 檢驗線段

# %figonly=用r和θ表示的直線

x = [-2, 5]
y = [5, -1]

from sympy import Point
from sympy import Line

line = Line(Point(x[0], y[0]), Point(x[1], y[1]))
seg = line.perpendicular_segment(Point(0, 0))

plt.plot([seg.p1.x, seg.p2.x], [seg.p1.y, seg.p2.y], "--o", color="gray")

from matplotlib.patches import Wedge

angle = np.rad2deg(np.arctan2(float(seg.p2.y), float(seg.p2.x)))
theta = Wedge((0, 0), 1, 0, angle, alpha=0.3)
# plt.add_patch(theta)
plt.text(1, 0.5, r"$\theta$", fontsize="large")
plt.text(0.8, 1.1, r"$r$", fontsize="large")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# %figonly=霍夫變換示意圖
k = 1.2
b = 3

xn, yn = 4, 3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3))
xs = np.linspace(0, 5, 4)
ys = xs * k + b

for x0, y0 in zip(xs, ys):
    ax1.plot(x0, y0, "o")

ax1.plot(xn, yn, ">")
ax1.margins(0.1, 0.1)

theta = np.linspace(0, np.pi, 100)
for x0, y0 in zip(xs, ys):
    r = x0 * np.cos(theta) + y0 * np.sin(theta)
    ax2.plot(theta, r)

r = xn * np.cos(theta) + yn * np.sin(theta)
ax2.plot(theta, r, "--")
ax2.set_xlim(0, np.max(theta))

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


# add_collection 只能用 ax

# %fig=使用HoughLinesP()檢驗圖形中的直線
img = cv2.imread("data/building.jpg", cv2.IMREAD_GRAYSCALE)
img_binary = cv2.Canny(img, 100, 255)
lines = cv2.HoughLinesP(
    img_binary,
    rho=1,
    theta=np.deg2rad(0.1),
    threshold=96,
    minLineLength=33,
    maxLineGap=4,
)

fig, ax = plt.subplots(figsize=(8, 6))
plt.imshow(img, cmap="gray")

from matplotlib.collections import LineCollection

lc = LineCollection(lines.reshape(-1, 2, 2))
ax.add_collection(lc)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檢驗圓形

# %fig=使用HoughCircles()檢驗圖形中的圓形
img = cv2.imread("data/coins.png", cv2.IMREAD_GRAYSCALE)
img_blur = cv2.GaussianBlur(img, (0, 0), 1.8)
circles = cv2.HoughCircles(
    img_blur,
    cv2.HOUGH_GRADIENT,
    dp=2.0,
    minDist=20.0,
    param1=170,
    param2=44,
    minRadius=16,
    maxRadius=40,
)

x, y, r = circles[0].T

fig, ax = plt.subplots(figsize=(8, 6))
plt.imshow(img, cmap="gray")

from matplotlib.collections import EllipseCollection

ec = EllipseCollection(
    widths=2 * r,
    heights=2 * r,
    angles=0,
    units="xy",
    facecolors="none",
    edgecolors="red",
    transOffset=ax.transData,
    offsets=np.c_[x, y],
)
ax.add_collection(ec)
ax.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 圖形分割
# Mean-Shift法

# %fig=使用pyrMeanShiftFiltering()進行圖形分割，從左到右參數sr分別為20, 40, 80
fig, axes = plt.subplots(1, 3, figsize=(9, 3))

img = cv2.imread("data/fruits.jpg")

srs = [20, 40, 80]
for ax, sr in zip(axes, srs):
    img2 = cv2.pyrMeanShiftFiltering(img, sp=20, sr=sr, maxLevel=1)
    ax.imshow(img2[:, :, ::-1])
    ax.set_axis_off()
    ax.set_title("sr = {}".format(sr))

fig.subplots_adjust(0.02, 0, 0.98, 1, 0.02, 0)

show()

print("------------------------------------------------------------")  # 60個

# 分水嶺算法

img = cv2.imread("data/pills.png")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray = cv2.blur(img_gray, (15, 15))
_, img_binary = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY)
peaks = img_gray == cv2.dilate(img_gray, np.ones((7, 7)), 1)

# NG peaks &= img_binary
peaks[1, 1] = True

from scipy.ndimage import label

markers, count = label(peaks)
cv2.watershed(img, markers)

"""
scpy2.opencv.watershed_demo：分水嶺算法的示範程式。
用滑鼠在圖形上繪制起始區域，起始區域將使用“目前標簽”填充，
按滑鼠右鍵切換到下一個標簽。每次繪制起始區域之後，將顯示分割的結果。
"""
print("------------------------------")  # 30個

# %figonly=使用watershed分割藥丸
fig, axes = plt.subplots(1, 2, figsize=(10, 3))
axes[0].imshow(img[:, :, ::-1])
peaks_img = np.zeros(img.shape[:2] + (4,), np.uint8)
peaks_img[peaks, 2] = 255
peaks_img[peaks, -1] = 255
axes[0].imshow(peaks_img)

colors = np.random.randint(64, 200, (count + 2, 3)).astype(np.uint8)
colors[markers[1, 1]] = 255, 255, 255
colors[-1] = 0
axes[1].imshow(colors[markers])
for ax in axes:
    ax.axis("off")
fig.subplots_adjust(0, 0, 1, 1, 0, 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
# 無 SURF() 函數
#SURF特征比對

#%fig=SURF()找到的關鍵點和每個關鍵點的局部圖形
img_gray1 = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE) #❶
surf = cv2.SURF(2000, 2)  #❷
key_points1 = surf.detect(img_gray1) #❸
key_points1.sort(key=lambda kp:kp.size, reverse=True) #❹

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
cv2.drawKeypoints(img_color1, key_points1[:25], img_color1, color=(255, 0, 0),  #❺
                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

from scpy2.utils.image import concat_keypoints

img_keypoints = concat_keypoints(img_gray1, key_points1[:25], 5, 5, scale=2)
#%array_image img_color1; img_keypoints

print("------------------------------")  # 30個

_, features1 = surf.compute(img_gray1, key_points1)
cc = features1.shape
print(cc)

#(145, 128)

img_gray2 = cv2.imread("dat/lena2.jpg", cv2.IMREAD_GRAYSCALE)
img_color2 = cv2.cvtColor(img_gray2, cv2.COLOR_GRAY2RGB)
surf2 = cv2.SURF(2000, 2)  
key_points2, features2 = surf2.detectAndCompute(img_gray2, None)

FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=100)   

fbm = cv2.FlannBasedMatcher(index_params, search_params) #❶
match_list = fbm.knnMatch(features1, features2, k=1) #❷

m = match_list[0][0]

#%C m.distance; m.queryIdx; m.trainIdx

#請讀者思考如何利用下面程式得到的matrix矩陣將變形之後的圖形復原成原始圖形。

key_positions1 = np.array([kp.pt for kp in key_points1])
key_positions2 = np.array([kp.pt for kp in key_points2])

index1 = np.array([m[0].queryIdx for m in match_list])
index2 = np.array([m[0].trainIdx for m in match_list])

distances = np.array([m[0].distance for m in match_list])

best_index = np.argsort(distances)[:50] #❶
matched_positions1 = key_positions1[index1[best_index]]
matched_positions2 = key_positions2[index2[best_index]]

matrix, mask = cv2.findHomography(matched_positions1, matched_positions2, cv2.RANSAC) #❷

#scpy2.opencv.surf_demo：SURF圖形比對示範程式。
#用滑鼠修改右側圖形的四個角的位置計算出透視變換之後的圖形，
#然後在原始圖形和變換之後的圖形之間搜尋比對點，並計算透視變換的矩陣。
"""

""" no module
#%figonly=顯示特征比對的關鍵點

from matplotlib.collections import LineCollection
from scpy2.utils.image import concat_images

COLORS = np.array([[0, 0.0, 0.5], [1, 0, 0]])

img_color1 = cv2.cvtColor(img_gray1, cv2.COLOR_GRAY2RGB)
merged_img = concat_images([img_color1, img_color2], margin=0)

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis("off")
plt.imshow(merged_img)
lines = np.concatenate([matched_positions1, matched_positions2], axis=1)
lines[:, 2] += img_color2.shape[1]
line_collection = LineCollection(lines.reshape(-1, 2, 2), 
                                 colors=COLORS[mask.ravel()], lw=1, alpha=0.5)
ax.add_collection(line_collection);

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 形狀與結構分析
# 輪廓檢驗

img_coin = cv2.imread("data/coins.png", cv2.IMREAD_COLOR)
img_coin_gray = cv2.cvtColor(img_coin, cv2.COLOR_BGR2GRAY)
img_coin_blur = cv2.GaussianBlur(img_coin_gray, (0, 0), 1.5, 1.5)
img_coin_binary = cv2.Canny(img_coin_blur.copy(), 60, 60)
img_coin_binary = cv2.morphologyEx(
    img_coin_binary, cv2.MORPH_CLOSE, np.ones((3, 3), "uint8")
)

for approx in ["NONE", "SIMPLE", "TC89_KCOS", "TC89_L1"]:
    approx_flag = getattr(cv2, "CHAIN_APPROX_{}".format(approx))
    coin_contours, hierarchy = cv2.findContours(
        img_coin_binary.copy(), cv2.RETR_EXTERNAL, approx_flag
    )
    print("{}: {}  ".format(approx, sum(contour.shape[0] for contour in coin_contours)))

# NONE: 3179   SIMPLE: 1579   TC89_KCOS: 849   TC89_L1: 802


# %fig=顯示所有圓度在0.8到1.2之間的輪廓
def circularity(contour):
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour) + 1e-6
    return perimeter * perimeter / (4 * np.pi * area)


coin_contours = [
    contour for contour in coin_contours if 0.8 < circularity(contour) < 1.2
]
cv2.drawContours(img_coin, coin_contours, -1, (255, 0, 0))

cvshow("demo1", img_coin)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

img_pattern = cv2.imread("data/nested_patterns.png")
img_pattern_gray = cv2.cvtColor(img_pattern, cv2.COLOR_BGR2GRAY)
_, img_pattern_binary = cv2.threshold(img_pattern_gray, 100, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    img_pattern_binary.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1
)
hierarchy.shape = -1, 4

root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]
print(root_index)

# [0, 7, 19]


def get_children(hierarchy, index):
    first_child = hierarchy.item(index, 2)
    if first_child >= 0:
        yield first_child
        brother = hierarchy.item(first_child, 0)
        while brother >= 0:
            yield brother
            brother = hierarchy.item(brother, 0)


def get_descendant(hierarchy, index, level=1):
    for child in get_children(hierarchy, index):
        yield level, child
        for item in get_descendant(hierarchy, child, level + 1):
            yield item


print(list(get_descendant(hierarchy, 0)))

# [(1, 1), (2, 2), (3, 3), (2, 4), (3, 5), (3, 6)]

# %figonly=顯示輪廓的階層結構
root_index = [i for i in range(len(hierarchy)) if hierarchy[i, 3] < 0]

lines = []
levels = []

for index in root_index:
    items = zip(*get_descendant(hierarchy, index))
    if items:
        children_level, children_index = items
        lines.extend([contours[i] for i in children_index])
        levels.extend(children_level)
    lines.append(contours[index])
    levels.append(0)

lines = [line[:, 0, :] for line in lines]

from matplotlib.collections import LineCollection
from matplotlib.collections import PolyCollection

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect("equal")
polys = PolyCollection(lines, array=np.array(levels), facecolors="none")
ax.add_collection(polys)
ax.set_xlim(0, img_pattern.shape[1])
ax.set_ylim(img_pattern.shape[0], 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 輪廓比對

img_patterns = cv2.imread("data/patterns.png", cv2.IMREAD_GRAYSCALE)
patterns, _ = cv2.findContours(img_patterns, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
img_targets = cv2.imread("data/targets.png", cv2.IMREAD_GRAYSCALE)
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

"""
CV_CONTOURS_MATCH_I1  11.3737,   0.3456,   0.0289,   1.0495,   0.0020
CV_CONTOURS_MATCH_I2   4.8051,   2.2220,   0.0179,   0.3624,   0.0013
CV_CONTOURS_MATCH_I3   0.9164,   0.4778,   0.0225,   0.4552,   0.0016
"""

# %figonly=使用`matchShapes()`比較由`approxPolyDP()`近似之後的輪廓
fig, ax = plt.subplots(figsize=(8, 8))
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
            target_poly = plt.Polygon(target2 + [0, y0], color="green", alpha=0.6)
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

# 型態轉換

points = np.random.rand(20, 2).astype(np.float32)
(x, y), (w, h), angle = cv2.minAreaRect(points)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# [OpenCV][Python]印出圖像中文字的位置及高寬
# 本文將說明如何去辨識出圖片文字​位置及高寬。


def read_posion(img):
    # 輸入背景黑色，物件白色的圖
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
    components = []
    # boxes_data = []
    for i in range(1, num_labels):  # 跳過背景
        x, y, w, h, _ = stats[i]
        components.append((x, y, w, h))

    components.sort(key=lambda c: c[0])  # 按 x 座標排序

    # 合併 x 軸在正負5範圍內的OCR
    merged_components = []
    current_component = list(components[0])

    for i in range(1, len(components)):
        if abs(components[i][0] - current_component[0]) <= 5:
            current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
            current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
            current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
            current_component[3] = (
                abs(components[i][1] - current_component[1]) + components[i][3]
            )  # h 取 Y2 - Y1 + H2
        else:
            merged_components.append(tuple(current_component[:4]))
            current_component = list(components[i][:4])

    # 合併最後一個OCR結果
    merged_components.append(tuple(current_component[:4]))

    return merged_components


filename = "data/captcha.png"

img = cv2.imread(filename)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
box = read_posion(gray_img)

for i, data in enumerate(box):
    x, y, h, w = data
    # 印出OCR 位置，高寬
    print(f"第{i}個OCR，x:{x},y:{y},h:{h},w:{w}")


"""
函式詳細說明
函式定義和參數:
read_posion(img) 函式接受一個參數
img：輸入的二值化圖像，背景是黑色，物件是白色。
計算連通域:
num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(img, connectivity=8)
使用 OpenCV 的 connectedComponentsWithStats 函數計算連通域
num_labels：連通域的數量。
labels：標籤圖，每個連通域有一個唯一的標籤。
stats：每個連通域的統計資料（x, y, w, h, area）。
_:忽略的中心點資料。
提取連通域並存入列表:
components = []
for i in range(1, num_labels):  # 跳過背景
    x, y, w, h, _ = stats[i]
    components.append((x, y, w, h))
遍歷 stats，跳過背景，提取每個連通域的位置信息和尺寸，存入 components 列表。
按 x 座標排序:
components.sort(key=lambda c: c[0])
將 components 按 x 座標進行排序。
合併相鄰的連通域:
merged_components = []
current_component = list(components[0])

for i in range(1, len(components)):
    if abs(components[i][0] - current_component[0]) <= 5:
        current_component[0] = min(current_component[0], components[i][0])  # X 取最小值
        current_component[1] = min(current_component[1], components[i][1])  # Y 取最小值
        current_component[2] = max(current_component[2], components[i][2])  # w 取最大值
        current_component[3] = abs(components[i][1] - current_component[1]) + components[i][3]  # h 取 Y2 - Y1 + H2
    else:
        merged_components.append(tuple(current_component[:4]))
        current_component = list(components[i][:4])

merged_components.append(tuple(current_component[:4]))
初始化 merged_components 列表和 current_component。
遍歷 components 列表，如果當前組件與前一組件的 x 座標差值在正負5範圍內，則合併它們。
合併後的結果存入 merged_components。
返回合併後的元件資訊:
return merged_components
返回合併後的元件資訊，這些資訊包括每個連通域的 x, y, w, h（左上角座標和寬高）。
"""
print("------------------------------------------------------------")  # 60個

# [Python]使用NumPy 進行影像黑白反轉

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 讀取影像（灰階模式）
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 黑白反轉
inverted_image = 255 - image

# 顯示原影像和反轉後的影像
cv2.imshow("Original Image", image)
cv2.imshow("Inverted Image", inverted_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
cv_img = cv2.imread(filename)
width = cv_img.shape[1]
height = cv_img.shape[0]
print(width)
print(height)

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

img = Image.open(filename)

mask = np.zeros([10, 5, 3], dtype=np.uint8)
# print(mask)
occlusion = np.logical_not(mask[:, :, -1]).astype(np.uint8)

# print(mask)

# mask[:, :, i] = mask[:, :, i] * occlusion
# occlusion = np.logical_and(occlusion, np.logical_not(mask[:, :, i]))

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

# 新進 與 測試

"""
    image = cv2.flip(image, 1)                        # 翻轉影像，使其如同鏡子
    image = image[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形
"""

print("------------------------------------------------------------")  # 60個

cvshow("src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()
