import sys

import matplotlib.pyplot as plt
import numpy as np
import math

print('------------------------------------------------------------')	#60個

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

listx = [0,800,1500,3200,4100,5000]
listy = [20,60,32,45,78,56]
plt.plot(listx, listy)
plt.xticks(range(0,5500,500))
plt.tick_params(axis='both', labelsize=10, color='red')

plt.show()

print('------------------------------------------------------------')	#60個

listx = ['c','c++','c#','java','python']
listy = [45,28,38,32,50]
plt.bar(listx, listy, width=0.5, color='r')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

plt.show()

print('------------------------------------------------------------')	#60個

listy = ['c','c++','c#','java','python']
listx = [45,28,38,32,50]
plt.barh(listy, listx, height=0.5, color='r')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

plt.show()

print('------------------------------------------------------------')	#60個

listx = ['c','c++','c#','java','python']
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]
plt.bar(listx, listy1, width=0.5, label='男')
plt.bar(listx, listy2, width=0.5, bottom=listy1, label='女')
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

plt.show()

print('------------------------------------------------------------')	#60個

width = 0.25
listx = ['c','c++','c#','java','python']
listx1 = [x - width/2 for x in range(len(listx))]
listx2 = [x + width/2 for x in range(len(listx))]
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]
plt.bar(listx1, listy1, width, label='男')
plt.bar(listx2, listy2, width, label='女')
plt.xticks(range(len(listx)), labels=listx)
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")

plt.show()

print('------------------------------------------------------------')	#60個

listx = [31,15,20,25,12,18,45,21,33,5,18,22,37,42,10]
listy = [68,20,61,32,45,56,10,18,70,64,43,66,19,77,21]
scale = [x**3 for x in [5,4,2,6,7,1,8,9,2,3,2,4,5,7,2]]

plt.xlim(0,50)
plt.ylim(0,80)
plt.scatter(listx, listy, c='r', s=scale, marker='o', alpha=0.5)

plt.show()

print('------------------------------------------------------------')	#60個

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)
plt.pie(sizes, 
	explode = explode, 
	labels = labels, 
	colors = colors,
	labeldistance = 1.1, 
	autopct = "%2.1f%%", 
	pctdistance = 0.6,
	shadow = True,
	startangle = 90)

plt.show()

print('------------------------------------------------------------')	#60個

