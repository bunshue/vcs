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
plt.show()

"""

2、通道分離與合并
"""

img=Image.open(filename)  #打開圖像
gray=img.convert('L')   #轉換成灰度
r,g,b=img.split()   #分離三通道
pic=Image.merge('RGB',(r,g,b)) #合并三通道
plt.figure('Peony')
plt.subplot(2,3,1)
plt.title('origin')
plt.imshow(img)
plt.subplot(2,3,2)
plt.title('gray')
plt.imshow(gray,cmap='gray')
plt.subplot(2,3,3)
plt.title('merge')
plt.imshow(pic)
plt.subplot(2,3,4)
plt.title('r')
plt.imshow(r,cmap='gray')
plt.subplot(2,3,5)
plt.title('g')
plt.imshow(g,cmap='gray')
plt.subplot(2,3,6)
plt.title('b')
plt.imshow(b,cmap='gray')
plt.show()

"""
圖像中的像素訪問

前面的一些例子中，我們都是利用Image.open（）來打開一幅圖像，然後直接對這個PIL對象進行操作。如果只是簡單的操作還可以，但是如果操作稍微復雜一些，就比較吃力了。因此，通常我們加載完圖片後，都是把圖片轉換成矩陣來進行更加復雜的操作。

python中利用numpy庫和scipy庫來進行各種數據操作和科學計算。我們可以通過pip來直接安裝這兩個庫

pip install numpy
pip install scipy

"""

img=np.array(Image.open(filename))  #打開圖像并轉化為數字矩陣
plt.figure('Peony')
plt.imshow(img)
plt.show()

"""

調用numpy中的array（）函數就可以將PIL對象轉換為數組對象。

查看圖片信息，可用如下的方法：

print img.shape  
print img.dtype 
print img.size 
print type(img)

如果是RGB圖片，那么轉換為array之後，就變成了一個rows*cols*channels的三維矩陣,因此，我們可以使用

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
plt.show()

"""
如果要對多個像素點進行操作，可以使用數組切片方式訪問。切片方式返回的是以指定間隔下標訪問 該數組的像素值。下面是有關灰度圖像的一些例子：
復制代碼

img[i,:] = im[j,:] # 將第 j 行的數值賦值給第 i 行

img[:,i] = 100 # 將第 i 列的所有數值設為 100

img[:100,:50].sum() # 計算前 100 行、前 50 列所有數值的和

img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean() # 第 i 行所有數值的平均值

img[:,-1] # 最後一列

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
plt.show()

#上述代碼中，我們使用get_cmap方法獲取了一個名為’jet’的顏色映射表。然後，將灰度圖像轉換為NumPy數組，再將數組應用于顏色映射表，得到彩色圖像。

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'
font_filename = 'C:/_git/vcs/_1.data/______test_files5/taipei_sans_tc_beta.ttf'

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
print('圖檔大小尺寸，寬度跟高度值，格式是元組(tuple): ', image.size)
print('圖片的寬度，單位像素(pixels): ', image.width)
print('圖片的高度，單位像素(pixels): ', image.height)

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save("tmp_pic_quality95.jpg", quality=95 )
image.close()

print("------------------------------------------------------------")  # 60個

image = Image.open(filename)
image.save("tmp_pic_quality_default.jpg")
image.close()

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

image = Image.open(filename)
image.save('tmp_pic_normal.jpg')
image.close()

print('------------------------------------------------------------')	#60個

image = Image.open(filename)
image.save('tmp_pic_high.jpg', quality = 95)
image.close()

print('------------------------------------------------------------')	#60個

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
from PIL import Image
import pytesseract

text  = pytesseract.image_to_string(Image.open('data/data17_10.jpg'),
                                               lang='chi_sim')
print(text)
with open('tmp_17_10.txt', 'w', encoding='utf-8') as fn:
    fn.write(text)
