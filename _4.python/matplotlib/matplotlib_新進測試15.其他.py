# matplotlib_新進測試14_其他

import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個


import os
import time
import random

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("箱圖")

# Creating dataset
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

fig = plt.figure(figsize=(10, 7))

# 圖加軸
ax = fig.add_axes([0, 0, 1, 1])

bp = ax.boxplot(data, labels=["mu = 100", "mu = 90", "mu = 80", "mu = 70"])
ax.set_title("Box plot")

plt.show()

print("------------------------------------------------------------")  # 60個

print("subplot 100張圖")

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

import matplotlib.image as img

# print('使用 matplotlib 顯示一圖')
image = img.imread(filename)

N = 100
for i in range(N):
    plt.subplot(10, N // 10, i + 1)
    plt.imshow(image)

plt.show()

print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個

# 導出圖表

from io import BytesIO
from lxml import etree
import base64
import webbrowser

data = pd.DataFrame({'id':['1','2','3','4','5'], # 構造數據
                     'math':[90,89,99,78,63],
                     'english':[89,94,80,81,94]})
plt.plot(data['math']) # matplotlib做圖
plt.plot(data['english'])

# 保存圖片（與網頁顯示無關）
plt.savefig('導出圖表.jpg',dpi=300)

# 保存網頁
buffer = BytesIO()
plt.savefig(buffer)  
plot_data = buffer.getvalue()

imb = base64.b64encode(plot_data)  # 生成網頁內容
ims = imb.decode()
imd = "data:image/png;base64,"+ims
data_im = """<h1>Figure</h1>  """ + """<img src="%s">""" % imd   
data_des = """<h1>Describe</h1>"""+data.describe().T.to_html()
root = "<title>Dataset</title>"
root = root + data_des + data_im

html = etree.HTML(root)
tree = etree.ElementTree(html)
tree.write('導出圖表.html')
#使用默認瀏覽器打開 html 文件
webbrowser.open('導出圖表.html',new = 1)

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

