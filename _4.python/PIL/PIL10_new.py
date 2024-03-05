"""
PIL 新進


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

print('顯示原圖')

image1 = Image.open(filename)    #建立Pillow物件 PIL讀取本機圖片, RGB模式
plt.imshow(image1)
plt.show()

print('------------------------------------------------------------')	#60個

"""
使用python進行數字圖片處理，還得安裝Pillow包。
雖然python里面自帶一個PIL（python images library), 但這個庫現在已經停止更新了，
所以使用Pillow, 它是由PIL發展而來的。

pip install Pillow
"""

print('------------------------------------------------------------')	#60個

"""
圖像通道\幾何變換\裁剪

一、圖像通道

1、彩色圖像轉灰度圖
"""

img=Image.open(filename)
gray=img.convert('L')
plt.figure('Peony')
plt.imshow(gray,cmap='gray')
plt.axis('off')
plt.show()

"""
使用函數convert()來進行轉換，它是圖像實例對象的一個方法，接受一個 mode 參數，用以指定一種色彩模式，mode 的取值可以是如下幾種：
· 1 (1-bit pixels, black and white, stored with one pixel per byte)
· L (8-bit pixels, black and white)
· P (8-bit pixels, mapped to any other mode using a colour palette)
· RGB (3x8-bit pixels, true colour)
· RGBA (4x8-bit pixels, true colour with transparency mask)
· CMYK (4x8-bit pixels, colour separation)
· YCbCr (3x8-bit pixels, colour video format)
· I (32-bit signed integer pixels)
· F (32-bit floating point pixels)

2、通道分離與合并
"""

img=Image.open(filename)  #打開圖像
gray=img.convert('L')   #轉換成灰度
r,g,b=img.split()   #分離三通道
pic=Image.merge('RGB',(r,g,b)) #合并三通道
plt.figure('Peony')
plt.subplot(2,3,1), plt.title('origin')
plt.imshow(img),plt.axis('off')
plt.subplot(2,3,2), plt.title('gray')
plt.imshow(gray,cmap='gray'),plt.axis('off')
plt.subplot(2,3,3), plt.title('merge')
plt.imshow(pic),plt.axis('off')
plt.subplot(2,3,4), plt.title('r')
plt.imshow(r,cmap='gray'),plt.axis('off')
plt.subplot(2,3,5), plt.title('g')
plt.imshow(g,cmap='gray'),plt.axis('off')
plt.subplot(2,3,6), plt.title('b')
plt.imshow(b,cmap='gray'),plt.axis('off')
plt.show()

"""

二、裁剪圖片

從原圖片中裁剪感興趣區域（roi),裁剪區域由4-tuple決定，該tuple中信息為(left, upper, right, lower)。 Pillow左邊系統的原點（0，0）為圖片的左上角。坐標中的數字單位為像素點。
"""

img=Image.open(filename)  #打開圖像
plt.figure('Peony')
plt.subplot(1,2,1)
plt.title('origin')
plt.imshow(img),plt.axis('off')

box=(80,100,260,300)
roi=img.crop(box)
plt.subplot(1,2,2)
plt.title('roi')
plt.imshow(roi),plt.axis('off')

plt.show()


"""

用plot繪制顯示出圖片后，將鼠標移動到圖片上，會在右下角出現當前點的坐標，以及像素值。

三、幾何變換 

Image類有resize()、rotate()和transpose()方法進行幾何變換。

　1、圖像的縮放和旋轉

dst = img.resize((128, 128))
dst = img.rotate(45) # 順時針角度表示

2、轉換圖像

dst = im.transpose(Image.FLIP_LEFT_RIGHT) #左右互換
dst = im.transpose(Image.FLIP_TOP_BOTTOM) #上下互換
dst = im.transpose(Image.ROTATE_90)  #順時針旋轉
dst = im.transpose(Image.ROTATE_180)
dst = im.transpose(Image.ROTATE_270)

transpose()和rotate()沒有性能差別。
"""


print('------------------------------------------------------------')	#60個

#添加水印
#一、添加文字水印

from PIL import Image, ImageDraw,ImageFont

im = Image.open(filename).convert('RGBA')
txt=Image.new('RGBA', im.size, (0,0,0,0))
fnt=ImageFont.truetype("c:/Windows/fonts/Tahoma.ttf", 20)
d=ImageDraw.Draw(txt)
d.text((txt.size[0]-80,txt.size[1]-30), 'Peony', font=fnt, fill=(255,0,255,255))
out=Image.alpha_composite(im, txt)
#out.show()
plt.imshow(out)
plt.show()


"""
#二、添加小圖片水印

