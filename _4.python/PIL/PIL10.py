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
from PIL import ImageFont
from PIL import ImageChops

import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

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

image = Image.new('RGB', (300, 180), 'aqua')  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.new('RGBA', (300, 180)) # 建立完全透明影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.new('RGBA', (300, 100), "Yellow")

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

print('無影像之PIL畫圖1')

image = Image.new('RGBA', (300, 300), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

# 繪製點
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([(x,y)], fill='Green')

# 繪製線條, 繪外框線
drawObj.line([(0,0), (299,0), (299,299), (0,299), (0,0)], fill="Black")
# 繪製右上角美工線
for x in range(150, 300, 10):
    drawObj.line([(x,0), (300,x-150)], fill="Blue")
# 繪製左下角美工線
for y in range(150, 300, 10):
    drawObj.line([(0,y), (y-150,300)], fill="Blue")    

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖2')

image = Image.new('RGBA', (300, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖3')

image = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 
fontInfo = ImageFont.truetype('OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)

strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖4')

image = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('PIL 有圖處理')

image = Image.open(filename)     # 建立Pillow物件
print("列出物件檔名 : ", image.filename)
print("列出物件型態 : ", type(image))
width, height = image.size           # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)

plt.imshow(image)
plt.show()

width, height = image.size
newPict1 = image.resize((width*2, height))   # 寬度是2倍

plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((width, height*2))   # 高度是2倍

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

plt.imshow(image.rotate(45, expand=True))   # 旋轉45度+圖像擴充
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
w = 305/4
h = 400/4
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
w = 305/4
h = 400/4
#                             x_st  y_st    x_sp     y_sp
cropPict = image_copied.crop((x_st, y_st, x_st + w, y_st + h))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
image = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
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

image1 = Image.open(filename)        # 建立Pillow物件
newPic = image1.resize((350,500))

nwidth, nheight = 450, 600
image2 = Image.new('RGB', (nwidth, nheight), "Yellow")

image2.paste(newPic, (50,50))

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

image1 = Image.open(filename)        # 建立Pillow物件
newPic = image1.resize((350,500))

nwidth, nheight = 450, 700
image2 = Image.new('RGB', (nwidth, nheight), "Yellow")

image2.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(image2)
name = "牡丹亭"
fontInfo = ImageFont.truetype(font_filename, 60)
drawObj.text((140,600), name, fill='Blue', font=fontInfo)

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

