"""
OpenCV 基本使用


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


#實例化8位圖
image_empty = np.zeros((480, 640), dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列
plt.title('空圖, 全黑')
plt.imshow(cv2.cvtColor(image_empty, cv2.COLOR_BGR2RGB))    #顯示圖片   #空圖, 全黑

plt.show()



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


