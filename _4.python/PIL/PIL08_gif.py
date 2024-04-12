"""
gif相關
"""

from PIL import Image

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

print("------------------------------------------------------------")  # 60個

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

print("gif轉jpg")
from PIL import ImageSequence

gif = Image.open(gif_filename)                # 讀取動畫圖檔

i = 0                                      # 設定編號變數
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGB')           # 取出每一格轉換成 RGB
    #frame.save(f'tmp_frame{i}.jpg', quality=65, subsampling=0)  # 儲存為 jpg
    i = i + 1                              # 編號增加 1

print("------------------------------------------------------------")  # 60個
print("用cv視窗播放gif檔案")

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

import cv2
from PIL import ImageSequence

gif = Image.open(gif_filename)

img_list = []                                      # 建立儲存影格的空串列
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')                  # 轉換成 RGBA
    opencv_img = np.array(frame, dtype=np.uint8)   # 轉換成 numpy 陣列
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)  # 顏色從 RGBA 轉換為 BGRA
    img_list.append(opencv_img)                    # 利用串列儲存該圖片資訊

loop = True                                        # 設定 loop 為 True
while loop:
    for i in img_list:
        cv2.imshow('image', i)                # 不斷讀取並顯示串列中的圖片內容
        if cv2.waitKey(200) == ord('q'):
            loop = False                           # 停止時同時也將 while 迴圈停止
            break

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個

from PIL import ImageSequence

gif_filename = "C:/_git/vcs/_1.data/______test_files1/__pic/_gif/cat.gif"

gif = Image.open(gif_filename)

img_list = []
for frame in ImageSequence.Iterator(gif):
    frame = frame.convert('RGBA')
    opencv_img = np.array(frame, dtype=np.uint8)
    opencv_img = cv2.cvtColor(opencv_img, cv2.COLOR_RGBA2BGRA)

    # 在圖形中間繪製黑色方塊
    x_st, y_st, w, h = 10, 10, 120, 40
    cv2.rectangle(opencv_img,(x_st, y_st),(x_st+w, y_st+h),(0,0,0),-1)

    # 在黑色方塊上方加入文字, 文字基準是左下角
    text = 'My Cat'
    org = (x_st, y_st+30)
    fontFace = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255,255,255)
    thickness = 2
    lineType = cv2.LINE_AA
    cv2.putText(opencv_img, text, org, fontFace, fontScale, color, thickness, lineType)

    img_list.append(opencv_img)

loop = True
while loop:
    for i in img_list:
        cv2.imshow('image', i)
        if cv2.waitKey(200) == ord('q'):
            loop = False
            break
# 建立要輸出的影格串列
output = []
for i in img_list:
    img = i
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)  # 因為 OpenCV 為 BGRA，要轉換成 RGBA
    img = Image.fromarray(img)    # 轉換成 PIL 格式
    img = img.convert('RGB')      # 轉換成 RGB ( 如果是 RGBA 會自動將黑色白色變成透明色 )
    output.append(img)            # 加入 output
# 儲存為 gif 動畫圖檔
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=200, loop=0, disposal=0)

cv2.destroyAllWindows()

print("------------------------------------------------------------")  # 60個
print("多個jpg組成一個gif檔")

from PIL import ImageSequence

gif = []
for i in range(1, 6):
    img = Image.open(f'C:/_git/vcs/_1.data/______test_files1/__pic/_scenery/ggb{i}.jpg')  # 開啟圖片
    gif.append(img)                    # 加入串列
# 儲存為 gif
gif[0].save("tmp_image.gif", save_all=True, append_images=gif[1:], duration=2000, loop=0, disposal=0)

print("------------------------------------------------------------")  # 60個

"""

n = 0
for i in source:                  # source 為要轉存的所有圖片陣列 ( opencv 格式，色彩為 RGBA )
    img = Image.fromarray(i)      # 轉換成 PIL 格式
    img.save(f'tmp_gif{n}.gif')  # 儲存為 gif
    n = n + 1                     # 改變儲存的檔名編號

output = []                       # 建立空串列
for i in range(n):
    img = Image.open(f'tmp_gif{i}.gif')  # 依序開啟每張 gif
    img = img.convert("RGBA")             # 轉換為 RGBA
    output.append(img)                    # 記錄每張圖片內容

# 轉存為 gif 動畫，設定 disposal=2
output[0].save("tmp_image.gif", save_all=True, append_images=output[1:], duration=100, loop=0, disposal=2)
"""



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

