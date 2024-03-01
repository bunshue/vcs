import cv2 as cv

# 設定 Haar 階層式分類器檔案路徑
path = "C:/Users/Admin/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/"
face_cascade = cv.CascadeClassifier(path + 'haarcascade_frontalface_alt.xml')

cap = cv.VideoCapture(0)

while True:
    # 偵測人臉
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(frame, scaleFactor=1.2,
                                               minNeighbors=4)    

    for (x, y, w, h) in face_rects:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    # 顯示畫面
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 退出視訊鏡頭
cap.release()
cv.destroyAllWindows()
