"""
scikit-image


"""

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

filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

print("------------------------------------------------------------")  # 60個

import skimage as ski
print(ski.__version__)

print('------------------------------------------------------------')	#60個

from skimage import data

image=data.coffee()

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個

from skimage import data, color, feature
import skimage.data

image = data.checkerboard()

plt.imshow(image)

plt.show()

print('------------------------------------------------------------')	#60個
"""
import skimage

image = skimage.data.coins()
edges = skimage.filters.sobel(image)
skimage.io.imshow(edges)
skimage.io.show()
"""
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

print('顯示scikit-image所有預設圖片')

from skimage import data

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
    caller = getattr(data, name)
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
axs[0, 0].imshow(data.astronaut())
axs[0, 1].imshow(data.binary_blobs(), cmap=plt.cm.gray)
axs[0, 2].imshow(data.brick(), cmap=plt.cm.gray)
axs[1, 0].imshow(data.colorwheel())
axs[1, 1].imshow(data.camera(), cmap=plt.cm.gray)
axs[1, 2].imshow(data.cat())
axs[2, 0].imshow(data.checkerboard(), cmap=plt.cm.gray)
axs[2, 1].imshow(data.clock(), cmap=plt.cm.gray)
further_img = np.full((300, 300), 255)
for xpos in [100, 150, 200]:
    further_img[150 - 10 : 150 + 10, xpos - 10 : xpos + 10] = 0
axs[2, 2].imshow(further_img, cmap=plt.cm.gray)
plt.subplots_adjust(wspace=0.1, hspace=0.1)

plt.show()

print('------------------------------------------------------------')	#60個

''' 不知道做什麼
from skimage import data
ccc =  data.binary_blobs(length=5, blob_size_fraction=0.2)
print(ccc)

"""
array([[ True, False,  True,  True,  True],
       [ True,  True,  True, False,  True],
       [False,  True, False,  True,  True],
       [ True, False, False,  True,  True],
       [ True, False, False, False,  True]])
"""
blobs = data.binary_blobs(length=256, blob_size_fraction=0.1)
# Finer structures
blobs = data.binary_blobs(length=256, blob_size_fraction=0.05)
# Blobs cover a smaller volume fraction of the image
blobs = data.binary_blobs(length=256, volume_fraction=0.3)

'''

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


