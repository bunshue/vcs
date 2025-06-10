"""
傅立葉變換 fft

np 傅立葉
np.fft.fft()  # 一維 fft
np.fft.ifft()  # 一維 ifft
np.fft.rfft

np.fft.fft2() + np.fft.fftshift  # 二維 fft
np.fft.ifft2  # 二維 ifft

cv 傅立葉 cv2.dft cv2.idft

"""

print("------------------------------------------------------------")  # 60個

import cv2
import pylab as pl

ESC = 27

NNNN = 100

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

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


# 三角波
def triangle_wave(size):
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, x, 0)
    y = np.where(x >= 0.5, 1 - x, y)
    return x, y


# 正弦波
def sine_wave1(size):
    A = 10
    f = 60
    # x = np.arange(0, 2 * np.pi, 2 * np.pi / size)
    x = np.linspace(0, 1 / f * 3, size)  # 時間, 3個週期
    # y = np.sin(x)
    y = A * np.sin(2 * np.pi * f * x)
    print("aaaa :", x.shape, y.shape)
    return x, y


# 正弦波
def sine_wave2(size):
    A = 10
    f = 60
    x = np.linspace(0, 1 / f * 3, size)  # 時間, 3個週期
    y = A * np.sin(2 * np.pi * f * x)
    print("bbbb :", x.shape, y.shape)
    return x, y


# 方波的頻譜、合成方波在跳變處出現抖動
def square_wave(size):
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, 1.0, 0)
    return x, y


# print("np顯示小數點以下3位, IDLE顯示寬度80字, 無壓縮顯示")
np.set_printoptions(precision=3, linewidth=80, suppress=False)

# print("np顯示小數點以下3位, IDLE顯示寬度80字, 有壓縮顯示")
# np.set_printoptions(precision=3, linewidth=80, suppress=True)

import scipy

