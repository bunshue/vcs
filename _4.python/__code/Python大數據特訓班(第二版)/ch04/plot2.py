import matplotlib.pyplot as plt

listx = [0,5,7,12,18,20]
listy = [20,60,32,45,78,56]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title", fontsize=20)	#圖表標題
plt.xlabel("X-Label", fontsize=14)		#x座標標題
plt.ylabel("Y-Label", fontsize=14)		#y座標標題
plt.legend()
plt.show()