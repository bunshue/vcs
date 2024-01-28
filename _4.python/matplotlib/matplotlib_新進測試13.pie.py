# matplotlib_新進測試13_pie

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
import sys
import time
import random

print("------------------------------------------------------------")  # 60個


#派圖
data = {'apples': 10, 'oranges': 15, 'lemons': 5, 'limes': 20}
explode = (0, 0.1, 0, 0)  # 向外擴展顯示的區域
plt.pie(data.values(), explode=explode, labels=data.keys(), autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal') # 設置餅圖爲正圓形
plt.show()




print("------------------------------------------------------------")  # 60個


#sorts = ["Travel","Entertainment","Education","Transporation","Food"]
sorts = [u"交通",u"娛樂",u"教育",u"交通",u"餐費"]

fee = [8000,2000,3000,5000,6000]
          
plt.pie(fee,labels=sorts,explode=(0,0.2,0,0,0),
        autopct="%1.2f%%")      # 繪製圓餅圖

plt.show()





print("------------------------------------------------------------")  # 60個






print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個




print("------------------------------------------------------------")  # 60個


