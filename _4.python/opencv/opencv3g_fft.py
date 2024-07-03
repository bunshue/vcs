"""

FFT



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
"""
#numpy 傅立葉

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20 * np.log(np.abs(fshift))

plt.figure('傅立葉', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(img, cmap = 'gray')

plt.subplot(122)
plt.title('fftshift')
plt.imshow(magnitude_spectrum, cmap = 'gray')

plt.suptitle('numpy 傅立葉')
plt.show()
"""
print("------------------------------------------------------------")  # 60個

# 逆傅立葉

img = cv2.imread("images/boat.bmp", 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
# print(iimg)
iimg = np.abs(iimg)
# print(iimg)

plt.figure("逆傅立葉", figsize=(16, 12))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("original")

plt.subplot(122)
plt.imshow(iimg, cmap="gray")
plt.title("iimg")

plt.suptitle("逆傅立葉")
plt.show()

print("------------------------------------------------------------")  # 60個

# 高通濾波

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
img = cv2.imread(filename, 0)

f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
fshift[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 0
ishift = np.fft.ifftshift(fshift)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

plt.figure("高通濾波", figsize=(16, 12))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("original")

plt.subplot(122)
plt.imshow(iimg, cmap="gray")
plt.title("iimg")

plt.suptitle("高通濾波")
plt.show()

print("------------------------------------------------------------")  # 60個

# 傅立葉變換

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
img = cv2.imread(filename, 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
result = 20 * np.log(cv2.magnitude(dftShift[:, :, 0], dftShift[:, :, 1]))

plt.figure("傅立葉變換", figsize=(16, 12))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("original")

plt.subplot(122)
plt.imshow(result, cmap="gray")
plt.title("result")

plt.suptitle("傅立葉變換")

plt.show()
# print(dft)

print("------------------------------------------------------------")  # 60個

# 逆傅立葉變換

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
img = cv2.imread(filename, 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
ishift = np.fft.ifftshift(dftShift)
iImg = cv2.idft(ishift)
iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])

plt.figure("逆傅立葉變換", figsize=(16, 12))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("original")

plt.subplot(122)
plt.imshow(iImg, cmap="gray")
plt.title("inverse")

plt.suptitle("逆傅立葉變換")
plt.show()

print("------------------------------------------------------------")  # 60個

# 低通濾波

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp"
img = cv2.imread(filename, 0)

dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dftShift = np.fft.fftshift(dft)
rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)
mask = np.zeros((rows, cols, 2), np.uint8)
# 两个通道，与频谱图像匹配
mask[crow - 30 : crow + 30, ccol - 30 : ccol + 30] = 1
fShift = dftShift * mask
ishift = np.fft.ifftshift(fShift)
iImg = cv2.idft(ishift)
iImg = cv2.magnitude(iImg[:, :, 0], iImg[:, :, 1])

plt.figure("低通濾波", figsize=(16, 12))
plt.subplot(121)
plt.imshow(img, cmap="gray")
plt.title("original")

plt.subplot(122)
plt.imshow(iImg, cmap="gray")
plt.title("result")

plt.suptitle("低通濾波")
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
