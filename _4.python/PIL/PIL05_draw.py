from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

selected_font = 'C:/_git/vcs/_1.data/______test_files1/ubuntu.ttf'

font_size=30

mesg = 'this is a lion mouse'

font = ImageFont.truetype(selected_font, font_size)
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

filename = 'C:/______test_files3/pil_test01.png'
img.save(filename)
print('已寫入檔案：' + filename)

plt.imshow(img)
plt.show()


from PIL import Image, ImageDraw, ImageFont

msg = 'lion-mouse'
selected_font = 'C:/_git/vcs/_1.data/______test_files1/ubuntu.ttf'

font_size = 30; #文字大小
font_r = 255;   #紅色值
font_g = 0;     #綠色值
font_b = 0;     #藍色值

fill = (font_r, font_g, font_b)

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(selected_font,font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)

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

#im.show()
filename = 'C:/______test_files3/tmppic_new'
im.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')



#在圖上寫字 OK, 只能英文字

import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

selected_font = 'C:/_git/vcs/_1.data/______test_files1/ubuntu.ttf'

filename1 = 'C:/_git/vcs/_1.data/______test_files1/sample_s.jpg'
filename2 = 'C:/______test_files3/tmppic_old.png'
filename3 = 'C:/______test_files3/tmppic_new.png'

text_msg = 'Hello, world!'
im = Image.open(filename1)

im.save(filename2, 'PNG')
print('舊檔存圖, 已寫入檔案：' + filename2)

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

dw = ImageDraw.Draw(im)

font = ImageFont.truetype(selected_font, 80)
fn_w, fn_h = dw.textsize(text_msg, font=font)

x = w/2-fn_w/2
y = h/2-fn_h/2
dw.text((x+5, y+5), text_msg, font=font, fill=(25,25,25))
dw.text((x, y), text_msg, font=font, fill=(128,255,255))

#im.show()  #顯示圖片
im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：' + filename)

plt.imshow(im)
plt.show()


#在圖上寫字

import os, sys
from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/sample.jpg'
filename2 = 'C:/______test_files3/pil_test03.png'
selected_font = 'C:/_git/vcs/_1.data/______test_files1/ubuntu.ttf'

#要做浮水印的文字
msg = "lion-mouse"
#文字大小
font_size = 10
fill = (255,255,255,100)

im = Image.open(filename1)
im_w, im_h = im.size

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype(selected_font, font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
dw = ImageDraw.Draw(im)
x = int(im_w/2 - fn_w/2)
y = int(im_h/2 - fn_h/2)
dw.text((0, 0), msg, font=font, fill=fill)
im.paste(im, (x, y), im)
#im.show()  #顯示圖片

im.save(filename2, 'PNG')
print('新檔存圖, 已寫入檔案：' + filename2)








#在圖上寫字 OK, 只能英文字

from PIL import Image, ImageDraw, ImageFont

selected_font = 'C:/_git/vcs/_1.data/______test_files1/ubuntu.ttf'
filename1 = 'C:/_git/vcs/_1.data/______test_files1/sample_s.jpg'
filename2 = 'C:/______test_files3/tmppic_old.png'
filename3 = 'C:/______test_files3/tmppic_new.png'


im = Image.open(filename1)
im.save(filename2+'.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename2+'.png')

w, h = im.size
print("W = " + str(w)+", H = " + str(h))

print("在圖上作畫")

dw = ImageDraw.Draw(im)

mesg = 'This is a lion-mouse'
font = ImageFont.truetype(selected_font, 80)
#fn_w, fn_h = dw.textsize(unicode(mesg, 'utf-8'), font=font)
fn_w, fn_h = dw.textsize(str(mesg), font=font)

x = w/2-fn_w/2
y = h/2-fn_h/2
dw.text((x+5, y+5), str(mesg), font=font, fill=(25,25,25))
dw.text((x, y), str(mesg), font=font, fill=(128,255,255))

#im.show()  #顯示圖片
im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)





# 在圖上作畫

from PIL import Image, ImageDraw

filename1 = 'C:/_git/vcs/_1.data/______test_files1/sample_s.jpg'
filename2 = 'C:/______test_files3/tmppic_old.png'
filename3 = 'C:/______test_files3/tmppic_new.png'


im = Image.open(filename1)

im.save(filename2, 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename2)

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

#im.show()  #顯示圖片

im.save(filename3, 'PNG')
print('新檔存圖, 已寫入檔案：'+filename3)



from PIL import Image
from matplotlib import patches
import matplotlib.pyplot as plt

#filename = 'C:/_git/vcs/_1.data/______test_files1/_emgu/lena.jpg'
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

