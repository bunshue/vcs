"""
cv2.bilateralFilter



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


filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("bilateralFilter 效果 1")
image_bilateralFilter = cv2.bilateralFilter(image, 25, 100, 100)

plt.figure("new24 bilateralFilter 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("bilateralFilter 效果 1")
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp"
image = cv2.imread(filename)

print("bilateralFilter 效果 2")
image_bilateralFilter = cv2.bilateralFilter(image, 55, 100, 100)

plt.figure("new25 bilateralFilter 效果 2", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("bilateralFilter 效果 2")
plt.imshow(cv2.cvtColor(image_bilateralFilter, cv2.COLOR_BGR2RGB))

plt.show()


print("------------------------------------------------------------")  # 60個

img = cv2.imread(filename)
output1 = cv2.bilateralFilter(img, 50, 0, 0)
output2 = cv2.bilateralFilter(img, 50, 50, 100)
output3 = cv2.bilateralFilter(img, 50, 100, 1000)

cv2.imshow('image1', output1)
cv2.imshow('image2', output2)
cv2.imshow('image3', output3)
cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
