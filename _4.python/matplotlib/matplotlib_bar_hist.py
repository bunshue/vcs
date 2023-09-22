# bar + hist 集合

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

n, bins, patches = plt.hist(x, num_bins, facecolor = 'yellow', edgecolor = 'yellow')
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

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '新進1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
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

cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4]

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

#plt.xticks(range(len(ChineseZodiacSigns)), ChineseZodiacSigns.keys())
#以上1行 相當於 以下3行
seq = [0, 1, 2, 3]
labels = ['鼠', '牛', '虎', '兔']
plt.xticks(seq, labels)

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





#第二張圖
plt.subplot(232)

#長條圖範例  bar圖畫字典

ranking = {
    'Toyota RAV4': 2958,
    'CMC Veryca': 1312,
    'Nissan Kicks': 1267,
    'Honda CRV': 1209,
    'Toyota Sienta': 1163,
    'Toyota Yaris': 936, 
    'Toyota': 911,
    'Ford Focus': 873,
    'M-Benz C-Class': 749,
    'Honda HR-V':704
}

plt.bar(range(len(ranking.values())), ranking.values(), width=0.8)
plt.xticks(range(len(ranking.values())), ranking.keys(), rotation=45)




#第三張圖
plt.subplot(233)

n = 10
x = [i for i in range(0, n+1)]                  # 長條圖x軸座標
y = x
width = 0.35                                    # 長條圖寬度
plt.xticks(x)
plt.bar(x, y, width, color='g')                 # 繪製長條圖

#第四張圖
plt.subplot(234)

plt.bar(range(10), np.random.randint(1,30,10), fc='#e55934')



#第五張圖
plt.subplot(235)

plt.bar(range(1,6), np.random.randint(1,30,5))


#第六張圖
plt.subplot(236)

plt.bar(np.arange(0.6, 5), np.random.randint(1,30,5))



plt.show()

print('------------------------------------------------------------')	#60個



