import sys

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
image.save("tmp_pic01.png")
#image.show()

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
image.save("tmp_pic02.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (300, 180))     # 建立完全透明影像
image.save("tmp_pic03.png")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
width, height = image.size

newPict1 = image.resize((width*2, height))   # 寬度是2倍
newPict1.save("tmp_pic04.jpg")

newPict2 = image.resize((width, height*2))   # 高度是2倍
newPict2.save("tmp_pic05.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
image.rotate(90).save("tmp_pic06.jpg")      # 旋轉90度
image.rotate(180).save("tmp_pic07.jpg")     # 旋轉180度
image.rotate(270).save("tmp_pic08.jpg")     # 旋轉270度

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                       # 建立Pillow物件
image.rotate(45).save("tmp_pic09.jpg")                  # 旋轉45度
image.rotate(45, expand=True).save("tmp_pic10.jpg")     # 旋轉45度圖像擴充

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                     # 建立Pillow物件
image.transpose(Image.FLIP_LEFT_RIGHT).save("tmp_pic11.jpg")    # 左右
image.transpose(Image.FLIP_TOP_BOTTOM).save("tmp_pic12.jpg")    # 上下

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
newImage.save("tmp_pic25.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\ebas927.ttf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

newImage.save("tmp_pic26.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
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

image = Image.open(filename)
print(image.format)
print(image.mode)
print(image.width)
print(image.height)
print(image.size)

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

print("------------------------------------------------------------")  # 60個

'''
from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#im.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

im = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(im)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#im.show()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
pic=im.convert("1")
#pic.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print(im.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 350
    new_im = im.crop((x, y, x1, y1))
    print(new_im.size)
    new_im.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = ImageEnhance.Brightness(im).enhance(2.5)
    new_im.save("tmp_pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter

im=Image.open(filename)
new=im.filter(ImageFilter.EDGE_ENHANCE)
#new.show()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
print('圖檔格式: ',im.format)
print('圖檔的色彩模式: ',im.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',im.size)
print('圖片的寬度，單位像素(pixels): ',im.width)
print('圖片的高度，單位像素(pixels): ',im.height)

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print(im.size)
    w=100
    r = w/im.size[0]
    h = int(im.size[1]*r) #依縮放比例計算高度
    new_im = im.resize((w, h))
    print(new_im.size)
    new_im.save("tmp_pic_view_resize.jpg" )

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(180)
    new_im.save("tmp_pic_rotate180.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    new_im.save("tmp_pic_rotate111.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    new_im.save("tmp_pic_rotate000.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save("tmp_pic_transpose90.jpg")
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save("tmp_pic_transposeLR.jpg")

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
im.save("tmp_pic_quality95.jpg", quality=95 )
im.close()

print("------------------------------------------------------------")  # 60個

im = Image.open(filename)
im.save("tmp_pic_quality_default.jpg")
im.close()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont
im=Image.open(filename)
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(im)
draw.text((50,50),"牡丹亭",font=imfont,fill=(0,255,255,255))
im.show()
'''
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

import matplotlib.pyplot as plt

img = Image.open(filename)

plt.imshow(img)

plt.show()

w,h = img.size

img1 = img.resize((w*2,h), Image.ANTIALIAS)

plt.imshow(img1)

plt.show()

img2 = img.convert('1')

plt.imshow(img2)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：基本繪圖

from PIL import Image, ImageDraw

import matplotlib.pyplot as plt

#繪直線

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.line([40,50,360,280], fill="blue", width=3)

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個


#繪矩形

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.rectangle((100,80,300,240), fill="yellow", outline="black")

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪點

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.point([(100,100), (100,101), (100,102)], fill='red')

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪圓或橢圓

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.ellipse((50,50,350,250), fill="purple", outline="green")

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#繪多邊形

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.polygon([(200,40),(60,250),(320,250)], fill="brown", outline="red")

plt.imshow(img)

plt.show()


print('------------------------------------------------------------')	#60個

#繪文字

from PIL import ImageFont



img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.text((150,80), "font demo", fill="red")  #繪英文文字

myfont = ImageFont.truetype("msyh.ttc",24)

drawimg.text((120,150),"雅黑字體示範", fill="blue", font=myfont)  #繪中文 

plt.imshow(img)

plt.show()

#繪文字

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

img = Image.new("RGB", (400,300), "lightgray")

drawimg = ImageDraw.Draw(img)

drawimg.text((120,80), "English Demo", fill="red")  #繪製英文文字

myfont = ImageFont.truetype(font_filename, 24)

drawimg.text((120,150), "中文字型示範", fill="blue", font=myfont) #繪製中文文字

plt.imshow(img)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：繪圖範例

from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

img = Image.new("RGB", (300,400), "lightgray")

drawimg = ImageDraw.Draw(img)

#繪圓
drawimg.ellipse((50,50,250,250), width=3, outline="gold")# 臉

#繪多邊形
drawimg.polygon([(100,90), (120,130), (80,130)], fill="brown", outline="red") #左眼精
drawimg.polygon([(200,90), (220,130), (180,130)],   fill="brown", outline="red")#右眼精

#繪矩形
drawimg.rectangle((140,140,160,180),    fill="blue", outline="black") #鼻子

#繪橢圓
drawimg.ellipse((100,200,200,220), fill="red") #嘴巴   

#繪文字
drawimg.text((130,280), "ABCDEFG", fill="orange")  #英文字

myfont = ImageFont.truetype(font_filename, 16)

drawimg.text((110,320), "測試使用中文字", fill="red", font=myfont) #中文字 

plt.imshow(img)

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
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
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
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
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
            im = Image.open(os.path.join(source, file))
            thumbnail = im.resize((320,200))
            thumbnail.save(os.path.join(target, targetfile))
            im.close()
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
    img = Image.open(image_path)
    r, g, b = img.split() # 分離三個通道
    img = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    img.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

"""
def blue_to_red2(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    for y in range(img.height):
        for x in range(img.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    img.show()
    
    
    
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

image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    new_image = image.crop((x, y, w, h))
    print(new_image.size)
    new_image.save('tmp_pic_crop.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageEnhance
with Image.open(filename) as image:
   new_image = ImageEnhance.Brightness(image).enhance(2.5)
   new_image.save('tmp_pic_brightness.jpg')

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
    new_image = image.resize((w, h))
    print(new_image.size)
    new_image.save('tmp_pic_resize.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    new_image = image.rotate(180)
    new_image.save('tmp_pic_rotate.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    new_image = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    new_image.save('tmp_pic_rotate30.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    new_image = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    new_image.save('tmp_pic_rotate30_zero.jpg')

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
    new_image = image.transpose(Image.ROTATE_90)
    new_image.save('tmp_pic_rotate_90.jpg')
    new_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    new_image.save('tmp_pic_flip.jpg')

print('------------------------------------------------------------')	#60個

im = Image.open(filename)
print(im.format)
print(im.mode)
print(im.width)
print(im.height)
print(im.size)

print("------------------------------------------------------------")  # 60個

print('保持圖片原始大小之旋轉')
with Image.open(filename) as im:
  new_im = im.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  new_im.save("tmp_pic_rotate60a.jpg")

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
with Image.open(filename) as im:
  new_im = im.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  new_im.save("tmp_pic_rotate60b.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print('原圖片的尺寸大小:',im.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    new_im = im.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', new_im.size)
    new_im.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as im:
    print('原圖片的尺寸大小:',im.size)
    w=100
    r = w/im.size[0]
    h = int(im.size[1]*r)
    new_im = im.resize((w, h))
    print('圖片經縮放後的尺寸大小:',new_im.size)
    new_im.save("tmp_pic_resize.jpg" )

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = ImageEnhance.Contrast(im).enhance(0.3)
    new_im.save("tmp_pic_contrast.jpg") 

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as im:
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save("tmp_pic_transpose1.jpg")
    new_im = im.transpose(Image.FLIP_TOP_BOTTOM)
    new_im.save("tmp_pic_transpose2.jpg")
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save("tmp_pic_transpose3.jpg")
    new_im = im.transpose(Image.ROTATE_180)
    new_im.save("tmp_pic_transpose4.jpg")
    new_im = im.transpose(Image.ROTATE_270)
    new_im.save("tmp_pic_transpose5.jpg")
    new_im = im.transpose(Image.TRANSPOSE)
    new_im.save("tmp_pic_transpose6.jpg")
    new_im = im.transpose(Image.TRANSVERSE)
    new_im.save("tmp_pic_transpose7.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter
im=Image.open(filename)
new=im.filter(ImageFilter.EDGE_ENHANCE)
#new.show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


