"""

PIL histogram

"""

import time
import glob
import shutil

from PIL import Image
from PIL import ImageDraw
from PIL import ImageOps
from PIL import ImageFont
from PIL import ImageFilter

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
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

print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
filename = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.bmp' #400X400
filename = '../opencv/data/pic_calcHist.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename)

plt.imshow(image1)
plt.title('原圖')
plt.show()

# PIL影像 => 灰階
image_gray = image1.convert('L')

plt.imshow(image_gray)
plt.title('灰階')
plt.show()

W, H = image_gray.size
print('原圖大小 W =', W, ', H =', H)

x_st = 30
y_st = 30
w = W - x_st * 2
h = H - y_st * 2
image_cropped = image_gray.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image_cropped)
plt.title('灰階 裁一塊')
plt.show()

image_cropped_hist = image_cropped.histogram()

W2, H2 = 320, 240
print('把原圖轉成', W2, 'X', H2, '大小')
image3 = image1.resize((W2, H2), Image.LANCZOS)# 使用 LANCZOS 調整影像大小

plt.imshow(image3)
plt.show()

image_gray = image3.convert('L')	#轉換成灰階圖像
hist = image_gray.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(image_cropped_hist))
ind = np.arange(0, len(image_cropped_hist))

plt.plot(ind, image_cropped_hist, color = 'cyan', label = 'cropped')
plt.plot(ind, hist, color = 'black', label = 'original')
plt.plot(ind, r_hist, color = 'red', label = 'Red Plane')
plt.plot(ind, g_hist, color = 'green', label = 'Green Plane')
plt.plot(ind, g_hist, color = 'blue', label = 'Blue Plane')

plt.xlim(0-10, 256+10)
plt.ylim(0, 4500+2000+2000)
plt.legend()

plt.show()

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個


