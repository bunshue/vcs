filename = 'C:/______test_files/_emgu/lena.jpg'
#filename = 'C:/______test_files/ims01.bmp'

'''
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt #匯入模組

img = cv2.imread(filename)	#讀取本機圖片

#另存新檔
#cv2.imwrite('aaaa.bmp', img);

shape = img.shape
h = shape[0]    #高
w = shape[1]    #寬
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階

print("寬 = ",w,", 高 = ",h,", D = ",d)

cv2.imshow('Original Picture', img) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#裁剪圖片

import matplotlib.pyplot as plt #匯入模組
import matplotlib.image as img  #匯入模組

image = img.imread(filename)

plt.imshow(image)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要

x_l, x_r = 150, 350 #保留的部分，由左而右
y_u, y_d = 150, 400 #保留的部分，由上而下
cut_img = image[y_u:y_d, x_l:x_r]

plt.imshow(cut_img)	#顯示圖片, 兩行都要
plt.show()              #顯示圖片, 兩行都要



#影像旋轉
#以影像中心為準，順時針旋轉30度 縮小為 0.5 倍

img = cv2.imread(filename)	#讀取本機圖片
h,w,d = img.shape   #d為dimension d=3 全彩 d=1 灰階  #讀取圖片格式

center = (w//2, h//2)

#                        旋轉中心 旋轉角度 縮放比例
P = cv2.getRotationMatrix2D(center, -30, 0.5)

rotate_img = cv2.warpAffine(img, P, (w, h))

cv2.imshow('image', rotate_img)#顯示圖片


print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#影像縮放
# OpenCV中的五種縮放模式
# 由快到慢
# 1  N  INTER_NEAREST
# 2  C  INTER_CUBIC
# 3  L  INTER_LINEAR
# 4  A  INTER_AREA
# 5  L  INTER_LANCZOS4
import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.image as img  #匯入模組

img = cv2.imread(filename)	#讀取本機圖片
#縮放的倍率
img_resized = cv2.resize(img, None, fx=1.50, fy=1.00, interpolation = cv2.INTER_LINEAR)

filename2 = 'resized_img.jpg';
cv2.imwrite(filename2, img_resized)

original = cv2.imread(filename)	#讀取本機圖片
cv2.imshow('Original Picture', original) #顯示圖片

resized = cv2.imread(filename2)	#讀取本機圖片
cv2.imshow('Resized Picture', resized) #顯示圖片

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()


#影像對比與亮度調整

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.image as img  #匯入模組

# output_image = alpha * imput_image + beta
def modify_contrast_and_brightness(img, alpha=1.0, beta = 0.0):
    array_alpha = np.array([alpha]) #對比度
    array_beta = np.array([beta]) #亮度
    img = cv2.add(img, array_beta)
    img = cv2.multiply(img, array_alpha)
    img = np.clip(img, 0, 255)
    return img

img = cv2.imread(filename)	#讀取本機圖片
modified_image = modify_contrast_and_brightness(img, 1.5, 10.0)
cv2.imshow('Modified Picture', modified_image) #顯示圖片

'''

#影像分析工具
#影像直方圖

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt #匯入模組

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
plt.hist(img.ravel(), 256, [0,256])
cv2.imshow('GrayScale Picture', img) #顯示圖片
plt.show()


#直方圖影像操作
#直方圖均值化

import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt #匯入模組

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)	#讀取本機圖片, 直接轉成灰階
equa = cv2.equalizeHist(img)
cv2.imshow('Histogram', equa)#顯示圖片
plt.hist(equa.ravel(), 256, [0,256])
plt.show()






'''
cv2.imshow('視窗標題 不支持中文', img) #顯示圖片

cv2.waitKey(0)  #待user輸入內容
cv2.destroyAllWindows() #關閉視窗

print('在此等待任意鍵繼續, 繼續後刪除本視窗')
cv2.waitKey()
cv2.destroyAllWindows()

'''


