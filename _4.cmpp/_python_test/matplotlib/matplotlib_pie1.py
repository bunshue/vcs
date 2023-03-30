# 派圖 集合

selected_font = 'C:/_git/vcs/_4.cmpp/_python_test/data/msch.ttf'

import matplotlib.pyplot as plt
import numpy as np

#plt.figure(figsize=(8,8))	#設定圖片視窗大小
plt.figure(num = 'plot 集合', figsize=[20, 15], dpi=84, facecolor="whitesmoke", edgecolor="r", linewidth=1, frameon=True)
#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

#第一張圖
plt.subplot(231)

sizes = [25, 30, 15, 10]
labels = ["北部", "西部", "南部", "東部"]
colors = ["red", "green", "blue", "yellow"]
explode = (0, 0, 0.2, 0)
#explode = (0, 0, 0.05, 0)
plt.pie(sizes, 
	explode = explode, 
	labels = labels, 
	colors = colors,
	labeldistance = 1.1, 
	autopct = "%2.1f%%", 
	pctdistance = 0.6,
	shadow = True,
	startangle = 90)

plt.axis("equal")
plt.legend()


#第二張圖
plt.subplot(232)

'''
圓餅圖是使用 pie 函數繪製出來的，語法為：

plt.pie(串列資料, [其餘參數值])

其餘參數介紹：
pie參數 	說明
color 	指定圓餅圖的顏色 ('blue', 'red', 'green', 'yellow', 色碼('#CC00CC')),預設為藍色 blue
label 	項目標題，需搭配 legend 函式才有效果
explode 	設定分隔的區塊位置
autopct 	項目百分比格式，語法為「%格式%%」，Example:autopct = "%2.2f%%"(表示整數2位數及小數點2位數)
pctdistance 	數值文字與圓心距離
shadow 	圓餅圖陰影開啟/關閉，True 有陰影，False 沒有陰影
startangle 	繪製起始角度，繪製會以逆時鐘旋轉計算角度
radius 	圓餅圖的半徑，預設是1
'''

#設定將使用的數值，將要有項目標題、數值串列、圓餅圖顏色、分隔的區塊位置
labels = ['A', 'B', 'C', 'D']
values = [60, 42, 83, 37]
colors = ['r', 'g', 'b', 'y']
explode = (0, 0, 0, 0.08)

#設定 pie 函數參數繪製圓餅圖
plt.pie(
values, # 數值
labels = labels, # 項目標題
colors = colors, # 指定圓餅圖的顏色
explode = explode, # 設定分隔的區塊位置
autopct = "%2.2f%%", # 項目百分比格式
pctdistance = 0.5, # 數值文字與圓心距離
shadow = True, # 圓餅圖陰影開啟/關閉
startangle = 90, # 繪製起始角度
radius = 0.9 # 圓餅圖的半徑，預設是1
)

#設定 legnd 的位置，將圖表顯示出來，並顯示圖例名稱
plt.legend(loc = "right") # 設定 legnd 的位置


#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)



#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)



plt.show()



