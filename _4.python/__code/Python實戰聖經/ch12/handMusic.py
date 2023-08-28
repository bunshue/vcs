from cvzone.HandTrackingModule import HandDetector
import cv2
from pygame import mixer
import glob

def playmp3(playsong): #播放新曲
    mixer.music.stop()
    mixer.music.load(playsong)   
    mixer.music.play(loops=-1)  
  
mp3files = glob.glob('mp3\*.mp3')
premusic = 0
count = 0
mixer.init()

cap = cv2.VideoCapture(0)
detector = HandDetector(minTrackCon=0.5, maxHands=2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    if lmList:
        bbox = bboxInfo['bbox']
        fingers = detector.fingersUp()
        totalFingers = fingers.count(1)
        if totalFingers>0 and totalFingers<5:  
            if (totalFingers-1) != premusic:  #手指數有改變
                if count>=3:  #連續3次手指數相同
                    playmp3(mp3files[totalFingers-1])
                    premusic = totalFingers-1
                else:  #相同手指數加1
                    count += 1
            else:
                count = 0  #手指數歸零
        elif totalFingers==5:
            mixer.music.stop()
            premusic = ''
            count = 0

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

