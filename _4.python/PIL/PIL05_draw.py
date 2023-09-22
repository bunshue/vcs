import sys
from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

print('------------------------------------------------------------')	#60個

print("在圖上寫字")

from PIL import Image, ImageDraw, ImageFont

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式

w, h = image1.size
print("W = " + str(w)+", H = " + str(h))

dw = ImageDraw.Draw(image1)

mesg = '牡丹亭'
font = ImageFont.truetype(font_filename, 60)
fn_w, fn_h = dw.textsize(mesg, font = font)

x_st = w / 2 - fn_w / 2
y_st = h / 2 - fn_h / 2 + 100
dw.text((x_st + 5, y_st + 5), mesg, font=font, fill=(25,25,25))
dw.text((x_st, y_st), mesg, font=font, fill=(128,255,255))

plt.imshow(image1)

plt.show()

print('------------------------------------------------------------')	#60個


font_size = 30

mesg = 'this is a lion mouse'

font = ImageFont.truetype(font_filename, font_size)
font_size = font.getsize(mesg)
print(font_size)

width = font_size[0]
height = font_size[1]
print(width)
print(height)

print('製作一個 W = ' + str(width) + ', H = ' + str(height) + ' 的圖片')
img = Image.new('RGBA', (width, height), (255, 255, 255, 0))

draw = ImageDraw.Draw(img)

#寫字
draw.text((0,0), mesg, (0,0,0), font)

plt.imshow(img)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw, ImageFont

msg = 'lion-mouse'

font_size = 30; #文字大小
font_r = 255;   #紅色值
font_g = 0;     #綠色值
font_b = 0;     #藍色值

fill = (font_r, font_g, font_b)

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(font_filename, font_size)
fn_w, fn_h = dw0.textsize(msg, font = font)

print(fn_w)
print(fn_h)

aaa = dw0.textlength(msg, font=font)
print(aaa)

'''
bbb = dw0.textbbox(msg, font=font)
print(bbb)
'''


'''
hello = draw.textlength("Hello", font)
world = draw.textlength("World", font)
hello_world = hello + world  # not adjusted for kerning
assert hello_world == draw.textlength("HelloWorld", font)  # may fail
'''

print(fn_w)
print(fn_h)
print('製作一個 W = ' + str(fn_w) + ', H = ' + str(fn_h) + ' 的圖片')
im = Image.new('RGBA', (fn_w, fn_h), (255,255,255,0))
dw = ImageDraw.Draw(im)
dw.text((0,0), msg, font=font, fill=fill)

plt.imshow(im)
plt.show()

print('------------------------------------------------------------')	#60個

#在圖上寫字

import os, sys
from PIL import Image, ImageDraw, ImageFont

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

#要做浮水印的文字
msg = "lion-mouse"
#文字大小
font_size = 10
fill = (255,255,255,100)

im = Image.open(filename)
im_w, im_h = im.size

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(font_filename, font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
dw = ImageDraw.Draw(im)
x = int(im_w/2 - fn_w/2)
y = int(im_h/2 - fn_h/2)
dw.text((0, 0), msg, font=font, fill=fill)
im.paste(im, (x, y), im)

plt.imshow(im)

plt.show()

print('------------------------------------------------------------')	#60個

# 在圖上作畫

from PIL import Image, ImageDraw

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

im = Image.open(filename)

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

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

from PIL import Image
from matplotlib import patches
import matplotlib.pyplot as plt

#filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

'''
image1 = Image.open(filename)
  
image = Image.open(filename)
image_1 = image.convert('1')	#轉換成二值化圖像

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(image_1)

plt.show()
'''

print('------------------------------------------------------------')	#60個

im=Image.open(filename)

image=im.resize((305*1, 400//2))  #修改圖像大小

pic = plt.imshow(image)

#在圖上作畫

#pic = plt.imshow(image, alpha = 0.5)
origin = (0, 0)
w = 305*75/100
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

from PIL import Image, ImageDraw, ImageFont

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




print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個


print("作業完成")

print('------------------------------------------------------------')	#60個


