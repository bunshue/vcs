"""

resize


"""

import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('縮放圖片')

img = cv2.imread(r'images/sample.jpg')
print(img.shape)

H = img.shape[0]
W = img.shape[1]
img_resize = cv2.resize(img, (W * 3, H * 2))
print(img_resize.shape)

#cv2.imshow('Sample pic', img_resize)
plt.title('原圖')
plt.imshow(cv2.cvtColor(img_resize, cv2.COLOR_BGR2RGB))

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4

image_original = cv2.imread(filename)	#讀取本機圖片

#縮放的倍率 fx fy
image_resized = cv2.resize(image_original, None, fx = 1.50, fy = 1.00, interpolation = cv2.INTER_LINEAR)

image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2RGB)
plt.imshow(image_original)
plt.show()

image_resized = cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB)
plt.imshow(image_resized)
plt.show()

print('------------------------------------------------------------')	#60個

