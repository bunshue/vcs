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
圖像的批量處理

有些時候，我們不僅要對一張圖片進行處理，可能還會對一批圖片處理。這時候，我們可以通過循環來執行處理，也可以調用程序自帶的圖片集合來處理。

圖片集合函數為：

skimage.io.ImageCollection(load_pattern,load_func=None)

這個函數是放在io模塊內的，帶兩個參數，第一個參數load_pattern, 表示圖片組的路徑，可以是一個str字符串。第二個參數load_func是一個回調函數，我們對圖片進行批量處理就可以通過這個回調函數實現。回調函數默認為imread(),即默認這個函數是批量讀取圖片。

"""
'''
import skimage.io as io
from skimage import data_dir
string = data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string)
print(len(coll))


#表示資料夾內有 23 張圖

"""
顯示結果為25, 說明

系統自帶了23張png的示例圖片，這些圖片都讀取了出來，放在圖片集合coll里。
如果我們想顯示其中一張圖片，則可以在后加上一行代碼：
io.imshow(coll[10])

如果一個文件夾里，我們既存放了一些jpg格式的圖片，又存放了一些png格式的圖片，現在想把它們全部讀取出來，該怎么做呢?
"""
import skimage.io as io
from skimage import data_dir
#string='d:/pic/*.jpg:d:/pic/*.png'
string = data_dir + '/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string)
print(len(coll))

print('------------------------------------------------------------')	#60個

"""
注意這個地方'd:/pic/*.jpg:d:/pic/*.png' ，是兩個字符串合在一起的，第一個是'd:/pic/*.jpg', 第二個是'd:/pic/*.png' ，合在一起后，中間用冒號來隔開，這樣就可以把d:/pic/文件夾下的jpg和png格式的圖片都讀取出來。如果還想讀取存放在其它地方的圖片，也可以一并加進去，只是中間同樣用冒號來隔開。

io.ImageCollection()這個函數省略第二個參數，就是批量讀取。如果我們不是想批量讀取，而是其它批量操作，如批量轉換為灰度圖，那又該怎么做呢？

那就需要先定義一個函數，然后將這個函數作為第二個參數，如：
"""

from skimage import data_dir,io,color

def convert_gray(f):
    rgb=io.imread(f)
    return color.rgb2gray(rgb)
    
string = data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string,load_func=convert_gray)
io.imshow(coll[8])
plt.show()



print('------------------------------------------------------------')	#60個


#這種批量操作對視頻處理是極其有用的，因為視頻就是一系列的圖片組合


from skimage import data_dir, io,color

class AVILoader:
    video_file = 'myvideo.avi'

    def __call__(self, frame):
        return video_read(self.video_file, frame)

avi_load = AVILoader()

frames = range(0, 1000, 10) # 0, 10, 20, ...
ic =io.ImageCollection(frames, load_func=avi_load)


print('------------------------------------------------------------')	#60個


"""
這段代碼的意思，就是將myvideo.avi這個視頻中每隔10幀的圖片讀取出來，放在圖片集合中。

得到圖片集合以后，我們還可以將這些圖片連接起來，構成一個維度更高的數組，連接圖片的函數為：

skimage.io.concatenate_images(ic)

帶一個參數，就是以上的圖片集合，如：
"""
"""
from skimage import data_dir,io,color

coll = io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = io.ImageCollection(data_dir + '/*.png')
mat=io.concatenate_images(coll)

#使用concatenate_images(ic)函數的前提是讀取的這些圖片尺寸必須一致，否則會出錯。我們看看圖片連接前后的維度變化：

from skimage import data_dir,io,color

coll = io.ImageCollection('C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg')
#coll = io.ImageCollection(data_dir + '/*.png')
print(len(coll))      #連接的圖片數量
print(coll[0].shape)   #連接前的圖片尺寸，所有的都一樣
mat=io.concatenate_images(coll)
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

from skimage import data_dir,io,transform,color
import numpy as np

def convert_gray(f):
     rgb=io.imread(f)    #依次讀取rgb圖片
     gray=color.rgb2gray(rgb)   #將rgb圖片轉換成灰度圖
     dst=transform.resize(gray,(256,256))  #將灰度圖片大小轉換為256*256
     return dst
    
#string = data_dir+'/*.png'
string = 'C:/_git/vcs/_1.data/______test_files1/__pic/_angry_bird/*.jpg'
coll = io.ImageCollection(string,load_func=convert_gray)
print(len(coll))

for i in range(len(coll)):
    print(i)
    #io.imsave(str(i)+'.jpg', coll[i])  #循環保存圖片  fail
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

from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
dst=transform.resize(img, (80, 60))
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

from skimage import transform,data
img = data.camera()
print(img.shape)  #圖片原始大小 
print(transform.rescale(img, 0.1).shape)  #縮小為原來圖片大小的0.1倍
print(transform.rescale(img, [0.5,0.25]).shape)  #縮小為原來圖片行數一半，列數四分之一
print(transform.rescale(img, 2).shape)   #放大為原來圖片大小的2倍
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
from skimage import transform,data
import matplotlib.pyplot as plt
img = data.camera()
print(img.shape)  #圖片原始大小
img1=transform.rotate(img, 60) #旋轉90度，不改變大小 
print(img1.shape)
img2=transform.rotate(img, 30,resize=True)  #旋轉30度，同時改變大小
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

import numpy as np
import matplotlib.pyplot as plt
from skimage import data,transform

image = data.astronaut()  #載入宇航員圖片
rows, cols, dim = image.shape  #獲取圖片的行數，列數和通道數
pyramid = tuple(transform.pyramid_gaussian(image, downscale=2))  #產生高斯金字塔圖像
#共生成了log(512)=9幅金字塔圖像，加上原始圖像共10幅，pyramid[0]-pyramid[1]

"""
#composite_image = np.ones((rows, cols + cols / 2, 3), dtype=np.double)  #生成背景
composite_image = np.ones((rows, cols + 256, 3), dtype=np.double)  #生成背景
"""

"""
除了高斯金字塔外，還有其它的金字塔，如：
skimage.transform.pyramid_laplacian(image, downscale=2)
"""
