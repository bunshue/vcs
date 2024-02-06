"""
各種邊緣檢測的方法

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

plt.figure('影像處理', figsize = (16, 12))
plt.subplot(231)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 1')
sobelx = cv2.Sobel(image, -1, 1, 0)

plt.subplot(232)
plt.title('Sobel 效果 1')
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 2 x 方向')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  

plt.subplot(233)
plt.title('Sobel 效果 2 x 方向')
plt.imshow(cv2.cvtColor(sobelx, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 3 y 方向')
sobely = cv2.Sobel(image, cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)

plt.subplot(234)
plt.title('Sobel 效果 3 y 方向')
plt.imshow(cv2.cvtColor(sobely, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 4 x-y 方向')
sobelxy=cv2.Sobel(image, cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 

plt.subplot(235)
plt.title('Sobel 效果 4 x-y 方向')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 5 先x 再y 方向')
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  

plt.subplot(236)
plt.title('Sobel 效果 5 先x 再y 方向')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 6')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0)
sobely = cv2.Sobel(image, cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(image, cv2.CV_64F,1,1)
sobelxy11=cv2.convertScaleAbs(sobelxy11)

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel xy')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Sobel xy11')
plt.imshow(cv2.cvtColor(sobelxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('Scharr 效果 1')
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  

print('Scharr 效果 2')
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)  

print('Scharr 效果 3')
scharrx = cv2.Scharr(image, cv2.CV_64F, 1, 0)
scharry = cv2.Scharr(image, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  

plt.figure('Scharr', figsize = (16, 12))
plt.subplot(221)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(222)
plt.title('Scharr 效果 1')
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(223)
plt.title('Scharr 效果 2')
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.subplot(224)
plt.title('Scharr 效果 3')
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/scharr.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('Scharr 效果')
#scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 1)   #fail
scharrxy11 = cv2.Scharr(image, cv2.CV_64F, 1, 0)    #ok
scharrxy11 = cv2.convertScaleAbs(scharrxy11)   # 转回uint8  

plt.figure('', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Scharr 效果')
plt.imshow(cv2.cvtColor(scharrxy11, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sobel.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 1')
scharrx = cv2.Sobel(image, cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(image, cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel x')
plt.imshow(cv2.cvtColor(scharrx, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Sobel y')
plt.imshow(cv2.cvtColor(scharry, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Sobel 效果 2')
sobelx = cv2.Sobel(image, cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(image, cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0) 
scharrx = cv2.Scharr(image, cv2.CV_64F,1,0)
scharry = cv2.Scharr(image, cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 

plt.figure('', figsize = (16, 12))
plt.subplot(131)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(132)
plt.title('Sobel xy')
plt.imshow(cv2.cvtColor(sobelxy, cv2.COLOR_BGR2RGB))

plt.subplot(133)
plt.title('Scharr xy')
plt.imshow(cv2.cvtColor(scharrxy, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/laplacian.bmp'

image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

print('顯示 Laplacian 效果')
Laplacian = cv2.Laplacian(image, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   

plt.figure('Laplacian', figsize = (16, 12))
plt.subplot(121)
plt.title('原圖')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

plt.subplot(122)
plt.title('Laplacian')
plt.imshow(cv2.cvtColor(Laplacian, cv2.COLOR_BGR2RGB))

plt.tight_layout()
plt.show()

print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個


