"""
PIL 基本使用

建立影像
PIL 無圖處理

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

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

print(ImageColor.getrgb("#0000ff"))         #(0, 0, 255)
print(ImageColor.getrgb("rgb(0,0,255)"))    #(0, 0, 255)
print(ImageColor.getrgb("rgb(0%,0%,100%)")) #(0, 0, 255)
print(ImageColor.getrgb("red"))             #(255, 0, 0)

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB")) #(0, 0, 255)
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))#(0, 0, 255, 255)
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("Blue", "RGBA"))        #(0, 0, 255, 255)
print(ImageColor.getcolor("#0000ff", "RGB"))      #(0, 0, 255)
print(ImageColor.getcolor("#0000ff", "RGBA"))

print('------------------------------------------------------------')	#60個

W, H = 640, 480

print('建立影像 RGB')

print('建立影像 RGB 全紅')
image = Image.new("RGB", (W, H), "#ff0000")  # 產生 RGB 色域，W x H 背景紅色的圖片

print('建立影像 RGB 半透明')
image = Image.new("RGB", (W, H), "#ff000055")  # 產生 RGBA 色域，W x H 背景半透明紅色的圖片

print('建立影像 RGBA 透明')
image = Image.new('RGBA', (W, H))

print('建立影像 RGBA 透明')
image = Image.new("RGBA",(W, H),"rgba(0,0,255,0)") #透明

print('建立影像 RGB 指定顏色')
image = Image.new("RGB",(W, H),"rgb(0,0,255)") #藍色

print('建立影像 RGB 指定顏色')
color = "aqua"
color = "yellow"
image = Image.new('RGB', (W, H), color)

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

