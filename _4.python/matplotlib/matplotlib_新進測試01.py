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


#foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = 'C:/_git/vcs/_1.data/______test_files1'


'''
import glob,cv2

files = glob.glob(foldername + "/*.jpg")  #建立測試資料
test_feature=[]
for file in files:
    print(file)
    img = cv2.imread(file)	#讀取本機圖片
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #灰階    
    _, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV) #轉為反相黑白 
    test_feature.append(img)

print(test_feature)

print('畫多張圖')


plt.gcf().set_size_inches(12, 14)

num=25

if num>25: num=25
for i in range(num):
    ax=plt.subplot(5,5, i+1)
    #ax.imshow(images[start_id], cmap='binary')  #顯示黑白圖片
    title = 'label = ' + str(i)
    ax.set_title(title,fontsize=12)  # X,Y軸不顯示刻度
    ax.set_xticks([]);ax.set_yticks([])        
plt.show()


'''

print('------------------------------------------------------------')	#60個


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



sys.exit()


print('------------------------------------------------------------')	#60個



N = 10

x2 = np.arange(N)
#y2 = x2 * np.random.randn(N)
y2 = np.random.randn(N)
y2 = x2

plt.scatter(x2, y2)
plt.show()

plt.bar(x2, y2)
plt.show()


plt.plot(x2, y2)
plt.show()


#箱形圖  便於確認資料分布的視覺化方法
plt.boxplot(y2)
plt.show()

import sys
sys.exit()


'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()
'''

print('------------------------------------------------------------')	#60個



'''
X = np.random.randn(300)
Y = np.random.randn(300)
plt.scatter(X, Y)
'''


plt.plot(np.random.randn(20))
plt.plot(range(20), np.random.randn(20))

plt.show()




print('------------------------------------------------------------')	#60個

'''
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
'''

print('------------------------------------------------------------')	#60個



x = np.linspace(-5, 5, 1000)
y = np.sin(x) / (x**2+1)

plt.plot(x,y,lw=5)
plt.plot(x,np.cos(x))
#plt.xticks(np.arange(-5,6))



#把這個函數大於 0 的地方標示出來。
y = np.sinc(x)
plt.plot(x,y)
plt.plot(x[y>0], y[y>0], 'o')




print('------------------------------------------------------------')	#60個




'''
print('------------------------------------------------------------')	#60個
                                
x = [x for x in range(0, 11)]                   
y = [(3 * y -18) for y in x]
plt.plot(x, y, '-*')   

plt.xticks(x)                           # 標記每個單一x數字
plt.axis([0, 10, -20, 15])              # 標記刻度範圍
plt.xlabel("children")
plt.ylabel("Apple")
plt.grid()                              # 加格線
plt.show()

print('------------------------------------------------------------')	#60個

x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]
y2 = [3 * y for y in x]
y3 = [4 * y for y in x]
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                              # 加格線
plt.show()
'''

print('------------------------------------------------------------')	#60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個







