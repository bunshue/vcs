# python import module : matplotlib pie

print("圓餅圖的應用")

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

#導入模組

import matplotlib.pyplot as plt

#設定將使用的數值，將要有項目標題、數值串列、圓餅圖顏色、分隔的區塊位置

labels = ['A', 'B', 'C', 'D']
values = [60, 42, 83, 37]
colors = ['r', 'g', 'b', 'y']
explode = (0, 0, 0, 0.08)

#設定圖表區寬高

plt.figure(figsize=(10,10)) # 設定圖表區寬高

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
plt.show()







