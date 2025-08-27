import cv2

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

filename1 = 'data/montage_left.JPG'
filename2 = 'data/montage_right_gray.JPG'

img1 = cv2.imread(filename1, cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(filename2, cv2.IMREAD_GRAYSCALE)

# 比較影像
diff_imgs1_2 = cv2.absdiff(img1, img2)

cv2.namedWindow('Difference', cv2.WINDOW_NORMAL)
diff_imgs1_2_resize = cv2.resize(diff_imgs1_2, (699, 700))
cv2.imshow('Difference', diff_imgs1_2_resize)
#cv2.waitKey(3000)
#cv2.destroyAllWindows()

crop_diff = diff_imgs1_2[10:2795, 10:2445]  # x, y, w, h = 10, 10, 2790, 2440

# 預處理影像模糊化(減少影像雜訊)
blurred = cv2.GaussianBlur(crop_diff, (5, 5), 0)

(minVal, maxVal, minLoc, maxLoc2) = cv2.minMaxLoc(blurred) # 傳回影像中像素值最小和最大的值及其位置 tuple
cv2.circle(img2, maxLoc2, 100, 255, 3) # 畫圓圈
x, y = int(img2.shape[1]/4), int(img2.shape[0]/4) # 設定視窗大小
img2_resize = cv2.resize(img2, (x, y)) # 視窗停滯 7 秒
cv2.imshow('Change', img2_resize) # 顯示視窗
cv2.waitKey(10000) # 視窗停滯 10 秒
cv2.destroyAllWindows() # 關閉視窗
