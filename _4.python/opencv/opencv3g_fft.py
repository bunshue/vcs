"""

FFT


np 傅立葉變換
np.fft.fft2()



"""

import cv2
import pylab as pl

ESC = 27

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


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"

print("------------------------------------------------------------")  # 60個


# 二維離散傅立葉變換

x = np.random.rand(8, 8)
print(x)

plt.imshow(x, cmap="gray")
show()

X = np.fft.fft2(x)
print(np.allclose(X[1:, 1:], X[7:0:-1, 7:0:-1].conj()))  # 共軛復數
print(X[::4, ::4])  # 虛數為零

"""
True
[[ 31.48765415+0.j  -2.80563949+0.j]
 [  0.75758598+0.j  -0.53147589+0.j]]
"""

x2 = np.fft.ifft2(X)  # 將頻域訊號轉換回空域訊號
print(x2)
cc = np.allclose(x, x2)  # 和原始訊號進行比較
print(cc)
# True

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
X = np.zeros((N, N))

cx, cy = N // 2, N // 2
print(cx, cy)

# X[cx-1:cx+2, cy-1:cy+2] = 1
X[cx, cy] = 1
print(X)

# X = cv2.imread(filename, 0) # 使用圖片資料
# X = sinc2d # 使用 sinc2d

print("------------------------------")  # 30個

# np 傅立葉變換
X_FFT = np.fft.fft2(X)
FFT_SHIFT = np.fft.fftshift(X_FFT)
print(FFT_SHIFT)

MAGNITUDE_SPECTRUM = 20 * np.log(np.abs(FFT_SHIFT))

print(MAGNITUDE_SPECTRUM)

plt.figure(figsize=(8, 6))
plt.subplot(121)
plt.title("原圖")
plt.imshow(X, cmap="gray")

plt.subplot(122)
plt.title("fftshift")
plt.imshow(MAGNITUDE_SPECTRUM, cmap="gray")

plt.suptitle("numpy 傅立葉")
show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 檔案 => cv2影像
image = cv2.imread(filename, 0)  # 0:灰度模式 cv2.IMREAD_GRAYSCALE
f = np.fft.fft2(image)
fshift = np.fft.fftshift(f)
s1 = np.log(np.abs(fshift))
# print(f)
# fimage = np.log(np.abs(f))
fimage = np.abs(s1)
print(fimage)

plt.figure(figsize=(8, 6))
plt.subplot(121)
plt.title("原圖")
plt.imshow(image, cmap="gray")

plt.subplot(122)
plt.title("fftshift")
plt.imshow(fimage, cmap="gray")

plt.suptitle("numpy 傅立葉")
show()

print("------------------------------------------------------------")  # 60個

# cv2 傅立葉變換

X = cv2.imread(filename, 0)

X_DFT = cv2.dft(np.float32(X), flags=cv2.DFT_COMPLEX_OUTPUT)
# print(X_DFT)

FFT_SHIFT = np.fft.fftshift(X_DFT)
result = 20 * np.log(cv2.magnitude(FFT_SHIFT[:, :, 0], FFT_SHIFT[:, :, 1]))

plt.figure(figsize=(8, 6))

plt.subplot(121)
plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(result, cmap="gray")
plt.title("fftshift")

plt.suptitle("傅立葉變換")

show()

print("------------------------------------------------------------")  # 60個

# np 逆傅立葉

X = cv2.imread(filename, 0)

X_FFT = np.fft.fft2(X)
FFT_SHIFT = np.fft.fftshift(X_FFT)
FFT_SHIFT_IFFTSHIFT = np.fft.ifftshift(FFT_SHIFT)

FFT_SHIFT_IFFTSHIFT_IFFT2 = np.fft.ifft2(FFT_SHIFT_IFFTSHIFT)

FFT_SHIFT_IFFTSHIFT_IFFT2 = np.abs(FFT_SHIFT_IFFTSHIFT_IFFT2)

