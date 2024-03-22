"""
cv2.boxFilter



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

print("boxFilter 效果 1")
image_boxFilter = cv2.boxFilter(image, -1, (5, 5))

plt.figure("new20 boxFilter 效果 1", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 1")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("boxFilter 效果 2")
image_boxFilter = cv2.boxFilter(image, -1, (5, 5), normalize=0)

plt.figure("new21 boxFilter 效果 2", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 2")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png"
image = cv2.imread(filename)

print("boxFilter 效果 3")
image_boxFilter = cv2.boxFilter(image, -1, (2, 2), normalize=0)

plt.figure("new22 boxFilter 效果 3", figsize=(16, 12))

plt.subplot(121)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title("boxFilter 效果 3")
plt.imshow(cv2.cvtColor(image_boxFilter, cv2.COLOR_BGR2RGB))

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
