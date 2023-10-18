# scatter 集合

import sys
import numpy as np
import matplotlib.pyplot as plt

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號                  圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'scatter 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

#散點圖
N = 500
#一般random
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y)

#常態random
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y)

#第二張圖
plt.subplot(232)

x = np.random.rand(N)
y = np.random.rand(N)

size = np.random.rand(N) * 50
color = np.random.rand(N)
plt.scatter(x, y, size, color)
plt.colorbar()

#第三張圖
plt.subplot(233)

plt.xlim(-3, 3)
plt.ylim(-3, 3)
x1 = np.random.normal(0, 1, 1024)
y1 = np.random.normal(0, 1, 1024)
plt.scatter(x1, y1, alpha = 0.3)

#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)

N = 500
x = np.random.rand(N)
y = np.random.rand(N)
plt.scatter(x, y, c=y, cmap = 'hsv')  # 色彩依 y 軸值變化
plt.colorbar()

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'scatter 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

#Hyperlinks
import numpy as np
import matplotlib.pyplot as plt

s = plt.scatter([1, 2, 3], [4, 5, 6])
s.set_urls(['https://www.bbc.com/news', 'https://www.google.com/', None])


#第二張圖
plt.subplot(232)


'''
xpt = np.linspace(0, 5, 50)                            # 建立含500個元素的陣列
ypt = 1 - 0.5*np.abs(xpt-2)                             # y陣列的變化
plt.scatter(xpt, ypt, s=50, c=ypt, cmap='hsv')          # 色彩隨y軸值變化


xpt = np.linspace(0, 5, 500)                            # 建立含500個元素的陣列
ypt = 1 - 0.5*np.abs(xpt-2)                             # y陣列的變化
plt.scatter(xpt, ypt, s=50, c=xpt, cmap='hsv')          # 色彩隨x軸值變化
'''

x = np.arange(50)
y = x
t = x
plt.scatter(x, y, c=t, cmap='rainbow')


#第三張圖
plt.subplot(233)

POINTS = 10
#由平均 0, 標準差 1 的分布中取 20 個數
#np.random.randn(20)

#試取 100 個, 算平均、標準差

x = np.arange(POINTS)
g = np.random.randn(POINTS)
g.mean()
g.std()

#不同的平均值和標準差
#比如我們想要平均值變成 70, 標準差 10 怎麼做呢?
#g2 = g*10 + 70

print(g)
#g.sort()
print(g)

plt.scatter(x, g, c = 'blue', marker = '.')



#第四張圖
plt.subplot(234)

listx = [31,15,20,25,12,18,45,21,33,5,18,22,37,42,10]
listy = [68,20,61,32,45,56,10,18,70,64,43,66,19,77,21]
scale = [x ** 3 for x in [5,4,2,6,7,1,8,9,2,3,2,4,5,7,2]]

plt.xlim(0, 50)
plt.ylim(0, 80)
plt.scatter(listx, listy, c = 'r', s = scale, marker = 'o', alpha = 0.5)


#第五張圖
plt.subplot(235)

minutes = [45, 34, 56, 77, 90, 90, 90, 34, 45, 44, 80, 15, 10, 12]
scores =  [90, 80, 100, 65, 5, 30, 55, 100, 90, 80, 60, 5, 0, 10]
plt.xlabel('解題時間')
plt.ylabel('分數')
plt.scatter(minutes, scores)

#第六張圖
plt.subplot(236)

import random

def loc(index):
    ''' 處理座標的移動 '''
    x_mov = random.choice([-3,-2,-1,1,2,3])     # 隨機x軸移動值
    xloc = x[index-1] + x_mov                   # 計算x軸新位置
    y_mov = random.choice([-5,-3,-1,1,3,5])     # 隨機y軸移動值
    yloc = y[index-1] + y_mov                   # 計算y軸新位置
    x.append(xloc)                              # x軸新位置加入串列
    y.append(yloc)                              # y軸新位置加入串列
    
num = 10000                                     # 設定隨機點的數量
x = [0]                                         # 設定第一次執行x座標
y = [0]                                         # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
#plt.axis('off')

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                          圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'scatter 集合 3 雜訊', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# y = 1.2x + 0.8
x = np.linspace(0, 5, 50)
y = 1.2 * x + 0.8
y = 1.2 * x + 0.8 + 0.3 * np.random.randn(50)   #加上noise

plt.scatter(x, y)
plt.plot(x, 1.2 * x + 0.8, 'r')


