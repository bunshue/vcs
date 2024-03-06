"""
PIL 基本使用

建立影像
PIL 無圖處理

"""

import os
import sys
import time
import random

import matplotlib.pyplot as plt

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

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

image = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
image = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片

print('建立影像 RGB 300 X 100')
W, H = 300, 100
color = "aqua"
image = Image.new('RGB', (W, H), color)
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('建立影像(透明) RGBA 300 X 100')
W, H = 300, 100
image = Image.new('RGBA', (W, H))
plt.imshow(image)
plt.show()

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (300, 180))     # 建立完全透明影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new('RGBA', (300, 100), "Yellow")
print(image.getpixel((150, 50)))      # 列印中心點的色彩

print("------------------------------------------------------------")  # 60個

image = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        image.putpixel((x, y), (0, 255, 255, 255))   # 填青色

for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        image.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))

print('------------------------------------------------------------')	#60個

print('建立影像 RGBA, 在上面畫圖')
W, H = 300, 100
color = "Yellow"
image = Image.new('RGBA', (W, H), color)

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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個






print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




"""
共用抽出

#存圖
#image.save("xxxx.jpg")
#image.save("xxxx.png")



#顯示
#image.show()



"""
