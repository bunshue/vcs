"""

"""

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.lower().split("/")[::-1][0]  # 將檔名換成小寫 ( 避免 JPG 與 jpg 干擾 )
    png = name.replace("jpg", "png")  # 取出圖片檔名，將 jpg 換成 png
    im.save(f"./demo/png/{png}", "png")  # 轉換成 png 並存檔


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.split("/")[::-1][0]  # 取出檔名
    im.save(f"./demo/jpg/{name}", quality=65, subsampling=0)  # 設定參數並存檔


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

imgs = glob.glob("./oxxo/*.jpg")  # 取得 demo 資料夾內所有的圖片
for i in imgs:
    im = Image.open(i)  # 依序開啟每一張圖片
    size = im.size  # 取得圖片尺寸
    print(size)


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
img2 = img.resize((200, 200))  # 調整圖片尺寸為 200x200
img2.save("tmp_pic01.jpg")  # 調整後存檔到 resize 資料夾


print("------------------------------------------------------------")  # 60個

import glob
from PIL import Image

imgs = glob.glob("./oxxo/*.jpg")
for i in imgs:
    im = Image.open(i)
    size = im.size
    name = i.split("/")[::-1][0]  # 取得圖片的名稱
    im2 = im.resize((200, 200))  # 調整圖片尺寸為 200x200
    im2.save(f"./oxxo/resize/{name}")  # 調整後存檔到 resize 資料夾


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.png")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(factor)  # 調整亮度，factor 為一個浮點數值
# 調整後的數值 = 原始數值 x factor


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(1.5)  # 提高亮度
output.save("tmp_oxxostudio_b15.jpg")  # 存檔

output = brightness.enhance(0.5)  # 降低亮度
output.save("tmp_oxxostudio_b05.jpg")  # 存檔


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("./oxxostudio.jpg")  # 開啟圖片
img_crop = img.crop((0, 0, 200, 100))  # 裁切圖片
img_crop.save("./tmp_pic05.jpg")  # 存檔
# img_crop.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("./oxxostudio.jpg")
img_r1 = img.rotate(30)  # 旋轉 30 度
img_r2 = img.rotate(30, expand=1)  # 旋轉 30 度，expand 設定 1
img_r1.save("./tmp_pic06.jpg")
img_r2.save("./test2.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
bg.save("oxxostudio.jpg")
# bg.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片
bg.save("oxxostudio.png")


print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")  # 開啟圖片
    img = img.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(img, (x * 300, y * 400))  # 貼上圖片

bg.save("oxxostudio.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageOps

bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    img = Image.open(f"d{i}.jpg")
    img = img.resize((300, 400))
    img = ImageOps.expand(img, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(img, (x * 300, y * 400))

bg.save("oxxostudio.jpg")

print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 開啟風景圖
icon = Image.open("./oxxostudio-icon.png")  # 開啟浮水印 icon
img.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon
img.save("./ok.jpg")  # 存檔為 ok.jpg
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size  # 取得風景圖尺寸
icon_w, icon_h = icon.size  # 取得 icon 尺寸
x = int((img_w - icon_w) / 2)  # 計算置中時 icon 左上角的 x 座標
y = int((img_h - icon_h) / 2)  # 計算置中時 icon 左上角的 y 座標

img.paste(icon, (x, y), icon)  # 設定 icon 左上角座標
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個


import glob
from PIL import Image

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片
icon = Image.open("./oxxostudio-icon.png")
for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    img.paste(icon, (0, 0), icon)  # 加入浮水印
    img.save(f"./demo/watermark/{name}")  # 以原本的名稱存檔


print("------------------------------------------------------------")  # 60個


from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 準備合成浮水印的圖
img2 = Image.open("./watermark-photo.jpg")  # 底圖
icon = Image.open("./oxxostudio-icon.png")

img_w, img_h = img.size
icon_w, icon_h = icon.size
x = int((img_w - icon_w) / 2)
y = int((img_h - icon_h) / 2)
img.paste(icon, (x, y), icon)  # 合成浮水印
img.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img2.paste(img, (0, 0), img)  # 合成底圖
img2.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")  # 開啟圖片
font = ImageFont.truetype("Teko-Regular.ttf", 100)  # 設定字型
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)  # 將文字畫入圖片
img.save("./ok.jpg")  # 儲存圖片
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")
w, h = img.size  # 取得圖片尺寸
font = ImageFont.truetype("Teko-Regular.ttf", 100)
draw = ImageDraw.Draw(img)
draw.text(
    (0, h - 100), "OXXO.STUDIO", fill=(255, 255, 255), font=font
)  # 使用 h-100 定位到下方
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")
font = ImageFont.truetype("Teko-Regular.ttf", 150)
# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
img.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖
img.save("./ok.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

# import os
img = Image.open("./photo.jpg")
w, h = img.size

font = ImageFont.truetype("Teko-Regular.ttf", 150)
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

img2 = Image.open("./photo.jpg")  # 再次開啟原本的圖為 img2
img2.paste(text, (50, 0), text)  # 將文字貼上 img2
img2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img.paste(img2, (0, 0), img2)  # 將 img2 貼上 img
img.save("./ok.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

imgs = glob.glob("./demo/*.jpg")  # 讀取 demo 資料夾裡所有的圖片

for i in imgs:
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    img = Image.open(i)  # 開啟圖片
    w, h = img.size
    font = ImageFont.truetype("Teko-Regular.ttf", 100)
    text = Image.new(mode="RGBA", size=(400, 100), color=(0, 0, 0, 0))
    draw = ImageDraw.Draw(text)
    draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)
    text = text.rotate(30, expand=1)
    img2 = Image.open(i)
    img2.paste(text, (50, 0), text)
    img2.convert("RGBA")
    img2.putalpha(150)
    img.paste(img2, (0, 0), img2)
    img.save(f"./test/{name}")


print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
w, h = img.size  # 讀取圖片長寬
level = 50  # 設定縮小程度
img2 = img.resize((int(w / level), int(h / level)))  # 縮小圖片
img2 = img2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小
img2.save("tmp_pic01.jpg")  # 存檔

print("------------------------------------------------------------")  # 60個

from PIL import Image

img = Image.open("oxxostudio.jpg")
w, h = img.size
level = 20
img2 = img.resize((int(w / level), int(h / level)))
img2 = img2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = img2.crop((x1, y1, x2, y2))  # 裁切區域
img.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域
img.save("tmp_pic02.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.BLUR)  # 套用基本模糊化
output.save("tmp_output.jpg")
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.BoxBlur(5))  # 套用 BoxBlur，設定模糊半徑為 5
output.save("tmp_output.jpg")


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.GaussianBlur(5))  # 套用 GaussianBlur，設定模糊半徑為 5
output.save("tmp_output.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=-100, threshold=3)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.SHARPEN)  # 套用圖片銳利化
output.save("tmp_output.jpg")  # 存檔
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
for i in range(3):
    img = img.filter(ImageFilter.SHARPEN)
img.save("tmp_output.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image
import pytesseract

img = Image.open("english.jpg")
text = pytesseract.image_to_string(img, lang="eng")
print(text)

print("------------------------------------------------------------")  # 60個

from PIL import Image
import pytesseract

img = Image.open("chinese.jpg")
text = pytesseract.image_to_string(img, lang="chi_tra")
print(text)


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