"""

print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = "C:/_git/vcs/_1.data/______test_files1/elephant.jpg"

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("操作像素")

image = Image.open(filename)
for x in range(100, 200):
    for y in range(250, 350):
        image.putpixel((x, y), (128, 128, 128))
image.show()

print('------------------------------------------------------------')	#60個

from PIL import Image, ImageOps
from IPython.display import display

#利用圖片大小強調數量多寡
#載入圖片與顯示圖片的範例

im = Image.open(filename)
display(im)

print('------------------------------------------------------------')	#60個


from pathlib import Path
from PIL import Image

infolder = "testfolder"
value1 = "outputfolder4"
extlist = ["*.jpg","*.png"]

#【函數: 轉存為jpg檔案】
def savepng(readfile, savefolder):
    try:
        img = Image.open(readfile)              #載入圖片檔
        savedir = Path(savefolder)
        savedir.mkdir(exist_ok=True)            #建立轉存資料夾
        #-----------------------------------
        filename = Path(readfile).stem+".jpg"   #建立檔案名稱
        savepath = savedir.joinpath(filename)
        if img.format == "PNG":
            newimg = Image.new("RGB", img.size, "white")
            newimg.paste(img, mask=img.split()[3])  #在白底背景繪製圖片
            newimg.save(savepath, format="JPEG", quality=95)    #轉存為JPG圖檔
        elif img.format == "JPEG":
            img.save(savepath, format="JPEG", quality=95)   #轉存為JPG圖檔
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

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

infile = filename#"earth.png"
savefile = "tmp_saveJPG2.jpg"

img = Image.open(infile)
if img.format == "PNG":
    newimg = Image.new("RGB", img.size, "WHITE")
    newimg.paste(img, mask=img)             # 將PNG檔壓在白底圖片上
    newimg.save(savefile, format="JPEG")    # JPG轉存檔案
elif img.format == "JPEG":
    img.save(savefile, format="JPEG")       # JPG轉存檔案

print("------------------------------------------------------------")  # 60個






print('------------------------------------------------------------')	#60個

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

from PIL import Image

img1 = Image.new("RGB",(300,200),"rgb(0,0,255)") #藍色
img1.save("tmp_blue.jpg")

img2 = Image.new("RGBA",(300,200),"rgba(0,0,255,0)") #透明
img2.save("tmp_alpha.png")

print('------------------------------------------------------------')	#60個

#利用圖片的個數強調數量

#以人形圖示的個數強調數量的範例


# 要排列的圖示個數
num = 10

# 圖片之間的邊界
margin = 5

# 載入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'

im = Image.open(filename)#"human.png"
im_width, im_height = im.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((im_width + margin) * num, im_height))
for i in range(num):
    canvas.paste(im, ((im_width + margin) * i, 0))

canvas

print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個





# 1 open save show

from PIL import Image

filename = 'C:/_git/vcs/_1.data/______test_files1/elephant.jpg'
infile = filename#"earth.png"
savefile = "tmp_savePNG1.png"

img = Image.open(infile)      #載入圖片檔
img.save(savefile, format="PNG")    #PNG轉存檔案

print('------------------------------------------------------------')	#60個

from PIL import Image

plt.figure('影像處理1', figsize = (10, 6))

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = Image.open(filename)
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(121)
plt.title(u'原圖')
plt.imshow(image)

image = Image.open(filename).convert('L')

plt.subplot(122)
plt.title(u'灰度圖')
plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

print("PIL_hist")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 打開圖像，并轉成灰度圖像
im = np.array(Image.open(filename).convert('L'))

# 新建一個圖像
plt.figure()
plt.subplot(121)

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

# 在原點的左上角顯示輪廓圖像
plt.contour(im, origin='image')
plt.axis('equal')
plt.title(u'圖像輪廓圖')

plt.subplot(122)
# 利用hist來繪制直方圖
# 第一個參數為一個一維數組
# 因為hist只接受一維數組作為輸入，所以要用flatten()方法將任意數組按照行優先準則轉化成一個一維數組
# 第二個參數指定bin的個數
plt.hist(im.flatten(), 128)
plt.title(u'圖像直方圖')
#刻度
plt.xlim([0-10,255+10])
plt.ylim([0,8000])

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_histeq")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

#from PCV.tools import imtools

# 添加中文字體支持
from matplotlib.font_manager import FontProperties

im = np.array(Image.open(filename).convert('L'))
# 打開圖像，并轉成灰度圖像
#im2, cdf = imtools.histeq(im)

plt.figure()

plt.subplot(2, 2, 1)
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.title(u'原始圖像')
plt.imshow(im)

plt.subplot(2, 2, 2)
plt.title(u'直方圖均衡化後的圖像')
#plt.imshow(im2)
plt.subplot(2, 2, 3)
plt.title(u'原始直方圖')
plt.hist(im.flatten(), 128, density=True)
plt.subplot(2, 2, 4)
plt.title(u'均衡化後的直方圖')
#plt.hist(im2.flatten(), 128, density=True)

plt.show()

print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im=np.array(Image.open(filename).convert('L'))
print(int(im.min()),int(im.max()))

im2=255-im               #對圖像進行反向處理
print('對圖像進行反向處理:\n',int(im2.min()),int(im2.max())) #查看最大/最小元素

im3=(100.0/255)*im+100   #將圖像像素值變換到100...200區間
print('將圖像像素值變換到100...200區間:\n',int(im3.min()),int(im3.max()))

im4=255.0*(im/255.0)**2  #對像素值求平方後得到的圖像
print('對像素值求平方後得到的圖像:\n',int(im4.min()),int(im4.max()))

plt.figure('影像處理2', figsize = (10, 6))
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示

plt.subplot(131)
plt.imshow(im2)
plt.title(r'$f(x)=255-x$')

plt.subplot(132)
plt.imshow(im3)
plt.title(r'$f(x)=\frac{100}{255}x+100$')

plt.subplot(133)
plt.imshow(im4)
plt.title(r'$f(x)=255(\frac{x}{255})^2$')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_mean")

from PIL import ImageStat

def darkchannel(input_img,h,w):
    dark_img = Image.new("L",(h,w),0)
    for x in range(0,h-1):
        for y in range(0,w-1):
            dark_img.putpixel((x,y),min(input_img.getpixel((x,y))))
    return dark_img
  
def airlight(input_img,h,w):
    nMinDistance=65536    
    w=int(round(w/2))
    h=int(round(h/2))
    if h*w>200:
        lu_box = (0, 0, w, h) 
        ru_box = (w, 0, 2*w, h) 
        lb_box = (0, h, w, 2*h) 
        rb_box = (w, h, 2*h,2*w)  
               
        lu = input_img.crop(lu_box);
        ru = input_img.crop(ru_box);
        lb = input_img.crop(lb_box);
        rb = input_img.crop(rb_box);
        lu_m=ImageStat.Stat(lu)
        ru_m=ImageStat.Stat(ru)
        lb_m=ImageStat.Stat(lb)
        rb_m=ImageStat.Stat(rb)
        lu_mean = lu_m.mean
        ru_mean = ru_m.mean
        lb_mean = lb_m.mean
        rb_mean = rb_m.mean
        lu_stddev = lu_m.stddev
        ru_stddev = ru_m.stddev
        lb_stddev = lb_m.stddev
        rb_stddev = rb_m.stddev 
        score0 = lu_mean[0]+lu_mean[1]+lu_mean[2] - lu_stddev[0]-lu_stddev[1]-lu_stddev[2]
        score1 = ru_mean[0]+ru_mean[1]+lu_mean[2] - ru_stddev[0]-ru_stddev[1]-ru_stddev[2]  
        score2 = lb_mean[0]+lb_mean[1]+lb_mean[2] - lb_stddev[0]-lb_stddev[1]-lb_stddev[2]
        score3 = rb_mean[0]+rb_mean[1]+rb_mean[2] - rb_stddev[0]-rb_stddev[1]-rb_stddev[2]
        x =max(score0,score1,score2,score3)       
        if x == score0:
             air =airlight(lu,h,w)
        if x == score1:
             air =airlight(ru,h,w)
        if x == score2:
             air =airlight(lb,h,w)
        if x == score3:
             air =airlight(rb,h,w)
    else:
        for i in range(0,h-1):
            for j in range(0,w-1):
                temp=input_img.getpixel((i,j))            
                distance = ((255 - temp[0])**2 +  (255 - temp[1])**2 + (255 - temp[2])**2)**0.5
                if nMinDistance > distance:
                    nMinDistance = distance;
                    air = temp
    return air

def transmssion(air,dark_img,h,w,OMIGA):
    trans_map=np.zeros((h,w))
    A=max(air)
    for i in range(0,h-1):
        for j in range(0,w-1):
            temp=1-OMIGA*dark_img.getpixel((i,j))/A
            trans_map[i,j]=max(0.1,temp)  
    for i in range(1,h-1):
        for j in range(1,w-1):
                tempup=(trans_map[i-1][j-1]+2*trans_map[i][j-1]+trans_map[i+1][j-1])
                tempmid=2*(trans_map[i-1][j]+2*trans_map[i][j]+trans_map[i+1][j])
                tempdown=(trans_map[i-1][j+1]+2*trans_map[i][j+1]+trans_map[i+1][j+1])
                trans_map[i,j]=(tempup+tempmid+tempdown)/16
    return trans_map
                   
def defog(img,t_map,air,h,w):
    dehaze_img = Image.new("RGB",(h,w),0)
    for i in range(0,h-1):
        for j in range(0,w-1):
            R,G,B=img.getpixel((i,j))
            R=int((R-air[0])/t_map[i,j]+air[0])
            G=int((G-air[1])/t_map[i,j]+air[1])
            B=int((B-air[2])/t_map[i,j]+air[2])
            dehaze_img.putpixel((i,j),(R,G,B)) 
    return dehaze_img                       
                    
filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img=Image.open(filename)
[h,w]=img.size
OMIGA =0.8  
dark_image=darkchannel(img,h,w)
air=airlight(img,h,w)
T_map=transmssion(air,dark_image,h,w,OMIGA)
fogfree_img=defog(img,T_map,air,h,w)

#把結果顯示出來
plt.imshow(fogfree_img)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_operation")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

plt.figure()
# 顯示原圖
image = Image.open(filename)
print(image.mode, image.size, image.format)
plt.subplot(231)
plt.title(u'原圖')
plt.imshow(image)

# 顯示灰度圖
image = Image.open(filename).convert('L')

plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.subplot(232)
plt.title(u'灰度圖')
plt.imshow(image)
# 復制并粘貼區域
image = Image.open(filename)
box = (100, 100, 200, 200)
region = image.crop(box)
region = region.transpose(Image.ROTATE_180)
image.paste(region, box)
plt.subplot(233)
plt.title(u'復制粘貼區域')
plt.imshow(image)

# 縮略圖
image = Image.open(filename)
size = 128, 128
image.thumbnail(size)
print(image.size)
plt.subplot(234)
plt.title(u'縮略圖')
plt.imshow(image)
#image.save('tmp_pic1.jpg')# 保存縮略圖

#調整圖像尺寸
image=Image.open(filename)
image=image.resize(size)
print(image.size)
plt.subplot(235)
plt.title(u'調整尺寸後的圖像')
plt.imshow(image)

#旋轉圖像45°
image=Image.open(filename)
image=image.rotate(45)
plt.subplot(236)
plt.title(u'旋轉45°後的圖像')
plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

print("de_noise")

import random
import cv2
import scipy.misc
import scipy.signal
import scipy.ndimage

"""中值濾波函數"""
def medium_filter(im, x, y, step):
    sum_s=[]
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s.append(im[x+k][y+m])
    sum_s.sort()
    return sum_s[(int(step*step/2)+1)]
"""均值濾波函數"""
def mean_filter(im, x, y, step):
    sum_s = 0
    for k in range(-int(step/2),int(step/2)+1):
        for m in range(-int(step/2),int(step/2)+1):
            sum_s += im[x+k][y+m] / (step*step)
    return sum_s

def convert_2d(r):
    n = 3
    # 3*3濾波器，每個系數都是1/9
    window = np.ones((n, n)) / n**2
    #使用濾波器卷積圖像
    # mode = same 表示輸出尺寸等于輸入尺寸
    # boundary 表示采用對稱邊界條件處理圖像邊緣
    s = scipy.signal.convolve2d(r, window, mode='same', boundary='symm')
    return s.astype(np.uint8)
"""添加噪聲"""
def add_salt_noise(img):
    rows, cols, dims = img.shape 
    R = np.mat(img[:, :, 0])
    G = np.mat(img[:, :, 1])
    B = np.mat(img[:, :, 2])
    Grey_sp = R * 0.299 + G * 0.587 + B * 0.114
    Grey_gs = R * 0.299 + G * 0.587 + B * 0.114
    snr = 0.9
    mu = 0
    sigma = 0.12    
    noise_num = int((1 - snr) * rows * cols)

    for i in range(noise_num):
        rand_x = random.randint(0, rows - 1)
        rand_y = random.randint(0, cols - 1)
        if random.randint(0, 1) == 0:
            Grey_sp[rand_x, rand_y] = 0
        else:
            Grey_sp[rand_x, rand_y] = 255    
    Grey_gs = Grey_gs + np.random.normal(0, 48, Grey_gs.shape)
    Grey_gs = Grey_gs - np.full(Grey_gs.shape, np.min(Grey_gs))
    Grey_gs = Grey_gs * 255 / np.max(Grey_gs)
    Grey_gs = Grey_gs.astype(np.uint8)
    # 中值濾波
    Grey_sp_mf = scipy.ndimage.median_filter(Grey_sp, (8, 8))
    Grey_gs_mf = scipy.ndimage.median_filter(Grey_gs, (8, 8))
    # 均值濾波
    n = 3
    window = np.ones((n, n)) / n ** 2
    Grey_sp_me = convert_2d(Grey_sp)
    Grey_gs_me = convert_2d(Grey_gs)
    plt.subplot(231)
    plt.title('椒鹽噪聲')
    plt.imshow(Grey_sp, cmap='gray')
    plt.subplot(232)
    plt.title('高斯噪聲')
    plt.imshow(Grey_gs, cmap='gray')
    plt.subplot(233)
    plt.title('椒鹽噪聲的中值濾波')
    plt.imshow(Grey_sp_mf, cmap='gray')
    plt.subplot(234)
    plt.title('高斯噪聲的中值濾波')
    plt.imshow(Grey_gs_mf, cmap='gray')
    plt.subplot(235)
    plt.title('椒鹽噪聲的均值濾波')
    plt.imshow(Grey_sp_me, cmap='gray')
    plt.subplot(236)
    plt.title('高斯噪聲的均值濾波')
    plt.imshow(Grey_gs_me, cmap='gray')
    plt.show()

filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/lena_color.png'

img = np.array(Image.open(filename))  #導入圖片
add_salt_noise(img)

print("------------------------------------------------------------")  # 60個

print("PIL_derivative")

#from pylab import *
from scipy.ndimage import  filters
import numpy

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im=np.array(Image.open(filename).convert('L'))
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.subplot(141)
plt.title(u'(a)原圖')
plt.imshow(im)
# sobel算子
imx=np.zeros(im.shape)
filters.sobel(im,1,imx)
plt.subplot(142)
plt.title(u'(b)x方向差分')
plt.imshow(imx)
imy=np.zeros(im.shape)
filters.sobel(im,0,imy)
plt.subplot(143)
plt.title(u'(c)y方向差分')
plt.imshow(imy)
mag=255-np.sqrt(imx**2+imy**2)
plt.subplot(144)
plt.title(u'(d)梯度幅值')
plt.imshow(mag)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_fuzzy")

from scipy.ndimage import filters
from matplotlib.font_manager import FontProperties

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
im=np.array(Image.open(filename).convert('L'))
plt.figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.subplot(141)
plt.title(u'原圖')
plt.imshow(im)
for bi,blur in enumerate([2,4,8]):
    im2=np.zeros(im.shape)
    im2=filters.gaussian_filter(im,blur)
    im2=np.uint8(im2)
    imNum=str(blur)
    plt.subplot(1,4,2+bi)
    plt.title(u'標準差為'+imNum)
    plt.imshow(im2)

#如果是彩色圖像，則分別對三個通道進行模糊
#for bi, blur in enumerate([2,4,8]):
#  im2 = zeros(im.shape)
#  for i in range(3):
#    im2[:, :, i] = filters.gaussian_filter(im[:, :, i], blur)
#  im2 = np.uint8(im2)
#  plt.subplot(1, 4,  2 + bi)
#  plt.imshow(im2)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_gaussian")

from scipy.ndimage import filters

def imx(im, sigma):
    imgx = np.zeros(im.shape)
    filters.gaussian_filter(im, sigma, (0, 1), imgx)
    return imgx
def imy(im, sigma):
    imgy = np.zeros(im.shape)
    filters.gaussian_filter(im, sigma, (1, 0), imgy)
    return imgy
def mag(im, sigma):
    # 還有gaussian_gradient_magnitude()
    imgmag = 255 - numpy.sqrt(imgx ** 2 + imgy ** 2)
    return imgmag

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
im = np.array(Image.open(filename).convert('L'))
plt.figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
sigma = [2, 5, 10]
for i in  sigma:
    plt.subplot(3, 4, 4*(sigma.index(i))+1)
    plt.imshow(im)
    imgx=imx(im, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+2)
    plt.imshow(imgx)
    imgy=imy(im, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+3)
    plt.imshow(imgy)
    imgmag=mag(im, i)
    plt.subplot(3, 4, 4*(sigma.index(i))+4)
    plt.imshow(imgmag)

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_ginput")

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

im = np.array(Image.open(filename))
plt.imshow(im)

print('請點擊3個點')
x = plt.ginput(3)
print('你已點擊:', x)
plt.show()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
img = Image.open(filename)
imgcopy=img.copy()

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

print("PIL_opening")

#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
from scipy.ndimage import measurements, morphology  

# 加載圖像和閾值，以確保它是二進制的
plt.figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
im = np.array(Image.open('data/castle.jpg').convert('L'))
plt.subplot(221)
plt.imshow(im)
plt.title(u'原圖')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)
plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
im_open = morphology.binary_opening(im, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數
plt.subplot(223)
plt.imshow(im_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

'''
print("------------------------------------------------------------")  # 60個

print("PIL_PCA")

from numpy import *
#measurements模塊實現二值圖像的計數和度量功能，morphology模塊實現形態學操作
from scipy.ndimage import measurements, morphology  
#from pylab import *

# 加載圖像和閾值，以確保它是二進制的
plt.figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
im = np.array(Image.open('data/castle.jpg').convert('L'))
plt.subplot(221)
plt.imshow(im)
plt.title(u'原圖')
im = (im < 128)
labels, nbr_objects = measurements.label(im) #圖像的灰度值表示對象的標簽
print ("Number of objects:", nbr_objects)
plt.subplot(222)
plt.imshow(labels)
plt.title(u'標記後的圖')
#形態學——使物體分離更好
im_open = morphology.binary_opening(im, np.ones((9, 5)), iterations=4) #開操作，第二個參數為結構元素，iterations覺定執行該操作的次數
plt.subplot(223)
plt.imshow(im_open)
plt.title(u'開運算後的圖像')
labels_open, nbr_objects_open = measurements.label(im_open)
print ("Number of objects:", nbr_objects_open)
plt.subplot(224)
plt.imshow(labels_open)
plt.title(u'開運算後進行標記後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_realROF")

from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

im = np.array(Image.open('data/gril.jpg').convert('L'))
#U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)
plt.figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
plt.subplot(1,3,1)
plt.imshow(im)
#plt.axis('equal')
plt.title(u'原噪聲圖像')
plt.subplot(1,3,2)
plt.imshow(G)
#plt.axis('equal')
plt.title(u'高斯模糊後的圖像')
plt.subplot(1,3,3)
#plt.imshow(U)
#plt.axis('equal')
plt.title(u'ROF降噪後的圖像')

plt.show()

print("------------------------------------------------------------")  # 60個

print("PIL_ROF")

from scipy.ndimage import filters
#from scipy.misc import imsave
#from PCV.tools import rof

# 創建合成圖像與噪聲
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))
#roll()函數：循環滾動數組中的元素，計算領域元素的差異。linalg.norm()函數可以衡量兩個數組見得差異
#U,T = rof.denoise(im,im)  
G = filters.gaussian_filter(im,10)
figure()
plt.gray()  #不使用顏色信息, 將圖像以灰階方式顯示
subplot(1,3,1)
imshow(im)
#axis('equal')
title(u'原噪聲圖像')

subplot(1,3,2)
imshow(G)
#axis('equal')
title(u'高斯模糊後的圖像')

subplot(1,3,3)
#imshow(U)
#axis('equal')
title(u'ROF降噪後的圖像')

show()

sys.exit()

print("------------------------------------------------------------")  # 60個

print("PIL_save")

def IsValidImage(img_path):
    """
    判斷文件是否為有效（完整）的圖片
    :param img_path:圖片路徑
    :return:True：有效 False：無效
    """
    bValid = True
    try:
        Image.open(img_path).verify()
    except:
        bValid = False
    return bValid


def transimg(img_path):
    """
    轉換圖片格式
    :param img_path:圖片路徑
    :return: True：成功 False：失敗
    """
    if IsValidImage(img_path):
        try:
            str = img_path.rsplit(".", 1)
            output_img_path = "tmp_" + str[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            im.save(output_img_path)
            return True
        except:
            return False
    else:
        return False


img_path = 'lena.png'
print(transimg(img_path))



print("------------------------------------------------------------")  # 60個

print('萃取圖片的輪廓')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#print('顯示原圖')
#plt.imshow(image1)
#plt.show()

#全彩轉灰階
image1 = image1.convert("L")
plt.imshow(image1)
plt.show()

W, H = image1.size
print('原圖大小 W =', W, ', H =', H)

# 輸出用, 製作一個與原圖大小相同的空白影像
image2 = Image.new('RGB', (W, H))

# 萃取輪廓
for y in range(0, H - 1):
    for x in range(0, W - 1):
        # 計算亮度差
        diff_x = image1.getpixel((x + 1, y)) - image1.getpixel((x, y))
        diff_y = image1.getpixel((x, y + 1)) - image1.getpixel((x, y))
        diff = diff_x + diff_y
        
        # 輸出
        if diff >= 20:
            image2.putpixel((x, y), (255, 0, 0))   #亮度差較大 著紅色
        else:
            image2.putpixel((x, y), (0, 0, 0))     #亮度差較小 著黑色

plt.imshow(image2)

plt.show()

print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個







"""

#另存新檔
image.save("tmp_pic_01.png")
#image.show()


img1.save("aaa.jpg")



"""



filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

img = Image.open(filename)
#img.show()
w,h=img.size
print(w,h) #320 240

filename=img.filename
print(filename)

print("------------------------------------------------------------")  # 60個


