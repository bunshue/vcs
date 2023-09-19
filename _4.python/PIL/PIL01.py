'''

裁剪圖片

'''

print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

print('圖片裁剪縮放')

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式

plt.imshow(image1)
plt.show()
 
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

print('把圖轉成 100X500 大小')
image3 = image1.resize((100, 500), Image.ANTIALIAS)

plt.imshow(image3)
plt.show()

print('------------------------------------------------------------')	#60個


#調整資料夾內所有圖片檔影像寬度, 加logo
      
import sys, os, glob
from PIL import Image, ImageDraw
import shutil

source_dir = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/resized_pic'
#logo_filename = 'C:/_git/vcs/_1.data/______test_files1/burn.bmp'        #fail, bad transparency mask
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/logo.png'

#準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
        #os.remove(target_dir)  #存取被拒 不可用
        shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
        os.mkdir(target_dir)

image_W = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_W) + " 像素")

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir + '/*.jpg') + glob.glob(source_dir + '/*.png')

logo = Image.open(logo_filename)    #PIL讀取本機圖片
logo = logo.resize((150, 150))   #調整圖像大小
#logo.show()

for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	image = Image.open(target_image)    #PIL讀取本機圖片
	w, h = image.size
	image = image.resize((800, int(800 / float(w) * h)))
	image.paste(logo, (0, 0), logo)
	image.save(target_dir + '/' + filename)
	image.close()

print("完成")
print('輸出圖片資料夾 : ', target_dir)

	
print('------------------------------------------------------------')	#60個

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample.jpg'
filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image1)  #原圖
plt.show()

image1g = image1.convert('L')	#轉換成灰階圖像
plt.imshow(image1g)      #灰階圖
plt.show()

W, H = image1g.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1g.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

image2_hist = image2.histogram()

print('把圖轉成 100X500 大小')
image3 = image1.resize((100, 500), Image.ANTIALIAS)

plt.imshow(image3)
plt.show()

