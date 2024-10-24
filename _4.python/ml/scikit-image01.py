"""
skimage : scikit-image SciKit (toolkit for SciPy)

pip install scikit-image

子模塊名稱　 	主要實現功能
io 	        讀取、保存和顯示圖片或視頻
data    	提供一些測試圖片和樣本數據
color 	        顏色空間變換
filters 	圖像增強、邊緣檢測、排序濾波器、自動閾值等
draw  	        操作于numpy數組上的基本圖形繪制，包括線條、矩形、圓和文本等
transform 	幾何變換或其它變換，如旋轉、拉伸和拉東變換等
morphology 	形態學操作，如開閉運算、骨架提取等
exposure 	圖片強度調整，如亮度調整、直方圖均衡等
feature 	特征檢測與提取等
measure 	圖像屬性的測量，如相似性或等高線等
segmentation 	圖像分割
restoration 	圖像恢復
util 	        通用函數

data    圖片資料模組
color   色彩處理模組

skimage 內建圖片位置
astronaut	      宇航員圖片      coffee	            一杯咖啡圖片
lena(x)               lena美女圖片    camera	            拿相機的人圖片
coins	              硬幣圖片        moon	            月亮圖片
checkerboard	      棋盤圖片        horse	            馬圖片
page	              書頁圖片        chelsea	            小貓圖片
hubble_deep_field     星空圖片        text	            文字圖片
clock	              時鐘圖片        immunohistochemistry  結腸圖片

"""

import skimage

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

from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("------------------------------------------------------------")  # 60個

#print(skimage.__version__)

print('------------------------------------------------------------')	#60個

image = np.full((300, 300), 255) # 300X300
for xpos in [100, 150, 200]:
    image[150 - 10 : 150 + 10, xpos - 10 : xpos + 10] = 0

plt.imshow(image, cmap=plt.cm.gray)
plt.show()

print('------------------------------------------------------------')	#60個

print('顯示scikit-image預設圖片')

image = skimage.data.coffee()
#image = skimage.data.checkerboard()

# 用 plt 顯示影像
plt.imshow(image)
plt.show()

# 用 skimage.io 顯示影像
skimage.io.imshow(image)
skimage.io.show()

print('------------------------------------------------------------')	#60個

print('做 sobel 處理')

image = skimage.data.coins()
edges = skimage.filters.sobel(image)

skimage.io.imshow(edges)
skimage.io.show()

print('------------------------------------------------------------')	#60個

print('顯示scikit-image所有預設圖片')

images = ('astronaut',
          'binary_blobs',
          'brick',
          'colorwheel',
          'camera',
          'cat',
          'checkerboard',
          'clock',
          'coffee',
          'coins',
          #'eagle',
          'grass',
          'gravel',
          'horse',
          'logo',
          'page',
          'text',
          'rocket',
          )


for name in images:
    print(name)
    caller = getattr(skimage.data, name)
    image = caller()
    """
    plt.figure()
    plt.title(name)
    if image.ndim == 2:
        plt.imshow(image, cmap=plt.cm.gray)
    else:
        plt.imshow(image)
    """

plt.show()

print('------------------------------------------------------------')	#60個

fig, axs = plt.subplots(nrows=3, ncols=3)

for ax in axs.flat:
    ax.axis("off")

axs[0, 0].imshow(skimage.data.astronaut())
axs[0, 1].imshow(skimage.data.binary_blobs(), cmap=plt.cm.gray)
axs[0, 2].imshow(skimage.data.brick(), cmap=plt.cm.gray)
axs[1, 0].imshow(skimage.data.colorwheel())
axs[1, 1].imshow(skimage.data.camera(), cmap=plt.cm.gray)
axs[1, 2].imshow(skimage.data.cat())
axs[2, 0].imshow(skimage.data.checkerboard(), cmap=plt.cm.gray)
axs[2, 1].imshow(skimage.data.clock(), cmap=plt.cm.gray)
axs[2, 2].imshow(skimage.data.coffee(), cmap=plt.cm.gray)

plt.subplots_adjust(wspace=0.1, hspace=0.1)

plt.show()

print('------------------------------------------------------------')	#60個

''' 不知道做什麼
ccc =  skimage.data.binary_blobs(length=5, blob_size_fraction=0.2)
print(ccc)

"""
array([[ True, False,  True,  True,  True],
       [ True,  True,  True, False,  True],
       [False,  True, False,  True,  True],
       [ True, False, False,  True,  True],
       [ True, False, False, False,  True]])
"""
blobs = skimage.data.binary_blobs(length=256, blob_size_fraction=0.1)
# Finer structures
blobs = skimage.data.binary_blobs(length=256, blob_size_fraction=0.05)
# Blobs cover a smaller volume fraction of the image
blobs = skimage.data.binary_blobs(length=256, volume_fraction=0.3)

'''

print('------------------------------------------------------------')	#60個


print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

image = skimage.io.imread(filename)
skimage.io.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個

img=skimage.io.imread(filename, True)   #True:轉為灰階
skimage.io.imshow(img)
plt.show()


img = skimage.data.astronaut()
skimage.io.imshow(img)
plt.show()

img =skimage.color.rgb2gray(img)
skimage.io.imshow(img)
plt.show()

print('skimage內建圖片位置 :', skimage.data_dir)

#存圖
img = skimage.data.astronaut()
img = skimage.data.chelsea()
skimage.io.imshow(img)
plt.show()
skimage.io.imsave('tmp_mmmm.jpg',img)  #依副檔名轉換圖片格式存檔

print('------------------------------------------------------------')	#60個

print('打印圖片訊息')
img=skimage.data.chelsea()
skimage.io.imshow(img)
print('顯示類型 :', type(img))
print('顯示尺寸 :', img.shape)
print('圖片寬度 :', img.shape[0])
print('圖片高度 :', img.shape[1])
print('圖片通道數 :', img.shape[2])
print('顯示總像素個數 :', img.size)
print('最大像素值 :', img.max())
print('最小像素值 :', img.min())
print('像素平均值 :', img.mean())

print('------------------------------------------------------------')	#60個

#輸出小貓圖片的G通道中的第20行30列的像素值

img=skimage.data.chelsea()
pixel=img[20,30,1]
print(pixel)

#顯示紅色單通道圖片

img=skimage.data.chelsea()
R=img[:,:,0]
skimage.io.imshow(R)

