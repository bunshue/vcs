"""
# plot 集合
step

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

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.plot(x, y, "o--", color="grey", alpha=0.4)
plt.step(x, y)

plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.plot(x, y, "o--", color="grey", alpha=0.4)
plt.step(x, y, "g", where="pre")

plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.plot(x, y, "o--", color="grey", alpha=0.4)
plt.step(x, y, "g", where="post")
plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.plot(x, y, "o--", color="grey", alpha=0.4)
plt.step(x, y, "g", where="mid")
plt.show()

print("------------------------------------------------------------")  # 60個

x = [1, 3, 5, 7, 9]
y = [1, 9, 25, 49, 81]
plt.bar(x, y, color="yellow")
plt.step(x, y, "*-", where="pre", color="g")
plt.xticks(np.arange(0, 10, step=1))

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(14)
y = np.sin(x / 3)
fig, ax = plt.subplots()
ax.set_title("step() - pre,post,mid參數的使用")
# 繪製階梯圖
ax.step(x, y + 2, where="pre")
ax.step(x, y + 1, where="mid")
ax.step(x, y, where="post")
# 繪製直線圖
ax.plot(x, y + 2, "D--", color="m", alpha=0.3)
ax.plot(x, y + 1, "D--", color="m", alpha=0.3)
ax.plot(x, y, "D--", color="m", alpha=0.3)
labels = ["pre", "mid", "post"]
ax.legend(title="參數 where", labels=labels)

plt.show()

print("------------------------------------------------------------")  # 60個

x = np.arange(14)
y = np.sin(x / 3)
fig, ax = plt.subplots()
ax.set_title("plot() - drawstyle參數的使用")
# 繪製階梯圖
ax.plot(x, y + 2, drawstyle="steps")
ax.plot(x, y + 1, drawstyle="steps-mid")
ax.plot(x, y, drawstyle="steps-post")
# 繪製直線圖
ax.plot(x, y + 2, "D--", color="m", alpha=0.3)
ax.plot(x, y + 1, "D--", color="m", alpha=0.3)
ax.plot(x, y, "D--", color="m", alpha=0.3)
labels = ["steps", "steps-mid", "steps-post"]
ax.legend(title="參數 drawstyle", labels=labels)

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
