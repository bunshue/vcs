# PIL 集合 new

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageColor

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'

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
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',image.size)
print('圖片的寬度，單位像素(pixels): ',image.width)
print('圖片的高度，單位像素(pixels): ',image.height)

image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
print(image.format)
print(image.mode)
print(image.width)
print(image.height)
print(image.size)

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (300, 180))     # 建立完全透明影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))      # 列印中心點的色彩
newImage.save("tmp_pic13.png")

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色

newImage.save("tmp_pic14.png")                         # 第一階段存檔

for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))

newImage.save("tmp_pic15.png")                         # 第一階段存檔

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
width, height = image.size

newPict1 = image.resize((width*2, height))   # 寬度是2倍
plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((width, height*2))   # 高度是2倍
plt.imshow(newPict2)
plt.show()


print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
image090=image.rotate(90)  # 旋轉90度
image180=image.rotate(180)  # 旋轉180度
image270=image.rotate(270)  # 旋轉270度

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                       # 建立Pillow物件
image45a=image.rotate(45)  # 旋轉45度
image45b=image.rotate(45, expand=True)  # 旋轉45度圖像擴充

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                     # 建立Pillow物件
image_flip1 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右
image_flip2 = image.transpose(Image.FLIP_TOP_BOTTOM)  # 上下

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
cropPict = image.crop((80, 30, 150, 100))   # 裁切區間
cropPict.save("tmp_pic16.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
copyPict = image.copy()                      # 複製
copyPict.save("tmp_pic17.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
copyPict.paste(cropPict, (20, 20))              # 第一次合成
copyPict.paste(cropPict, (20, 100))             # 第二次合成
copyPict.save("tmp_pic18.jpg")                   # 儲存

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

newImage.save("tmp_pic19.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

from PIL import ImageFilter

image = Image.open(filename)       # 建立Pillow物件
filterPict = image.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic20_BLUR.jpg")

filterPict = image.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic21_CONTOUR.jpg")

filterPict = image.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic22_EMBOSS.jpg")

filterPict = image.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic23_FIND_EDGES.jpg")

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
newImage.save("tmp_pic24.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
# fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36) 找不到字形
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
fontInfo = ImageFont.truetype(font_filename, 36)

drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\ebas927.ttf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\DFZongYiStd-W9.otf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

newImage.save("tmp_pic26.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
#fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
fontInfo = ImageFont.truetype(font_filename, 36)

drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)
newImage.save("tmp_pic27.png")

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

print('------------------------------------------------------------')	#60個

#filter
from PIL import Image,ImageFilter
image=Image.open(filename)
image2=image.filter(ImageFilter.EDGE_ENHANCE)
#image2.show()

print('------------------------------------------------------------')	#60個

#crop
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 300
    image2 = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image2.size)
    image2.save("tmp_pic29.jpg")

print('------------------------------------------------------------')	#60個

#rotate0
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image2.save("tmp_pic30.jpg")

print('------------------------------------------------------------')	#60個

# rotate1
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image2.save( "tmp_pic31_rotate.jpg")

print('------------------------------------------------------------')	#60個

# resize
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image2 = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image2.size)
    image2.save("tmp_pic31_resize.jpg" )

print('------------------------------------------------------------')	#60個

#sharpness
from PIL import Image,ImageEnhance
with Image.open(filename) as image:
    image2 = ImageEnhance.Contrast(image).enhance(0.3)
    image2.save("tmp_pic32_contrast.jpg") 

print('------------------------------------------------------------')	#60個

# transpose
from PIL import Image,ImageEnhance
with Image.open(filename) as image:
    image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image2.save( "tmp_pic33b.jpg")
    image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image2.save( "tmp_pic33c.jpg")
    image2 = image.transpose(Image.ROTATE_90)
    image2.save( "tmp_pic33d.jpg")
    image2 = image.transpose(Image.ROTATE_180)
    image2.save( "tmp_pic33e.jpg")
    image2 = image.transpose(Image.ROTATE_270)
    image2.save( "tmp_pic33f.jpg")
    image2 = image.transpose(Image.TRANSPOSE)
    image2.save( "tmp_pic33g.jpg")
    image2 = image.transpose(Image.TRANSVERSE)
    image2.save( "tmp_pic33h.jpg")

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
pic=image.convert("1")
#pic.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 350
    image_new = image.crop((x, y, x1, y1))
    print(image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Brightness(image).enhance(2.5)
    image_new.save("tmp_pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter

image = Image.open(filename)
image_new = image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print(image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save("tmp_pic_view_resize.jpg" )

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save("tmp_pic_rotate180.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate111.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate000.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose90.jpg")
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transposeLR.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
image.save("tmp_pic_quality95.jpg", quality=95 )
image.close()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
image.save("tmp_pic_quality_default.jpg")
image.close()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont
image=Image.open(filename)
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(image)
draw.text((50,50),"牡丹亭",font=imfont,fill=(0,255,255,255))
#image.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

import matplotlib.pyplot as plt

image = Image.open(filename)

plt.imshow(image)

plt.show()

w,h = image.size

image1 = image.resize((w*2,h), Image.LANCZOS)

plt.imshow(image1)

plt.show()

image2 = image.convert('1')

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：基本繪圖

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt

#繪直線

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.line([40,50,360,280], fill="blue", width=3)

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個


#繪矩形

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.rectangle((100,80,300,240), fill="yellow", outline="black")

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪點

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.point([(100,100), (100,101), (100,102)], fill='red')

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪圓或橢圓

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.ellipse((50,50,350,250), fill="purple", outline="green")

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪多邊形

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.polygon([(200,40),(60,250),(320,250)], fill="brown", outline="red")

plt.imshow(image)

plt.show()


print('------------------------------------------------------------')	#60個

#繪文字

from PIL import ImageFont

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((150,80), "font demo", fill="red")  #繪英文文字

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
myfont = ImageFont.truetype(font_filename, 24)

draw_image.text((120,150),"雅黑字體示範", fill="blue", font=myfont)  #繪中文 

plt.imshow(image)

plt.show()

#繪文字

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((120,80), "English Demo", fill="red")  #繪製英文文字

myfont = ImageFont.truetype(font_filename, 24)

draw_image.text((120,150), "中文字型示範", fill="blue", font=myfont) #繪製中文文字

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：繪圖範例

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

image = Image.new("RGB", (300,400), "lightgray")

draw_image = ImageDraw.Draw(image)

#繪圓
draw_image.ellipse((50,50,250,250), width=3, outline="gold")# 臉

#繪多邊形
draw_image.polygon([(100,90), (120,130), (80,130)], fill="brown", outline="red") #左眼精
draw_image.polygon([(200,90), (220,130), (180,130)],   fill="brown", outline="red")#右眼精

#繪矩形
draw_image.rectangle((140,140,160,180),    fill="blue", outline="black") #鼻子

#繪橢圓
draw_image.ellipse((100,200,200,220), fill="red") #嘴巴   

#繪文字
draw_image.text((130,280), "ABCDEFG", fill="orange")  #英文字

myfont = ImageFont.truetype(font_filename, 16)

draw_image.text((110,320), "測試使用中文字", fill="red", font=myfont) #中文字 

plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
"""
print("------------------------------------------------------------")  # 60個

import os

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
"""

post_html = """
</table>
</body>
</html>
"""
"""
table_html = ""

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容            
            table_html += "<tr><td><a href='{}'><img src='{}'></a></td></tr>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

import os

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
"""

post_html = """
</tr>
</table>
</body>
</html>
"""


table_html = ""
"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for index, file in enumerate(allfiles):
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容         
            table_html += "<td><a href='{}'><img src='{}'></a></td>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
            if (index+1) % 3 == 0:
                table_html += "</tr><tr>"
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

def blue_to_red(image_path):
    image = Image.open(image_path)
    r, g, b = image.split() # 分離三個通道
    image = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    image.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

"""
def blue_to_red2(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    image.show()
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    

import sys
import matplotlib.pyplot as plt

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw
image = Image.new("RGB", (400, 300), '#00FF00')
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    image_new = image.crop((x, y, w, h))
    print(image_new.size)
    image_new.save('tmp_pic_crop.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageEnhance
with Image.open(filename) as image:
   image_new = ImageEnhance.Brightness(image).enhance(2.5)
   image_new.save('tmp_pic_brightness.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFilter
image = Image.open(filename)
plt.imshow(image)
plt.title('原圖')
plt.show()

new = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(new)
plt.title('after filter')
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
pic = image.convert("1")
plt.imshow(pic)
plt.title('convert L')
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    w = 200
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save('tmp_pic_resize.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save('tmp_pic_rotate.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30_zero.jpg')

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save('tmp_pic_normal.jpg')
image.close()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save('tmp_pic_high.jpg', quality = 95)
image.close()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw, ImageFont
image = Image.open(filename)
imfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 40)
draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Peony', font = imfont, fill = (0, 255, 255, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save('tmp_pic_rotate_90.jpg')
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save('tmp_pic_flip.jpg')

print('------------------------------------------------------------')	#60個

print('保持圖片原始大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60a.jpg")

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60b.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    image_new = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image_new = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image_new.size)
    image_new.save("tmp_pic_resize.jpg" )

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Contrast(image).enhance(0.3)
    image_new.save("tmp_pic_contrast.jpg") 

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transpose1.jpg")
    image_new = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_new.save("tmp_pic_transpose2.jpg")
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose3.jpg")
    image_new = image.transpose(Image.ROTATE_180)
    image_new.save("tmp_pic_transpose4.jpg")
    image_new = image.transpose(Image.ROTATE_270)
    image_new.save("tmp_pic_transpose5.jpg")
    image_new = image.transpose(Image.TRANSPOSE)
    image_new.save("tmp_pic_transpose6.jpg")
    image_new = image.transpose(Image.TRANSVERSE)
    image_new.save("tmp_pic_transpose7.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter
image=Image.open(filename)
image_new=image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個
"""
print("車牌")
import pytesseract
text = pytesseract.image_to_string(Image.open('data/atq9305.jpg'))
print(type(text), "   ", text)

print("------------------------------------------------------------")  # 60個

import pytesseract
import time

carDict = {}
myPath = "C:\\_git\\vcs\\_4.python\\PIL\\new1\\"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        carDict[keyText] = entryTime

print("------------------------------------------------------------")  # 60個


"""
from PIL import Image
import pytesseract
import time

carDict = {}
myPath = "foldername"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        exitSecond = time.time()
        dxSecond = exitSecond - carDict[keyText]
        hour = dxSecond % 3600          # 由餘數判斷是否進位
        hours = dxSecond // 3600        # 計算小時數
        if hour != 0:
            hours += 1
        print("停車費用 : ", hours * 60, " 元 ")
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        entrySecond = time.time()
        carDict[keyText] = entrySecond
"""
print("------------------------------------------------------------")  # 60個

import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_26.jpg'),
                                    lang='chi_tra')
print(text)

print("------------------------------------------------------------")  # 60個

import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_27.jpg'),
                                               lang='chi_sim')
print(text)
"""
print("------------------------------------------------------------")  # 60個

"""
import os

def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            image = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            image = image.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            image.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)
"""
print("------------------------------------------------------------")  # 60個

"""
import os

def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            image = Image.open(path)
            image_rgb = image.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            image_rgb.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')
"""

print("------------------------------------------------------------")  # 60個

"""
from PIL import Image, ImageDraw, ImageFont

def generate_product_image(product_image_path, background_image_path, promo_text):
    # 加載產品和背景影像
    product_image = Image.open(product_image_path).resize((200, 200))
    background_image = Image.open(background_image_path)
    # 在背景影像上放置產品影像
    background_image.paste(product_image, (50, 50), product_image)
    # 在影像上添加促銷文字
    draw = ImageDraw.Draw(background_image)
    font = ImageFont.truetype("arial.ttf", size=45)
    draw.text((50, 260), promo_text, font=font, fill="white")
    # 保存或返回影像
    background_image.save('output_promo_image.jpg')

generate_product_image('product.png', 'background.jpg', '特價促銷!')
"""
print("------------------------------------------------------------")  # 60個



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

hungPic = Image.open(filename)        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 600
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))
newImage.save("tmp_pic_2.jpg")

print("------------------------------------------------------------")  # 60個

"""
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_10.jpg'),
                                               lang='chi_sim')
print(text)
with open('tmp_17_10.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)
"""

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

from PIL import Image
from PIL import ImageFilter
rushMore = Image.open(filename)       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic_4_BLUR.png")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic_4_CONTOUR.png")
filterPict = rushMore.filter(ImageFilter.DETAIL)
filterPict.save("tmp_pic_4_DETAIL.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE_MORE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE_MORE.png")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic_4_EMBOSS.png")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic_4_FIND_EDGES.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH)
filterPict.save("tmp_pic_4_SMOOTH.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH_MORE)
filterPict.save("tmp_pic_4_SMOOTH_MORE.png")
filterPict = rushMore.filter(ImageFilter.SHARPEN)
filterPict.save("tmp_pic_4_SHARPEN.png")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image, ImageDraw, ImageFont

hungPic = Image.open(filename)        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 700
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(newImage)
name = "牡丹亭"
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 60)
drawObj.text((140,600), name, fill='Blue', font=fontInfo)

newImage.save("tmp_pic_6.jpg")

print("------------------------------------------------------------")  # 60個



from PIL import Image

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("------------------------------------------------------------")  # 60個

"""

image = Image.open(filename)
print(image.format, image.size, image.mode)

#image.show()

print("------------------------------------------------------------")  # 60個

print("剪裁圖像")

image = Image.open(filename)
rect = 80, 20, 310, 360
image.crop(rect).show()

print('------------------------------------------------------------')	#60個

print("生成縮略圖")

image = Image.open(filename)
size = 128, 128
image.thumbnail(size)
image.show()
"""
print("------------------------------------------------------------")  # 60個

print("縮放和黏貼圖像")

filename2 = "C:/_git/vcs/_1.data/______test_files1/bear.jpg"

image1 = Image.open(filename2)
image2 = Image.open(filename)
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

image1.show()

"""
print("旋轉和翻轉")

image = Image.open(filename)
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

print('------------------------------------------------------------')	#60個
"""

print("操作像素")

image = Image.open(filename)
for x in range(100, 200):
    for y in range(250, 350):
        image.putpixel((x, y), (128, 128, 128))
image.show()

sys.exit()

print("------------------------------------------------------------")  # 60個

print("濾鏡效果")

from PIL import Image, ImageFilter

image = Image.open(filename)
image.filter(ImageFilter.CONTOUR).show()




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



"""

#另存新檔
image.save("tmp_pic_01.png")
#image.show()





"""
