"""
PIL 基本使用

顯示圖片

顯示圖片訊息

"""
print("------------------------------------------------------------")  # 60個

import PIL
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

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

print('顯示圖片與顯示圖片資訊')

# 檔案 => PIL影像
image = Image.open(filename)

print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('顯示圖片訊息')
print("列出物件檔名 : ", image.filename)
print("列出物件型態 : ", type(image))
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)
print("列出物件模式   : ", image.mode)

width, height = image.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)

#print(image.mode)
#print(image.size)

W, H = image.size
print('原圖大小 W =', W, ', H =', H)

print('圖片維度 圖片資訊')
print('Size : ', image.size, 'Mode : ', image.mode, 'Format : ', image.format)

"""
#查看圖片信息，可用如下的方法：
print(image.shape)
print(image.dtype)
print(image.size)
print(type(image))
"""

# 檔案 => PIL影像
print("%s:" % filename, image.format, "%dx%d" % image.size, image.mode)
print(image.info, image.tile)

plt.imshow(image)
plt.show()

image.close()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

#純圖片指定座標取得顏色方法
def rgb_of_pixel(image_path, x, y):
    # 檔案 => PIL影像 => RGB影像
    image = Image.open(image_path).convert('RGB')
    r, g, b = image.getpixel((x, y))
    a = (r, g, b)
    return a

print(rgb_of_pixel(filename, 131, 81))

print("------------------------------------------------------------")  # 60個

#split

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#通道分離與合併

# 檔案 => PIL影像
image=Image.open(filename)
print(image.size)

# PIL影像 => 灰階
gray_image=image.convert('L')   #轉換成灰度
print(gray_image.size)

# 分離三通道
r,g,b=image.split()
print(r.size)

#合併三通道
pic=Image.merge('RGB',(r,g,b))
print(pic.size)

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

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

#convert
print('彩色轉灰階')

# 檔案 => PIL影像
image=Image.open(filename)

# PIL影像 => 灰階
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

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

print('顯示原圖 顯示PIL影像 與 顯示numpy陣列')

#建立Pillow物件 PIL讀取本機圖片, RGB模式, 存成PIL影像格式

# 檔案 => PIL影像
image = Image.open(filename)
#image = image.convert('L')  #fail
print(type(image))
#顯示PIL影像
#plt.imshow(image)
#plt.show()

print('取得通道與名稱')
cc = image.getbands()
print(cc)
print('共有 :', len(cc), '個通道')
for i in range(len(cc)):
    print("通道", cc[i])

print('模式')
print(image.mode)

print('尺寸')
print(image.size)

print('信息')
print(image.info)

# PIL影像 => numpy陣列
image=np.array(image)
print(type(image))
#顯示numpy陣列
#plt.imshow(image)
#plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)

plt.subplot(121)
plt.title('原圖')
plt.imshow(image)

r, g, b = image.split() # 分離三個通道
image = Image.merge("RGB",(b,g,r))# 將藍色通道和紅通道互換

plt.subplot(122)
plt.title('兩通道互換')
plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

