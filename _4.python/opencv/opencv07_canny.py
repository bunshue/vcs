import cv2

o=cv2.imread("images/lena.bmp",cv2.IMREAD_GRAYSCALE)

r1=cv2.Canny(o,128,200)
r2=cv2.Canny(o,32,128)

cv2.imshow("Original",o)
cv2.imshow("Canny 1",r1)
cv2.imshow("Canny 2",r2)

cv2.waitKey()
cv2.destroyAllWindows()

