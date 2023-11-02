'''
各種邊緣檢測的方法

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

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 1')
sobelx = cv2.Sobel(o,-1,1,0)
cv2.imshow("Sobel 1",sobelx)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 2 x 方向')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
cv2.imshow("Sobel x",sobelx)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 3 y 方向')
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("Sobel y",sobely)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 4 x-y 方向')
sobelxy=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 
cv2.imshow("Sobel xy",sobelxy)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 5 先x 再y 方向')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
cv2.imshow("Sobel xy",sobelxy)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('------------------------------------------------------------')	#60個

print('顯示 Sobel 效果 6')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy11=cv2.convertScaleAbs(sobelxy11)
cv2.imshow("Sobel xy",sobelxy)
cv2.imshow("Sobel xy11",sobelxy11)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('------------------------------------------------------------')	#60個

print('顯示 Scharr 效果 1')
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
cv2.imshow("Scharr x",scharrx)

print('------------------------------------------------------------')	#60個

print('顯示 Scharr 效果 2')
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)  
cv2.imshow("Scharr y",scharry)

print('------------------------------------------------------------')	#60個

print('顯示 Scharr 效果 3')
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  
cv2.imshow("Scharr xy",scharrxy)

print('------------------------------------------------------------')	#60個

o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Scharr 效果 4 fail')
#scharrxy11=cv2.Scharr(o,cv2.CV_64F,1,1)
#cv2.imshow("xy11 aaaa",scharrxy11)

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 1')
scharrx = cv2.Sobel(o,cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(o,cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 
cv2.imshow("Sobel x",scharrx)
cv2.imshow("Sobel y",scharry)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 2')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0,ksize=3)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0) 
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0) 
cv2.imshow("Sobel xy",sobelxy)
cv2.imshow("Scharr xy",scharrxy)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('Laplacian.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Laplacian 效果')
Laplacian = cv2.Laplacian(o,cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   
cv2.imshow("Laplacian",Laplacian)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


