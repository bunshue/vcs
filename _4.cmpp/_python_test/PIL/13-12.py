import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

filename = 'data/sample_s.jpg'

im = Image.open(filename)
filename = '__temp/tmppic_old'
im.save(filename+'.png', 'PNG')
print('舊檔存圖, 已寫入檔案：'+filename+'.png')

im_w, im_h = im.size
print("W = " + str(im_w)+", H = " + str(im_h))

print("在圖上作畫")

text_msg = '此為測試用影像'
font = ImageFont.truetype('data/ubuntu.ttf', 80)
dw = ImageDraw.Draw(im)
#fn_w, fn_h = dw.textsize(unicode(text_msg, 'utf-8'), font=font)
fn_w, fn_h = dw.textsize(str(text_msg), font=font)

x = im_w/2-fn_w/2
y = im_h/2-fn_h/2
dw.text((x+5, y+5), str(text_msg), font=font, fill=(25,25,25))
dw.text((x, y), str(text_msg), font=font, fill=(128,255,255))

#im.show()
filename = '__temp/tmppic_new'
im.save(filename+'.png', 'PNG')
print('新檔存圖, 已寫入檔案：'+filename+'.png')



