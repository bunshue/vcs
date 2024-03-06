"""

PIL 畫圖


"""
import os
import sys
from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

print('draw01------------------------------------------------------------')	#60個

# 在圖上作畫

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

im = Image.open(filename)

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫1")

dw = ImageDraw.Draw(im)

#畫一個外框
dw.rectangle((0,0,w,h), fill=None, outline=(255,0,0), width=10)
#畫線
dw.line((0,0,w,h),width=20, fill=(255,0,0))
dw.line((w,0,0,h),width=20, fill=(255,0,0))
#畫圓
dw.ellipse((0,0,w,h),outline=(255,255,0))
#寫字
mesg = 'This is a lion-mouse'
dw.text((100,100), mesg)

plt.imshow(im)

plt.show()

print('------------------------------------------------------------')	#60個

print("在圖上寫字")


filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式

w, h = image1.size
print("W = " + str(w)+", H = " + str(h))

dw = ImageDraw.Draw(image1)

mesg = '牡丹亭'
font = ImageFont.truetype(font_filename, 60)
xx, yy, text_width, text_height = dw.textbbox((0, 0), mesg, font=font, spacing=0, align='left')

x_st = w / 2 - text_width / 2
y_st = h / 2 - text_height / 2 + 100
dw.text((x_st + 5, y_st + 5), mesg, font=font, fill=(25,25,25))
dw.text((x_st, y_st), mesg, font=font, fill=(128,255,255))

plt.imshow(image1)

plt.show()

print('------------------------------------------------------------')	#60個


font_size = 30

mesg = 'this is a lion mouse'

font = ImageFont.truetype(font_filename, font_size)

xx, yy, width, height = font.getbbox(mesg)

print('製作一個 W = ' + str(width) + ', H = ' + str(height) + ' 的圖片')
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(img)

#寫字
draw.text((0,0), mesg, (0,0,0), font)

plt.imshow(img)
plt.show()

print('------------------------------------------------------------')	#60個

mesg = 'lion-mouse'

font_size = 30; #文字大小
fill = (255, 0, 0)    #字的顏色RGB

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(font_filename, font_size)

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

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

#要做浮水印的文字
mesg = "lion-mouse"
#文字大小
font_size = 10
fill = (255,255,255,100)

im = Image.open(filename)
im_w, im_h = im.size

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(font_filename, font_size)
xx, yy, text_width, text_height = dw0.textbbox((0, 0), mesg, font=font, spacing=0, align='left')

im = Image.new('RGBA', (text_width, text_height), (255,0,0,0))
dw = ImageDraw.Draw(im)
x = int(im_w/2 - text_width/2)
y = int(im_h/2 - text_height/2)
dw.text((0, 0), mesg, font=font, fill=fill)
im.paste(im, (x, y), im)

plt.imshow(im)

plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image
from matplotlib import patches

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im=Image.open(filename)

image=im.resize((300*1, 400//2))  #修改圖像大小

pic = plt.imshow(image)

#在圖上作畫

#pic = plt.imshow(image, alpha = 0.5)
origin = (0, 0)
w = 300*75/100
h = 400/2*75/100
#畫出矩形
patch  = patches.Rectangle(origin, w, h, fill=False, linewidth=2, color='r')
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


plt.text(100, 10, "ABCDEFG", fontsize=20, weight="bold", va="bottom", color='b')  

text = "CCCCCCC"  #取得文字
plt.text(vertices[0][0], vertices[0][1], text, fontsize=20, va="top", color='b')  #列印文字

plt.axis("off")

plt.show()



print('------------------------------------------------------------')	#60個

image1 = Image.open(filename)        # 建立Pillow物件
newPic = image1.resize((350,500))

W, H = 450, 700
image2 = Image.new('RGB', (W, H), "Yellow")

image2.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(image2)
name = "牡丹亭"
fontInfo = ImageFont.truetype(font_filename, 60)
drawObj.text((140,600), name, fill = 'Blue', font = fontInfo)

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
# 使用古老英文字型, 
fontInfo = ImageFont.truetype('OLDENGL.TTF', 36)
drawObj.text((50,100), strText, fill='Blue', font=fontInfo)

strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill = 'Blue', font = fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖4')

W, H = 600, 300
image = Image.new('RGBA', (W, H), "Yellow")  # 建立600*300黃色底的影像
drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill = 'Blue', font = fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('無影像之PIL畫圖5 same?')

W, H = 600, 300
image = Image.new('RGBA', (W, H), 'Yellow')  # 建立600*300黃色底的影像

drawObj = ImageDraw.Draw(image)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50, 50), strText, fill='Blue')         # 使用預設字型與字型大小
# 使用古老英文字型, 字型大小是36
fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
drawObj.text((50, 100), strText, fill='Blue', font=fontInfo)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

font_filename = 'C:/Windows/Fonts/mingliu.ttc'
fontInfo = ImageFont.truetype(font_filename, 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)  # 開啟圖片
font = ImageFont.truetype(font_filename, 50)  # 設定字型
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
draw.text((0, 0), "牡丹亭", fill=(0, 0, 255), font=font)  # 將文字畫入圖片

img.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
w, h = img.size  # 取得圖片尺寸
font = ImageFont.truetype(font_filename, 100)
draw = ImageDraw.Draw(img)
draw.text(
    (0, h - 100), "牡丹亭", fill=(255, 255, 255), font=font
)  # 使用 h-100 定位到下方

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
font = ImageFont.truetype(font_filename, 150)
# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
img.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
w, h = img.size

font = ImageFont.truetype(font_filename, 150)
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

img2 = Image.open(filename)  # 再次開啟原本的圖為 img2
img2.paste(text, (50, 0), text)  # 將文字貼上 img2
img2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img.paste(img2, (0, 0), img2)  # 將 img2 貼上 img

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
font = ImageFont.truetype(font_filename, 40)  # 設定字型與尺寸

draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
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

print("------------------------------------------------------------")  # 60個

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

print("------------------------------------------------------------")  # 60個

image = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
image=Image.open(filename)
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(image)
draw.text((50,50),"牡丹亭",font=imfont,fill=(0,255,255,255))
#image.show()

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

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((120,80), "English Demo", fill="red")  #繪製英文文字

myfont = ImageFont.truetype(font_filename, 24)

draw_image.text((120,150), "中文字型示範", fill="blue", font=myfont) #繪製中文文字

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

myfont = ImageFont.truetype(font_filename, 16)

draw_image.text((110,320), "測試使用中文字", fill="red", font=myfont) #中文字 

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

image = Image.open(filename)
imfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 40)
draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Peony', font = imfont, fill = (0, 255, 255, 255))
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


"""
newImage.save("tmp_pic24.png")
img.save("tmp_pic20.png")  # 儲存為 png
newImage.save("tmp_pic26.png")

newImage.save("tmp_pic27.png")

newImage.save("tmp_pic25.png")



"""
