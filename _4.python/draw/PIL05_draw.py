"""

PIL 畫圖


"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf"  # 無中文
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"  # 有中文

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print("量測字串的大小")
mesg = "傷心橋下春波綠，曾是驚鴻照影來。"

filename = "C:/_git/vcs/_4.python/_data/elephant.jpg"

image = Image.open(filename)  # PIL讀取本機圖片, RGB模式
dw = ImageDraw.Draw(image)

font_size = 30
font = ImageFont.truetype(font_filename, font_size)
xx, yy, text_width, text_height = dw.textbbox(
    (0, 0), mesg, font=font, spacing=0, align="left"
)
print("量測結果 :", xx, yy, text_width, text_height)
print("字寬 :", text_width)
print("字高 :", text_height)

print("取得文字長")
length = dw.textlength(mesg, font=font)
print("L =", length)

xx, yy, width, height = font.getbbox(mesg)
print("取得 W = " + str(width) + ", H = " + str(height))

print("draw01------------------------------------------------------------")  # 60個

# 開啟圖片, 在圖片上作畫
# 檔案 => PIL影像
image = Image.open(filename)  # PIL讀取本機圖片, RGB模式
w, h = image.size
print("W = " + str(w) + ", H = " + str(h))

# 新建空白影像, 在影像上作畫
W, H = 640, 480
image = Image.new("RGBA", (W, H), "Yellow")  # 指定背景顏色
image = Image.new("RGB", (W, H), "#00FF00")  # 指定背景顏色
image = Image.new("RGB", (W, H))  # 無背景顏色, 黑色
image = Image.new("RGBA", (W, H), (0, 0, 0, 0))  # 指定背景顏色
image = Image.new("RGB", (W, H), "lightgray")  # 指定背景顏色

# 建立繪圖物件
dw = ImageDraw.Draw(image)

# 畫點
dw.point([(100, 100), (100, 101), (100, 102)], fill="red")

# 畫直線
x1, y1 = 20, 20
x2, y2 = 150, 20
dw.line((x1, y1, x2, y2), fill=(255, 0, 0), width=3)

x1, y1 = 20, 50
x2, y2 = 150, 50
dw.line((x1, y1, x2, y2), fill="lime", width=4)

# 畫直線連線
dw.line([(100, 0), (50, 80), (150, 80), (100, 0)], fill="blue")


# 畫矩形
w, h = 150, 100
x_st, y_st = 10, 100  # 左上
x_sp, y_sp = x_st + w, y_st + h  # 右下
# 空心矩形
dw.rectangle((x_st, y_st, x_sp, y_sp), fill=None, outline=(255, 0, 0), width=10)
# 實心矩形
x_st, y_st = x_st + 25, y_st + 25  # 左上
w, h = w - 50, h - 50
x_sp, y_sp = x_st + w, y_st + h  # 右下
dw.rectangle((x_st, y_st, x_sp, y_sp), fill="Red")
# dw.rectangle((x_st, y_st, x_sp, y_sp), fill="yellow", outline="black")
# dw.rectangle((x_st, y_st, x_sp, y_sp), outline='Black')


# 畫圓 橢圓
x_st, y_st = 10, 210  # 左上
x_sp, y_sp = x_st + 150, y_st + 100  # 右下
# 空心
dw.ellipse((x_st, y_st, x_sp, y_sp), outline=(0, 255, 0), width=5)
dw.ellipse((x_st + 10, y_st - 10, x_sp - 20, y_sp - 20), outline="gold", width=5)

# 實心
x_st, y_st, w, h = 10, 300, 100, 50
x_sp, y_sp = x_st + w, y_st + h
dw.ellipse((x_st, y_st, x_sp, y_sp), fill="red")
# dw.ellipse((x_st, y_st, x_sp, y_sp), fill="purple", outline="green")
# dw.ellipse([(x_st, y_st), (x_sp, y_sp)], fill = (255, 255, 0, 255))


x_st, y_st, w, h = 200, 10 + 50, 100, 50
x_sp, y_sp = x_st + w, y_st + h


# 畫多邊形

dx, dy = 50, 100
x1, y1 = 200, 280
x2, y2 = x1 - dx, y1 + dy
x3, y3 = x1 + dx, y1 + dy
x4, y4 = x1, y1 + dy + dy

# dw.polygon([(x1, y1), (x2, y2), (x3, y3)], fill="brown", outline="red")
dw.polygon([(x1, y1), (x2, y2), (x3, y3), (x4, y4)], fill="Aqua")  # 鼻子


dy = 40
x_st, y_st = 300, 40

# 使用古老英文字型
font_size = 30
font = ImageFont.truetype("OLDENGL.TTF", font_size)
font = ImageFont.truetype("C:\Windows\Fonts\OLDENGL.TTF", font_size)
dw.text((x_st, y_st), "Welcome 1111", fill="Blue", font=font)  # 藍字

font = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", font_size)
y_st += dy
dw.text((x_st, y_st), "Welcome 2222", font=font, fill=(0, 255, 255, 255))

font = ImageFont.truetype("C:/Windows/fonts/Tahoma.ttf", font_size)
y_st += dy
dw.text((x_st, y_st), "Welcome 3333", font=font, fill=(255, 0, 255, 255))


# msch
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
font = ImageFont.truetype(font_filename, font_size)
y_st += dy
dw.text((x_st + 5, y_st + 5), "歡迎來到美國111 msch", font=font, fill=(25, 25, 25))  # 畫陰影
dw.text((x_st, y_st), "歡迎來到美國111 msch", font=font, fill=(128, 255, 255))  # 畫文字

# 使用M$的新細明體中文字型
font_filename = "C:/Windows/Fonts/mingliu.ttc"
font = ImageFont.truetype(font_filename, font_size)
y_st += dy
dw.text((x_st, y_st), "歡迎來到美國222 mingliu", fill="blue", font=font)


plt.imshow(image)
plt.show()


# another

W, H = 640, 480
image = Image.new("RGB", (W, H), "lightgray")  # 指定背景顏色

# 建立繪圖物件
dw = ImageDraw.Draw(image)

x_st, y_st = 400, 20
# 繪製點
for x in range(x_st, x_st + 200, 4):
    for y in range(y_st, y_st + 100, 4):
        dw.point([(x, y)], fill="Green")

# 繪製點
x_st, y_st = 400, 160
for i in range(x_st, x_st + 200, 10):
    for j in range(y_st, y_st + 100, 10):
        dw.point([(i, j)], fill="red")

# 繪製線條, 繪外框線
dw.line([(0, 0), (299, 0), (299, 299), (0, 299), (0, 0)], fill="Black")

# 繪製右上角美工線
for x in range(150, 300, 10):
    dw.line([(x, 0), (300, x - 150)], fill="Blue")

# 繪製左下角美工線
for y in range(150, 300, 10):
    dw.line([(0, y), (y - 150, 300)], fill="Blue")

# 繪直線
for i in range(0, 640, 10):
    dw.line([(i, 480), (320, 320)], width=2, fill="blue")

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

""" TBD
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
im = Image.open(filename)
im_w, im_h = im.size

