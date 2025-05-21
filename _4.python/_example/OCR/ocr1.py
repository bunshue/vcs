"""



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
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個

"""
pyocr：簡單易用OCR

!apt install tesseract-ocr libtesseract-dev tesseract-ocr
!pip install pyocr
"""

import pyocr
from PIL import Image

tools = pyocr.get_available_tools()
# print(tools)
if len(tools) == 0:
    print("沒有可用的OCR！")
else:
  tool = tools[0]
  txt = tool.image_to_string(
      Image.open('text1.jpg'),
      builder=pyocr.builders.TextBuilder()
  )
  print("辨識文字：{}".format(txt))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
keras-ocr模組：效果強大OCR

!pip install keras-ocr
"""

import keras_ocr

pipeline = keras_ocr.pipeline.Pipeline()
images = []
imgfiles = [
    'ad1.jpg',
    # 'ad02.jpg',
]
for imgfile in imgfiles:
    print('加入辨識圖片 :', imgfile)
    images.append(keras_ocr.tools.read(imgfile))
prediction_groups = pipeline.recognize(images)
#print(len(prediction_groups))
# print(prediction_groups)

_, axs = plt.subplots(ncols=len(images), figsize=(12, 8))
for i in range(len(prediction_groups)):
    if len(prediction_groups) == 1:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs)
    else:
        keras_ocr.tools.drawAnnotations(image=images[i], predictions=prediction_groups[i], ax=axs[i])

plt.show()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
