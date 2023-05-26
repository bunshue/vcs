#filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'

import cv2
import numpy as np
import matplotlib.pyplot as plt

#讀取圖片
img = cv2.imread(filename)
#實例化8位圖
emptyImage = np.zeros(img.shape, np.uint8)
emptyImage2 = img.copy()
#灰度圖
emptyImage3 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#顯示圖片
cv2.imshow("emptyImage",emptyImage)
cv2.imshow("emptyImage2",emptyImage2)
cv2.imshow("emptyImage3",emptyImage3)
cv2.imshow("img",img)
#保存圖片 質量為5 和 100
cv2.imwrite("./1.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
cv2.imwrite("./2.jpg",img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
#png壓縮大小
cv2.imwrite("./3.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
cv2.imwrite("./4.png",img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])

#cv2.namedWindow("image")
#cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#-- Read image -----------------------------------------------------------------------
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey()

#-- Edge detection -------------------------------------------------------------------

edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
cv2.imshow('Canny', edges)
cv2.waitKey()
edges = cv2.dilate(edges, None)
cv2.imshow('Dilate', edges)
cv2.waitKey()
edges = cv2.erode(edges, None)
cv2.imshow('Erode', edges)
cv2.waitKey()

#cv2.imwrite('C:/Temp/person-masked.jpg', masked)           # Save


'''
import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

img = cv2.imread(filename)

# split image into channels
c_red, c_green, c_blue = cv2.split(img)

# merge with mask got on one of a previous steps
#img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

cv2.imshow('R', c_red)
cv2.waitKey()

cv2.imshow('G', c_green)
cv2.waitKey()

cv2.imshow('B', c_blue)
cv2.waitKey()
'''

'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/_opencv/lena.jpg'

#== Parameters =======================================================================
BLUR = 21
CANNY_THRESH_1 = 10
CANNY_THRESH_2 = 200
MASK_DILATE_ITER = 10
MASK_ERODE_ITER = 10
MASK_COLOR = (0.0,0.0,1.0) # In BGR format


#== Processing =======================================================================

#-- Read image -----------------------------------------------------------------------
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#-- Edge detection -------------------------------------------------------------------
edges = cv2.Canny(gray, CANNY_THRESH_1, CANNY_THRESH_2)
edges = cv2.dilate(edges, None)
edges = cv2.erode(edges, None)

# split image into channels
c_red, c_green, c_blue = cv2.split(img)

# merge with mask got on one of a previous steps
img_a = cv2.merge((c_red, c_green, c_blue, mask.astype('float32') / 255.0))

# show on screen (optional in jupiter)
#%matplotlib inline
plt.imshow(img_a)
plt.show()

# save to disk
cv2.imwrite('img/girl_1.png', img_a*255)

# or the same using plt
plt.imsave('img/girl_2.png', img_a)

cv2.imshow('img', masked)                                   # Displays red, saves blue

cv2.waitKey()
'''




