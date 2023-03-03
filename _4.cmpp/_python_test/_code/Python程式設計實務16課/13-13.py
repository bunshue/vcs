# _*_ coding: utf-8 _*_
# 程式 13-13 (Python 3 Version)
import os
from PIL import Image, ImageDraw, ImageFont

msg = input('請輸入要轉換的文字：')
font_size = int(input('文字大小：'))
font_r = int(input('紅色值：'))
font_g = int(input('綠色值：'))
font_b = int(input('藍色值：'))
filename = input('要儲存的檔案名稱：')
fill = (font_r, font_g, font_b)

im0 = Image.new('RGBA', (1,1))
dw0 = ImageDraw.Draw(im0)
font = ImageFont.truetype('font/wt014.ttf',font_size)
fn_w, fn_h = dw0.textsize(msg, font=font)
im = Image.new('RGBA', (fn_w, fn_h), (255,0,0,0))
dw = ImageDraw.Draw(im)
dw.text((0,0), msg, font=font, fill=fill)
if os.path.exists(filename+'.png'):
    ans = input('此檔案已存在，要覆寫嗎？(y/n)')
    if ans != 'y' and ans != 'Y':
        exit(1)
im.save(filename+'.png', 'PNG')
print('已寫入檔案：'+filename+'.png')