im = Image.open(filename)
mark=Image.open("logo_small.gif")
layer=Image.new('RGBA', im.size, (0,0,0,0))
layer.paste(mark, (im.size[0]-150,im.size[1]-60))
out=Image.composite(layer,im,layer)
#out.show()
plt.imshow(out)
plt.show()

"""

print('------------------------------------------------------------')	#60個

"""
圖像中的像素訪問

前面的一些例子中，我們都是利用Image.open（）來打開一幅圖像，然后直接對這個PIL對象進行操作。如果只是簡單的操作還可以，但是如果操作稍微復雜一些，就比較吃力了。因此，通常我們加載完圖片后，都是把圖片轉換成矩陣來進行更加復雜的操作。

python中利用numpy庫和scipy庫來進行各種數據操作和科學計算。我們可以通過pip來直接安裝這兩個庫

pip install numpy
pip install scipy

"""

img=np.array(Image.open(filename))  #打開圖像并轉化為數字矩陣
plt.figure('Peony')
plt.imshow(img)
plt.axis('off')
plt.show()

"""

調用numpy中的array（）函數就可以將PIL對象轉換為數組對象。

查看圖片信息，可用如下的方法：

print img.shape  
print img.dtype 
print img.size 
print type(img)

如果是RGB圖片，那么轉換為array之后，就變成了一個rows*cols*channels的三維矩陣,因此，我們可以使用

img[i,j,k]

來訪問像素值。

例1：打開圖片，并隨機添加一些椒鹽噪聲
"""

img=np.array(Image.open(filename))

#隨機生成5000個椒鹽
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
plt.figure('Peony')
plt.imshow(img)
plt.axis('off')
plt.show()

"""

 

例2：將lena圖像二值化，像素值大于128的變為1，否則變為0
"""

img=np.array(Image.open(filename).convert('L'))

rows,cols=img.shape
for i in range(rows):
    for j in range(cols):
        if (img[i,j]<=128):
            img[i,j]=0
        else:
            img[i,j]=1
            
plt.figure('Peony')
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()

"""

 

如果要對多個像素點進行操作，可以使用數組切片方式訪問。切片方式返回的是以指定間隔下標訪問 該數組的像素值。下面是有關灰度圖像的一些例子：
復制代碼

img[i,:] = im[j,:] # 將第 j 行的數值賦值給第 i 行

img[:,i] = 100 # 將第 i 列的所有數值設為 100

img[:100,:50].sum() # 計算前 100 行、前 50 列所有數值的和

img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean() # 第 i 行所有數值的平均值

img[:,-1] # 最后一列

img[-2,:] (or im[-2]) # 倒數第二行

"""


print('------------------------------------------------------------')	#60個


"""
圖像直方圖

我們先來看兩個函數reshape和flatten:

假設我們先生成一個一維數組：

vec=np.arange(15)
print vec

顯示為：

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

如果我們要把這個一維數組，變成一個3*5二維矩陣，我們可以使用reshape來實現

mat= vec.reshape(3,5)
print mat

顯示為

[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]]

現在如果我們返過來，知道一個二維矩陣，要變成一個一維數組，就不能用reshape了，只能用flatten. 我們來看兩者的區別

a1=mat.reshape(1,-1)  #-1表示為任意，讓系統自動計算
print a1
a2=mat.flatten()
print a2

顯示為：

a1:  [[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]]
a2:  [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14]

可以看出，用reshape進行變換，實際上變換后還是二維數組，兩個方括號，因此只能用flatten.

我們要對圖像求直方圖，就需要先把圖像矩陣進行flatten操作，使之變為一維數組，然后再進行統計。

一、畫灰度圖直方圖

繪圖都可以調用matplotlib.pyplot庫來進行，其中的hist函數可以直接繪制直方圖。

調用方式：

n, bins, patches = plt.hist(arr, bins=50, density = True, facecolor='green', alpha=0.75)

hist的參數非常多，但常用的就這五個，只有第一個是必須的，后面四個可選

arr: 需要計算直方圖的一維數組

bins: 直方圖的柱數，可選項，默認為10

density: 是否將得到的直方圖向量歸一化。默認為False

facecolor: 直方圖顏色

alpha: 透明度

返回值 ：

n: 直方圖向量，是否歸一化由參數設定

bins: 返回各個bin的區間范圍

