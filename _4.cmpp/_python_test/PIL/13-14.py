#在圖上寫字
import os, sys
from PIL import Image, ImageDraw, ImageFont

filename = 'data\sample.jpg'

#要做浮水印的文字
msg = "lion-mouse"
#文字大小
font_size = 10
fill = (255,255,255,100)

image_file = Image.open(filename)
im_w, im_h = image_file.size

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype('data/ubuntu.ttf',font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
dw = ImageDraw.Draw(im)
x = int(im_w/2 - fn_w/2)
y = int(im_h/2 - fn_h/2)
dw.text((0, 0), msg, font=font, fill=fill)
image_file.paste(im, (x, y), im)
#image_file.show()

filename = '__temp/tmppic_new'
image_file.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')



