"""

Kaggle Cats and Dogs Dataset

"""

mnist_npz_filename = "C:/_git/vcs/_big_files/mnist.npz"

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


""" 將圖片分成兩大群
img_directory = 'C:/_git/vcs/_big_files/kagglecatsanddogs_5340/PetImages/'
validation_split = 0.1

import os
import random

subclasses = os.listdir(img_directory)

for subclass in subclasses:
    os.makedirs(img_directory + 'train/' + subclass, exist_ok=True)
    os.makedirs(img_directory + 'validation/' + subclass, exist_ok=True)
    for img in os.listdir(img_directory + subclass):
        rand = random.choices(['train/', 'validation/'], [1-validation_split, validation_split])[0]
        os.rename(img_directory + subclass + '/' + img, img_directory + rand + subclass + '/' + img)
    os.rmdir(img_directory + subclass)
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