#修改像素值
#對小貓圖片隨機添加椒鹽噪聲

img=skimage.data.chelsea()

#隨機生成5000個椒鹽
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
skimage.io.imshow(img)
plt.show()



print('------------------------------------------------------------')	#60個

#通過對數組的裁剪，就可以實現對圖片的裁剪。
#對小貓圖片進行裁剪

img=skimage.data.chelsea()
roi=img[80:180,100:200,:]
skimage.io.imshow(roi)
plt.show()

print('------------------------------------------------------------')	#60個

#對多個像素點進行操作，使用數組切片方式訪問。
#切片方式返回的是以指定間隔下標訪問 該數組的像素值。
#下面是有關灰度圖像的一些例子：
"""
img[i,:] = im[j,:] # 將第 j 行的數值賦值給第 i 行

img[:,i] = 100 # 將第 i 列的所有數值設為 100

img[:100,:50].sum() # 計算前 100 行、前 50 列所有數值的和

img[50:100,50:100] # 50~100 行，50~100 列（不包括第 100 行和第 100 列）

img[i].mean() # 第 i 行所有數值的平均值

img[:,-1] # 最后一列

img[-2,:] (or im[-2]) # 倒數第二行
"""

#最后我們再看兩個對像素值進行訪問和改變的例子：
#例5：將astronaut圖片進行二值化，像素值大于128的變為1，否則變為0

#img = skimage.data.astronaut()
img = skimage.data.chelsea()
img_gray=skimage.color.rgb2gray(img)
rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i,j]<=0.5):
            img_gray[i,j]=0
        else:
            img_gray[i,j]=1
skimage.io.imshow(img_gray)
plt.show()

#這個例子，使用了color模塊的rgb2gray（）函數，將彩色三通道圖片轉換成灰度圖。轉換結果為float64類型的數組，范圍為[0,1]之間。

img = skimage.data.chelsea()
reddish = img[:, :, 0] >170
img[reddish] = [0, 255, 0]
skimage.io.imshow(img)
plt.show()

#這個例子先對R通道的所有像素值進行判斷，如果大于170，則將這個地方的像素值變為[0,255,0], 即G通道值為255，R和B通道值為0。

print('------------------------------------------------------------')	#60個

#圖像數據類型及顏色空間轉換


#數據類型
img=skimage.data.chelsea()
print(img.dtype.name)


#顏色空間及其轉換
#通過圖像的顏色空間轉換來改變數據類型。
#常用的顏色空間有灰度空間、rgb空間、hsv空間和cmyk空間。顏色空間轉換以后，圖片類型都變成了float型。
#所有的顏色空間轉換函數，都放在skimage的color模塊內。

#rgb轉灰度圖

img=skimage.data.chelsea()
gray=skimage.color.rgb2gray(img)
skimage.io.imshow(gray)

plt.show()

"""

其它的轉換，用法都是一樣的，列舉常用的如下：
skimage.color.rgb2grey(rgb)
skimage.color.rgb2hsv(rgb)
skimage.color.rgb2lab(rgb)
skimage.color.gray2rgb(image)
skimage.color.hsv2rgb(hsv)
skimage.color.lab2rgb(lab)

實際上，上面的所有轉換函數，都可以用一個函數來代替
skimage.color.convert_colorspace(arr, fromspace, tospace)
表示將arr從fromspace顏色空間轉換到tospace顏色空間。

例：rgb轉hsv
img=skimage.data.chelsea()
hsv=skimage.color.convert_colorspace(img,'RGB','HSV')
skimage.io.imshow(hsv)

"""


print('------------------------------------------------------------')	#60個

#在color模塊的顏色空間轉換函數中，還有一個比較有用的函數是
#skimage.color.label2rgb(arr), 可以根據標簽值對圖片進行著色。以后的圖片分類后著色就可以用這個函數。
#例：將astronaut圖片分成三類，然后用默認顏色對三類進行著色

img=skimage.data.astronaut()
gray=skimage.color.rgb2gray(img)
rows,cols=gray.shape
labels=np.zeros([rows,cols])
for i in range(rows):
    for j in range(cols):
        if(gray[i,j]<0.4):
            labels[i,j]=0
        elif(gray[i,j]<0.75):
            labels[i,j]=1
        else:
            labels[i,j]=2
dst=skimage.color.label2rgb(labels)
skimage.io.imshow(dst)
plt.show()

print("------------------------------------------------------------")  # 60個

"""
#圖像的繪制
實際上前面我們就已經用到了圖像的繪制，如：
skimage.io.imshow(img)  
這一行代碼的實質是利用matplotlib包對圖片進行繪制，
繪制成功后，返回一個matplotlib類型的數據。
因此，我們也可以這樣寫：
import matplotlib.pyplot as plt
plt.imshow(img)
imshow()函數格式為：
matplotlib.pyplot.imshow(X, cmap=None)
X: 要繪制的圖像或數組。
cmap: 顏色圖譜（colormap), 默認繪制為RGB(A)顏色空間。

其它可選的顏色圖譜如下列表：
顏色圖譜	描述
autumn 		紅-橙-黃	bone 		黑-白，x線
cool 		青-洋紅		copper 		黑-銅
flag 		紅-白-藍-黑	gray 		黑-白
hot 		黑-紅-黃-白	hsv 		hsv顏色空間， 紅-黃-綠-青-藍-洋紅-紅
inferno 	黑-紅-黃	jet 		藍-青-黃-紅
magma 		黑-紅-白	pink 		黑-粉-白
plasma 		綠-紅-黃	prism 	 	紅-黃-綠-藍-紫-...-綠模式
spring 		洋紅-黃		summer 		綠-黃
viridis 	藍-綠-黃	winter 		藍-綠

用的比較多的有gray,jet等，如：
plt.imshow(image,plt.cm.gray)
plt.imshow(img,cmap=plt.cm.jet)

在窗口上繪制完圖片后，返回一個AxesImage對象。
要在窗口上顯示這個對象，我們可以調用show()函數來進行顯示，
但進行練習的時候（ipython環境中），
一般我們可以省略show（）函數，也能自動顯示出來。
"""

img=skimage.data.astronaut()
dst=skimage.io.imshow(img)
print(type(dst))
skimage.io.show()

#可以看到，類型是'matplotlib.image.AxesImage'。
#顯示一張圖片，我們通常會這樣寫：

