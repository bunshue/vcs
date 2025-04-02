# 特徵描述

import cv2
import numpy as np

image = cv2.imread('blox.jpg')

sift_feature = cv2.xfeatures2d.SIFT_create()
surf_feature = cv2.xfeatures2d.SURF_create()
orb_feature = cv2.ORB_create()

sift_kp = sift_feature.detect(image)
surf_kp = surf_feature.detect(image)
orb_kp  = orb_feature.detect(image)

sift_out = cv2.drawKeypoints(image, sift_kp, None)
surf_out = cv2.drawKeypoints(image, surf_kp, None)
orb_out  = cv2.drawKeypoints(image, orb_kp, None)

font = cv2.FONT_HERSHEY_SIMPLEX
loc = (10, 40)
color = (0, 0, 255)
cv2.putText(image, 'origin', loc, font, 1, color, 2, cv2.LINE_AA)
cv2.putText(sift_out, 'sift', loc, font, 1, color, 2, cv2.LINE_AA)
cv2.putText(surf_out, 'surt', loc, font, 1, color, 2, cv2.LINE_AA)
cv2.putText(orb_out, 'orb', loc, font, 1, color, 2, cv2.LINE_AA)

image = cv2.vconcat(
    cv2.hconcat([image, sift_out]), 
    cv2.hconcat([surf_out, orb_out])
)

cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
