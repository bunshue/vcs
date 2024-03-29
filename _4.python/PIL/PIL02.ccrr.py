"""

PIL 圖片相關的處理

無 影像處理

CCRR

裁剪 .crop
複製 .copy
縮放 .resize
旋轉 .rotate(

貼上 .paste

合成
鏡射 .transpose(

拆分 .split() r, g, b = image1.split()   #r, g, b為三個通道的list
合併 .merge


幾何變換 

Image類有resize()、rotate()和transpose()方法進行幾何變換。

1、圖像的縮放和旋轉

dst = image.resize((128, 128))
dst = image.rotate(45) # 順時針角度表示

2、轉換圖像

dst = im.transpose(Image.FLIP_LEFT_RIGHT) #左右互換
dst = im.transpose(Image.FLIP_TOP_BOTTOM) #上下互換
dst = im.transpose(Image.ROTATE_90)  #順時針旋轉
dst = im.transpose(Image.ROTATE_180)
dst = im.transpose(Image.ROTATE_270)

transpose()和rotate()沒有性能差別。


"""
from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageFilter

import glob
import shutil
from time import sleep

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

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)
print(image.format, image.size, image.mode)

print("顯示PIL影像")
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 縮放 resize')

# 檔案 => PIL影像
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

print('寬度變2倍, 高度變一半')
image2 = image1.resize((W*2, H//2), Image.LANCZOS)

print('寬度變2倍, 高度不變')
image3 = image1.resize((W*2, H))   # 寬度是2倍

print('寬度不變, 高度變2倍')
image4 = image1.resize((W, H*2))   # 高度是2倍

print('------------------------------------------------------------')	#60個

print('依比例縮放圖片')

# 檔案 => PIL影像
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image2 = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image2.size)

print("------------------------------------------------------------")  # 60個

print('測試 裁剪 crop')

# 檔案 => PIL影像
image1 = Image.open(filename)    #PIL讀取本機圖片, RGB模式
W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

x_st = 50
y_st = 50
w = W - x_st * 2
h = H - y_st * 2

#                     x_st  y_st    x_sp     y_sp
image2 = image1.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間, 左上點到右下點

print('裁剪一塊 (x_sy, y_st, x_sp, y_sp)')

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片
#plt.imshow(image_copied)
#plt.show()

x_st = 0
y_st = 0
w = 300 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
image_crop = image_copied.crop((x_st, y_st, x_st + w, y_st + h))  # 裁切區間
image_copied.paste(image_crop, (20, 20))          # 第一次合成
image_copied.paste(image_crop, (20, 20 + 120))    # 第二次合成
image_copied.paste(image_crop, (20, 20 + 240))    # 第三次合成

print('合成圖片')
plt.imshow(image_copied)
plt.show()

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
image = Image.open(filename)     # 建立Pillow物件

print('複製圖片')
image_copied = image.copy() #複製圖片

x_st = 0
y_st = 0
w = 300 / 4
h = 400 / 4
#                             x_st  y_st    x_sp     y_sp
image_crop = image_copied.crop((x_st, y_st, x_st + w, y_st + h))    # 裁切區間
cropW, cropH = image_crop.size           # 獲得裁切區間的寬與高

W, H = 600, 320                        # 新影像寬與高
image = Image.new('RGB', (W, H), "Yellow")  # 建立新影像
for x in range(20, W - 20, cropW):         # 雙層迴圈合成
    for y in range(20, H - 20, cropH):
        image.paste(image_crop, (x, y))        # 合成

print('合成圖片')
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

print('測試 旋轉 rotate')

# 檔案 => PIL影像
image = Image.open(filename)     # 建立Pillow物件

print('旋轉90度')
image90 = image.rotate(90)

print('旋轉180度')
image180 = image.rotate(180)

print('旋轉270度')
image270 = image.rotate(270)

print('旋轉45度')
image45a = image.rotate(45)

print('旋轉45度 + 圖像擴充')
image45a = image.rotate(45, expand = True)

print('旋轉60度 + xxx1')
image60a = image.rotate(60, Image.BILINEAR,0,None,None,'#BBCC55')

print('旋轉60度 + xxx2')
image60b = image.rotate(60, Image.BILINEAR, 1, None, None, '#BBCC55')

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)     # 建立Pillow物件

