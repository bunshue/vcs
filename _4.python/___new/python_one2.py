"""
一本精通 - Python 範例應用大全
"""

import os
import sys
import time
import random

# 有順序

print("------------------------------------------------------------")  # 60個
print("Python 影像處理")
print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code001.py

# Copyright © https://steam.oxxostudio.tw

import glob

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除
jpg = glob.glob("./demo/*.[jJ][pP][gG]")  # 使用 [jJ][pP][gG] 萬用字元，抓出副檔名不論大小寫的 jpg 檔案
print(images)
"""
['./demo/pic-001.jpg', './demo/pic-002.jpg', './demo/pic-003.jpg',
'./demo/pic-004.jpg', './demo/pic-005.jpg', './demo/pic-006.jpg',
'./demo/pic-007.jpg', './demo/pic-008.jpg', './demo/pic-009.jpg',
'./demo/pic-010.jpg']
"""


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code002.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.lower().split("/")[::-1][0]  # 將檔名換成小寫 ( 避免 JPG 與 jpg 干擾 )
    png = name.replace("jpg", "png")  # 取出圖片檔名，將 jpg 換成 png
    im.save(f"./demo/png/{png}", "png")  # 轉換成 png 並存檔


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code003.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image

jpg = glob.glob("./demo/*.[jJ][pP][gG]")
print(jpg)
for i in jpg:
    print(i)
    im = Image.open(i)  # 開啟圖片檔案
    name = i.split("/")[::-1][0]  # 取出檔名
    im.save(f"./demo/jpg/{name}", quality=65, subsampling=0)  # 設定參數並存檔


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code004.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
print(img.size)  # (1280,720) 印出長寬尺寸

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code005.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import glob
from PIL import Image

imgs = glob.glob("./oxxo/*.jpg")  # 取得 demo 資料夾內所有的圖片
for i in imgs:
    im = Image.open(i)  # 依序開啟每一張圖片
    size = im.size  # 取得圖片尺寸
    print(size)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code006.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
img2 = img.resize((200, 200))  # 調整圖片尺寸為 200x200
img2.save("test.jpg")  # 調整後存檔到 resize 資料夾


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code007.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code008.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.png")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(factor)  # 調整亮度，factor 為一個浮點數值
# 調整後的數值 = 原始數值 x factor


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code009.py

# Copyright © https://steam.oxxostudio.tw

from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")  # 開啟影像
brightness = ImageEnhance.Brightness(img)  # 設定 img 要加強亮度
output = brightness.enhance(1.5)  # 提高亮度
output.save("oxxostudio_b15.jpg")  # 存檔

output = brightness.enhance(0.5)  # 降低亮度
output.save("oxxostudio_b05.jpg")  # 存檔


print("------------------------------------------------------------")  # 60個

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("./oxxostudio.jpg")  # 開啟圖片
img_crop = img.crop((0, 0, 200, 100))  # 裁切圖片
img_crop.save("./test.jpg")  # 存檔
# img_crop.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code012.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("./oxxostudio.jpg")
img_r1 = img.rotate(30)  # 旋轉 30 度
img_r2 = img.rotate(30, expand=1)  # 旋轉 30 度，expand 設定 1
img_r1.save("./test1.jpg")
img_r2.save("./test2.jpg")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code013.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
bg.save("oxxostudio.jpg")
# bg.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code014.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片
bg.save("oxxostudio.png")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code015.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code016.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code017.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("./watermark-photo.jpg")  # 開啟風景圖
icon = Image.open("./oxxostudio-icon.png")  # 開啟浮水印 icon
img.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon
img.save("./ok.jpg")  # 存檔為 ok.jpg
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code018.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code019.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code020.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code021.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFont, ImageDraw

img = Image.open("./photo.jpg")  # 開啟圖片
font = ImageFont.truetype("Teko-Regular.ttf", 100)  # 設定字型
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
draw.text((0, 0), "OXXO.STUDIO", fill=(255, 255, 255), font=font)  # 將文字畫入圖片
img.save("./ok.jpg")  # 儲存圖片
# img.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code022.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code023.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code024.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code025.py

# Copyright © https://steam.oxxostudio.tw

from PIL import Image, ImageFont, ImageDraw

# import os
# os.chdir('/content/drive/MyDrive/Colab Notebooks')  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除
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

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code026.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image

img = Image.open("oxxostudio.jpg")  # 開啟圖片
w, h = img.size  # 讀取圖片長寬
level = 50  # 設定縮小程度
img2 = img.resize((int(w / level), int(h / level)))  # 縮小圖片
img2 = img2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小
img2.save("test.jpg")  # 存檔


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code027.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

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
img.save("test.jpg")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code028.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.BLUR)  # 套用基本模糊化
output.save("output.jpg")
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code029.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.BoxBlur(5))  # 套用 BoxBlur，設定模糊半徑為 5
output.save("output.jpg")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code030.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(ImageFilter.GaussianBlur(5))  # 套用 GaussianBlur，設定模糊半徑為 5
output.save("output.jpg")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code031.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=-100, threshold=3)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code032.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")  # 開啟圖片
output = img.filter(ImageFilter.SHARPEN)  # 套用圖片銳利化
output.save("output.jpg")  # 存檔
# output.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code033.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
for i in range(3):
    img = img.filter(ImageFilter.SHARPEN)
