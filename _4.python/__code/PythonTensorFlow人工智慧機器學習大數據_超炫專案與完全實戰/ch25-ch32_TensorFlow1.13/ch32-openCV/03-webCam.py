#!/usr/bin/env python
# author: Powen Ko  柯博文老師  www.powenko.com
# -*- coding: utf-8 -*-
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()