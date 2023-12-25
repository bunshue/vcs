# -*- coding: utf-8 -*-

from PIL import Image
with Image.open("pic/2.jpg") as im:
    print('原圖片的尺寸大小:',im.size)
    w=300
    r = w/im.size[0]
    h = int(im.size[1]*r)
    new_im = im.resize((w, h))
    print('圖片經縮放後的尺寸大小:',new_im.size)
    new_im.save( "pic/2_resize.jpg" )
