"""
skimage : scikit-image SciKit (toolkit for SciPy)


"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


"""
#圖像的繪制
實際上前面我們就已經用到了圖像的繪制，如：
io.imshow(img)  
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

from skimage import io,data
img=data.astronaut()
dst=io.imshow(img)
print(type(dst))
io.show()

#可以看到，類型是'matplotlib.image.AxesImage'。顯示一張圖片，我們通常更愿意這樣寫：

import matplotlib.pyplot as plt
from skimage import io,data
img=data.astronaut()
plt.imshow(img)
plt.show()


print('------------------------------------------------------------')	#60個

 
"""
matplotlib是一個專業繪圖的庫，相當于matlab中的plot,可以設置多個figure窗口,設置figure的標題，隱藏坐標尺，甚至可以使用subplot在一個figure中顯示多張圖片。一般我們可以這樣導入matplotlib庫：

import matplotlib.pyplot as plt

也就是說，我們繪圖實際上用的是matplotlib包的pyplot模塊。

一、用figure函數和subplot函數分別創建主窗口與子圖

例:分開并同時顯示宇航員圖片的三個通道
"""

from skimage import data
import matplotlib.pyplot as plt
img=data.astronaut()
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
#除了上面那種方法創建顯示窗口和劃分子圖，還有另外一種編寫方法也可以，
#如下例: 

import matplotlib.pyplot as plt
from skimage import data,color

img = data.immunohistochemistry()
hsv = color.rgb2hsv(img)

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
from skimage import data
from skimage.viewer import ImageViewer

img = data.coins()
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

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個

