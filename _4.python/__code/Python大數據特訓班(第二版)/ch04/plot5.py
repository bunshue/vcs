import matplotlib.pyplot as plt

listx = [0,5,7,12,18,20]
listy = [20,60,32,45,78,56]
plt.plot(listx, listy, color="red", lw="2.0", ls="--", label="label")
plt.title("Chart Title")    #圖表標題
plt.xlabel("X-Label")       #x座標標題
plt.ylabel("Y-Label")       #y座標標題
plt.xlim(0, 20)             #設定x座標範圍
plt.ylim(0, 100)            #設定y座標範圍
plt.grid(color='black', linestyle=":", linewidth='1', alpha=0.5)
plt.legend()
plt.show()