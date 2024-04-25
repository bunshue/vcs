"""

PIL histogram

"""

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

#把一張圖的RGB通道分開顯示出來

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'
filename = 'C:/_git/vcs/_1.data/______test_files1/ims01.bmp'
#filename = 'C:/_git/vcs/_4.python/opencv/data/RGB_R.bmp' #400X400
#filename = '../opencv/data/pic_calcHist.jpg'
filename = "C:/_git/vcs/_4.python/_data/eq1.bmp"  # 560X400
#filename = "C:/_git/vcs/_4.python/_data/eq3.bmp"  # 480X360
#filename = "C:/_git/vcs/_4.python/_data/eq4.bmp"  # 480X360

plt.figure(
    num="配合圖形遮罩計算直方圖",
    figsize=(12, 8),
    dpi=100,
    facecolor="whitesmoke",
    edgecolor="r",
    linewidth=1,
    frameon=True,
)

plt.subplot(211)
# 檔案 => PIL影像
image1 = Image.open(filename)
plt.imshow(image1)

# PIL影像 => 灰階
# 灰階才能做histogram處理
image2 = image1.convert('L')	#轉換成灰階圖像

plt.subplot(212)

image2_hist = image2.histogram()
print('len = ', len(image2_hist))
index = np.arange(0, len(image2_hist))
plt.plot(index, image2_hist, color = 'yellow', label = '原圖灰階', linewidth = 2)

print('RGB影像不可以做histogram, 分離成獨立通道後才可以做histogram')
r, g, b = image1.split()   #r, g, b為三個通道的list
r_hist = r.histogram()
g_hist = g.histogram()
b_hist = b.histogram()

print('len = ', len(r_hist))
index = np.arange(0, len(r_hist))

plt.plot(index, r_hist, color = 'red', label = 'R 通道')
plt.plot(index, g_hist, color = 'green', label = 'G 通道')
plt.plot(index, b_hist, color = 'blue', label = 'B 通道')

plt.xlim(0-10, 256+10)
plt.ylim(0, 4500+2000+2000)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個