print('左右相反')
image1 = image.transpose(Image.FLIP_LEFT_RIGHT)   # 左右

print('上下顛倒')
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)   # 上下

print('旋轉90度')
rotate90 = image.transpose(Image.ROTATE_90)

image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
image2 = image.transpose(Image.ROTATE_90)
image2 = image.transpose(Image.ROTATE_180)
image2 = image.transpose(Image.ROTATE_270)
image2 = image.transpose(Image.TRANSPOSE)
image2 = image.transpose(Image.TRANSVERSE)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)

r, g, b = image.split()

plt.imshow(image)
plt.title('image')
plt.show()

plt.imshow(r)
plt.title('r')
plt.show()

plt.imshow(g)
plt.title('g')
plt.show()

plt.imshow(b)
plt.title('b')
plt.show()

print('RGB相反排列')
convert_image = Image.merge('RGB', (b, g, r))

plt.imshow(convert_image)
plt.title('bgr')
plt.show()

# 檔案 => PIL影像
image = Image.open(filename)    #PIL讀取本機圖片
r, g, b = image.split()

convert_image = Image.merge('RGB', (b, g, r))
#NG image

convert_image = Image.merge('RGB', (r, g, b))
#OK image

print('------------------------------------------------------------')	#60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/bear.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files2/bear_filter.jpg'

# 檔案 => PIL影像
image = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
plt.imshow(image)
plt.show()

#對圖形套用過濾器
im_sharp = image.filter(ImageFilter.SHARPEN)

plt.imshow(im_sharp)
plt.show()

#分解圖形顏色 例如RGB的紅綠藍
#看不出效果
r,g,b = im_sharp.split()

plt.imshow(r)
plt.show()

plt.imshow(g)
plt.show()

plt.imshow(b)
plt.show()

print('------------------------------------------------------------')	#60個

#調整資料夾內所有圖片檔影像寬度, 加logo
      
source_dir = 'C:/_git/vcs/_1.data/______test_files1/__pic/_book'
target_dir = 'C:/_git/vcs/_1.data/______test_files2/tmp_resized_pic'
#logo_filename = 'C:/_git/vcs/_1.data/______test_files1/burn.bmp'        #fail, bad transparency mask
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/logo.png'

#準備輸出資料夾 若已存在, 則先刪除再建立 若不存在, 則建立
if os.path.exists(target_dir):
        #os.remove(target_dir)  #存取被拒 不可用
        shutil.rmtree(target_dir)
if not os.path.exists(target_dir):
        os.mkdir(target_dir)

image_W = 800

print("將資料夾 " + source_dir + " 內所有圖片檔調整寬度成 " + str(image_W) + " 像素")

print('Processing: {}'.format(source_dir))

#單層
allfiles = glob.glob(source_dir + '/*.jpg') + glob.glob(source_dir + '/*.png')

# 檔案 => PIL影像
logo = Image.open(logo_filename)    #PIL讀取本機圖片
logo = logo.resize((150, 150))   #調整圖像大小

plt.imshow(logo)
plt.show()

for target_image in allfiles:
	pathname, filename = os.path.split(target_image)
	print(filename)
	# 檔案 => PIL影像
	image = Image.open(target_image)    #PIL讀取本機圖片
	W, H = image.size
	image = image.resize((800, int(800 / float(W) * H)))
	image.paste(logo, (0, 0), logo)
	image.save(target_dir + '/' + filename)
	image.close()

print("完成")
print('輸出圖片資料夾 : ', target_dir)

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#print('顯示原圖')
#plt.imshow(image1)
#plt.show()

# PIL影像 => 灰階
image1g = image1.convert('L')	#轉換成灰階圖像
plt.imshow(image1g)      #灰階圖
plt.show()

W, H = image1g.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1g.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

image2_hist = image2.histogram()

W2, H2 = 400, 200
print('把原圖轉成', W2, 'X', H2, '大小')
image3 = image1.resize((W2, H2), Image.LANCZOS)

plt.imshow(image3)
plt.show()

