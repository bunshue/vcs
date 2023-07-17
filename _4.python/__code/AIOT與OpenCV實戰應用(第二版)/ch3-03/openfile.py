import cv2

frame = cv2.imread('demo.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
