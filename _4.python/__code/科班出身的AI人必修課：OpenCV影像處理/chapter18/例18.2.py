import numpy as np
import cv2

cap = cv2.VideoCapture('viptrain.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    c = cv2.waitKey(1)
    if c==27:   #ESC键
        break
cap.release()
cv2.destroyAllWindows()