img.save("output.jpg")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code034.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image, ImageFilter

img = Image.open("oxxostudio.jpg")
output = img.filter(
    ImageFilter.UnsharpMask(radius=5, percent=100, threshold=10)
)  # 套用 UnsharpMask
output.show()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code035.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")  # 使用 PIL Image 開啟圖片
exif = piexif.load(img.info["exif"])  # 使用 piexif 讀取圖片 Exif 資訊
print(exif)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code036.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])
# 建立字典對照表
info = {
    "0th": [271, 272, 282, 283, 305, 306, 316],
    "Exif": [
        33434,
        33437,
        34855,
        36867,
        36868,
        36880,
        36881,
        36882,
        40962,
        40963,
        42035,
        42036,
    ],
    "1st": [282, 283],
    "GPS": [2, 4, 5, 17, 24, 31],
}
# 根據對照表，印出照片 exif 裡的資訊 ( 有就印出，沒有就略過 )
for i in info:
    for j in info[i]:
        if j in exif[i]:
            print(j, ":", exif[i][j])


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code037.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import piexif

img = Image.open("./oxxostudio.jpg")
exif = piexif.load(img.info["exif"])

exif["0th"][305] = b"OXXO.STUDIO"  # 修改編輯軟體
exif["0th"][306] = b"2020:01:01 00:00:00"  # 修改編輯時間
exif["Exif"][36867] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif["Exif"][36868] = b"2020:01:01 00:00:00"  # 加入檔案建立時間
exif_new = piexif.dump(exif)  # 更新 Exif
img.save("./iphone-edit.jpg", exif=exif_new)  # 另存新檔並加入 Exif


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code038.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import pytesseract

img = Image.open("english.jpg")
text = pytesseract.image_to_string(img, lang="eng")
print(text)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch13\code039.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

from PIL import Image
import pytesseract

img = Image.open("chinese.jpg")
text = pytesseract.image_to_string(img, lang="chi_tra")
print(text)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("Python 聲音處理")
print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code001.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
print(song)  # <pydub.audio_segment.AudioSegment object at 0x7faaa545a7f0>


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code002.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")  # 輸出為 wav
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code003.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("output.wav", bitrate="96k")  # 輸出壓縮比率為 96k 的 mp3 檔案
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code004.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
duration = song.duration_seconds  # 讀取長度
channels = song.channels  # 讀取聲道數量
print(channels, duration)  # 印出資訊


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code005.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song[1500:5500].export("output.mp3")  # 取出 1500 毫秒～5500 毫秒長度的聲音，輸出為 output.mp3
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code006.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment

song1 = AudioSegment.from_mp3("oxxo1.mp3")  # 讀取第一個 mp3 檔案
song2 = AudioSegment.from_mp3("oxxo2.mp3")  # 讀取第二個 mp3 檔案
output = song1 + song2  # 串接兩段聲音
output.export("output.mp3")  # 輸出為 output.mp3
print("ok")  # 輸出後印出 ok


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code007.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
output = song * 3  # 乘以 3，重複三次變成三倍長
output.export("output.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code008.py

# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3
output1 = song[:] + 10  # 將所有陣列中的資料增加 10 ( 變大聲 )
output2 = song[:] - 10  # 將所有陣列中的資料減少 10 ( 變小聲 )
output1.export("output1.mp3")  # 輸出聲音
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code009.py

# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.apply_gain(10)  # 將音量增加 10 ( 變大聲 )
output2 = song.apply_gain(-10)  # 將音量減少 10 ( 變小聲 )
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code010.py

# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.fade_in(3000)  # 開頭三秒 ( 3000ms ) 淡入
output2 = song.fade_out(3000)  # 結尾三秒 ( 3000ms ) 淡出
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code011.py

# Copyright © https://steam.oxxostudio.tw

from pydub import AudioSegment
import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用
song = AudioSegment.from_mp3("oxxostudio.mp3")

output1 = song.fade(to_gain=15, start=1000, duration=2000)
# 從 1 秒的位置開始，慢慢變大聲到增加 15，過程持續 2 秒

output2 = song.fade(to_gain=-30, end=3000, duration=2000)
# 從 1 秒的位置開始 ( 3000-2000 )，慢慢變小聲到減少 30，過程持續 2 秒

output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code012.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.overlay(song, loop=True)  # 混合說話聲音和背景音樂
output.export("output.mp3")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code013.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.reverse()  # 反轉說話聲音
output.export("output.mp3")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code014.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用

from pydub import AudioSegment

song = AudioSegment.from_mp3("test.mp3")  # 讀取聲音檔案


# 定義加速與減速的函式
def speed_change(sound, speed=1.0):
    rate = sound._spawn(
        sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)}
    )
    return rate.set_frame_rate(sound.frame_rate)


