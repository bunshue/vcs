"""
PIL 基本使用

顯示圖片

顯示圖片訊息

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
'''
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

'''


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


"""
PIL 新進

"""

import numpy as np
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt

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


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


"""
PIL 偽彩色圖像處理

"""

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

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


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個






print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


