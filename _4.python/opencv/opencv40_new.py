"""


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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
"""
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

img = cv2.imread(filename) #cv2讀取圖片, 自動轉成array

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #轉換為HSV
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  #轉換為RGB

plt.imshow(rgb)
plt.show()

coordinate = rgb[131, 81] #輸入要取得顏色的指定座標
print(coordinate)

#print(array([255, 219,  79], dtype=uint8))




print('------------------------------------------------------------')	#60個


import cv2

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = cv2.imread(filename)

image[0,0]=[0,0,255]
image[70:120, 200:250]=[0,255,0]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.show()
"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