img=skimage.data.astronaut()
plt.imshow(img)
plt.show()

print('------------------------------------------------------------')	#60個
 
"""
matplotlib是一個專業繪圖的庫，相當于matlab中的plot,可以設置多個figure窗口,
設置figure的標題，隱藏坐標尺，甚至可以使用subplot在一個figure中顯示多張圖片。
一般我們可以這樣導入matplotlib庫：

import matplotlib.pyplot as plt

也就是說，我們繪圖實際上用的是matplotlib包的pyplot模塊。

一、用figure函數和subplot函數分別創建主窗口與子圖

例:分開并同時顯示宇航員圖片的三個通道
"""

img=skimage.data.astronaut()
plt.figure(num='astronaut',figsize=(8,8))  #創建一個名為astronaut的窗口,并設置大小 

plt.subplot(2,2,1)     #將窗口分為兩行兩列四個子圖，則可顯示四幅圖片
plt.title('origin image')   #第一幅圖片標題
plt.imshow(img)      #繪制第一幅圖片

plt.subplot(2,2,2)     #第二個子圖
plt.title('R channel')   #第二幅圖片標題
plt.imshow(img[:,:,0],plt.cm.gray)      #繪制第二幅圖片,且為灰度圖
plt.axis('off')     #不顯示坐標尺寸

plt.subplot(2,2,3)     #第三個子圖
plt.title('G channel')   #第三幅圖片標題
plt.imshow(img[:,:,1],plt.cm.gray)      #繪制第三幅圖片,且為灰度圖
plt.axis('off')     #不顯示坐標尺寸

plt.subplot(2,2,4)     #第四個子圖
plt.title('B channel')   #第四幅圖片標題
plt.imshow(img[:,:,2],plt.cm.gray)      #繪制第四幅圖片,且為灰度圖
plt.axis('off')     #不顯示坐標尺寸

plt.show()   #顯示窗口

"""
在圖片繪制過程中，我們用matplotlib.pyplot模塊下的figure（）函數來創建顯示窗口，該函數的格式為：

matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None)

所有參數都是可選的，都有默認值，因此調用該函數時可以不帶任何參數，其中：

num: 整型或字符型都可以。如果設置為整型，則該整型數字表示窗口的序號。如果設置為字符型，則該字符串表示窗口的名稱。用該參數來命名窗口，如果兩個窗口序號或名相同，則后一個窗口會覆蓋前一個窗口。

figsize: 設置窗口大小。是一個tuple型的整數，如figsize=（8，8）

dpi: 整形數字，表示窗口的分辨率。

facecolor: 窗口的背景顏色。

edgecolor: 窗口的邊框顏色。

用figure()函數創建的窗口，只能顯示一幅圖片，如果想要顯示多幅圖片，則需要將這個窗口再劃分為幾個子圖，在每個子圖中顯示不同的圖片。我們可以使用subplot（）函數來劃分子圖，函數格式為：

matplotlib.pyplot.subplot(nrows, ncols, plot_number)

nrows: 子圖的行數。

ncols: 子圖的列數。

plot_number: 當前子圖的編號。

如：

plt.subplot(2,2,1)

則表示將figure窗口劃分成了2行2列共4個子圖，當前為第1個子圖。我們有時也可以用這種寫法：

plt.subplot(221)

兩種寫法效果是一樣的。每個子圖的標題可用title()函數來設置，是否使用坐標尺可用axis()函數來設置，如：

plt.subplot(221)
plt.title("first subwindow")
plt.axis('off')  
""" 

#二、用subplots來創建顯示窗口與劃分子圖
#除了上面那種方法創建顯示窗口和劃分子圖，還有另外一種編寫方法也可以

img = skimage.data.immunohistochemistry()
hsv = skimage.color.rgb2hsv(img)

fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax0, ax1, ax2, ax3 = axes.ravel()

ax0.imshow(img)
ax0.set_title("Original image")

ax1.imshow(hsv[:, :, 0], cmap=plt.cm.gray)
ax1.set_title("H")

ax2.imshow(hsv[:, :, 1], cmap=plt.cm.gray)
ax2.set_title("S")

ax3.imshow(hsv[:, :, 2], cmap=plt.cm.gray)
ax3.set_title("V")

for ax in axes.ravel():
    ax.axis('off')

fig.tight_layout()  #自動調整subplot間的參數

plt.show()

print('------------------------------------------------------------')	#60個

"""
直接用subplots()函數來創建并劃分窗口。注意，比前面的subplot()函數多了一個s，該函數格式為：

matplotlib.pyplot.subplots(nrows=1, ncols=1)

nrows: 所有子圖行數，默認為1。

ncols: 所有子圖列數，默認為1。

返回一個窗口figure, 和一個tuple型的ax對象，該對象包含所有的子圖,可結合ravel()函數列出所有子圖，如：

fig, axes = plt.subplots(2, 2, figsize=(7, 6))
ax0, ax1, ax2, ax3 = axes.ravel()

創建了2行2列4個子圖，分別取名為ax0,ax1,ax2和ax3, 每個子圖的標題用set_title()函數來設置，如：

ax0.imshow(img)
ax0.set_title("Original image")

如果有多個子圖，我們還可以使用tight_layout()函數來調整顯示的布局，該函數格式為：

matplotlib.pyplot.tight_layout(pad=1.08, h_pad=None, w_pad=None, rect=None)

所有的參數都是可選的，調用該函數時可省略所有的參數。

pad: 主窗口邊緣和子圖邊緣間的間距，默認為1.08

h_pad, w_pad: 子圖邊緣之間的間距，默認為 pad_inches

rect: 一個矩形區域，如果設置這個值，則將所有的子圖調整到這個矩形區域內。

一般調用為：

plt.tight_layout()  #自動調整subplot間的參數

""" 

#三、其它方法繪圖并顯示
#除了使用matplotlib庫來繪制圖片，skimage還有另一個子模塊viewer，也提供一個函數來顯示圖片。
#不同的是，它利用Qt工具來創建一塊畫布，從而在畫布上繪制圖像。

"""
from skimage.viewer import ImageViewer

img = skimage.data.coins()
viewer = ImageViewer(img)
viewer.show()
"""

