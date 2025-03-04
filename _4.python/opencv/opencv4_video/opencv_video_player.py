import cv2

ESC = 27
SPACE = 32

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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

print("------------------------------------------------------------")  # 60個

print("使用 cv2 取得一個avi檔的播放時間")
import datetime

filename = "C:/_git/vcs/_1.data/______test_files1/_video/i2c.avi"

cap = cv2.VideoCapture(filename)

frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 總影格數
fps = cap.get(cv2.CAP_PROP_FPS)  # 影格速率
sec = int(frame / fps)  # 播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  # 轉換成時分秒格式
print("播放時間=", timestr)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pathlib import Path
import datetime

infolder = "C:/_git/vcs/_1.data/______test_files1/_video"
extlist = ["*.mp4", "*.mov"]


# 【函數: 取得影片檔的播放時間】
def getplaytime(readfile):
    try:
        cap = cv2.VideoCapture(readfile)  # 載入檔案
        frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 總影格數
        fps = cap.get(cv2.CAP_PROP_FPS)  # 影格速率
        sec = int(frame / fps)  # 播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  # 轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"


# 【函數: 搜尋資料夾與子資料夾的影片檔】
def findfiles(infolder):
    totalsec = 0
    msg = ""
    for ext in extlist:  # 以多個副檔名調查
        filelist = []
        for p in Path(infolder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
            filelist.append(str(p))  # 新增至列表
        for filename in sorted(filelist):  # 再替每個檔案排序
            val1, val2 = getplaytime(filename)
            totalsec += val1
            msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=totalsec))
    msg += "總播放時間 " + totaltimestr
    return msg


# 【執行函數】
msg = findfiles(infolder)
print(msg)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("播放影片")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

cap = cv2.VideoCapture(video_filename)  # 開啟影片

# 以迴圈從影片檔案讀取影格，並顯示出來
while cap.isOpened():
    ret, frame = cap.read()  # 從影片擷取一張影像
    if ret == True:
        # frame = cv2.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))    #調整畫面大小
        # frame = cv2.Canny(frame,100,200)  #加上Canny處理
        cv2.imshow("Video Player", frame)
    else:
        break

    k = cv2.waitKey(1)
    if k == 27:  # ESC
        break
    elif k == ord("q"):  # 若按下 q 鍵則離開迴圈
        break
    elif k == ord("s"):  # 若按下 s 鍵則存圖
        cv2.imwrite("video_snapshot.jpg", frame)

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 播放视频，并把每帧保存成图片：

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

cap = cv2.VideoCapture(video_filename)

fps = cap.get(cv2.CAP_PROP_FPS)

success, frame = cap.read()
i = 0
while success:
    # cv2.imshow("video",frame)
    # cv2.waitKey(int(1000/fps))#若要正常顯示，則需要delay
    i = i + 1
    # many
    # cv2.imwrite("./tmp_video_clip_%04d.jpg" % i, frame)
    success, frame = cap.read()
    # if i > 10:
    # break

print("共有" + str(i) + "張圖片")

cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# OpenCV如何讀取特定時間區段？

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"

# 影片捕捉物件
cap = cv2.VideoCapture(video_filename)
fps = cap.get(cv2.CAP_PROP_FPS)

# 設定開始時間(秒)
start_time_sec = 3
start_frame = int(start_time_sec * fps)
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

# 設定結束時間(秒)
end_time_sec = 15
end_frame = int(end_time_sec * fps)

# 如果還沒處理到結束的frame位置則...
while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
    ret, frame = cap.read()

    if not ret:
        break  # 當所有幀都被讀取完畢時退出循環

    # 在這裡處理每一幀的操作，例如顯示視頻，保存幀等
    # print('a', end = ' ')

# 釋放資源
cap.release()
cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("影片去背景")

video_filename = "C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4"
# video_filename = "D:\______大整理/Carreno Busta vs Kei Nishikori Final Set Tie Break HD.mp4"

cap = cv2.VideoCapture(video_filename)

fgbg = cv2.createBackgroundSubtractorMOG2()

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    fgmask = fgbg.apply(frame)

    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, element)

    foreground = cv2.bitwise_and(frame, frame, mask=fgmask)

    cv2.imshow("Foreground Detection", foreground)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
