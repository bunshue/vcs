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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print("測試 01------------------------------------------------------------")  # 60個
'''
# 影像對比與亮度調整
import matplotlib.image as img


# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(image, alpha=1.0, beta=0.0):
    array_alpha = np.array([alpha])  # 對比度
    array_beta = np.array([beta])  # 亮度
    image = cv2.add(image, array_beta)
    image = cv2.multiply(image, array_alpha)
    image = np.clip(image, 0, 255)
    return image


plt.figure(
    num="影像對比與亮度調整",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)
image = cv2.imread(filename)  # 讀取本機圖片
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

modified_image = modify_contrast_and_brightness(image, 1.5, 10.0)
plt.subplot(122)
plt.imshow(cv2.cvtColor(modified_image, cv2.COLOR_BGR2RGB))
plt.title("影像對比與亮度調整")

plt.show()

print("測試 02------------------------------------------------------------")  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = 'C:/_git/vcs/_4.python/opencv/data/rgb256X300.bmp'
filename = 'C:/_git/vcs/_4.python/opencv/data/rgb512.bmp'

image = cv2.imread(filename)

plt.subplot(331)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")

"""same
b=image[:,:,0]
g=image[:,:,1]
r=image[:,:,2]
"""

b, g, r = cv2.split(image)

print(image.shape)
# print(image)

print(b.shape)
# print(b)

print(g.shape)
# print(g)

print(r.shape)
# print(r)

print("顯示 ch2 紅 通道 圖")
plt.subplot(334)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("紅 第2通道")

print("顯示 ch1 綠 通道 圖")
plt.subplot(335)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("綠 第1通道")

print("顯示 ch0 藍 通道 圖")
plt.subplot(336)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("藍  第0通道")

print("設定第2通道為0")
image[:, :, 2] = 0
plt.subplot(337)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("設定第2通道為0")

print("再設定第1通道為0")
image[:, :, 1] = 0
plt.subplot(338)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第1通道為0")

print("再設定第0通道為0")
image[:, :, 0] = 0
plt.subplot(339)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("再設定第0通道為0")

plt.show()

print("測試 05------------------------------------------------------------")  # 60個

plt.figure(
    num="將一圖分解成 藍 綠 紅 三通道",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png"
filename = 'C:/_git/vcs/_4.python/opencv/data/rgb256X300.bmp'
filename = 'C:/_git/vcs/_4.python/opencv/data/rgb512.bmp'

image = cv2.imread(filename)

b, g, r = cv2.split(image)

bgr = cv2.merge([b, g, r])
rgb = cv2.merge([r, g, b])

plt.subplot(231)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.subplot(232)
plt.imshow(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))  # 照BGR排列 OK
plt.title("B-G-R OK")
plt.subplot(233)
plt.imshow(cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB))  # 照RGB排列 錯相
plt.title("R-G-B NG")

plt.subplot(234)
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))
plt.title("R分量")
plt.subplot(235)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))
plt.title("G分量")
plt.subplot(236)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("B分量")

plt.show()

print("測試 06------------------------------------------------------------")  # 60個

filename = "images/girl.bmp"
image = cv2.imread(filename)
imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

plt.figure(
    num="顯示結果",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("原圖BGR OK")

plt.subplot(122)
plt.imshow(cv2.cvtColor(imageRGB, cv2.COLOR_BGR2RGB))
plt.title("原圖RGB NG")

plt.show()

print("測試 07------------------------------------------------------------")  # 60個

plt.figure(
    num="灰度圖像顯示演示",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

image = cv2.imread("images/8.bmp")
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(221)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(222)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray_r)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap="gray")

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap="gray_r")

plt.show()

print("測試 08------------------------------------------------------------")  # 60個

plt.figure(
    num="灰度圖像顯示演示",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

filename = "images/girl.bmp"
image = cv2.imread(filename)
g = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure("灰度圖像顯示演示")
plt.subplot(221)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.subplot(223)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.imshow(cv2.cvtColor(g, cv2.COLOR_BGR2RGB), cmap=plt.cm.gray)

plt.show()

print("測試 09------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Laplacian(img, -1, 1, 5)        # 偵測邊緣

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()


print("測試 09------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Sobel(img, -1, 1, 1, 1, 7)      # 偵測邊緣

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()


print("測試 09------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 轉成灰階
img = cv2.medianBlur(img, 7)                 # 模糊化，去除雜訊
output = cv2.Canny(img, 36, 36)              # 偵測邊緣
print(output)

cv2.imshow('image', output)
cv2.waitKey()
cv2.destroyAllWindows()



print("測試 09------------------------------------------------------------")  # 60個


mask = np.zeros((300,300,3), dtype='uint8')      # 建立 300x300 的黑色畫布
cv2.circle(mask,(150,150),100,(255,255,255),-1)  # 在畫布上中心點加入一個半徑 100 的白色圓形
mask = cv2.GaussianBlur(mask, (35, 35), 0)       # 進行高斯模糊

cv2.imshow('image', mask)
cv2.waitKey()
cv2.destroyAllWindows()

print("測試 09------------------------------------------------------------")  # 60個

""" TBD
mask = np.zeros((300,300,3), dtype='uint8')
cv2.circle(mask,(150,150),100,(255,255,255),-1)
mask = cv2.GaussianBlur(mask, (35, 35), 0)
mask = mask / 255                          # 除以 255，計算每個像素的黑白色彩在 255 中所佔的比例

img = cv2.imread(filename)               # 開啟圖片
bg = np.zeros((300,300,3), dtype='uint8')  # 產生一張黑色背景
bg = 255 - bg                              # 轉換成白色背景
img = img / 255                            # 除以 255，計算每個像素的色彩在 255 中所佔的比例
bg = bg / 255                              # 除以 255，計算每個像素的色彩在 255 中所佔的比例

out  = bg * (1 - mask) + img * mask        # 根據比例混合
out = (out * 255).astype('uint8')          # 乘以 255 之後轉換成整數

cv2.imshow('image',out)
cv2.waitKey()
cv2.destroyAllWindows()
"""
'''

