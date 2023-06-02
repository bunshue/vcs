'''
WebCam 使用

一般使用

目前 webcam 僅 x64 電腦可用
'''

import os
import cv2
import time
import urllib
import urllib.request   #用來建立請求
import numpy as np

def get_video_info(video):
    video_info = {}
    
    video_info['frames'] = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    video_info['width'] = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_info['height'] = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_info['fps'] = video.get(cv2.CAP_PROP_FPS)
    return video_info

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

'''
print('顯示網路圖片')
url = 'https://upload.wikimedia.org/wikipedia/commons/8/85/%E5%8C%97%E7%96%86%E5%8D%9A%E7%89%A9%E9%99%A2%E5%B7%A5%E5%AD%97%E6%A5%BC.jpg'
image = load_img_by_url(url)
cv2.imshow('Picture Viewer', image) #顯示圖片
'''

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'
vid = cv2.VideoCapture(video_filename)

'''
print('顯示影片中的某一幀圖片')
image = get_image_by_pos(vid, 20, False, False)
cv2.imshow('Picture Viewer', image) #顯示圖片

'''

video_info = get_video_info(vid)
print(video_info)




