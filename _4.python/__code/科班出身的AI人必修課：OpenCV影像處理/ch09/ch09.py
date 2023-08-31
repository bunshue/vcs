import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 1')
sobelx = cv2.Sobel(o,-1,1,0)
cv2.imshow("Sobel",sobelx)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 2')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
cv2.imshow("Sobel",sobelx)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 3')
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)
cv2.imshow("y",sobely)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 4')
sobelxy=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy=cv2.convertScaleAbs(sobelxy) 
cv2.imshow("xy",sobelxy)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 5')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
cv2.imshow("xy",sobelxy)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 6')
sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  
sobely = cv2.convertScaleAbs(sobely)  
sobelxy =  cv2.addWeighted(sobelx,0.5,sobely,0.5,0)  
sobelxy11=cv2.Sobel(o,cv2.CV_64F,1,1)
sobelxy11=cv2.convertScaleAbs(sobelxy11) 
cv2.imshow("xy",sobelxy)
cv2.imshow("xy11",sobelxy11)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Scharr 效果 1')
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
cv2.imshow("x",scharrx)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Scharr 效果 2')
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)  
cv2.imshow("y",scharry)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Scharr 效果 3')
scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry)  
scharrxy =  cv2.addWeighted(scharrx,0.5,scharry,0.5,0)  
cv2.imshow("xy",scharrxy)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個
'''fail
o = cv2.imread('scharr.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Scharr 效果 4')
scharrxy11=cv2.Scharr(o,cv2.CV_64F,1,1)
cv2.imshow("xy11",scharrxy11)

cv2.waitKey()
cv2.destroyAllWindows()
'''
print('------------------------------------------------------------')	#60個

o = cv2.imread('sobel4.bmp',cv2.IMREAD_GRAYSCALE)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 Sobel 效果 1')
scharrx = cv2.Sobel(o,cv2.CV_64F,1,0,-1)
scharry = cv2.Sobel(o,cv2.CV_64F,0,1,-1)
scharrx = cv2.convertScaleAbs(scharrx)   # 转回uint8  
scharry = cv2.convertScaleAbs(scharry) 
cv2.imshow("x",scharrx)
cv2.imshow("y",scharry)

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
cv2.imshow("sobelxy",sobelxy)
cv2.imshow("scharrxy",scharrxy)

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