song_slow = speed_change(song, 0.75)  # 聲音減速
song_fast = speed_change(song, 2.0)  # 聲音加速

song_slow.export("song_slow.mp3")
song_fast.export("song_fast.mp3")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code015.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 開啟聲音檔案
output = song * 2  # 讓聲音檔案變成兩倍長
play(output)  # 播放聲音


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code016.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from IPython.display import Audio  # 載入 IPython.display 的 Audio模組

Audio("output.mp3")  # 播放聲音


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code017.py

# Copyright © https://steam.oxxostudio.tw

import pyaudio
import wave

chunk = 1024  # 記錄聲音的樣本區塊大小
sample_format = (
    pyaudio.paInt16
)  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2  # 聲道數量
fs = 44100  # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5  # 錄音秒數
filename = "oxxostudio.wav"  # 錄音檔名

p = pyaudio.PyAudio()  # 建立 pyaudio 物件

print("開始錄音...")

# 開啟錄音串流
stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []  # 建立聲音串列

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)  # 將聲音記錄到串列中

stream.stop_stream()  # 停止錄音
stream.close()  # 關閉串流
p.terminate()

print("錄音結束...")

wf = wave.open(filename, "wb")  # 開啟聲音記錄檔
wf.setnchannels(channels)  # 設定聲道
wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
wf.setframerate(fs)  # 設定取樣頻率
wf.writeframes(b"".join(frames))  # 存檔
wf.close()


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code018.py

# Copyright © https://steam.oxxostudio.tw

import pyaudio
import wave
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 5
filename = "oxxostudio.wav"

p = pyaudio.PyAudio()

print("開始錄音...")

stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("錄音結束...")

wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()

