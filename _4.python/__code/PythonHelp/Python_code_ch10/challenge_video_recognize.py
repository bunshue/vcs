import cv2 as cv

names = {1: "Demming"}  # 將使用者 ID 聯結到使用者名稱

xml_filename = "C:/_git/vcs/_4.python/opencv/data/_xml/haarcascades/haarcascade_frontalface_default.xml"
detector = cv.CascadeClassifier(xml_filename)

# 初始化辨識器物件，並載入訓練資料
recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read('lbph_trainer.yml')

#設定視訊鏡頭
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cloud not open video device.")
#cap.set(3,320) # 設定螢幕寬度
#cap.set(4,240) # 設定螢幕高度

while True:
    _, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    face_rects = detector.detectMultiScale(frame, scaleFactor=1.2,
                                           minNeighbors=5)    

    for (x, y, w, h) in face_rects:
        #縮放影像使它變成能訓練的大小
        gray_resize = cv.resize(gray[y:y+h,x:x+w],
                                (100,100),
                                cv.INTER_LINEAR)
        predicted_id, dist = recognizer.predict(gray_resize)
        if predicted_id ==1 and dist <= 110:
            name = names[predicted_id]
        else:
            name = 'unknown'
        cv.rectangle(frame, (x,y), (x+w, y+h), (255, 255, 0), 2)
        cv.putText(frame, name, (x+1, y+h-5),
                  cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,0), 1)
        # 顯示畫面
        cv.imshow('frame', frame)
        
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 退出視訊鏡頭
cap.release()
cv.destroyAllWindows()
