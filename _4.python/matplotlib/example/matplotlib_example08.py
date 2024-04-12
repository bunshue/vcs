"""
matplotlib 範例

"""

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

#折線圖
def lineChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.plot(x, s, marker='.')

#長條圖
def barChart(s,x):
    plt.xlabel('城市名稱')
    plt.ylabel('民調原分比')
    plt.title('各種城市喜好度比較')
    plt.bar(x, s)

#橫條圖
def barhChart(s,x):
    plt.barh(x, s)

#圓餅圖
def pieChart(s,x):	 
    plt.pie(s,labels=x, autopct='%.2f%%')

#要繪圖的數據
x = ['第一季', '第二季', '第三季', '第四季']
s = [13.2, 20.1, 11.9, 14.2]

#定義子圖
plt.figure(1, figsize=(8, 6),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(2,2,1)
pieChart(s,x)

x = ['程式設計概論', '多媒體概論', '計算機概論', '網路概論']
s = [3560, 4000, 4356, 1800]
plt.subplot(2,2,2)
barhChart(s,x)

x = ['新北市', '台北市', '高雄市', '台南市','桃園市','台中市']
s = [0.2, 0.3, 0.15, 0.23,0.19, 0.27]
plt.subplot(223)
lineChart(s,x)

plt.subplot(224)
barChart(s,x)

plt.show()

print('------------------------------------------------------------')	#60個

#橫條圖
def diagram_1(s,x):
	plt.barh(x, s)

#圓餅圖
def diagram_2(s,x):	 
	plt.pie(s,labels=x, autopct='%.2f%%')
#折線圖+長條圖

def diagram_4(s,x):
    plt.plot(x, s, marker='.')
    plt.bar(x, s, alpha=0.5)	

#長條圖
def diagram_3(s,x):
	plt.bar(x, s)	

#要繪圖的數據
x = ['高雄','台中','宜蘭','花蓮']
s = [89,58,63,50]

#設定子圖
plt.figure(1, figsize=(8, 8),clear=True)
plt.subplots_adjust(left=0.1, right=0.95)

plt.subplot(221)
diagram_1(s,x)

plt.subplot(222)
diagram_2(s,x)

plt.subplot(223)
diagram_3(s,x)

plt.subplot(2,2,4)
diagram_4(s,x)

plt.show()


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個

