"""

PIL 畫圖


"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

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

print("------------------------------------------------------------")  # 60個

print('量測字串的大小')
filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
image = Image.open(filename)    #PIL讀取本機圖片, RGB模式
dw = ImageDraw.Draw(image)
mesg = '傷心橋下春波綠，曾是驚鴻照影來。'
xx, yy, text_width, text_height = dw.textbbox((0, 0), mesg, font=font, spacing=0, align='left')
print(xx, yy, text_width, text_height)
#0 12 200 58

print('draw01------------------------------------------------------------')	#60個
print('PIL畫字大全')

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

# 檔案 => PIL影像
image = Image.open(filename)    #PIL讀取本機圖片, RGB模式
w, h = image.size
print("W = " + str(w)+", H = " + str(h))

dw = ImageDraw.Draw(image)

#畫字1
mesg = 'This is a lion-mouse'
dw.text((100,100), mesg)

#畫字2

mesg = '大象與我'
x_st = 100
y_st = 150
dw.text((x_st + 5, y_st + 5), mesg, font=font, fill=(25,25,25)) #畫陰影
dw.text((x_st, y_st), mesg, font=font, fill=(128,255,255)) #畫文字





plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

mesg = "歡迎來到美國"
xx, yy, width, height = font.getbbox(mesg)

print('製作一個 W = ' + str(width) + ', H = ' + str(height) + ' 的圖片')
image = Image.new('RGBA', (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(image)

#寫字
draw.text((0,0), mesg, (0,0,0), font)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

mesg = '歡迎來到美國'

fill = (255, 0, 0)    #字的顏色RGB

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)

print('取得文字框')
xx, yy, text_width, text_height = dw0.textbbox((0, 0), mesg, font=font, spacing=0, align='left')
print('xx =', xx)
print('yy =', yy)
print('W =', text_width)
print('H =', text_height)

print('取得文字長')
length = dw0.textlength(mesg, font=font)
print('L =', length)

print('製作一個 W = ' + str(text_width) + ', H = ' + str(text_height) + ' 的圖片')
im = Image.new('RGBA', (text_width, text_height), (255,255,255,0))
dw = ImageDraw.Draw(im)
dw.text((0,0), mesg, font=font, fill=fill)

plt.imshow(im)
plt.show()

print('draw01------------------------------------------------------------')	#60個

# 在圖上作畫

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

# 檔案 => PIL影像
image = Image.open(filename)    #PIL讀取本機圖片, RGB模式

w, h = image.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫1")

dw = ImageDraw.Draw(image)

#畫矩形
dw.rectangle((0,0,w,h), fill=None, outline=(255,0,0), width=10)

#畫線
dw.line((0,0,w,h),width=20, fill=(255,0,0))
dw.line((w,0,0,h),width=20, fill=(255,0,0))

#畫圓
dw.ellipse((0,0,w,h),outline=(255,255,0))


plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個

""" TBD
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
im = Image.open(filename)
im_w, im_h = im.size

plt.imshow(im)
plt.show()

W = im_w
H = im_h


#im是原圖
#im0是要貼上的浮水印

im0 = Image.new('RGBA', (W, H))
dw0 = ImageDraw.Draw(im0)

#寫字
mesg = "牡丹亭"

dw0.text((0,0), mesg, (255,0,0), font)

plt.imshow(im0)
plt.show()

im = Image.new('RGBA', (W, H), (255,0,255,0))
dw = ImageDraw.Draw(im)

x=3
y=3

fill = (255,0,0,100) # R G B A
dw.text((0, 0), mesg, font=font, fill=fill)

#將im0貼到im上
im.paste(im0, (x, y), im)

plt.imshow(im)

plt.show()

