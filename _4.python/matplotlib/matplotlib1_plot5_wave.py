# plot 集合 5 畫 wave

import matplotlib

import wave
from scipy.io import wavfile

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

mywav = "_data/notify1.wav"
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Waveform of nofity.wav file")
plt.ylabel("Amplitude")
plt.xlabel("Sample")
plt.show()

print("------------------------------------------------------------")  # 60個

mywav = "_data/notify1.wav"
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("Good Morning聲波圖")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.show()

print("------------------------------------------------------------")  # 60個

mywav = "_data/notify1.wav"
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title("早安 聲波圖")
plt.ylabel("Amplitude")
plt.xlabel("Sample")

plt.show()

print("------------------------------------------------------------")  # 60個


# 建立繪製聲波的函式
def visualize(path):
    print("畫圖...")
    raw = wave.open(path)  # 開啟聲音
    signal = raw.readframes(-1)  # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()  # 取得 framerate
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))  # 根據聲音採樣產生成對應的時間

    plt.plot(time, signal)  # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")  # 圖表標題
    plt.xlabel("Time")  # 橫軸標題
    plt.show()


wave_filename = "C:/_git/vcs/_1.data/______test_files1/_wav/hello.wav"
wave_filename = "_data/notify1.wav"
visualize(wave_filename)  # 讀取聲音

print(
    "matplotlib 07 ------------------------------------------------------------"
)  # 60個

""" fail
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

mp3_filename = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
song = AudioSegment.from_mp3(mp3_filename)  # 讀取 mp3 檔案
song.export("aaaa.wav", format="wav")  # 轉換並儲存為 wav

fig, ax = plt.subplots()


def visualize(path):
    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = np.frombuffer(signal, dtype="int16")
    f_rate = raw.getframerate()
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))

    ax.plot(time, signal)
    plt.title("Sound Wave")
    plt.xlabel("Time")
    plt.show()


visualize("aaaa.wav")
"""

print(
    "matplotlib 08 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 09 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 10 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 11 ------------------------------------------------------------"
)  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