patches: 返回每個bin里面包含的數據，是一個list
"""

img=np.array(Image.open(filename).convert('L'))

plt.figure('Peony')
arr=img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density = True, facecolor='green', alpha=0.5)

plt.show()

"""
二、彩色圖片直方圖
實際上是和灰度直方圖一樣的，只是分別畫出三通道的直方圖，然后疊加在一起。
"""

src=Image.open(filename)
r, g, b=src.split()

plt.figure('Peony')
array_r = np.array(r).flatten()
plt.hist(array_r, bins=256, alpha=0.5, density = True,facecolor='r',edgecolor='r',stacked=1)
array_g = np.array(g).flatten()
plt.hist(array_g, bins=256, alpha=0.5, density = True, facecolor='g',edgecolor='g',stacked=1)
array_b = np.array(b).flatten()
plt.hist(array_b, bins=256, alpha=0.5, density = True, facecolor='b',edgecolor='b')
plt.show()

print('------------------------------------------------------------')	#60個

import torchvision.transforms as transforms

from PIL import Image

print('------------------------------------------------------------')	#60個

"""
from PIL import Image,ImageDraw
image = Image.open("captcha.png").convert("L")	#轉換成灰階圖像
"""


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


#PIL之基本設定


""" not ready
from PIL import Image, ImageDraw, ImageFont

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.jpg'
im = Image.open(filename1)

filename2 = 'C:/_git/vcs/_1.data/______test_files2/picture1_partial.jpg'
image3 = image1.resize((100, 500), Image.ANTIALIAS)
image = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

"""

print('------------------------------------------------------------')	#60個

#PIL 偽彩色圖像處理

from PIL import Image

print('------------------------------------------------------------')	#60個

#filename = 'C:/_git/vcs/_1.data/______test_files1/pic_256X100.png'
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image = Image.open(filename)

#彩色轉黑白
# 轉換為灰度圖像
gray_image = image.convert('L')

#3. 偽彩色處理

#偽彩色處理可以通過將灰度值映射到彩色值來實現。通常，我們使用一個顏色映射表（Color Map）來定義灰度和彩色之間的映射關系。
#在Python中，可以使用matplotlib庫來生成顏色映射表并將灰度圖像轉換為彩色圖像。

# 定義顏色映射表
cmap = plt.get_cmap('jet')

# 將灰度圖像轉換為彩色圖像
color_image = cmap(np.array(gray_image))

# 顯示彩色圖像
plt.imshow(color_image)
plt.axis('off')
plt.show()

#上述代碼中，我們使用get_cmap方法獲取了一個名為’jet’的顏色映射表。然后，將灰度圖像轉換為NumPy數組，再將數組應用于顏色映射表，得到彩色圖像。


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個



filename1 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/red_300X300.bmp'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

filename1 = 'C:/_git/vcs/_1.data/______test_files1/picture2.jpg'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/picture1.bmp'

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
imagehash.whash(img, mode='db4')
colorhash:      HSV color hash
hashmethod == 'crop-resistant':
crop-resistant: Crop-resistant hash
imagehash.crop_resistant_hash
"""

from PIL import Image
import imagehash

hash1 = imagehash.average_hash(Image.open(filename1))
print(hash1)
hash2 = imagehash.average_hash(Image.open(filename2))
print(hash2)

if hash1 == hash2:
    print('兩圖相同')
else:
    print('兩圖不同')

print('------------------------------------------------------------')	#60個

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/green_300X300.bmp'

#純圖片指定座標取得顏色方法
def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    a = (r, g, b)
    return a

print(rgb_of_pixel(filename, 131, 81))

print("------------------------------------------------------------")  # 60個

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

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff0000")  # 產生 RGB 色域，400x300 背景紅色的圖片
bg.save("oxxostudio.jpg")
# bg.show()  # Colab 不支援直接顯示，如果使用本機環境會開啟圖片檢視器


print("------------------------------------------------------------")  # 60個

from PIL import Image

bg = Image.new("RGB", (400, 300), "#ff000055")  # 產生 RGBA 色域，400x300 背景半透明紅色的圖片
bg.save("oxxostudio.png")

print("------------------------------------------------------------")  # 60個

# Pytesseract 辨識圖片中的文字

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

print("------------------------------------------------------------")  # 60個

from PIL import Image
from PIL import ImageColor

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'

print('------------------------------------------------------------')	#60個

print(ImageColor.getrgb("#0000ff"))
print(ImageColor.getrgb("rgb(0, 0, 255)"))
print(ImageColor.getrgb("rgb(0%, 0%, 100%)"))
print(ImageColor.getrgb("Blue"))
print(ImageColor.getrgb("blue"))

print('------------------------------------------------------------')	#60個

