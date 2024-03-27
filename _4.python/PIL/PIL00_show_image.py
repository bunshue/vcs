"""
PIL 基本使用

顯示圖片

顯示圖片訊息

"""
print("------------------------------------------------------------")  # 60個

import PIL
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

print('------------------------------------------------------------')	#60個

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

print('查詢 PIL 版本')
print(PIL.__version__)

print("------------------------------------------------------------")  # 60個

print('顯示原圖')

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)

plt.show()

print('顯示圖片訊息')
print("列出物件檔名 : ", image1.filename)
print("列出物件型態 : ", type(image1))
print("列出物件副檔名 : ", image1.format)
print("列出物件描述   : ", image1.format_description)
print("列出物件模式   : ", image1.mode)

W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('圖片維度 圖片資訊')
print('Size : ', image1.size, 'Mode : ', image1.mode, 'Format : ', image1.format)

image1.close()

print('------------------------------------------------------------')	#60個

"""
#PIL 存圖
print('圖片另存新檔')
image1.save('tmp_image1.jpg')
image1.save('tmp_image2.jpg', 'JPEG')
image1.save('tmp_image3.png')
image1.save('tmp_image4.png', 'PNG')
image1.save('tmp_image5.bmp') 

"""

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)       # 建立Pillow物件
print("列出物件檔名 : ", image.filename)
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)
print("列出物件型態 : ", type(image))
width, height = image.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)

#print(image.mode)
#print(image.size)

plt.imshow(image)
plt.show()

image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

"""
#查看圖片信息，可用如下的方法：
print(image.shape)
print(image.dtype)
print(image.size)
print(type(image))
"""

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

im = Image.open(filename)
print("%s:" % filename, im.format, "%dx%d" % im.size, im.mode)
print(im.info, im.tile)


print("------------------------------------------------------------")  # 60個



filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

#純圖片指定座標取得顏色方法
def rgb_of_pixel(image_path, x, y):
    im = Image.open(image_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

print(rgb_of_pixel(filename, 131, 81))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

#image1.save('xxxxx.png')

print("------------------------------------------------------------")  # 60個

#split

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#通道分離與合併

image=Image.open(filename)  #打開圖像, 彩色
print(image.size)

gray_image=image.convert('L')   #轉換成灰度
print(gray_image.size)
r,g,b=image.split()   #分離三通道
print(r.size)

pic=Image.merge('RGB',(r,g,b)) #合併三通道
print(pic.size)

plt.figure('picture')

plt.subplot(2,3,1)
plt.title('原圖')
plt.imshow(image)

plt.subplot(2,3,2)
plt.title('灰階')
plt.imshow(gray_image,cmap='gray')
print(gray_image.size)

"""
r,g,b=gray_image.split()   #分離三通道
gray_image = Image.merge('RGB',(r,g,b)) #合併三通道
plt.imshow(gray_image)
"""
plt.subplot(2,3,3)
plt.title('合併三通道')
plt.imshow(pic)

plt.subplot(2,3,4)
plt.title('R通道')
plt.imshow(r,cmap='gray')

plt.subplot(2,3,5)
plt.title('G通道')
plt.imshow(g,cmap='gray')

plt.subplot(2,3,6)
plt.title('B通道')
plt.imshow(b,cmap='gray')

plt.show()


sys.exit()



print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#convert
print('彩色轉灰階')

image=Image.open(filename)
gray_image=image.convert('L')

plt.figure('picture')
plt.subplot(121)
plt.imshow(image)
plt.title('彩色')

plt.subplot(122)
plt.imshow(gray_image,cmap='gray')
plt.title('灰階')

plt.show()



print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



