# ch23_6.py
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

df = pd.read_csv("out23_4.csv",index_col=0)
height = df['身高']                               # 獲得身高欄位
h_index = [0,0,0,0,0]                             # 身高區間欄位
for h in height:
    if int(h) < 150:
        h_index[0] += 1
    elif int(h) < 160:
        h_index[1] += 1
    elif int(h) < 170:
        h_index[2] += 1
    elif int(h) < 180:
        h_index[3] += 1
    else:
        h_index[4] += 1
    
fields = ['<150', '15x', '16x', '17x', '>180']
# 繪製直條圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]      # 使用黑體
plt.bar(fields, h_index, width=0.35)
plt.ylabel('人數')
plt.xlabel('身高')
plt.show()

    








