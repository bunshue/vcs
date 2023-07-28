import cv2

cap = cv2.VideoCapture('coin.jpg')

ret, frame = cap.read()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (13, 13), 0)
edged = cv2.Canny(gray, 50, 150)

contours, hierarchy = cv2.findContours(
    edged.copy(), 
    cv2.RETR_EXTERNAL, 
    cv2.CHAIN_APPROX_SIMPLE)

out = frame.copy()
cv2.drawContours(out, contours, -1, (0, 255, 128), 2)

frame = cv2.hconcat([frame, out])

cv2.imshow('frame', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()