"""
最后總結一下，繪制和顯示圖片常用到的函數有：
函數名 	功能 	調用格式
figure 	創建一個顯示窗口 	plt.figure(num=1,figsize=(8,8)
imshow 	繪制圖片 	plt.imshow(image)
show 	顯示窗口 	plt.show()
subplot 	劃分子圖 	plt.subplot(2,2,1)
title 	設置子圖標題(與subplot結合使用） 	plt.title('origin image')
axis 	是否顯示坐標尺 	plt.axis('off')
subplots 	創建帶有多個子圖的窗口 	fig,axes=plt.subplots(2,2,figsize=(8,8))
ravel 	為每個子圖設置變量 	ax0,ax1,ax2,ax3=axes.ravel()
set_title 	設置子圖標題（與axes結合使用） 	ax0.set_title('first window')
tight_layout 	自動調整子圖顯示布局 	plt.tight_layout()
"""

print("------------------------------------------------------------")  # 60個

"""
圖像的批量處理

有些時候，我們不僅要對一張圖片進行處理，可能還會對一批圖片處理。這時候，我們可以通過循環來執行處理，也可以調用程序自帶的圖片集合來處理。

圖片集合函數為：

skimage.io.ImageCollection(load_pattern,load_func=None)

這個函數是放在io模塊內的，帶兩個參數，第一個參數load_pattern, 表示圖片組的路徑，可以是一個str字符串。第二個參數load_func是一個回調函數，我們對圖片進行批量處理就可以通過這個回調函數實現。回調函數默認為imread(),即默認這個函數是批量讀取圖片。

"""
'''

string = skimage.data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = skimage.io.ImageCollection(string)
print(len(coll))


#表示資料夾內有 23 張圖

"""
顯示結果為25, 說明

系統自帶了23張png的示例圖片，這些圖片都讀取了出來，放在圖片集合coll里。
如果我們想顯示其中一張圖片，則可以在后加上一行代碼：
skimage.io.imshow(coll[10])

如果一個文件夾里，我們既存放了一些jpg格式的圖片，又存放了一些png格式的圖片，現在想把它們全部讀取出來，該怎么做呢?
"""

#string='d:/pic/*.jpg:d:/pic/*.png'
string = skimage.data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = skimage.io.ImageCollection(string)
print(len(coll))

print('------------------------------------------------------------')	#60個

"""
注意這個地方'd:/pic/*.jpg:d:/pic/*.png' ，是兩個字符串合在一起的，第一個是'd:/pic/*.jpg', 第二個是'd:/pic/*.png' ，合在一起后，中間用冒號來隔開，這樣就可以把d:/pic/文件夾下的jpg和png格式的圖片都讀取出來。如果還想讀取存放在其它地方的圖片，也可以一并加進去，只是中間同樣用冒號來隔開。

skimage.io.ImageCollection()這個函數省略第二個參數，就是批量讀取。如果我們不是想批量讀取，而是其它批量操作，如批量轉換為灰度圖，那又該怎么做呢？

那就需要先定義一個函數，然后將這個函數作為第二個參數，如：
"""

def convert_gray(f):
    rgb=skimage.io.imread(f)
    return skimage.color.rgb2gray(rgb)
    
string = skimage.data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = skimage.io.ImageCollection(string,load_func=convert_gray)
skimage.io.imshow(coll[8])
plt.show()

print('------------------------------------------------------------')	#60個

#這種批量操作對視頻處理是極其有用的，因為視頻就是一系列的圖片組合

class AVILoader:
    video_file = 'myvideo.avi'

    def __call__(self, frame):
        return video_read(self.video_file, frame)

avi_load = AVILoader()

frames = range(0, 1000, 10) # 0, 10, 20, ...
ic =skimage.io.ImageCollection(frames, load_func=avi_load)

print('------------------------------------------------------------')	#60個

"""
這段代碼的意思，就是將myvideo.avi這個視頻中每隔10幀的圖片讀取出來，放在圖片集合中。

得到圖片集合以后，我們還可以將這些圖片連接起來，構成一個維度更高的數組，連接圖片的函數為：

skimage.io.concatenate_images(ic)

帶一個參數，就是以上的圖片集合，如：
"""
"""

coll = skimage.io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = skimage.io.ImageCollection(skimage.data_dir + '/*.png')
mat=skimage.io.concatenate_images(coll)

#使用concatenate_images(ic)函數的前提是讀取的這些圖片尺寸必須一致，否則會出錯。我們看看圖片連接前后的維度變化：

coll = skimage.io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = skimage.io.ImageCollection(skimage.data_dir + '/*.png')
print(len(coll))      #連接的圖片數量
print(coll[0].shape)   #連接前的圖片尺寸，所有的都一樣
mat=skimage.io.concatenate_images(coll)
print(mat.shape)  #連接后的數組尺寸
"""



"""

顯示結果：

2
(870, 580, 3)
(2, 870, 580, 3)

可以看到，將2個3維數組，連接成了一個4維數組

如果我們對圖片進行批量操作后，想把操作后的結果保存起來，也是可以辦到的。

例：把系統自帶的所有png示例圖片，全部轉換成256*256的jpg格式灰度圖，保存在d:/data/文件夾下

改變圖片的大小，我們可以使用tranform模塊的resize()函數，后續會講到這個模塊。
"""

def convert_gray(f):
     rgb=skimage.io.imread(f)    #依次讀取rgb圖片
     gray=skimage.color.rgb2gray(rgb)   #將rgb圖片轉換成灰度圖
     dst=skimage.transform.resize(gray,(256,256))  #將灰度圖片大小轉換為256*256
     return dst
    
#string = skimage.data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = skimage.io.ImageCollection(string,load_func=convert_gray)
print(len(coll))

for i in range(len(coll)):
    print(i)
    #skimage.io.imsave(str(i)+'.jpg', coll[i])  #循環保存圖片  fail
    print(str(i)+'.jpg')
    #print(str(i)+'.jpg')
    #print(i)
plt.show()

print('------------------------------------------------------------')	#60個

'''


"""
圖像的形變與縮放

圖像的形變與縮放，使用的是skimage的transform模塊，函數比較多，功能齊全。

1、改變圖片尺寸resize

函數格式為：

skimage.transform.resize(image, output_shape)

image: 需要改變尺寸的圖片

output_shape: 新的圖片尺寸
"""

img = skimage.data.camera()
dst=skimage.transform.resize(img, (80, 60))
plt.figure('resize')