song = AudioSegment.from_mp3("song.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_wav("oxxostudio.wav")  # 讀取錄音 wav 檔案
output = voice.overlay(song, loop=True)  # 混合錄音和背景音樂
play(output)  # 播放聲音
output.export("output.mp3")  # 輸出為 mp3
print("ok")

print("------------------------------------------------------------")  # 60個

import numpy as np

samplerate = 44100  # 取樣頻率

def get_wave(freq, duration=0.5):
    amplitude = 4096  # 震幅 ( 音量大小 )
    t = np.linspace(
        0, duration, int(samplerate * duration)
    )  # 使用等差級數，在指定時間長度裡，根據取樣頻率建立區間
    wave = amplitude * np.sin(2 * np.pi * freq * t)  # 在每個區間裡放入指定頻率的波形
    return wave


def get_piano_notes():
    octave = ["C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B"]  # 建立音符英文字對照表
    base_freq = 261.63  # 預設為 C4 的頻率
    note_freqs = {
        octave[i]: base_freq * pow(2, (i / 12)) for i in range(len(octave))
    }  # 產生頻率和英文字的對照
    note_freqs[""] = 0.0  # 如果是空值則為 0 ( 無聲音 )
    return note_freqs


def get_song_data(music_notes):
    note_freqs = get_piano_notes()  # 取的英文與音符對照表
    song = [
        get_wave(note_freqs[note]) for note in music_notes.split("-")
    ]  # 根據音樂的音符，對應到對照表產生指定串列
    song = np.concatenate(song)  # 連接為新陣列
    return song


# 音樂的音符表
music_notes = "C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C"
data = get_song_data(music_notes)  # 轉換成頻率對照表
data = data * (16300 / np.max(data))  # 調整震幅 ( 音量大小 )

from scipy.io.wavfile import write

write("twinkle-twinkle.wav", samplerate, data.astype(np.int16))  # 寫入檔案


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch14\code023.py

# Copyright © https://steam.oxxostudio.tw

{
    A0: {frequency: "27.50", wavelength: "1254.55"},
    A1: {frequency: "55.00", wavelength: "627.27"},
    A2: {frequency: "110.00", wavelength: "313.64"},
    A3: {frequency: "220.00", wavelength: "156.82"},
    A4: {frequency: "440.00", wavelength: "78.41"},
    A5: {frequency: "880.00", wavelength: "39.20"},
    A6: {frequency: "1760.00", wavelength: "19.60"},
    A7: {frequency: "3520.00", wavelength: "9.80"},
    A8: {frequency: "7040.00", wavelength: "4.90"},
    B0: {frequency: "30.87", wavelength: "1117.67"},
    B1: {frequency: "61.74", wavelength: "558.84"},
    B2: {frequency: "123.47", wavelength: "279.42"},
    B3: {frequency: "246.94", wavelength: "139.71"},
    B4: {frequency: "493.88", wavelength: "69.85"},
    B5: {frequency: "987.77", wavelength: "34.93"},
    B6: {frequency: "1975.53", wavelength: "17.46"},
    B7: {frequency: "3951.07", wavelength: "8.73"},
    B8: {frequency: "7902.13", wavelength: "4.37"},
    C0: {frequency: "16.35", wavelength: "2109.89"},
    C1: {frequency: "32.70", wavelength: "1054.94"},
    C2: {frequency: "65.41", wavelength: "527.47"},
    C3: {frequency: "130.81", wavelength: "263.74"},
    C4: {frequency: "261.63", wavelength: "131.87"},
    C5: {frequency: "523.25", wavelength: "65.93"},
    C6: {frequency: "1046.50", wavelength: "32.97"},
    C7: {frequency: "2093.00", wavelength: "16.48"},
    C8: {frequency: "4186.01", wavelength: "8.24"},
    D0: {frequency: "18.35", wavelength: "1879.69"},
    D1: {frequency: "36.71", wavelength: "939.85"},
    D2: {frequency: "73.42", wavelength: "469.92"},
    D3: {frequency: "146.83", wavelength: "234.96"},
    D4: {frequency: "293.66", wavelength: "117.48"},
    D5: {frequency: "587.33", wavelength: "58.74"},
    D6: {frequency: "1174.66", wavelength: "29.37"},
    D7: {frequency: "2349.32", wavelength: "14.69"},
    D8: {frequency: "4698.63", wavelength: "7.34"},
    E0: {frequency: "20.60", wavelength: "1674.62"},
    E1: {frequency: "41.20", wavelength: "837.31"},
    E2: {frequency: "82.41", wavelength: "418.65"},
    E3: {frequency: "164.81", wavelength: "209.33"},
    E4: {frequency: "329.63", wavelength: "104.66"},
    E5: {frequency: "659.25", wavelength: "52.33"},
    E6: {frequency: "1318.51", wavelength: "26.17"},
    E7: {frequency: "2637.02", wavelength: "13.08"},
    E8: {frequency: "5274.04", wavelength: "6.54"},
    F0: {frequency: "21.83", wavelength: "1580.63"},
    F1: {frequency: "43.65", wavelength: "790.31"},
    F2: {frequency: "87.31", wavelength: "395.16"},
    F3: {frequency: "174.61", wavelength: "197.58"},
    F4: {frequency: "349.23", wavelength: "98.79"},
    F5: {frequency: "698.46", wavelength: "49.39"},
    F6: {frequency: "1396.91", wavelength: "24.70"},
    F7: {frequency: "2793.83", wavelength: "12.35"},
    F8: {frequency: "5587.65", wavelength: "6.17"},
    G0: {frequency: "24.50", wavelength: "1408.18"},
    G1: {frequency: "49.00", wavelength: "704.09"},
    G2: {frequency: "98.00", wavelength: "352.04"},
    G3: {frequency: "196.00", wavelength: "176.02"},
    G4: {frequency: "392.00", wavelength: "88.01"},
    G5: {frequency: "783.99", wavelength: "44.01"},
    G6: {frequency: "1567.98", wavelength: "22.00"},
    G7: {frequency: "3135.96", wavelength: "11.00"},
    G8: {frequency: "6271.93", wavelength: "5.50"},
    "A#0": {frequency: "29.14", wavelength: "1184.13"},
    "Bb0": {frequency: "29.14", wavelength: "1184.13"},
    "A#1": {frequency: "58.27", wavelength: "592.07"},
    "Bb1": {frequency: "58.27", wavelength: "592.07"},
    "A#2": {frequency: "116.54", wavelength: "296.03"},
    "Bb2": {frequency: "116.54", wavelength: "296.03"},
    "A#3": {frequency: "233.08", wavelength: "148.02"},
    "Bb3": {frequency: "233.08", wavelength: "148.02"},
    "A#4": {frequency: "466.16", wavelength: "74.01"},
    "Bb4": {frequency: "466.16", wavelength: "74.01"},
    "A#5": {frequency: "932.33", wavelength: "37.00"},
    "Bb5": {frequency: "932.33", wavelength: "37.00"},
    "A#6": {frequency: "1864.66", wavelength: "18.50"},
    "Bb6": {frequency: "1864.66", wavelength: "18.50"},
    "A#7": {frequency: "3729.31", wavelength: "9.25"},
    "Bb7": {frequency: "3729.31", wavelength: "9.25"},
    "A#8": {frequency: "7458.62", wavelength: "4.63"},
    "Bb8": {frequency: "7458.62", wavelength: "4.63"},
    "C#0": {frequency: "17.32", wavelength: "1991.47"},
    "Db0": {frequency: "17.32", wavelength: "1991.47"},
    "C#1": {frequency: "34.65", wavelength: "995.73"},
    "Db1": {frequency: "34.65", wavelength: "995.73"},
    "C#2": {frequency: "69.30", wavelength: "497.87"},
    "Db2": {frequency: "69.30", wavelength: "497.87"},
    "C#3": {frequency: "138.59", wavelength: "248.93"},
    "Db3": {frequency: "138.59", wavelength: "248.93"},
    "C#4": {frequency: "277.18", wavelength: "124.47"},
    "Db4": {frequency: "277.18", wavelength: "124.47"},
    "C#5": {frequency: "554.37", wavelength: "62.23"},
    "Db5": {frequency: "554.37", wavelength: "62.23"},
    "C#6": {frequency: "1108.73", wavelength: "31.12"},
    "Db6": {frequency: "1108.73", wavelength: "31.12"},
    "C#7": {frequency: "2217.46", wavelength: "15.56"},
    "Db7": {frequency: "2217.46", wavelength: "15.56"},
    "C#8": {frequency: "4434.92", wavelength: "7.78"},
    "Db8": {frequency: "4434.92", wavelength: "7.78"},
    "D#0": {frequency: "19.45", wavelength: "1774.20"},
    "Eb0": {frequency: "19.45", wavelength: "1774.20"},
    "D#1": {frequency: "38.89", wavelength: "887.10"},
    "Eb1": {frequency: "38.89", wavelength: "887.10"},
    "D#2": {frequency: "77.78", wavelength: "443.55"},
    "Eb2": {frequency: "77.78", wavelength: "443.55"},
    "D#3": {frequency: "155.56", wavelength: "221.77"},
    "Eb3": {frequency: "155.56", wavelength: "221.77"},
    "D#4": {frequency: "311.13", wavelength: "110.89"},
    "Eb4": {frequency: "311.13", wavelength: "110.89"},
    "D#5": {frequency: "622.25", wavelength: "55.44"},
    "Eb5": {frequency: "622.25", wavelength: "55.44"},
    "D#6": {frequency: "1244.51", wavelength: "27.72"},
    "Eb6": {frequency: "1244.51", wavelength: "27.72"},
    "D#7": {frequency: "2489.02", wavelength: "13.86"},
    "Eb7": {frequency: "2489.02", wavelength: "13.86"},
    "D#8": {frequency: "4978.03", wavelength: "6.93"},
    "Eb8": {frequency: "4978.03", wavelength: "6.93"},
    "F#0": {frequency: "23.12", wavelength: "1491.91"},
    "Gb0": {frequency: "23.12", wavelength: "1491.91"},
    "F#1": {frequency: "46.25", wavelength: "745.96"},
    "Gb1": {frequency: "46.25", wavelength: "745.96"},
    "F#2": {frequency: "92.50", wavelength: "372.98"},
    "Gb2": {frequency: "92.50", wavelength: "372.98"},
    "F#3": {frequency: "185.00", wavelength: "186.49"},
    "Gb3": {frequency: "185.00", wavelength: "186.49"},
    "F#4": {frequency: "369.99", wavelength: "93.24"},
    "Gb4": {frequency: "369.99", wavelength: "93.24"},
    "F#5": {frequency: "739.99", wavelength: "46.62"},
    "Gb5": {frequency: "739.99", wavelength: "46.62"},
    "F#6": {frequency: "1479.98", wavelength: "23.31"},
    "Gb6": {frequency: "1479.98", wavelength: "23.31"},
    "F#7": {frequency: "2959.96", wavelength: "11.66"},
    "Gb7": {frequency: "2959.96", wavelength: "11.66"},
    "F#8": {frequency: "5919.91", wavelength: "5.83"},
    "Gb8": {frequency: "5919.91", wavelength: "5.83"},
    "G#0": {frequency: "25.96", wavelength: "1329.14"},
    "Ab0": {frequency: "25.96", wavelength: "1329.14"},
    "G#1": {frequency: "51.91", wavelength: "664.57"},
    "Ab1": {frequency: "51.91", wavelength: "664.57"},
    "G#2": {frequency: "103.83", wavelength: "332.29"},
    "Ab2": {frequency: "103.83", wavelength: "332.29"},
    "G#3": {frequency: "207.65", wavelength: "166.14"},
    "Ab3": {frequency: "207.65", wavelength: "166.14"},
    "G#4": {frequency: "415.30", wavelength: "83.07"},
    "Ab4": {frequency: "415.30", wavelength: "83.07"},
    "G#5": {frequency: "830.61", wavelength: "41.54"},
    "Ab5": {frequency: "830.61", wavelength: "41.54"},
    "G#6": {frequency: "1661.22", wavelength: "20.77"},
    "Ab6": {frequency: "1661.22", wavelength: "20.77"},
    "G#7": {frequency: "3322.44", wavelength: "10.38"},
    "Ab7": {frequency: "3322.44", wavelength: "10.38"},
    "G#8": {frequency: "6644.88", wavelength: "5.19"},
    "Ab8": {frequency: "6644.88", wavelength: "5.19"},
}


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("Python 影片處理")
print("------------------------------------------------------------")  # 60個


# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code001.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]  # 要轉換的格式清單

# 使用 for 迴圈轉換成所有格式
for i in format_list:
    output = video.copy()
    output.write_videofile(
        f"output.{i}",
        temp_audiofile="temp-audio.m4a",
        remove_temp=True,
        codec="libx264",
        audio_codec="aac",
    )

print("ok")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code002.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

format_list = ["avi", "mov", "wmv", "flv", "asf", "mkv"]

for n in range(3):
    video = VideoFileClip(f"oxxo_{n}.mp4")  # 使用 for 迴圈讀取影片
    for i in format_list:
        output = video.copy()
        output.write_videofile(
            f"output_{n}.{i}",
            temp_audiofile="temp-audio.m4a",
            remove_temp=True,
            codec="libx264",
            audio_codec="aac",
        )

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code003.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

video = AudioSegment.from_file("oxxostudio.mp4")  # 讀取 mp4 檔案
output.export("video.mp3")  # 講讀取的聲音輸出為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code004.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from pydub import AudioSegment

video = AudioSegment.from_file("oxxostudio.mp4")
output = video[2000:10000]  # 剪輯聲音
output = output[:] + 10  # 放大聲音
output.export("output.mp3")
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code005.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
audio = video.audio  # 取出聲音
audio.write_audiofile("song.mp3")  # 輸出聲音為 mp3
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code006.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
audio = AudioFileClip("song.mp3")  # 讀取音樂

output = video2.set_audio(audio)  # 合併影片與聲音
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 注意要設定相關參數，不然轉出來的影片會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code007.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.subclip(12, 15)  # 剪輯影片 ( 單位秒 )
output.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code008.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")  # 開啟第一段影片
o2 = VideoFileClip("oxxo2.mp4")  # 開啟第二段影片
o3 = VideoFileClip("oxxo3.mp4")  # 開啟第三段影片
output = concatenate_videoclips([o1, o2, o3])  # 合併影片
output.write_videofile(
    "output123.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code009.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o1 = o1.resize((1280, 720))  # 改變尺寸
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3])
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code010.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

