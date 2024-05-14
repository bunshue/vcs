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

print('播放影片')

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret:
      cv2.imshow("Frame", frame)
  k = cv2.waitKey(1)
  if k == 27:     #ESC
    break
  elif k == ord('q'): # 若按下 q 鍵則離開迴圈
    break
  elif k == ord('s'): # 若按下 s 鍵則存圖
    cv2.imwrite('video_snapshot.jpg', frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

#播放视频，并把每帧保存成图片：

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

fps = cap.get(cv2.CAP_PROP_FPS)

success, frame = cap.read()
i = 0
while success:
    #cv2.imshow("video",frame)
    #cv2.waitKey(int(1000/fps))#若要正常顯示，則需要delay
    i = i + 1
    cv2.imwrite("./tmp_video_clip_%04d.jpg" % i,frame)
    success, frame = cap.read()
    #if i > 10:
      #break

print('共有' + str(i) + '張圖片')

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


