import os
import sys
import cv2 as cv

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_detector = cv.CascadeClassifier(xml_filename)

# 打開視訊鏡頭
cap = cv.VideoCapture(0)
if not cap.isOpened(): 
    print("Could not open video device.")
cap.set(3, 640)  # 畫面寬度
cap.set(4, 480)  # 畫面高度

# 向使用者解釋程序
print("""當螢幕提示時，請輸入你的訊息。\n
      然後取下眼鏡，直視攝影鏡頭。\n
      請做出多種不同的表情，包括正常的、快樂的、悲傷的、疲倦的，\n
      直到聽到提示喊停為止。""")

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

cap.release()
cv.destroyAllWindows()
