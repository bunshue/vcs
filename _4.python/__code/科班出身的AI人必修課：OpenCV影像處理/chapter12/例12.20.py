import cv2

image = cv2.imread('contours.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])   #返回坐标值
print("returnPoints为默认值True时返回值hull的值：\n",hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False) #返回索引值
print("returnPoints为False时返回值hull的值：\n",hull2)
