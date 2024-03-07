"""

GaussianBlur

Canny


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
'''
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/barbara.bmp'

#原圖
image = cv2.imread(filename, 0)

# 高斯模糊，Canny边缘检测需要的
image_blur = cv2.GaussianBlur(image, (5, 5), 0)    #執行高斯模糊化

# 进行边缘检测，减少图像空间中需要检测的点数量
image_canny = cv2.Canny(image_blur, 50, 150)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('GaussianBlur')
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Canny')
plt.imshow(cv2.cvtColor(image_canny, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

#Gaussian lowpass filter

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_noise.png'
image = cv2.imread(filename)

print('GaussianBlur 1')
kernel_size = (5, 5)   #卷積的矩陣大小 ksize 指定區域單位 ( 必須是大於 1 的奇數 )
sigma = 0       #sigma值     sigmaX X 方向標準差，預設 0，sigmaY Y 方向標準差，預設 0
image_blur = cv2.GaussianBlur(image, kernel_size, 0) #執行高斯模糊化

plt.figure('GaussianBlur', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('GaussianBlur')
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread(filename)

image_blur = cv2.GaussianBlur(image, (5, 5), 0) #執行高斯模糊化

plt.figure('GaussianBlur', figsize = (16, 12))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title('GaussianBlur')

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/bilTest.bmp'
image = cv2.imread(filename)

print('GaussianBlur 2')
image_blur = cv2.GaussianBlur(image, (55, 55), 0) #執行高斯模糊化

plt.figure('GaussianBlur', figsize = (16, 12))
plt.subplot(121)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('原圖')

plt.subplot(122)
plt.imshow(cv2.cvtColor(image_blur, cv2.COLOR_BGR2RGB))
plt.title('GaussianBlur')

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

image_canny1 = cv2.Canny(image,128,200)
image_canny2 = cv2.Canny(image,32,128)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Canny 1')
plt.imshow(cv2.cvtColor(image_canny1, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Canny 2')
plt.imshow(cv2.cvtColor(image_canny2, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""
#執行高斯模糊化

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0) #執行高斯模糊化
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # 只需在原始图像的边缘添加一些颜色
    cv2.imshow('canny demo',dst)



original_img = cv2.imread("lena.png", 0)
#canny(): 边缘检测
img1 = cv2.GaussianBlur(original_img, (3, 3), 0)   #執行高斯模糊化
canny = cv2.Canny(img1, 50, 150)



"""

'''


print("------------------------------------------------------------")  # 60個

print("CannyThreshold")

def CannyThreshold(lowThreshold):
    detected_edges = cv2.GaussianBlur(gray, (3, 3), 0) #執行高斯模糊化
    detected_edges = cv2.Canny(detected_edges,
                               lowThreshold,
                               lowThreshold*ratio,
                               apertureSize = kernel_size)
    dst = cv2.bitwise_and(img,img,mask = detected_edges)  # 只需在原始圖像的邊緣添加一些顏色
    cv2.imshow('canny demo', dst)

lowThreshold = 0
max_lowThreshold = 100
ratio = 3
kernel_size = 3 
img = cv2.imread('data/lena.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.namedWindow('canny demo') 
cv2.createTrackbar('Min threshold','canny demo',lowThreshold, max_lowThreshold, CannyThreshold)
 
CannyThreshold(0)  # 初始化
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


print("sharpening")

# 圖像銳化函數
def my_not_sharpen(image, k, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    # 注意不能直接用減法，對于圖像格式結果為負時會自動加上256
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    # 兩個矩陣中有一個不是圖像格式，則結果就不會轉換為圖像格式
    sharpen_image = image + k * model   
    sharpen_image = cv2.convertScaleAbs(sharpen_image)
    return sharpen_image

# 提取圖像邊界信息函數
def my_get_model(image, blur_size=(5, 5), blured_sigma=3):
    blured_image = cv2.GaussianBlur(image, blur_size, blured_sigma)  #執行高斯模糊化
    model = np.zeros(image.shape, dtype=np.int64)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            model[i][j] = int(image[i][j]) - int(blured_image[i][j])
    model = cv2.convertScaleAbs(model)
    return model

original_image_lena = cv2.imread('data/lena.png', 0)

# 獲得圖像邊界信息
edge_image_lena = my_get_model(original_image_lena)

# 獲得銳化圖像
sharpen_image_lena = my_not_sharpen(original_image_lena, 3)

# 顯示結果
plt.subplot(131)
plt.title('原始圖像')
plt.imshow(original_image_lena)
plt.subplot(132)
plt.title('邊緣檢測')
plt.imshow(edge_image_lena)
plt.subplot(133)
plt.title('非銳化')
plt.imshow(sharpen_image_lena)
plt.show()



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個





print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



