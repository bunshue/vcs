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