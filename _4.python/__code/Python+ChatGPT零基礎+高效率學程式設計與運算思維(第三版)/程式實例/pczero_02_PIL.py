import os
import sys
import time
import random

print('------------------------------------------------------------')	#60個

# ex17_2.ipynb
from PIL import Image

hungPic = Image.open("hung.jpg")        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 600
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))
newImage.save("fig17_2.jpg")


print('------------------------------------------------------------')	#60個


# ex17_4.ipynb
from PIL import Image
from PIL import ImageFilter
rushMore = Image.open("palace.png")       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("fig17_4_BLUR.png")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("fig17_4_CONTOUR.png")
filterPict = rushMore.filter(ImageFilter.DETAIL)
filterPict.save("fig17_4_DETAIL.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE)
filterPict.save("fig17_4_EDGE_ENHANCE.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE_MORE)
filterPict.save("fig17_4_EDGE_ENHANCE_MORE.png")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("fig17_4_EMBOSS.png")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("fig17_4_FIND_EDGES.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH)
filterPict.save("fig17_4_SMOOTH.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH_MORE)
filterPict.save("fig17_4_SMOOTH_MORE.png")
filterPict = rushMore.filter(ImageFilter.SHARPEN)
filterPict.save("fig17_4_SHARPEN.png")


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

# ex17_6.py
from PIL import Image, ImageDraw, ImageFont

hungPic = Image.open("hung.jpg")        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 700
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(newImage)
name = "洪錦魁"
fontInfo = ImageFont.truetype('NotoSansTC-Bold.otf', 60)
drawObj.text((140,600), name, fill='Blue', font=fontInfo)


newImage.save("fig17_6.jpg")

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個





