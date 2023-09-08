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

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進測試 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

N = 10

x2 = np.arange(N)
#y2 = x2 * np.random.randn(N)
y2 = np.random.randn(N)
y2 = x2

plt.scatter(x2, y2)



#第二張圖
plt.subplot(232)

plt.bar(x2, y2)

#第三張圖
plt.subplot(233)

plt.plot(x2, y2)

#第四張圖
plt.subplot(234)

plt.boxplot(y2) #箱形圖  便於確認資料分布的視覺化方法

#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)


plt.show()

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

'''
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
'''



print('------------------------------------------------------------')	#60個

'''



xpt = list(range(1,11))        # 建立1-100序列x座標點

plt.plot(squares, lw=10)       # 串列squares數據是y軸的值, 線條寬度是10
plt.tick_params(axis='both', labelsize=12, color='red')

plt.plot(seq, data1, 'g--', seq, data2, 'r-.', seq, data3, 'y:', seq, data4, 'k.')   
plt.plot(seq, data1, '-*', seq, data2, '-o', seq, data3, '-^', seq, data4, '-s')   
plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   

seq = [2021, 2022, 2023]                # 年度
plt.xticks(seq)                         # 設定x軸刻度

plt.plot(seq, Benz, '-*', seq, BMW, '-o', seq, Lexus, '-^')   


'''

'''
print('------------------------------------------------------------')	#60個




print('------------------------------------------------------------')	#60個
plt.plot(x, y, label="$sin(x)$", color='red', lw=2)
plt.plot(x, z, label="$cos(x^2)$", color='b')


plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)
'''

print('------------------------------------------------------------')	#60個

'''
plt.plot(x, np.sin(x), c='#e63946', lw=3)
plt.plot(x, np.sin(3*x), c='#7fb069', lw=3)
plt.scatter(x, np.random.randn(100), c='#daa73e', s=50, alpha=0.5)
plt.bar(range(10), np.random.randint(1,30,10), fc='#e55934')

plt.plot(x,y,'r-.')


print('------------------------------------------------------------')	#60個

plt.plot(x, y, marker='o')
plt.plot(x, y, c='#6b8fb4', lw=5, marker='o', mfc='#fffa7c', mec="#084c61", mew=3, ms=20)

plt.show()

'''
print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')
print(dat.head())

print('------------------------------------------------------------')	#60個

#計算平均數、中位數、眾數

import pandas as pd
import numpy as np

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')

# 平均數、中位數
print('平均數', np.mean(dat['數學']))
print('中位數', np.median(dat['數學']))

# 眾數
bincnt = np.bincount(dat['數學'])  # 計算同樣的值的個數
mode = np.argmax(bincnt)  # 取得bincnt中最大的值
print('眾數', mode)

print('------------------------------------------------------------')	#60個
print('畫出頻率分布圖')

import matplotlib.pyplot as plt
import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')

# 計算各組別頻率
hist = [0]*10 # 頻率（元素個數10，初始化為0）
for dat in dat['數學']:
    if dat < 10:   hist[0] += 1
    elif dat < 20:  hist[1] += 1
    elif dat < 30:  hist[2] += 1
    elif dat < 40:  hist[3] += 1
    elif dat < 50:  hist[4] += 1
    elif dat < 60:  hist[5] += 1
    elif dat < 70:  hist[6] += 1
    elif dat < 80:  hist[7] += 1
    elif dat < 90:  hist[8] += 1
    elif dat <= 100:  hist[9] += 1 
print('頻率:', hist)

# 頻率分布圖
x = list(range(1,11))  # x軸的值
labels = ['0~','10~','20~','30~','40~','50~','60~','70~','80~','90~']  # x軸的刻度標籤
plt.bar(x, hist, tick_label=labels, width=1)# 描繪長條圖

plt.show()



print('------------------------------------------------------------')	#60個
print('描繪頻率分布圖')

import matplotlib.pyplot as plt
import pandas as pd

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_onigiri.csv'
dat = pd.read_csv(filename, encoding='UTF-8')

# 頻率分布圖
plt.hist(dat['店長'], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat['太郎'], bins=range(0, 200, 10), alpha=0.5)

plt.show()



print('計算平均數、變異數、標準差')


import numpy as np
print('店長---------')
print('平均:', np.mean(dat['店長']))
print('變異數:', np.var(dat['店長']))
print('標準差:', np.std(dat['店長']))

print('太郎---------')
print('平均:', np.mean(dat['太郎']))
print('變異數:', np.var(dat['太郎']))
print('標準差:', np.std(dat['太郎']))

print('------------------------------------------------------------')	#60個
print('亂數')

import random
rand = [] 
for i in range(10):
    rand.append(random.randint(0,100)) # 產生0～100的亂數
print(rand)

print('------------------------------------------------------------')	#60個

a = 4     # 亂數的初始值
b = 7
c = 9
rn = 1    
rand = []
for i in range(20):
    rn = ((a * rn + b) % c)    # 產生亂數
    rand.append(rn)
print(rand)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