image1g = image3.convert('L')	#轉換成灰階圖像
hist = image1g.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(image2_hist))
ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color = 'cyan', label = 'cropped')
plt.plot(ind, hist, color = 'black', lw = 2, label = 'original')
plt.plot(ind, r_hist, color = 'red', label = 'Red Plane')
plt.plot(ind, g_hist, color = 'green', label = 'Green Plane')
plt.plot(ind, g_hist, color = 'blue', label = 'Blue Plane')
plt.xlim(0-10, 256+10)
plt.ylim(0, 8000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個

print('合併圖 2 X 4 a')

bg = Image.new("RGB", (1200, 800), "#000000")  # 產生一張 1200x800 的全黑圖片
for i in range(1, 9):
    image = Image.open(f"C:/_git/vcs/_1.data/______test_files1/__pic/_MU/poster_0{i}.jpg")  # 開啟圖片
    image2 = image.resize((300, 400))  # 縮小尺寸為 300x400
    x = (i - 1) % 4  # 根據開啟的順序，決定 x 座標
    y = (i - 1) // 4  # 根據開啟的順序，決定 y 座標 ( // 為快速取整數 )
    bg.paste(image2, (x * 300, y * 400))  # 貼上圖片

bg.save("tmp_compound2X4a.jpg")

print("------------------------------------------------------------")  # 60個

print('合併圖 2 X 4 b')
bg = Image.new("RGB", (1240, 840), "#000000")  # 因為擴張，所以將尺寸改成 1240x840
for i in range(1, 9):
    image = Image.open(f"C:/_git/vcs/_1.data/______test_files1/__pic/_MU/poster_0{i}.jpg")  # 開啟圖片
    image2 = image.resize((300, 400))
    image3 = ImageOps.expand(image2, 20, "#ffffff")  # 擴張邊緣，產生邊框
    x = (i - 1) % 4
    y = (i - 1) // 4
    bg.paste(image3, (x * 300, y * 400))

bg.save("tmp_compound2X4b.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

# 檔案 => PIL影像
image = Image.open(filename)  # 開啟風景圖

# 檔案 => PIL影像
icon = Image.open(logo_filename)  # 開啟浮水印 icon

image.paste(icon, (0, 0), icon)  # 將風景圖貼上 icon

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

# 檔案 => PIL影像
image = Image.open(filename)

# 檔案 => PIL影像
icon = Image.open(logo_filename)

image_w, image_h = image.size  # 取得風景圖尺寸
icon_w, icon_h = icon.size  # 取得 icon 尺寸
x = int((image_w - icon_w) / 2)  # 計算置中時 icon 左上角的 x 座標
y = int((image_h - icon_h) / 2)  # 計算置中時 icon 左上角的 y 座標

image.paste(icon, (x, y), icon)  # 設定 icon 左上角座標

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

print('將一個資料夾內的所有圖片加上logo')

foldername = 'tmp_watermark'

if not os.path.exists(foldername):
    os.mkdir(foldername)

logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

images = glob.glob("./data/*.jpg")  # 讀取 demo 資料夾裡所有的圖片, 撈出一層

# 檔案 => PIL影像
icon = Image.open(logo_filename)
for i in images:
    #print(i)
    name = i.split("/")[::-1][0]  # 取得圖片名稱
    #print(name)
    # 檔案 => PIL影像
    image = Image.open(i)  # 開啟圖片
    
    image.paste(icon, (0, 0), icon)  # 加入浮水印

    short_filename = os.path.basename(i)
    #print("短檔名 :", short_filename)
    image.save(f"./{foldername}/{short_filename}")  # 以原本的名稱存檔

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
logo_filename = 'C:/_git/vcs/_1.data/______test_files1/_icon/唐.png'

# 檔案 => PIL影像
image = Image.open(filename)  # 準備合成浮水印的圖

# 檔案 => PIL影像
image2 = Image.open(filename)  # 底圖

# 檔案 => PIL影像
icon = Image.open(logo_filename)

image_w, image_h = image.size
icon_w, icon_h = icon.size
x = int((image_w - icon_w) / 2)
y = int((image_h - icon_h) / 2)
image.paste(icon, (x, y), icon)  # 合成浮水印
image.convert("RGBA")  # 圖片轉換為 RGBA 模式 ( 才能調整 alpha 色版 )
image.putalpha(100)  # 調整透明度，範圍 0～255，0 為全透明
image2.paste(image, (0, 0), image)  # 合成底圖
#image2.save("./tmp_elephant_add_watermark.jpg")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

# 檔案 => PIL影像
image = Image.open(filename)  # 開啟圖片

w, h = image.size  # 讀取圖片長寬
level = 5  # 設定縮小程度
image2 = image.resize((int(w / level), int(h / level)))  # 縮小圖片
image2 = image2.resize((w, h), resample=Image.NEAREST)  # 放大圖片為原始大小

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

# 檔案 => PIL影像
image = Image.open(filename)

w, h = image.size
level = 5
image2 = image.resize((int(w / level), int(h / level)))
image2 = image2.resize((w, h), resample=Image.NEAREST)

x1, y1 = 60, 60  # 定義選取區域的左上角座標
x2, y2 = 250, 250  # 定義選取區域的右上角座標
area = image2.crop((x1, y1, x2, y2))  # 裁切區域
image.paste(area, (x1, y1))  # 在原本的圖片裡貼上馬賽克區域

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
image = Image.open(filename)           # 建立Pillow物件

image090=image.rotate(90)  # 旋轉90度
image180=image.rotate(180)  # 旋轉180度
image270=image.rotate(270)  # 旋轉270度
image45a=image.rotate(45)  # 旋轉45度
image45b=image.rotate(45, expand=True)  # 旋轉45度圖像擴充
image_flip1 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右
image_flip2 = image.transpose(Image.FLIP_TOP_BOTTOM)  # 上下
image_crop = image.crop((80, 30, 150, 100))   # 裁切區間

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)           # 建立Pillow物件
image_copy = image.copy()                      # 複製

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
img = Image.open(filename)
imgcopy=img.copy()

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
image = Image.open(filename)               # 建立Pillow物件
image_copy = image.copy()                          # 複製
image_crop = image_copy.crop((80, 30, 150, 100))    # 裁切區間
image_copy.paste(image_crop, (20, 20))              # 第一次合成
image_copy.paste(image_crop, (20, 100))             # 第二次合成

print("------------------------------------------------------------")  # 60個

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename1)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.LANCZOS)

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)