plt.imshow(im)
plt.show()

W = im_w
H = im_h


#im是原圖
#im0是要貼上的浮水印

im0 = Image.new('RGBA', (W, H))
dw = ImageDraw.Draw(im0)

#寫字
mesg = "牡丹亭"

dw.text((0,0), mesg, (255,0,0), font)

plt.imshow(im0)
plt.show()

im = Image.new('RGBA', (W, H), (255,0,255,0))
dw = ImageDraw.Draw(im)

x=3
y=3

fill = (255,0,0,100) # R G B A
dw.text((0, 0), mesg, font=font, fill=fill)

#將im0貼到im上
im.paste(im0, (x, y), im)

plt.imshow(im)

plt.show()

"""

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
dw = ImageDraw.Draw(text)
dw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
image.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)
w, h = image.size

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
dw = ImageDraw.Draw(text)
dw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

# 檔案 => PIL影像
image2 = Image.open(filename)  # 再次開啟原本的圖為 image2
image2.paste(text, (50, 0), text)  # 將文字貼上 image2
image2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
image2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
image.paste(image2, (0, 0), image2)  # 將 image2 貼上 image

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"

font_size = 30
font = ImageFont.truetype(font_filename, font_size)

dw = ImageDraw.Draw(image)  # 準備在圖片上繪圖
# 將文字畫入圖片
dw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
dw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)

print("------------------------------------------------------------")  # 60個

newImage = Image.new("RGBA", (300, 300), "Yellow")  # 建立300*300黃色底的影像
dw = ImageDraw.Draw(newImage)

# 繪製點
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        dw.point([(x, y)], fill="Green")

# 繪製線條, 繪外框線
dw.line([(0, 0), (299, 0), (299, 299), (0, 299), (0, 0)], fill="Black")
# 繪製右上角美工線
for x in range(150, 300, 10):
    dw.line([(x, 0), (300, x - 150)], fill="Blue")
# 繪製左下角美工線
for y in range(150, 300, 10):
    dw.line([(0, y), (y - 150, 300)], fill="Blue")

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

"""
def generate_product_image(product_image_path, background_image_path, promo_text):
    # 加載產品和背景影像
    product_image = Image.open(product_image_path).resize((200, 200))
    background_image = Image.open(background_image_path)
    # 在背景影像上放置產品影像
    background_image.paste(product_image, (50, 50), product_image)
    # 在影像上添加促銷文字
    dw = ImageDraw.Draw(background_image)
    font = ImageFont.truetype("arial.ttf", size=45)
    dw.text((50, 260), promo_text, font=font, fill="white")
    # 保存或返回影像
    background_image.save('output_promo_image.jpg')

generate_product_image('product.png', 'background.jpg', '特價促銷!')
"""
print("------------------------------------------------------------")  # 60個

print("PIL_line")

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

# 讀取圖像到數組中
# 檔案 => PIL影像 => numpy陣列
image = np.array(Image.open(filename))

plt.figure()
plt.imshow(image)

x = [100, 100, 200, 200]
y = [200, 400, 200, 400]
# 使用紅色星狀標記繪制點
plt.plot(x, y, "r*")

# 繪制連接兩個點的線（默認為藍色）
plt.plot(x[:2], y[:2])

plt.title("畫圖")

# show()命令首先打開圖形用戶界面（GUI），然後新建一個窗口，該圖形用戶界面會循環阻斷腳本，然後暫停，
# 直到最後一個圖像窗口關閉。每個腳本里，只能調用一次show()命令，通常相似腳本的結尾調用。
plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
