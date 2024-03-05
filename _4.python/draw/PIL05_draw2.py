import sys
from PIL import Image, ImageDraw, ImageFont

import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/ubuntu.ttf'    #無中文
font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'      #有中文

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)  # 開啟圖片
font = ImageFont.truetype(font_filename, 50)  # 設定字型
draw = ImageDraw.Draw(img)  # 準備在圖片上繪圖
draw.text((0, 0), "牡丹亭", fill=(0, 0, 255), font=font)  # 將文字畫入圖片

img.show()


print("------------------------------------------------------------")  # 60個


from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
w, h = img.size  # 取得圖片尺寸
font = ImageFont.truetype(font_filename, 100)
draw = ImageDraw.Draw(img)
draw.text(
    (0, h - 100), "牡丹亭", fill=(255, 255, 255), font=font
)  # 使用 h-100 定位到下方

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
font = ImageFont.truetype(font_filename, 150)
# 設定一張空白圖片，背景 (0,0,0,0) 表示透明背景
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)  # 畫入文字
text = text.rotate(30, expand=1)  # 旋轉這張圖片，expand 設定 1 表示展開旋轉，不要裁切
img.paste(text, (50, 0), text)  # 將文字的圖片貼上原本的圖

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFont, ImageDraw

img = Image.open(filename)
w, h = img.size

font = ImageFont.truetype(font_filename, 150)
text = Image.new(mode="RGBA", size=(600, 150), color=(0, 0, 0, 0))
draw = ImageDraw.Draw(text)
draw.text((0, 0), "牡丹亭", fill=(255, 255, 255), font=font)
text = text.rotate(30, expand=1)

img2 = Image.open(filename)  # 再次開啟原本的圖為 img2
img2.paste(text, (50, 0), text)  # 將文字貼上 img2
img2.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
img2.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
img.paste(img2, (0, 0), img2)  # 將 img2 貼上 img

print("------------------------------------------------------------")  # 60個






print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個




