# bar 集合

selected_font = 'C:/_git/vcs/_1.data/______test_files1/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'bar 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

filename = 'C:/_git/vcs/_1.data/______test_files1/popu.txt'

with open(filename, 'r') as fp:
	populations = fp.readlines()

city = list()
popu = list()

for p in populations:
	cc, pp = p.split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city))

plt.bar(ind, popu)
plt.xticks(ind+0.5, city)
#plt.title('台灣各縣市人口統計')


#第二張圖
plt.subplot(232)

print("垂直/水平 長條圖");

#設定將使用的數值
x = ['Chinese', 'English', 'Math', 'Social', 'Nature']
y = [79, 63, 71, 83, 97]

print("垂直長條圖");
#繪製出垂直 Bar，這邊使用的是 bar 函數，設定的是 width 寬度
#plt.bar(x, y, width=0.5, color='red')

print("水平長條圖");
#繪製出水平 Bar，這邊使用的是 barh 函數，設定的是 height 寬度
plt.barh(x, y, height=0.5, color='blue')

plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('資訊程式課程選修人數', fontsize="18") # 設定圖表標題內容及大小


#第三張圖
plt.subplot(233)


'''
#疊加長條圖的應用

#疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的

#設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2
'''

x = ['Chinese', 'English', 'Math', 'Social', 'Nature']
y1 = [30, 26, 37, 22, 28]
y2 = [20, 31, 24, 24, 33]

#Step 3. 將兩條長條圖繪製出來，其中第二條 y2 的 y 軸基底座標是建立在 y1 上

plt.bar(x, y1, width=0.5, label='Male')
plt.bar(x, y2, width=0.5, bottom=y1, label='Female')

plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('資訊程式課程選修人數', fontsize="18") # 設定圖表標題內容及大小
plt.legend()


#第四張圖
plt.subplot(234)

x = ['c','c++','c#','java','python']
y1 = [25,20,20,16,28]
y2 = [20,8,18,16,22]

plt.bar(x, y1, width=0.5, label='男')
plt.bar(x, y2, width=0.5, bottom=y1, label='女')

plt.xlabel("程式課程")
plt.ylabel("選修人數")
plt.title("資訊程式課程選修人數")
plt.legend()

#第五張圖
plt.subplot(235)

width = 0.25
listx = ['c','c++','c#','java','python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]

plt.bar(listx1, listy1, width, label='男')
plt.bar(listx2, listy2, width, label='女')

plt.xticks(range(len(listx)), labels=listx)

plt.xlabel("程式課程")
plt.ylabel("選修人數")
plt.title("資訊程式課程選修人數")
plt.legend()

#第六張圖
plt.subplot(236)

listx1 = [1,5,7,9,13,16]
listy1 = [15,50,80,40,70,50]
plt.bar(listx1, listy1, label="男性")
listx2 = [2,6,8,11,14,16]
listy2 = [10,40,30,50,80,60]
plt.bar(listx2, listy2, color="red", label="女性")
plt.legend()
plt.xlim(0, 20)
plt.ylim(0, 100)
plt.title("零用金統計")
plt.xlabel("年齡")
plt.ylabel("零用金數目")

plt.show()




# hist 集合

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'hist 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)

#第一張圖
plt.subplot(231)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10 #資料數
plt.hist(np.random.randn(1000), N, facecolor='yellow', edgecolor='yellow')

#第二張圖
plt.subplot(232)

import numpy as np
import matplotlib.pyplot as plt
from numpy.random import normal,rand
x = normal(size=200)

N = 10 #資料數
plt.hist(x,bins=N)


#第三張圖
plt.subplot(233)
normal_samples = np.random.normal(size = 100000) # 生成 100000 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples)



#第四張圖
plt.subplot(234)

uniform_samples = np.random.uniform(size = 100000) # 生成 100000 組介於 0 與 1 之間均勻分配隨機變數
plt.hist(uniform_samples)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()



# 派圖 集合

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = '派圖 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)

#第一張圖
plt.subplot(231)

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)        # 設定分隔的區塊位置
plt.pie(sizes, 
	explode = explode,      # 設定分隔的區塊位置
	labels = labels, 
	colors = colors,
	labeldistance = 1.1, 
	autopct = "%2.1f%%",    #項目百分比的格式
	pctdistance = 0.6,
	shadow = True,
	startangle = 90)        # 繪製起始角度

plt.axis("equal")
plt.legend()


#第二張圖
plt.subplot(232)

'''
圓餅圖是使用 pie 函數繪製出來的，語法為：

plt.pie(串列資料, [其餘參數值])

其餘參數介紹：
pie參數 	說明
color 	指定圓餅圖的顏色 ('blue', 'red', 'green', 'yellow', 色碼('#CC00CC')),預設為藍色 blue
label 	項目標題，需搭配 legend 函式才有效果
explode 	設定分隔的區塊位置
autopct 	項目百分比格式，語法為「%格式%%」，Example:autopct = "%2.2f%%"(表示整數2位數及小數點2位數)
pctdistance 	數值文字與圓心距離
shadow 	圓餅圖陰影開啟/關閉，True 有陰影，False 沒有陰影
startangle 	繪製起始角度，繪製會以逆時鐘旋轉計算角度
radius 	圓餅圖的半徑，預設是1
'''

#設定將使用的數值，將要有項目標題、數值串列、圓餅圖顏色、分隔的區塊位置
labels = ['A', 'B', 'C', 'D']
values = [60, 42, 83, 37]
colors = ['r', 'g', 'b', 'y']
explode = (0, 0, 0, 0.08)       #設定分隔的區塊位置

#設定 pie 函數參數繪製圓餅圖
plt.pie(
values, # 數值
labels = labels, # 項目標題
colors = colors, # 指定圓餅圖的顏色
explode = explode, # 設定分隔的區塊位置
autopct = "%2.2f%%", # 項目百分比格式
pctdistance = 0.5, # 數值文字與圓心距離
shadow = True, # 圓餅圖陰影開啟/關閉
startangle = 90, # 繪製起始角度
radius = 0.9 # 圓餅圖的半徑，預設是1
)

#設定 legnd 的位置，將圖表顯示出來，並顯示圖例名稱
plt.legend(loc = "right") # 設定 legnd 的位置


#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()





