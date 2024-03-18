"""
PIL 基本使用 pixel處理


"""

import os
import sys
import time
import random
import matplotlib.pyplot as plt
from PIL import Image   # Importing Image class from PIL module

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

print("操作像素, 使用 putpixel 修改一塊")

image = Image.open(filename)
for x in range(100, 200):
    for y in range(250, 350):
        image.putpixel((x, y), (255, 0, 0))

plt.imshow(image)
plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個

print("------------------------------------------------------------")  # 60個

print('萃取圖片的輪廓')

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片

#全彩轉灰階
image1 = image1.convert("L")

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

plt.subplot(121)
plt.imshow(image1)
plt.title('原圖')

plt.subplot(122)
plt.imshow(image2)
plt.title('萃取圖片的輪廓')

plt.show()



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