"""

print('------------------------------------------------------------')	#60個

from matplotlib import patches

#在圖上作畫

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
im=Image.open(filename)
im_w, im_h = im.size
W = im_w
H = im_h

pic = plt.imshow(im, alpha = 0.8)    #alpha顯示

x_st = 20
y_st = 20
w = W - 40
h = H - 40

#畫出矩形
patch  = patches.Rectangle((x_st, y_st), w, h, fill=False, linewidth=2, color='r')
pic.axes.add_patch(patch)

#畫多邊形
vertices = []
vertices.append((0, 0))
vertices.append((100, 0))
vertices.append((100, 100))
vertices.append((50, 150))
vertices.append((0, 100))
vertices.append((0, 0))
patch = patches.Polygon(vertices, closed=True, fill=False, linewidth=2, color='g')
pic.axes.add_patch(patch)

text = "AAAAA"
plt.text(100, 10, text, fontsize=20, weight="bold", va="bottom", color='b')  

text = "BBBBB"
plt.text(100, 50, text, fontsize=20, va="top", color='b')  #列印文字

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename)        # 建立Pillow物件
newPic = image1.resize((300,400))

W, H = 400, 550
image2 = Image.new('RGB', (W, H), "Yellow")

image2.paste(newPic, (50, 50))

drawObj = ImageDraw.Draw(image2)
name = "牡丹亭"

font_size = 30
font = ImageFont.truetype(font_filename, font_size)
font = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', font_size)

drawObj.text((100,450), name, fill = 'Blue', font = font)

plt.imshow(image2)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖1')

W, H = 300, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立300*300黃色底的影像
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

W, H = 300, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立300*300黃色底的影像
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

W, H = 600, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立600*300黃色底的影像

drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
font = ImageFont.truetype('OLDENGL.TTF', 36)
font = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=font)

strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

#新細明體中文字型
font_filename = 'C:/Windows/Fonts/mingliu.ttc'

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

drawObj.text((50,180), strCtext, fill = 'Blue', font = font)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)  # 開啟圖片

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw = ImageDraw.Draw(image)  # 準備在圖片上繪圖
draw.text((0, 0), "牡丹亭", fill=(0, 0, 255), font=font)  # 將文字畫入圖片

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)
w, h = image.size  # 取得圖片尺寸

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw = ImageDraw.Draw(image)
draw.text(
    (0, h - 100), "牡丹亭", fill=(255, 255, 255), font=font
)  # 使用 h-100 定位到下方

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
image.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)
w, h = image.size

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

# 檔案 => PIL影像
image2 = Image.open(filename)  # 再次開啟原本的圖為 image2
image2.paste(text, (50, 0), text)  # 將文字貼上 image2
image2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
image2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
image.paste(image2, (0, 0), image2)  # 將 image2 貼上 image

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw = ImageDraw.Draw(image)  # 準備在圖片上繪圖
# 將文字畫入圖片
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
font = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)

drawObj.text((50,100), strText, fill='Blue', font=font)
# 處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

drawObj.text((50,180), strCtext, fill='Blue', font=font)

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

drawObj.text((50,180), strCtext, fill='Blue', font=font)

plt.imshow(newImage)
plt.show()

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
font = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)

drawObj.text((50,100), strText, fill='Blue', font=font)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
font = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=font)

plt.imshow(newImage)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image=Image.open(filename)

font=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(image)
draw.text((50,50),"牡丹亭",font=font,fill=(0,255,255,255))

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

#Pillow：基本繪圖

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

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((150,80), "font demo", fill="red")  #繪英文文字

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw_image.text((120,150),"雅黑字體示範", fill="blue", font=font)

plt.imshow(image)

plt.show()

#繪文字

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((120,80), "English Demo", fill="red")  #繪製英文文字

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw_image.text((120,150), "中文字型示範", fill="blue", font=font)

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：繪圖範例

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

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

draw_image.text((110,320), "測試使用中文字", fill="red", font=font)

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (400, 300), '#00FF00')
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()


print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
image = Image.open(filename)

font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 40)
draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Peony', font = font, fill = (0, 255, 255, 255))
plt.imshow(image)
plt.show()


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("新進")

newImage = Image.new('RGBA', (300, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

drawObj.rectangle((0,0,299,299), outline='Black')   # 影像外框線
drawObj.ellipse((30,60,130,100),outline='Black')    # 左眼外框
drawObj.ellipse((65,65,95,95),fill='Blue')          # 左眼
drawObj.ellipse((170,60,270,100),outline='Black')   # 右眼外框
drawObj.ellipse((205,65,235,95),fill='Blue')        # 右眼
drawObj.polygon([(150,120),(180,180),(120,180),(150,120)],fill='Aqua') # 鼻子
drawObj.rectangle((100,210,200,240), fill='Red')    # 嘴   

print('------------------------------------------------------------')	#60個

print('建立影像 RGBA, 在上面畫圖')
W, H = 400, 300
color = "Yellow"
image = Image.new('RGBA', (W, H), color)

for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        image.putpixel((x, y), (0, 255, 255, 255))   # 填青色

for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        image.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA")) # 填藍色

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

#添加水印
#一、添加文字水印

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => RGBA
im = Image.open(filename).convert('RGBA')
txt=Image.new('RGBA', im.size, (0,0,0,0))
font=ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d=ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30), 'Peony', font=font, fill=(255,0,255,255))
out=Image.alpha_composite(im, txt)
plt.imshow(out)
plt.show()

print('------------------------------------------------------------')	#60個

"""
#二、添加小圖片水印