# 新增圖表區
plt.figure()
plt.plot([1,2,3])
# 新增圖表區並設定屬性
plt.figure(figsize=[8,4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(figsize=[8,4])
plt.axes([0,0,0.4,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.5,0,0.4,1])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

print('------------------------------------------------------------')	#60個

plt.figure(figsize=[8,4])
plt.axes([0,0,0.8,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.55,0.1,0.2,0.2])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

print('------------------------------------------------------------')	#60個

# 設定圖書分類及銷售額比例
listx = ['商業理財','文學小說','藝術設計','人文科普','語言電腦','心靈養生','生活風格','親子共享']
listm = [0.14,0.16,0.08,0.13,0.16,0.12,0.16,0.05] #男性比例
listf = [0.1,0.19,0.06,0.1,0.13,0.13,0.2,0.09] #女性比例
# 將比例乘以100
listm = [x*100 for x in listm] 
listf = [x*100 for x in listf]
# 設定圖表區尺寸以及使用字型
plt.figure(figsize=(12,9))

# 男性圖書分類銷售率圖餅圖
plt.subplot(221)
plt.title('圖書分類銷售比率-男性', fontsize=16)
plt.pie(listm, labels = listx, autopct='%2.1f%%')

# 女性圖書分類銷售率圖餅圖
plt.subplot(222)
plt.title('圖書分類銷售比率-女性', fontsize=16)
plt.pie(listf, labels = listx, autopct='%2.1f%%')

# 圖書分類男女銷售率長條圖
plt.subplot(223)
width = 0.4
listx1 = [x- width/2 for x in range(len(listx))]
listx2 = [x+ width/2 for x in range(len(listx))]

plt.title('圖書分類銷售長條圖-性別', fontsize=16)
plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)

plt.bar(listx1, listm, width, label='男')
plt.bar(listx2, listf, width, label='女')
plt.xticks(range(len(listx)), labels=listx, rotation=45)
plt.legend()

# 圖書分類男女銷售率折線圖
plt.subplot(224)
plt.title('圖書分類銷售折線圖-性別', fontsize=16)
plt.xlabel('圖書分類', fontsize=12)
plt.ylabel('銷售比率(%)', fontsize=12)

plt.plot(listx, listm, marker='s', label='男')
plt.plot(listx, listf, marker='s', label='女')
plt.gca().grid(True)
plt.xticks(rotation=45)
plt.legend()

plt.show()

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

n = np.linspace(1.1, 10, 90)            # 建立1.1-10的陣列
count = 0                               # 用於計算每5筆輸出換行
for i in n:
    count += 1
    print('{0:2.1f} = {1:4.3f}'.format(i, np.log10(i)), end='    ')
    if count % 5 == 0:                  # 每5筆輸出就換行
        print()

print('------------------------------------------------------------')	#60個

x1 = np.linspace(0.1, 10, 99)                   # 建立含30個元素的陣列
x2 = np.linspace(0.1, 10, 99)                   # 建立含30個元素的陣列
y1 = [math.log2(x) for x in x1]
y2 = [math.log(x, 0.5) for x in x2]
plt.plot(x1, y1, label="base = 2")
plt.plot(x2, y2, label="base = 0.5")

plt.legend(loc="best")                          # 建立圖例
plt.axis([0, 10, -5, 5])
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

degrees = [30, 45, 60, 90, 120, 135, 150, 180]
for degree in degrees:
    print('角度 = {0:3d},   弧度 = {1:6.3f}'.format(degree, math.pi*degree/180))

print('------------------------------------------------------------')	#60個

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    curve = 2 * math.pi * r * degree / 360
    print('角度 = {0:3d},   弧長 = {1:6.3f}'.format(degree, curve))

print('------------------------------------------------------------')	#60個

degrees = [30, 60, 90, 120]
r = 10
for degree in degrees:
    area = math.pi * r * r * degree / 360
    print('角度 = {0:3d},   扇形面積 = {1:6.3f}'.format(degree, area))

print('------------------------------------------------------------')	#60個

degrees = [x*30 for x in range(0,13)]
for d in degrees:
    rad = math.radians(d)
    sin = math.sin(rad)
    cos = math.cos(rad)
    print('角度={0:3d}, 弧度={1:5.2f}, sin{2:3d}={3:5.2f}, cos{4:3d}={5:5.2f}'
          .format(d, rad, d, sin, d, cos))

print('------------------------------------------------------------')	#60個

degrees = [x*15 for x in range(0,25)]
x = [math.cos(math.radians(d)) for d in degrees]
y = [math.sin(math.radians(d)) for d in degrees]

plt.scatter(x,y)
plt.axis('equal')
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

degrees = np.arange(0, 360)
x = np.cos(np.radians(degrees))
y = np.sin(np.radians(degrees))

plt.plot(x,y)
plt.axis('equal')
plt.grid()
plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0.1, 1000, 100000)          # 建立含100000個元素的陣列
y = [(1+1/x)**x for x in x]
plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0.1, 1000, 100000)          # 建立含100000個元素的陣列
y = [(1+1/x)**x for x in x]
#plt.axis([0, 10, 0, 3])
plt.plot(x, y, label="Euler's Number")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(-5, 5, 10000)               # 建立含10000個元素的陣列
y = [1/(1+np.e**-x) for x in x]
plt.axis([-5, 5, 0, 1])
plt.plot(x, y, label="Logistic function")

plt.legend(loc="best")                      # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

x = np.linspace(0.01, 0.99, 100)               # 建立含1000個元素的陣列
y = [np.log(x/(1-x)) for x in x]
plt.axis([0, 1, -5, 5])
plt.plot(x, y, label="Logit function")
plt.plot(0.5, np.log(0.5/(1-0.5)),'-o')

plt.legend(loc="best")                          # 建立圖例
plt.grid()

plt.show()

print('------------------------------------------------------------')	#60個

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()

print('------------------------------------------------------------')	#60個

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

#plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

plt.show()


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個

