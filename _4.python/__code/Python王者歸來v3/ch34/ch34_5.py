# ch34_5.py
import cv2

pictPath = r'C:\opencv\data\haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(pictPath)          # 建立辨識物件
img = cv2.imread("g2.jpg")                              # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)      # 藍色框住人臉
cv2.imshow("Face", img)                                 # 顯示影像

cv2.waitKey(0)
cv2.destroyAllWindows()






 