'''
print("------------------------------------------------------------")  # 60個
# 使用 np 傅立葉
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

""" 自己造資料
N = 11
image = np.zeros((N, N))
#print(image)
cx, cy = N // 2, N // 2
#print(cx, cy)
image[cx-1:cx+2, cy-1:cy+2] = 1
# image[cx, cy] = 1
#print(image)
"""

plt.subplot(221)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
s1 = np.log(np.abs(fshift))
# fimage = np.log(np.abs(f))
fimage = np.abs(s1)
plt.subplot(222)
plt.imshow(fimage, cmap="gray")
plt.title("fftshift")

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(fshift))  # 轉成頻譜
plt.subplot(223)
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心
ifshift = np.fft.ifftshift(fshift)  # 逆傅立葉變換,  # 0 頻率頻率移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉變換, 將頻域訊號轉換回時域訊號
src_back = np.abs(src_tmp)  # 取絕對值
plt.subplot(224)
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("ifft")

plt.suptitle("使用 np 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 高通濾波

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心

# 高通濾波器
rows, cols = image.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
fshift[row - 30 : row + 30, col - 30 : col + 30] = 0  # 設定區塊為低頻率分量是0

ifshift = np.fft.ifftshift(fshift)  # 逆傅立葉變換  # 0 頻率分量移回左上角
src_tmp = np.fft.ifft2(ifshift)  # 逆傅立葉變換, 將頻域訊號轉換回時域訊號
src_back = np.abs(src_tmp)  # 取絕對值

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("高通濾波灰階影像")

plt.suptitle("高通濾波")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 二維離散傅立葉變換

print("NXN的隨機影像")
N = 5
image = np.random.rand(N, N)

plt.imshow(image, cmap="gray")
show()

print(image)

print("------------------------------")  # 30個
print("傅立葉變換")

X = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
print(X)
print("------------------------------")  # 30個
print("逆傅立葉變換")
x2 = np.fft.ifft2(X)  # 逆傅立葉變換, 將頻域訊號轉換回時域訊號
print(x2)

print("------------------------------")  # 30個
# np.allclose():檢查兩個數組是否每個元素都相似, 預設誤差在1e-05內
cc = np.allclose(image, x2)  # 和原始訊號進行比較
print(cc)
print("------------------------------------------------------------")  # 60個

print("製作 sinc2d 資料")

N = 100
sinc2d = np.zeros((N, N))
for x, x1 in enumerate(np.linspace(-2 * np.pi, 2 * np.pi, N)):
    for y, x2 in enumerate(np.linspace(-2 * np.pi, 2 * np.pi, N)):
        # sinc2d[x, y] = np.sin(x1) * np.sin(x2) / (x1 * x2)  # 二維 sinc 函數
        sinc2d[x, y] = np.sqrt(x1**2 + x2**2)

# 製作 sinc2d 資料 same
# x1 = np.linspace(-10, 10, N)
# x2 = np.linspace(-10, 10, N)
# sinc2d = np.outer(np.sin(x1), np.sin(x2)) / np.outer(x1, x2)  # 二維 sinc 函數

# plt.imshow(sinc2d)
# show()

print("製作 簡易 X矩陣 資料")
N = 5
image = np.zeros((N, N))

cx, cy = N // 2, N // 2
print(cx, cy)

# image[cx-1:cx+2, cy-1:cy+2] = 1
image[cx, cy] = 1
print(image)

# image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式
# image = sinc2d # 使用 sinc2d

print("------------------------------")  # 30個

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
fshift = np.fft.fftshift(f)  # 0 頻率分量移至中心

spectrum = 20 * np.log(np.abs(fshift))
print(spectrum)

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(spectrum, cmap="gray")
plt.title("fftshift")

plt.suptitle("使用 np 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
# fshift = np.fft.fftshift(f)            # 0 頻率分量移至中心
spectrum = 20 * np.log(np.abs(f))  # 轉成頻譜

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")

plt.suptitle("使用 np 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("使用 cv 傅立葉 ST")
# cv2.dft
# cv2.idft
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

fshift = np.fft.fftshift(X_DFT)
result = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(result, cmap="gray")
plt.title("fftshift")

plt.suptitle("使用 cv 傅立葉")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# cv2 逆傅立葉變換

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

fshift = np.fft.fftshift(X_DFT)
ifshift = np.fft.ifftshift(fshift)  # 逆傅立葉變換
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(src_back, cmap="gray")
plt.title("ifft")

plt.suptitle("使用 cv 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 低通濾波

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

fshift = np.fft.fftshift(X_DFT)  # 0 頻率分量移至中心

# 低通濾波器
rows, cols = image.shape  # 取得影像外形
crow, ccol = rows // 2, cols // 2
mask = np.zeros((rows, cols, 2), np.uint8)
# 两个通道，与频谱图像匹配
mask[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 1
FFT_SHIFT_MASK = fshift * mask
ifshift = np.fft.ifftshift(FFT_SHIFT_MASK)  # 逆傅立葉變換
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(src_back, cmap="gray")
plt.title("低通濾波影像")

plt.suptitle("低通濾波")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 低通濾波

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

dftshift = np.fft.fftshift(X_DFT)  # 0 頻率分量移至中心

# 低通濾波器
rows, cols = image.shape  # 取得影像外形
row, col = rows // 2, cols // 2  # rows, cols的中心
mask = np.zeros((rows, cols, 2), np.uint8)
mask[row - 30 : row + 30, col - 30 : col + 30] = 1  # 設定區塊為低頻率分量是1

fshift = dftshift * mask
ifshift = np.fft.ifftshift(fshift)  # 逆傅立葉變換  # 0 頻率分量移回左上角
src_tmp = cv2.idft(ifshift)  # 逆傅立葉
src_back = cv2.magnitude(src_tmp[:, :, 0], src_tmp[:, :, 1])

plt.subplot(131)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(132)
plt.imshow(src_back, cmap="gray")  # 灰階顯示
plt.title("低通濾波灰階影像")

plt.subplot(133)
plt.imshow(src_back)
plt.title("低通濾波影像")

plt.suptitle("低通濾波")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("頻譜")

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)

fshift = np.fft.fftshift(X_DFT)
spectrum = 20 * np.log(cv2.magnitude(fshift[:, :, 0], fshift[:, :, 1]))

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(spectrum, cmap="gray")
plt.title("頻譜")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換, 轉成頻率域
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(X_DFT)  # 0 頻率分量移至中心
# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(122)
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")

plt.suptitle("使用 cv 傅立葉")
show()

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 傅立葉變換, 轉成頻率域
X_DFT = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
dftshift = np.fft.fftshift(X_DFT)  # 0 頻率分量移至中心

# 計算映射到[0,255]的振幅
spectrum = 20 * np.log(cv2.magnitude(dftshift[:, :, 0], dftshift[:, :, 1]))

# 執行逆傅立葉
idftshift = np.fft.ifftshift(dftshift)  # 逆傅立葉變換
tmp = cv2.idft(idftshift)
dst = cv2.magnitude(tmp[:, :, 0], tmp[:, :, 1])

plt.subplot(131)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

plt.subplot(132)
plt.imshow(spectrum, cmap="gray")  # 灰階顯示
plt.title("頻譜圖")

plt.subplot(133)
plt.imshow(dst, cmap="gray")  # 灰階顯示
plt.title("逆傅立葉影像")

plt.suptitle("使用 cv 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2Conv")

from scipy import signal

# 圖像矩陣
I = np.array(
    [
        [34, 56, 1, 0, 255, 230, 45, 12],
        [0, 201, 101, 125, 52, 12, 124, 12],
        [3, 41, 42, 40, 12, 90, 123, 45],
        [5, 245, 98, 32, 34, 234, 90, 123],
        [12, 12, 10, 41, 56, 89, 189, 5],
        [112, 87, 12, 45, 78, 45, 10, 1],
        [42, 123, 234, 12, 12, 21, 56, 43],
        [1, 2, 45, 123, 10, 44, 123, 90],
    ],
    np.float64,
)
# 卷積核
kernel = np.array([[1, 0, -1], [1, 0, 1], [1, 0, -1]], np.float64)
# I 與 kernel 進行全卷積
confull = signal.convolve2d(I, kernel, mode="full", boundary="fill", fillvalue=0)
# I 的傅里葉變換
FT_I = np.zeros((I.shape[0], I.shape[1], 2), np.float64)

# 傅立葉變換
cv2.dft(I, FT_I, cv2.DFT_COMPLEX_OUTPUT)
# kernel 的傅里葉變換
FT_kernel = np.zeros((kernel.shape[0], kernel.shape[1], 2), np.float64)

# 傅立葉變換
cv2.dft(kernel, FT_kernel, cv2.DFT_COMPLEX_OUTPUT)
# 傅里葉變換
fft2 = np.zeros((confull.shape[0], confull.shape[1]), np.float64)
# 對 I 進行右側和下側補 0
I_Padded = np.zeros(
    (I.shape[0] + kernel.shape[0] - 1, I.shape[1] + kernel.shape[1] - 1), np.float64
)
I_Padded[: I.shape[0], : I.shape[1]] = I
FT_I_Padded = np.zeros((I_Padded.shape[0], I_Padded.shape[1], 2), np.float64)

# 傅立葉變換
cv2.dft(I_Padded, FT_I_Padded, cv2.DFT_COMPLEX_OUTPUT)
# 對 kernel 進行右側和下側補 0
kernel_Padded = np.zeros(
    (I.shape[0] + kernel.shape[0] - 1, I.shape[1] + kernel.shape[1] - 1), np.float64
)
kernel_Padded[: kernel.shape[0], : kernel.shape[1]] = kernel
FT_kernel_Padded = np.zeros(
    (kernel_Padded.shape[0], kernel_Padded.shape[1], 2), np.float64
)

# 傅立葉變換
cv2.dft(kernel_Padded, FT_kernel_Padded, cv2.DFT_COMPLEX_OUTPUT)
# 兩個傅里葉變換相乘
FT_Ikernel = cv2.mulSpectrums(FT_I_Padded, FT_kernel_Padded, cv2.DFT_ROWS)
# 利用傅里葉變換求全 ( full ) 卷積
ifft2 = np.zeros(FT_Ikernel.shape[:2], np.float64)

# 傅立葉變換
cv2.dft(FT_Ikernel, ifft2, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
print(np.max(ifft2 - confull))

# 全卷積進行傅里葉變換等於兩個傅里葉變換的點乘
FT_confull = np.zeros((confull.shape[0], confull.shape[1], 2), np.float64)
# 傅立葉變換
cv2.dft(confull, FT_confull, cv2.DFT_COMPLEX_OUTPUT)
print(FT_confull - FT_Ikernel)
print(np.max(FT_confull - FT_Ikernel))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2toConv")

from scipy import signal


# 利用傅里葉變換計算離散的二維卷積
def fft2Conv(I, kernel, borderType=cv2.BORDER_DEFAULT):
    # 圖像矩陣的高、寬
    R, C = I.shape[:2]
    # 卷積核的高、寬
    r, c = kernel.shape[:2]
    # 卷積核的半徑
    tb = (r - 1) / 2
    lr = (c - 1) / 2
    # 第一步：擴充邊界
    I_padded = cv2.copyMakeBorder(I, tb, tb, lr, lr, borderType)
    # 第二步：對 I_padded 和 kernel 右側和下側補零
    # 滿足二維快速傅里葉變換的行數、列數
    rows = cv2.getOptimalDFTSize(I_padded.shape[0] + r - 1)
    cols = cv2.getOptimalDFTSize(I_padded.shape[1] + c - 1)
    # 補零
    I_padded_zeros = np.zeros((rows, cols), np.float64)
    I_padded_zeros[: I_padded.shape[0], : I_padded.shape[1]] = I_padded
    kernel_zeros = np.zeros((rows, cols), np.float64)
    kernel_zeros[: kernel.shape[0], : kernel.shape[1]] = kernel
    # 第三步：快速傅里葉變換
    fft2_Ipz = np.zeros((rows, cols, 2), np.float64)
    cv2.dft(I_padded_zeros, fft2_Ipz, cv2.DFT_COMPLEX_OUTPUT)
    fft2_kz = np.zeros((rows, cols, 2), np.float64)
    cv2.dft(kernel_zeros, fft2_kz, cv2.DFT_COMPLEX_OUTPUT)
    # 第四步：兩個快速傅里葉變換點乘
    Ipz_rz = cv2.mulSpectrums(fft2_Ipz, fft2_kz, cv2.DFT_ROWS)
    # 第五步：傅里葉逆變換，并只取實部
    ifft2FullConv = np.zeros((rows, cols), np.float64)
    cv2.dft(
        Ipz_rz, ifft2FullConv, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE
    )
    print(np.max(ifft2FullConv))
    # 第六步：裁剪，同輸入的圖像矩陣尺寸一樣
    sameConv = np.copy(ifft2FullConv[r - 1 : R + r - 1, c - 1 : C + c - 1])
    return sameConv


# 圖像矩陣
I = np.array(
    [
        [34, 56, 1, 0, 255, 230, 45, 12],
        [0, 201, 101, 125, 52, 12, 124, 12],
        [3, 41, 42, 40, 12, 90, 123, 45],
        [5, 245, 98, 32, 34, 234, 90, 123],
        [12, 12, 10, 41, 56, 89, 189, 5],
        [112, 87, 12, 45, 78, 45, 10, 1],
        [42, 123, 234, 12, 12, 21, 56, 43],
        [1, 2, 45, 123, 10, 44, 123, 90],
    ],
    np.float32,
)

# 卷積核
kernel = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], np.float32)
# same 卷積
consame = signal.convolve2d(I, kernel, mode="same", boundary="symm")
print(consame)

""" fail
# 利用傅里葉變換計算卷積
sameConv = fft2Conv(I,kernel,cv2.BORDER_REFLECT)
print(sameConv)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

image = plt.imread("data/castle3.jpg")

# 根據公式轉成灰度圖
image = 0.2126 * image[:, :, 0] + 0.7152 * image[:, :, 1] + 0.0722 * image[:, :, 2]

plt.figure(figsize=(12, 8))

plt.subplot(231)
plt.imshow(image, "gray")
plt.title("原圖")

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域

plt.subplot(232)
plt.imshow(np.abs(f), "gray")
plt.title("二維傅里葉變換")

# 將圖像變換的原點移動到頻域矩形的中心，并顯示效果
fshift = np.fft.fftshift(f)

plt.subplot(233)
plt.imshow(np.abs(fshift), "gray")
plt.title("頻域矩形的中心")

# 對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(f))

plt.subplot(235)
plt.imshow(log_fft2, "gray")
plt.title("傅立葉變換對數變換")

# 對中心化后的結果進行對數變換，并顯示結果
log_FFT_SHIFT = np.log(1 + np.abs(fshift))

plt.subplot(236)
plt.imshow(log_FFT_SHIFT, "gray")
plt.title("中心化的對數變化")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 跑不出來 skip
print("image_dft2")

PI = 3.141591265

image = plt.imread('data/castle3.jpg')

#根據公式轉成灰度圖
image = 0.2126 * image[:,:,0] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,2]

plt.subplot(131)
plt.imshow(image,'gray')
plt.title('原圖')

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域
log_fft2 = np.log(1 + np.abs(f))

plt.subplot(132)
plt.imshow(log_fft2,'gray')
plt.title('log_fft2')

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

show()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

N = 256
image = cv2.resize(image, (N, N))

f = np.fft.fft2(image)  # 對 image 做np fft, 轉成頻率域

X_mag = np.log10(np.abs(f))

fshift = np.fft.fftshift(X_mag)

rects = [
    (80, 125, 85, 130),
    (90, 90, 95, 95),
    (150, 10, 250, 250),
    (110, 110, 146, 146),
]

"""
    scpy2.opencv.fft2d_demo：示範二維離散傅立葉變換，
    使用者在左側的頻域模值圖形上用滑鼠繪制隱藏區域，
    右側的圖形為頻域訊號經由隱藏處理之後所轉換成的時域訊號。
"""

# %fig=(左上)用fft2()計算的頻域訊號，(中上)使用fftshift()移位之後的頻域訊號，(其它)各個領域所對應的時域訊號
filtered_results = []
for i, (x0, y0, x1, y1) in enumerate(rects):
    mask = np.zeros((N, N), dtype=np.bool)
    mask[x0 : x1 + 1, y0 : y1 + 1] = True
    mask[N - x1 : N - x0 + 1, N - y1 : N - y0 + 1] = True
    mask = np.fft.fftshift(mask)
    X_freq2 = f * mask
    X_filtered = np.fft.ifft2(f).real
    filtered_results.append(X_filtered)

fig, axes = pl.subplots(2, 3, figsize=(9, 6))
axes = axes.ravel()
axes[0].imshow(X_mag, cmap=pl.cm.gray)
axes[1].imshow(fshift, cmap=pl.cm.gray)

ax = axes[1]
for i, (x0, y0, x1, y1) in enumerate(rects):
    r = pl.Rectangle((x0, y0), x1 - x0, y1 - y0, alpha=0.2)
    ax.add_artist(r)
    pl.text(
        (x0 + x1) / 2,
        (y0 + y1) / 2,
        str(i + 1),
        color="white",
        transform=ax.transData,
        ha="center",
        va="center",
        alpha=0.8,
    )

for ax, result in zip(axes[2:], filtered_results):
    ax.imshow(result, cmap=pl.cm.gray)

for ax in axes:
    ax.set_axis_off()

fig.subplots_adjust(0.01, 0.01, 0.99, 0.99, 0.02, 0.02)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

seq = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # 時間值
water = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 水
sugar = [2, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 0]  # 糖
grass = [4, 0, 0, 4, 0, 0, 4, 0, 0, 4, 0, 0]  # 仙草
pearl = [3, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0]  # 黑珍珠

plt.plot(seq, water, "-o", label="水")  # 繪含標記的water折線圖
plt.plot(seq, sugar, "-x", label="糖")  # 繪含標記的sugar折線圖
plt.plot(seq, grass, "-s", label="仙草")  # 繪含標記的grass折線圖
plt.plot(seq, pearl, "-p", label="黑珍珠")  # 繪含標記的pearl折線圖

plt.axis([0, 12, 0, 5])  # 建立軸大小
plt.xlabel("時間軸")  # 時間軸
plt.ylabel("份數")  # 份數
show()

print("------------------------------------------------------------")  # 60個

copies = [1, 2, 4, 3]  # 份數
N = len(copies)
x = np.arange(N)
width = 0.35
plt.bar(x, copies, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("份數")  # 份數
plt.xticks(x, ("1", "2", "3", "4"))
plt.grid(axis="y")
show()

print("------------------------------------------------------------")  # 60個

start = 0
end = 1
x = np.linspace(start, end, 500)  # x 軸區間
y = np.sin(2 * np.pi * 4 * x)  # 建立正弦曲線
plt.plot(x, y)
plt.xlabel("時間(秒)")  # 時間
plt.ylabel("振幅")  # 振幅
plt.title("正弦曲線", fontsize=16)  # 標題
show()

print("------------------------------------------------------------")  # 60個

amplitude = [0, 0, 0, 1, 0, 0, 0]
N = len(amplitude)
x = np.arange(N)
width = 0.3
plt.bar(x, amplitude, width)  # 直條圖
plt.xlabel("頻率")  # 頻率
plt.ylabel("振幅")  # 振幅
plt.xticks(x, ("1", "2", "3", "4", "5", "6", "7"))
plt.grid(axis="y")
show()

print("------------------------------------------------------------")  # 60個

start = 0
# 起始時間
end = 5
# 結束時間
# 兩個正弦波的訊號頻率
freq1 = 5
# 頻率是 5 Hz
freq2 = 8
# 頻率是 8 Hz
# 建立時間軸的np陣列, 用500個點
time = np.linspace(start, end, 500)
# 建立2個正弦波
amplitude1 = np.sin(2 * np.pi * freq1 * time)
amplitude2 = np.sin(2 * np.pi * freq2 * time)

figure, axis = plt.subplots(3, 1)
plt.subplots_adjust(hspace=1)

# 時間域的 sin 波 1
axis[0].set_title("頻率是 5 Hz的 sin 波")
axis[0].plot(time, amplitude1)
axis[0].set_xlabel("時間")
axis[0].set_ylabel("振幅")

# 時間域的 sin 波 2
axis[1].set_title("頻率是 8 Hz的 sin 波")
axis[1].plot(time, amplitude2)
axis[1].set_xlabel("時間")
axis[1].set_ylabel("振幅")

# 加總sin波
amplitude = amplitude1 + amplitude2
axis[2].set_title("2個不同頻率正弦波的結果")
axis[2].plot(time, amplitude)
axis[2].set_xlabel("時間")
axis[2].set_ylabel("振幅")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2")


# 快速傅里葉變換
def fft2Image1(image):
    # 得到行、列
    r, c = image.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = image
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 計算圖像矩陣的快速傅里葉變換
fft2 = fft2Image1(image)

# 傅里葉逆變換
ifft2 = np.zeros(fft2.shape[:2], np.float32)
cv2.dft(fft2, ifft2, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)

# 裁剪
image2 = np.copy(ifft2[: image.shape[0], : image.shape[1]])
# 裁剪後的結果 image2 等於 image，兩個相減的最大值為零
print(np.max(image - image2))

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 spectrum")


# 快速傅里葉變換
def fft2Image2(image):
    # 得到行、列
    r, c = image.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = image
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


# 傅里葉幅度譜
def amplitudeSpectrum(fft2):
    # 求幅度
    real2 = np.power(fft2[:, :, 0], 2.0)
    Imag2 = np.power(fft2[:, :, 1], 2.0)
    amplitude = np.sqrt(real2 + Imag2)
    return amplitude


# 幅度譜的灰度級顯示
def graySpectrum(amplitude):
    # 對比度拉伸
    # cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude + 1.0)
    # 歸一化,傅里葉譜的灰度級顯示
    spectrum = np.zeros(amplitude.shape, np.float32)
    cv2.normalize(amplitude, spectrum, 0, 1, cv2.NORM_MINMAX)
    return spectrum


# 相位譜
def phaseSpectrum(fft2):
    # 得到行數、列數
    rows, cols = fft2.shape[:2]
    # 計算相位角
    phase = np.arctan2(fft2[:, :, 1], fft2[:, :, 0])
    # 顯示該相位譜時，首先需要將相位角轉換為 [ -180 , 180]
    spectrum = phase / math.pi * 180
    return spectrum


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式
cv2.imshow("image", image)

# 快速傅里葉變換
fft2 = fft2Image2(image)

# 求幅度譜
amplitude = amplitudeSpectrum(fft2)
amc = np.copy(amplitude)
amc[amc > 255] = 255
amc = amc.astype(np.uint8)
# cv2.imshow("originam",amc)

# 幅度譜的灰度級顯示
ampSpectrum = graySpectrum(amplitude)
ampSpectrum *= 255
ampSpectrum = ampSpectrum.astype(np.uint8)
cv2.imshow("amplitudeSpectrum", ampSpectrum)

# 相位譜的灰度級顯示
phaseSpe = phaseSpectrum(fft2)
cv2.imshow("phaseSpectrum", phaseSpe)

# 傅里葉幅度譜的中心化

# 第一步：圖像乘以(-1)^(r+c)
rows, cols = image.shape
fimage = np.copy(image)
fimage = fimage.astype(np.float32)
for r in range(rows):
    for c in range(cols):
        if (r + c) % 2:
            fimage[r][c] = -1 * image[r][c]
        else:
            fimage[r][c] = image[r][c]

# 第二步：快速傅里葉變換
imagefft2 = fft2Image2(fimage)

# 第三步：傅里葉的幅度譜
amSpe = amplitudeSpectrum(imagefft2)

# 幅度譜的灰度級顯示
graySpe = graySpectrum(amSpe)
cv2.imshow("amSpe", graySpe)
graySpe *= 255
graySpe = graySpe.astype(np.uint8)

# 第四步：相位譜的灰度級顯示
phSpe = phaseSpectrum(imagefft2)

cv2.imshow("phSpe", phSpe)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 saliencyMap")


# 快速傅里葉變換
def fft2Image3(image):
    # 得到行、列
    r, c = image.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = image
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


# 傅里葉幅度譜
def amplitudeSpectrum(fft2):
    # 求幅度
    real, Imag = cv2.split(fft2)
    amplitude = cv2.magnitude(real, Imag)
    # amplitude = cv2.magnitude(fft2[:,:,0],fft2[:,:,1])
    return amplitude


# 幅度譜的灰度級顯示
def graySpectrum(amplitude):
    # 對比度拉伸
    # cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude + 1.0)
    # 歸一化,傅里葉譜的灰度級顯示
    spectrum = np.zeros(amplitude.shape, np.float32)
    cv2.normalize(amplitude, spectrum, 0, 1, cv2.NORM_MINMAX)
    return spectrum


# 相位譜
def phaseSpectrum(fft2):
    # 得到行數、列數
    rows, cols = fft2.shape[:2]
    # 計算相位角
    phase = np.arctan2(fft2[:, :, 1], fft2[:, :, 0])
    # 顯示該相位譜時，首先需要將相位角轉換為 [ -180 , 180]
    # spectrum = phase/math.pi*180
    return phase


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

# 第一步：計算圖像的快速傅里葉變換
fft2 = fft2Image3(image)

# 第二步：計算傅里葉幅度譜的灰度級
# 求幅度譜
amplitude = amplitudeSpectrum(fft2)
# 幅度譜的灰度級
logAmplitude = graySpectrum(amplitude)

# 第三步：計算相位
phase = phaseSpectrum(fft2)
# 餘弦譜（用於計算實部）
cosSpectrum = np.cos(phase)
# 正弦譜（用於計算虛部）
sinSectrum = np.sin(phase)

# 第四步：計算殘差（Spectral Residual）
# 對幅度譜的灰度級進行均值平滑
meanLogAmplitude = cv2.boxFilter(logAmplitude, cv2.CV_32FC1, (3, 3))
# 殘差
spectralResidual = logAmplitude - meanLogAmplitude

# 第五步：計算傅里葉逆變換,顯著性
# 殘差的指數
expSR = np.exp(spectralResidual)

# 分別計算實部和虛部
real = expSR * cosSpectrum
imaginary = expSR * sinSectrum

# 合併實部和虛部
com = np.zeros((real.shape[0], real.shape[1], 2), np.float32)
com[:, :, 0] = real
com[:, :, 1] = imaginary

# 逆變換
ifft2 = np.zeros(com.shape, np.float32)

# 傅立葉變換
cv2.dft(com, ifft2, cv2.DFT_COMPLEX_OUTPUT + cv2.DFT_INVERSE)

# 顯著性
saliencymap = np.power(ifft2[:, :, 0], 2) + np.power(ifft2[:, :, 1], 2)

# 對顯著性進行高斯平滑
saliencymap = cv2.GaussianBlur(saliencymap, (11, 11), 2.5)  # 執行高斯模糊化

# 顯示檢測到的顯著性
# cv2.normalize(saliencymap,saliencymap,0,1,cv2.NORM_MINMAX)
saliencymap = saliencymap / np.max(saliencymap)

# 提高對比度，進行伽馬變換
saliencymap = np.power(saliencymap, 0.5)
saliencymap = np.round(saliencymap * 255)
saliencymap = saliencymap.astype(np.uint8)
cv2.imshow("saliencymap", saliencymap)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("頻率域濾波 LPFilter")

# 截止頻率
radius = 50
MAX_RADIUS = 100
# 低通濾波類型
lpType = 0
MAX_LPTYPE = 2


# 快速傅里葉變換
def fft2Image4(image):
    # 得到行、列
    r, c = image.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = image
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


# 傅里葉幅度譜
def amplitudeSpectrum(fft2):
    # 求幅度
    real2 = np.power(fft2[:, :, 0], 2.0)
    Imag2 = np.power(fft2[:, :, 1], 2.0)
    amplitude = np.sqrt(real2 + Imag2)
    return amplitude


# 幅度譜的灰度級顯示
def graySpectrum(amplitude):
    # 對比度拉伸
    # cv2.log(amplitude+1.0,amplitude)
    amplitude = np.log(amplitude + 1.0)
    # 歸一化,傅里葉譜的灰度級顯示
    spectrum = np.zeros(amplitude.shape, np.float32)
    cv2.normalize(amplitude, spectrum, 0, 1, cv2.NORM_MINMAX)
    return spectrum


# 構建低通濾波器
def createLPFilter(shape, center, radius, lpType=0, n=2):
    # 濾波器的高和寬
    rows, cols = shape[:2]
    r, c = np.mgrid[0:rows:1, 0:cols:1]
    c -= center[0]
    r -= center[1]
    d = np.power(c, 2.0) + np.power(r, 2.0)
    # 構造低通濾波器
    lpFilter = np.zeros(shape, np.float32)
    if radius <= 0:
        return lpFilter
    if lpType == 0:  # 理想低通濾波
        lpFilter = np.copy(d)
        lpFilter[lpFilter < pow(radius, 2.0)] = 1
        lpFilter[lpFilter >= pow(radius, 2.0)] = 0
    elif lpType == 1:  # 巴特沃斯低通濾波
        lpFilter = 1.0 / (1.0 + np.power(np.sqrt(d) / radius, 2 * n))
    elif lpType == 2:  # 高斯低通濾波
        lpFilter = np.exp(-d / (2.0 * pow(radius, 2.0)))
    return lpFilter


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式
cv2.imshow("image", image)

# 第二步：每一元素乘以 (-1)^(r+c)
fimage = np.zeros(image.shape, np.float32)
for r in range(image.shape[0]):
    for c in range(image.shape[1]):
        if (r + c) % 2:
            fimage[r][c] = -1 * image[r][c]
        else:
            fimage[r][c] = image[r][c]

# 第三和四步：補零和快速傅里葉變換
fImagefft2 = fft2Image4(fimage)

# 傅里葉譜
amplitude = amplitudeSpectrum(fImagefft2)

# 傅里葉譜的灰度級顯示
spectrum = graySpectrum(amplitude)
cv2.imshow("originalSpectrum", spectrum)

# 找到傅里葉譜最大值的位置
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(amplitude)

# 低通傅里葉譜灰度級的顯示窗口
cv2.namedWindow("lpFilterSpectrum", 1)


def nothing(*arg):
    pass


# 調節低通濾波類型
cv2.createTrackbar("lpType", "lpFilterSpectrum", lpType, MAX_LPTYPE, nothing)
# 調節截斷頻率
cv2.createTrackbar("radius", "lpFilterSpectrum", radius, MAX_RADIUS, nothing)
# 低通濾波結果
result = np.zeros(spectrum.shape, np.float32)
while True:
    # 得到當前的截斷頻率、低通濾波類型
    radius = cv2.getTrackbarPos("radius", "lpFilterSpectrum")
    lpType = cv2.getTrackbarPos("lpType", "lpFilterSpectrum")
    # 第五步：構建低通濾波器
    lpFilter = createLPFilter(spectrum.shape, maxLoc, radius, lpType)
    # 第六步：低通濾波器和快速傅里葉變換對應位置相乘（點乘）
    rows, cols = spectrum.shape[:2]
    fImagefft2_lpFilter = np.zeros(fImagefft2.shape, fImagefft2.dtype)
    for i in range(2):
        fImagefft2_lpFilter[:rows, :cols, i] = fImagefft2[:rows, :cols, i] * lpFilter
    # 低通傅里葉變換的傅里葉譜
    lp_amplitude = amplitudeSpectrum(fImagefft2_lpFilter)
    # 顯示低通濾波後的傅里葉譜的灰度級
    lp_spectrum = graySpectrum(lp_amplitude)
    cv2.imshow("lpFilterSpectrum", lp_spectrum)
    # 第七和八步：對低通傅里葉變換執行傅里葉逆變換,并只取實部
    cv2.dft(
        fImagefft2_lpFilter,
        result,
        cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE,
    )
    # 第九步：乘以(-1)^(r+c)
    for r in range(rows):
        for c in range(cols):
            if (r + c) % 2:
                result[r][c] *= -1
    # 第十步：數據類型轉換,并進行灰度級顯示，截取左上角，大小和輸入圖像相等
    for r in range(rows):
        for c in range(cols):
            if result[r][c] < 0:
                result[r][c] = 0
            elif result[r][c] > 255:
                result[r][c] = 255
    lpResult = result.astype(np.uint8)
    lpResult = lpResult[: image.shape[0], : image.shape[1]]
    cv2.imshow("LPFilter", lpResult)

    k = cv2.waitKey(5)
    if k == ESC:
        break
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("頻率域濾波 HomomorphicFilter")


# 快速傅里葉變換
def fft2Image5(image):
    # 得到行、列
    r, c = image.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = image
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


# 傅里葉幅度譜
def amplitudeSpectrum(fft2):
    # 求幅度
    real2 = np.power(fft2[:, :, 0], 2.0)
    Imag2 = np.power(fft2[:, :, 1], 2.0)
    amplitude = np.sqrt(real2 + Imag2)
    return amplitude


I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式
cv2.imshow("I", I)

# 第二步：取對數
lI = np.log(I + 1.0)
lI = lI.astype(np.float32)

# 第三步：每一元素乘以 (-1)^(r+c)
fI = np.copy(lI)
for r in range(I.shape[0]):
    for c in range(I.shape[1]):
        if (r + c) % 2:
            fI[r][c] = -1 * fI[r][c]

# 第四、五步：補零和快速傅里葉變換
fft2 = fft2Image5(fI)

# 第六步：構造高頻增強濾波器（ high-emphasis Filter）
# 找到傅里葉譜中的最大值的位置
amplitude = amplitudeSpectrum(fft2)
minValue, maxValue, minLoc, maxLoc = cv2.minMaxLoc(amplitude)

# 濾波器的高和寬
rows, cols = fft2.shape[:2]
r, c = np.mgrid[0:rows:1, 0:cols:1]
c -= maxLoc[0]
r -= maxLoc[1]
d = np.power(c, 2.0) + np.power(r, 2.0)
high, low, k, radius = 2.5, 0.5, 1, 300
heFilter = (high - low) * (1 - np.exp(-k * d / (2.0 * pow(radius, 2.0)))) + low

# 第七步：快速傅里葉變換與高頻增強濾波器的點乘
fft2Filter = np.zeros(fft2.shape, fft2.dtype)
for i in range(2):
    fft2Filter[:rows, :cols, i] = fft2[:rows, :cols, i] * heFilter

# 第八、九步：高頻增強傅里葉變換執行傅里葉逆變換,并只取實部
X_DFT = cv2.dft(fft2Filter, flags=cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)

# 第十步：裁剪，和輸入圖像的尺寸一樣
ifI = np.copy(X_DFT[: I.shape[0], : I.shape[1]])

# 第十一步：每一元素乘以 (-1)^(r+c)
for i in range(ifI.shape[0]):
    for j in range(ifI.shape[1]):
        if (i + j) % 2:
            ifI[i][j] = -1 * ifI[i][j]
# 第十二步：取指數
eifI = np.exp(ifI) - 1

# 第十三步：歸一化，并進行數據類型轉換
eifI = (eifI - np.min(eifI)) / (np.max(eifI) - np.min(eifI))
eifI = 255 * eifI
eifI = eifI.astype(np.uint8)

cv2.imshow("homomorphicFilter", eifI)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("np.fft 02 合成時域訊號")
print("一維 fft b")
# FFT 頻域訊號處理

NNNN = 100

# 三角波
x, y = triangle_wave(NNNN)
fy = np.fft.fft(y) / NNNN  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
ify = np.fft.ifft(fy)  # 一維 ifft

plt.figure(figsize=(12, 8))

# 繪制三角波的FFT的前20項的振幅，由於不含索引為偶數的值均為0， 因此取
# log之後無窮小，無法繪圖，用np.clip函數設定陣列值的上下限，確保繪圖正確
plt.subplot(4,4,1)
plt.plot(x, y, label="原資料")

plt.subplot(4,4,2)
plt.scatter(fy.real, fy.imag, s=100, label="FFT")

plt.subplot(4,4,3)
plt.plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
plt.xlabel("頻率視窗(frequency bin)")
plt.ylabel("幅值(dB)")

plt.subplot(4,4,4)
plt.plot(ify.real, label="IFFT")

# 正弦波
x, y = sine_wave1(NNNN)
fy = np.fft.fft(y) / NNNN  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
ify = np.fft.ifft(fy)  # 一維 ifft

# 繪制三角波的FFT的前20項的振幅，由於不含索引為偶數的值均為0， 因此取
# log之後無窮小，無法繪圖，用np.clip函數設定陣列值的上下限，確保繪圖正確
plt.subplot(4,4,5)
plt.plot(x, y, label="原資料")

plt.subplot(4,4,6)
plt.scatter(fy.real, fy.imag, s=100, label="FFT")

plt.subplot(4,4,7)
plt.plot(np.clip(20 * np.log10(np.abs(fy)), -120, 120), "o")
plt.xlabel("頻率視窗(frequency bin)")
plt.ylabel("幅值(dB)")

plt.subplot(4,4,8)
plt.plot(ify.real, label="IFFT")

# 方波
x, y = square_wave(NNNN)
fy = np.fft.fft(y) / NNNN  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
ify = np.fft.ifft(fy)  # 一維 ifft

plt.subplot(4,4,9)
plt.plot(y, label="原始方波", linewidth=2)

plt.subplot(4,4,10)

plt.scatter(fy.real, fy.imag, s=100, label="FFT")

plt.subplot(4,4,11)
plt.plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
plt.xlabel("頻率視窗(frequency bin)")
plt.ylabel("幅值(dB)")

plt.subplot(4,4,12)
plt.plot(ify.real, label="IFFT")

# 正弦波
x, y = sine_wave2(NNNN)
fy = np.fft.fft(y) / NNNN  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
ify = np.fft.ifft(fy)  # 一維 ifft

plt.subplot(4,4,13)
plt.plot(x, y, label="原資料")

plt.subplot(4,4,14)
plt.scatter(fy.real, fy.imag, s=100, label="FFT")

plt.subplot(4,4,15)
plt.plot(np.clip(20 * np.log10(np.abs(fy)), -120, 120), "o")
plt.xlabel("頻率視窗(frequency bin)")
plt.ylabel("幅值(dB)")

plt.subplot(4,4,16)
plt.plot(ify.real, label="IFFT")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一維 fft a")

N = 100  # 取樣點數, 精細程度
x, y = sine_wave2(N)

fy = np.fft.fft(y)  # 一維 fft
abs_y = np.abs(fy)  # 取復數的絕對值，即復數的模(雙邊頻譜)

plt.subplot(131)
plt.plot(y)
plt.title("原始波形")

plt.subplot(132)
plt.plot(fy, "black")
plt.title("fy")

plt.subplot(133)
plt.plot(abs_y, "r")
plt.title("abs_y")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("一維 fft c")

N = 8
x = np.arange(0, 2 * np.pi, 2 * np.pi / N)
y = np.sin(x)
# 做FFT, 除以FFT的長度
fy = np.fft.fft(y) / len(y)  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
print(np.array_str(fy, suppress_small=True))  # 壓縮顯示法

x = np.arange(0, 2 * np.pi, 2 * np.pi / 128)
y = 0.3 * np.cos(x) + 0.5 * np.cos(2 * x + np.pi / 4) + 0.8 * np.cos(3 * x - np.pi / 3)
# 做FFT, 除以FFT的長度
fy = np.fft.fft(y) / len(y)  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度
print(np.array_str(fy[:4], suppress_small=True))  # 壓縮顯示法
print(np.abs(fy[1]), np.rad2deg(np.angle(fy[1])))  # 周期為128取樣點的余弦波的振幅和相位
print(np.abs(fy[2]), np.rad2deg(np.angle(fy[2])))  # 周期為64取樣點的余弦波的振幅和相位
print(np.abs(fy[3]), np.rad2deg(np.angle(fy[3])))  # 周期為42.667取樣點的余弦波的振幅和相位

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
'''
print("np.fft 04 觀察訊號的頻譜")

