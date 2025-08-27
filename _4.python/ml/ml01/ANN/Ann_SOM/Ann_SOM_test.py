# Ann_SOM_test.py

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

font_filename = "D:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
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


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# Analyzer.py

import csv

reader = csv.reader(file(r"/Users/alexander/temp/data1mt10000.csv", "rb"))
lastPositions = list()
i = 0
maxLastPosition = 0
maxI = 0
for row in reader:
    # print i
    i += 1
    lastChange = 0
    if i == 1:
        print(len(row))
    for position in range(len(row) - 1):
        if row[position] != row[position + 1]:
            lastChange = position
    lastPositions.append(lastChange)
    if maxLastPosition < lastChange:
        maxLastPosition = lastChange
        maxI = i
print(maxLastPosition)
print(maxI)

w = csv.writer(file(r"/Users/alexander/temp/lastChangePositions.csv", "wb"))
w.writerow(lastPositions)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# SOM Clustering

from ImageContainer import ImageContainer
from ImageContainer import ImagePattern

from SOM import SOM

imgContainer = ImageContainer()
imgContainer.fromDirectory("/Users/alexander/Pictures/qwe/")
# imgContainer.analyzeAll()
som = SOM(3, 5, 5, None)
som.clustering(imgContainer.images)

for image in imgContainer.images:
    print(som.coordinates(image))


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()


print("------------------------------------------------------------")  # 60個

