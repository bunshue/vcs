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

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')

plt.tight_layout()
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

plt.subplot(122)
plt.imshow(img,cmap = 'gray')
plt.title('Detected Point')

plt.tight_layout()
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

plt.tight_layout()
plt.show()
'''

print('------------------------------------------------------------')	#60個

d = 400
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        p1x = x
        p1y = y
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x, p1y),(p2x, p2y), color, 2)
image = np.ones((d, d, 3), dtype = "uint8") * 255
cv2.namedWindow('Demo19.10')
cv2.setMouseCallback('Demo19.10', draw)
while(1):
    cv2.imshow('Demo19.10', image)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()

print('------------------------------------------------------------')	#60個

#fail
d = 400
global thickness
thickness = -1
def fill(x):
    pass
def draw(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        p1x = x
        p1y = y
        p2x = np.random.randint(1, d - 50)  #np.random之randint不含尾
        p2y = np.random.randint(1, d - 50)  #np.random之randint不含尾
        color = np.random.randint(0, high = 256, size = (3,)).tolist()  #np.random之randint不含尾
        cv2.rectangle(image,(p1x,p1y),(p2x,p2y),color,thickness)

image = np.ones((d, d, 3), np.uint8) * 255
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw)
cv2.createTrackbar('R', 'image', 0, 1, fill)
while(1):
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xFF
    g = cv2.getTrackbarPos('R', 'image')
    if g == 0:
        thickness = -1
    else:
        thickness = 2        
    if k == 27:
        break   

cv2.destroyAllWindows()





print('------------------------------------------------------------')	#60個



