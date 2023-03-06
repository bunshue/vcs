# Python 新進測試 17


print("畫一個派圖")

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
plt.show()




print("畫圖表 1")
import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, 'g--*', markersize=12)
plt.show()


print("畫圖表 2")
import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title", fontsize=20)	#圖表標題
plt.xlabel("X-Label", fontsize=14)		#x座標標題
plt.ylabel("Y-Label", fontsize=14)		#y座標標題
plt.legend()
plt.show()


print("畫圖表 3")
import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")	#圖表標題
plt.xlabel("X-Label")		#x座標標題
plt.ylabel("Y-Label")		#y座標標題
plt.xlim(0, 20)            #設定x座標範圍
plt.ylim(0, 100)             #設定y座標範圍
plt.legend()
plt.show()


print("畫圖表 4")
import matplotlib.pyplot as plt

listx = [1,5,7,9,13,18]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")	#圖表標題
plt.xlabel("X-Label")		#x座標標題
plt.ylabel("Y-Label")		#y座標標題
plt.xlim(0, 20)            #設定x座標範圍
plt.ylim(0, 100)             #設定y座標範圍
plt.grid(color='black', linestyle=":", linewidth='1', alpha=0.5)
plt.legend()
plt.show()