#第二張圖
plt.subplot(232)

x = np.linspace(0, 10, 200)
y1 = np.sin(x)
y2 = np.sin(x) + 0.3 * np.random.randn(200)

plt.plot(x, y1, 'r')

plt.scatter(x, y2)


#第三張圖
plt.subplot(233)


#曲線資料加入雜訊
x = np.linspace(-5, 5, 51)
y = np.sin(x)
yn = y + np.random.rand(1, len(y)) * 1.5

plt.scatter(x, yn, c = 'blue', marker = '.')
plt.plot(x, y + 0.75, 'r')



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)

from pylab import *

rc("xtick.major", pad=8)

data = """
   Sovereign of the Seas   90     1637   1,522                                             2,500             Sail Three-Decker                  Lavery        
   Naseby                  80     1655   1,258                                             2,100             Sail Three-Decker                  Lavery        
   Prince                 100     1670   1,403                                             2,300             Sail Three-Decker                  Lavery        
   Royal James            100     1671   1,416                                             2,300             Sail Three-Decker                  Lavery        
   Royal Charles          100     1673   1,443                                             2,400             Sail Three-Decker                  Lavery        
   Royal James            100     1675   1,422                                             2,400             Sail Three-Decker                  Lavery        
   Royal Prince            92     1663   1,432                                             2,400             Sail Three-Decker                  Lavery        
   Britannia              100     1682   1,739                                             2,900             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1701   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Royal Anne             100     1703   1,722                                             2,900             Sail Three-Decker                  Lavery        
   London                 100     1706   1,685                                             2,800             Sail Three-Decker                  Lavery        
   Royal George           100     1715   1,801                                             3,000             Sail Three-Decker                  Lavery        
   Britannia              100     1719   1,895                                             3,100             Sail Three-Decker                  Lavery        
   Royal William          100     1719   1,918                                             3,200             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1728   1,883                                             3,100             Sail Three-Decker                  Lavery        
   Victory                100     1737   1,921                                             3,200             Sail Three-Decker                  Lavery        
   Royal George           100     1756   2,047                                             3,400             Sail Three-Decker                  Lavery        
   Britannia              100     1762   2,116                                             3,500             Sail Three-Decker                  Lavery        
   Victory                100     1765   2,142                                             3,600             Sail Three-Decker                  Lavery        
   Royal Sovereign        100     1786   2,175                                             3,600             Sail Three-Decker                  Lavery        
   Royal George           100     1788   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Caledonia              120     1808   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Ville de Paris         110     1795   2,351                                             3,900             Sail Three-Decker                  Lavery        
   Hibernia               110     1804   2,530                                             4,200             Sail Three-Decker                  Lavery        
   Queen Charlotte        100     1790   2,286                                             3,800             Sail Three-Decker                  Lavery        
   Nelson                 120     1814   2,617                                             4,300             Sail Three-Decker                  Lavery        
   St Vincent             120     1815   2,601                                             4,300             Sail Three-Decker                  Lavery        
   Howe                   120     1815   2,619                                             4,300             Sail Three-Decker                  Lavery        
   Britannia              120     1820   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Prince Regent          120     1823   2,613                                             4,300             Sail Three-Decker                  Lavery        
   Queen Charlotte        104     1810   2,289                                             3,800             Sail Three-Decker                  Lavery        
   Princess Charlotte     104     1825   2,443                                             4,100             Sail Three-Decker                  Lavery        
   Royal Adelaide         104     1828   2,446                                             4,100             Sail Three-Decker                  Lavery        
   Royal George           120     1827   2,616                                             4,300             Sail Three-Decker                  Lavery        
   Neptune                120     1832   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Royal William          120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Waterloo               120     1833   2,694                                             4,500             Sail Three-Decker                  Lavery        
   St George              120     1840   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Trafalgar              120     1841   2,694                                             4,500             Sail Three-Decker                  Lavery        
   Queen                  110     1839   3,104                                             5,100             Sail Three-Decker                  Lavery        
   Duke of Wellington     131     1852   3,759                                5,829        5,829 Steam Three-Decker (conversion from sail)      Lambert       
   Marlborough            131     1855   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Sovereign        131     1857   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Prince of Wales        131     1860   3,853                                6,065        6,065 Steam Three-Decker (conversion from sail)      Lambert       
   Royal Albert           121     1854   3,726                                5,572        5,572 Steam Three-Decker (conversion from sail)      Lambert       
   Windsor Castle         102     1858   3,099                                             5,100 Steam Three-Decker (conversion from sail)      Lambert       
   Victoria               121     1859   4,116                                6,959        6,959             Steam Three-Decker                 Lambert       
   Howe                   121     1860   4,236                                             7,000             Steam Three-Decker                 Lambert       
   Saint Jean d'Acre      101     1853   3,200                                5,499        5,499              Steam Two-Decker                  Lambert       
   Conqueror              101     1855   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Donegal                101     1858   3,224                                5,720        5,720              Steam Two-Decker                  Lambert       
   Duncan                 101     1859   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Gibraltar              101     1860   3,715                                5,950        5,950              Steam Two-Decker                  Lambert       
   Warrior                 40     1860   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Black Prince            40     1861   6,039                                9,180        9,180             Iron-Clad Frigate              Lyon & Winfield   
   Achilles                26     1863   6,121                                9,820        9,820             Iron-Clad Frigate              Lyon & Winfield   
   Minotaur                36     1863   6,643                               10,690       10,690             Iron-Clad Frigate              Lyon & Winfield   
   Agincourt               36     1865   6,638                               10,600       10,600             Iron-Clad Frigate              Lyon & Winfield   
   Northumberland          36     1866   6,631                               10,784       10,784             Iron-Clad Frigate              Lyon & Winfield   
   Lord Clyde              24     1864   4,067                                7,750        7,750    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Lord Warden             16     1865   4,080                                7,842        7,842    Centre-Battery Iron-Clad Frigate       Lyon & Winfield   
   Bellerophon             15     1865   4,720                                7,551        7,551          Centre-Battery Iron-Clad          Lyon & Winfield   
   Hercules                14     1868   5,234                                8,830        8,830          Centre-Battery Iron-Clad          Lyon & Winfield   
   Monarch                  7     1868   5,102                                8,322        8,322             Masted Turret Ship             Lyon & Winfield   
   Captain                  6     1869   4,272                                7,767        7,767             Masted Turret Ship             Lyon & Winfield   
   Sultan                  12     1870   5,234                                9,540        9,540          Centre-Battery Iron-Clad          Lyon & Winfield   
   Devastation              4     1871   4,407                                9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Thunderer                4     1872                                        9,390        9,390            Mastless Turret Ship            Lyon & Winfield   
   Alexandra               12     1875                                        9,490        9,490          Centre-Battery Iron-Clad          Lyon & Winfield   
   Dreadnought              4     1875                                       10,820       10,820            Mastless Turret Ship            Lyon & Winfield   
   Temeraire                8     1876                                        8,571        8,571          Centre-Battery Iron-Clad          Lyon & Winfield   
   Inflexible               4     1876                                       11,880       11,880        Central Citadel Turret Ship         Lyon & Winfield   
"""

