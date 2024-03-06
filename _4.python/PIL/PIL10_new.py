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

#例2：將lena圖像二值化，像素值大于128的變為1，否則變為0

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

import torchvision.transforms as transforms

from PIL import Image

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




print("------------------------------------------------------------")  # 60個


