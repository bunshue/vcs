import cv2
import numpy as np 

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

#cap = cv2.VideoCapture(video_filename)  # 開啟影片
cap = cv2.VideoCapture("video.avi")  # 開啟影片

if not cap.isOpened():
  print("開啟影片失敗")
  sys.exit()

frameNum = 0 

#阅读直到视频完成
while True:
  # 获取一帧
  ret, frame = cap.read()  # 從影片擷取一張影像
  frameNum += 1
  if ret == True:   
    tempframe = frame    
    if(frameNum==1):
        previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
        print(111)
    if(frameNum>=2):
        currentframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)        
        currentframe = cv2.absdiff(currentframe,previousframe) 
        median = cv2.medianBlur(currentframe,3)        
        ret, threshold_frame = cv2.threshold(currentframe, 20, 255, cv2.THRESH_BINARY)
        gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)  #執行高斯模糊化
 
        print(222) 
        # 显示结果帧
        cv2.imshow('Original',frame) 
        cv2.imshow('Frame',currentframe) 
        cv2.imshow('median',median) 
 
        # 按键盘上的Q键退出
        if cv2.waitKey(33) & 0xFF == ord('q'):
          break    
    previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
  # 跳出循环
  else: 
    break 

cap.release() 
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

