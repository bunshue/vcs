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

'''

"""
高級形態學處理

形態學處理，除了最基本的膨脹、腐蝕、開/閉運算、黑/白帽處理外，還有一些更高級的運用，如凸包，連通區域標記，刪除小塊區域等。

1、凸包

凸包是指一個凸多邊形，這個凸多邊形將圖片中所有的白色像素點都包含在內。

函數為：

skimage.morphology.convex_hull_image(image)

輸入為二值圖像，輸出一個邏輯二值圖像。在凸包內的點為True, 否則為False

"""
""" pic NG
import matplotlib.pyplot as plt
from skimage import data,color,morphology

#生成二值測試圖像
img=color.rgb2gray(data.horse())
img=(img<0.5)*1

chull = morphology.convex_hull_image(img)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(img,plt.cm.gray)
ax0.set_title('original image')

ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

plt.show()
"""

"""
convex_hull_image()是將圖片中的所有目標看作一個整體，因此計算出來只有一個最小凸多邊形。如果圖中有多個目標物體，每一個物體需要計算一個最小凸多邊形，則需要使用convex_hull_object（）函數。

函數格式：skimage.morphology.convex_hull_object(image, neighbors=8)

輸入參數image是一個二值圖像，neighbors表示是采用4連通還是8連通，默認為8連通。

"""

""" NG
import matplotlib.pyplot as plt
from skimage import data,color,morphology,feature

#生成二值測試圖像
img=color.rgb2gray(data.coins())
#檢測canny邊緣,得到二值圖片
edgs=feature.canny(img, sigma=3, low_threshold=10, high_threshold=50) 

chull = morphology.convex_hull_object(edgs)

#繪制輪廓
fig, axes = plt.subplots(1,2,figsize=(8,8))
ax0, ax1= axes.ravel()
ax0.imshow(edgs,plt.cm.gray)
ax0.set_title('many objects')
ax1.imshow(chull,plt.cm.gray)
ax1.set_title('convex_hull image')

plt.show()
"""


"""
2、連通區域標記

在二值圖像中，如果兩個像素點相鄰且值相同（同為0或同為1），那么就認為這兩個像素點在一個相互連通的區域內。而同一個連通區域的所有像素點，都用同一個數值來進行標記，這個過程就叫連通區域標記。在判斷兩個像素是否相鄰時，我們通常采用4連通或8連通判斷。在圖像中，最小的單位是像素，每個像素周圍有8個鄰接像素，常見的鄰接關系有2種：4鄰接與8鄰接。4鄰接一共4個點，即上下左右，如下左圖所示。8鄰接的點一共有8個，包括了對角線位置的點，如下右圖所示。

在skimage包中，我們采用measure子模塊下的label（）函數來實現連通區域標記。

函數格式：

skimage.measure.label（image,connectivity=None)

參數中的image表示需要處理的二值圖像，connectivity表示連接的模式，1代表4鄰接，2代表8鄰接。

輸出一個標記數組（labels), 從0開始標記。

"""

import numpy as np
import scipy.ndimage as ndi
from skimage import measure,color
import matplotlib.pyplot as plt

#編寫一個函數來生成原始二值圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成網絡
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯濾波
    return mask > mask.mean()

data = microstructure(l=128)*1 #生成測試圖片

labels=measure.label(data,connectivity=2)  #8連通區域標記
dst=color.label2rgb(labels)  #根據不同的標記顯示不同的顏色
print('regions number:',labels.max()+1)  #顯示連通區域塊數(從0開始標記)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax1.axis('off')
ax2.imshow(dst,interpolation='nearest')
ax2.axis('off')

fig.tight_layout()
plt.show()

"""
在代碼中，有些地方乘以1，則可以將bool數組快速地轉換為int數組。

結果如圖：有10個連通的區域，標記為0-9

如果想分別對每一個連通區域進行操作，比如計算面積、外接矩形、凸包面積等，則需要調用measure子模塊的regionprops（）函數。該函數格式為：

skimage.measure.regionprops(label_image)

返回所有連通區塊的屬性列表，常用的屬性列表如下表：
屬性名稱 	類型 	描述
area 	int 	區域內像素點總數
bbox 	tuple 	邊界外接框(min_row, min_col, max_row, max_col)
centroid 	array　　 	質心坐標
convex_area 	int 	凸包內像素點總數
convex_image 	ndarray 	和邊界外接框同大小的凸包　　
coords 	ndarray 	區域內像素點坐標
Eccentricity  	float 	離心率
equivalent_diameter  	float 	和區域面積相同的圓的直徑
euler_number 	int　　 	區域歐拉數
extent  	float 	區域面積和邊界外接框面積的比率
filled_area 	int 	區域和外接框之間填充的像素點總數
perimeter  	float 	區域周長
label 	int 	區域標記

3、刪除小塊區域

有些時候，我們只需要一些大塊區域，那些零散的、小塊的區域，我們就需要刪除掉，則可以使用morphology子模塊的remove_small_objects（)函數。

函數格式：skimage.morphology.remove_small_objects(ar, min_size=64, connectivity=1, in_place=False)

參數：

ar: 待操作的bool型數組。

min_size: 最小連通區域尺寸，小于該尺寸的都將被刪除。默認為64.

connectivity: 鄰接模式，1表示4鄰接，2表示8鄰接

in_place: bool型值，如果為True,表示直接在輸入圖像中刪除小塊區域，否則進行復制后再刪除。默認為False.

返回刪除了小塊區域的二值圖像。
"""

import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#編寫一個函數來生成原始二值圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]  #生成網絡
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n)) #高斯濾波
    return mask > mask.mean()

data = microstructure(l=128) #生成測試圖片

dst=morphology.remove_small_objects(data,min_size=300,connectivity=1)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, plt.cm.gray, interpolation='nearest')
ax2.imshow(dst,plt.cm.gray,interpolation='nearest')

fig.tight_layout()
plt.show()

"""
在此例中，我們將面積小于300的小塊區域刪除（由1變為0），結果如下圖：

 4、綜合示例：閾值分割+閉運算+連通區域標記+刪除小區塊+分色顯示
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from skimage import data,filters,segmentation,measure,morphology,color

#加載并裁剪硬幣圖片
image = data.coins()[50:-50, 50:-50]

thresh =filters.threshold_otsu(image) #閾值分割
bw =morphology.closing(image > thresh, morphology.square(3)) #閉運算

cleared = bw.copy()  #復制
segmentation.clear_border(cleared)  #清除與邊界相連的目標物

label_image =measure.label(cleared)  #連通區域標記
borders = np.logical_xor(bw, cleared) #異或
label_image[borders] = -1
image_label_overlay =color.label2rgb(label_image, image=image) #不同標記用不同顏色顯示

fig,(ax0,ax1)= plt.subplots(1,2, figsize=(8, 6))
ax0.imshow(cleared,plt.cm.gray)
ax1.imshow(image_label_overlay)

for region in measure.regionprops(label_image): #循環得到每一個連通區域屬性集
    
    #忽略小區域
    if region.area < 100:
        continue

    #繪制外包矩形
    minr, minc, maxr, maxc = region.bbox
    rect = mpatches.Rectangle((minc, minr), maxc - minc, maxr - minr,
                              fill=False, edgecolor='red', linewidth=2)
    ax1.add_patch(rect)
fig.tight_layout()
plt.show()

'''

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

