import cv2
import numpy as np

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 erode 效果 1')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(o,kernel)
cv2.imshow("erosion",erosion)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/erode.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 erode 效果 2')
kernel = np.ones((9,9),np.uint8)
erosion = cv2.erode(o,kernel,iterations =5)
cv2.imshow("erosion",erosion)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 dilate 效果 1')
kernel = np.ones((9,9),np.uint8)
dilation = cv2.dilate(o,kernel)
cv2.imshow("dilation",dilation)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/dilation.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 dilate 效果 2')
kernel = np.ones((5,5),np.uint8)
dilation = cv2.dilate(o,kernel,iterations = 9)
cv2.imshow("dilation", dilation)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening.bmp'
img1=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img1",img1)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/opening2.bmp'
img2=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img2",img2)

print('顯示 morphologyEx 效果 1')
k=np.ones((10,10),np.uint8)
r1=cv2.morphologyEx(img1,cv2.MORPH_OPEN,k)
r2=cv2.morphologyEx(img2,cv2.MORPH_OPEN,k)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing.bmp'
img1=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img1",img1)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/closing2.bmp'
img2=cv2.imread(filename)
print('顯示原圖')
cv2.imshow("img2",img2)

print('顯示 morphologyEx 效果 2')
k=np.ones((10,10),np.uint8)
r1=cv2.morphologyEx(img1,cv2.MORPH_CLOSE,k,iterations=3)
r2=cv2.morphologyEx(img2,cv2.MORPH_CLOSE,k,iterations=3)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/gradient.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 morphologyEx 效果 3')
k=np.ones((5,5),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_GRADIENT,k)
cv2.imshow("result",r)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/tophat.bmp'
o1=cv2.imread(filename,cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original1",o1)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o2=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original2",o2)

print('顯示 morphologyEx 效果 4')
k=np.ones((5,5),np.uint8)
r1=cv2.morphologyEx(o1,cv2.MORPH_TOPHAT,k)
r2=cv2.morphologyEx(o2,cv2.MORPH_TOPHAT,k)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/blackhat.bmp'
o1=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original1",o1)

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
o2=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original2",o2)

print('顯示 morphologyEx 效果 5')
k=np.ones((5,5),np.uint8)
r1=cv2.morphologyEx(o1,cv2.MORPH_BLACKHAT,k)
r2=cv2.morphologyEx(o2,cv2.MORPH_BLACKHAT,k)
cv2.imshow("result1",r1)
cv2.imshow("result2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (5,5))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (5,5))
print("kernel1=\n",kernel1)
print("kernel2=\n",kernel2)
print("kernel3=\n",kernel3)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/kernel.bmp'
o=cv2.imread(filename, cv2.IMREAD_UNCHANGED)
print('顯示原圖')
cv2.imshow("original",o)

print('顯示 dilate 效果')
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59,59))
dst1 = cv2.dilate(o,kernel1)
dst2 = cv2.dilate(o,kernel2)
dst3 = cv2.dilate(o,kernel3)
cv2.imshow("dst1",dst1)
cv2.imshow("dst2",dst2)
cv2.imshow("dst3",dst3)

cv2.waitKey()
cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個


