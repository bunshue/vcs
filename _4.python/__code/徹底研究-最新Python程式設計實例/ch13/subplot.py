# -*- coding: utf-8 -*- 

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] ='Microsoft JhengHei'
plt.rcParams['font.size']=12

#橫條圖
def diagram_1(s,x):
	plt.barh(x, s)

#圓餅圖
def diagram_2(s,x):	 
	plt.pie(s,labels=x, autopct='%.2f%%')
#折線圖+長條圖

def diagram_4(s,x):
    plt.plot(x, s, marker='.')
    plt.bar(x, s, alpha=0.5)	

#長條圖
def diagram_3(s,x):
	plt.bar(x, s)	

#要繪圖的數據
x = ['高雄','台中','宜蘭','花蓮']
s = [89,58,63,50]

#設定子圖
plt.figure(1, figsize=(8, 8),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s,x)

plt.subplot(222)
diagram_2(s,x)

plt.subplot(223)
diagram_3(s,x)

plt.subplot(2,2,4)
diagram_4(s,x)

plt.show()
