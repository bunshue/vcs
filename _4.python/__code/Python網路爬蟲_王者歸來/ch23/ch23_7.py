# ch23_7.py
import pandas as pd
import matplotlib.pyplot as plt
from pylab import mpl

df = pd.read_csv("out23_4.csv",index_col=0)
ages = df['出生年']                             # 獲得出生年欄位
age_index = [0,0,0,0,0]                         # 歲數區間欄位

for age in ages:
    if int(age) < 1980:
        age_index[0] += 1                       # 大於40歲
    elif int(age) < 1985:                   
        age_index[1] += 1                       # 35 < age <= 40
    elif int(age) < 1990:
        age_index[2] += 1                       # 30 < age <= 35
    elif int(age) < 1995:
        age_index[3] += 1                       # 25 < age <= 30
    else:
        age_index[4] += 1                       # 小於25
        
fields = ['>40', '35-40', '30-35', '25-30', '<25']
# 繪製直條圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]    # 使用黑體
plt.bar(fields, age_index, width=0.35)
plt.ylabel('人數')
plt.xlabel('年齡')
plt.show()       
   





