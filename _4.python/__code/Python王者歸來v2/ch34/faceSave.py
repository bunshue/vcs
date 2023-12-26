# faceSave.py
import cv2
from PIL import Image

ID = input("請輸入身份證字號 = ")               # 讀取所輸入的身分證字號
print("臉形檔案將儲存在 ", ID + ".jpg")
faceFile = ID + ".jpg"                          # 未來的臉形檔案                       

pictPath = r'C:\opencv\sources\data\haarcascades\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)  # 建立辨識檔案物件
cv2.namedWindow("Photo")
cap = cv2.VideoCapture(0)                       # 開啟攝影機
while(cap.isOpened()):                          # 如果攝影機有開啟就執行迴圈
    ret, img = cap.read()                       # 讀取影像
    cv2.imshow("Photo", img)                    # 顯示影像在OpenCV視窗
    if ret == True:                             # 讀取影像如果成功
        key = cv2.waitKey(200)                  # 0.2秒檢查一次
        if key == ord("a") or key == ord("A"):  # 如果按A或a
            cv2.imwrite("photo.jpg", img)       # 將影像寫入photo.jpg           
            break
cap.release()                                   # 關閉攝影機

faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20),
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Find " + str(len(faces)) + " face",
            (img.shape[1]-110, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
    myimg = Image.open("photo.jpg")                     # PIL模組開啟
    imgCrop = myimg.crop((x, y, x+w, y+h))              # 裁切
    imgResize = imgCrop.resize((150,150), Image.ANTIALIAS)
    imgResize.save(faceFile)                            # 儲存檔案
    
cv2.namedWindow("FaceRecognition", cv2.WINDOW_NORMAL)
cv2.imshow("FaceRecognition", img)


