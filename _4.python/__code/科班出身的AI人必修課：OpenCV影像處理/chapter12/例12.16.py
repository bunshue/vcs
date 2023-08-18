import cv2

image = cv2.imread('cc.bmp')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("original", image)
ellipse = cv2.fitEllipse(contours[0])
print("ellipse=",ellipse)
cv2.ellipse(image, ellipse,(0,255,0),3)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()
