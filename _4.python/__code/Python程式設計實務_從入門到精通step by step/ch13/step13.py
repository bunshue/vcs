import sys
from PIL import Image
from PIL import ImageColor

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

'''
print('------------------------------------------------------------')	#60個

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0, 0, 255)"))
print(ImageColor.getrgb("rgb(0%, 0%, 100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("blue"))

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("#0000ff", "RGB"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("#0000ff", "RGBA"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
print(ImageColor.getcolor("Blue", "RGBA"))

print('------------------------------------------------------------')	#60個

image = Image.open(filename)       # 建立Pillow物件
print("列出物件型態 : ", type(image))
width, height = image.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)       # 建立Pillow物件
print("列出物件檔名 : ", image.filename)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)       # 建立Pillow物件
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)       # 建立Pillow物件
#image.save("pic.png")
#image.show()

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
#image.save("out17_7.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (300, 180))     # 建立完全透明影像
#image.save("out17_8.png")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
width, height = image.size
newPict1 = image.resize((width*2, height))   # 寬度是2倍
#newPict1.save("out17_9_1.jpg")
newPict2 = image.resize((width, height*2))   # 高度是2倍
#newPict2.save("out17_9_2.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
#image.rotate(90).save("out17_10_1.jpg")      # 旋轉90度
#image.rotate(180).save("out17_10_2.jpg")     # 旋轉180度
#image.rotate(270).save("out17_10_3.jpg")     # 旋轉270度

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                       # 建立Pillow物件
#image.rotate(45).save("out17_11_1.jpg")                  # 旋轉45度
#image.rotate(45, expand=True).save("out17_11_2.jpg")     # 旋轉45度圖像擴充

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                     # 建立Pillow物件
#image.transpose(Image.FLIP_LEFT_RIGHT).save("out17_12_1.jpg")    # 左右
#image.transpose(Image.FLIP_TOP_BOTTOM).save("out17_12_2.jpg")    # 上下

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))      # 列印中心點的色彩
#newImage.save("out17_13.png")

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色
#newImage.save("out17_14_1.png")                         # 第一階段存檔

for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))
#newImage.save("out17_14_2.png")                         # 第一階段存檔

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
cropPict = image.crop((80, 30, 150, 100))   # 裁切區間
#cropPict.save("out17_15.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
copyPict = image.copy()                      # 複製
#copyPict.save("out17_16.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
copyPict.paste(cropPict, (20, 20))              # 第一次合成
copyPict.paste(cropPict, (20, 100))             # 第二次合成
#copyPict.save("out17_17.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

#newImage.save("out17_18.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

from PIL import ImageFilter

image = Image.open(filename)       # 建立Pillow物件
filterPict = image.filter(ImageFilter.BLUR)
#filterPict.save("out17_19_BLUR.jpg")

filterPict = image.filter(ImageFilter.CONTOUR)
#filterPict.save("out17_19_CONTOUR.jpg")

filterPict = image.filter(ImageFilter.EMBOSS)
#filterPict.save("out17_19_EMBOSS.jpg")

filterPict = image.filter(ImageFilter.FIND_EDGES)
#filterPict.save("out17_19_FIND_EDGES.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

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
#newImage.save("out17_20.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   
#newImage.save("out17_21.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '明志科技大學'                           # 設定欲列印中文字串

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\ebas927.ttf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

#newImage.save("out17_22.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Ming-Chi Institute of Technology'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '明志科技大學'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)
#newImage.save("out17_22_1.png")

print("------------------------------------------------------------")  # 60個

import qrcode

codeText = 'http://www.deepstone.com.tw'
img = qrcode.make(codeText)                 # 建立QR code 物件
print("檔案格式", type(img))
#img.save("out17_23.jpg")



import qrcode
im = qrcode.make("https://pmm.zct.com.tw/trial/")
#im.save("qrcode.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

image = Image.open(filename)
width, height = image.size
"""
image.show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
image.filter(ImageFilter.GaussianBlur(4)).show()
image.filter(ImageFilter.EMBOSS).show()
image.thumbnail((width // 4, height // 4))
image.show()
"""

'''

print('------------------------------------------------------------')	#60個

from PIL import Image
im = Image.open(filename)
print(im.format)
print(im.mode)
print(im.width)
print(im.height)
print(im.size)


print('------------------------------------------------------------')	#60個

#filter
from PIL import Image,ImageFilter
im=Image.open("pic/car.jpg")
new=im.filter(ImageFilter.EDGE_ENHANCE)
new.show()


print('------------------------------------------------------------')	#60個

#crop

from PIL import Image
with Image.open("pic/4.jpg") as im:
    print('原圖片的尺寸大小:',im.size)
    x = 100
    y = 100
    x1 = 1000
    y1 = 1400
    new_im = im.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', new_im.size)
    new_im.save( "pic/4_crop.jpg")

print('------------------------------------------------------------')	#60個

#rotate0

from PIL import Image
with Image.open("pic/3.jpg") as im:
  new_im = im.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  new_im.save( "pic/3_rotate0.jpg")
  






print('------------------------------------------------------------')	#60個

# rotate1
from PIL import Image
with Image.open("pic/3.jpg") as im:
  new_im = im.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  new_im.save( "pic/3_rotate1.jpg")
  

print('------------------------------------------------------------')	#60個

# resize

from PIL import Image
with Image.open("pic/2.jpg") as im:
    print('原圖片的尺寸大小:',im.size)
    w=300
    r = w/im.size[0]
    h = int(im.size[1]*r)
    new_im = im.resize((w, h))
    print('圖片經縮放後的尺寸大小:',new_im.size)
    new_im.save( "pic/2_resize.jpg" )

print('------------------------------------------------------------')	#60個

#sharpness

from PIL import Image,ImageEnhance
with Image.open(filename) as im:
    new_im = ImageEnhance.Contrast(im).enhance(0.3)
    new_im.save( "pic/1_Contrast.jpg") 

print('------------------------------------------------------------')	#60個

# transpose

from PIL import Image,ImageEnhance
with Image.open("pic/8.jpg") as im:
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save( "pic/8_1.jpg")
    new_im = im.transpose(Image.FLIP_TOP_BOTTOM)
    new_im.save( "pic/8_2.jpg")
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save( "pic/8_3.jpg")
    new_im = im.transpose(Image.ROTATE_180)
    new_im.save( "pic/8_4.jpg")
    new_im = im.transpose(Image.ROTATE_270)
    new_im.save( "pic/8_5.jpg")
    new_im = im.transpose(Image.TRANSPOSE)
    new_im.save( "pic/8_6.jpg")
    new_im = im.transpose(Image.TRANSVERSE)
    new_im.save( "pic/8_7.jpg")


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個