o1 = VideoFileClip("oxxo1.mp4")
o2 = VideoFileClip("oxxo2.mp4")
o3 = VideoFileClip("oxxo3.mp4")
output = concatenate_videoclips([o1, o2, o3], method="compose")  # 設定 method 為 compose
output.write_videofile(
    "output456.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code011.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v3 = VideoFileClip("oxxo3.mp4")  # 讀取影片
v4 = VideoFileClip("oxxo4.mp4")  # 讀取影片
v1 = v1.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v2 = v2.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v3 = v3.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
v4 = v4.resize((480, 360)).margin(10)  # 改變尺寸，增加邊界
output = clips_array([[v1, v2], [v3, v4]])  # 排列影片，v1 和 v2 一組，v3 和 v4 一組
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code012.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
# 輸出影片，注意後方需要加上參數，不然會沒有聲音
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code013.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

v1 = VideoFileClip("oxxo1.mp4")  # 讀取影片
v2 = VideoFileClip("oxxo2.mp4")  # 讀取影片
v1 = mask_color(v1, color=0, thr=10, s=0)  # 設定 v1 遮罩為半透明
# color=0 表示黑色，thr 和 s 是參數，這種設定為半透明
output = CompositeVideoClip([v2, v1])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code014.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
clip_1 = video.subclip(2, 5)  # 裁切出三秒影片
clip_2 = video.subclip(17, 21).set_start(2).crossfadein(1)  # 裁切出四秒影片，設定兩秒後再開始，淡入一秒
clip_3 = video.subclip(50, 53).set_start(5).crossfadein(1)  # 裁切出三秒影片，設定五秒後再開始，淡入一秒

output = CompositeVideoClip([clip_1, clip_2, clip_3])

output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code015.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.resize((480, 360))  # 改變尺寸
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code016.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.resize(width=480)  # 改變尺寸，設定寬度改變為 480
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code017.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = crop(video, x1=10, y1=10, width=50, height=50)  # 方法 1，指定左上 (x1, y1) 座標和寬高
output_2 = crop(
    video, x1=10, y1=10, x2=50, y2=50
)  # 方法 2，指定左上 (x1, y1) 座標和右下 ( x2, y2 )座標
output_3 = crop(video, x1=10, width=100)  # 方法 3，指定左上 x1 座標和寬度，就會自動採用 y1=0 和影片高度

output_1.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code018.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.rotate(90)  # 影片旋轉 90 度
output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code019.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_x = mirror_x(video)  # 左右翻轉
output_y = mirror_y(video)  # 垂直翻轉

output_x.write_videofile(
    "output_x.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_y.write_videofile(
    "output_y.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code020.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output_1 = speedx(video, factor=2)  # 2 倍速
output_2 = speedx(video, factor=0.5)  # 0.5 倍速
output_3 = speedx(video, final_duration=2)  # 將影片變成 2 秒長

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code021.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output_1 = time_mirror(video)  # 反轉影片
output_2 = time_symmetrize(video)  # 播到底後反轉影片回頭

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code022.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = lum_contrast(video, lum=-50, contrast=0)  # 亮度減少 50
output_2 = lum_contrast(video, lum=150, contrast=0)  # 亮度增加 150
output_3 = lum_contrast(video, lum=0, contrast=-0.5)  # 對比減少 0.5
output_4 = lum_contrast(video, lum=0, contrast=2)  # 對比增加 2

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code023.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from moviepy.video.fx.all import *

video = VideoFileClip("oxxostudio.mp4")
output_1 = colorx(video, 1.5)  # 調整顏色
output_2 = gamma_corr(video, 1)  # 調整 gamma 值
output_3 = blackwhite(video)  # 黑白影片
output_4 = invert_colors(video)  # 負片效果

output_1.write_videofile(
    "output_1.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_2.write_videofile(
    "output_2.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_3.write_videofile(
    "output_3.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
output_4.write_videofile(
    "output_4.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code024.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")  # 讀取影片
output = video.resize((360, 180))  # 壓縮影片
output = output.subclip(13, 15)  # 取出 13～15 秒的片段
output.write_gif("output.gif")  # 將這個片段轉換成 gif
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code025.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
output = video.resize((360, 180))
output = output.subclip(13, 15)
output.write_gif("output_fps24.gif", fps=24)  # 256 色一秒 24 格
output.write_gif("output_fps8.gif", fps=8)  # 256 色一秒 8 格
output.write_gif("output_fps8_c2.gif", fps=8, colors=2)  # 2 色一秒 8 格
output.write_gif("output_fps8_c16.gif", fps=8, colors=16)  # 16 色一秒 8 格
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code026.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))  # 建立色彩模式為 RGBA，尺寸 360x180 的空白圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)  # 設定字型與尺寸
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
# 將文字畫入圖片
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")  # 儲存為 png


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code027.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img = Image.new("RGBA", (360, 180))
font = ImageFont.truetype("NotoSansTC-Regular.otf", 40)
draw = ImageDraw.Draw(img)
draw.text(
    (10, 120),
    "OXXO.STUDIO",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="red",
)
draw.text(
    xy=(50, 0),
    text="大家好\n哈哈",
    align="center",
    fill=(255, 255, 255),
    font=font,
    stroke_width=2,
    stroke_fill="blue",
)
img.save("ok.png")

video = VideoFileClip("baby_shark.mp4")  # 讀取影片
clip = video.resize((360, 180)).subclip(10, 12)  # 縮小影片尺寸，剪輯出 10～12 秒的片段
text_clip = ImageClip("ok.png", transparent=True).set_duration(2)  # 讀取圖片，將圖片變成長度兩秒的影片

output = CompositeVideoClip([clip, text_clip])  # 混合影片
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)

