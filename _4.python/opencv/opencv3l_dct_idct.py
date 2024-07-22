"""
頻率域影像處理


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
filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

image = cv2.imread(filename, 0)
print(image.shape)

print("顯示原圖")
cv2.imshow("original", image)

# 將型態轉成float後再計算DCT
image_float = image.astype(float)

# DCT
image_dct = cv2.dct(image_float)

# 將型態轉成OpenCV允許顯示的型態
result1 = image_dct.astype(np.uint8)

print("顯示 DCT 結果")
cv2.imshow("DCT Result", result1)

H, W = image_dct.shape
print(image_dct.shape)

# 做IDCT
image_idct = cv2.idct(image_dct)
# 將型態轉成OpenCV允許顯示的型態
result2 = image_idct.astype(np.uint8)

print("顯示 IDCT 結果")
cv2.imshow("IDCT Result", result2)

cv2.waitKey()
cv2.destroyAllWindows()

# 用matplotlib顯示
plt.figure("DCT-IDCT", figsize=(16, 12))
plt.subplot(131)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title("經過DCT")
plt.imshow(cv2.cvtColor(result1, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title("再經過IDCT")
plt.imshow(cv2.cvtColor(result2, cv2.COLOR_BGR2RGB))

plt.show()

print("------------------------------------------------------------")  # 60個