plt.subplot(121)
plt.title('before resize')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('before resize')
plt.imshow(dst,plt.cm.gray)

plt.show()

#將camera圖片由原來的512*512大小，變成了80*60大小。從下圖中的坐標尺，我們能夠看出來：

"""
2、按比例縮放rescale

函數格式為：

skimage.transform.rescale(image, scale[, ...])

scale參數可以是單個float數，表示縮放的倍數，也可以是一個float型的tuple，如[0.2,0.5],表示將行列數分開進行縮放
"""

img = skimage.data.camera()
print(img.shape)  #圖片原始大小 
print(skimage.transform.rescale(img, 0.1).shape)  #縮小為原來圖片大小的0.1倍
print(skimage.transform.rescale(img, [0.5,0.25]).shape)  #縮小為原來圖片行數一半，列數四分之一
print(skimage.transform.rescale(img, 2).shape)   #放大為原來圖片大小的2倍
"""
結果為：
(512, 512)
(51, 51)
(256, 128)
(1024, 1024)

3、旋轉 rotate

skimage.transform.rotate(image, angle[, ...],resize=False)

angle參數是個float類型數，表示旋轉的度數

resize用于控制在旋轉時，是否改變大小 ，默認為False
"""

img = skimage.data.camera()
print(img.shape)  #圖片原始大小
img1=skimage.transform.rotate(img, 60) #旋轉90度，不改變大小 
print(img1.shape)
img2=skimage.transform.rotate(img, 30,resize=True)  #旋轉30度，同時改變大小
print(img2.shape)   

plt.figure('resize')

plt.subplot(121)
plt.title('rotate 60')
plt.imshow(img1,plt.cm.gray)

plt.subplot(122)
plt.title('rotate  30')
plt.imshow(img2,plt.cm.gray)

plt.show()


"""
4、圖像金字塔

以多分辨率來解釋圖像的一種有效但概念簡單的結構就是圖像金字塔。圖像金字塔最初用于機器視覺和圖像壓縮，一幅圖像的金字塔是一系列以金字塔形狀排列的分辨率逐步降低的圖像集合。金字塔的底部是待處理圖像的高分辨率表示，而頂部是低分辨率的近似。當向金字塔的上層移動時，尺寸和分辨率就降低。

在此，我們舉一個高斯金字塔的應用實例，函數原型為：

skimage.transform.pyramid_gaussian(image, downscale=2)
downscale控制著金字塔的縮放比例
"""

image = skimage.data.astronaut()  #載入宇航員圖片
rows, cols, dim = image.shape  #獲取圖片的行數，列數和通道數
pyramid = tuple(skimage.transform.pyramid_gaussian(image, downscale=2))  #產生高斯金字塔圖像
#共生成了log(512)=9幅金字塔圖像，加上原始圖像共10幅，pyramid[0]-pyramid[1]

"""
#composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  #生成背景
composite_image = np.ones((rows, cols + 256, 3), dtype=np.double)  #生成背景
"""

"""
除了高斯金字塔外，還有其它的金字塔，如：
skimage.transform.pyramid_laplacian(image, downscale=2)
"""

print("------------------------------------------------------------")  # 60個

"""
#對比度與亮度調整

圖像亮度與對比度的調整，是放在skimage包的exposure模塊里面

1、gamma調整

原理：I=Ig

對原圖像的像素，進行冪運算，得到新的像素值。公式中的g就是gamma值。

如果gamma>1, 新圖像比原圖像暗

如果gamma<1,新圖像比原圖像亮

函數格式為：skimage.exposure.adjust_gamma(image, gamma=1)

gamma參數默認為1，原像不發生變化 。
"""

#img_as_float() 將 unit8 轉換為 float
image = skimage.img_as_float(skimage.data.moon())
gam1= skimage.exposure.adjust_gamma(image, 2)   #調暗
gam2= skimage.exposure.adjust_gamma(image, 0.5)  #調亮
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(131)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(132)
plt.title('gamma=2')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.subplot(133)
plt.title('gamma=0.5')
plt.imshow(gam2,plt.cm.gray)
plt.axis('off')

plt.show()

"""
2、log對數調整

這個剛好和gamma相反

原理：I=log(I)
"""

#img_as_float() 將 unit8 轉換為 float
image = skimage.img_as_float(skimage.data.moon())
gam1= skimage.exposure.adjust_log(image)   #對數調整
plt.figure('adjust_gamma',figsize=(8,8))

plt.subplot(121)
plt.title('origin image')
plt.imshow(image,plt.cm.gray)
plt.axis('off')

plt.subplot(122)
plt.title('log')
plt.imshow(gam1,plt.cm.gray)
plt.axis('off')

plt.show()

"""
3、判斷圖像對比度是否偏低
函數：is_low_contrast(img)
返回一個bool型值
"""

image =skimage.data.moon()
result=skimage.exposure.is_low_contrast(image)
print(result)

#輸出為False

"""
4、調整強度

函數：skimage.exposure.rescale_intensity(image, in_range='image', out_range='dtype')

in_range 表示輸入圖片的強度范圍，默認為'image', 表示用圖像的最大/最小像素值作為范圍

out_range 表示輸出圖片的強度范圍，默認為'dype', 表示用圖像的類型的最大/最小值作為范圍

默認情況下，輸入圖片的[min,max]范圍被拉伸到[dtype.min, dtype.max]，如果dtype=uint8, 那么dtype.min=0, dtype.max=255
"""

image = np.array([51, 102, 153], dtype=np.uint8)
mat=skimage.exposure.rescale_intensity(image)
print(mat)

#輸出為[  0 127 255]
#即像素最小值由51變為0，最大值由153變為255，整體進行了拉伸，但是數據類型沒有變，還是uint8
#前面我們講過，可以通過img_as_float()函數將unit8類型轉換為float型，實際上還有更簡單的方法，就是乘以1.0

image = np.array([51, 102, 153], dtype=np.uint8)
print(image*1.0)

#即由[51,102,153]變成了[  51.  102.  153.]
#而float類型的范圍是[0,1]，因此對float進行rescale_intensity 調整后，范圍變為[0,1],而不是[0,255]

image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=skimage.exposure.rescale_intensity(tmp)
print(mat)

#結果為[ 0.   0.5  1. ]
#如果原始像素值不想被拉伸，只是等比例縮小，就使用in_range參數，如：

