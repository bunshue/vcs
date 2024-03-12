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
                32, ImageGrab.grab().size)  # 幀率為32，可以調節

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
for _ in range(600):
    print(_, end = " ")
    time.sleep(1)  # 錄製10s
    
t1.stop_record()


print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




