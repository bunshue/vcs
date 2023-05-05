import cv2	#導入 OpenCV 模組
import numpy as np
import matplotlib.pyplot as plt

import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'

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

filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'

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



