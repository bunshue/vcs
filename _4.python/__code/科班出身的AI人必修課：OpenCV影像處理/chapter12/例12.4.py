import cv2
import numpy as np

image = cv2.imread('moments.bmp')
cv2.imshow("original", image) 
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
n=len(contours)
contoursImg=[]
for i in range(n):
    temp=np.zeros(image.shape, np.uint8)
    contoursImg.append(temp)
    contoursImg[i]=cv2.drawContours(contoursImg[i],contours,i,255,3) 
    cv2.imshow("contours[" + str(i)+"]",contoursImg[i]) 
print("观察各个轮廓的矩（moments）:")
for i in range(n):
    print("轮廓"+str(i)+"的矩:\n",cv2.moments(contours[i]))
print("观察各个轮廓的面积:")
for i in range(n):
    print("轮廓"+str(i)+"的面积:%d" %cv2.moments(contours[i])['m00'])

cv2.waitKey()
cv2.destroyAllWindows()
