# python import module : matplotlib plot 畫折線圖

#導入模組
import matplotlib.pyplot as plt

x1 = [1, 5, 9, 13, 17]
y1 = [5, 30, 15, 35, 5]

#連線
#plt.plot(x1, y1, color='red')

#linestyle 虛線樣式
#plt.plot(x1, y1, color='red', linestyle="--")

#linestyle 虛點樣式
#plt.plot(x1, y1, color='red', linestyle="-.")

#linestyle 虛點樣式「:」
#plt.plot(x1, y1, color='red', linestyle=":")

#marker 點「.」標記
#因為需要展示出效果，因此把 linestyle 設為實線，linewidth 為 2.0，markersize 設為 16
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".")

#marker 圓「o」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="o")

#marker 星「*」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="*")

#marker 矩形「s」標記
#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker="s")


#plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".", label="Test")


# 繪製折線圖，顏色「紅色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 1」
plt.plot(x1, y1, color='red', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 1")

x2 = [3, 8, 12, 16, 20]
y2 = [8, 33, 18, 38, 8]
# 繪製折線圖，顏色「藍色」，線條樣式「-」，線條寬度「2」，標記大小「16」，標記樣式「.」，圖例名稱「Plot 2」
plt.plot(x2, y2, color='blue', linestyle="-", linewidth="2", markersize="16", marker=".", label="Plot 2")


plt.xlabel('x label', fontsize="10") # 設定 x 軸標題內容及大小
plt.ylabel('y label', fontsize="10") # 設定 y 軸標題內容及大小
plt.title('Plot title', fontsize="18") # 設定圖表標題內容及大小

#設定 x, y 軸座標範圍
#plt.xlim(0, 30) # 設定 x 軸座標範圍
#plt.ylim(0, 50) # 設定 y 軸座標範圍

plt.legend()

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

plt.show()  #將圖表呈現出來

