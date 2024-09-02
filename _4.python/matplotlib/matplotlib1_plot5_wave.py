"""
畫 wave

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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

print("使用wavfile模組")
from scipy.io import wavfile

wave_filename = "_data/notify1.wav"
sample_rate, data = wavfile.read(wave_filename)  # 讀取.wav文件

# 繪製聲波圖
plt.figure(figsize=(10, 6))

plt.plot(data)
plt.title("聲波圖")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.show()

print("------------------------------------------------------------")  # 60個

print("使用wave模組")
import wave

wave_filename = "C:/_git/vcs/_1.data/______test_files1/_wav/hello.wav"
wave_filename = "_data/notify1.wav"

# 繪製聲波
raw = wave.open(wave_filename)  # 開啟聲音
signal = raw.readframes(-1)  # 讀取全部聲音採樣
signal = np.frombuffer(signal, dtype="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
f_rate = raw.getframerate()  # 取得 framerate
time = np.linspace(0, len(signal) / f_rate, num=len(signal))  # 根據聲音採樣產生成對應的時間

plt.figure(figsize=(10, 6))

plt.plot(time, signal)  # 畫線，橫軸時間，縱軸陣列值
plt.title("Sound Wave")  # 圖表標題
plt.xlabel("Time")  # 橫軸標題

plt.show()

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
