'''
WebCam 使用

一般使用

目前 webcam 僅 x64 電腦可用
'''

import cv2
import time

import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_video_info(video):
    video_info = {}
    video_info['frames'] = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))
    video_info['width'] = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    video_info['height'] = int(video.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    video_info['fps'] = video.get(cv2.cv.CV_CAP_PROP_FPS)
    return video_info

def loop(video, end_frame, func, transpose=False, gray=True, counter=24):
    pos = 0
    while pos < end_frame:
        img = get_image_by_pos(video, pos, gray, transpose)
        func(img)
        pos += counter 

def get_image_by_pos(video, pos, gray, transpose):
    
    video.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos)
    flag, img = video.read()
    
    if transpose:
        cv2.transpose(img, img)
    if gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.equalizeHist(img)

    return img

def load_img_by_url(img_url):
    req = urllib.urlopen(img_url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, 0)
    return img

