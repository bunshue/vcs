'''
使用 cv2 顯示圖片

vs

使用 matplotlib 顯示圖片

'''

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
#filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

print('------------------------------------------------------------')	#60個

print('取得 OpenCV 版本')

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

print(cv2.__version__)
print(major_ver)
print(minor_ver)
print(subminor_ver)

print('------------------------------------------------------------')	#60個

print('使用 cv2 顯示圖片')

image = cv2.imread(filename)	#讀取本機圖片

cv2.imshow('Peony', image)  #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

"""
cv2.imshow('視窗標題 不支持中文', image) #顯示圖片

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()
"""

print('------------------------------------------------------------')	#60個

print('使用 matplotlib 顯示圖片, 需先BGR轉RGB')

plt.title('使用 matplotlib 顯示圖片, 需先BGR轉RGB')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
