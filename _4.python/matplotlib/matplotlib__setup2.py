
'''
plt之基本設定

'''

import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個


import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

week = [0,1,2,3,4,5,6]
temperature = [23,25,29,31,26,30,24]
labels = ['Sunday','Monday','Tuesday','Wednesday',
          'Thursday','Friday','Saturday']

plt.xticks(week,labels,rotation=30) #字體加旋轉

plt.plot(temperature,"-o")
plt.title("一週的平均溫度", fontsize=24)
plt.xlabel("星期", fontsize=14)
plt.ylabel("溫度", fontsize=14)
plt.show()





'''



year = [2015,2016,2017,2018,2019]
plt.xticks(year)

plt.plot(year, city1, 'r-.s', lw=2, ms=10, label="台北")
plt.plot(year, city2, 'g--*', lw=2, ms=10, label="台中")





x = [0.5,1.0,10,50,100]
labels = ['A','B','C','D','E']
plt.xticks(x,labels)





xmin, xmax, ymin, ymax = plt.axis()
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"ymin = {ymin}")
print(f"ymax = {ymax}")


xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
print(f"xmin = {xmin}")
print(f"xmax = {xmax}")
print(f"ymin = {ymin}")
print(f"ymax = {ymax}")
plt.show()




調整x軸刻度
import matplotlib.pyplot as plt

x = [0.5,1.0,10,50,100]
y = [5,10,35,20,25]
value = range(len(x))
plt.plot(value,y,"-o")
plt.xticks(value,x)
plt.show()


調整x軸刻度
import matplotlib.pyplot as plt

x = [0.5,1.0,10,50,100]
y = [5,10,35,20,25]
value = range(len(x))
plt.plot(value,y,"-o")
plt.xticks(value,x)
plt.show()


調整x軸刻度
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數
plt.xticks(np.arange(0,7,step=0.5))
plt.plot(x, y1, color='c')          # 設定青色cyan            
plt.plot(x, y2, color='r')          # 設定紅色red
plt.show()

調整xy軸刻度
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 500)    # 建立含500個元素的陣列
y1 = np.sin(x)                      # sin函數
y2 = np.cos(x)                      # cos函數

plt.xticks(np.arange(0,7,step=0.5))
plt.yticks(np.arange(-1,1.5,step=0.5))

plt.plot(x, y1, color='c')          # 設定青色cyan            
plt.plot(x, y2, color='r')          # 設定紅色red
plt.show()




import matplotlib.pyplot as plt
import numpy as np

font1 = {'family':'Old English Text MT',
        'color':'blue',
        'weight':'bold',
        'size':20}
font2 = {'family':'Old English Text MT',
        'color':'green',
        'weight':'normal',
        'size':12}

print('文字顯示不同字型')
plt.title('Sin and Cos function',fontdict=font1)
plt.xlabel('x-value',fontdict=font2)
plt.ylabel('y-value',fontdict=font2)

plt.show()





locs, the_labels = plt.xticks()         # 回傳位置與標籤字串
print(f'locs       = {locs}')
print(f'the_labels = {the_labels}')



plt.rcParams['xtick.labelsize'] = 34	X軸刻度的文字大小
plt.rcParams['ytick.labelsize'] = 16	Y軸刻度的文字大小


print('x軸刻度設定')
plt.tick_params(axis='x',direction='in',color='b')
print('y軸刻度設定')
plt.tick_params(axis='y',length=10,direction='inout',color='g')

plt.xticks(np.arange(0,7,step=0.5),color='b')
plt.yticks(np.arange(-1,1.5,step=0.5),color='g')


plt.tick_params(axis='both',length=10,direction='inout',color='r')


'''
