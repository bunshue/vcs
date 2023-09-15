
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

plt.rcParams["font.family"] = ["Microsoft JhengHei"]





#舊金山市中心（1991–2020年正常值，1849年至今極端數據） 

#月份 	1月 	2月 	3月 	4月 	5月 	6月 	7月 	8月 	9月 	10月 	11月 	12月 	全年 

#平均高溫 °C
listy1 = [14.3, 15.8, 16.7, 17.2, 17.8, 19.2, 19.1, 19.9, 21.2, 21.0, 17.6, 14.4]   #, 17.8

#平均低溫 °C
listy2 = [8.1, 8.8, 9.4, 9.8, 10.8, 11.7, 12.4, 13.1, 13.1, 12.4, 10.4, 8.3]    #, 10.7

#平均降雨量 mm
listy3 = [112, 111, 80, 41, 18, 5.1, 0.25, 1.5, 2.5, 24, 66, 121]   #, 581

#在同一張圖 畫 兩條曲線
month = np.arange(1, 13)
print(type(month))
print(month)

plt.plot(month, listy1, 'r-.s', lw = 2, markersize = 5, label = "平均高溫")
plt.plot(month, listy2, 'g-.s', lw = 2, markersize = 5, label = "平均低溫")
plt.plot(month, listy3, 'b--*', lw = 2, markersize = 5, label = "平均降雨量")

'''
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
plt.plot(listx, listy, color = "red", ls = "--")
'''

#同一個指令畫兩條線
#plt.plot(month, listy1, 'r-.s', month, listy2, 'y-s')

plt.legend()

month_chi = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
plt.xticks(month, month_chi, rotation = 45)

plt.xlim(0.5, 12.5) #x軸顯示邊界
plt.ylim(-10, 150)  #y軸顯示邊界

plt.grid(color = 'k', ls = ':', lw = 2, alpha = 0.5)    #畫格點
plt.grid(color = 'r', linestyle = ":", linewidth = '1', alpha = 0.5)    #畫格點

plt.show()









'''
調整x軸刻度 1
week = [0,1,2,3,4,5,6]
labels = ['Sunday','Monday','Tuesday','Wednesday',
          'Thursday','Friday','Saturday']

plt.xticks(week,labels,rotation=30) #字體加旋轉


調整x軸刻度 2
year = [2015,2016,2017,2018,2019]
plt.xticks(year)

調整x軸刻度 3
x = [0.5,1.0,10,50,100]
labels = ['A','B','C','D','E']
plt.xticks(x,labels)

調整x軸刻度 4
x = [0.5,1.0,10,50,100]
value = range(len(x))
plt.xticks(value,x)

調整x軸刻度 5
plt.xticks(np.arange(0,7,step=0.5)) # 設定x軸刻度為0 ~ 6.5, 每隔0.5
plt.yticks(np.arange(-1,1.5,step=0.5))


plt.xticks(np.arange(0,7,step=0.5),color='b')
plt.yticks(np.arange(-1,1.5,step=0.5),color='g')


調整x軸刻度 6
x = [0.5,1.0,10,50,100]
value = range(len(x))
plt.xticks(value,x)

調整x軸刻度 7




plt.rcParams['xtick.labelsize'] = 34	X軸刻度的文字大小
plt.rcParams['ytick.labelsize'] = 16	Y軸刻度的文字大小


print('x軸刻度設定')
plt.tick_params(axis='x',direction='in',color='b')
print('y軸刻度設定')
plt.tick_params(axis='y',length=10,direction='inout',color='g')

plt.tick_params(axis='both',length=10,direction='inout',color='r')



locs, the_labels = plt.xticks()         # 回傳位置與標籤字串
print(f'locs       = {locs}')
print(f'the_labels = {the_labels}')




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



'''
