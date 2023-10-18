# bar 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'bar 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

print('用bar圖畫出字典資料 並標明數值')
animals = {'鼠' : 3, '牛' : 48, '虎' : 33, '兔' : 8}
print(type(animals))
print(animals)

plt.bar(range(len(animals)), animals.values(), facecolor="#99ccff")

#plt.xticks(range(len(animals)), animals.keys())
#以上1行 相當於 以下3行
seq = [0, 1, 2, 3]
labels = ['米老鼠', '班尼牛', '跳跳虎', '彼得兔']
plt.xticks(seq, labels, rotation = -45)

plt.ylim((0, 55))
for x, y in zip(range(len(animals)), animals.values()):
    plt.text(x-0.05, y+0.5, "{:>8,.0f}".format(y), ha='center')


#第二張圖
plt.subplot(232)

print("垂直/水平 長條圖");

#設定將使用的數值
x = ['國文', '英文', '數學', '社會', '自然']
y = [79, 63, 71, 83, 97]

print("垂直長條圖");
#繪製出垂直 Bar，這邊使用的是 bar 函數，設定的是 width 寬度
plt.bar(x, y, width = 0.5, color = 'red')       #直向bar圖
#plt.bar(x, y, fc = '#e55934', ec = 'none')      #直向bar圖
#plt.xticks(x, y)       #設定x軸刻度為文字

print("水平長條圖");
#繪製出水平 Bar，這邊使用的是 barh 函數，設定的是 height 寬度
#plt.barh(x, y, height = 0.5, color = 'blue')   #橫向bar圖
#plt.barh(x, y)                                 #橫向bar圖
#plt.yticks(index, labels)       #設定y軸刻度為文字


#第三張圖
plt.subplot(233)

"""
#疊加長條圖的應用
#疊加長條圖是繪製出兩個長條圖，並以推疊的方式繪製而出的
#設定將使用的數值，因為這邊需要兩組數值，因此有 y1, y2
"""

x = ['國文', '英文', '數學', '社會', '自然']
y1 = [30, 26, 37, 22, 28]
y2 = [20, 31, 24, 24, 33]

#Step 3. 將兩條長條圖繪製出來，其中第二條 y2 的 y 軸基底座標是建立在 y1 上

plt.bar(x, y1, width = 0.5, label = '男')
plt.bar(x, y2, width = 0.5, bottom = y1, label = '女')

plt.legend()


#第四張圖
plt.subplot(234)

x = ['c', 'c++', 'c#', 'java', 'python']
y1 = [25,20,20,16,28]
y2 = [20,8,18,16,22]

plt.bar(x, y1, width = 0.5, label = '男')
plt.bar(x, y2, width = 0.5, bottom = y1, label = '女')

plt.legend()

#第五張圖
plt.subplot(235)

width = 0.25
listx = ['c', 'c++', 'c#', 'java', 'python']
listx1 = [x - width / 2 for x in range(len(listx))]
listx2 = [x + width / 2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]

plt.bar(listx1, listy1, width, label = '男')
plt.bar(listx2, listy2, width, label = '女')

plt.xticks(range(len(listx)), labels = listx)

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

plt.show()


print('------------------------------------------------------------')	#60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'bar 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

labels = ["Python", "C++", "Java", "JS", "C", "C#"]
index = np.arange(len(labels))
ratings = [5.16, 5.73, 14.99, 3.17, 11.86, 4.45]
change = [1.12, 0.3, -1.69, 0.29, 3.41, -0.45]

index = np.arange(len(labels) * 2)
plt.bar(index[0::2], ratings, label = "rating")
plt.bar(index[1::2], change, label = "change", color="r")
plt.legend()
plt.xticks(index[0::2], labels)

#第二張圖
plt.subplot(232)

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_txt/台灣各縣市人口.txt'

with open(filename, 'r') as fp:
	populations = fp.readlines()

city = list()
popu = list()

for p in populations:
	cc, pp = p.split(',')
	city.append(cc)
	popu.append(int(pp))

index = np.arange(len(city))

print(index)
print(city)
print(popu)
plt.bar(index, popu)
plt.xticks(index + 0.5, city, rotation = -70)

#第三張圖
plt.subplot(233)


#長條圖範例  bar圖畫字典

animals = {
        '鼠': 3,
        '牛': 48,
        '虎': 33,
        '兔': 8,
        '龍': 38,
        '蛇': 16,
        '馬': 36,
        '羊': 29,
        '猴': 22,
        '雞': 6,
        '狗': 12,
        '豬': 42
        }

plt.bar(range(len(animals.values())), animals.values(), width = 0.8)
plt.xticks(range(len(animals.values())), animals.keys())


#第四張圖
plt.subplot(234)

n = 10
x = [i for i in range(0, n+1)]                  # 長條圖x軸座標
y = x
width = 0.35                                    # 長條圖寬度
plt.xticks(x)
plt.bar(x, y, width, color='g')                 # 繪製長條圖

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

#第六張圖
plt.subplot(236)


plt.show()

print('------------------------------------------------------------')	#60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'bar 集合 3', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

weights = [3, 48, 33, 8, 38]
plt.bar(range(1,6), weights)

#第二張圖
plt.subplot(232)

plt.bar(np.arange(0.6, 5), weights)


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

print('------------------------------------------------------------')	#60個
#          編號              圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = 'bar 集合 4', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)

listx = ['c', 'c++', 'c#', 'java', 'python']
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx, listy1, width = 0.5, label = '男')
plt.bar(listx, listy2, width = 0.5, bottom = listy1, label = '女')
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

#第二張圖
plt.subplot(232)

width = 0.25
listx = ['c','c++','c#','java','python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]
listy1 = [25, 20, 20, 16, 28]
listy2 = [20, 8, 18, 16, 22]
plt.bar(listx1, listy1, width, label = '男')
plt.bar(listx2, listy2, width, label = '女')
plt.xticks(range(len(listx)), labels = listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

#第三張圖
plt.subplot(233)

print('畫出頻率分布圖')

filename = 'C:/_git/vcs/_1.data/______test_files1/__RW/_csv/python_ReadWrite_CSV6_score.csv'

dat = pd.read_csv(filename, encoding = 'UTF-8')

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
x = list(range(1, 11))  # x軸的值
labels = ['0~', '10~', '20~', '30~', '40~', '50~', '60~', '70~', '80~', '90~']  # x軸的刻度標籤
plt.bar(x, hist, tick_label = labels, width = 1)  # 描繪長條圖

#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)




plt.show()

print('------------------------------------------------------------')	#60個





print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個
print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



"""
plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小

plt.xlabel('程式課程', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('選修人數', fontsize="10") # 設定 y 軸標題標題內容及大小
plt.title('資訊程式課程選修人數', fontsize="18") # 設定圖表標題內容及大小






較複雜的


-------------------

from collections import Counter

cyl = [6, 6, 4, 6, 8, 6, 8, 4, 4, 6, 6, 8, 8, 8, 8, 8, 8, 4, 4, 4, 4, 8, 8, 8, 8, 4, 4, 4, 8, 6, 8, 4]

labels, values = zip(*Counter(cyl).items())
indexes = np.arange(len(values))

plt.bar(indexes, values, width = 0.5)
plt.xticks(indexes, labels)



-------------------



-------------------


-------------------






"""