# 156.25Hz和234.375Hz的波形和頻譜
f1 = 156.25  # Hz
f2 = 234.375  # Hz
sampling_rate, NNNN = 8000, 512
T = np.arange(0, 1.0, 1.0 / sampling_rate)
y = np.sin(2 * np.pi * f1 * T) + 2 * np.sin(2 * np.pi * f2 * T)

plt.figure(figsize=(8, 8))

XS = y[:NNNN]
xf = np.fft.rfft(XS) / NNNN
freqs = np.linspace(0, sampling_rate / 2, NNNN // 2 + 1)
xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

plt.subplot(411)
plt.plot(T[:NNNN], XS)
plt.xlabel("時間(秒)")

plt.subplot(412)
plt.plot(freqs, xfp)
plt.xlabel("頻率(Hz)")
plt.xlim(0, 1000)  # 設定 x 軸邊界
plt.subplots_adjust(hspace=0.4)

print("------------------------------")  # 30個

# 非完整周期（200Hz和300Hz）的正弦波經由FFT變換之後出現頻譜洩漏
y = np.sin(2 * np.pi * 200 * T) + 2 * np.sin(2 * np.pi * 300 * T)

XS = y[:NNNN]
xf = np.fft.rfft(XS) / NNNN
freqs = np.linspace(0, sampling_rate / 2, NNNN // 2 + 1)
xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

plt.subplot(413)
plt.plot(T[:NNNN], XS)
plt.xlabel("時間(秒)")

plt.subplot(414)
plt.plot(freqs, xfp)
plt.xlabel("頻率(Hz)")
plt.xlim(0, 1000)  # 設定 x 軸邊界
plt.subplots_adjust(hspace=0.4)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("np.fft 05")

plt.figure(figsize=(6, 6))

# 50Hz正弦波的512點FFT所計算的頻譜的實際波形
plt.subplot(311)
T = np.arange(0, 1.0, 1.0 / 8000)
y = np.sin(2 * np.pi * 50 * T)[:512]
plt.plot(np.hstack([y, y, y]))

plt.subplot(312)


plt.subplot(313)
T = np.arange(0, 1.0, 1.0 / 8000)
y = np.sin(2 * np.pi * 50 * T)[:512]
plt.plot(np.hstack([y, y, y]))

show()

print("------------------------------")  # 30個

sampling_rate, NNNN = 8000, 512
T = np.arange(0, 1.0, 1.0 / sampling_rate)
y = np.sin(2 * np.pi * 200 * T) + 2 * np.sin(2 * np.pi * 300 * T)

XS = y[:NNNN]

xf = np.fft.rfft(XS) / NNNN

freqs = np.linspace(0, sampling_rate // 2, NNNN // 2 + 1)

xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))

plt.figure(figsize=(8, 4))
plt.plot(freqs, xfp, label="矩形窗")

plt.xlabel("頻率(Hz)")

a = plt.axes([0.4, 0.2, 0.4, 0.4])
a.plot(freqs, xfp, label="矩形窗")

a.set_xlim(100, 400)
a.set_ylim(-40, 0)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("np.fft 10 精確測量訊號頻率")


def make_wave(amp, freq, phase, tend, rate):
    period = 1.0 / rate
    t = np.arange(0, tend, period)
    x = np.zeros_like(t)
    for a, f, p in zip(amp, freq, phase):
        x += a * np.sin(2 * np.pi * f * t + p)
    return t, x


RATE = 8000
t, x = make_wave([1, 2, 0.5], [44, 150, 330], [1, 1.4, 1.8], 0.3, RATE)
x += np.random.randn(len(x))

FFT_SIZE = 1024
spect1 = np.fft.rfft(x[:FFT_SIZE] * np.hanning(FFT_SIZE))
freqs = np.fft.fftfreq(FFT_SIZE, 1.0 / RATE)

bin_width = freqs[1] - freqs[0]

amp_spect1 = np.abs(spect1)
(loc,) = scipy.signal.argrelmax(amp_spect1, order=3)
mask = amp_spect1[loc] > amp_spect1.mean() * 3
loc = loc[mask]
peak_freqs = freqs[loc]
print("bin width:", bin_width)
print("Peak Frequencies:", peak_freqs)

# bin width: 7.8125
# Peak Frequencies: [  46.875  148.438  328.125]

COUNT = FFT_SIZE // 4
dt = COUNT / 8000.0

spect2 = np.fft.rfft(x[COUNT : COUNT + FFT_SIZE] * np.hanning(FFT_SIZE))

phase1 = np.angle(spect1[loc])
phase2 = np.angle(spect2[loc])

phase_delta = phase2 - phase1
print(phase_delta)

# [ 2.595 -1.29  -2.899]

max_n = (peak_freqs.max() + 3 * bin_width) * dt
n = np.arange(max_n)

possible_freqs = (phase_delta + 2 * np.pi * n[:, None]) / (2 * np.pi * dt)

idx = np.argmin(np.abs(peak_freqs - possible_freqs), axis=0)
peak_freqs2 = possible_freqs[idx, np.arange(len(peak_freqs))]
print("Peak Frequencies:", peak_freqs2)

# Peak Frequencies: [  44.155  149.833  329.33 ]

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("小波變換")

import pywt

x, y = sine_wave1(NNNN)

cA, cD = pywt.dwt(y, "db2")

cD = np.zeros(len(cD))
y_new = pywt.idwt(cA, cD, "db2")

plt.plot(y, "r", lw=10)
plt.plot(y_new, "g", lw=3)

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pywt

# 获取数据
ecg = pywt.data.ecg()  # 生成心电信号
index = []
data = []
coeffs = []

for i in range(len(ecg) - 1):
    X = float(i)
    Y = float(ecg[i])
    index.append(X)
    data.append(Y)
# 创建小波对象并定义参数
w = pywt.Wavelet("db8")  # 选用Daubechies8小波
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
print("maximum level is" + str(maxlev))
threshold = 0  # 阈值过滤

# 分解成小波分量，到选定的层次:
coeffs = pywt.wavedec(data, "db8", level=maxlev)  # 将信号进行小波分解
for i in range(1, len(coeffs)):
    coeffs[i] = pywt.threshold(coeffs[i], threshold * max(coeffs[i]))
datarec = pywt.waverec(coeffs, "db8")  # 将信号进行小波重构
mintime = 0
maxtime = mintime + len(data)
print(mintime, maxtime)

plt.subplot(311)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("微伏(uV)")
plt.title("原始信号")
plt.subplot(312)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("微伏(uV)")
plt.title("利用小波技术去噪信号")
plt.subplot(313)
plt.plot(index[mintime:maxtime], data[mintime:maxtime] - datarec[mintime:maxtime])
plt.xlabel("时间(s)")
plt.ylabel("误差(uV)")

plt.tight_layout()
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


"""
【numpy】几种fft函数的使用
fft
输入实数samples，如果输入的sample是带虚数部分的话，虚数部分会被默认删除。
"""

t = np.arange(12)
b = np.sin(t)
print(b)
print("sum(b)=", np.sum(b))

s = np.fft.fft(b)
print(s)

"""
rfft
rfft其实就是对fft的结果输出做了省略。
针对刚刚提到的共轭特性，其实输出结果是要保留(N+1)//2个结果就可以了。
"""

t = np.arange(12)
b = np.sin(t)
print(b)
print("sum(b)=", np.sum(b))

s = np.fft.fft(b)
print("fft result:", s)

s = np.fft.rfft(b)
print("rfft result:", s)

"""
fftfreq

返回fft的频率节点

上面的fft和rfft将时域数据转为频域，得到的数据的bin是哪些范围？
可以通过fftfreq来获取

第一个参数n是时域数据的数据个数，第二个参数d是表示每一个bin的尺度。一般是1/sample_rate
"""

t = np.arange(12)
b = np.sin(t)
print(b)
print("sum(b)=", np.sum(b))

s = np.fft.fft(b)
print("fft result:", s)

s = np.fft.rfft(b)
print("rfft result:", s)

s = np.fft.fftfreq(12, d=1 / 8000)
print(s.shape)
print(s)

# ifft是逆向fft操作

t = np.arange(12)
b = np.sin(t)
print(b)

s = np.fft.fft(b)
# print(s)

y = np.fft.ifft(s)
print("restore:", y)

"""
它的结果虽然也是复数，但是在实数部分，可以看到，就是结果；

所以也可以直接输出实数部分np.fft.ifft(s).real
"""

"""
irfft

irfft是配合rfft使用的； 上面的例子可以看到，如果信号长度是n, 那么fft的输出结果的长度也是n；
但是rfft的结果是n//2+1;

irfft匹配的是rfft，所以它的参数长度与ifft是不同的；两者也不可混用。
"""

t = np.arange(12)
b = np.sin(t)
print(b)

s = np.fft.rfft(b)
# print(s)

y = np.fft.irfft(s)
print("restore:", y)

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


# 取四捨五入到小數點以下2位
spectrum = np.around(spectrum, decimals=2)


print("------------------------------")  # 30個


# %fig=（左上）用fft2()計算的頻域訊號，
# （中上）使用fftshift()移位之後的頻域訊號，
# （其它）各個領域所對應的時域訊號


# 沒有用的檔案

image = cv2.imread("data/fft/shape1.jpg", cv2.IMREAD_GRAYSCALE)  # 灰度模式
image = cv2.imread("data/fft/shape2.jpg", cv2.IMREAD_GRAYSCALE)  # 灰度模式
"data/fft/jk.jpg"
"data/fft/snow.jpg"


np.fft.fft2(image)


image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式
image = cv2.imread(filename, 0)  # 0:灰度模式 cv2.IMREAD_GRAYSCALE


# plt.figure(figsize=(8, 6))

plt.axis("off")

ifshift = np.fft.ifftshift(fshift)  # 逆傅立葉變換  # 0 頻率頻率移回左上角

print("------------------------------------------------------------")  # 60個

tmp = np.linspace(1, 2, 4)
print(tmp)
print(np.array_str(tmp, suppress_small=True))  # 壓縮顯示法

print("------------------------------------------------------------")  # 60個

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)  # 灰度模式

