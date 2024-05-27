import cv2
# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread('test.jpg')    # 讀取圖片
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 轉成灰階圖片
# 偵測臉部
faces = face_cascade.detectMultiScale(gray,
    scaleFactor=1.1, minNeighbors=3, minSize=(40, 40))
# 繪製人臉區域的方框
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.namedWindow('Detect')
cv2.imshow('Detect', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