s2x, s2y, s3x, s3y, t3x, t3y, ix, iy, lx, ly = [], [], [], [], [], [], [], [], [], []

for l in data.splitlines():
    if len(l) < 5: 
        continue
    n = l[:26].strip()
    y = int(l[33:39])
    try:
        t = int(l[39:47].replace(',', ''))
    except: 
        continue
    if 'Steam Two-Decker' in l:
        s2x.append(y)
        s2y.append(t)
    elif 'Steam Three-Decker' in l:
        s3x.append(y)
        s3y.append(t)
    elif 'Sail Three-Decker' in l:
        t3x.append(y)
        t3y.append(t)
    elif 'igate' in l:
        ix.append(y)
        iy.append(t)
    else:
        lx.append(y)
        ly.append(t)

ll = .7
scatter(t3x, t3y, c = 'b', marker = 'o', lw = ll, label = 'Sail 3-Deckers')
scatter(s3x, s3y, c = 'orange', marker = 'o', lw = ll, label = 'Steam 3-Deckers')
scatter(s2x, s2y, c = 'r', marker = 'o', lw = ll, label = 'Steam 2-Deckers')
scatter(ix, iy, c = 'g', marker = 'o', lw = ll, label = 'Iron-clad Frigates')
scatter(lx, ly, c = 'cyan', marker = 'o', lw = ll, label = 'Later Iron-clads')

legend(loc="upper left")
ylim(0, 7000)
xlim(1630, 1875)
xticks(range(1630, 1930, 50))
xlabel("Year launched")
ylabel("Tonnage (BOM)")
grid(True, ls = '-', c = '#a0a0a0')

plt.show()

print('------------------------------------------------------------')	#60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(num = 'scatter 集合 4', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)




