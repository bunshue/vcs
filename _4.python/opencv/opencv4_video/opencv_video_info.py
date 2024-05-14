import cv2
import time
import urllib
import urllib.request   #用來建立請求

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

def show_video_info(filename):
    video = cv2.VideoCapture(filename);

    fps = video.get(cv2.CAP_PROP_FPS)
    print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

    print("data video.get(cv2.CAP_PROP_POS_MSEC) : {0}".format(video.get(cv2.CAP_PROP_POS_MSEC)))#Current position of the video file in milliseconds.
    print("data video.get(cv2.CAP_PROP_POS_FRAMES) : {0}".format(video.get(cv2.CAP_PROP_POS_FRAMES)))#0-based index of the frame to be decoded/captured next.
    print("data video.get(cv2.CAP_PROP_POS_AVI_RATIO) : {0}".format(video.get(cv2.CAP_PROP_POS_AVI_RATIO)))#Relative position of the video file: 0=start of the film, 1=end of the film.
    print("data video.get(cv2.CAP_PROP_FRAME_WIDTH) : {0}".format(video.get(cv2.CAP_PROP_FRAME_WIDTH)))#Width of the frames in the video stream.
    print("data video.get(cv2.CAP_PROP_FRAME_HEIGHT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))#Height of the frames in the video stream.
    print("data video.get(cv2.CAP_PROP_FPS) : {0}".format(video.get(cv2.CAP_PROP_FPS)))#Frame rate.
    print("data video.get(cv2.CAP_PROP_FOURCC) : {0}".format(video.get(cv2.CAP_PROP_FOURCC)))#4-character code of codec. see VideoWriter::fourcc .
    print("data video.get(cv2.CAP_PROP_FRAME_COUNT) : {0}".format(video.get(cv2.CAP_PROP_FRAME_COUNT)))#Number of frames in the video file.
    print("data video.get(cv2.CAP_PROP_FORMAT) : {0}".format(video.get(cv2.CAP_PROP_FORMAT)))#Format of the Mat objects returned by VideoCapture::retrieve().
    print("data video.get(cv2.CAP_PROP_MODE) : {0}".format(video.get(cv2.CAP_PROP_MODE)))#Backend-specific value indicating the current capture mode.
    print("data video.get(cv2.CAP_PROP_BRIGHTNESS) : {0}".format(video.get(cv2.CAP_PROP_BRIGHTNESS)))#Brightness of the image (only for cameras).
    print("data video.get(cv2.CAP_PROP_CONTRAST) : {0}".format(video.get(cv2.CAP_PROP_CONTRAST)))#Contrast of the image (only for cameras).
    print("data video.get(cv2.CAP_PROP_SATURATION) : {0}".format(video.get(cv2.CAP_PROP_SATURATION)))#Saturation of the image (only for cameras).
    print("data video.get(cv2.CAP_PROP_HUE) : {0}".format(video.get(cv2.CAP_PROP_HUE)))#Hue of the image (only for cameras).
    print("data video.get(cv2.CAP_PROP_GAIN) : {0}".format(video.get(cv2.CAP_PROP_GAIN)))#Gain of the image (only for cameras).
    print("data video.get(cv2.CAP_PROP_EXPOSURE) : {0}".format(video.get(cv2.CAP_PROP_EXPOSURE)))#Exposure (only for cameras).
    print("data video.get(cv2.CAP_PROP_CONVERT_RGB) : {0}".format(video.get(cv2.CAP_PROP_CONVERT_RGB)))#Boolean flags indicating whether images should be converted to RGB.
    print("data video.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U) : {0}".format(video.get(cv2.CAP_PROP_WHITE_BALANCE_BLUE_U)))#Currently unsupported.
    print("data video.get(cv2.CAP_PROP_RECTIFICATION) : {0}".format(video.get(cv2.CAP_PROP_RECTIFICATION)))#Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently).
    print("data video.get(cv2.CAP_PROP_MONOCHROME) : {0}".format(video.get(cv2.CAP_PROP_MONOCHROME)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_SHARPNESS) : {0}".format(video.get(cv2.CAP_PROP_SHARPNESS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_AUTO_EXPOSURE) : {0}".format(video.get(cv2.CAP_PROP_AUTO_EXPOSURE)))#DC1394: exposure control done by camera, user can adjust reference level using this feature.
    print("data video.get(cv2.CAP_PROP_GAMMA) : {0}".format(video.get(cv2.CAP_PROP_GAMMA)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_TEMPERATURE) : {0}".format(video.get(cv2.CAP_PROP_TEMPERATURE)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_TRIGGER) : {0}".format(video.get(cv2.CAP_PROP_TRIGGER)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_TRIGGER_DELAY) : {0}".format(video.get(cv2.CAP_PROP_TRIGGER_DELAY)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V) : {0}".format(video.get(cv2.CAP_PROP_WHITE_BALANCE_RED_V)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_ZOOM) : {0}".format(video.get(cv2.CAP_PROP_ZOOM)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_FOCUS) : {0}".format(video.get(cv2.CAP_PROP_FOCUS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_GUID) : {0}".format(video.get(cv2.CAP_PROP_GUID)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_ISO_SPEED) : {0}".format(video.get(cv2.CAP_PROP_ISO_SPEED)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_BACKLIGHT) : {0}".format(video.get(cv2.CAP_PROP_BACKLIGHT)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_PAN) : {0}".format(video.get(cv2.CAP_PROP_PAN)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_TILT) : {0}".format(video.get(cv2.CAP_PROP_TILT)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_ROLL) : {0}".format(video.get(cv2.CAP_PROP_ROLL)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_IRIS) : {0}".format(video.get(cv2.CAP_PROP_IRIS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_SETTINGS) : {0}".format(video.get(cv2.CAP_PROP_SETTINGS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    print("data video.get(cv2.CAP_PROP_BUFFERSIZE) : {0}".format(video.get(cv2.CAP_PROP_BUFFERSIZE)))#Pop up video/camera filter dialog (note: only supported by DSHOW backend currently. Property value is ignored)
    print("data video.get(cv2.CAP_PROP_AUTOFOCUS) : {0}".format(video.get(cv2.CAP_PROP_AUTOFOCUS)))#xxxxxxxxxxxxxxxxxxxxxxxxxxx
    video.release();

def loop(video, end_frame, func, transpose = False, gray = True, counter = 24):
    pos = 0
    while pos < end_frame:
        img = get_image_by_pos(video, pos, gray, transpose)
        func(img)
        pos += counter 

def get_image_by_pos(video, pos, gray, transpose):

    video.set(cv2.CAP_PROP_POS_FRAMES, pos)
    flag, img = video.read()
    
    if transpose:
        cv2.transpose(img, img)
    if gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)

    return img

def load_img_by_url(img_url):
    req = urllib.request.urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype = np.uint8)
    img = cv2.imdecode(arr, 0)
    return img

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/鹿港.mp4'
video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
show_video_info(video_filename)

"""
print('顯示網路圖片')
url = 'https://upload.wikimedia.org/wikipedia/commons/8/85/%E5%8C%97%E7%96%86%E5%8D%9A%E7%89%A9%E9%99%A2%E5%B7%A5%E5%AD%97%E6%A5%BC.jpg'
image = load_img_by_url(url)
cv2.imshow('Picture Viewer', image) #顯示圖片
"""

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)

"""
print('顯示影片中的某一幀圖片')
image = get_image_by_pos(vid, 20, False, False)
cv2.imshow('Picture Viewer', image) #顯示圖片
"""

print('------------------------------------------------------------')	#60個

def get_video_info(video):
    video_info = {}
    
    video_info['width'] = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_info['height'] = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_info['frames'] = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_info['fps'] = video.get(cv2.CAP_PROP_FPS)
    video_info['length'] = video.get(cv2.CAP_PROP_FRAME_COUNT) / video.get(cv2.CAP_PROP_FPS)
    print(type(video_info))
    return video_info

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)

video_info = get_video_info(vid)
print(video_info)

print('------------------------------------------------------------')	#60個

print('影片資訊')
video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

cap = cv2.VideoCapture(video_filename)

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print("影格尺寸:", width, "x", height)

#取得Codec編碼
fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
codec = (chr(fourcc&0xFF)+chr((fourcc>>8)&0xFF)+
        chr((fourcc>>16)&0xFF)+chr((fourcc>>24)&0xFF))
print("Codec編碼:", codec)

fps = cap.get(cv2.CAP_PROP_FPS)
print("FPS =", fps)

frame_count = 0
while True:
  ret, frame = cap.read()
  if not ret:
      break
  frame_count = frame_count + 1

print("總影格數 = ", frame_count)
cap.release()

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


