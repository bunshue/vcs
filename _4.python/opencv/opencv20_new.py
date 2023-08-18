'''
圖片邊緣檢測

圖片轉換成灰階Grayscale的部分，
利用Canny邊緣檢測使用多階段算法來檢測圖像中的各種邊緣。

OpenCV具有findContour()幫助從圖像中提取輪廓的功能。


再來就把所有輪廓繪製起來，最後show出圖片 利用imshow語法。



'''
import cv2
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = cv2.imread(filename)
cv2.imshow('Input Image', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 30, 200)
cv2.imshow('Canny Edges', edged)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)

print("Number of Contours found = " + str(len(contours)))

cv2.drawContours(image, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