plt.figure(figsize=(8, 6))

plt.subplot(121)
plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(FFT_SHIFT_IFFTSHIFT_IFFT2, cmap="gray")
plt.title("FFT_SHIFT_IFFTSHIFT_IFFT2")

plt.suptitle("逆傅立葉")
show()

print("------------------------------------------------------------")  # 60個

# cv2 逆傅立葉變換

X = cv2.imread(filename, 0)

X_DFT = cv2.dft(np.float32(X), flags=cv2.DFT_COMPLEX_OUTPUT)
FFT_SHIFT = np.fft.fftshift(X_DFT)
FFT_SHIFT_IFFTSHIFT = np.fft.ifftshift(FFT_SHIFT)
FFT_SHIFT_IFFTSHIFT_IDFT = cv2.idft(FFT_SHIFT_IFFTSHIFT)
FFT_SHIFT_IFFTSHIFT_IDFT = cv2.magnitude(
    FFT_SHIFT_IFFTSHIFT_IDFT[:, :, 0], FFT_SHIFT_IFFTSHIFT_IDFT[:, :, 1]
)

plt.figure(figsize=(8, 6))

plt.subplot(121)
plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(FFT_SHIFT_IFFTSHIFT_IDFT, cmap="gray")
plt.title("FFT_SHIFT_IFFTSHIFT_IDFT")

plt.suptitle("逆傅立葉變換")
show()

print("------------------------------------------------------------")  # 60個

# 高通濾波

X = cv2.imread(filename, 0)

X_FFT = np.fft.fft2(X)

