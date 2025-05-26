"""

cv2.blur


"""

import cv2

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


print("------------------------------------------------------------")  # 60個
'''
filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("blur 效果 1")
r = cv2.blur(image, (5, 5))

plt.figure("blur 效果", figsize=(16, 12))
plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("blur 效果 1")
plt.imshow(cv2.cvtColor(r, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("blur 效果 2")
image_blur_05 = cv2.blur(image, (5, 5))
image_blur_30 = cv2.blur(image, (30, 30))

plt.figure("blur 效果", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("blur 效果 2")
plt.imshow(cv2.cvtColor(image_blur_05, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("blur 效果 2")
plt.imshow(cv2.cvtColor(image_blur_30, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"

img = cv2.imread(filename)
output1 = cv2.blur(img, (5, 5))  # 指定區域單位為 (5, 5)
output2 = cv2.blur(img, (25, 25))  # 指定區域單位為 (25, 25)

cv2.imshow("image1", output1)
cv2.imshow("image2", output2)

cv2.waitKey(0)  # 按下任意鍵停止
cv2.destroyAllWindows()
'''
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
# 刪除影像雜訊_濾波
print("------------------------------------------------------------")  # 60個

filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("使用 均值濾波器.blur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (3, 3))  # 使用 3x3 濾波核
dst2 = cv2.blur(src, (5, 5))  # 使用 5x5 濾波核
dst3 = cv2.blur(src, (7, 7))  # 使用 7x7 濾波核
dst4 = cv2.blur(src, (29, 29))  # 使用 29x29 濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)
cv2.imshow("dst 29 x 29", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 方框濾波器.boxFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.boxFilter(src, -1, (2, 2), normalize=0)  # ksize是 2x2 的濾波核
dst2 = cv2.boxFilter(src, -1, (3, 3), normalize=0)  # ksize是 3x3 的濾波核
dst3 = cv2.boxFilter(src, -1, (5, 5), normalize=0)  # ksize是 5x5 的濾波核

cv2.imshow("dst 2 x 2", dst1)
cv2.imshow("dst 3 x 3", dst2)
cv2.imshow("dst 5 x 5", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = np.ones((3, 3), np.float32) * 150
src[1, 1] = 20
print(f"原陣列 src = \n {src}")

dst = cv2.medianBlur(src, 3)
print(f"中值濾波後 dst = \n {dst}")

print("------------------------------------------------------------")  # 60個

print("使用 中值濾波器.medianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.medianBlur(src, 3)  # 使用邊長是 3 的濾波核
dst2 = cv2.medianBlur(src, 5)  # 使用邊長是 5 的濾波核
dst3 = cv2.medianBlur(src, 7)  # 使用邊長是 7 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 7 x 7", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 高斯濾波器.GaussianBlur()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 使用 3 x 3 的濾波核
dst2 = cv2.GaussianBlur(src, (5, 5), 0, 0)  # 使用 5 x 5 的濾波核
dst3 = cv2.GaussianBlur(src, (29, 29), 0, 0)  # 使用 29 x 29 的濾波核
cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 5 x 5", dst2)
cv2.imshow("dst 15 x 15", dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur()")

src = cv2.imread("data/border.jpg")

dst1 = cv2.blur(src, (3, 3))  # 均值濾波器 - 3x3 濾波核
dst2 = cv2.blur(src, (7, 7))  # 均值濾波器 - 7x7 濾波核

dst3 = cv2.GaussianBlur(src, (3, 3), 0, 0)  # 高斯濾波器 - 3x3 的濾波核
dst4 = cv2.GaussianBlur(src, (7, 7), 0, 0)  # 高斯濾波器 - 7x7 的濾波核

cv2.imshow("dst 3 x 3", dst1)
cv2.imshow("dst 7 x 7", dst2)
cv2.imshow("Gauss dst 3 x 3", dst3)
cv2.imshow("Gauss dst 7 x 7", dst4)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 均值濾波器.blur() / 高斯濾波器.GaussianBlur() / 雙邊濾波器.bilateralFilter()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

dst1 = cv2.blur(src, (15, 15))  # 均值濾波器
dst2 = cv2.GaussianBlur(src, (15, 15), 0, 0)  # 高斯濾波器
dst2 = cv2.bilateralFilter(src, 15, 100, 100)  # 雙邊濾波器

cv2.imshow("blur", dst1)
cv2.imshow("GaussianBlur", dst1)
cv2.imshow("bilateralFilter", dst2)

cv2.waitKey()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("使用 2D濾波核.filter2D()")

src = cv2.imread(filename2)
cv2.imshow("src", src)

kernel = np.ones((11, 11), np.float32) / 121  # 自訂卷積核
dst = cv2.filter2D(src, -1, kernel)  # 自定義濾波器
cv2.imshow("dst", dst)

cv2.waitKey()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
