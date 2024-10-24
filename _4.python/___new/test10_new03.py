"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個
"""
import glob,cv2

foldername = "animal"
 
#建立測試資料
filenames = glob.glob(foldername + '/*.jpg') + glob.glob(foldername + '/*.png')

for filename in filenames:
    print(filename)



print("------------------------------------------------------------")  # 60個

filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

#filename = 'C:/_git/vcs/_4.python/_data/picture1.jpg'

os.system(filename)  # 用系統內建的程式開啟檔案

"""

print("------------------------------------------------------------")  # 60個

print("統計一串英文字串個字母出現的頻率")

from collections import defaultdict

text = "this is a lion-mouse"

frequency = defaultdict(int)
for symbol in text:
    frequency[symbol] += 1
print(frequency)

heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
print(heap)

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