plt.imshow(image)

plt.show()

w,h = image.size

image1 = image.resize((w*2,h), Image.LANCZOS)

plt.imshow(image1)

plt.show()

image2 = image.convert('1')

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename)        # 建立Pillow物件
image2 = image1.resize((350,500))

W, H = 450, 600
image3 = Image.new('RGB', (W, H), "Yellow")

image3.paste(image2, (50,50))

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_resize2.png"

# 檔案 => PIL影像
image = Image.open(infile)
image = image.resize((100, 100), Image.LANCZOS)     #調整大小

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earthH.png"
savefile = "tmp_resize1.png"

max_size = 100

# 檔案 => PIL影像
image = Image.open(infile)
ratio = max_size / max(image.size)    #根據長寬較長的一邊決定縮放比率
w = int(image.width * ratio)
h = int(image.height * ratio)
image = image.resize((w, h), Image.LANCZOS)     #調整大小

"""
#調整圖片大小的範例
mini_im = im.resize((int(im.size[0] * 0.2), int(im.size[1] * 0.2)))
display(mini_im)
print(mini_im.size)
"""

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
# 檔案 => PIL影像
image = Image.open(filename)
w,h=image.size #320 240

image1=image.resize((w*2,h))

image2=image.resize((w,h*2))

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
# 檔案 => PIL影像
image = Image.open(filename)
imagecopy=image.copy() #複製
#切割貓熊並改變尺寸
image1=imagecopy.crop((190,184,415,350)).resize((160,140))
imagecopy.paste(image1,(40,30)) #貼上
image2=image1.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
imagecopy.paste(image2,(220,40))#貼上

print("------------------------------------------------------------")  # 60個


def emptydir(dirname):
    if os.path.isdir(dirname):
        shutil.rmtree(dirname)
        sleep(1)  #需延遲,否則會出錯
    os.mkdir(dirname)

image_dir="data"
target_dir = 'tmp_bmp_photo'
target_dir2 = 'tmp_gray_photo'
emptydir(target_dir)
emptydir(target_dir2)
files=glob.glob(image_dir+"\*.jpg") + glob.glob(image_dir+"\*.png")
for i, f in enumerate(files):
    # 檔案 => PIL影像
    image = Image.open(f)
    image_new = image.resize((800, 600), Image.LANCZOS)
    path,filename = f.split("\\") #路徑、檔名   
    name,ext = filename.split(".") #主檔名、副檔名
    #以bmp格式存檔
    image_new.save(target_dir+'/' + name + 'aaa.bmp')
    
    #轉換為灰階
    image_gray = image_new.convert('L')  
    # gray001.jpg、gray002.jpg...
    outname = str("gray") + str('{:0>3d}').format(i+1) + 'aaa.jpg'
    image_gray.save(target_dir2+'/'+outname)
    print("{} 複製完成!".format(f))
    image.close()   

