"""
PIL 新進

使用python進行數字圖片處理，還得安裝Pillow包。
雖然python里面自帶一個PIL（python images library), 但這個庫現在已經停止更新了，
所以使用Pillow, 它是由PIL發展而來的。

pip install Pillow


PIL中所涉及的基本概念有如下幾個：
通道（bands）
模式（mode）
尺寸（size）
坐標系統（coordinate system）
調色板（palette）
信息（info）
濾波器（filters）

1、  通道
彩色圖片 RGB 3通道
灰階圖片 1通道

2、  模式

圖像的模式定義了圖像的類型和像素的位寬。當前支持如下模式：

1：1位像素，表示黑和白，但是存儲的時候每個像素存儲為8bit。
L：8位像素，表示黑和白。
P：8位像素，使用調色板映射到其他模式。
RGB：3x8位像素，為真彩色。
RGBA：4x8位像素，有透明通道的真彩色。
CMYK：4x8位像素，顏色分離。
YCbCr：3x8位像素，彩色視頻格式。
I：32位整型像素。
F：32位浮點型像素。

3、  尺寸
4、  坐標系統

PIL使用笛卡爾像素坐標系統，坐標(0，0)位于左上角。
注意：坐標值表示像素的角；位于坐標（0，0）處的像素的中心實際上位于（0.5，0.5）。
坐標經常用于二元組（x，y）。
長方形則表示為四元組，前面是左上角坐標。
例如，一個覆蓋800x600的像素圖像的長方形表示為（0，0，800，600）。

5、  調色板

調色板模式 ("P")使用一個顏色調色板為每個像素定義具體的顏色值

6、  信息

使用info屬性可以為一張圖片添加一些輔助信息。這個是字典對象。
加載和保存圖像文件時，多少信息需要處理取決于文件格式。

7、  濾波器

對于將多個輸入像素映射為一個輸出像素的幾何操作，PIL提供了4個不同的采樣濾波器：

NEAREST：最近濾波。從輸入圖像中選取最近的像素作為輸出像素。它忽略了所有其他的像素。
BILINEAR：雙線性濾波。在輸入圖像的2x2矩陣上進行線性插值。注意：PIL的當前版本，做下采樣時該濾波器使用了固定輸入模板。
BICUBIC：雙立方濾波。在輸入圖像的4x4矩陣上進行立方插值。注意：PIL的當前版本，做下采樣時該濾波器使用了固定輸入模板。
ANTIALIAS：平滑濾波。這是PIL 1.1.3版本中新的濾波器。
對所有可以影響輸出像素的輸入像素進行高質量的重采樣濾波，以計算輸出像素值。
在當前的PIL版本中，這個濾波器只用于改變尺寸和縮略圖方法。

注意：在當前的PIL版本中，ANTIALIAS濾波器是下采樣（例如，將一個大的圖像轉換為小圖）時唯一正確的濾波器。
BILIEAR和BICUBIC濾波器使用固定的輸入模板，用于固定比例的幾何變換和上采樣是最好的。

Image模塊中的方法resize()和thumbnail()用到了濾波器。

PIL 之 resize()

image.resize(size, filter=None)

>>>im_resize = im.resize((256,256))

對參數filter不賦值的話，方法resize()默認使用NEAREST濾波器。

>>>im_resize0 = im.resize((256,256), Image.BILINEAR)
>>>im_resize1 = im.resize((256,256), Image.BICUBIC)
>>>im_resize2 = im.resize((256,256), Image.ANTIALIAS)

PIL 之 thumbnail()

image.thumbnail(size, filter=None)

>>>im.thumbnail((200,200))

這里需要說明的是，方法thumbnail()需要保持寬高比，對于size=(200,200)的輸入參數，其最終的縮略圖尺寸為(200, 112)。
對參數filter不賦值的話，方法thumbnail()默認使用NEAREST濾波器。如果要使用其他濾波器可以通過下面的方法來實現：

>>> im.thumbnail((200,200),Image.BILINEAR)
>>> im.thumbnail((200,200), Image.BICUBIC)
>>> im.thumbnail((200,200), Image.ANTIALIAS)



"""

print("------------------------------------------------------------")  # 60個

import PIL
from PIL import Image

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
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

filename1 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/red_300X300.bmp"
filename2 = "C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp"

filename1 = "C:/_git/vcs/_1.data/______test_files1/picture2.jpg"
filename2 = "C:/_git/vcs/_1.data/______test_files1/picture1.bmp"

"""
平均雜湊（aHash）
ahash:          Average hash
hashfunc = imagehash.average_hash
感知雜湊（pHash）
phash:          Perceptual hash
hashfunc = imagehash.phash
差異雜湊（dHash）
dhash:          Difference hash
hashfunc = imagehash.dhash
小波雜湊（wHash）
whash-haar:     Haar wavelet hash
hashfunc = imagehash.whash
whash-db4:      Daubechies wavelet hash
imagehash.whash(image, mode='db4')
colorhash:      HSV color hash
hashmethod == 'crop-resistant':
crop-resistant: Crop-resistant hash
imagehash.crop_resistant_hash
"""
import imagehash

