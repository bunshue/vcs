# CH14 AI整合實戰（一）：手勢操控、健身教練與刷臉簽到

print("------------------------------------------------------------")  # 60個

#14-1 AI整合實戰：手勢操控


from cvzone.HandTrackingModule import HandDetector
import cv2
import turtle

print('手勢偵測操控海龜繪圖')

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
screen = turtle.Screen()
screen.setup(startx=20, starty=50)
msg = "Stop"

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        if totalFingers == 0: 
            msg = "Stop"
        if totalFingers == 1:
            if fingers[0] == 1:
                if msg != "TurnRight":
                    msg = "TurnRight"
                    turtle.right(90) 
        if totalFingers == 2:
            if fingers[1] == 1 and fingers[2] == 1:
                if msg != "Forward":
                    msg = "Forward"
                    turtle.forward(50)               
        if totalFingers == 5:
            break
        cv2.putText(img, msg, (bbox[0]+100,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    else:
        msg = "Stop"
    print(msg)    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
turtle.bye()        
cap.release()
cv2.destroyAllWindows()



print("------------------------------------------------------------")  # 60個


print('手勢偵測操控PowerPoint')


#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-1-2.py

from cvzone.HandTrackingModule import HandDetector
import cv2, os
from win32com.client import Dispatch

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.5, maxHands=1)
app = Dispatch("PowerPoint.Application")
app.Visible = 1
pptx = app.Presentations.Open(os.getcwd()+"/Turtle.pptx")
msg = "Stop"
isRun = False
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        bbox = hand["bbox"]        
        fingers = detector.fingersUp(hand)
        totalFingers = fingers.count(1)
        if totalFingers == 0: 
            msg = "Stop"
        if totalFingers == 1:
            if fingers[0] == 1:
                if msg != "Next" and isRun:
                    msg = "Next"
                    pptx.SlideShowWindow.View.Next()
            if fingers[1] == 1:
                if msg != "Previous" and isRun:
                    msg = "Previous"
                    pptx.SlideShowWindow.View.Previous()    
        if totalFingers == 2:
            if fingers[1] == 1 and fingers[2] == 1:
                msg = "Run"
                pptx.SlideShowSettings.Run()
                isRun = True
        if totalFingers == 5:
            if isRun:
                pptx.SlideShowWindow.View.Exit()
            pptx.Close() 
            break
        cv2.putText(img, msg, (bbox[0]+100,bbox[1]-30),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    else:
        msg = "Stop"
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

os.system('taskkill /F /IM POWERPNT.EXE')  #app.Quit() not work
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-2-1.py

#14-2 AI整合實戰：健身教練

from cvzone.PoseModule import PoseDetector
import cv2
import numpy as np

cap = cv2.VideoCapture("media/Site_up.mp4")
detector = PoseDetector()
dir = 0  # 0: 仰臥 1: 起坐
count = 0
while True:
    success, img = cap.read()
    if success:
        h, w, c = img.shape
        pose, img = detector.findPose(img, draw=True)
        if pose:
            lmList = pose["lmList"]
            angle, img = detector.findAngle(lmList[12], lmList[24],
                                            lmList[26], img)
            # 顯示進度條
            bar = np.interp(angle, (20, 100), (w//2-100, w//2+100))
            cv2.rectangle(img, (w//2-100, h-150), (int(bar), h-100),
                               (0, 255, 0), cv2.FILLED)
            if angle <= 50:   # 目前狀態:起坐
                if dir == 0:  # 之阱狀態:仰臥
                    count = count + 0.5
                    dir = 1   # 更新狀態:起坐
            if angle >= 90:   # 目前狀態:仰臥
                if dir == 1:  # 之前狀態:起坐
                    count = count + 0.5
                    dir = 0   # 更新狀態:仰臥
            msg = str(int(count))        
            cv2.putText(img, msg, (w-150, 150),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        5, (255, 255, 255), 20)
        cv2.imshow("Pose", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-2-2.py

from cvzone.PoseModule import PoseDetector
import cv2
import numpy as np

cap = cv2.VideoCapture("media/Push_Up.mp4")
detector = PoseDetector()
dir = 0  # 0: 挺身 1: 伏地
count = 0
while True:
    success, img = cap.read()
    if success:
        h, w, c = img.shape
        pose, img = detector.findPose(img, draw=True)
        if pose:
            lmList = pose["lmList"]
            angle1, img = detector.findAngle(lmList[11], lmList[23],
                                             lmList[25], img)
            angle2, img = detector.findAngle(lmList[11], lmList[13],
                                             lmList[15], img)
            # 顯示進度條
            bar = np.interp(angle2, (60, 175), (w//2-100, w//2+100))
            cv2.rectangle(img, (w//2-100, h-150), (int(bar), h-100),
                               (0, 255, 0), cv2.FILLED)
            print(int(angle1), int(angle2))
            # 目前狀態::伏地
            if angle2 <= 110 and angle1 >= 165 and angle1 <= 180:
                if dir == 0:   # 之前狀態:挺身
                    count = count + 0.5
                    dir = 1    # 更新狀態:伏地
            # 目前狀態::挺身
            if angle2 >= 160 and angle1 >= 150 and angle1 <= 180:
                if dir == 1:   # 之前狀態:伏地
                    count = count + 0.5
                    dir = 0    # 更新狀態:挺身
            msg = str(int(count))         
            cv2.putText(img, msg, (w-150, 150),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        5, (255, 0, 255), 20)
        cv2.imshow("Pose", img)
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-2-3.py

from cvzone.PoseModule import PoseDetector
import cv2
import numpy as np

cap = cv2.VideoCapture("media/Squat.mp4")
detector = PoseDetector()
dir = 0  # 0: 站起  1: 蹲下
count = 0
while True:
    success, img = cap.read()
    if success:
        h, w, c = img.shape
        pose, img = detector.findPose(img, draw=True)
        if pose:
            lmList = pose["lmList"]
            angle, img = detector.findAngle(lmList[24], lmList[26],
                                            lmList[28], img)
            # 顯示進度條
            bar = np.interp(angle, (95, 175), (w//2-100, w//2+100))
            cv2.rectangle(img, (w//2-100, 50), (int(bar), 100),
                               (0, 255, 0), cv2.FILLED)
            if angle <= 110:  # 目前狀態:蹲下
                if dir == 0:  # 之前狀態:站起
                    count = count + 0.5
                    dir = 1   # 更新狀態:蹲下
            if angle >= 165:  # 目前狀態:站起
                if dir == 1:  # 之前狀態:蹲下
                    count = count + 0.5
                    dir = 0   # 更新狀態:站起
            msg = str(int(count))        
            cv2.putText(img, msg, (30, 150),
                        cv2.FONT_HERSHEY_SIMPLEX, 5,
                        (255, 255, 255), 20)
        cv2.imshow("Pose", img)        
    else:
        break
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

#14-3 AI整合實戰：刷臉簽到

#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-3.py

import face_recognition
import cv2
import pickle

known_face_list = [
    {
        "name": "Mary",
        "filename": "mary.jpg",
        "face_encoding": None
    },
    {
        "name": "Jane",
        "filename": "jane.jpg",
        "face_encoding": None      
    },
    {
        "name": "Grace",
        "filename": "grace.jpg",
        "face_encoding": None      
    }
]

for data in known_face_list:
    fname = "images/"+data["filename"]
    print("人臉:[", fname, "]編碼中...")
    img = cv2.imread(fname)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    encodings = face_recognition.face_encodings(rgb_img)
    data["face_encoding"] = encodings[0]
    print("人臉:[", fname, "]編碼完成...")
     
with open("faces_encoding.dat", "wb") as f:
    pickle.dump(known_face_list, f)
print("人臉編碼已經成功寫入faces_encoding.dat...")


print("------------------------------------------------------------")  # 60個

#14-3 AI整合實戰：刷臉簽到
#檔案 : C:\_git\vcs\_4.python\__code\看圖學Python人工智慧程式設計\ch14\ch14-3a.py

import face_recognition
import cv2
import numpy as np
import pickle

with open("faces_encoding.dat", "rb") as f:
    known_face_list = pickle.load(f)    
known_face_encodings = []
for data in known_face_list:
    known_face_encodings.append(data["face_encoding"])

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb_img)
    encodings = face_recognition.face_encodings(rgb_img,
                                                locations)
    for idx, encoding in enumerate(encodings):
        top, right, bottom, left = locations[idx]        
        distances = face_recognition.face_distance(
                           known_face_encodings, encoding)
        best_match_index = np.argmin(distances)
        if distances[best_match_index] < 0.4:
            name = known_face_list[best_match_index]["name"]
        else:
            name = "Unknown"
        cv2.rectangle(img, (left, top), (right, bottom),
                                  (0, 0, 255), 2)
        cv2.rectangle(img, (left, bottom-35), (right, bottom),
                                  (0, 0, 255), cv2.FILLED) 
        cv2.putText(img, name, (left+6, bottom-6),
                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 255, 255), 1)
    cv2.imshow("Face", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個