print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code028.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw

img_empty = Image.new("RGBA", (360, 180))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 24)  # 設定文字字體和大小
video = VideoFileClip("oxxostudio.mp4").resize((360, 180))  # 讀取影片，改變尺寸
output_list = []  # 記錄最後要組合的影片片段


# 建立文字字卡函式
def text_clip(xy, text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    draw.text(
        xy, text, fill=(255, 255, 255), font=font, stroke_width=2, stroke_fill="black"
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 文字串列，包含座標和內容
text_list = [
    [(100, 140), "你到底要怎樣？"],
    [(90, 140), "給我 CDPRO2 呀！"],
    [(60, 140), "但是 CDPRO2 過時啦！"],
]

# 影片串列，包含要切取的時間片段
video_list = [[13, 16], [21, 24], [38, 41]]

# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i][0], text_list[i][1], f"text_{i}.png")

# 使用 for 迴圈，合併字卡和影片
for i in range(len(video_list)):
    text_in_video(video_list[i], f"text_{i}.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_gif("output.gif", fps=6, colors=32)  # 轉換成 gif 動畫
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code029.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除


# 定義轉換為總秒數的函式
def time2sec(t):
    arr = t.split(" --> ")  # 根據「' --> '」拆分文字
    s1 = arr[0].split(",")  # 前方的文字為開始時間
    s2 = arr[1].split(",")  # 後方的文字為結束時間
    # 計算開始時間的總秒數
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    # 計算結束時間的總秒數
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]  # 回傳開始時間與結束時間的串列


f = open("oxxostudio.srt", "r")  # 使用 open 方法的 r 開啟字幕檔案
srt = f.read()  # 讀取字幕檔案內容
f.close()  # 關閉檔案
srt_list = srt.split("\n")  # 將內容根據換行符號 \n 拆分成串列
sec = 1  # 串列中秒數從第二項開始 ( 串列的第二項的索引值為 1 )
text = 2  # 串列中文字內容從第三項開始 ( 串列的第三項的索引值為 2 )
sec_list = [[0, 0]]  # 定義時間串列的開頭為 [0,0]
text_list = [""]  # 定義字幕內容串列的開頭為空字串 ''
# 使用迴圈，讀取字幕檔案串列的每個項目
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4  # 如果遇到時間內容，就將 sec + 4 ( 因為時間每隔 4 個項目會出現 )
        # 如果兩個串列項目內容前後對不上 ( 前一個結束時間不等於後一個的開始時間 )
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            # 在時間串列中間添加一個開始時間與結束時間內容 ( 表示該區間沒有字幕 )
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            # 在文字串列中間添加一個空字串 ( 表示該區間沒有字幕 )
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))  # 添加時間到時間串列
    if i == text:
        text = text + 4  # 如果遇到文字內容，就將 text + 4 ( 因為文字每隔 4 個項目會出現 )
        text_list.append(srt_list[i])  # 添加文字到文字串列

