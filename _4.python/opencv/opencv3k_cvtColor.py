"""

Color Space Conversions

RGB、灰階、HLS、HSV 轉換

會用到的轉換

BGR轉RGB

BGR轉GRAY
BGR轉BGRA
BGR轉HSV
HSV轉BGR
BGR轉Lab


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

filename = "C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp"

print("------------------------------------------------------------")  # 60個

print("圖片色彩空間的轉換")

image1 = cv2.imread(filename, cv2.IMREAD_UNCHANGED)

plt.figure(
    num="",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(231)
plt.title("未轉換 BGR")
plt.imshow(image1)

image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

plt.subplot(232)
plt.title("BGR轉RGB")
plt.imshow(image2)


image3 = cv2.cvtColor(image1, cv2.COLOR_BGR2Lab)

plt.subplot(233)
plt.title("BGR轉LAB")
plt.imshow(image3)

plt.subplot(234)
plt.imshow(cv2.cvtColor(image3, cv2.COLOR_BGR2RGB))
plt.title('BGR轉LAB再轉RGB')


plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



