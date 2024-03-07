"""
PIL 基本使用

建立影像
PIL 無圖處理

"""

import os
import sys
import time
import random

import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

print('------------------------------------------------------------')	#60個

print('PIL 無圖處理')

print('------------------------------------------------------------')	#60個

print(ImageColor.getrgb("#0000ff"))         #(0, 0, 255)
print(ImageColor.getrgb("rgb(0,0,255)"))    #(0, 0, 255)
print(ImageColor.getrgb("rgb(0%,0%,100%)")) #(0, 0, 255)
print(ImageColor.getrgb("Blue"))            #(0, 0, 255)
print(ImageColor.getrgb("red"))

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB")) #(0, 0, 255)
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))#(0, 0, 255, 255)
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("Blue", "RGBA"))        #(0, 0, 255, 255)
print(ImageColor.getcolor("#0000ff", "RGB"))      #(0, 0, 255)
print(ImageColor.getcolor("#0000ff", "RGBA"))

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
image = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片

print('建立影像 RGB 300 X 100')
W, H = 300, 100
color = "aqua"
image = Image.new('RGB', (W, H), color)

plt.imshow(image)
plt.show()

print(image.getpixel((W//2, H//2)))      # 列印中心點的色彩

print('------------------------------------------------------------')	#60個

print('建立影像(透明) RGBA 300 X 100')
W, H = 300, 100
image = Image.new('RGBA', (W, H))
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個


print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




"""
共用抽出

#存圖
#image.save("xxxx.jpg")
#image.save("xxxx.png")



#顯示
#image.show()



"""
