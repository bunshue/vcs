"""

cv2.grabCut



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

print("------------------------------------------------------------")  # 60個
# grabCut 影像擷取
print("------------------------------------------------------------")  # 60個

src = cv2.imread(filename2)  # 讀取影像

mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (150, 50, 200, 480)  # 建立ROI區域
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1

# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT
)

# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

dst = cv2.rectangle(dst, rect, RED, 2)

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個

src = cv2.imread("../data2b/hung.jpg")  # 讀取影像
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (10, 30, 380, 360)  # 建立ROI區域
# 呼叫grabCut()進行分割
cv2.grabCut(src, mask, rect, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_RECT)

maskpict = cv2.imread("hung_mask.jpg")  # 讀取影像
newmask = cv2.imread("hung_mask.jpg", cv2.IMREAD_GRAYSCALE)  # 灰階讀取
mask[newmask == 0] = 0  # 白色內容則確定是前景
mask[newmask == 255] = 1  # 黑色內容則確定是背景
cv2.grabCut(src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask == 0) | (mask == 2), 0, 1).astype("uint8")
dst = src * mask[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(131)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(132)
plt.imshow(cv2.cvtColor(maskpict, cv2.COLOR_BGR2RGB))
plt.title("遮罩影像")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

src = cv2.imread("lena.jpg")  # 讀取影像
bgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
fgdModel = np.zeros((1, 65), np.float64)  # 建立內部用暫時計算陣列
rect = (30, 30, 280, 280)  # 建立ROI區域
mask = np.zeros(src.shape[:2], np.uint8)  # 建立遮罩, 大小和src相同
mask[30:324, 30:300] = 3
mask[90:200, 90:200] = 1
# 呼叫grabCut()進行分割, 迭代 3 次, 回傳mask1
# 其實mask1 = mask, 因為mask也會同步更新
mask1, bgd, fgd = cv2.grabCut(
    src, mask, None, bgdModel, fgdModel, 3, cv2.GC_INIT_WITH_MASK
)
# 將 0, 2設為0 --- 1, 3設為1
mask2 = np.where((mask1 == 0) | (mask1 == 2), 0, 1).astype("uint8")
dst = src * mask2[:, :, np.newaxis]  # 計算輸出影像

plt.subplot(121)
plt.imshow(cv2.cvtColor(src, cv2.COLOR_BGR2RGB))
plt.title("原圖")
plt.axis("off")

plt.subplot(122)
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.title("擷取影像")
plt.axis("off")

show()

print("------------------------------------------------------------")  # 60個
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


print("------------------------------------------------------------")  # 60個
