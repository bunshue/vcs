import cv2
import datetime

infile = "testmovie1.mp4"
cap = cv2.VideoCapture(infile)                  #載入檔案
frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)       #總影格數
fps = cap.get(cv2.CAP_PROP_FPS)                 #影格速率
sec = int(frame / fps)                          #播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
print("播放時間=",timestr)
