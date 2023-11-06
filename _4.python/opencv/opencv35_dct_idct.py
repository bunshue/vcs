"""
頻率域影像處理


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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'
img = cv2.imread(filename, 0)
print('顯示原圖')
cv2.imshow("original", img)

#將型態轉成float後再計算DCT
img_float = img.astype(float)

#DCT
img_dct = cv2.dct(img_float)

#將型態轉成OpenCV允許顯示的型態
result1 = img_dct.astype(np.uint8)

print('顯示 DCT 結果')
cv2.imshow("DCT Result", result1)


#做IDCT
img_idct = cv2.idct(img_dct)
#將型態轉成OpenCV允許顯示的型態
result2 = img_idct.astype(np.uint8)

print('顯示 IDCT 結果')
cv2.imshow("IDCT Result", result2)



cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個