print(sec_list)
print(text_list)


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code030.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *
from PIL import Image, ImageFont, ImageDraw


def time2sec(t):
    arr = t.split(" --> ")
    s1 = arr[0].split(",")
    s2 = arr[1].split(",")
    start = (
        int(s1[0].split(":")[0]) * 3600
        + int(s1[0].split(":")[1]) * 60
        + int(s1[0].split(":")[2])
        + float(s1[1]) * 0.001
    )
    end = (
        int(s2[0].split(":")[0]) * 3600
        + int(s2[0].split(":")[1]) * 60
        + int(s2[0].split(":")[2])
        + float(s2[1]) * 0.001
    )
    return [start, end]


f = open("oxxostudio.srt", "r")
srt = f.read()
f.close()
srt_list = srt.split("\n")
# print(text_list)
sec = 1
text = 2
srt_list = [[0, 0]]
text_list = [""]
for i in range(len(srt_list)):
    if i == sec:
        sec = sec + 4
        if sec_list[-1][1] != time2sec(srt_list[i])[0]:
            sec_list.append([sec_list[-1][1], time2sec(srt_list[i])[0]])
            text_list.append("")
        sec_list.append(time2sec(srt_list[i]))
    if i == text:
        text = text + 4
        text_list.append(srt_list[i])

