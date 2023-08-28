from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)
detector = PoseDetector(mode=True)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findPose(img)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

