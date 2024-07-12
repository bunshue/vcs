"""
opencv 集合 新進


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
'''

"""
print('練習組合成一張大圖 picasa效果')

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

image1 = cv2.resize(image1, (image1.shape[1]//ratio, image1.shape[0]//ratio))
image2 = cv2.resize(image2, (image2.shape[1]//ratio, image2.shape[0]//ratio))
image3 = cv2.resize(image3, (image3.shape[1]//ratio, image3.shape[0]//ratio))
print(image1.shape)

output = np.zeros((768, 1024, 3), dtype='uint8')         # 設定合成的影像為一張全黑的畫布

x_st = 50
y_st = 50
w, h = image1.shape[1], image1.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image1[0:h, 0:w]      # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 300
y_st = 200
w, h = image2.shape[1], image2.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image2[0:h, 0:w]      # 設定 output 的某個區域為即時影像 image 的某區域

x_st = 150
y_st = 300
w, h = image3.shape[1], image3.shape[0]
output[y_st:y_st+h, x_st:x_st+w] = image3[0:h, 0:w]      # 設定 output 的某個區域為即時影像 image 的某區域

plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_4.python/_data/picture_add1.bmp"
filename2 = "C:/_git/vcs/_4.python/_data/picture_add2.bmp"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

print("兩圖直接相加")
result1 = image1 + image2

print("兩圖用cv相加")
result2 = cv2.add(image1, image2)

print("兩圖做比例疊加 左1.0 右1.0")
result3 = cv2.addWeighted(image1, 1.0, image2, 1.0, 0) # 0 為墊高值

plt.figure(
    num="相加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("兩圖直接相加")
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("兩圖用cv相加")
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("兩圖做比例疊加 左1.0 右1.0")
plt.imshow(cv2.cvtColor(result3, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray2.bmp"

# 檔案 => cv2影像
lena = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/dollar.bmp"

# 檔案 => cv2影像
dollar = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="疊加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.title("原圖1")
plt.imshow(cv2.cvtColor(lena, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("原圖2")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

print("兩圖擷取某塊做alpha疊加, 再貼回原圖, 並顯示之")
face1 = lena[220:400, 250:350]
face2 = dollar[160:340, 200:300]
add = cv2.addWeighted(face1, 0.6, face2, 0.4, 0)
dollar[160:340, 200:300] = add

plt.subplot(133)
plt.title("兩圖擷取某塊做alpha疊加, 再貼回原圖")
plt.imshow(cv2.cvtColor(dollar, cv2.COLOR_BGR2RGB))

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

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
plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

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

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

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

plt.suptitle('影像移動')
plt.show()

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
plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/demo.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename)

H, W, D = image.shape

pts1 = np.float32([[150, 50], [400, 50], [60, 450], [310, 450]])
pts2 = np.float32([[50, 50], [H - 50, 50], [50, W - 50], [H - 50, W - 50]])
M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(image, M, (W, H))

plt.figure(
    num="new11",
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
plt.title("result")
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))

plt.show()

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


# 上面就是椒盐噪声函数，下面是使用方法，大家可以愉快的玩耍了
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

plt.show()

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
plt.title("art")
plt.imshow(cv2.cvtColor(art, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個
"""
print("去除圖片的雜訊")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image2 = cv2.imread(filename)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖")

image2_denoised = cv2.fastNlMeansDenoisingColored(image2, h=5)

plt.subplot(122)
plt.imshow(cv2.cvtColor(image2_denoised, cv2.COLOR_BGR2RGB))
plt.title("去除圖片的雜訊")

plt.show()

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

plt.show()

print("------------------------------------------------------------")  # 60個

print("createCLAHE_image 生成自適應均衡化圖像")

# 檔案 => cv2影像
image = cv2.imread("data/building.png", 0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(image)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

plt.imshow(cv2.cvtColor(cl1, cv2.COLOR_BGR2RGB))
plt.show()

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
plt.imshow(original_image_lena)

plt.subplot(132)
plt.title("邊緣檢測")
plt.imshow(edge_image_lena)

plt.subplot(133)
plt.title("梯度處理")
plt.imshow(sharpen_image_lena)

plt.show()

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
plt.imshow(original_image_test1)

fig.add_subplot(132)
plt.title("邊緣檢測")
plt.imshow(my_show_edge(result))

fig.add_subplot(133)
plt.title("銳化處理")
plt.imshow(my_laplace_result_add(original_image_test1, result))

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_cv2")

from matplotlib import pyplot as plt


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

plt.show()

print("------------------------------------------------------------")  # 60個

print("image_fft")

Fs = 1200
# 采樣頻率
Ts = 1 / Fs
# 采樣區間
x = np.arange(0, 1, Ts)  # 時間向量，1200個
y = 5 * np.sin(2 * np.pi * 600 * x)
N = 1200
frq = np.arange(N)  # 頻率數1200個數
half_x = frq[range(int(N / 2))]  # 取一半區間
fft_y = np.fft.fft(y)
abs_y = np.abs(fft_y)  # 取復數的絕對值，即復數的模(雙邊頻譜)
angle_y = 180 * np.angle(fft_y) / np.pi  # 取復數的弧度,并換算成角度
gui_y = abs_y / N  # 歸一化處理（雙邊頻譜）
gui_half_y = gui_y[range(int(N / 2))]  # 由于對稱性，只取一半區間（單邊頻譜）

# 繪製結果
fig = plt.figure(
    num="image_fft",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 畫出原始波形的前50個點
plt.subplot(231)
plt.plot(frq[0:50], y[0:50])
plt.title("原始波形")
# 畫出雙邊未求絕對值的振幅譜
plt.subplot(232)
plt.plot(frq, fft_y, "black")
plt.title("雙邊振幅譜(未求振幅絕對值)")
# 畫出雙邊求絕對值的振幅譜
plt.subplot(233)
plt.plot(frq, abs_y, "r")
plt.title("雙邊振幅譜(未歸一化)")
# 畫出雙邊相位譜
plt.subplot(234)
plt.plot(frq[0:50], angle_y[0:50], "violet")
plt.title("雙邊相位譜(未歸一化)")
# 畫出雙邊振幅譜(歸一化)
plt.subplot(235)
plt.plot(frq, gui_y, "g")
plt.title("雙邊振幅譜(歸一化)")

# 畫出單邊振幅譜(歸一化)
plt.subplot(236)
plt.plot(half_x, gui_half_y, "blue")
plt.title("單邊振幅譜(歸一化)")
plt.show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

# 檔案 => cv2影像
image = plt.imread("data/castle3.jpg")

# 根據公式轉成灰度圖
image = 0.2126 * image[:, :, 0] + 0.7152 * image[:, :, 1] + 0.0722 * image[:, :, 2]

# 繪製結果
fig = plt.figure(
    num="image_fft2",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

# 顯示原圖
plt.subplot(231)
plt.imshow(image, "gray")
plt.title("原始圖像")
# 進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)

plt.subplot(232)
plt.imshow(np.abs(fft2), "gray")
plt.title("二維傅里葉變換")
# 將圖像變換的原點移動到頻域矩形的中心，并顯示效果
shift2center = np.fft.fftshift(fft2)

plt.subplot(233)
plt.imshow(np.abs(shift2center), "gray")
plt.title("頻域矩形的中心")
# 對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(fft2))

plt.subplot(235)
plt.imshow(log_fft2, "gray")
plt.title("傅立葉變換對數變換")
# 對中心化后的結果進行對數變換，并顯示結果
log_shift2center = np.log(1 + np.abs(shift2center))

plt.subplot(236)
plt.imshow(log_shift2center, "gray")
plt.title("中心化的對數變化")

plt.show()

print("------------------------------------------------------------")  # 60個

print("magnitude_spectrum")

# 檔案 => cv2影像
image = cv2.imread("data/lena.png", 0)

dft = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))

# 繪製結果
fig = plt.figure(
    num="magnitude_spectrum",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121), plt.imshow(image, cmap="gray")
plt.title("原始圖像")

plt.subplot(122)
plt.imshow(magnitude_spectrum, cmap="gray")
plt.title("級頻譜")

plt.show()

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

newimage = CreateNewImg(image)
cv2.imshow("原始圖像", image)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

cv2.imshow("去霧后圖像", newimage / 255)
""" 不能用
plt.imshow(cv2.cvtColor(newimage / 255, cv2.COLOR_BGR2RGB))
plt.show()
"""

print("------------------------------------------------------------")  # 60個

print("兩圖相減")

filename1 = "data/_compare/compare1.jpg"
filename2 = "data/_compare/compare2.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

# image3 = math.fabs(image1-image2)
image3 = image1 - image2

fig = plt.figure(
    num="兩圖相減",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
plt.title("原圖1")

plt.subplot(132)
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.title("原圖2")

plt.subplot(133)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title("兩圖相減")

plt.show()

print("------------------------------------------------------------")  # 60個


def salt_pepper_noise(image, fraction, salt_vs_pepper):
    img = np.copy(image)
    size = img.size
    num_salt = np.ceil(fraction * size * salt_vs_pepper).astype("int")
    num_pepper = np.ceil(fraction * size * (1 - salt_vs_pepper)).astype("int")
    row, column = img.shape

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_pepper)
    y = np.random.randint(0, row - 1, num_pepper)
    img[y, x] = 0  # 撒上胡椒

    # 隨機的座標點
    x = np.random.randint(0, column - 1, num_salt)
    y = np.random.randint(0, row - 1, num_salt)
    img[y, x] = 255  # 撒上鹽
    return img


fraction = 0.1  # 雜訊佔圖的比例
salt_vs_pepper = 0.5  # 鹽與胡椒的比例

filename = "C:/_git/vcs/_4.python/_data/tiger.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
noisy = salt_pepper_noise(image, fraction, salt_vs_pepper)

plt.imshow(cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB))
plt.title("胡椒(黑)鹽(白)效果")

plt.show()

# 黑點就好比胡椒，白點就像是鹽，這種加上雜訊的方式，就稱為椒鹽雜訊（Salt & Pepper Noise）

print("------------------------------------------------------------")  # 60個

"""
print("image_dft2")

print('跑不出來 skip')

PI = 3.141591265

# 檔案 => cv2影像
image = plt.imread('data/castle3.jpg')

#根據公式轉成灰度圖
image = 0.2126 * image[:,:,0] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,2]

#顯示原圖
plt.subplot(131),plt.imshow(image,'gray'),plt.title('original')

#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)
log_fft2 = np.log(1 + np.abs(fft2))
plt.subplot(132),plt.imshow(log_fft2,'gray'),plt.title('log_fft2')

h , w = image.shape
#生成一個同樣大小的復數矩陣
F = np.zeros([h,w],'complex128')
for u in range(h):
    for v in range(w):
        res = 0
        for x in range(h):
            for y in range(w):
                res += image[x,y] * np.exp(-1.j * 2 * PI * (u * x / h + v * y / w))
        F[u,v] = res

log_F = np.log(1 + np.abs(F))
plt.subplot(133)
plt.imshow(log_F,'gray')
plt.title('log_F')
"""

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename)

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 轉成灰階

# image2 = cv2.cvtColor(image1, 6)  # 也可以用數字對照 6 表示轉換成灰階
# 套用 medianBlur() 中值模糊
image3 = cv2.medianBlur(image2, 7)  # 模糊化，去除雜訊 7, 25 彩色黑白皆可
image4 = cv2.Canny(image3, 36, 36)  # 偵測邊緣

# 套用自適應二值化黑白影像
image5 = cv2.adaptiveThreshold(
    image3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

plt.figure(
    num="相加",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))

plt.subplot(232)
plt.title("轉成灰階")
plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))

plt.subplot(233)
plt.title("模糊化，去除雜訊")
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))

plt.subplot(234)
plt.title("偵測邊緣")
plt.imshow(cv2.cvtColor(image4, cv2.COLOR_BGR2RGB))

plt.subplot(235)
plt.title("自適應二值化黑白影像")
plt.imshow(cv2.cvtColor(image5, cv2.COLOR_BGR2RGB))

plt.subplot(236)
plt.title("")

plt.tight_layout()  # 緊密排列，並填滿原圖大小
plt.show()

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
plt.show()

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
plt.show()

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

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

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

cv2.imshow("image blue", image_b)
cv2.imshow("image green", image_g)
cv2.imshow("image red", image_r)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_04")

# 檔案 => cv2影像
image = cv2.imread(filename)
print("原圖為彩色")
cv2.imshow("image1", image)
print("彩色轉灰階")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉換成灰階影像

cv2.imshow("image", image)

cv2.waitKey()
cv2.destroyAllWindows()

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

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_06")

print("像素操作 全張負片")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

image = 255 - image  # 使用 255 減去陣列中所有數值

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

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

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_08")

# 檔案 => cv2影像
image = cv2.imread(filename)

output = image  # 建立 output 變數

alpha = 1
beta = 10

cv2.convertScaleAbs(image, output, alpha, beta)  # 套用 convertScaleAbs

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

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

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_12 addWeighted 要一樣大的圖")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

output = cv2.addWeighted(image1, 1.0, image2, 1.0, 100)  # 整體墊高100

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_13 subtract 兩圖相減")

filename1 = "C:/_git/vcs/_4.python/opencv/data/RGB_R.png"
filename2 = "C:/_git/vcs/_4.python/opencv/data/RGB_G.png"

# 檔案 => cv2影像
image1 = cv2.imread(filename1)

# 檔案 => cv2影像
image2 = cv2.imread(filename2)

output = cv2.subtract(image1, image2)  # 相減

cv2.imshow("image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_14 漸層色")

# 檔案 => cv2影像
image = cv2.imread(filename)

w, h = 400, 400
image1 = np.zeros([h, w, 3])
for i in range(h):
    image[i, :, 1] = int(256 * i / 400)  # 從上往下填入綠色漸層

image = image.astype("float32") / 255  # 轉換內容類型

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_15 漸層色")

w = 400
h = 400
image = np.zeros([h, w, 3])
for i in range(h):
    for j in range(w):
        image[i, j, 0] = int(256 * (j + i) / (w + h))
        image[i, j, 2] = int(256 * (j + i) / (w + h))

image = image.astype("float32") / 255

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_16")

w = 400
h = 400
image = np.zeros([h, w, 4])  # 第三個值為 4
for i in range(h):
    image[i, :, 3] = int(256 * i / 400)  # 設定第四個值 ( 透明度 )

image = image.astype("float32") / 255

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_17 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

# 檔案 => cv2影像
image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)  # 開啟圖片

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 因為是 jpg，要轉換顏色為 BGRA
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 新增 gray 變數為轉換成灰階的圖片

h = image.shape[0]  # 取得圖片高度
w = image.shape[1]  # 取得圖片寬度

# 依序取出圖片中每個像素
for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x, 3] = 255 - gray[y, x]
            # 如果該像素的灰階度大於 200，調整該像素的透明度
            # 使用 255 - gray[y, x] 可以將一些邊緣的像素變成半透明，避免太過鋸齒的邊緣

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_18 logo處理")

logo_filename = "C:/_git/vcs/_4.python/opencv/data/opencv_logo.png"

# 檔案 => cv2影像
image = cv2.imread(logo_filename, cv2.IMREAD_UNCHANGED)

image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

h = image.shape[0]
w = image.shape[1]

for x in range(w):
    for y in range(h):
        if gray[y, x] > 200:
            image[y, x] = [0, 255, 255, 255]  # 亮色改成黃色

cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

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

cv2.imshow("image", bg)
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_20")

# 檔案 => cv2影像
image = cv2.imread(filename)


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


h, w = image.shape[:2]  # 取得原始影像的長寬
mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 製作 mask，長寬都要加上 2
output = floodFill(image, mask, (100, 10), (0, 0, 255), (100, 100, 60), (100, 100, 100))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_21")

# 檔案 => cv2影像
image = cv2.imread(filename)


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


h, w = image.shape[:2]
mask = np.zeros((h + 2, w + 2, 1), np.uint8)  # 全黑遮罩
mask = 255 - mask  # 變成全白遮罩
mask[0:100, 0:200] = 0  # 將左上角長方形變成黑色

# 只處理mask區域
output = floodFill(image, mask, (100, 10), (0, 0, 255), (100, 100, 60), (200, 200, 200))

cv2.imshow("image", output)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_23")


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

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_24")
print("按Q離開")

# 檔案 => cv2影像
image = cv2.imread(filename)  # 開啟圖片
image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)  # 轉換成 BGRA ( 因為需要 alpha 色版 )
w = image.shape[1]  # 取得寬度
h = image.shape[0]  # 取得高度
white = 255 - np.zeros((h, w, 4), dtype="uint8")  # 建立白色圖
a = 1  # 一開始 a 為 1
while True:
    a = a - 0.01  # a 不斷減少 0.01
    if a < 0:
        a = 0  # 如果 a 小於 0 就讓 a 等於 0
    output = cv2.addWeighted(white, a, image, 1 - a, 0)  # 根據 a 套用權重
    cv2.imshow("image", output)  # 顯示圖片
    if cv2.waitKey(1) == ord("q"):
        break

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

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

show = image1.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

cv2.imshow("image", show)
cv2.waitKey()
cv2.destroyAllWindows()

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

mona = mona.astype("float32") / 255  # 如果要使用 imshow 必須要轉換類型

cv2.imshow("image", mona)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_34")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)  # 開啟圖片

qrcode = cv2.QRCodeDetector()  # 建立 QRCode 偵測器
data, bbox, rectified = qrcode.detectAndDecode(image)  # 偵測圖片中的 QRCode
# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)  # QRCode 的內容
    print(bbox)  # QRCode 的邊界
    print(rectified)  # 換成垂直 90 度的陣列

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_35")

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 取得座標的函式
def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)  # 轉置矩陣，把 x 放在同一欄，y 放在同一欄
    xmax = int(np.amax(box_roll[0]))  # 取出 x 最大值
    xmin = int(np.amin(box_roll[0]))  # 取出 x 最小值
    ymax = int(np.amax(box_roll[1]))  # 取出 y 最大值
    ymin = int(np.amin(box_roll[1]))  # 取出 y 最小值
    return (xmin, ymin, xmax, ymax)


# 如果 bbox 是 None 表示圖片中沒有 QRCode
if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 5)  # 畫矩形

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_36")

from PIL import ImageFont, ImageDraw, Image  # 載入 PIL ( 為了放中文字 )

filename = "C:/_git/vcs/_4.python/opencv/data/QR1.png"

# 檔案 => cv2影像
image = cv2.imread(filename)

qrcode = cv2.QRCodeDetector()
data, bbox, rectified = qrcode.detectAndDecode(image)


# 建立放入文字的函式
def putText(x, y, text, color=(0, 0, 0)):
    global image
    # font_filename = 'NotoSansTC-Regular.otf'      # 字體 ( 從 Google Font 下載 )
    font = ImageFont.truetype(font_filename, 20)  # 設定字型與大小
    imagePil = Image.fromarray(image)  # 將 image 轉換成 PIL 圖片物件
    draw = ImageDraw.Draw(imagePil)  # 建立繪圖物件
    draw.text((x, y), text, fill=color, font=font)  # 寫入文字
    image = np.array(imagePil)  # 轉換回 np array


def boxSize(arr):
    global data
    box_roll = np.rollaxis(arr, 1, 0)
    xmax = int(np.amax(box_roll[0]))
    xmin = int(np.amin(box_roll[0]))
    ymax = int(np.amax(box_roll[1]))
    ymin = int(np.amin(box_roll[1]))
    return (xmin, ymin, xmax, ymax)


if bbox is not None:
    print(data)
    print(bbox)
    print(rectified)
    box = boxSize(bbox[0])
    cv2.rectangle(image, (box[0], box[1]), (box[2], box[3]), (0, 0, 255), 5)

cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_37")

""" many-qr-code
from PIL import ImageFont, ImageDraw, Image

# 檔案 => cv2影像
image = cv2.imread("many-qrcode.jpg")

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

qrcode = cv2.QRCodeDetector()
ok, data, bbox, rectified = qrcode.detectAndDecodeMulti(image)   # 改用 detectAndDecodeMulti
# 如果有偵測到
if ok:
    # 使用 for 迴圈取出每個 QRCode 的資訊
    for i in range(len(data)):
        print(data[i])
        print(bbox[i])
        text = data[i]          # QRCode 內容
        box = boxSize(bbox[i])  # QRCode 左上與右下座標
        cv2.rectangle(image,(box[0],box[1]),(box[2],box[3]),(0,0,255),5)  # 標記外框
        putText(box[0],box[3],text)   # 寫出文字

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()
"""

print("------------------------------------------------------------")  # 60個
print("OpenCV_38")

""" barcode
from PIL import ImageFont, ImageDraw, Image

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

cv2.imshow('image', image)
cv2.waitKey()
cv2.destroyAllWindows()
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
'''

print("------------------------------------------------------------")  # 60個

print("OpenCV_41 Trackbar之使用")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename)

cv2.imshow("ImageShow", image)

def apply_function(val):
    print('數值 :', val, end = " ")


# cv2.createTrackbar('滑桿名稱', '視窗名稱', min, max, fn)
# min 最小值 ( 最小為 0，不可為負值 )
# max 最大值
# fn 滑桿數值改變時要執行的函式
# 加入滑桿 0 ~ 200, 預設 100
cv2.createTrackbar("test", "ImageShow", 0, 200, apply_function)
cv2.setTrackbarPos("test", "ImageShow", 100)

keycode = cv2.waitKey(0)
cv2.destroyAllWindows()

sys.exit()
print("------------------------------------------------------------")  # 60個
print("OpenCV_42")


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("OpenCV_39 按ESC離開")

cv2.namedWindow("ImageShow")  # 建立一個名為 ImageShow 的視窗

while True:
    keycode = cv2.waitKey(0)  # 持續等待，直到按下鍵盤按鍵才會繼續
    c = chr(keycode)  # 將 ASCII 代碼轉換成真實字元
    print(c, keycode)  # 印出結果
    if keycode == 27:
        break  # 如果代碼等於 27，結束迴圈 ( 27 表示按鍵 ESC )

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

# 新進 與 測試

"""

    image = cv2.flip(image, 1)                        # 翻轉影像，使其如同鏡子
    image = image[:, int((w-h)/2):int((h+(w-h)/2))]   # 將影像變成正方形

"""


print("------------------------------------------------------------")  # 60個

print("二值化")


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename)

THRESHOLD = 127


#        cv2.threshold(image, 閥值, 最大灰度值, 使用的二值化方法)
t, rst = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY)
# t, rst = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_BINARY_INV)
# t, rst = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TRUNC)
# t, rst = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TOZERO_INV)
# t, rst = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TOZERO)

plt.figure(
    num="new29 二值化",
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
plt.title("二值化圖, 閥值 = " + str(THRESHOLD) + ", 小於變全黑, 大於變全白")
plt.imshow(cv2.cvtColor(rst, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

THRESHOLD = 127

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/computer.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

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

plt.show()

print("------------------------------------------------------------")  # 60個

THRESHOLD = 127

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/tiffany.bmp"

# 檔案 => cv2影像
image = cv2.imread(filename, 0)

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

plt.show()

print("------------------------------------------------------------")  # 60個

print("圖片的二值化處理, 要先轉成灰階, 再二值化")

THRESHOLD = 30
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

thr, image_binary = cv2.threshold(image, THRESHOLD, 255, cv2.THRESH_TOZERO)
print(thr)

plt.imshow(cv2.cvtColor(image_binary, cv2.COLOR_BGR2RGB))
plt.show()

print("------------------------------------------------------------")  # 60個

print("OpenCV_09 各種二值化")

THRESHOLD = 127

# 檔案 => cv2影像
image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 轉換前，都先將圖片轉換成灰階色彩
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

cv2.imshow("image", image)
cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.imshow("image3", output3)
cv2.imshow("image4", output4)
cv2.imshow("image5", output5)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("OpenCV_10")

THRESHOLD = 127

# 檔案 => cv2影像
image = cv2.imread(filename)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 轉換前，都先將圖片轉換成灰階色彩
ret, output1 = cv2.threshold(image_gray, THRESHOLD, 255, cv2.THRESH_BINARY)
output2 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
output3 = cv2.adaptiveThreshold(
    image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)

cv2.imshow("image", image)
cv2.imshow("image1", output1)
cv2.imshow("image2", output2)
cv2.imshow("image3", output3)
cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

