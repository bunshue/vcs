"""
pandas的使用


"""


print("------------------------------")  # 30個

# 共同
import os
import sys
import time
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

# 1111city.py
import pandas as pd
import matplotlib.pyplot as plt

# 繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("1111data.xlsx")
city = ["台北", "新北", "桃園", "台中", "台南", "高雄"]  # 六都
citycount = []  # 存六都工作職缺數量的串列
for i in range(len(city)):
    df1 = df[df["工作地點"].str.contains(city[i])]  # 取出包含指定地點的資料
    citycount.append(len(df1))

ser = pd.Series(citycount, index=city)  # 串列轉Series
print(ser)
plt.axis("off")
ser.plot(kind="pie", title="六都電腦職缺數量", figsize=(6, 6))  # 繪製圓餅圖

print("------------------------------------------------------------")  # 60個

# 1111salary.py
import pandas as pd
import re
import matplotlib.pyplot as plt

# 繪圖中文字型
plt.rcParams["font.sans-serif"] = "mingliu"
plt.rcParams["axes.unicode_minus"] = False

df = pd.read_excel("1111data.xlsx")
city = ["台北", "新北", "桃園", "台中", "台南", "高雄"]  # 六都
salarylist = []
for i in range(len(city)):
    df1 = df[(df["工作地點"].str.contains(city[i])) & (df["薪資"].str.contains("月薪"))]
    indexlist = df1.index  # 取得資料索引
    total = 0  # 薪資總額
    for j in range(len(df1)):
        salarytem = df1["薪資"][indexlist[j]].replace(",", "")  # 以資料索引取得資料
        salanum = re.findall(r"\d+\.?\d*", salarytem)  # 取出資料中的數值
        if len(salanum) == 1:  # 若是1個數值即為薪資
            salary = int(salanum[0])
        else:  # 若是2個數值則取平均數
            salary = (int(salanum[0]) + int(salanum[1])) / 2
        total += salary
    salarycity = int(total / len(df1))  # 平均薪資
    salarylist.append(salarycity)

ser = pd.Series(salarylist, index=city)  # 串列轉Series
print(ser)
plt.ylabel("單位：元")
ser.plot(kind="bar", title="六都電腦職缺薪資", figsize=(5, 5))  # 繪製長條圖

print("------------------------------------------------------------")  # 60個


# dataframe.py
import pandas as pd

columns = ["姓名", "班級"]
data = [
    ["林大和", "一年甲班"],
    ["張小明", "一年乙班"],
    ["林美麗", "一年乙班"],
    ["鄭中林", "二年甲班"],
    ["林品朋", "二年甲班"],
    ["陳明朋", "二年乙班"],
]
df = pd.DataFrame(data, columns=columns)
# print(df)

df1 = df[df["班級"] == "二年甲班"]
# print(df1)
df2 = df[df["姓名"].str.contains("林")]
# print(df2)
df3 = df[(df["姓名"].str.contains("林")) & (df["班級"].str.contains("一年"))]
print(df3)


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