image = np.array([51, 102, 153], dtype=np.uint8)
tmp=image*1.0
mat=skimage.exposure.rescale_intensity(tmp,in_range=(0,255))
print(mat)

#輸出為：[ 0.2  0.4  0.6]，即原像素值除以255
#如果參數in_range的[main,max]范圍要比原始像素值的范圍[min,max] 大或者小，那就進行裁剪，如：

mat=skimage.exposure.rescale_intensity(tmp,in_range=(0,102))
print(mat)

#輸出[ 0.5  1.   1. ]，即原像素值除以102，超出1的變為1
#如果一個數組里面有負數，現在想調整到正數，就使用out_range參數。如：

image = np.array([-10, 0, 10], dtype=np.int8)
mat=skimage.exposure.rescale_intensity(image, out_range=(0, 127))
print(mat)

#輸出[  0  63 127]

print("------------------------------------------------------------")  # 60個

"""
#直方圖與均衡化

在圖像處理中，直方圖是非常重要，也是非常有用的一個處理要素。

在skimage庫中對直方圖的處理，是放在exposure這個模塊中。

1、計算直方圖

函數：skimage.exposure.histogram(image, nbins=256)

在numpy包中，也提供了一個計算直方圖的函數histogram(),兩者大同小義。

返回一個tuple（hist, bins_center), 前一個數組是直方圖的統計量，后一個數組是每個bin的中間值
"""

image = skimage.data.camera()*1.0
hist1=np.histogram(image, bins=2)   #用numpy包計算直方圖
hist2=skimage.exposure.histogram(image, nbins=2)  #用skimage計算直方圖
print(hist1)
print(hist2)

#(array([107432, 154712], dtype=int64), array([ 0. , 127.5, 255. ]))
#(array([107432, 154712], dtype=int64), array([ 63.75, 191.25]))
#分成兩個bin，每個bin的統計量是一樣的，但numpy返回的是每個bin的兩端的范圍值，而skimage返回的是每個bin的中間值

"""
2、繪制直方圖

繪圖都可以調用matplotlib.pyplot庫來進行，其中的hist函數可以直接繪制直方圖。

調用方式：

n, bins, patches = plt.hist(arr, bins=10, density=False, facecolor='black', edgecolor='black',alpha=1，histtype='bar')

hist的參數非常多，但常用的就這六個，只有第一個是必須的，后面四個可選

arr: 需要計算直方圖的一維數組

bins: 直方圖的柱數，可選項，默認為10

density: 是否將得到的直方圖向量歸一化。默認為False

facecolor: 直方圖顏色

edgecolor: 直方圖邊框顏色

alpha: 透明度

histtype: 直方圖類型，‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’

返回值 ：

n: 直方圖向量，是否歸一化由參數density設定

bins: 返回各個bin的區間范圍

patches: 返回每個bin里面包含的數據，是一個list
"""

img = skimage.data.camera()
plt.figure("hist")
arr = img.flatten()
n, bins, patches = plt.hist(arr, bins=256, density = True, edgecolor='None',facecolor='red')
plt.show()

"""
其中的flatten()函數是numpy包里面的，用于將二維數組序列化成一維數組。
是按行序列，如
mat=[[1 2 3
　　　  4 5 6]]

經過 mat.flatten()后，就變成了

mat=[1 2 3 4 5 6]

3、彩色圖片三通道直方圖

一般來說直方圖都是征對灰度圖的，如果要畫rgb圖像的三通道直方圖，實際上就是三個直方圖的疊加。

"""

img=skimage.data.astronaut()
ar=img[:,:,0].flatten()
plt.hist(ar, bins=256, density = True, facecolor='r',edgecolor='r',stacked=1)
ag=img[:,:,1].flatten()
plt.hist(ag, bins=256, density = True, facecolor='g',edgecolor='g',stacked=1)
ab=img[:,:,2].flatten()
plt.hist(ab, bins=256, density = True, facecolor='b',edgecolor='b')
plt.show()

"""
其中，加一個參數hold=1,表示可以疊加

4、直方圖均衡化

如果一副圖像的像素占有很多的灰度級而且分布均勻，那么這樣的圖像往往有高對比度和多變的灰度色調。直方圖均衡化就是一種能僅靠輸入圖像直方圖信息自動達到這種效果的變換函數。它的基本思想是對圖像中像素個數多的灰度級進行展寬，而對圖像中像素個數少的灰度進行壓縮，從而擴展取值的動態范圍，提高了對比度和灰度色調的變化，使圖像更加清晰。
"""

img=skimage.data.moon()
plt.figure("hist",figsize=(8,8))

arr=img.flatten()
plt.subplot(221)
plt.imshow(img,plt.cm.gray)  #原始圖像
plt.subplot(222)
plt.hist(arr, bins=256, density = True, edgecolor='None',facecolor='red') #原始圖像直方圖

img1=skimage.exposure.equalize_hist(img)
arr1=img1.flatten()
plt.subplot(223)
plt.imshow(img1,plt.cm.gray)  #均衡化圖像
plt.subplot(224)
plt.hist(arr1, bins=256, density = True,edgecolor='None',facecolor='red') #均衡化直方圖

plt.show()

print('------------------------------------------------------------')	#60個

"""
圖像簡單濾波

對圖像進行濾波，可以有兩種效果：一種是平滑濾波，用來抑制噪聲；另一種是微分算子，可以用來檢測邊緣和特征提取。

skimage庫中通過filters模塊進行濾波操作。

1、sobel算子

sobel算子可用來檢測邊緣

函數格式為：skimage.filters.sobel(image, mask=None)
"""

img = skimage.data.camera()
edges = skimage.filters.sobel(img)
plt.imshow(edges,plt.cm.gray)
plt.show()

"""
2、roberts算子

roberts算子和sobel算子一樣，用于檢測邊緣

調用格式也是一樣的：

edges = skimage.filters.roberts(img)

3、scharr算子

功能同sobel，調用格式：

edges = skimage.filters.scharr(img)

4、prewitt算子

功能同sobel，調用格式：

edges = skimage.filters.prewitt(img)

5、canny算子

canny算子也是用于提取邊緣特征，但它不是放在filters模塊，而是放在feature模塊

函數格式：skimage.feature.canny(image，sigma=1.0)

可以修改sigma的值來調整效果
"""

img = skimage.data.camera()
edges1 = skimage.feature.canny(img)   #sigma=1
edges2 = skimage.feature.canny(img,sigma=3)   #sigma=3