print('轉換尺寸及灰階處理結束！')

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    image2 = image.crop((x, y, w, h))
    print(image2.size)

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    print(image.size)
    w = 200
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image2 = image.resize((w, h))
    print(image2.size)

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    image2 = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image2.size)

print("------------------------------------------------------------")  # 60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image2 = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image2.size)

print("------------------------------------------------------------")  # 60個

print("縮放和黏貼圖像")

filename2 = "C:/_git/vcs/_1.data/______test_files1/bear.jpg"

# 檔案 => PIL影像
image1 = Image.open(filename2)

# 檔案 => PIL影像
image2 = Image.open(filename)

rect = 80, 20, 310, 360
guido_head = image2.crop(rect)
width, height = guido_head.size
image1.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))

plt.imshow(image1)
plt.show()

print("------------------------------------------------------------")  # 60個

print("剪裁圖像")

# 檔案 => PIL影像
image = Image.open(filename)

rect = 80, 20, 310, 360
image.crop(rect)

plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

print("生成縮略圖")

# 檔案 => PIL影像
image = Image.open(filename)

size = 128, 128
image.thumbnail(size)

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

#crop

# 檔案 => PIL影像
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 300
    image2 = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image2.size)

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    image2 = image.rotate(180)

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    image2 = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
with Image.open(filename) as image:
    image2 = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')

print('------------------------------------------------------------')	#60個

print('保持圖片原始大小之旋轉')
# 檔案 => PIL影像
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
# 檔案 => PIL影像
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
# 檔案 => PIL影像
image = Image.open(filename)

image1=image.rotate(45)#旋轉45度
image2=image.rotate(90) #旋轉90度
image3=image.rotate(180)#旋轉180度

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename)

image2=image.transpose(Image.FLIP_LEFT_RIGHT)#左右翻轉
image3=image.transpose(Image.FLIP_TOP_BOTTOM)#上下翻轉

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image = Image.open(filename) # w,h=image.size #320 240

image1=image.crop((0,0,160,120))
image2=image.crop((161,0,320,120))
image3=image.crop((0,121,160,240))
image4=image.crop((161,121,320,240))

image.close()

print("------------------------------------------------------------")  # 60個

#裁剪圖片
#從原圖片中裁剪感興趣區域（roi),裁剪區域由4-tuple決定，該tuple中信息為(left, upper, right, lower)。 Pillow左邊系統的原點（0，0）為圖片的左上角。坐標中的數字單位為像素點。

# 檔案 => PIL影像
image=Image.open(filename)  #打開圖像
plt.figure('Peony')
plt.subplot(1,2,1)
plt.title('origin')
plt.imshow(image),plt.axis('off')

box=(80,100,260,300)
roi=image.crop(box)
plt.subplot(1,2,2)
plt.title('roi')
plt.imshow(roi),plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

# 檔案 => PIL影像
image1 = Image.open(filename)               # 建立Pillow物件
image2 = image1.copy()                          # 複製
image3 = image2.crop((80, 30, 150, 100))    # 裁切區間
cropW, cropH = image3.size           # 獲得裁切區間的寬與高

W, H = 600, 320                        # 新影像寬與高
image4 = Image.new('RGB', (W, H), "Yellow")  # 建立新影像
for x in range(20, W-20, cropW):         # 雙層迴圈合成
    for y in range(20, H-20, cropH):
        image4.paste(image3, (x, y))        # 合成

print("------------------------------------------------------------")  # 60個

print("PIL_operation")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

plt.figure()
# 顯示原圖

# 檔案 => PIL影像
image = Image.open(filename)
print(image.mode, image.size, image.format)

plt.subplot(231)
plt.title(u'原圖')
plt.imshow(image)

# 顯示灰度圖
# 檔案 => PIL影像 => 灰階
image = Image.open(filename).convert('L')

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(232)
plt.title(u'灰度圖')
plt.imshow(image)
# 複製並粘貼區域

# 檔案 => PIL影像
image = Image.open(filename)
box = (100, 100, 200, 200)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)

