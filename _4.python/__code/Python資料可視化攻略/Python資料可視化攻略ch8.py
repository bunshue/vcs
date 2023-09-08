import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns #海生, 自動把圖畫得比較好看
import plotly.offline
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots
import squarify

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei

#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

'''
Chapter8：資訊圖表的視覺化手法
何謂資訊圖表
象形圖
排列圖片的方法
資訊圖表使用的函式庫
'''



print('------------------------------------------------------------')	#60個

from PIL import Image, ImageOps
from IPython.display import display


#利用圖片大小強調數量多寡
#載入圖片與顯示圖片的範例


im = Image.open("fruit_momo.png")
display(im)


print('------------------------------------------------------------')	#60個


#調整圖片大小的範例

mini_im = im.resize((int(im.size[0] * 0.2), int(im.size[1] * 0.2)))
display(mini_im)
print(mini_im.size)


print('------------------------------------------------------------')	#60個

#利用圖片的個數強調數量

#以人形圖示的個數強調數量的範例


# 要排列的圖示個數
num = 10

# 圖片之間的邊界
margin = 5

# 載入圖片
im = Image.open("human.png")
im_width, im_height = im.size

# 將圖片入作為畫布使用的Image
canvas = Image.new("RGBA", ((im_width + margin) * num, im_height))
for i in range(num):
    canvas.paste(im, ((im_width + margin) * i, 0))

canvas



print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



