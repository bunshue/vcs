# _*_ coding: utf-8 _*_
# 程式 13-14 (Python 3 Version)
import os, sys
from PIL import Image, ImageDraw, ImageFont

if len(sys.argv)<2:
    print("請指定要處理的圖形檔案！")
    exit(1)
filename = sys.argv[1]

msg = input('請輸入要做浮水印的文字：')
font_size = int(input('文字大小：'))
fill = (255,255,255,100)

image_file = Image.open(filename)
im_w, im_h = image_file.size

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype('font/wt014.ttf',font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
dw = ImageDraw.Draw(im)
x = int(im_w/2 - fn_w/2)
y = int(im_h/2 - fn_h/2)
dw.text((0, 0), msg, font=font, fill=fill)
image_file.paste(im, (x, y), im)
image_file.show()
filename, ext = filename.split('.')
if os.path.exists(filename+'_wm.png'):
    ans = input('此檔案已存在，要覆寫嗎？(y/n)')
    if ans != 'y' and ans != 'Y':
        exit(1)

image_file.save(filename+'_wm.png', 'PNG')
print('已寫入檔案：'+filename+'_wm.png')
