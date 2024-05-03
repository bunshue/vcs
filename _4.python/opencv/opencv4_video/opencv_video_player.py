import cv2

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print('------------------------------------------------------------')	#60個

print('播完影片不會有錯誤訊息')

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
      cv2.imshow("Frame", frame)
  if cv2.waitKey(1) & 0xFF == ord("q"):
      break

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

# 開啟影片檔案
filename = 'C:/dddddddddd/____download/V000000119.mp4'

'''
cap = cv2.VideoCapture(filename)

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
  ret, frame = cap.read()

  cv2.imshow('frame',frame)

  k = cv2.waitKey(1)
  if k == 27:     #ESC
    break
  elif k == ord('q'): # 若按下 q 鍵則離開迴圈
    break
  elif k == ord('s'): # 若按下 s 鍵則存圖
    cv2.imwrite('video_snapshot.jpg', frame)

cap.release()
cv2.destroyAllWindows()
'''


#播放视频，并把每帧保存成图片：

#cap = cv2.VideoCapture(filename,'utf-8')
cap = cv2.VideoCapture(filename)

fps = cap.get(cv2.CAP_PROP_FPS)
size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

success, frame = cap.read()
i = 0
'''
while success:
    cv2.imshow("video",frame)
    #cv2.waitKey(1000/int(fps))
    #cv2.imwrite("./img/%d.jpg" % i,frame)
    i = i + 1
    success, frame = cap.read()
'''


'''
filename = 'C:/_git/vcs/_1.data/______test_files1/_video/鹿港.mp4'

video = cv2.VideoCapture(filename)   #, 'utf-8')

fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

success, frame = video.read()
i = 0
while success:
    cv2.imshow("video",frame)
    #cv2.waitKey(1000/int(fps))
    #cv2.waitKey(20)
    cv2.imwrite("C:/_git/vcs/_1.data/______test_files2/%05d.jpg" % i, frame)
    i = i + 1
    success, frame = video.read()
video.release();

print('共有' + str(i) + '張圖片')
'''



