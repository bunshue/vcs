import cv2

cv2.namedWindow('WebCam')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    if ret == True:
        cv2.imshow('WebCam', img)
        k = cv2.waitKey(100)
        if k == ord("z") or k == ord("Z"):
            cv2.imwrite("media\\catch.jpg", img)
            break
cap.release()
cv2.waitKey(0)
cv2.destroyWindow('WebCam')