print(sec_list)
print(text_list)

img_empty = Image.new("RGBA", (480, 240))  # 產生 RGBA 空圖片
font = ImageFont.truetype("NotoSansTC-Regular.otf", 20)  # 設定文字字體和大小
video = VideoFileClip("baby_shark.mp4").resize((480, 240))  # 讀取影片，改變尺寸
video_duration = float(video.duration)  # 讀取影片總長度
output_list = []  # 記錄最後要組合的影片片段

# 如果字幕最後的時間小於總長度
if sec_list[-1][1] != video_duration:
    sec_list.append([sec_list[-1][1], video_duration])  # 添加時間到時間串列
    text_list.append("")  # 添加空字串到文字串列


# 建立文字字卡函式
def text_clip(text, name):
    img = img_empty.copy()  # 複製空圖片
    draw = ImageDraw.Draw(img)  # 建立繪圖物件，並寫入文字
    text_width = 21 * len(text)  # 在 480x240 文字大小 20 狀態下，一個中文字長度約 21px
    draw.text(
        ((480 - text_width) / 2, 10),
        text,
        fill=(255, 255, 255),
        font=font,
        stroke_width=2,
        stroke_fill="black",
    )
    img.save(name)  # 儲存


# 建立影片和文字合併的函式
def text_in_video(t, text_img):
    clip = video.subclip(t[0], t[1])  # 剪輯影片到指定長度
    text = ImageClip(text_img, transparent=True).set_duration(
        t[1] - t[0]
    )  # 讀取字卡，調整為影片長度
    combine_clip = CompositeVideoClip([clip, text])  # 合併影片和文字
    output_list.append(combine_clip)  # 添加到影片片段裡


# 使用 for 迴圈，產生文字字卡
for i in range(len(text_list)):
    text_clip(text_list[i], "srt.png")
    text_in_video(sec_list[i], "srt.png")

output = concatenate_videoclips(output_list)  # 合併所有影片片段
output.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code031.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.mp4")
frame = video.save_frame("frame1.jpg", t=22)
frame = video.save_frame("frame2.jpg", t=22.1)
frame = video.save_frame("frame3.jpg", t=22.2)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code032.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

img_clip = ImageClip("oxxostudio.jpg", transparent=True).set_duration(2)
img_clip.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code032-1.py

# Copyright © https://steam.oxxostudio.tw


import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

img1 = ImageClip("oxxo1.jpg", transparent=True).set_duration(3)
img2 = (
    ImageClip("oxxo2.jpg", transparent=True).set_duration(4).set_start(2).crossfadein(1)
)
img3 = (
    ImageClip("oxxo3.jpg", transparent=True).set_duration(3).set_start(5).crossfadein(1)
)

output = CompositeVideoClip([img1, img2, img3])

output.write_videofile(
    "output.mp4",
    fps=30,
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")

print("------------------------------------------------------------")  # 60個

# 檔案 : C:\_git\vcs\_4.python\__code\_oxxo\python\ch15\code033.py

# Copyright © https://steam.oxxostudio.tw

import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

from moviepy.editor import *

video = VideoFileClip("oxxostudio.gif")
video.write_videofile(
    "output.mp4",
    temp_audiofile="temp-audio.m4a",
    remove_temp=True,
    codec="libx264",
    audio_codec="aac",
)
print("ok")


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
