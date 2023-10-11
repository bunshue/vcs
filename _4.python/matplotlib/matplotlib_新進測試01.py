import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import math
import random

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進測試 01', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

N = 11
y = np.arange(N)
#y = np.random.randn(N)
print(y)
y[3]=10
print(y)

#盒鬚圖（Box plot）
plt.boxplot(y) #箱形圖  便於確認資料分布的視覺化方法

#第二張圖
plt.subplot(232)

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


#第三張圖
plt.subplot(233)

#畫點
plt.plot(0, 1, '-o')    #在 (0, 1) 上 畫一點
plt.plot(1, 5, 'r-o')
plt.plot(2, 10, 'r-o')
plt.plot(3, 20, 'r-o')


#第四張圖
plt.subplot(234)

X = []
Y = []
for i in range(1000):
    theta = 2 * random.random() * math.pi
    r = random.random() * 5
    x = math.cos(theta) * r + 5
    y = math.sin(theta) * r + 5
    X.append(x)
    Y.append(y)

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])

plt.axis('equal')       #軸比例

#第五張圖
plt.subplot(235)

X = []
Y = []
for i in range(1000):
    x=random.randint(0, 10) + random.random()
    y=random.randint(0, 10) + random.random()
    if ((x - 5) ** 2 + (y - 5) ** 2) > 25:
        #print('Reject ({0}, {1})'.format(x, y))
        continue
    else :
        X.append(x)
        Y.append(y)
print(len(X))        

plt.scatter(X, Y)
print(len(X))
plt.axis([0, 10, 0, 10])
plt.axis('equal')       #軸比例

#第六張圖
plt.subplot(236)

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 正常顯示
x1 = np.linspace(-1.5,1.5,31)
y1 = np.cos(x1)**2

# 移除 y1 > 0.6 的點
x2 = x1[y1 <= 0.6]
y2 = y1[y1 <= 0.6]

# 遮罩 y1 > 0.7 的點
y3 = np.ma.masked_where(y1 > 0.7, y1)

# 將 y1 > 0.8 的點設為 NaN
y4 = y1.copy()
y4[y4 > 0.8] = np.nan

plt.plot(x1*0.1, y1, 'o-', label='正常顯示')
plt.plot(x2*0.4, y2, 'o-', label='移除點')
plt.plot(x1*0.7, y3, 'o-', label='遮罩點')
plt.plot(x1*1.0, y4, 'o-', label='將點設為NaN')
plt.legend()
plt.title('Cos函數顯示與遮蔽點的應用')


plt.show()

sys.exit()

print('------------------------------------------------------------')	#60個

#foldername = 'C:/_git/vcs/_1.data/______test_files1/source_pic'
foldername = 'C:/_git/vcs/_1.data/______test_files1'


"""
import glob, cv2

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


"""

print('------------------------------------------------------------')	#60個

"""
x = np.linspace(start=-10, stop=10, num=101)

#plt.plot(x, np.absolute(x))

xx = x + 1j * x[:, np.newaxis]

plt.imshow(np.abs(xx), extent=[-10, 10, -10, 10], cmap='gray')
"""

print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding='UTF-8')
print(dat.head())

print('------------------------------------------------------------')	#60個

#計算平均數、中位數、眾數

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

# 讀入csv檔
filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV7_onigiri.csv'
dat = pd.read_csv(filename, encoding='UTF-8')

# 頻率分布圖
plt.hist(dat['店長'], bins=range(0, 200, 10), alpha=0.5)
plt.hist(dat['太郎'], bins=range(0, 200, 10), alpha=0.5)

plt.show()

print('計算平均數、變異數、標準差')

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

rand = [] 
for i in range(10):
    rand.append(random.randint(0,100)) # 產生0～100的亂數
print(rand)

print('------------------------------------------------------------')	#60個

a = 4     # 亂數的初始值
b = 7
c = 9   #取亂數結果 0 ~ 8之整數
rn = 1

rand = []
for i in range(20):
    rn = (a * rn + b) % c   # 不用亂數模組, 自己運算出亂數
    rand.append(rn)
print(rand)

print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