plt.figure('canny',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""

從結果可以看出，sigma越小，邊緣線條越細小。

6、gabor濾波

gabor濾波可用來進行邊緣檢測和紋理特征提取。

函數調用格式：skimage.filters.gabor_filter(image, frequency)

通過修改frequency值來調整濾波效果，返回一對邊緣結果，一個是用真實濾波核的濾波結果，一個是想象的濾波核的濾波結果。
"""

"""
#沒有 gabor_filter

img = skimage.data.camera()
filt_real, filt_imag = skimage.filters.gabor_filter(img,frequency=0.6)   

plt.figure('gabor',figsize=(8,8))

plt.subplot(121)
plt.title('filt_real')
plt.imshow(filt_real,plt.cm.gray)  

plt.subplot(122)
plt.title('filt-imag')
plt.imshow(filt_imag,plt.cm.gray)

plt.show()
"""

"""

以上為frequency=0.6的結果圖。

以上為frequency=0.1的結果圖

7、gaussian濾波

多維的濾波器，是一種平滑濾波，可以消除高斯噪聲。

調用函數為：skimage.filters.gaussian_filter(image, sigma)

通過調節sigma的值來調整濾波效果
"""

"""
#沒有 gaussian_filter

img = skimage.data.astronaut()
edges1 = skimage.filters.gaussian_filter(img,sigma=0.4)   #sigma=0.4
edges2 = skimage.filters.gaussian_filter(img,sigma=5)   #sigma=5

plt.figure('gaussian',figsize=(8,8))
plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()
"""

"""
可見sigma越大，過濾后的圖像越模糊

8.median

中值濾波，一種平滑濾波，可以消除噪聲。

需要用skimage.morphology模塊來設置濾波器的形狀。
"""

from skimage.morphology import disk

img = skimage.data.camera()
edges1 = skimage.filters.median(img,disk(5))
edges2 = skimage.filters.median(img,disk(9))

plt.figure('median',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""
從結果可以看出，濾波器越大，圖像越模糊。

9、水平、垂直邊緣檢測

上邊所舉的例子都是進行全部邊緣檢測，有些時候我們只需要檢測水平邊緣，或垂直邊緣，就可用下面的方法。

水平邊緣檢測：sobel_h, prewitt_h, scharr_h

垂直邊緣檢測： sobel_v, prewitt_v, scharr_v
"""

img = skimage.data.camera()
edges1 = skimage.filters.sobel_h(img)  
edges2 = skimage.filters.sobel_v(img) 

plt.figure('sobel_v_h',figsize=(8,8))

plt.subplot(121)
plt.imshow(edges1,plt.cm.gray)  

plt.subplot(122)
plt.imshow(edges2,plt.cm.gray)

plt.show()

"""

上邊左圖為檢測出的水平邊緣，右圖為檢測出的垂直邊緣。

10、交叉邊緣檢測

可使用Roberts的十字交叉核來進行過濾，以達到檢測交叉邊緣的目的。這些交叉邊緣實際上是梯度在某個方向上的一個分量。

其中一個核：

 0   1
-1   0

對應的函數：

roberts_neg_diag(image）

"""

img = skimage.data.camera()
dst = skimage.filters.roberts_neg_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""
另外一個核：

1   0
0  -1

對應函數為：

roberts_pos_diag(image）
"""

img = skimage.data.camera()
dst = skimage.filters.roberts_pos_diag(img) 

plt.figure('filters',figsize=(8,8))
plt.subplot(121)
plt.title('origin image')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('filted image')
plt.imshow(dst,plt.cm.gray)

plt.show()

print('------------------------------------------------------------')	#60個

"""
圖像自動閾值分割

圖像閾值分割是一種廣泛應用的分割技術，利用圖像中要提取的目標區域與其背景在灰度特性上的差異，把圖像看作具有不同灰度級的兩類區域(目標區域和背景區域)的組合，選取一個比較合理的閾值，以確定圖像中每個像素點應該屬于目標區域還是背景區域，從而產生相應的二值圖像。

在skimage庫中，閾值分割的功能是放在filters模塊中。

我們可以手動指定一個閾值，從而來實現分割。也可以讓系統自動生成一個閾值，下面幾種方法就是用來自動生成閾值。

1、threshold_otsu

基于Otsu的閾值分割方法，函數調用格式：

skimage.filters.threshold_otsu(image, nbins=256)

參數image是指灰度圖像，返回一個閾值。
"""

image = skimage.data.camera()
thresh = skimage.filters.threshold_otsu(image)   #返回一個閾值
dst =(image <= thresh)*1.0   #根據閾值進行分割

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()

"""

返回閾值為87，根據87進行分割得下圖:

2、threshold_yen

使用方法同上：

thresh = skimage.filters.threshold_yen(image) 

返回閾值為198，分割如下圖：

3、threshold_li

使用方法同上：

thresh = skimage.filters.threshold_li(image)

返回閾值64.5，分割如下圖：

4、threshold_isodata

閾值計算方法：

threshold = (image[image <= threshold].mean() +image[image > threshold].mean()) / 2.0

使用方法同上：

thresh = skimage.filters.threshold_isodata(image)

返回閾值為87，因此分割效果和threshold_otsu一樣。

5、threshold_adaptive

調用函數為：

skimage.filters.threshold_adaptive(image, block_size, method='gaussian'）

block_size: 塊大小，指當前像素的相鄰區域大小，一般是奇數（如3，5，7。。。）

method: 用來確定自適應閾值的方法，有'mean', 'generic', 'gaussian' 和 'median'。省略時默認為gaussian

該函數直接訪問一個閾值后的圖像，而不是閾值。
"""
"""
#沒有 threshold_adaptive

image = skimage.data.camera()
dst = skimage.filters.threshold_adaptive(image, 15) #返回一個閾值圖像

plt.figure('thresh',figsize=(8,8))

plt.subplot(121)
plt.title('original image')
plt.imshow(image,plt.cm.gray)

plt.subplot(122)
plt.title('binary image')
plt.imshow(dst,plt.cm.gray)

plt.show()
"""

"""

大家可以修改block_size的大小和method值來查看更多的效果。如：

dst1 = skimage.filters.threshold_adaptive(image,31,'mean') 
dst2 = skimage.filters.threshold_adaptive(image,5,'median')
"""

print('------------------------------------------------------------')	#60個

"""
基本圖形的繪制

圖形包括線條、圓形、橢圓形、多邊形等。

在skimage包中，繪制圖形用的是draw模塊，不要和繪制圖像搞混了。

1、畫線條

函數調用格式為：

skimage.draw.line(r1,c1,r2,c2)

r1,r2: 開始點的行數和結束點的行數

c1,c2: 開始點的列數和結束點的列數

返回當前繪制圖形上所有點的坐標，如：

rr, cc =draw.line(1, 5, 8, 2)

表示從（1，5）到（8，2）連一條線，返回線上所有的像素點坐標[rr,cc]
"""

from skimage import draw

img = skimage.data.chelsea()
print(img.shape)

rr, cc =draw.line(1, 150, 270, 400)
img[rr, cc] =255
plt.imshow(img,plt.cm.gray)
plt.show()

"""
如果想畫其它顏色的線條，則可以使用set_color（）函數，格式為：

skimage.draw.set_color(img, coords, color)

例：

draw.set_color(img,[rr,cc],[255,0,0])

則繪制紅色線條。
"""

from skimage import draw

img=skimage.data.chelsea()
rr, cc =draw.line(1, 150, 270, 250)
draw.set_color(img,[rr,cc],[0,0,255])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
2、畫圓

函數格式：skimage.draw.circle(cy, cx, radius）

cy和cx表示圓心點，radius表示半徑
"""

"""沒有circle

from skimage import draw

img=skimage.data.chelsea()
rr, cc=draw.circle(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()
"""

"""
3、多邊形

函數格式：skimage.draw.polygon(Y,X)

Y為多邊形頂點的行集合，X為各頂點的列值集合。
"""

from skimage import draw

img=skimage.data.chelsea()
Y=np.array([10,10,60,60])
X=np.array([200,400,400,200])
rr, cc=draw.polygon(Y,X)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
我在此處只設置了四個頂點，因此是個四邊形。

4、橢圓

格式：skimage.draw.ellipse(cy, cx, yradius, xradius）

cy和cx為中心點坐標，yradius和xradius代表長短軸。
"""

from skimage import draw

img=skimage.data.chelsea()
rr, cc=draw.ellipse(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
5、貝塞兒曲線
格式：skimage.draw.bezier_curve(y1,x1,y2,x2,y3,x3,weight)
y1,x1表示第一個控制點坐標
y2,x2表示第二個控制點坐標
y3,x3表示第三個控制點坐標
weight表示中間控制點的權重，用于控制曲線的彎曲度。
"""

from skimage import draw

img=skimage.data.chelsea()
rr, cc=draw.bezier_curve(150,50,50,280,260,400,2)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
6、畫空心圓
和前面的畫圓是一樣的，只是前面是實心圓，而此處畫空心圓，只有邊框線。
格式：skimage.draw.circle_perimeter(yx,yc,radius)
yx,yc是圓心坐標，radius是半徑
"""

from skimage import draw

img=skimage.data.chelsea()
rr, cc=draw.circle_perimeter(150,150,50)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()

"""
7、空心橢圓
格式：skimage.draw.ellipse_perimeter(cy, cx, yradius, xradius）
cy,cx表示圓心
yradius,xradius表示長短軸
"""

from skimage import draw

img=skimage.data.chelsea()
rr, cc=draw.ellipse_perimeter(150, 150, 30, 80)
draw.set_color(img,[rr,cc],[255,0,0])
plt.imshow(img,plt.cm.gray)
plt.show()
 

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

import matplotlib.cm as cm

depth = 4
filter_shape = (3, 3) 
   
w_shape = (depth, 3, filter_shape[0], filter_shape[1]) 
dist = np.random.uniform(-0.2, 0.2, size=w_shape)
output = 5

astronaut = skimage.data.astronaut()
img = np.asarray(astronaut, dtype='float32') / 255
filtered_img = img.transpose(2, 0, 1).reshape(1, 3, 512, 512)

plt.axis('off')
plt.imshow(img)
plt.show()

for img in range(depth):
  fig = plt.figure()   
  plt.axis( 'off')   
  plt.imshow(filtered_img[0, img, :, :, ], cmap = cm.gray)
  plt.show()

print("------------------------------------------------------------")  # 60個

print("RGB - LAB 轉換")

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
cyan = [0, 255, 255]
magenta = [255, 0, 255]
yellow = [255, 255, 0]

import numpy as np
import skimage

def get_lab_from_rgb(color):
    rgb = np.array(color, dtype=np.uint8)
    lab = skimage.color.rgb2lab(rgb, illuminant="D65")
    print(lab)

get_lab_from_rgb(red)
get_lab_from_rgb(green)
get_lab_from_rgb(blue)
get_lab_from_rgb(cyan)
get_lab_from_rgb(magenta)
get_lab_from_rgb(yellow)




color = red
rgb = np.array(color, dtype=np.uint8)
lab = skimage.color.rgb2lab(rgb, illuminant="D65")
print(lab)





lab1 = [53.24058794, 80.09230823, 67.20275104]
lab2 = [ 87.73509949, -86.18302974,  83.17970318]
lab3 = [  32.29567257,   79.18559091, -107.85730021]
lab4 = [ 91.11330144, -48.09059623, -14.12632982]
lab5 = [ 60.32350653,  98.23305386, -60.82101524]
lab6 = [ 97.13950704, -21.55468102,  94.47812228]


def get_rgb_from_lab(lab):
    rgb = skimage.color.lab2rgb(lab, illuminant="D50")
    print(rgb)
    #print(round(rgb[0]*255))
    #print(round(rgb[1]*255))
    #print(round(rgb[2]*255))
    rgb = np.array(rgb*256, dtype=np.uint8)
    print(rgb)

"""    
rgb = skimage.color.lab2rgb(lab1, illuminant="D65")
#print(round(rgb[0]*255))
#print(round(rgb[1]*255))
#print(round(rgb[2]*255))
rgb = np.array(rgb*256, dtype=np.uint8)
print(rgb)
"""
get_rgb_from_lab(lab1)
get_rgb_from_lab(lab2)
get_rgb_from_lab(lab3)
get_rgb_from_lab(lab4)
get_rgb_from_lab(lab5)
get_rgb_from_lab(lab6)

print("------------------------------------------------------------")  # 60個


