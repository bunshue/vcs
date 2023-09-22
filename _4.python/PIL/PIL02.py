'''

PIL 圖片相關的處理

有 影像處理

濾鏡



'''

import sys
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print('------------------------------------------------------------')	#60個


print('萃取圖片的輪廓')

import matplotlib.pyplot as plt
from PIL import Image

# 讀入圖片
filename = 'C:/_git/vcs/_1.data/______test_files1/_image_processing/sample2.png'
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

# 輸出用
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

print('測試 濾鏡 filter')

from PIL import ImageFilter

image = Image.open(filename)     # 建立Pillow物件

print('ImageFilter.BLUR')
filterPict = image.filter(ImageFilter.BLUR)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.CONTOUR')
filterPict = image.filter(ImageFilter.CONTOUR)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.DETAIL')
filterPict = image.filter(ImageFilter.DETAIL)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EDGE_ENHANCE')
filterPict = image.filter(ImageFilter.EDGE_ENHANCE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EDGE_ENHANCE_MORE')
filterPict = image.filter(ImageFilter.EDGE_ENHANCE_MORE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.EMBOSS')
filterPict = image.filter(ImageFilter.EMBOSS)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.FIND_EDGES')
filterPict = image.filter(ImageFilter.FIND_EDGES)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SMOOTH')
filterPict = image.filter(ImageFilter.SMOOTH)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SMOOTH_MORE')
filterPict = image.filter(ImageFilter.SMOOTH_MORE)
plt.imshow(filterPict)
plt.show()

print('ImageFilter.SHARPEN')
filterPict = image.filter(ImageFilter.SHARPEN)
plt.imshow(filterPict)
plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('完成')

