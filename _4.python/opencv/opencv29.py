import sys
import cv2
import numpy as np
from matplotlib import pyplot as plt

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)
img2 = img.copy()
template = cv2.imread('images/temp.bmp',0)
th, tw = template.shape[::]
img = img2.copy()
rv = cv2.matchTemplate(img,template,cv2.TM_SQDIFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = minLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)

plt.subplot(121)
plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')
plt.xticks([])
plt.yticks([])

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_gray.bmp'
img = cv2.imread(filename, 0)
img2 = img.copy()
template = cv2.imread('images/temp.bmp',0)
tw, th = template.shape[::-1]
img = img2.copy()
rv = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(rv)
topLeft = maxLoc
bottomRight = (topLeft[0] + tw, topLeft[1] + th)
cv2.rectangle(img,topLeft, bottomRight, 255, 2)

plt.subplot(121)
plt.imshow(rv,cmap = 'gray')
plt.title('Matching Result')
plt.xticks([])
plt.yticks([])

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')
plt.xticks([])
plt.yticks([])

plt.show()

print('------------------------------------------------------------')	#60個

img = cv2.imread('images/lena4.bmp',0)
template = cv2.imread('images/lena4Temp.bmp',0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.9
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), 255, 1)
plt.imshow(img,cmap = 'gray')
plt.xticks([])
plt.yticks([])

plt.show()

print('------------------------------------------------------------')	#60個

a=np.array([3,6,8,1,2,88])
b=np.where(a>5)
print(b)

print('------------------------------------------------------------')	#60個

a=np.array([[3,6,8,77,66],[1,2,88,3,98],[11,2,67,5,2]])
print(a)
b=np.where(a>5)
print(b)

print('------------------------------------------------------------')	#60個

list2d =np.arange(18).reshape(3,6)
print(list2d)
h,w=list2d.shape[::]
print(h,w)
w,h=list2d.shape[::-1]
print(w,h)

print('------------------------------------------------------------')	#60個

list2d =np.arange(18).reshape(3,6)
print(list2d)
print(list2d[::-1])

print('------------------------------------------------------------')	#60個

loc = ([1,2,3,4],[11,12,13,14])
for i in zip(*loc):
    print(i)

print('------------------------------------------------------------')	#60個

loc = ([1,2,3,4],[11,12,13,14])
print(loc)
print(loc[::-1])

print('------------------------------------------------------------')	#60個

x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
t = (x,y,z)
print(t)
for i in zip(*t):
    print(i)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



