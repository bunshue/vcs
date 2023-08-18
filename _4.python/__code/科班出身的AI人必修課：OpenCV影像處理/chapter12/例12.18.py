import cv2

image = cv2.imread('cc.bmp')
cv2.imshow("original", image)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
area,trgl = cv2.minEnclosingTriangle(contours[0])
print("area=",area)
print("trgl:",trgl)
for i in range(0, 3):
    print('x')
    #cv2.line(image, tuple(trgl[i][0]), tuple(trgl[(i + 1) % 3][0]), (255,255,255), 2)
cv2.imshow("result", image)

cv2.waitKey()
cv2.destroyAllWindows()