FFT_SHIFT = np.fft.fftshift(X_FFT)
rows, cols = X.shape
crow, ccol = int(rows / 2), int(cols / 2)
FFT_SHIFT[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 0
FFT_SHIFT_IFFTSHIFT = np.fft.ifftshift(FFT_SHIFT)

FFT_SHIFT_IFFTSHIFT_IFFT2 = np.fft.ifft2(FFT_SHIFT_IFFTSHIFT)
FFT_SHIFT_IFFTSHIFT_IFFT2 = np.abs(FFT_SHIFT_IFFTSHIFT_IFFT2)

plt.figure(figsize=(8, 6))

plt.subplot(121)
plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(FFT_SHIFT_IFFTSHIFT_IFFT2, cmap="gray")
plt.title("FFT_SHIFT_IFFTSHIFT_IFFT2")

plt.suptitle("高通濾波")
show()

print("------------------------------------------------------------")  # 60個

# 低通濾波

X = cv2.imread(filename, 0)

X_DFT = cv2.dft(np.float32(X), flags=cv2.DFT_COMPLEX_OUTPUT)
FFT_SHIFT = np.fft.fftshift(X_DFT)
rows, cols = X.shape
crow, ccol = int(rows / 2), int(cols / 2)
MASK = np.zeros((rows, cols, 2), np.uint8)
# 两个通道，与频谱图像匹配
MASK[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 1
FFT_SHIFT_MASK = FFT_SHIFT * MASK
FFT_SHIFT_MASK_IFFTSHIFT = np.fft.ifftshift(FFT_SHIFT_MASK)
FFT_SHIFT_MASK_IFFTSHIFT_IDFT = cv2.idft(FFT_SHIFT_MASK_IFFTSHIFT)
FFT_SHIFT_MASK_IFFTSHIFT_IDFT = cv2.magnitude(
    FFT_SHIFT_MASK_IFFTSHIFT_IDFT[:, :, 0], FFT_SHIFT_MASK_IFFTSHIFT_IDFT[:, :, 1]
)

plt.figure(figsize=(8, 6))

plt.subplot(121)
plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(FFT_SHIFT_MASK_IFFTSHIFT_IDFT, cmap="gray")
plt.title("FFT_SHIFT_MASK_IFFTSHIFT_IDFT")

plt.suptitle("低通濾波")
show()

print("------------------------------------------------------------")  # 60個

print("MAGNITUDE_SPECTRUM")

X = cv2.imread(filename, 0)

X_DFT = cv2.dft(np.float32(X), flags=cv2.DFT_COMPLEX_OUTPUT)

FFT_SHIFT = np.fft.fftshift(X_DFT)
MAGNITUDE_SPECTRUM = 20 * np.log(cv2.magnitude(FFT_SHIFT[:, :, 0], FFT_SHIFT[:, :, 1]))

plt.figure(figsize=(8, 6))

plt.subplot(121), plt.imshow(X, cmap="gray")
plt.title("原圖")

plt.subplot(122)
plt.imshow(MAGNITUDE_SPECTRUM, cmap="gray")
plt.title("級頻譜 MAGNITUDE_SPECTRUM")

show()

print("------------------------------------------------------------")  # 60個

print("傅里葉變換 fft2")


# 快速傅里葉變換
def fft2Image(src):
    # 得到行、列
    r, c = src.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
    # 快速傅里葉變換
    cv2.dft(fft2, fft2, cv2.DFT_COMPLEX_OUTPUT)
    return fft2


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# 計算圖像矩陣的快速傅里葉變換
fft2 = fft2Image(image)
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
def fft2Image(src):
    # 得到行、列
    r, c = src.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
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


# 第一步：讀入圖像
# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# 顯示原圖
cv2.imshow("image", image)
# 快速傅里葉變換
fft2 = fft2Image(image)
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
imagefft2 = fft2Image(fimage)
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
def fft2Image(src):
    # 得到行、列
    r, c = src.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
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


# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

# 第一步：計算圖像的快速傅里葉變換
fft2 = fft2Image(image)

# 第二步：計算傅里葉幅度譜的灰度級
# 求幅度譜
amplitude = amplitudeSpectrum(fft2)
# 幅度譜的灰度級
logAmplitude = graySpectrum(amplitude)

# 第三步：計算相位
phase = phaseSpectrum(fft2)
# 余弦譜（用於計算實部）
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
# 合并實部和虛部
com = np.zeros((real.shape[0], real.shape[1], 2), np.float32)
com[:, :, 0] = real
com[:, :, 1] = imaginary
# 逆變換
ifft2 = np.zeros(com.shape, np.float32)
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
cv2.dft(I, FT_I, cv2.DFT_COMPLEX_OUTPUT)
# kernel 的傅里葉變換
FT_kernel = np.zeros((kernel.shape[0], kernel.shape[1], 2), np.float64)
cv2.dft(kernel, FT_kernel, cv2.DFT_COMPLEX_OUTPUT)
# 傅里葉變換
fft2 = np.zeros((confull.shape[0], confull.shape[1]), np.float64)
# 對 I 進行右側和下側補 0
I_Padded = np.zeros(
    (I.shape[0] + kernel.shape[0] - 1, I.shape[1] + kernel.shape[1] - 1), np.float64
)
I_Padded[: I.shape[0], : I.shape[1]] = I
FT_I_Padded = np.zeros((I_Padded.shape[0], I_Padded.shape[1], 2), np.float64)
cv2.dft(I_Padded, FT_I_Padded, cv2.DFT_COMPLEX_OUTPUT)
# 對 kernel 進行右側和下側補 0
kernel_Padded = np.zeros(
    (I.shape[0] + kernel.shape[0] - 1, I.shape[1] + kernel.shape[1] - 1), np.float64
)
kernel_Padded[: kernel.shape[0], : kernel.shape[1]] = kernel
FT_kernel_Padded = np.zeros(
    (kernel_Padded.shape[0], kernel_Padded.shape[1], 2), np.float64
)
cv2.dft(kernel_Padded, FT_kernel_Padded, cv2.DFT_COMPLEX_OUTPUT)
# 兩個傅里葉變換相乘
FT_Ikernel = cv2.mulSpectrums(FT_I_Padded, FT_kernel_Padded, cv2.DFT_ROWS)
# 利用傅里葉變換求全 ( full ) 卷積
ifft2 = np.zeros(FT_Ikernel.shape[:2], np.float64)
cv2.dft(FT_Ikernel, ifft2, cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
print(np.max(ifft2 - confull))

# 全卷積進行傅里葉變換等於兩個傅里葉變換的點乘
FT_confull = np.zeros((confull.shape[0], confull.shape[1], 2), np.float64)
cv2.dft(confull, FT_confull, cv2.DFT_COMPLEX_OUTPUT)
print(FT_confull - FT_Ikernel)
print(np.max(FT_confull - FT_Ikernel))

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

print("頻率域濾波 LPFilter")

# 截止頻率
radius = 50
MAX_RADIUS = 100
# 低通濾波類型
lpType = 0
MAX_LPTYPE = 2


# 快速傅里葉變換
def fft2Image(src):
    # 得到行、列
    r, c = src.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
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


# 第一步：讀入圖像
# 檔案 => cv2影像
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
# 顯示原圖
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
fImagefft2 = fft2Image(fimage)
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

print("頻率域濾波 HomomorphicFilter")


# 快速傅里葉變換
def fft2Image(src):
    # 得到行、列
    r, c = src.shape[:2]
    # 得到快速傅里葉變換最優擴充
    rPadded = cv2.getOptimalDFTSize(r)
    cPadded = cv2.getOptimalDFTSize(c)
    # 邊緣擴充，下邊緣和右邊緣擴充值為零
    fft2 = np.zeros((rPadded, cPadded, 2), np.float32)
    fft2[:r, :c, 0] = src
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


# 第一步：讀入圖像
# 檔案 => cv2影像
I = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
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
fft2 = fft2Image(fI)
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
ifft2 = cv2.dft(fft2Filter, flags=cv2.DFT_REAL_OUTPUT + cv2.DFT_INVERSE + cv2.DFT_SCALE)
# 第十步：裁剪，和輸入圖像的尺寸一樣
ifI = np.copy(ifft2[: I.shape[0], : I.shape[1]])
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

print("image_fft")

Fs = 1200  # 采樣頻率
Ts = 1 / Fs  # 采樣區間
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
    num="",
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

show()

print("------------------------------------------------------------")  # 60個

print("image_ftt2")

# 檔案 => cv2影像
image = plt.imread("data/castle3.jpg")

# 根據公式轉成灰度圖
image = 0.2126 * image[:, :, 0] + 0.7152 * image[:, :, 1] + 0.0722 * image[:, :, 2]

# 繪製結果
fig = plt.figure(
    num="",
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
plt.title("原圖")

# 進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)

plt.subplot(232)
plt.imshow(np.abs(fft2), "gray")
plt.title("二維傅里葉變換")

# 將圖像變換的原點移動到頻域矩形的中心，并顯示效果
FFT_SHIFT = np.fft.fftshift(fft2)

plt.subplot(233)
plt.imshow(np.abs(FFT_SHIFT), "gray")
plt.title("頻域矩形的中心")

# 對傅立葉變換的結果進行對數變換，并顯示效果
log_fft2 = np.log(1 + np.abs(fft2))

plt.subplot(235)
plt.imshow(log_fft2, "gray")
plt.title("傅立葉變換對數變換")

# 對中心化后的結果進行對數變換，并顯示結果
log_FFT_SHIFT = np.log(1 + np.abs(FFT_SHIFT))

plt.subplot(236)
plt.imshow(log_FFT_SHIFT, "gray")
plt.title("中心化的對數變化")

show()

print("------------------------------------------------------------")  # 60個

""" 跑不出來 skip
print("image_dft2")

PI = 3.141591265

# 檔案 => cv2影像
image = plt.imread('data/castle3.jpg')

#根據公式轉成灰度圖
image = 0.2126 * image[:,:,0] + 0.7152 * image[:,:,1] + 0.0722 * image[:,:,2]

#顯示原圖
plt.subplot(131)
plt.imshow(image,'gray')
plt.title('原圖')

#進行傅立葉變換，并顯示結果
fft2 = np.fft.fft2(image)
log_fft2 = np.log(1 + np.abs(fft2))

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

N = 256
X = cv2.imread("data/lena.jpg", cv2.IMREAD_GRAYSCALE)
X = cv2.resize(X, (N, N))
X_freq = np.fft.fft2(X)
X_mag = np.log10(np.abs(X_freq))
FFT_SHIFT = np.fft.fftshift(X_mag)

rects = [
    (80, 125, 85, 130),
    (90, 90, 95, 95),
    (150, 10, 250, 250),
    (110, 110, 146, 146),
]

"""
    scpy2.opencv.fft2d_demo：示範二維離散傅立葉變換，
    使用者在左側的頻域模值圖形上用滑鼠繪制隱藏區域，
    右側的圖形為頻域訊號經由隱藏處理之後所轉換成的空域訊號。
"""

# %fig=(左上)用fft2()計算的頻域訊號，(中上)使用fftshift()移位之後的頻域訊號，(其它)各個領域所對應的空域訊號
filtered_results = []
for i, (x0, y0, x1, y1) in enumerate(rects):
    MASK = np.zeros((N, N), dtype=np.bool)
    MASK[x0 : x1 + 1, y0 : y1 + 1] = True
    MASK[N - x1 : N - x0 + 1, N - y1 : N - y0 + 1] = True
    MASK = np.fft.fftshift(MASK)
    X_freq2 = X_freq * MASK
    X_filtered = np.fft.ifft2(X_freq).real
    filtered_results.append(X_filtered)

fig, axes = pl.subplots(2, 3, figsize=(9, 6))
axes = axes.ravel()
axes[0].imshow(X_mag, cmap=pl.cm.gray)
axes[1].imshow(FFT_SHIFT, cmap=pl.cm.gray)

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

print("傅里葉變換")


# 將頻域數據轉換成時序數據
# bins爲頻域數據，n設置使用前多少個頻域數據，loop設置生成數據的長度
def fft_combine(bins, n, loops=1):
    length = int(len(bins) * loops)
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(bins[:n]):
        if k != 0:
            p *= 2  # 除去直流成分之外, 其餘的係數都乘2
        data += np.real(p) * np.cos(k * index)  # 餘弦成分的係數爲實數部分
        data -= np.imag(p) * np.sin(k * index)  # 正弦成分的係數爲負的虛數部分
    return index, data


data = pd.read_csv("data/AirPassengers.csv")
ts = data["#Passengers"]

# 平穩化
ts_log = np.log(ts)
ts_diff = ts_log.diff(1)  # 差分
ts_diff = ts_diff.dropna()  # 去除空數據
fy = np.fft.fft(ts_diff)
print(fy[:10])  # 顯示前10個頻域數據
conv1 = np.real(np.fft.ifft(fy))  # 逆變換
index, conv2 = fft_combine(fy / len(ts_diff), int(len(fy) / 2 - 1), 1.3)  # 只關心一半數據
plt.plot(ts_diff, "r")
plt.plot(conv1 - 0.5, "g")  # 爲看清楚，將顯示區域下拉0.5
plt.plot(conv2 - 1, "b")

show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


# 取四捨五入到小數點以下2位
MAGNITUDE_SPECTRUM = np.around(MAGNITUDE_SPECTRUM, decimals=2)


print("------------------------------")  # 30個


# %fig=（左上）用fft2()計算的頻域訊號，
# （中上）使用fftshift()移位之後的頻域訊號，
# （其它）各個領域所對應的空域訊號
