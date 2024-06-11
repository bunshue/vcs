'''
#pandas製作資料 修改資料 用matplotlib顯示

'''

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

# 使用 NumPy 生成随机数
random_data = np.random.normal(170, 10, 250)

# 将数据转换为 Pandas DataFrame
dataframe = pd.DataFrame(random_data)

# 使用 Pandas hist() 方法绘制直方图
dataframe.hist()

# 设置图表属性
plt.title("RUNOOB hist() Test")
plt.xlabel("X-Value")
plt.ylabel("Y-Value")

plt.show()

print("------------------------------------------------------------")  # 60個

# 生成随机数据
data = pd.Series(np.random.normal(size=100))

data.hist()

# 设置图形标题和坐标轴标签
plt.title("RUNOOB hist() Tes")
plt.xlabel("X-Values")
plt.ylabel("Y-Values")

plt.show()

print("------------------------------------------------------------")  # 60個

# 構建序列
data1 = pd.Series(
    {"中專": 0.2515, "大專": 0.3724, "本科": 0.3336, "碩士": 0.0368, "其他": 0.0057}
)
print(data1)
data1.name = ""
# 控制餅圖為正圓
plt.axes(aspect="equal")
# plot方法對序列進行繪圖
data1.plot(
    kind="pie",  # 選擇圖形類型
    autopct="%.1f%%",  # 餅圖中添加數值標簽
    radius=1,  # 設置餅圖的半徑
    startangle=180,  # 設置餅圖的初始角度
    counterclock=False,  # 將餅圖的順序設置為順時針方向
    title="失信用戶的受教育水平分布",  # 為餅圖添加標題
    wedgeprops={"linewidth": 1.5, "edgecolor": "green"},  # 設置餅圖內外邊界的屬性值
    textprops={"fontsize": 10, "color": "black"},  # 設置文本標簽的屬性值
)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

print('------------------------------------------------------------')	#60個


print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個



print('------------------------------------------------------------')	#60個


