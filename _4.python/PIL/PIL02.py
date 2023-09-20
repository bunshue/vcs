'''

PIL 無圖處理


'''




'''
共用抽出

#存圖
#image.save("xxxx.png")

#顯示
#image.show()

'''


import os
import sys
import time
import random

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

import matplotlib.pyplot as plt

print('------------------------------------------------------------')	#60個

print('PIL 無圖處理')

print('------------------------------------------------------------')	#60個

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0, 0, 255)"))
print(ImageColor.getrgb("rgb(0%, 0%, 100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("red"))

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("#0000ff", "RGB"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("#0000ff", "RGBA"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
print(ImageColor.getcolor("Blue", "RGBA"))

print('------------------------------------------------------------')	#60個

W, H = 300, 180
image = Image.new('RGB', (W, H), 'aqua')  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

W, H = 300, 180
image = Image.new('RGBA', (W, H)) # 建立完全透明影像
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

W, H = 300, 100
image = Image.new('RGBA', (W, H), "Yellow")

print('列印中心點的色彩')
print(image.getpixel((150, 50)))

for x in range(50, 251):                            # x軸區間在50-250
    for y in range(20, 51):                        # y軸區間在20-50
        image.putpixel((x, y), (255, 0, 0, 255))   # 填紅色

for x in range(50, 251):                            # x軸區間在50-250            
    for y in range(51, 81):                       # y軸區間在51-80
        image.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA")) # 填藍色

plt.imshow(image)
plt.show()



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