plt.subplot(233)
plt.title(u'復制粘貼區域')
plt.imshow(image)

# 縮略圖
# 檔案 => PIL影像
image = Image.open(filename)

size = 128, 128
image.thumbnail(size)
print(image.size)

plt.subplot(234)
plt.title(u'縮略圖')
plt.imshow(image)
#image.save('tmp_pic1.jpg')# 保存縮略圖

#調整圖像尺寸
# 檔案 => PIL影像
image=Image.open(filename)

image=image.resize(size)
print(image.size)

plt.subplot(235)
plt.title(u'調整尺寸後的圖像')
plt.imshow(image)

#旋轉圖像45°
# 檔案 => PIL影像
image=Image.open(filename)

image=image.rotate(45)

plt.subplot(236)
plt.title(u'旋轉45°後的圖像')
plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

#使用pillow操作图像

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
img = Image.open(filename)

# 檔案 => PIL影像
img2 = Image.open(filename)

#img3 = img2.crop((335, 435, 430, 615))
img3 = img2.crop((100, 100, 150, 150))
for x in range(4):
    for y in range(5):
        img2.paste(img3, (95 * y , 180 * x))

img2.resize((img.size[0] // 2, img.size[1] // 2))
img2.rotate(90)

plt.imshow(img2)
plt.show()

print('------------------------------------------------------------')	#60個

""" 處理資料夾有問題
foldername = 'C:/_git/vcs/_1.data/______test_files3/DrAP_test'

allfiles = os.listdir(foldername)
print(allfiles)
for file in allfiles:
    print(file)
    filename, ext = os.path.splitext(file)
    filename = filename + "_s"
    targetfile = filename + ext
    #print(foldername, file)
    image = Image.open(os.path.join(foldername, file))
    thumbnail = image.resize((320,200))
    #thumbnail.save(os.path.join(target, targetfile))
    image.close()
    thumbnail.close()
    print("{}-->{}".format(file, targetfile))
"""
print("------------------------------------------------------------")  # 60個

#paste

#把同樣的圖片排列成 M X N

# 要排列的圖示個數
M = 5
N = 8

# 圖片之間的邊界
margin = 5

# 載入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/AB_red.jpg'
# 檔案 => PIL影像
image = Image.open(filename)
print(image.size)

W, H = image.size

# 建立圖片 W*N X H*M
image_MXN = Image.new("RGBA", ((W + margin) * N, (H + margin) * M))

for j in range(M):
    for i in range(N):
        image_MXN.paste(image, ((W + margin) * i, (H + margin) * j))

plt.imshow(image_MXN)

plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_saveJPG2.jpg"

# 檔案 => PIL影像
img = Image.open(infile)
if img.format == "PNG":
    newimg = Image.new("RGB", img.size, "WHITE")
    newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上
    newimg.save(savefile, format="JPEG")    # JPG轉存檔案
elif img.format == "JPEG":
    img.save(savefile, format="JPEG")       # JPG轉存檔案

print("------------------------------------------------------------")  # 60個

from pathlib import Path

infolder = "testfolder"
value1 = "outputfolder4"
extlist = ["*.jpg","*.png"]

#【函數: 轉存為jpg檔案】
def savepng(readfile, savefolder):
    try:
        # 檔案 => PIL影像
        img = Image.open(readfile)              #載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        #-----------------------------------
        filename = Path(readfile).stem+".jpg"   #建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  #在白底背景繪製圖片
            #newimg.save(savepath, format="JPEG", quality=95)    #轉存為JPG圖檔
        elif img.format == "JPEG":
            #img.save(savepath, format="JPEG", quality=95)   #轉存為JPG圖檔
            pass
        #-----------------------------------
        msg = "在"+savefolder + "轉存" + filename + "了喲。\n"
        return msg
    except:
        return readfile + "：程式執行失敗。"
#【函數: 處理資料夾之內的圖片檔】
def savefiles(infolder, savefolder):
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).glob(ext):  #將這個資料夾的檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            msg += savepng(filename, savefolder)
    return msg

#【執行函數】
msg = savefiles(infolder, value1)
print(msg)




print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個

"""
# 存檔
# 檔案 => PIL影像 => 檔案
image2.save("tmp_pic31_resize.jpg" )
image2.save(savefile, format="PNG")
"""
