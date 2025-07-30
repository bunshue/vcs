# OpenCV 共同
# from opencv_common import *

import cv2

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

# import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    # pass
    plt.tight_layout()  # 緊密排列，並填滿原圖大小
    plt.show()


def cvshow(title, image):
    # pass
    cv2.imshow(title, image)
    cv2.waitKey()
    cv2.destroyAllWindows()


print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

print("------------------------------------------------------------")  # 60個

ESC = 27
SPACE = 32
ENTER = 13
width, height = 640, 480  # 影像寬, 影像高
maxval = 255  # 定義像素最大值, 閾值

print("------------------------------------------------------------")  # 60個

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"
filename3 = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
filename4a = "C:/_git/vcs/_4.python/opencv/data/ims_640X480.bmp"
filename4b = "C:/_git/vcs/_4.python/opencv/data/ims_320X240.jpg"
filename_rgb = "C:/_git/vcs/_4.python/opencv/data/rgb512.bmp"

filename_lena_color = "C:/_git/vcs/_4.python/opencv/data/lena_color.jpg"
filename_lena_gray = "C:/_git/vcs/_4.python/opencv/data/lena_gray.bmp"
filename_barbara = "C:/_git/vcs/_4.python/opencv/data/barbara.bmp"
filename_gray = "C:/_git/vcs/_4.python/opencv/data/threshold/gray_scale.jpg"

video_filename = "C:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

print("------------------------------------------------------------")  # 60個

# OpenCV_顏色共同
RED = (0, 0, 255)  # B G R
GREEN = (0, 255, 0)  # B G R
BLUE = (255, 0, 0)  # B G R
CYAN = (255, 255, 0)  # B G R
MAGENTA = (255, 0, 255)  # B G R
YELLOW = (0, 255, 255)  # B G R
BLACK = (0, 0, 0)  # B G R
WHITE = (255, 255, 255)  # B G R
colors = [RED, GREEN, BLUE, CYAN, MAGENTA, YELLOW, BLACK, WHITE]

# BGR
color = [
    (0, 0, 255),  # 紅色, Red
    (0, 255, 0),  # 草綠色, Lime
    (255, 0, 0),  # 藍色, Blue
    (0, 255, 255),  # 黃色, Yellow
    (255, 0, 255),  # 品紅色, Fuchsia Magenta
    (255, 255, 0),  # 青色或水色, Cyan / Aqua
    (0, 0, 0),  # 黑色, Black
    (255, 255, 255),  # 白色, White
    (0, 0, 128),  # 栗色, Maroon
    (0, 128, 128),  # 橄欖綠, Olive
    (0, 128, 0),  # 綠色, Green
    (128, 128, 0),  # 藍綠色, Teal
    (128, 0, 0),  # 藏青色, Navy
    (128, 0, 128),  # 紫色, Purple
    (192, 192, 192),  # 銀色, Silver
    (128, 128, 128),  # 灰色, Gray
]

print("------------------------------------------------------------")  # 60個


def drawText(image, x_st, y_st, text, scale=0.8, color=WHITE):
    # 文字背景
    # cv2.rectangle(frame, (x_st - 12, y_st - 35), (x_st + 360, y_st + 15), GREEN, -1)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = scale
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(
        image, text, (x_st, y_st), fontFace, fontScale, color, thickness, lineType
    )


print("------------------------------------------------------------")  # 60個
