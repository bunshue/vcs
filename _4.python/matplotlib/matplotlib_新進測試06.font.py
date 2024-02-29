"""
另法顯示中文
"""

import matplotlib.pyplot as plt  # 圖表使用套件

listCity = ['高雄市', '屏東縣', '臺東縣', '新北市', '臺中市', '臺北市', '臺南市', '新竹縣', '彰化縣', '嘉義縣', '雲林縣', '桃園市', '宜蘭縣', '苗栗縣', '南投縣', '基隆市', '花蓮縣']

listCount = [12, 24, 11, 11, 18, 8, 16, 11, 18, 8, 11, 9, 54, 40, 31, 10, 9]

# 繪製柱狀圖
font = {"family": "DFKai-SB"}  # 設定柱狀圖可以顯示中文
plt.rc("font", **font)
plt.barh(listCity, listCount, label="農業區")  # 橫向柱狀圖串列數據設定
plt.title("各縣市農場數量")  # 柱狀圖名稱
plt.xlim(0, 60)  # X軸範圍0~60
plt.xlabel("數量")  # X軸名稱
plt.ylabel("縣市")  # Y軸名稱
for y, x in enumerate(listCount):  # 使用迴圈讓柱狀末端顯示各縣市農業區總數
    plt.text(x, y, "%s" % x, ha="center")
plt.legend()  # 圖例(柱狀圖)說明
plt.grid(True)  # 顯示格線

plt.show()  # 顯示繪圖結果


