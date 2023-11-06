"""

cut

resize

rotate


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

print('------------------------------------------------------------')	#60個


#裁剪圖片

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
image = cv2.imread(filename)	#讀取本機圖片

# 裁切區域的 x 與 y 座標（左上角）
x_st = 100
y_st = 100

# 裁切區域的長度與寬度
w = 250
h = 250

# 裁切圖片
crop_image = image[y_st : y_st + h, x_st : x_st + w]

cv2.imshow("cropped", crop_image)   # 顯示圖片

image_empty = np.zeros(image.shape, dtype = np.uint8)   #依照原圖大小建立一個圖像的二維陣列

#cv2.imshow("empty", image_empty)    #顯示圖片   #空圖, 全黑

#將擷取的圖貼到新建的黑圖
image_empty[y_st : y_st + h, x_st : x_st + w] = crop_image
cv2.imshow("cropped+new", image_empty)   # 顯示圖片

# 寫入圖檔, 偽執行
#cv2.imwrite('crop.jpg', crop_image)

cv2.waitKey()
cv2.destroyAllWindows()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

