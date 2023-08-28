import numpy as np
import cv2

img = cv2.imread('building.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)

cv2.imshow('img',img)
cv2.imshow('cl1',cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()
