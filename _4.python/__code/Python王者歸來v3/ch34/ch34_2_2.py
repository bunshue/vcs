# ch34_2_2.py
import cv2

img = cv2.imread("street.jpg")                  # BGR讀取
cv2.imshow("BGR Color Space", img)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # BGR轉HSV
cv2.imshow("HSV Color Space", img_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()









 
