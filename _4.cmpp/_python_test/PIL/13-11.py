import sys, os, glob
from PIL import Image, ImageDraw, ImageFont

text_msg = 'Hello, world!'
im = Image.open('data\sample_s.jpg')
im_w, im_h = im.size

font = ImageFont.truetype('data/ubuntu.ttf', 80)
dw = ImageDraw.Draw(im)
fn_w, fn_h = dw.textsize(text_msg, font=font)

x = im_w/2-fn_w/2
y = im_h/2-fn_h/2
dw.text((x+5, y+5), text_msg, font=font, fill=(25,25,25))
dw.text((x, y), text_msg, font=font, fill=(128,255,255))
im.show()