image1g = image3.convert('L')	#轉換成灰階圖像
hist = image1g.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color='cyan', label='cropped')
plt.plot(ind, hist, color='black', lw=2, label='original')
plt.plot(ind, r_hist, color='red', label='Red Plane')
plt.plot(ind, g_hist, color='green', label='Green Plane')
plt.plot(ind, g_hist, color='blue', label='Blue Plane')
plt.xlim(0, 255)
plt.ylim(0, 8000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

print('萃取圖片的輪廓')

import matplotlib.pyplot as plt
from PIL import Image

# 讀入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample2.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image1)
plt.show()

#全彩轉灰階
image1 = image1.convert("L")
plt.imshow(image1)
plt.show()

# 圖片大小
W, H = image1.size

# 輸出用
image2 = Image.new('RGB', (W, H))

# 萃取輪廓
for y in range(0, H - 1):
    for x in range(0, W - 1):
        # 計算亮度差
        diff_x = image1.getpixel((x + 1, y)) - image1.getpixel((x, y))
        diff_y = image1.getpixel((x, y + 1)) - image1.getpixel((x, y))
        diff = diff_x + diff_y
        
        # 輸出
        if diff >= 20:
            image2.putpixel((x, y), (255, 0, 0))   #亮度差較大 著紅色
        else:
            image2.putpixel((x, y), (0, 0, 0))     #亮度差較小 著黑色

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個


import sys

import matplotlib.pyplot as plt
from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/flower.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.show()

#convert_image.save('rgb_to_bgr.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

black_and_white = image.convert('1')

plt.imshow(black_and_white)
plt.show()

#black_and_white.save('b_and_w.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

gray_iamge = image.convert('L')

plt.imshow(gray_iamge)
plt.show()

#gray_iamge.save('gray_image.jpg') 

print('------------------------------------------------------------')	#60個

from PIL import Image

image = Image.open(filename)

rotate_image = image.transpose(Image.ROTATE_90)
plt.imshow(rotate_image)
plt.show()

#rotate_image.save('rotate_90.jpg')#儲存90度旋轉的圖片

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個








'''
共用抽出

#存圖
#image.save("xxxx.png")

#顯示
#image.show()

'''

import os
import sys
import time
import random

from PIL import Image
from PIL import ImageColor
from PIL import ImageFilter
from PIL import ImageDraw
#from PIL import ImageFont
from PIL import ImageChops

import matplotlib.pyplot as plt

#font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

print('PIL 無圖處理')

print('------------------------------------------------------------')	#60個

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0, 0, 255)"))
print(ImageColor.getrgb("rgb(0%, 0%, 100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("red"))

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("#0000ff", "RGB"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("#0000ff", "RGBA"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
print(ImageColor.getcolor("Blue", "RGBA"))

print('------------------------------------------------------------')	#60個

W, H = 300, 180
image = Image.new('RGB', (W, H), 'aqua')  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

W, H = 300, 180
image = Image.new('RGBA', (W, H)) # 建立完全透明影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

W, H = 300, 100
image = Image.new('RGBA', (W, H), "Yellow")

print('列印中心點的色彩')
print(image.getpixel((150, 50)))

for x in range(50, 251):                            # x軸區間在50-250
    for y in range(20, 51):                        # y軸區間在20-50
        image.putpixel((x, y), (255, 0, 0, 255))   # 填紅色

for x in range(50, 251):                            # x軸區間在50-250            
    for y in range(51, 81):                       # y軸區間在51-80
        image.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA")) # 填藍色

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('PIL 有圖處理')

image = Image.open(filename)     # 建立Pillow物件
print("列出物件檔名 : ", image.filename)
print("列出物件型態 : ", type(image))
W, H = image.size           # 獲得影像寬度和高度
print("寬度 = ", W)
print("高度 = ", H)
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)

plt.imshow(image)
plt.show()

W, H = image.size
newPict1 = image.resize((W * 2, H))   # 寬度是2倍

plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((W, H * 2))   # 高度是2倍

plt.imshow(newPict2)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

plt.imshow(image.rotate(90))    # 旋轉90度
plt.show()

plt.imshow(image.rotate(180))   # 旋轉180度
plt.show()

plt.imshow(image.rotate(270))   # 旋轉270度
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

plt.imshow(image.rotate(45))   # 旋轉45度
plt.show()

plt.imshow(image.rotate(45, expand = True))   # 旋轉45度+圖像擴充
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('左右相反')
plt.imshow(image.transpose(Image.FLIP_LEFT_RIGHT))   # 左右
plt.show()

print('上下顛倒')
plt.imshow(image.transpose(Image.FLIP_TOP_BOTTOM))   # 上下
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

x_st = 0
y_st = 0
w = 305/3
h = 400/3
#                      x_st   y_st   x_sp     y_sp
cropPict = image.crop((x_st, y_st, x_st + w, y_st + h)) # 裁切區間

print('顯示一塊')
plt.imshow(cropPict)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片
#plt.imshow(image_copied)
#plt.show()

x_st = 0
y_st = 0
w = 305 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
cropPict = image_copied.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間
image_copied.paste(cropPict, (20, 20))          # 第一次合成
image_copied.paste(cropPict, (20, 20 + 120))    # 第二次合成
image_copied.paste(cropPict, (20, 20 + 240))    # 第三次合成

print('合成圖片')
plt.imshow(image_copied)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片

x_st = 0
y_st = 0
w = 305 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
cropPict = image_copied.crop((x_st, y_st, x_st + w, y_st + h))    # 裁切區間
cropW, cropH = cropPict.size           # 獲得裁切區間的寬與高

W, H = 600, 320                        # 新影像寬與高
image = Image.new('RGB', (W, H), "Yellow")  # 建立新影像
for x in range(20, W - 20, cropW):         # 雙層迴圈合成
    for y in range(20, H - 20, cropH):
        image.paste(cropPict, (x, y))        # 合成

print('合成圖片')
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)     # 建立Pillow物件

print('ImageFilter.BLUR')
filterPict = image.filter(ImageFilter.BLUR)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.CONTOUR')
filterPict = image.filter(ImageFilter.CONTOUR)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.DETAIL')
filterPict = image.filter(ImageFilter.DETAIL)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EDGE_ENHANCE')
filterPict = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EDGE_ENHANCE_MORE')
filterPict = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EMBOSS')
filterPict = image.filter(ImageFilter.EMBOSS)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.FIND_EDGES')
filterPict = image.filter(ImageFilter.FIND_EDGES)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SMOOTH')
filterPict = image.filter(ImageFilter.SMOOTH)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SMOOTH_MORE')
filterPict = image.filter(ImageFilter.SMOOTH_MORE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SHARPEN')
filterPict = image.filter(ImageFilter.SHARPEN)
plt.imshow(filterPict)
plt.show()

print('------------------------------------------------------------')	#60個

def compare_images(filename1, filename2, threshold=0.8):
    #比較兩張圖像的相似度，返回相似度值（0~1之間的浮點數）
    image1 = Image.open(filename1).convert('RGBA')
    image2 = Image.open(filename2).convert('RGBA')
    diff = ImageChops.difference(image1, image2)
    histogram = diff.histogram()
    pixels = sum(histogram)
    similarity = 1 - (pixels / float(image1.size[0] * image1.size[1] * 3))
    print(similarity)
    return similarity >= threshold

# 測試比較相似度
filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'
is_similar = compare_images(filename1, filename2)
print('相似度:', is_similar)

print('------------------------------------------------------------')	#60個