# 檔案 => PIL影像
im = Image.open(filename)

# 檔案 => PIL影像
mark=Image.open("logo_small.gif")

layer=Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150,im.size[1]-60))
out=Image.composite(layer,im,layer)
#out.show()
plt.imshow(out)
plt.show()

"""

print('------------------------------------------------------------')	#60個

"""
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

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename

# 檔案 => PIL影像
image = Image.open(infile)

draw = ImageDraw.Draw(image)  #在圖片畫線的準備
draw.line((0, 0, image.width, image.height), fill="RED", width=8) #畫線

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimage=ImageDraw.Draw(image)

#繪多邊形
drawimage.polygon([(200,100),(350,150),(50,150)],fill="blue",outline="red")#屋頂
#繪矩形
drawimage.rectangle((100,150,300,250),fill="green",outline="black") #房間
#繪圓
drawimage.ellipse((300,40,350,90),fill="red")#太陽 
#繪橢圓
drawimage.ellipse((60,80,100,100),fill="white") #白雲一   
drawimage.ellipse((100,60,130,80),fill="white") #白雲二 
#繪文字
drawimage.text((120,170),"e-happy",fill="orange")
font_filename = 'C:/Windows/Fonts/mingliu.ttc'

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

drawimage.text((120,200),"文淵閣工作室",fill="red",font=font)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.new("RGB",(400,300),"lightgray") #淡灰色
drawimage=ImageDraw.Draw(image)
  
#繪點
for i in range(0,400,10):
    for j in range(0,300,10):    
        drawimage.point([(i,j)],fill="red")  
#繪直線
for i in range(0,400,10):
    drawimage.line([(i,300),(200,150)],width=2,fill="blue") 

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print("PIL_line")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 讀取圖像到數組中
# 檔案 => PIL影像 => numpy陣列
image = np.array(Image.open(filename))

plt.figure()
plt.imshow(image)

x = [100, 100, 200, 200]
y = [200, 400, 200, 400]
# 使用紅色星狀標記繪制點
plt.plot(x, y, 'r*')

# 繪制連接兩個點的線（默認為藍色）
plt.plot(x[:2], y[:2])

plt.title('畫圖')

# show()命令首先打開圖形用戶界面（GUI），然後新建一個窗口，該圖形用戶界面會循環阻斷腳本，然後暫停，
# 直到最後一個圖像窗口關閉。每個腳本里，只能調用一次show()命令，通常相似腳本的結尾調用。
plt.show()

print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


