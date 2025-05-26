import os
import time
from playsound import playsound
import cv2 as cv

xml_filename1 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_cascade = cv.CascadeClassifier(xml_filename1)

xml_filename2 = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_eye.xml"
eye_cascade = cv.CascadeClassifier(xml_filename2)

# 切換到放置影像的資料夾
os.chdir('corridor_5')
contents = sorted(os.listdir())

# 偵測人臉並判斷是否開火
for image in contents:
    discharge_weapon = True
   
    img_gray = cv.imread(image, cv.IMREAD_GRAYSCALE)
    height, width = img_gray.shape
    cv.imshow(f'Motion detected {image}', img_gray)
    cv.waitKey(2000)
    cv.destroyWindow(f'Motion detected {image}')
    print('a')

    # 找到偵測到的人臉矩形
    face_rect_list = []
    print('b')
    face_rect_list.append(face_cascade.detectMultiScale(image=img_gray,
                                                        scaleFactor=1.1,
                                                        minNeighbors=5))
    print('c')

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
        playsound("tone.wav", block=False) # 播放音訊檔案
        cv.imshow('Detected Faces', img_gray) # 顯示當前偵測完成之影像
        cv.waitKey(2000) # 視窗停滯 2 秒
        cv.destroyWindow('Detected Faces') # 關閉視窗
        time.sleep(5) # 暫停程式 5 秒

    else:
        print(f"No face in {image}. Discharging weapon!") # 印出開火訊息
        cv.putText(img_gray, 'FIRE!', (int(width / 2) - 20, int(height / 2)),
                   cv.FONT_HERSHEY_PLAIN, 3, 255, 3)
        playsound("gunfire.wav", block=False) # 播放槍聲檔案
        cv.imshow('Mutant', img_gray) # 顯示當前偵測完成之影像
        cv.waitKey(2000) # 視窗停滯 2 秒
        cv.destroyWindow('Mutant') # 關閉視窗
        time.sleep(3)  # 暫停程式 3 秒
