# 派圖 集合

font_filename = 'C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf'

import sys
import matplotlib.pyplot as plt
import numpy as np

#設定中文字型及負號正確顯示
#設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei" # 將字體換成 Microsoft JhengHei
#設定負號
plt.rcParams["axes.unicode_minus"] = False # 讓負號可正常顯示

print('------------------------------------------------------------')	#60個

# 派圖 集合

#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '派圖 集合 1', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


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
values = [3, 48, 33, 8, 38]
labels = ['鼠', '牛', '虎', '兔', '龍']
colors = ['r', 'g', 'b', 'c', 'm']
# 分離係數，所以只有 '虎' 會分離
explode = (0, 0, 0.08, 0, 0)       #設定分隔的區塊位置

#設定 pie 函數參數繪製圓餅圖
# 從 90° 開始，逆時針排列，並加上陰影，並加上每塊的比例，格式為 '%1.2f%%'
plt.pie(values,             # 數值
        labels = labels,    # 項目標題
        colors = colors,    # 指定圓餅圖的顏色
        explode = explode,  # 設定分隔的區塊位置
	labeldistance = 1.1, 
	autopct = "%2.1f%%",    #項目百分比的格式, 顯示數字
        pctdistance = 0.5,  # 數值文字與圓心距離
        shadow = True,      # 圓餅圖陰影開啟/關閉
        startangle = 90,    # 繪製起始角度
        radius = 0.9        # 圓餅圖的半徑，預設是1
        )

#設定 legnd 的位置，將圖表顯示出來，並顯示圖例名稱
plt.legend(loc = "right") # 設定 legnd 的位置
#plt.legend()

plt.axis('equal')   # 調整比例，確認顯示為圓形

#第二張圖
plt.subplot(232)




#第三張圖
plt.subplot(233)



#第四張圖
plt.subplot(234)


#第五張圖
plt.subplot(235)


#第六張圖
plt.subplot(236)

lexus_models = {
    'CT-200h': 139, 
    'ES': 167, 
    'GS': 221, 
    'IS': 173,
    'LC': 539,
    'LS': 337,
    'LX': 465,
    'NX': 155,
    'RC': 243,
    'RX': 224,
    'RX L': 260,
    'UX': 139
               }
lexus_prices = np.array(list(lexus_models.values()), dtype=np.int64)
lexus = list()
lexus.append(np.count_nonzero(lexus_prices<=150))
lexus.append(np.count_nonzero((lexus_prices>150)&(lexus_prices<=200)))
lexus.append(np.count_nonzero((lexus_prices>200)&(lexus_prices<=300)))
lexus.append(np.count_nonzero(lexus_prices>300))

labels = ['<=150', '151~200', '201~300', '>300']
explode = [0.2, 0, 0, 0]

plt.pie(lexus, explode = explode, autopct = '%1.0f%%', radius = 1.0, labels = labels, shadow = True)

plt.show()


sys.exit()

print('------------------------------------------------------------')	#60個


#          編號               圖像大小[英吋]       解析度    背景色                      邊框顏色                      邊框有無
plt.figure(num = '派圖 集合 2', figsize = (20, 15), dpi = 84, facecolor = "whitesmoke", edgecolor = "r", linewidth = 1, frameon = True)

#第一張圖
plt.subplot(231)


#第二張圖
plt.subplot(232)


#第三張圖
plt.subplot(233)


#第四張圖
plt.subplot(234)





#第五張圖
plt.subplot(235)



#第六張圖
plt.subplot(236)




plt.show()

print('------------------------------------------------------------')	#60個






print('------------------------------------------------------------')	#60個


