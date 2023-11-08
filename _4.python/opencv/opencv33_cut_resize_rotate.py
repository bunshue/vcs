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

print('圖片裁剪縮放')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'

image = cv2.imread(filename)	#讀取本機圖片

x = 100
y = 100
w = 100
h = 100

# 寫入圖檔, 偽執行
#cv2.imwrite(filename2, image[y:y + h, x:x + w])



print('------------------------------------------------------------')	#60個


print('旋轉圖片')

#影像旋轉
#以影像中心為準，順時針旋轉30度 縮小為 0.7 倍

image = cv2.imread(filename)	#讀取本機圖片
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb)
plt.show()

h, w, d = image.shape   #d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w//2, h//2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.7)

rotate_image = cv2.warpAffine(image, P, (w, h))

rotate_image = cv2.cvtColor(rotate_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotate_image)
plt.show()


print('------------------------------------------------------------')	#60個
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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