"""
骨架提取與分水嶺算法

骨架提取與分水嶺算法也屬于形態學處理范疇，都放在morphology子模塊內。

1、骨架提取

骨架提取，也叫二值圖像細化。這種算法能將一個連通區域細化成一個像素的寬度，用于特征提取和目標拓撲表示。

morphology子模塊提供了兩個函數用于骨架提取，分別是Skeletonize（）函數和medial_axis（）函數。我們先來看Skeletonize（）函數。

格式為：skimage.morphology.skeletonize(image)

輸入和輸出都是一幅二值圖像。
"""

from skimage import morphology,draw
import numpy as np
import matplotlib.pyplot as plt

#創建一個二值圖像用于測試
image = np.zeros((400, 400))

#生成目標對象1(白色U型)
image[10:-10, 10:100] = 1
image[-100:-10, 10:-10] = 1
image[10:-10, -100:-10] = 1

#生成目標對象2（X型）
rs, cs = draw.line(250, 150, 10, 280)
for i in range(10):
    image[rs + i, cs] = 1
rs, cs = draw.line(10, 150, 250, 280)
for i in range(20):
    image[rs + i, cs] = 1

#生成目標對象3（O型）
ir, ic = np.indices(image.shape)
circle1 = (ic - 135)**2 + (ir - 150)**2 < 30**2
circle2 = (ic - 135)**2 + (ir - 150)**2 < 20**2
image[circle1] = 1
image[circle2] = 0

#實施骨架算法
skeleton =morphology.skeletonize(image)

#顯示結果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()

"""
生成一幅測試圖像，上面有三個目標對象，分別進行骨架提取，結果如下：

例2：利用系統自帶的馬圖片進行骨架提取
"""

""" pic NG
from skimage import morphology,data,color
import matplotlib.pyplot as plt

image=color.rgb2gray(data.horse())
image=1-image #反相
#實施骨架算法
skeleton =morphology.skeletonize(image)

#顯示結果
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))

ax1.imshow(image, cmap=plt.cm.gray)
ax1.axis('off')
ax1.set_title('original', fontsize=20)

ax2.imshow(skeleton, cmap=plt.cm.gray)
ax2.axis('off')
ax2.set_title('skeleton', fontsize=20)

fig.tight_layout()
plt.show()
"""

