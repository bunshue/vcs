# bar 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'bar 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

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

print('------------------------------------------------------------')	#60個

# hist 集合

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'hist 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

# Fixing random state for reproducibility
np.random.seed(1234567)

N = 10000 #資料個數
num_bins = 100 #直方圖顯示時的束數

#第一張圖
plt.subplot(231)

print('以直方圖顯示常態分佈')
x = np.random.randn(N)  #常態分佈數字

n, bins, patches = plt.hist(x, num_bins, facecolor='yellow', edgecolor='yellow')
print(n)
print(bins)

#第二張圖
plt.subplot(232)

normal_samples = np.random.normal(size = N) # 生成 N 組標準常態分配（平均值為 0，標準差為 1 的常態分配）隨機變數
plt.hist(normal_samples, bins = num_bins)

#第三張圖
plt.subplot(233)

uniform_samples = np.random.uniform(size = N) # 生成 N 組介於 0 與 1 之間均勻分配隨機變數
plt.hist(uniform_samples, bins = num_bins)

#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()

print('------------------------------------------------------------')	#60個


# 派圖 集合

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '派圖 集合', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

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

labels = ["東部", "南部", "北部", "中部"]
sizes = [5, 10, 20, 15]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.05, 0)
plt.pie(sizes,explode = explode,labels = labels,colors = colors,\
    labeldistance = 1.1,autopct = "%3.1f%%",shadow = True,\
    startangle = 90,pctdistance = 0.6)
plt.axis("equal")
plt.legend()


#第四張圖
plt.subplot(234)

labels = ["Python","C++","Java","JS","C","C#"]
ratings = [5, 6, 15, 3, 12, 4]

plt.pie(ratings, labels=labels)
plt.title("程式語言的使用率") 
plt.axis("equal")

#第五張圖
plt.subplot(235)

patches, texts = plt.pie(ratings, labels=labels)
plt.legend(patches, labels, loc="best")
plt.title("程式語言的使用率") 
plt.axis("equal")


#第六張圖
plt.subplot(236)

lexus_models = {
    'CT-200h': 139, 
    'ES': 167, 
    'GS': 221, 
    'IS': 173,
    'LC': 539,
    'LS': 337,
    'LX': 465,
    'NX': 155,
    'RC': 243,
    'RX': 224,
    'RX L': 260,
    'UX': 139
               }
lexus_prices = np.array(list(lexus_models.values()), dtype=np.int64)
lexus = list()
lexus.append(np.count_nonzero(lexus_prices<=150))
lexus.append(np.count_nonzero((lexus_prices>150)&(lexus_prices<=200)))
lexus.append(np.count_nonzero((lexus_prices>200)&(lexus_prices<=300)))
lexus.append(np.count_nonzero(lexus_prices>300))
labels = ['<=150', '151~200', '201~300', '>300']
explode = [0.2, 0, 0, 0]
plt.pie(lexus, explode=explode, autopct='%1.0f%%', 
        radius=2.0, labels=labels, shadow=True)
plt.title('Lexus Models Prices')

plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

labels = ["Python","C++","Java","JS","C","C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]

plt.bar(index, ratings)
plt.xticks(index, labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 

#第二張圖
plt.subplot(232)


plt.barh(index, ratings)
plt.yticks(index, labels)
plt.xlabel("使用率")
plt.title("程式語言的使用率") 




#第三張圖
plt.subplot(233)


index = np.arange(len(labels)*2)

plt.bar(index[0::2], ratings, label="rating")
plt.bar(index[1::2], change, label="change",
        color="r")
plt.legend()
plt.xticks(index[0::2], labels)
plt.ylabel("使用率")
plt.title("程式語言的使用率") 

#第四張圖
plt.subplot(234)

from collections import Counter

cyl = [6 ,6 ,4 ,6 ,8 ,6 ,8 ,4 ,4 ,6 ,6 ,8 ,8 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,4 ,8 ,8 ,8 ,8 ,4 ,4 ,4 ,8 ,6 ,8 ,4]

labels, values = zip(*Counter(cyl).items())
indexes = np.arange(len(values))

plt.bar(indexes, values, width = 0.5)
plt.xticks(indexes, labels)


#第五張圖
plt.subplot(235)


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


#第六張圖
plt.subplot(236)

print('用bar圖畫出字典資料 並標明數值')
ChineseZodiacSigns = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8}
print(type(ChineseZodiacSigns))
print(ChineseZodiacSigns)

plt.bar(range(len(ChineseZodiacSigns)), ChineseZodiacSigns.values(), facecolor="#99ccff")
plt.xticks(range(len(ChineseZodiacSigns)), ChineseZodiacSigns.keys())
plt.ylim((0, 55))
for x, y in zip(range(len(ChineseZodiacSigns)), ChineseZodiacSigns.values()):
    plt.text(x-0.05, y+0.5, "{:>8,.0f}".format(y), ha='center')



plt.show()


print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

plt.bar(range(1,6), np.random.randint(1,30,5))

#第二張圖
plt.subplot(232)

plt.bar(np.arange(0.6, 5), np.random.randint(1,30,5))

#第三張圖
plt.subplot(233)

#雙色的長條圖
x = np.arange(1,6)
plt.bar(x - 0.4, [3, 10, 8, 12, 6], width=0.4, ec='none', fc='#e63946')
plt.bar(x, [6, 3, 12, 5, 8], width=0.4, ec='none', fc='#7fb069')

#第四張圖
plt.subplot(234)

#疊加型的資料
A = np.random.randint(2,15,5)
B = np.random.randint(2,15,5)
C = np.random.randint(2,15,5)

plt.bar(x, A, fc='#e63946', ec='none')
plt.bar(x, B, fc='#7fb069', ec='none', bottom = A)
plt.bar(x, C, fc='#e55934', ec='none', bottom = A+B)

#第五張圖
plt.subplot(235)

#橫放的長條圖
x = np.arange(0.6, 6)
plt.barh(x, np.random.randint(1,15,6), fc='#e55934', ec='none')

#第六張圖
plt.subplot(236)

#雙向的長條圖
x = np.arange(0.6,6)
A = np.random.randint(1,15,6)
B = np.random.randint(1,15,6)
plt.barh(x, A, fc='#e63946', ec='none')
plt.barh(x, -B, fc='#7fb069', ec='none')



plt.show()

print('------------------------------------------------------------')	#60個

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

area = ['大陸','東南亞','東北亞','美國','歐洲','澳紐']
people = [10000,12600,9600,7500,5100,4800]

'''
#case 1
plt.pie(people,labels=area)

#case 2
plt.pie(people,labels=area,autopct="%1.2f%%")
'''
#case 3, 突出一塊
exp = [0.0,0.0,0.0,0.0,0.0,0.1]
plt.pie(people,labels=area,explode=exp,autopct="%1.2f%%")

plt.title('五月份國外旅遊調查表',fontsize=16,color='b')




#第二張圖
plt.subplot(232)





#第三張圖
plt.subplot(233)





#第四張圖
plt.subplot(234)





#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)




plt.show()

print('------------------------------------------------------------')	#60個