print(ImageColor.getcolor("#0000ff", "RGB"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGB"))
print(ImageColor.getcolor("Blue", "RGB"))
print(ImageColor.getcolor("#0000ff", "RGBA"))
print(ImageColor.getcolor("rgb(0, 0, 255)", "RGBA"))
print(ImageColor.getcolor("Blue", "RGBA"))

print('------------------------------------------------------------')	#60個

image = Image.open(filename)       # 建立Pillow物件
print("列出物件檔名 : ", image.filename)
print("列出物件副檔名 : ", image.format)
print("列出物件描述   : ", image.format_description)
print("列出物件型態 : ", type(image))
width, height = image.size               # 獲得影像寬度和高度
print("寬度 = ", width)
print("高度 = ", height)

#print(image.mode)
#print(image.size)

plt.imshow(image)
plt.show()


image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ',image.size)
print('圖片的寬度，單位像素(pixels): ',image.width)
print('圖片的高度，單位像素(pixels): ',image.height)

image = Image.open(filename)
print('圖檔格式: ', image.format)
print('圖檔的色彩模式: ', image.mode)
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
print(image.format)
print(image.mode)
print(image.width)
print(image.height)
print(image.size)

print('------------------------------------------------------------')	#60個

image = Image.new("RGB", (300, 180), "aqua")  # 建立aqua顏色影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

image = Image.new("RGBA", (300, 180))     # 建立完全透明影像
plt.imshow(image)
plt.show()

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 100), "Yellow")
print(newImage.getpixel((150, 50)))      # 列印中心點的色彩
newImage.save("tmp_pic13.png")

print("------------------------------------------------------------")  # 60個

newImage = Image.new('RGBA', (300, 300), "Yellow")
for x in range(50, 251):                                # x軸區間在50-250
    for y in range(50, 151):                            # y軸區間在50-150
        newImage.putpixel((x, y), (0, 255, 255, 255))   # 填青色

newImage.save("tmp_pic14.png")                         # 第一階段存檔

for x in range(50, 251):                                # x軸區間在50-250            
    for y in range(151, 251):                           # y軸區間在151-250
        newImage.putpixel((x, y), ImageColor.getcolor("Blue", "RGBA"))

newImage.save("tmp_pic15.png")                         # 第一階段存檔

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
width, height = image.size

newPict1 = image.resize((width*2, height))   # 寬度是2倍
plt.imshow(newPict1)
plt.show()

newPict2 = image.resize((width, height*2))   # 高度是2倍
plt.imshow(newPict2)
plt.show()