print("測試 09------------------------------------------------------------")  # 60個


# Prewitt horizontal edge-emphasizing filter 邊緣加強的影像處理技術

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
image = cv2.imread(filename)

print("filter2D 效果")
kernel = np.ones((9, 9), np.float32) / 81
image_filter2D = cv2.filter2D(image, -1, kernel)

plt.figure(
    num="new26 filter2D 效果",
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
plt.title("filter2D 效果")
plt.imshow(cv2.cvtColor(image_filter2D, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"
image = cv2.imread(filename, cv2.COLOR_BGR2GRAY)

kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=int)  # 水平值一樣, 偵測水平的邊緣
kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=int)  # 垂直值一樣, 偵測垂直的邊緣

print("filter2D 效果")

x = cv2.filter2D(image, cv2.CV_16S, kernel_x)
y = cv2.filter2D(image, cv2.CV_16S, kernel_y)

absX = cv2.convertScaleAbs(x)
absY = cv2.convertScaleAbs(y)

plt.figure(
    num="new27",
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
plt.title("Prewitt_horizon")
# 躺平的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absX, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("Prewitt_vertical")
# 直放的書本的邊緣有被強調出來
plt.imshow(cv2.cvtColor(absY, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

print("製作毛玻璃效果")

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

import numpy as np

img = cv2.imread(filename)
result = img.copy()
H, W = result.shape[:2]
print(H, W)

for y in range(H-5):
    for x in range(W-5):
        random_num = np.random.randint(0, 5)
        result[y, x] = img[y+random_num, x+random_num]

cv2.imshow('src', img)
cv2.imshow('result', result)

cv2.waitKey(0)
cv2.destroyAllWindows()


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


print("圖像平滑 salt")


# 模擬椒鹽噪聲，number 指添加椒鹽噪聲的數量
def salt(image, number):
    # 圖像的寬高
    rows, cols = image.shape
    # 加入椒鹽噪聲後的圖像
    saltImage = np.copy(image)
    for i in range(number):
        randR = random.randint(0, rows - 1)
        randC = random.randint(0, cols - 1)
        saltImage[randR][randC] = 0
    return saltImage

filename = "C:/_git/vcs/_4.python/_data/tiger.jpg"

# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 顯示原圖
cv2.imshow("image", image)

# 添加椒鹽噪聲
saltImage = salt(image, 2000)
cv2.imshow("saltImage", saltImage)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

# 檔案 => cv2影像
image1 = cv2.imread(filename)

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)  # 彩色轉灰階

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


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
