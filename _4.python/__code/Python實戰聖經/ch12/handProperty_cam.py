from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(minTrackCon=0.5, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        bbox = bboxInfo['bbox']
        #左右手
        myHandType = detector.handType() 
        cv2.putText(img, 'Hand:{}'.format(myHandType), (bbox[0], bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
    
        #伸出手指數
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        cv2.putText(img, 'Finger:{}'.format(totalFingers), (bbox[0]+100, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)
    
        #兩特徵點距離
        distance, img, info = detector.findDistance(8, 12, img) #食指與中指
        cv2.putText(img, 'Dist:{}'.format(str(int(distance))), (bbox[0]+200, bbox[1]-25), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

