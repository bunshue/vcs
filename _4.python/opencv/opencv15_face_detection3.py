import cv2
import numpy as np

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

# OpenCV 人臉識別分類器
xml_filename1 = 'C:/_git/vcs/_1.data/______test_files1/_material/_face-detection/haarcascades/haarcascade_frontalface_default.xml'
#face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
face_classifier = cv2.CascadeClassifier(xml_filename1)

vid = cv2.VideoCapture(video_filename)

#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    if ret == True:
        #frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2))) #調整畫面大小
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('Video', frame)    # 顯示圖片, 彩色

        k = cv2.waitKey(1)
        if k == 27:     #ESC
            break
        elif k == ord('q'): # 若按下 q 鍵則離開迴圈
            break
        elif k == ord('s'): # 若按下 s 鍵則存圖
            image_filename = 'Image_' + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '.jpg';
            cv2.imwrite(image_filename, frame)
            print('已存圖')
    else:
        break

# 釋放所有資源
vid.release()
cv2.destroyAllWindows() # 關閉所有 OpenCV 視窗

    

    


