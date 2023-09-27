# plot1.py

# plot2.py

# plot3.py

# plot4.py
import matplotlib.pyplot as plt

listx = [0,800,1500,3200,4100,5000]
listy = [20,60,32,45,78,56]
plt.plot(listx, listy)
plt.xticks(range(0,5500,500))
plt.tick_params(axis='both', labelsize=10, color='red')
plt.show()


# plot5.py

# bar1.py
import matplotlib.pyplot as plt

listx = ['c','c++','c#','java','python']
listy = [45,28,38,32,50]
plt.bar(listx, listy, width=0.5, color='rgb')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# bar2.py
import matplotlib.pyplot as plt

listy = ['c','c++','c#','java','python']
listx = [45,28,38,32,50]
plt.barh(listy, listx, height=0.5, color='rgb')
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# bar3.py
import matplotlib.pyplot as plt

listx = ['c','c++','c#','java','python']
listy1 = [25,20,20,16,28]
listy2 = [20,8,18,16,22]
plt.bar(listx, listy1, width=0.5, label='男')
plt.bar(listx, listy2, width=0.5, bottom=listy1, label='女')
plt.legend()
plt.title("資訊程式課程選修人數")
plt.xlabel("程式課程")
plt.ylabel("選修人數")
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# bar4.py
import matplotlib.pyplot as plt

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
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# scatter.py
import matplotlib.pyplot as plt

listx = [31,15,20,25,12,18,45,21,33,5,18,22,37,42,10]
listy = [68,20,61,32,45,56,10,18,70,64,43,66,19,77,21]
scale = [x**3 for x in [5,4,2,6,7,1,8,9,2,3,2,4,5,7,2]]

plt.xlim(0,50)
plt.ylim(0,80)
plt.scatter(listx, listy, c='r', s=scale, marker='o', alpha=0.5)

plt.show()

# pie.py
import matplotlib.pyplot as plt

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
# 設定中文字型及負號正確顯示
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" 
plt.rcParams["axes.unicode_minus"] = False
plt.show()

# figure.py
import matplotlib.pyplot as plt
# 新增圖表區
plt.figure()
plt.plot([1,2,3])
# 新增圖表區並設定屬性
plt.figure(figsize=[8,4], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
plt.plot([1,2,3])

plt.show()

# subplot4.py
import matplotlib.pyplot as plt

plt.figure(figsize=[8,4])
plt.axes([0,0,0.4,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.5,0,0.4,1])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

# subplot5.py
import matplotlib.pyplot as plt

plt.figure(figsize=[8,4])
plt.axes([0,0,0.8,1])
plt.title(label='Chart 1')
plt.plot([1,2,3],'r:o')

plt.axes([0.55,0.1,0.2,0.2])
plt.title(label='Chart 2')
plt.plot([1,2,3],'g--o')

plt.show()

# booksale.py
import matplotlib.pyplot as plt

# 設定圖書分類及銷售額比例
listx = ['商業理財','文學小說','藝術設計','人文科普','語言電腦','心靈養生','生活風格','親子共享']
listm = [0.14,0.16,0.08,0.13,0.16,0.12,0.16,0.05] #男性比例
listf = [0.1,0.19,0.06,0.1,0.13,0.13,0.2,0.09] #女性比例
# 將比例乘以100
listm = [x*100 for x in listm] 
listf = [x*100 for x in listf]
# 設定圖表區尺寸以及使用字型
plt.figure(figsize=(12,9))
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

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
