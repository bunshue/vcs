# -*- coding: utf-8 -*-

from PIL import Image
with Image.open("pic/4.jpg") as im:
    print('原圖片的尺寸大小:',im.size)
    x = 100
    y = 100
    x1 = 1000
    y1 = 1400
    new_im = im.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', new_im.size)
    new_im.save( "pic/4_crop.jpg")
