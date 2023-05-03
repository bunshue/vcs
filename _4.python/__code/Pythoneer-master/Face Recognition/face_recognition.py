import cv2
import numpy as np

filename = 'C:/______test_files2/human2.jpg'

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

'''
#影片
vid = cv2.VideoCapture('spiderman.mp4')
#In the [your_file_name] mention the Video File that you want to process and detect the Face in

while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)       
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)        
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) == 27:
        break
vid.release()
'''

#圖片
image = cv2.imread(filename)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    #設定圖片顏色, 先將圖片轉成灰階

faces = face_cascade.detectMultiScale(gray, 1.2, 3)
#1.2 表示每次影像尺寸減小的比例
#3 表示每一個目標至少要被檢測到4次才算是真正的目標
#faces表示檢測到的人臉目標list

for (x,y,w,h) in faces:
    cv2.rectangle(image, (x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]

cv2.imshow('image', image)

#另存新檔
#cv2.imwrite('aaaaa.jpg', image)

print('wait kere')
cv2.waitKey(0)
print('收到按鍵')
cv2.destroyAllWindows() #銷毀建立的物件

