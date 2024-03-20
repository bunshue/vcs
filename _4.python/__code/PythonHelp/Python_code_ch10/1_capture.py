import os
import pyttsx3
import cv2 as cv
from playsound import playsound

xml_filename = r'C:\_git\vcs\_4.python\_data\haarcascade_frontalface_default.xml'

# 設定音訊
engine = pyttsx3.init()
engine.setProperty('rate', 145) # 設定語速
engine.setProperty('volume', 1.0) # 設定音量 (1.0 為最大值)

# 設定音訊檔案路徑
root_dir = os.path.abspath('.')
tone_path = os.path.join(root_dir, 'tone.wav')

# 設定 Haar 分類器檔案路徑
face_detector = cv.CascadeClassifier(xml_filename)

# 打開視訊鏡頭
cap = cv.VideoCapture(0)
if not cap.isOpened(): 
    print("Could not open video device.")
cap.set(3, 640)  # 畫面寬度
cap.set(4, 480)  # 畫面高度

# 向使用者解釋程序
engine.say("當螢幕提示時，請輸入你的訊息。\
           然後取下眼鏡，直視攝影鏡頭。\
           請做出多種不同的表情，包括正常的、快樂的、悲傷的、疲倦的，\
           直到聽到提示喊停為止。")
engine.runAndWait()
name = input("\nEnter last name: ")
user_id = input("Enter assigned ID Number: ")
print("\nCapturing face. Look at the camera now!")

# 新建資料夾用於放置影像
if not os.path.isdir('trainer'):
    os.mkdir('trainer')
os.chdir('trainer')

frame_count = 0
 
while True:
    # 獲取畫面影像，共 30 張
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rects = face_detector.detectMultiScale(gray, scaleFactor=1.2,
                                                minNeighbors=5)     
    for (x, y, w, h) in face_rects:
        frame_count += 1 # 增加畫面數計數
        cv.imwrite(str(name) + '.' + str(user_id) + '.'
                   + str(frame_count) + '.jpg', gray[y:y+h, x:x+w]) # 儲存影像至資料夾
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # 畫出矩形
        cv.imshow('image', frame)  # 顯示影像
        cv.waitKey(400) # 視窗停滯 0.4 秒
    if frame_count >= 30:
        break
     
print("\nImage collection complete. Exiting...")
playsound(tone_path, block=False)
cap.release()
cv.destroyAllWindows()
