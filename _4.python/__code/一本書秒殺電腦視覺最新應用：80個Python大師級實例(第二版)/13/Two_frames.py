import cv2
import numpy as np 
 
cap = cv2.VideoCapture("video.avi")
# 检查相机是否打开成功
if (cap.isOpened()== False): 
  print("打开视频流或文件时出错")
frameNum = 0 
#阅读直到视频完成
while(cap.isOpened()):
  # 获取一帧
  ret, frame = cap.read()
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
        gauss_image = cv2.GaussianBlur(threshold_frame, (3, 3), 0)
 
        print(222) 
        # 显示结果帧
        cv2.imshow('原图',frame) 
        cv2.imshow('Frame',currentframe) 
        cv2.imshow('median',median) 
 
        # 按键盘上的Q键退出
        if cv2.waitKey(33) & 0xFF == ord('q'):
          break    
    previousframe = cv2.cvtColor(tempframe, cv2.COLOR_BGR2GRAY)
  # 跳出循环
  else: 
    break 
# 完成所有操作后，释放video capture对象
cap.release() 
# 关闭所有帧
cv2.destroyAllWindows()