print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
image090=image.rotate(90)  # 旋轉90度
image180=image.rotate(180)  # 旋轉180度
image270=image.rotate(270)  # 旋轉270度

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                       # 建立Pillow物件
image45a=image.rotate(45)  # 旋轉45度
image45b=image.rotate(45, expand=True)  # 旋轉45度圖像擴充

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)                     # 建立Pillow物件
image_flip1 = image.transpose(Image.FLIP_LEFT_RIGHT)  # 左右
image_flip2 = image.transpose(Image.FLIP_TOP_BOTTOM)  # 上下

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
cropPict = image.crop((80, 30, 150, 100))   # 裁切區間
cropPict.save("tmp_pic16.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)           # 建立Pillow物件
copyPict = image.copy()                      # 複製
copyPict.save("tmp_pic17.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
copyPict.paste(cropPict, (20, 20))              # 第一次合成
copyPict.paste(cropPict, (20, 100))             # 第二次合成
copyPict.save("tmp_pic18.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)               # 建立Pillow物件
copyPict = image.copy()                          # 複製
cropPict = copyPict.crop((80, 30, 150, 100))    # 裁切區間
cropWidth, cropHeight = cropPict.size           # 獲得裁切區間的寬與高

width, height = 600, 320                        # 新影像寬與高
newImage = Image.new('RGB', (width, height), "Yellow")  # 建立新影像
for x in range(20, width-20, cropWidth):         # 雙層迴圈合成
    for y in range(20, height-20, cropHeight):
        newImage.paste(cropPict, (x, y))        # 合成

newImage.save("tmp_pic19.jpg")                   # 儲存

print("------------------------------------------------------------")  # 60個

from PIL import ImageFilter

image = Image.open(filename)       # 建立Pillow物件
filterPict = image.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic20_BLUR.jpg")

filterPict = image.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic21_CONTOUR.jpg")

filterPict = image.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic22_EMBOSS.jpg")

filterPict = image.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic23_FIND_EDGES.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

newImage = Image.new('RGBA', (300, 300), "Yellow")  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

# 繪製點
for x in range(100, 200, 3):
    for y in range(100, 200, 3):
        drawObj.point([(x,y)], fill='Green')

# 繪製線條, 繪外框線
drawObj.line([(0,0), (299,0), (299,299), (0,299), (0,0)], fill="Black")
# 繪製右上角美工線
for x in range(150, 300, 10):
    drawObj.line([(x,0), (300,x-150)], fill="Blue")
# 繪製左下角美工線
for y in range(150, 300, 10):
    drawObj.line([(0,y), (y-150,300)], fill="Blue")    
newImage.save("tmp_pic24.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
# fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36) 找不到字形
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
fontInfo = ImageFont.truetype(font_filename, 36)

drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\ebas927.ttf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

#fontInfo = ImageFont.truetype('C:\Windows\Fonts\DFZongYiStd-W9.otf', 48)
#drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)

newImage.save("tmp_pic26.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw, ImageFont

newImage = Image.new('RGBA', (600, 300), 'Yellow')  # 建立300*300黃色底的影像
drawObj = ImageDraw.Draw(newImage)

strText = 'Welcome to the United States'        # 設定欲列印英文字串
drawObj.text((50,50), strText, fill='Blue')         # 使用預設字型與字型大小

# 使用古老英文字型, 字型大小是36
#fontInfo = ImageFont.truetype('C:\Windows\Fonts\OLDENGL.TTF', 36)
font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
fontInfo = ImageFont.truetype(font_filename, 36)

drawObj.text((50,100), strText, fill='Blue', font=fontInfo)
# 使用Microsoft所提供的新細明體中文字型處理中文字體
strCtext = '歡迎來到美國'                           # 設定欲列印中文字串
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 48)
drawObj.text((50,180), strCtext, fill='Blue', font=fontInfo)
newImage.save("tmp_pic27.png")

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageFilter

image = Image.open(filename)
width, height = image.size

"""
image.show()
image.transpose(Image.FLIP_LEFT_RIGHT).show()
image.filter(ImageFilter.GaussianBlur(4)).show()
image.filter(ImageFilter.EMBOSS).show()
image.thumbnail((width // 4, height // 4))
image.show()
"""

print('------------------------------------------------------------')	#60個

#filter
from PIL import Image,ImageFilter
image=Image.open(filename)
image2=image.filter(ImageFilter.EDGE_ENHANCE)
#image2.show()

print('------------------------------------------------------------')	#60個

#crop
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 300
    image2 = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image2.size)
    image2.save("tmp_pic29.jpg")

print('------------------------------------------------------------')	#60個

#rotate0
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image2.save("tmp_pic30.jpg")

print('------------------------------------------------------------')	#60個

# rotate1
with Image.open(filename) as image:
  image2 = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image2.save( "tmp_pic31_rotate.jpg")

print('------------------------------------------------------------')	#60個

# resize
with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image2 = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image2.size)
    image2.save("tmp_pic31_resize.jpg" )

print('------------------------------------------------------------')	#60個

#sharpness
from PIL import Image,ImageEnhance
with Image.open(filename) as image:
    image2 = ImageEnhance.Contrast(image).enhance(0.3)
    image2.save("tmp_pic32_contrast.jpg") 

print('------------------------------------------------------------')	#60個

# transpose
from PIL import Image,ImageEnhance
with Image.open(filename) as image:
    image2 = image.transpose(Image.FLIP_LEFT_RIGHT)
    image2.save( "tmp_pic33b.jpg")
    image2 = image.transpose(Image.FLIP_TOP_BOTTOM)
    image2.save( "tmp_pic33c.jpg")
    image2 = image.transpose(Image.ROTATE_90)
    image2.save( "tmp_pic33d.jpg")
    image2 = image.transpose(Image.ROTATE_180)
    image2.save( "tmp_pic33e.jpg")
    image2 = image.transpose(Image.ROTATE_270)
    image2.save( "tmp_pic33f.jpg")
    image2 = image.transpose(Image.TRANSPOSE)
    image2.save( "tmp_pic33g.jpg")
    image2 = image.transpose(Image.TRANSVERSE)
    image2.save( "tmp_pic33h.jpg")

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400,300), '#00FF00')
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400,300))
draw=ImageDraw.Draw(image)
draw.ellipse([(100,100),(320,200)], fill=(255,255,0,255))
#image.show()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
pic=image.convert("1")
#pic.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    x1 = 250
    y1 = 350
    image_new = image.crop((x, y, x1, y1))
    print(image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Brightness(image).enhance(2.5)
    image_new.save("tmp_pic_brightness.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter

image = Image.open(filename)
image_new = image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print(image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save("tmp_pic_view_resize.jpg" )

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save("tmp_pic_rotate180.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate111.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save("tmp_pic_rotate000.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose90.jpg")
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transposeLR.jpg")

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
image.save("tmp_pic_quality95.jpg", quality=95 )
image.close()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
image.save("tmp_pic_quality_default.jpg")
image.close()

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageDraw,ImageFont

image=Image.open(filename)
imfont=ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf",120)
draw=ImageDraw.Draw(image)
draw.text((50,50),"牡丹亭",font=imfont,fill=(0,255,255,255))
#image.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

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

#Pillow：基本繪圖

from PIL import Image, ImageDraw

#繪直線

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.line([40,50,360,280], fill="blue", width=3)

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個


#繪矩形

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.rectangle((100,80,300,240), fill="yellow", outline="black")

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪點

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.point([(100,100), (100,101), (100,102)], fill='red')

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪圓或橢圓

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.ellipse((50,50,350,250), fill="purple", outline="green")

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#繪多邊形

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.polygon([(200,40),(60,250),(320,250)], fill="brown", outline="red")

plt.imshow(image)

plt.show()


print('------------------------------------------------------------')	#60個

#繪文字

from PIL import ImageFont

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((150,80), "font demo", fill="red")  #繪英文文字

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
myfont = ImageFont.truetype(font_filename, 24)

draw_image.text((120,150),"雅黑字體示範", fill="blue", font=myfont)  #繪中文 

plt.imshow(image)

plt.show()

#繪文字

from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (400,300), "lightgray")

draw_image = ImageDraw.Draw(image)

draw_image.text((120,80), "English Demo", fill="red")  #繪製英文文字

myfont = ImageFont.truetype(font_filename, 24)

draw_image.text((120,150), "中文字型示範", fill="blue", font=myfont) #繪製中文文字

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

#Pillow：繪圖範例

from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGB", (300,400), "lightgray")

draw_image = ImageDraw.Draw(image)

#繪圓
draw_image.ellipse((50,50,250,250), width=3, outline="gold")# 臉

#繪多邊形
draw_image.polygon([(100,90), (120,130), (80,130)], fill="brown", outline="red") #左眼精
draw_image.polygon([(200,90), (220,130), (180,130)],   fill="brown", outline="red")#右眼精

#繪矩形
draw_image.rectangle((140,140,160,180),    fill="blue", outline="black") #鼻子

#繪橢圓
draw_image.ellipse((100,200,200,220), fill="red") #嘴巴   

#繪文字
draw_image.text((130,280), "ABCDEFG", fill="orange")  #英文字

myfont = ImageFont.truetype(font_filename, 16)

draw_image.text((110,320), "測試使用中文字", fill="red", font=myfont) #中文字 

plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

"""
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
            thumbnail.save(os.path.join(target, targetfile))
            image.close()
            thumbnail.close()
            print("{}-->{}".format(file, targetfile))
    else:
        print("目標資料夾已存在，無法進行。")
else:    
    print("找不到來源資料夾。")
"""
print("------------------------------------------------------------")  # 60個

import os

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
            thumbnail.save(os.path.join(target, targetfile))
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

import os

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
            thumbnail.save(os.path.join(target, targetfile))
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

def blue_to_red(image_path):
    image = Image.open(image_path)
    r, g, b = image.split() # 分離三個通道
    image = Image.merge("RGB",(b,g,r))# 將藍色通道和通道互換
    image.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
#blue_to_red(filename)

print('------------------------------------------------------------')	#60個

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
    
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
blue_to_red2(filename)
"""    

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 300))
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw

image = Image.new("RGB", (400, 300), '#00FF00')
draw = ImageDraw.Draw(image)
draw.ellipse([(100, 100), (320, 200)], fill = (255, 255, 0, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    x = 50
    y = 50
    w = 200
    h = 200
    image_new = image.crop((x, y, w, h))
    print(image_new.size)
    image_new.save('tmp_pic_crop.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageEnhance

with Image.open(filename) as image:
   image_new = ImageEnhance.Brightness(image).enhance(2.5)
   image_new.save('tmp_pic_brightness.jpg')

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageFilter

image = Image.open(filename)
plt.imshow(image)
plt.title('原圖')
plt.show()

new = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(new)
plt.title('after filter')
plt.show()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
pic = image.convert("1")
plt.imshow(pic)
plt.title('convert L')
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    print(image.size)
    w = 200
    r = w/image.size[0]
    h = int(image.size[1]*r) #依縮放比例計算高度
    image_new = image.resize((w, h))
    print(image_new.size)
    image_new.save('tmp_pic_resize.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(180)
    image_new.save('tmp_pic_rotate.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 1, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30.jpg')

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.rotate(30, Image.BILINEAR, 0, None, None, '#ffff66')
    image_new.save('tmp_pic_rotate30_zero.jpg')

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save('tmp_pic_normal.jpg')
image.close()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save('tmp_pic_high.jpg', quality = 95)
image.close()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageDraw, ImageFont

image = Image.open(filename)
imfont = ImageFont.truetype("C:\\Windows\\Fonts\\Arial\\arial.ttf", 40)
draw = ImageDraw.Draw(image)
draw.text((100, 100), 'Peony', font = imfont, fill = (0, 255, 255, 255))
plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個

with Image.open(filename) as image:
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save('tmp_pic_rotate_90.jpg')
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save('tmp_pic_flip.jpg')

print('------------------------------------------------------------')	#60個

print('保持圖片原始大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,0,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60a.jpg")

print("------------------------------------------------------------")  # 60個

print('保持圖片內容大小之旋轉')
with Image.open(filename) as image:
  image_new = image.rotate(60,Image.BILINEAR,1,None,None,'#BBCC55')
  image_new.save("tmp_pic_rotate60b.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    x = 50
    y = 50
    x1 = 150
    y1 = 200
    image_new = image.crop((x, y, x1, y1))
    print('圖片經裁切後的尺寸大小:', image_new.size)
    image_new.save("tmp_pic_crop.jpg")

print("------------------------------------------------------------")  # 60個

with Image.open(filename) as image:
    print('原圖片的尺寸大小:',image.size)
    w=100
    r = w/image.size[0]
    h = int(image.size[1]*r)
    image_new = image.resize((w, h))
    print('圖片經縮放後的尺寸大小:',image_new.size)
    image_new.save("tmp_pic_resize.jpg" )

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = ImageEnhance.Contrast(image).enhance(0.3)
    image_new.save("tmp_pic_contrast.jpg") 

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageEnhance

with Image.open(filename) as image:
    image_new = image.transpose(Image.FLIP_LEFT_RIGHT)
    image_new.save("tmp_pic_transpose1.jpg")
    image_new = image.transpose(Image.FLIP_TOP_BOTTOM)
    image_new.save("tmp_pic_transpose2.jpg")
    image_new = image.transpose(Image.ROTATE_90)
    image_new.save("tmp_pic_transpose3.jpg")
    image_new = image.transpose(Image.ROTATE_180)
    image_new.save("tmp_pic_transpose4.jpg")
    image_new = image.transpose(Image.ROTATE_270)
    image_new.save("tmp_pic_transpose5.jpg")
    image_new = image.transpose(Image.TRANSPOSE)
    image_new.save("tmp_pic_transpose6.jpg")
    image_new = image.transpose(Image.TRANSVERSE)
    image_new.save("tmp_pic_transpose7.jpg")

print("------------------------------------------------------------")  # 60個

from PIL import Image,ImageFilter

image=Image.open(filename)
image_new=image.filter(ImageFilter.EDGE_ENHANCE)
#image_new.show()

print("------------------------------------------------------------")  # 60個
"""
print("車牌")
import pytesseract
text = pytesseract.image_to_string(Image.open('data/atq9305.jpg'))
print(type(text), "   ", text)

print("------------------------------------------------------------")  # 60個

import pytesseract
import time

carDict = {}
myPath = "C:\\_git\\vcs\\_4.python\\PIL\\new1\\"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        carDict[keyText] = entryTime

print("------------------------------------------------------------")  # 60個


"""
from PIL import Image
import pytesseract
import time

carDict = {}
myPath = "foldername"
while True:
    carPlate = input("請掃描或輸入車牌(Q/q代表結束) : ")
    if carPlate == 'Q' or carPlate == 'q':
        break
    carPlate = myPath + carPlate
    keyText = pytesseract.image_to_string(Image.open(carPlate))    
    if keyText in carDict:
        exitTime = time.asctime()
        print("車輛出場時間 : ", keyText, ":", exitTime)
        exitSecond = time.time()
        dxSecond = exitSecond - carDict[keyText]
        hour = dxSecond % 3600          # 由餘數判斷是否進位
        hours = dxSecond // 3600        # 計算小時數
        if hour != 0:
            hours += 1
        print("停車費用 : ", hours * 60, " 元 ")
        del carDict[keyText]
    else:
        entryTime = time.asctime()
        print("車輛入場時間 : ", keyText, ":", entryTime)
        entrySecond = time.time()
        carDict[keyText] = entrySecond
"""
print("------------------------------------------------------------")  # 60個

import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_26.jpg'),
                                    lang='chi_tra')
print(text)

print("------------------------------------------------------------")  # 60個

import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_27.jpg'),
                                               lang='chi_sim')
print(text)
"""
print("------------------------------------------------------------")  # 60個

"""
import os

def batch_resize_images(input_folder, output_folder, size=(300, 300)):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍歷輸入資料夾中的所有影像檔案
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.png')):
            # 打開影像
            image = Image.open(os.path.join(input_folder, filename))
            # 調整影像尺寸
            image = image.resize(size, Image.ANTIALIAS)
            # 保存調整尺寸後的影像到輸出資料夾
            image.save(os.path.join(output_folder, filename))

# 假設有一個包含原始圖片的資料夾 'input_images' 和
# 一個用於存放調整後圖片的資料夾 'output_images'
input_folder = 'input_images'
output_folder = 'output_images'

# 呼叫函數，將所有圖片調整為300x300大小
batch_resize_images(input_folder, output_folder)
"""
print("------------------------------------------------------------")  # 60個

"""
import os

def batch_convert_images(directory, target_format='.jpg'):
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            path = os.path.join(directory, filename)
            image = Image.open(path)
            image_rgb = image.convert('RGB')  # 轉換為RGB模式以便保存為JPEG
            image_rgb.save(path.replace('.png', target_format), quality=95)

# 呼叫批次更改函數
batch_convert_images('images_directory')
"""

print("------------------------------------------------------------")  # 60個

"""
from PIL import Image, ImageDraw, ImageFont

def generate_product_image(product_image_path, background_image_path, promo_text):
    # 加載產品和背景影像
    product_image = Image.open(product_image_path).resize((200, 200))
    background_image = Image.open(background_image_path)
    # 在背景影像上放置產品影像
    background_image.paste(product_image, (50, 50), product_image)
    # 在影像上添加促銷文字
    draw = ImageDraw.Draw(background_image)
    font = ImageFont.truetype("arial.ttf", size=45)
    draw.text((50, 260), promo_text, font=font, fill="white")
    # 保存或返回影像
    background_image.save('output_promo_image.jpg')

generate_product_image('product.png', 'background.jpg', '特價促銷!')
"""
print("------------------------------------------------------------")  # 60個



filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image

hungPic = Image.open(filename)        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 600
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))
newImage.save("tmp_pic_2.jpg")

print("------------------------------------------------------------")  # 60個

"""
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_10.jpg'),
                                               lang='chi_sim')
