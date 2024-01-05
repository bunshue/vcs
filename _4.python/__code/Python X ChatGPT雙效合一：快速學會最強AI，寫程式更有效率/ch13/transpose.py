# -*- coding: utf-8 -*-

from PIL import Image,ImageEnhance
with Image.open("pic/8.jpg") as im:
    new_im = im.transpose(Image.FLIP_LEFT_RIGHT)
    new_im.save( "pic/8_1.jpg")
    new_im = im.transpose(Image.FLIP_TOP_BOTTOM)
    new_im.save( "pic/8_2.jpg")
    new_im = im.transpose(Image.ROTATE_90)
    new_im.save( "pic/8_3.jpg")
    new_im = im.transpose(Image.ROTATE_180)
    new_im.save( "pic/8_4.jpg")
    new_im = im.transpose(Image.ROTATE_270)
    new_im.save( "pic/8_5.jpg")
    new_im = im.transpose(Image.TRANSPOSE)
    new_im.save( "pic/8_6.jpg")
    new_im = im.transpose(Image.TRANSVERSE)
    new_im.save( "pic/8_7.jpg")
