#输出边缘和结构信息

import cv2

image = cv2.imread('contours.bmp')  
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
o=cv2.drawContours(image, contours, -1, (0, 0, 255), 5)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()



