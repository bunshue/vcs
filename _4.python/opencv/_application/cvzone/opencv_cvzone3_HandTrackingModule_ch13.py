
#使用 CVZone

#CH13 人工智慧應用（二）：多手勢追蹤與人體姿態評估

"""
13-1 CVZone多手勢追蹤
13-2 CVZone辨識手勢（一）：剪刀、石頭與布
13-3 CVZone辨識手勢（二）：OK手勢
13-4 CVZone人體姿態評估
13-5 CVZone辨識人體姿勢（一）：仰臥起坐
13-6 CVZone辨識人體姿勢（二）：伏地挺身
"""

print("------------------------------------------------------------")  # 60個

import cv2
from cvzone.HandTrackingModule import HandDetector

filename = 'D:/_git/vcs/_4.python/opencv/data/_face/face03.jpg'

print("------------------------------------------------------------")  # 60個

img = cv2.imread("images/hand.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=1)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]   # 第1隻手
    centerPoint1 = hand1["center"]
    print(centerPoint1)
    cv2.circle(img, centerPoint1, 10, (0, 255, 255), cv2.FILLED)
    handType1 = hand1["type"]
    print(handType1)
    cv2.putText(img, handType1, (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hands.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]   # 第1隻手
    centerPoint1 = hand1["center"]
    cv2.circle(img, centerPoint1, 10, (0, 255, 255), cv2.FILLED)
    if len(hands) == 2:
        hand2 = hands[1]   # 第2隻手
        centerPoint2 = hand2["center"]
        print(centerPoint2)
        cv2.circle(img, centerPoint2, 10, (0, 255, 255), cv2.FILLED)
        
cv2.imshow("Hands", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands = detector.findHands(img, draw=False)
if hands:
    hand1 = hands[0]   # 第1隻手
    bbox1 = hand1["bbox"]
    x, y, w, h = bbox1
    cv2.rectangle(img, (x, y), (x+w, y+h),
                              (0, 0, 255), 2)
    lmList1 = hand1["lmList"]
    for point in lmList1:
        x, y = point
        cv2.circle(img, (x, y), 3, (0, 255, 255), cv2.FILLED)    

cv2.imshow("Hand", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hands.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands = detector.findHands(img, draw=False)
if hands:
    hand1 = hands[0]   # 第1隻手
    x, y, w, h = hand1["bbox"]
    cv2.rectangle(img, (x, y), (x+w, y+h),
                               (0, 0, 255), 2)
    for point in hand1["lmList"]:
        cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)     
    if len(hands) == 2:
        hand2 = hands[1]   # 第2隻手
        x, y, w, h = hand2["bbox"]
        cv2.rectangle(img, (x, y), (x+w, y+h),
                                   (0, 0, 255), 2)
        for point in hand2["lmList"]:
            cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)
        
cv2.imshow("Hands", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand2.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=1)
hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    bbox = hand["bbox"]        
    fingers = detector.fingersUp(hand)
    print(fingers)
    totalFingers = fingers.count(1)
    msg = "Fingers:" + str(totalFingers)
    cv2.putText(img, msg, (bbox[0]+100,bbox[1]-30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand3.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    bbox1 = hand1["bbox"]
    length, info, img = detector.findDistance(lmList1[4],lmList1[8],img)
    print(info)
    msg = "Dist:" + str(int(length))
    cv2.putText(img, msg, (bbox1[0]+100,bbox1[1]-30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)        

cv2.imshow("Hand", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hands3.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    if len(hands) == 2:
        hand2 = hands[1]
        lmList2 = hand2["lmList"]
        bbox2 = hand2["bbox"]
        length, info, img = detector.findDistance(lmList1[8],
                                                  lmList2[8], img)
        print(info)
        msg = "Dist:" + str(int(length))
        cv2.putText(img, msg,(bbox2[0]+100,bbox2[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
cv2.imshow("Hands", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

img = cv2.imread("images/hand2.jpg")
detector = HandDetector(detectionCon=0.5, maxHands=2)
hands, img = detector.findHands(img)
if hands:
    hand1 = hands[0]
    lmList1 = hand1["lmList"]
    angle, img = detector.findAngle(lmList1[9], lmList1[10],
                                    lmList1[11], img)
    print(angle)
    print(detector.angleCheck(angle, 150, addOn=20))
    print(detector.angleCheck(angle, 100, addOn=20))

cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)
while cap.isOpened():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        centerPoint1 = hand1["center"]
        cv2.circle(img, centerPoint1, 10, (0, 255, 255),
                   cv2.FILLED)
        if len(hands) == 2:
            hand2 = hands[1]
            centerPoint2 = hand2["center"]
            cv2.circle(img, centerPoint2, 10, (0, 255, 255),
                       cv2.FILLED)
            
    cv2.imshow("Hands", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
while cap.isOpened():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        msg = "Fingers:" + str(totalFingers)
        cv2.putText(img, msg, (bbox[0]+100,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Hand", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=2)
while cap.isOpened():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand1 = hands[0]
        lmList1 = hand1["lmList"]
        bbox1 = hand1["bbox"]
        length, info, img = detector.findDistance(lmList1[8],lmList1[12],img)
        msg = "Dist:" + str(int(length))
        cv2.putText(img, msg,(bbox1[0]+100,bbox1[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)        
        if len(hands) == 2:
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            length, info, img = detector.findDistance(lmList1[8],lmList2[8],img)
            msg = "Dist:" + str(int(length))
            cv2.putText(img, msg,(bbox2[0]+100,bbox2[1]-30),
                            cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Hands", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)
img = cv2.imread("images/Scissors.png")
msg = "None"
hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    fingers = detector.fingersUp(hand)
    print(fingers)
    totalFingers = fingers.count(1)
    if totalFingers == 5:
        msg = "Paper"
    if totalFingers == 0:
        msg = "Rock"
    if totalFingers == 2:
        if fingers[1] == 1 and fingers[2] == 1:
            msg = "Scissors"
    cv2.putText(img, msg, (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
            
cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
while cap.isOpened():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        print(totalFingers)
        msg = "None"
        if totalFingers == 5:
            msg = "Paper"
        if totalFingers == 0:
            msg = "Rock"
        if totalFingers == 2:
            if fingers[1] == 1 and fingers[2] == 1:
                msg = "Scissors"
        cv2.putText(img, msg, (bbox[0]+200,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
        
    cv2.imshow("Hand", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

detector = HandDetector(detectionCon=0.5, maxHands=1)
img = cv2.imread("images/OK.jpg")
hands, img = detector.findHands(img)
if hands:
    hand = hands[0]
    lmList1 = hand["lmList"]
    fingers = detector.fingersUp(hand)
    totalFingers = fingers.count(1)
    print(totalFingers)
    msg = "None"
    if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        length, info, img = detector.findDistance(lmList1[8],lmList1[4],img)
        print("Length:", length)
        if length <= 30:
            angle, img = detector.findAngle(lmList1[5], lmList1[6], lmList1[7],img)
            print("Angle:", angle)
            if detector.angleCheck(angle, 100, addOn=20):                    
                msg = "OK"
    cv2.putText(img, msg, (10, 30),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cv2.imshow("Hand", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
while cap.isOpened():
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]
        lmList1 = hand["lmList"]
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        print(totalFingers)
        msg = "None"
        if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            length, info, img = detector.findDistance(lmList1[8],lmList1[4],img)
            print("Length:", length)
            if length <= 30:
                angle, img = detector.findAngle(lmList1[5], lmList1[6], lmList1[7],img)
                print("Angle:", angle)
                if detector.angleCheck(angle, 100, addOn=20):                    
                    msg = "OK"
        cv2.putText(img, msg, (bbox[0]+200,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow("Hand", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
        
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/woman.jpg")
detector = PoseDetector(detectionCon=0.5, trackCon=0.5)
pose, img = detector.findPose(img, bboxWithHands=False)
if pose:
    x1, y1, w, h = pose["bbox"]
    cv2.rectangle(img, (x1, y1),
                       (x1 + w, y1 + h),
                       (255, 0, 255), 2)             
    center = pose["center"]
    cv2.circle(img, center, 15, (0, 255, 255), cv2.FILLED)

cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/woman2.jpg")
detector = PoseDetector()
pose = detector.findPose(img, draw=False)
if pose:
    lmList = pose["lmList"]
    for point in lmList:
        cv2.circle(img, point, 3, (0, 255, 255), cv2.FILLED)

cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle, img = detector.findAngle(lmList[24], lmList[26], lmList[28], img)
    print(angle)
    print(detector.angleCheck(angle, 140, addOn=20))
    print(detector.angleCheck(angle, 90, addOn=20))
    
cv2.imshow("Pose", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle = detector.findAngle(lmList[24], lmList[26], lmList[28])
    msg = str(int(angle))
    point1, point2, center = lmList[24], lmList[26], lmList[28]
    cv2.line(img, point1, point2, (255, 255, 255), 3)
    cv2.line(img, center, point2, (255, 255, 255), 3)
    cv2.circle(img, point1, 10, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, point1, 15, (0, 0, 255), 2)
    cv2.circle(img, point2, 10, (0, 255, 255), cv2.FILLED)
    cv2.circle(img, point2, 15, (0, 255, 255), 2)
    cv2.circle(img, center, 10, (0, 0, 255), cv2.FILLED)
    cv2.circle(img, center, 15, (0, 0, 255), 2)
    cv2.putText(img, msg, (10, 35),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Pose", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    length, distInfo, img = detector.findDistance(lmList[11], lmList[25], img)
    print(length, distInfo)

cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/fitness.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    length, distInfo = detector.findDistance(lmList[11], lmList[25])
    msg = str(int(length))
    point1, point2, center = distInfo
    cv2.line(img, point1, point2, (255, 0, 255), 3)
    cv2.circle(img, point1, 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, point2, 15, (255, 0, 255), cv2.FILLED)
    cv2.circle(img, center, 15, (0, 0, 255), cv2.FILLED)
    cv2.putText(img, msg, (10, 35),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    
cv2.imshow("Pose", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

cap = cv2.VideoCapture(0)
detector = PoseDetector()
while cap.isOpened():
    success, img = cap.read()
    pose, img = detector.findPose(img)
    if pose:
        x1, y1, w, h = pose["bbox"]
        cv2.rectangle(img, (x1, y1),
                           (x1 + w, y1 + h),
                           (255, 0, 255), 2)
        center = pose["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Pose", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/site_up.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle, img = detector.findAngle(lmList[11], lmList[23], lmList[25], img)
    print(angle)
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from cvzone.PoseModule import PoseDetector
import cv2

img = cv2.imread("images/push_up.jpg")
detector = PoseDetector()
pose, img = detector.findPose(img)
if pose:
    lmList = pose["lmList"]
    angle1, img = detector.findAngle(lmList[11], lmList[23], lmList[25], img)
    print(angle1)
    angle2, img = detector.findAngle(lmList[11], lmList[13], lmList[15], img)
    print(angle2)
    
cv2.imshow("Pose", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



