import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

''' ok
d1 = [10 for y in range(1, 9)]          # data1線條之y值
d2 = [20 for y in range(1, 9)]          # data2線條之y值
d3 = [30 for y in range(1, 9)]          # data3線條之y值
d4 = [40 for y in range(1, 9)]          # data4線條之y值
d5 = [50 for y in range(1, 9)]          # data5線條之y值
d6 = [60 for y in range(1, 9)]          # data6線條之y值
d7 = [70 for y in range(1, 9)]          # data7線條之y值
d8 = [80 for y in range(1, 9)]          # data8線條之y值
d9 = [90 for y in range(1, 9)]          # data9線條之y值
d10 = [100 for y in range(1, 9)]        # data10線條之y值
d11 = [110 for y in range(1, 9)]        # data11線條之y值
d12 = [120 for y in range(1, 9)]        # data12線條之y值

seq = [1, 2, 3, 4, 5, 6, 7, 8]
plt.plot(seq,d1,'-1',seq,d2,'-2',seq,d3,'-3',seq,d4,'-4',
         seq,d5,'-s',seq,d6,'-p',seq,d7,'-*',seq,d8,'-+',
         seq,d9,'-D',seq,d10,'-d',seq,d11,'-H',seq,d12,'-h')   
plt.show()
'''

print('------------------------------------------------------------')	#60個

'''
plt.plot(0, 1, '-o')    #在 (0, 1) 上 畫一點


#畫點
plt.plot(1, 5, 'r-o')
plt.plot(2, 10, 'r-o')
plt.plot(3, 20, 'r-o')





plt.show()
'''
print('------------------------------------------------------------')	#60個

#opencv
filename = 'C:/_git/vcs/_1.data/______test_files1/picture1.jpg'

import matplotlib.pyplot as plt
import cv2

image = cv2.imread(filename)	#讀取本機圖片

#plt.imshow(image)#直接顯示 影像錯誤 因為opencv的imread讀出來是BGR排列
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))#先轉換成RGB再顯示


plt.show()


print('------------------------------------------------------------')	#60個





