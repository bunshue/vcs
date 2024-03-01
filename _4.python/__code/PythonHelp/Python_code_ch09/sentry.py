import os
import time
from datetime import datetime
from playsound import playsound
import pyttsx3
import cv2 as cv

# 設定語音引擎
engine = pyttsx3.init()
engine.setProperty('rate', 145)  # 設定語速
engine.setProperty('volume', 1.0)  # 設定音量 (1.0 為最大值)

# 設定音訊檔案路徑
root_dir = os.path.abspath('.')
gunfire_path = os.path.join(root_dir, 'gunfire.wav')
tone_path = os.path.join(root_dir, 'tone.wav')

# 設定 Haar 階層式分類器檔案路徑
path = "C:/Users/Admin/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/"
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(path + 'haarcascade_eye.xml')

# 切換到放置影像的資料夾
os.chdir('corridor_5')
contents = sorted(os.listdir())

# 偵測人臉並判斷是否開火
for image in contents:
    print(f"\nMotion detected...{datetime.now()}")
    discharge_weapon = True
    engine.say("你已經進入射擊區域。\
               請停止腳步，立即把頭轉向槍的位置。 \
               當你聽到聲響，你只有 5 秒鐘的時間能通過。")
    engine.runAndWait()
    time.sleep(3)
    
    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    height, width = img_gray.shape
    cv.imshow(f'Motion detected {image}', img_gray)
    cv.waitKey(2000)
    cv.destroyWindow(f'Motion detected {image}')

    # 找到偵測到的人臉矩形
    face_rect_list = []  
    face_rect_list.append(face_cascade.detectMultiScale(image=img_gray,
                                                        scaleFactor=1.1,
                                                        minNeighbors=5))
    print(f"Searching {image} for eyes.")
    for rect in face_rect_list:
        for (x, y, w, h) in rect:
            rect_4_eyes = img_gray[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(image=rect_4_eyes,
                                                scaleFactor=1.05,
                                                minNeighbors=2)
            for (xe, ye, we, he) in eyes:
                print("Eye detected.")
                center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
                radius = int((we + he) / 3)
                cv.circle(rect_4_eyes, center, radius, 255, 2)
                cv.rectangle(img_gray, (x, y), (x+w, y+h), (255, 255, 255), 2)
                discharge_weapon = False
                break
            
    if discharge_weapon == False:
        playsound(tone_path, block=False) # 播放音訊檔案
        cv.imshow('Detected Faces', img_gray) # 顯示當前偵測完成之影像
        cv.waitKey(2000) # 視窗停滯 2 秒
        cv.destroyWindow('Detected Faces') # 關閉視窗
        time.sleep(5) # 暫停程式 5 秒

    else:
        print(f"No face in {image}. Discharging weapon!") # 印出開火訊息
        cv.putText(img_gray, 'FIRE!', (int(width / 2) - 20, int(height / 2)),
                   cv.FONT_HERSHEY_PLAIN, 3, 255, 3)
        playsound(gunfire_path, block=False) # 播放槍聲檔案
        cv.imshow('Mutant', img_gray) # 顯示當前偵測完成之影像
        cv.waitKey(2000) # 視窗停滯 2 秒
        cv.destroyWindow('Mutant') # 關閉視窗
        time.sleep(3)  # 暫停程式 3 秒

engine.stop()  # 停止 pyttsx3 引擎
