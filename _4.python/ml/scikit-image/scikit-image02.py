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

skimage 內建圖片位置
astronaut	      宇航員圖片      coffee	            一杯咖啡圖片
lena(x)               lena美女圖片    camera	            拿相機的人圖片
coins	              硬幣圖片        moon	            月亮圖片
checkerboard	      棋盤圖片        horse	            馬圖片
page	              書頁圖片        chelsea	            小貓圖片
hubble_deep_field     星空圖片        text	            文字圖片
clock	              時鐘圖片        immunohistochemistry  結腸圖片

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


filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

from skimage import io
img=io.imread(filename)
io.imshow(img)

plt.show()


from skimage import io
img=io.imread(filename, True)   #True:轉為灰階
io.imshow(img)
plt.show()


from skimage import data    #圖片資料模組
from skimage import color   #色彩處理模組

img = data.astronaut()
io.imshow(img)
plt.show()

img =color.rgb2gray(img)
io.imshow(img)
plt.show()

from skimage import data_dir
print('skimage內建圖片位置 :', data_dir)

'''
#存圖
from skimage import io,data
img = data.astronaut()
img = data.chelsea()
io.imshow(img)
plt.show()
io.imsave('mmmm.jpg',img)  #依副檔名轉換圖片格式存檔

print('------------------------------------------------------------')	#60個

print('打印圖片訊息')
from skimage import io,data
img=data.chelsea()
io.imshow(img)
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

from skimage import io,data
img=data.chelsea()
pixel=img[20,30,1]
print(pixel)


#顯示紅色單通道圖片

from skimage import io,data
img=data.chelsea()
R=img[:,:,0]
io.imshow(R)


#修改像素值
#對小貓圖片隨機添加椒鹽噪聲

from skimage import io,data
import numpy as np
img=data.chelsea()

#隨機生成5000個椒鹽
rows,cols,dims=img.shape
for i in range(5000):
    x=np.random.randint(0,rows)
    y=np.random.randint(0,cols)
    img[x,y,:]=255
    
io.imshow(img)
plt.show()



print('------------------------------------------------------------')	#60個

#通過對數組的裁剪，就可以實現對圖片的裁剪。
#對小貓圖片進行裁剪

from skimage import io,data
img=data.chelsea()
roi=img[80:180,100:200,:]
io.imshow(roi)
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

from skimage import io,data,color
#img = data.astronaut()
img = data.chelsea()
img_gray=color.rgb2gray(img)
rows,cols=img_gray.shape
for i in range(rows):
    for j in range(cols):
        if (img_gray[i,j]<=0.5):
            img_gray[i,j]=0
        else:
            img_gray[i,j]=1
io.imshow(img_gray)
plt.show()

#這個例子，使用了color模塊的rgb2gray（）函數，將彩色三通道圖片轉換成灰度圖。轉換結果為float64類型的數組，范圍為[0,1]之間。

from skimage import io, data
img = data.chelsea()
reddish = img[:, :, 0] >170
img[reddish] = [0, 255, 0]
io.imshow(img)
plt.show()

#這個例子先對R通道的所有像素值進行判斷，如果大于170，則將這個地方的像素值變為[0,255,0], 即G通道值為255，R和B通道值為0。


'''


print('------------------------------------------------------------')	#60個

#圖像數據類型及顏色空間轉換


#數據類型
from skimage import io,data
img=data.chelsea()
print(img.dtype.name)


#顏色空間及其轉換
#通過圖像的顏色空間轉換來改變數據類型。
#常用的顏色空間有灰度空間、rgb空間、hsv空間和cmyk空間。顏色空間轉換以后，圖片類型都變成了float型。
#所有的顏色空間轉換函數，都放在skimage的color模塊內。

#rgb轉灰度圖

from skimage import io,data,color
img=data.chelsea()
gray=color.rgb2gray(img)
io.imshow(gray)
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
from skimage import io,data,color
img=data.chelsea()
hsv=color.convert_colorspace(img,'RGB','HSV')
io.imshow(hsv)

"""


print('------------------------------------------------------------')	#60個

#在color模塊的顏色空間轉換函數中，還有一個比較有用的函數是
#skimage.color.label2rgb(arr), 可以根據標簽值對圖片進行著色。以后的圖片分類后著色就可以用這個函數。
#例：將astronaut圖片分成三類，然后用默認顏色對三類進行著色

from skimage import io,data,color
import numpy as np
img=data.astronaut()
gray=color.rgb2gray(img)
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
dst=color.label2rgb(labels)
io.imshow(dst)
plt.show()

print('------------------------------------------------------------')	#60個
