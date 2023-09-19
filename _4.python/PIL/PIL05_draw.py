from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

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

import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

filename = r'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

mesg = '牡丹亭'
im = Image.open(filename)

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

dw = ImageDraw.Draw(im)

font = ImageFont.truetype(font_filename, 80)
fn_w, fn_h = dw.textsize(mesg, font = font)

x = w/2-fn_w/2
y = h/2-fn_h/2
dw.text((x+5, y+5), mesg, font=font, fill=(25,25,25))
dw.text((x, y), mesg, font=font, fill=(128,255,255))

plt.imshow(im)

plt.show()

sys.exit()

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

print("作業完成")

print('------------------------------------------------------------')	#60個
