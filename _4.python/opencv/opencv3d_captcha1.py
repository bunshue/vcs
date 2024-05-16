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

filename = 'C:/_git/vcs/_4.python/opencv/data/captcha/captcha03.png"

image = cv2.imread(filename)  # 讀取本機圖片

plt.figure("影像處理", figsize=(16, 8))

plt.subplot(221)
plt.title("原圖")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # 轉為灰階
plt.subplot(222)
plt.title("轉為灰階")
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))

_, image_gray_inv = cv2.threshold(image_gray, 150, 255, cv2.THRESH_BINARY_INV)  # 轉為反相黑白
plt.subplot(223)
plt.title("轉為反相黑白")
plt.imshow(cv2.cvtColor(image_gray_inv, cv2.COLOR_BGR2RGB))

print(image_gray_inv.shape)
print(len(image_gray_inv))
print(len(image_gray_inv[3]))

for i in range(len(image_gray_inv)):  # i為每一列
    for j in range(len(image_gray_inv[i])):  # j為每一行
        if image_gray_inv[i][j] == 255:  # 顏色為白色
            count = 0
            for k in range(-2, 3):
                for l in range(-2, 3):
                    try:
                        if image_gray_inv[i + k][j + l] == 255:  # 若是白點就將count加1
                            count += 1
                    except IndexError:
                        pass
            if count <= 6:  # 週圍少於等於6個白點
                image_gray_inv[i][j] = 0  # 將白點去除

image_dilation = cv2.dilate(image_gray_inv, (8, 8), iterations=1)  # 圖形加粗 擴大使膨脹
plt.subplot(224)
plt.title("擴大使膨脹")
plt.imshow(cv2.cvtColor(image_dilation, cv2.COLOR_BGR2RGB))

plt.show()
