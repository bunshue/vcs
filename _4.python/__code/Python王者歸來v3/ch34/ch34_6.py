# ch34_6.py
import cv2
import os

if not os.path.exists("facedata"):                  # 如果不存在資料夾
    os.mkdir("facedata")                            # 就建立facedata

pictPath = r'C:\opencv\data\haarcascade_frontalface_alt2.xml'
face_cascade = cv2.CascadeClassifier(pictPath)      # 建立辨識檔案物件
img = cv2.imread("g5.jpg")                          # 讀取影像
faces = face_cascade.detectMultiScale(img, scaleFactor=1.1,
        minNeighbors = 3, minSize=(20,20))          # 偵測影像
# 標註右下角底色是黃色
cv2.rectangle(img, (img.shape[1]-140, img.shape[0]-20),         
              (img.shape[1],img.shape[0]), (0,255,255), -1)
# 標註找到多少的人臉
cv2.putText(img, "Finding " + str(len(faces)) + " face",
            (img.shape[1]-135, img.shape[0]-5),
            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
# 將人臉框起來, 由於有可能找到好幾個臉所以用迴圈繪出來
# 同時將影像儲存在facedata資料夾, 但是必須先建立此資料夾
num = 1                                             # 檔名編號
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)  # 藍色框住人臉
    filename = "facedata\\face" + str(num) + ".jpg" # 路徑 + 檔名
    imageCrop = img[y:y+h,x:x+w]                    # 裁切
    imageResize = cv2.resize(imageCrop,(160,160))   # 重製大小
    cv2.imwrite(filename, imageResize)              # 儲存影像
    num += 1                                        # 檔案編號                                
    
cv2.imshow("Face", img)                             # 顯示影像
cv2.waitKey(0)
cv2.destroyAllWindows()





 
