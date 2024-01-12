import sys

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'


'''
print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
