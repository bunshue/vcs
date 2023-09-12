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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)     # 建立Pillow物件
print("列出物件檔名 : ", image.filename)
print("列出物件型態 : ", type(image))
width, height = image.size           # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)

#存圖
#image.save("out17_6.png")

#顯示
#image.show()

image = Image.open(filename)           # 建立Pillow物件

width, height = image.size
newPict1 = image.resize((width*2, height))   # 寬度是2倍
#存圖
#newPict1.save("out17_9_1.jpg")

newPict2 = image.resize((width, height*2))   # 高度是2倍
#存圖
#newPict2.save("out17_9_2.jpg")

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
#存圖
#image.save("out17_7.jpg")

print('------------------------------------------------------------')	#60個

image = Image.new("RGBA", (300, 180)) # 建立完全透明影像
#存圖
#image.save("out17_8.png")

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)           # 建立Pillow物件

#存圖
#image.rotate(90).save("out17_10_1.jpg")      # 旋轉90度
#image.rotate(180).save("out17_10_2.jpg")     # 旋轉180度
#image.rotate(270).save("out17_10_3.jpg")     # 旋轉270度

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)                   # 建立Pillow物件
#存圖
#image.rotate(45).save("out17_11_1.jpg")              # 旋轉45度
#image.rotate(45, expand=True).save("out17_11_2.jpg") # 旋轉45度圖像擴充


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)                   # 建立Pillow物件

#存圖
#image.transpose(Image.FLIP_LEFT_RIGHT).save("out17_12_1.jpg")  # 左右
#image.transpose(Image.FLIP_TOP_BOTTOM).save("out17_12_2.jpg")  # 上下

print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))  # 列印中心點的色彩
#存圖
#newImage.save("out17_13.png")


print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                            # x軸區間在50-250
    for y in range(50, 151):                        # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色

#存圖
#newImage.save("out17_14_1.png")                     # 第一階段存檔
for x in range(50, 251):                            # x軸區間在50-250            
    for y in range(151, 251):                       # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))
#存圖
#newImage.save("out17_14_2.png")                     # 第一階段存檔

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)        # 建立Pillow物件
cropPict = image.crop((80, 30, 150, 100)) # 裁切區間

#存圖
#cropPict.save("out17_15.jpg")

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)   # 建立Pillow物件
copyPict = image.copy()              # 複製
#存圖
#copyPict.save("out17_16.jpg")

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)             # 建立Pillow物件
copyPict = image.copy()                        # 複製
cropPict = copyPict.crop((80, 30, 150, 100))  # 裁切區間
copyPict.paste(cropPict, (20, 20))            # 第一次合成
copyPict.paste(cropPict, (20, 100))           # 第二次合成
#存圖
#copyPict.save("out17_17.jpg")                 # 儲存

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件
image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

#存圖
#newImage.save("out17_18.jpg")                   # 儲存

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image = Image.open(filename)     # 建立Pillow物件

filterPict = image.filter(ImageFilter.BLUR)
#存圖
#filterPict.save("out17_19_BLUR.jpg")

filterPict = image.filter(ImageFilter.CONTOUR)
#存圖
#filterPict.save("out17_19_CONTOUR.jpg")

filterPict = image.filter(ImageFilter.EMBOSS)
#存圖
#filterPict.save("out17_19_EMBOSS.jpg")

filterPict = image.filter(ImageFilter.FIND_EDGES)
#存圖
#filterPict.save("out17_19_FIND_EDGES.jpg")

print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (300, 300), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

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

#存圖
#newImage.save("out17_20.png")

print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (300, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   

#存圖
#newImage.save("out17_21.png")

print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 
fontInfo = ImageFont.truetype('OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 使用Google公司的NotoSansTC-Bold.otf中文字型
strCtext = '明志科技大學'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('NotoSansTC-Bold.otf', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

#存圖
#newImage.save("out17_22.png")

print('------------------------------------------------------------')	#60個

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
# 使用Google公司的NotoSansTC-Bold.otf中文字型
strCtext = '明志科技大學'                           # 設定欲列印中文字串

fontInfo = ImageFont.truetype('NotoSansTC-Bold.otf', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

#存圖
#newImage.save("out17_23.png")

print('------------------------------------------------------------')	#60個

def compare_images(image1_path, image2_path, threshold=0.8):
    """
    比較兩張圖像的相似度，返回相似度值（0~1之間的浮點數）
    """
    image1 = Image.open(image1_path).convert('RGBA')
    image2 = Image.open(image2_path).convert('RGBA')
    diff = ImageChops.difference(image1, image2)
    histogram = diff.histogram()
    pixels = sum(histogram)
    similarity = 1 - (pixels / float(image1.size[0] * image1.size[1] * 3))
    print(similarity)
    return similarity >= threshold

'''
# 測試比較相似度
image1_path = 'star.jpg'
image2_path = 'face.jpg'
is_similar = compare_images(image1_path, image2_path)
print('相似度:', is_similar)
'''


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




