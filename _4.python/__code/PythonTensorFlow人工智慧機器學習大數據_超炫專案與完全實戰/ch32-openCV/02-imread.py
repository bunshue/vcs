#!/usr/bin/env python
# author: Powen Ko  柯博文老師  www.powenko.com
# -*- coding: utf-8 -*-

import numpy as np
import cv2

img = cv2.imread('1.jpg')
img[0,0]=[0,0,255]
img[10:20,10:20]=[0,255,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

