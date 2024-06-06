"""
螢幕錄影


"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import time
import threading
import cv2
import numpy as np
from PIL import ImageGrab

class VideoCapThread(threading.Thread):

    def __init__(self, video_file='record.avi'):
        threading.Thread.__init__(self)
        self.b_record = True
        self.video = cv2.VideoWriter(video_file, 
                cv2.VideoWriter_fourcc(*'XVID'),
                20, ImageGrab.grab().size)  # 幀率為32，可以調節

    def run(self):
        while self.b_record:
            im = ImageGrab.grab()
            imm = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR)
            self.video.write(imm)
        self.video.release()
        cv2.destroyAllWindows()


    def stop_record(self):
        self.b_record = False

avi_file = 'tmp_screen_recorder_01.avi'

t1 = VideoCapThread(avi_file)
t1.start()

import datetime
now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)
record_time_st = time.time()

for _ in range(300):
    print(_, end = " ")
    time.sleep(1)  # 錄製 5 min
    
t1.stop_record()

now = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print("現在時間 :", now)

record_time_elapsed = time.time() - record_time_st
print('作業時間 :', format(record_time_elapsed, ".2f"), '秒')

# delay 很嚴重 
#300 sec => 378 sec, 不可用

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




