import sys
import matplotlib.pyplot as plt
import numpy as np
import math

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


print('PM2.5與風向之關聯性')

import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_excel('abc.xlsx')

x=df.WindDirec

y=df.PM25

plt.scatter(x,y)

plt.show()

"""
由於政府公開資料的格式問題，導致風向與PM2.5的視覺化呈現有困難(僅每小時資料提供風向)
因此風向與PM2.5關聯性，將改以文獻閱讀為主
"""

from IPython.display import Image

from IPython.core.display import HTML 

PATH = "PM25.png"                          #圖片路徑

Image(filename = PATH , width=600, height=600) 

from IPython.display import Image

from IPython.core.display import HTML 

PATH2 = "wind-direction.png"                          #圖片路徑

Image(filename = PATH2 , width=600, height=600)   



print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個
print('作業完成')
print('------------------------------------------------------------')	#60個