"""
medial_axis就是中軸的意思，利用中軸變換方法計算前景（1值）目標對象的寬度，格式為：

skimage.morphology.medial_axis(image, mask=None, return_distance=False)

mask: 掩模。默認為None, 如果給定一個掩模，則在掩模內的像素值才執行骨架算法。

return_distance: bool型值，默認為False. 如果為True, 則除了返回骨架，還將距離變換值也同時返回。這里的距離指的是中軸線上的所有點與背景點的距離。
"""

import numpy as np
import scipy.ndimage as ndi
from skimage import morphology
import matplotlib.pyplot as plt

#編寫一個函數，生成測試圖像
def microstructure(l=256):
    n = 5
    x, y = np.ogrid[0:l, 0:l]
    mask = np.zeros((l, l))
    points = l * np.random.rand(2, n**2)
    mask[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
    mask = ndi.gaussian_filter(mask, sigma=l/(4.*n))
    return mask > mask.mean()

data = microstructure(l=64) #生成測試圖像

#計算中軸和距離變換值
skel, distance =morphology.medial_axis(data, return_distance=True)

#中軸上的點到背景像素點的距離
dist_on_skel = distance * skel

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
ax1.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
#用光譜色顯示中軸
#ax2.imshow(dist_on_skel, cmap=plt.cm.spectral, interpolation='nearest')
ax2.imshow(dist_on_skel, interpolation='nearest')
ax2.contour(data, [0.5], colors='w')  #顯示輪廓線

fig.tight_layout()
plt.show()

"""
2、分水嶺算法

分水嶺在地理學上就是指一個山脊，水通常會沿著山脊的兩邊流向不同的“匯水盆”。分水嶺算法是一種用于圖像分割的經典算法，是基于拓撲理論的數學形態學的分割方法。如果圖像中的目標物體是連在一起的，則分割起來會更困難，分水嶺算法經常用于處理這類問題，通常會取得比較好的效果。

分水嶺算法可以和距離變換結合，尋找“匯水盆地”和“分水嶺界限”，從而對圖像進行分割。二值圖像的距離變換就是每一個像素點到最近非零值像素點的距離，我們可以使用scipy包來計算距離變換。

在下面的例子中，需要將兩個重疊的圓分開。我們先計算圓上的這些白色像素點到黑色背景像素點的距離變換，選出距離變換中的最大值作為初始標記點（如果是反色的話，則是取最小值），從這些標記點開始的兩個匯水盆越集越大，最后相交于分山嶺。從分山嶺處斷開，我們就得到了兩個分離的圓。

例1：基于距離變換的分山嶺圖像分割
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature

#創建兩個帶有重疊圓的圖像
x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1)**2 + (y - y1)**2 < r1**2
mask_circle2 = (x - x2)**2 + (y - y2)**2 < r2**2
image = np.logical_or(mask_circle1, mask_circle2)

#現在我們用分水嶺算法分離兩個圓
distance = ndi.distance_transform_edt(image) #距離變換
#local_maxi =feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
#                            labels=image)   #尋找峰值
local_maxi =feature.peak_local_max(distance, footprint=np.ones((3, 3)),
                            labels=image)   #尋找峰值

markers = ndi.label(local_maxi)[0] #初始標記點
"""沒有watershed
labels =morphology.watershed(-distance, markers, mask=image) #基于距離變換的分水嶺算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(-distance, cmap=plt.cm.jet, interpolation='nearest')
ax1.set_title("Distance")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()
"""

"""

分水嶺算法也可以和梯度相結合，來實現圖像分割。一般梯度圖像在邊緣處有較高的像素值，而在其它地方則有較低的像素值，理想情況 下，分山嶺恰好在邊緣。因此，我們可以根據梯度來尋找分山嶺。

例2：基于梯度的分水嶺圖像分割
"""

""" pic NG
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,color,data,filters

image =color.rgb2gray(data.camera())
denoised = filter.rank.median(image, morphology.disk(2)) #過濾噪聲

#將梯度值低于10的作為開始標記點
markers = filters.rank.gradient(denoised, morphology.disk(5)) <10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denoised, morphology.disk(2)) #計算梯度
labels =morphology.watershed(gradient, markers, mask=image) #基于梯度的分水嶺算法

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6, 6))
axes = axes.ravel()
ax0, ax1, ax2, ax3 = axes

ax0.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
ax0.set_title("Original")
ax1.imshow(gradient, cmap=plt.cm.spectral, interpolation='nearest')
ax1.set_title("Gradient")
ax2.imshow(markers, cmap=plt.cm.spectral, interpolation='nearest')
ax2.set_title("Markers")
ax3.imshow(labels, cmap=plt.cm.spectral, interpolation='nearest')
ax3.set_title("Segmented")

for ax in axes:
    ax.axis('off')

fig.tight_layout()
plt.show()

"""

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
