import sys
import os
from datetime import datetime
import cv2 as cv

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
face_detector = cv.CascadeClassifier(xml_filename)

names = {1: "Demming"}  # 將使用者 ID 聯結到使用者名稱

# 初始化辨識器物件，並載入訓練資料
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lbph_trainer.yml')

#test_path = './tester'  # 若使用的是你的臉，請取消註解
test_path = './demming_tester' # 使用提供的臉部影像
image_paths = [os.path.join(test_path, f) for f in os.listdir(test_path)]

# 執行人臉辨識並更新存取日誌檔案
for image in image_paths:
    predict_image = cv.imread(image, cv.IMREAD_GRAYSCALE)
    faces = face_detector.detectMultiScale(predict_image,
                                          scaleFactor=1.05,
                                          minNeighbors=5)
    for (x, y, w, h) in faces:
        print(f"\nAccess requested at {datetime.now()}.")
        face = cv.resize(predict_image[y:y + h, x:x + w], (100, 100))   
        predicted_id, dist = recognizer.predict(face)
        if predicted_id == 1 and dist <= 95:
            name = names[predicted_id]
            print("{} identified as {} with distance={}"
                  .format(image, name, round(dist, 1)))
            print(f"Access granted to {name} at {datetime.now()}.",
                  file=open('lab_access_log.txt', 'a'))
        else:
            name = 'unknown'
            print(f"{image} is {name}.")
        
        cv.rectangle(predict_image, (x, y), (x + w, y + h), 255, 2) # 繪製矩形
        cv.putText(predict_image, name, (x + 1, y + h -5),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, 255, 1) # 標示使用者名稱
        cv.imshow('ID', predict_image) # 顯示影像     
        cv.waitKey(2000) # 視窗停滯 2 秒
        cv.destroyAllWindows() # 關閉視窗
