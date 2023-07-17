import matplotlib.pyplot as plt

listx = [1,5,7,9,13,16]
listy = [15,50,80,40,70,50]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title", fontsize=20)	#圖表標題
plt.xlabel("X-Label", fontsize=14)		#x座標標題
plt.ylabel("Y-Label", fontsize=14)		#y座標標題
plt.legend()
plt.show()