# 檔案 => PIL影像
image1 = Image.open(filename1)

# 檔案 => PIL影像
image2 = Image.open(filename2)

hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)

print("圖一的hash :", hash1)
print("圖二的hash :", hash2)

if hash1 == hash2:
    print("兩圖相同")
else:
    print("兩圖不同")

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
font_filename = "C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf"

print("------------------------------------------------------------")  # 60個

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
"""

post_html = """
</table>
</body>
</html>
"""
"""
table_html = ""

source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for file in allfiles:
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            #thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容            
            table_html += "<tr><td><a href='{}'><img src='{}'></a></td></tr>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

pre_html = """
<!DOCTYPE html>
<head>
<meta charset='utf-8'/>
</head>
<body>
<table>
<tr>
"""

post_html = """
</tr>
</table>
</body>
</html>
"""


table_html = ""
"""
source = input("請輸入來源資料夾：")
if os.path.exists(source):
    target = input("請輸入目標資料夾：")
    if not os.path.exists(target):
        os.mkdir(target)
        allfiles = os.listdir(source)
        for index, file in enumerate(allfiles):
            filename, ext = os.path.splitext(file)
            filename = filename + "_s"
            targetfile = filename + ext
            image = Image.open(os.path.join(source, file))
            thumbnail = image.resize((320,200))
            #thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
#以下的程式碼用來建立HTML索引檔的表格內容         
            table_html += "<td><a href='{}'><img src='{}'></a></td>".format(
                os.path.join("..", os.path.join(source, file)),
                targetfile)
            if (index+1) % 3 == 0:
                table_html += "</tr><tr>"
#以上的程式碼用來建立HTML索引檔的表格內容
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
html = pre_html + table_html + post_html
with open(os.path.join(target, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)
"""
print("------------------------------------------------------------")  # 60個

"""
def blue_to_red2(image_path):
    image = Image.open(image_path)
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = pixels[x, y]

            #若該點的藍色成分明顯超過紅色及綠色,我們便將之視為藍色
            if b > r and b > g:
                #將藍色分轉為紅色
                pixels[x, y] = (b, g, r)
    image.show()

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'    
blue_to_red2(filename)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

"""
print("PIL_ginput")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像 => numpy陣列
im = np.array(Image.open(filename))
plt.imshow(im)

print('請點擊3個點')
x = plt.ginput(3)
print('你已點擊:', x)
plt.show()
"""

print("------------------------------------------------------------")  # 60個

"""
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

from PIL import Image

chiling = Image.open(filename)
chiling.show()

#使用濾鏡。

from PIL import ImageFilter

chiling.filter(ImageFilter.EMBOSS).show()
chiling.filter(ImageFilter.CONTOUR).show()

#圖像剪裁和粘貼。

rect = 220, 690, 265, 740 
watch = chiling.crop(rect)
watch.show()
blured_watch = watch.filter(ImageFilter.GaussianBlur(4))
chiling.paste(blured_watch, (220, 690))
chiling.show()

#生成鏡像。

chiling2 = chiling.transpose(Image.FLIP_LEFT_RIGHT)
chiling2.show()

#生成縮略圖。

width, height = chiling.size
width, height = int(width * 0.4), int(height * 0.4)
chiling.thumbnail((width, height))

#合成圖片。

frame = Image.open(filename)
frame.show()
frame.paste(chiling, (210, 150))
frame.paste(chiling2, (522, 150))
frame.show()

"""


print("------------------------------------------------------------")  # 60個


from PIL import Image

filename = (
    "C:/_git/vcs/_1.data/______test_files1/__pic/_image_processing/pic6_childrenb.png"
)

image_width = 800

img = Image.open(filename)
w, h = img.size
print(img.size)

img = img.resize((image_width, int(image_width / float(w) * h)))

img.save("aaaaa.png")
print("<{}> resize 完成!".format(filename))
img.close()

print("------------------------------------------------------------")  # 60個

"""
import glob
import os
import threading

from PIL import Image

PREFIX = 'thumbnails'

def generate_thumbnail(infile, size, format='PNG'):
    #生成指定圖片文件的縮略圖
	file, ext = os.path.splitext(infile)
	file = file[file.rfind('/') + 1:]
	outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
	img = Image.open(infile)
	img.thumbnail(size, Image.ANTIALIAS)
	img.save(outfile, format)

def main():
	if not os.path.exists(PREFIX):
		os.mkdir(PREFIX)
	# 撈出單層png檔
	for infile in glob.glob('images/*.png'):
		for size in (32, 64, 128):
            # 創建並啟動線程
			threading.Thread(
				target=generate_thumbnail, 
				args=(infile, (size, size))
			).start()
			

if __name__ == '__main__':
	main()

"""

print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_4.python/_data/picture1.jpg"
# filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_gif/SpongeBob.gif'

from PIL import Image

img = Image.open(filename)
print(img.mode)

# 01   Img_8 = img.convert("P")
# 02   Img_8.save('xxx.png')
