import os
import sys
import time
import random

from PIL import Image

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("------------------------------------------------------------")  # 60個

"""

image = Image.open(filename)
print(image.format, image.size, image.mode)

#image.show()

print("------------------------------------------------------------")  # 60個

print("剪裁圖像")

image = Image.open(filename)
rect = 80, 20, 310, 360
image.crop(rect).show()

print('------------------------------------------------------------')	#60個

print("生成縮略圖")

image = Image.open(filename)
size = 128, 128
image.thumbnail(size)
image.show()
"""
print("------------------------------------------------------------")  # 60個

print("縮放和黏貼圖像")

filename2 = "C:/_git/vcs/_1.data/______test_files1/bear.jpg"

image1 = Image.open(filename2)
image2 = Image.open(filename)
rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

image1.show()

"""
print("旋轉和翻轉")

image = Image.open(filename)
image.rotate(180).show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()

print('------------------------------------------------------------')	#60個
"""

print("操作像素")

image = Image.open(filename)
for x in range(100, 200):
    for y in range(250, 350):
        image.putpixel((x, y), (128, 128, 128))
image.show()

sys.exit()

print("------------------------------------------------------------")  # 60個

print("濾鏡效果")

from PIL import Image, ImageFilter

image = Image.open(filename)
image.filter(ImageFilter.CONTOUR).show()

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