plt.subplot(121)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

image = image[::3, ::2]  # j每隔3, i每隔2

plt.subplot(122)
plt.imshow(image, cmap="gray")  # 灰階顯示原圖
plt.title("原圖")

show()

print(y[::3, ::3])
print("-----")
print(y[::4, ::4])  # 虛數為零


# np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120)


print("------------------------------")  # 30個

plt.axis("off")


"""
對 y 做 一維fft
fy = fft(y)
直流部分 DC = fy[0].real  # 直流部分
對 fy做 一維ifft
ify = ifft(fy)

# np.allclose():檢查兩個數組是否每個元素都相似, 預設誤差在1e-05內
cc = np.allclose(y, ify)  # 和原始訊號進行比較
print(cc)

"""

plt.subplots_adjust(bottom=0.15)
plt.subplots_adjust(bottom=0.15)


# 白色噪聲的頻譜接近水平直線（注意Y軸的範圍）
x = np.random.randn(10000)
plt.plot(x)
show()

print("------------------------------------------------------------")  # 60個


fy = np.fft.fft(y)  # np.array 做 fft  # 一維 fft
ify = np.fft.ifft(fy)  # 一維 ifft
conv1 = np.real(ify)  # 取實部

plt.subplot(212)
plt.plot(y, "r")
plt.plot(conv1 - 0.5, "g")  # 爲看清楚，將顯示區域下拉0.5


