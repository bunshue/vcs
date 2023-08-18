import cv2
import numpy as np

#---------------读取并显示原始图像------------------
image = cv2.imread('cc.bmp')  
cv2.imshow("original", image)

#---------------提取图像轮廓------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#---------------构造矩形边界------------------ 
x,y,w,h = cv2.boundingRect(contours[0])
brcnt = np.array([[[x, y]], [[x+w, y]], [[x+w, y+h]], [[x, y+h]]])
cv2.drawContours(image, [brcnt], -1, (0, 0,255), 2)

#---------------显示矩形边界------------------
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()
