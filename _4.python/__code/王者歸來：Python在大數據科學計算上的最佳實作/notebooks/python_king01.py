
"""


"""

import os
import sys
import time
import random
import numpy as np
import pandas as pd

print("------------------------------------------------------------")  # 60個

# 電影打分資料MovieLens中讀入使用者資料

import pandas as pd
columns = 'user_id', 'age', 'sex', 'occupation', 'zip_code'
df = pd.read_csv("data/ml-100k/u.user", 
                 delimiter="|", header=None, names=columns)
print(df.head())

""" fail
#%fig=使用Pandas統計電影打分使用者的職業
df.groupby("occupation").age.mean().order().plot(kind="bar", figsize=(12, 4));
"""

print("------------------------------------------------------------")  # 60個

"""
在下面的實例中，讀入圖形moon.jpg，並轉為二值圖形。
找到二值圖中黑白區域相交的邊線，並計算其周長和面積。
然後透過這兩個參數計算pi。

"""

import cv2

img = cv2.imread("data/moon.jpg", cv2.IMREAD_GRAYSCALE)
_, bimg = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)
contour, _ = cv2.findContours(bimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_L1)
contour = cv2.approxPolyDP(contour[0], epsilon=2, closed=False)
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour, True)
cc = perimeter**2 / (4 * area)
print(cc)


print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個



