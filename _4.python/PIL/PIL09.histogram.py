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

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

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

print("------------------------------------------------------------")  # 60個
print('------------------------------------------------------------')	#60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

# 檔案 => PIL影像
image1 = Image.open(filename)    #PIL讀取本機圖片, 讀取的是RGB格式的圖片
#print('顯示原圖')
#plt.imshow(image1)
#plt.show()

# PIL影像 => 灰階
image1g = image1.convert('L')	#轉換成灰階圖像
plt.imshow(image1g)      #灰階圖
plt.show()

W, H = image1g.size
print('原圖大小 W =', W, ', H =', H)

x_st = 100
y_st = 200
w = 200
h = 200
image2 = image1g.crop((x_st, y_st, x_st + w, y_st + h))

plt.imshow(image2)
plt.show()

image2_hist = image2.histogram()

W2, H2 = 400, 200
print('把原圖轉成', W2, 'X', H2, '大小')
image3 = image1.resize((W2, H2), Image.LANCZOS)# 使用 LANCZOS 調整影像大小

plt.imshow(image3)
plt.show()

image1g = image3.convert('L')	#轉換成灰階圖像
hist = image1g.histogram()

r, g, b = image3.split()   #r, g, b為三個通道的list
print('r', r)
print('g', g)
print('b', b)
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(image2_hist))
ind = np.arange(0, len(image2_hist))

plt.plot(ind, image2_hist, color = 'cyan', label = 'cropped')
plt.plot(ind, hist, color = 'black', lw = 2, label = 'original')
plt.plot(ind, r_hist, color = 'red', label = 'Red Plane')
plt.plot(ind, g_hist, color = 'green', label = 'Green Plane')
plt.plot(ind, g_hist, color = 'blue', label = 'Blue Plane')
plt.xlim(0-10, 256+10)
plt.ylim(0, 8000)
plt.legend()

plt.show()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個


