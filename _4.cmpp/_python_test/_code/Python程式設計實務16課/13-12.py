# _*_ coding: utf-8 _*_
# 程式 13-12 (Python 3 Version)
import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

text_msg = '此為測試用影像'
im = Image.open('sample_s.jpg')
im_w, im_h = im.size

font = ImageFont.truetype('font/wt014.ttf', 80)
dw = ImageDraw.Draw(im)
fn_w, fn_h = dw.textsize(unicode(text_msg, 'utf-8'), font=font)
x = im_w/2-fn_w/2
y = im_h/2-fn_h/2
dw.text((x+5, y+5), unicode(text_msg, 'utf-8'), font=font, fill=(25,25,25))
dw.text((x, y), unicode(text_msg, 'utf-8'), font=font, fill=(128,255,255))
im.show()