# ch23_5.py
import pandas as pd
from urllib.parse import unquote
from pprint import pprint
import matplotlib.pyplot as plt
from pylab import mpl

df = pd.read_csv("out23_4.csv",index_col=0)
edu = df['學歷']                                # 獲得學歷欄位
education = []
for txt in edu:
    txt = txt[1:].replace('\\x','%')            # 將字串轉成url字串
    txt = txt.replace("'",'')                   # 拿掉'
    t = unquote(txt, encoding='utf-8')          # 轉成簡體中文
    education.append(t)                         # 加入學歷字串
# 計算每個學歷欄位的人數
education_count = {wd:education.count(wd) for wd in set(education)}
edu_list = []                                   # 學歷串列
edu_count = []                                  # 學歷人數
for e, c in education_count.items():
    print(e, c)
    edu_list.append(e)
    edu_count.append(c)    
# 繪製圓餅圖
mpl.rcParams["font.sans-serif"] = ["SimHei"]    # 使用黑體 
plt.pie(edu_count,labels=edu_list,explode=(0,0,0.2,0,0,0,0),
        autopct="%1.2f%%")                      # 繪製圓餅圖
plt.show()

    








