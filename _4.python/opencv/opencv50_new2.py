"""
opencv 集合

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

"""

彩色影像轉HSV(RGB to HSV 或 BGR to HSV)

HSV簡單介紹分別為：
色相(H)：色彩的顏色名稱，如紅色、黃色等。
飽和度(S)：色彩的純度，越高色彩越純，低則逐漸變灰，數值為0-100%。
明度(V)：亮度，數值為0-100%。


使用 cv2.cvtColor 轉換顏色空間時，第二個參數與HSV相關的有：
cv2.COLOR_BGR2HSV
cv2.COLOR_HSV2BGR
cv2.COLOR_RGB2HSV
cv2.COLOR_HSV2RGB

opencv 預設的排列方式為BGR，而不是RGB

所以這邊使用的是 cv2.COLOR_BGR2HSV

當然實際上使用時不會只是單純RGB轉換成HSV就結束了，
通常會去針對HSV顏色區間去作後續的處理

範例. 物件偵測 - 找出綠色的物體

彩色轉HSV常見的應用可能有物件偵測，去背處理(排除綠色的背景)，
以下就來示範如何找出圖片中綠色的水果，類似的應用可能有找出草地的背景，

"""

import cv2
import numpy as np

image = cv2.imread('fruit.jpg')
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

plt.subplot(131)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

plt.subplot(132)
plt.imshow(cv2.cvtColor(hsv, cv2.COLOR_BGR2RGB))
plt.title('轉HSV')

lower_green = np.array([35, 43, 46])#綠色下限
upper_green = np.array([77, 255, 255])#綠色上限
mask = cv2.inRange(hsv, lower_green, upper_green)
res = cv2.bitwise_and(image, image, mask=mask)

plt.subplot(133)
plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
plt.title('抓出綠色的部分')

plt.show()


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