#第二張圖
plt.subplot(232)

print('繪製散布圖')
import matplotlib.pyplot as plt
import pandas as pd

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

# 讀入資料
dat = pd.read_csv(filename, encoding='UTF-8')

# 散布圖
plt.scatter(dat['數學'], dat['理科'])
plt.axis('equal')


#共變異數與相關係數
import numpy as np
correlation = np.corrcoef(dat['數學'], dat['理科']) # 計算相關係數
correlation[0,1]  # 顯示在畫面



#第三張圖
plt.subplot(233)


#連接2點的直線

import matplotlib.pyplot as plt
import numpy as np

# 資料
x = np.arange(1, 5.1, 0.1)
y = 1/2*x + (1/2)

# 繪圖
plt.scatter(x, y)
plt.grid(color='0.8')




#第四張圖
plt.subplot(234)

x = np.random.randn(100)
y = np.random.randn(100)

plt.scatter(x, y, s=250)

#畫不同顏色的scatter
cl = np.random.randint(1, 4, 100)
plt.scatter(x, y, s=100, c=cl, alpha=0.6, cmap="Paired")

#第五張圖
plt.subplot(235)






#第六張圖
plt.subplot(236)

# Generate 100 random data points along 3 dimensions
x, y, scale = np.random.randn(3, 100)

# Map each onto a scatterplot we'll create with Matplotlib
plt.scatter(x=x, y=y, c=scale, s=np.abs(scale)*500)

plt.show()


print('------------------------------------------------------------')	#60個

#          編號                      圖像大小[英吋]     解析度    背景色                    邊框顏色                         邊框有無
plt.figure(num = 'scatter 集合 5', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                          # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.linspace(0.0, 2*np.pi, N)            # 建立 50 個點
y1 = np.sin(x)
plt.scatter(x, y1, c=colors, marker='*')    # 繪製 sine
y2 = np.cos(x)
plt.scatter(x, y2, c=colors, marker='s')    # 繪製 cos

#第二張圖
plt.subplot(232)

N = 50                                      # 色彩數列的點數
colorused = ['b','c','g','k','m','r','y']   # 定義顏色
colors = []                                 # 建立色彩數列
for i in range(N):                     # 隨機設定顏色
    colors.append(np.random.choice(colorused))
x = np.random.randint(1,11,N)          # 建立 x
y = np.random.randint(1,11,N)          # 建立 y
size =  (30 * np.random.rand(N))**2    # 散點大小數列
plt.scatter(x, y, s=size, c=colors)         # 繪製散點
plt.xticks(np.arange(0,12,step=1.0))        # x 軸刻度
plt.yticks(np.arange(0,12,step=1.0))        # y 軸刻度

#第三張圖
plt.subplot(233)

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=x,cmap='rainbow')  # 色彩隨 x 軸值變化

#第四張圖
plt.subplot(234)

x = np.linspace(0, 5, 500)                # 含500個元素的陣列
y = 1 - 0.5*np.abs(x-2)                   # y陣列的變化
plt.scatter(x,y,s=50,c=y,cmap='rainbow')  # 色彩隨 y 軸值變化
plt.colorbar()                            # 色彩條


#第五張圖
plt.subplot(235)

import random

def loc(index):
    #處理座標的移動
    x_mov = random.choice([-3, 3])          # 隨機x軸移動值
    xloc = x[index-1] + x_mov               # 計算x軸新位置
    y_mov = random.choice([-5, -1, 1, 5])   # 隨機y軸移動值
    yloc = y[index-1] + y_mov               # 計算y軸新位置
    x.append(xloc)                          # x軸新位置加入串列
    y.append(yloc)                          # y軸新位置加入串列
    
num = 10000                                 # 設定隨機點的數量
x = [0]                                     # 設定第一次執行x座標
y = [0]                                     # 設定第一次執行y座標

for i in range(1, num):                     # 建立點的座標
    loc(i)
t = x                                       # 色彩隨x軸變化
plt.scatter(x, y, s=2, c=t, cmap='brg')
plt.axis('off')                             # 隱藏座標


#第六張圖
plt.subplot(236)


x = np.linspace(0, 10, 51)
print(type(x))

y1 = np.sin(x) * 5 + 5
y2 = np.cos(x) * 5 + 5

plt.scatter(x, y1, c = 'r')       #畫出每個x-y對應點
plt.scatter(x, y2, c = 'g')       #畫出每個x-y對應點


plt.show()

print('------------------------------------------------------------')	#60個






