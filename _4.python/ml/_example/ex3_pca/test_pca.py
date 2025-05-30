"""
test pca

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

print("------------------------------------------------------------")  # 60個


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# eigencog_face.py

from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")


ef.compute()
E = []
X = np.mat(np.zeros((10, 10304)))
for i in range(16):
    X = ef.Mat[i * 10 : (i + 1) * 10, :].copy()
    # X = ef.normalize(X.mean(axis =0),0,255)
    X = X.mean(axis=0)
    imgs = X.reshape(112, 92)
    E.append(imgs)
ef.subplot(title="AT&T Eigen Facedatabase", images=E)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# eigencog_test.py

from pca import *

ef = Eigenfaces()
ef.dist_metric = ef.distEclud
ef.loadimgs("orl_faces/")

ef.compute()
# 创建测试集
testImg = ef.X[30]
print("实际值 =", ef.y[30], "->", "预测值 =", ef.predict(testImg))

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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


print("------------------------------------------------------------")  # 60個
