# 新進測試04

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


print(
    "matplotlib 05 ------------------------------------------------------------"
)  # 60個

import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

filename = "C:/_git/vcs/_1.data/______test_files1/picture1.jpg"

img = Image.open(filename)
brightness = ImageEnhance.Brightness(img)  # 調整亮度
contrast = ImageEnhance.Contrast(img)  # 調整對比
color = ImageEnhance.Color(img)  # 調整飽和度
sharpness = ImageEnhance.Sharpness(img)  # 調整銳利度

output_b5 = brightness.enhance(5)  # 提高亮度
output_b05 = brightness.enhance(0.5)  # 降低亮度
output_c5 = contrast.enhance(5)  # 提高對比
output_c05 = contrast.enhance(0.5)  # 降低對比
output_color5 = color.enhance(5)  # 提高飽和度
output_color01 = color.enhance(0.1)  # 降低飽和度
output_s15 = sharpness.enhance(15)  # 提高銳利度
output_s0 = sharpness.enhance(0)  # 降低銳利度

plt.figure(figsize=(15, 10))  # 改變圖表尺寸
plt.subplot(241)  # 建立 4x2 子圖表的上方從左數來第一個圖表
plt.imshow(output_b5)
plt.title("brightness:5")
plt.subplot(242)  # 建立 4x2 子圖表的上方從左數來第二個圖表
plt.imshow(output_b05)
plt.title("brightness:0.5")
plt.subplot(243)  # 建立 4x2 子圖表的上方從左數來第三個圖表
plt.imshow(output_c5)
plt.title("contrast:5")
plt.subplot(244)  # 建立 4x2 子圖表的上方從左數來第四個圖表
plt.imshow(output_c05)
plt.title("contrast:0.5")
plt.subplot(245)  # 建立 4x2 子圖表的下方從左數來第一個圖表
plt.imshow(output_color5)
plt.title("color:5")
plt.subplot(246)  # 建立 4x2 子圖表的下方從左數來第二個圖表
plt.imshow(output_color01)
plt.title("color:0.1")
plt.subplot(247)  # 建立 4x2 子圖表的下方從左數來第三個圖表
plt.imshow(output_s15)
plt.title("sharpness:15")
plt.subplot(248)  # 建立 4x2 子圖表的下方從左數來第四個圖表
plt.imshow(output_s0)
plt.title("sharpness:0")

plt.show()


print(
    "matplotlib 06 ------------------------------------------------------------"
)  # 60個

import matplotlib.pyplot as plt
import numpy as np
import wave

fig, ax = plt.subplots()  # 建立單一圖表


# 建立繪製聲波的函式
def visualize(path):
    raw = wave.open(path)  # 開啟聲音
    signal = raw.readframes(-1)  # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()  # 取得 framerate
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))  # 根據聲音採樣產生成對應的時間

    ax.plot(time, signal)  # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")  # 圖表標題
    plt.xlabel("Time")  # 橫軸標題
    plt.show()


wave_filename = "C:/_git/vcs/_1.data/______test_files1/_wav/hello.wav"
visualize(wave_filename)  # 讀取聲音

print(
    "matplotlib 07 ------------------------------------------------------------"
)  # 60個

""" fail
import matplotlib.pyplot as plt
import numpy as np
import wave
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

""" fail
import pyaudio
import wave
from concurrent.futures import ThreadPoolExecutor
import numpy as np
import matplotlib.pyplot as plt

chunk = 1024  # 記錄聲音的樣本區塊大小
sample_format = (
    pyaudio.paInt16
)  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2  # 聲道數量
fs = 44100  # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
filename = "oxxostudio.wav"  # 錄音檔名

p = pyaudio.PyAudio()  # 建立 pyaudio 物件

# 開啟錄音串流
stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)
frames = []  # 建立聲音串列
run = True  # 設定開始錄音

fig, ax = plt.subplots()  # 建立單一圖表


# 定義錄音的函式
def record():
    global run, stream, p, frames, wf
    print("錄音開始...")
    while run:
        data = stream.read(chunk)
        frames.append(data)  # 將聲音記錄到串列中
    stream.stop_stream()  # 停止錄音
    stream.close()  # 關閉串流
    p.terminate()
    print("錄音結束...")
    wf = wave.open(filename, "wb")  # 開啟聲音記錄檔
    wf.setnchannels(channels)  # 設定聲道
    wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
    wf.setframerate(fs)  # 設定取樣頻率
    wf.writeframes(b"".join(frames))  # 存檔
    wf.close()
    visualize(filename)  # 執行畫圖函式


# 定義鍵盤按鍵函式
def keyin():
    global run
    if input() == "a":
        run = False  # 如果按下 a，就上 run 等於 False


# 定義繪製圖表函式
def visualize(path):
    print("畫圖...")
    raw = wave.open(path)  # 開啟聲音
    signal = raw.readframes(-1)  # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()  # 取得 framerate
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))  # 根據聲音採樣產生成對應的時間

    ax.plot(time, signal)  # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")  # 圖表標題
    plt.xlabel("Time")  # 橫軸標題
    plt.show()


executor = ThreadPoolExecutor()  # 平行任務處理
e2 = executor.submit(keyin)
e1 = executor.submit(record)
executor.shutdown()
"""

print(
    "matplotlib 09 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 10 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 11 ------------------------------------------------------------"
)  # 60個


print(
    "matplotlib 12 ------------------------------------------------------------"
)  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