print(text)
with open('tmp_17_10.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)
"""

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

from PIL import Image
from PIL import ImageFilter
rushMore = Image.open(filename)       # 建立Pillow物件
filterPict = rushMore.filter(ImageFilter.BLUR)
filterPict.save("tmp_pic_4_BLUR.png")
filterPict = rushMore.filter(ImageFilter.CONTOUR)
filterPict.save("tmp_pic_4_CONTOUR.png")
filterPict = rushMore.filter(ImageFilter.DETAIL)
filterPict.save("tmp_pic_4_DETAIL.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE.png")
filterPict = rushMore.filter(ImageFilter.EDGE_ENHANCE_MORE)
filterPict.save("tmp_pic_4_EDGE_ENHANCE_MORE.png")
filterPict = rushMore.filter(ImageFilter.EMBOSS)
filterPict.save("tmp_pic_4_EMBOSS.png")
filterPict = rushMore.filter(ImageFilter.FIND_EDGES)
filterPict.save("tmp_pic_4_FIND_EDGES.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH)
filterPict.save("tmp_pic_4_SMOOTH.png")
filterPict = rushMore.filter(ImageFilter.SMOOTH_MORE)
filterPict.save("tmp_pic_4_SMOOTH_MORE.png")
filterPict = rushMore.filter(ImageFilter.SHARPEN)
filterPict.save("tmp_pic_4_SHARPEN.png")

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from PIL import Image, ImageDraw, ImageFont

hungPic = Image.open(filename)        # 建立Pillow物件
newPic = hungPic.resize((350,500))

nwidth, nheight = 450, 700
newImage = Image.new('RGB', (nwidth, nheight), "Yellow")

newImage.paste(newPic, (50,50))

drawObj = ImageDraw.Draw(newImage)
name = "牡丹亭"
fontInfo = ImageFont.truetype('C:\Windows\Fonts\mingliu.ttc', 60)
drawObj.text((140,600), name, fill='Blue', font=fontInfo)

newImage.save("tmp_pic_6.jpg")

print("------------------------------------------------------------")  # 60個



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





"""

#另存新檔
image.save("tmp_pic_01.png")
#image.show()





"""

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


