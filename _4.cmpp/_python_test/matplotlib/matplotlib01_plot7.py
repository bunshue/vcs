import matplotlib.pyplot as plt

#在同一張圖 畫 兩條曲線

month1 = [1,2,3,4,5,6,7,8,9,10,11,12]
month2 = [1,2,3,4,5,6,7,8,9,10,11,12]

listy1 = [128,210,199,121,105,98,152,107,150,122,180,220]
listy2 = [150,200,180,110,100,80,80,100,130,120,110,200]

plt.plot(month1, listy1) #直線連線
plt.plot(month1, listy1, 'r-.s')#少參數
plt.plot(month1, listy1, 'r-.s', lw=2, ms=10, label="台北")#多參數

plt.plot(month2, listy2) #直線連線
plt.plot(month2, listy2, 'g--*')#少參數
plt.plot(month2, listy2, 'g--*', lw=2, ms=10, label="台中")#多參數

#同一個指令畫兩條線
#plt.plot(month1, listy1, 'r-.s', month2, listy2, 'y-s')

plt.legend()
plt.xticks(month1)
plt.xlim(0.5, 12.5)     #x軸顯示邊界
plt.ylim(50, 250)   #y軸顯示邊界
plt.title("Sales Report", fontsize=18)
plt.xlabel("Month", fontsize=12)
plt.ylabel("Million", fontsize=12)
plt.title("銷售報表", fontsize=18)
plt.xlabel("月", fontsize=12)
plt.ylabel("百萬", fontsize=12)

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.grid(color='k', ls=':', lw=1, alpha=0.5)    #畫格點

plt.tick_params(axis='both', labelsize=16, color='red')#xy軸多加tick
#plt.tick_params(axis='y', color='red')#y軸多加tick

plt.show()  #將圖表呈現出來
