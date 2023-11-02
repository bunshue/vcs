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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o=cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)

cv2.imshow("Original",o)
cv2.imshow("Canny 1",r1)
cv2.imshow("Canny 2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

