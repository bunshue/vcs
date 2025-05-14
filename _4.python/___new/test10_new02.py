"""

"""

print("------------------------------------------------------------")  # 60個

# 共同
import os
import sys
import time
import math
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # 海生, 自動把圖畫得比較好看

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小


def show():
    plt.show()
    pass


print("------------------------------------------------------------")  # 60個
'''
N = 100
index = np.arange(N)
bar_width = 0.8
figsize = (8, 8)

woe_fig = plt.figure(figsize=figsize)

plt.title("Number of Observations and WoE per bucket")
ax = woe_fig.add_subplot(111)
ax.set_ylabel("Observations")
# plt.xticks(index + bar_width / 2, self.bins["labels"])
# plt.bar(index, self.bins["obs"], bar_width, color="b", label="Observations")
ax2 = ax.twinx()
ax2.set_ylabel("Weight of Evidence")
ax2.plot(
    index + bar_width / 2,
    # self.bins["woe"],
    "bo-",
    linewidth=4.0,
    color="r",
    label="WoE",
)
handles1, labels1 = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
handles = handles1 + handles2
labels = labels1 + labels2
plt.legend(handles, labels)
woe_fig.autofmt_xdate()

show()
'''
print("------------------------------------------------------------")  # 60個

import pyttsx3

engine = pyttsx3.init()
test_txt=input("Enter the text you want to hear")
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)                                                     #you can change the rate here
for voice in voices:
    print(voice)
    engine.setProperty('voice',voice.id)
    engine.say(test_txt)       
    engine.runAndWait()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
