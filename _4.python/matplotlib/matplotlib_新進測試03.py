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

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10)  # 建立含10個元素的陣列
ypt1 = xpt / xpt  # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)  # 時間複雜度是 O(logn)
ypt3 = xpt  # 時間複雜度是 O(n)
plt.plot(xpt, ypt1, "-o", label="O(1)")
plt.plot(xpt, ypt2, "-o", label="O(logn)")
plt.plot(xpt, ypt3, "-o", label="O(n)")
plt.legend(loc="best")  # 建立圖例
plt.show()


print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
import numpy as np

xpt = np.linspace(1, 10, 10)  # 建立含10個元素的陣列
ypt1 = xpt / xpt  # 時間複雜度是 O(1)
ypt2 = np.log2(xpt)  # 時間複雜度是 O(logn)
ypt3 = xpt  # 時間複雜度是 O(n)
ypt4 = xpt * np.log2(xpt)  # 時間複雜度是 O(nlogn)
ypt5 = xpt * xpt  # 時間複雜度是 O(n*n)
plt.plot(xpt, ypt1, "-o", label="O(1)")
plt.plot(xpt, ypt2, "-o", label="O(logn)")
plt.plot(xpt, ypt3, "-o", label="O(n)")
plt.plot(xpt, ypt4, "-o", label="O(nlogn)")
plt.plot(xpt, ypt5, "-o", label="O(n*n)")
plt.legend(loc="best")  # 建立圖例
plt.show()



print("------------------------------------------------------------")  # 60個


import numpy as np
import matplotlib.pyplot as plt


def kmeans(x, y, cx, cy):
    """目前功能只是繪群集元素點"""
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心
    plt.show()


# 群集中心, 元素的數量, 數據最大範圍
cluster_number = 3  # 群集中心數量
seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)


print("------------------------------------------------------------")  # 60個


import numpy as np
import matplotlib.pyplot as plt


def length(x1, y1, x2, y2):
    """計算2點之間的距離"""
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    """對元素執行分群"""
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 為每個點找群集
        distance = INF  # 設定最初距離
        for j in range(cluster_number):  # 計算每個點與群集中心的距離
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此點加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    """建立群集和繪製各群集點和線條"""
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心

    c = ["r", "g", "y"]  # 群集的線條顏色
    for index, node in enumerate(clusters):  # 為每個群集中心建立線條
        linex = []  # 線條的 x 座標
        liney = []  # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])  # 建立線條x座標串列
            liney.append([n[1], cy[index]])  # 建立線條y座標串列
        color_c = c[index]  # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 為第i群集繪線條
    plt.show()


# 群集中心, 元素的數量, 數據最大範圍
INF = 999  # 假設最大距離
cluster_number = 3  # 群集中心數量
seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

kmeans(x, y, cluster_x, cluster_y)


print("------------------------------------------------------------")  # 60個

import numpy as np
import matplotlib.pyplot as plt


def length(x1, y1, x2, y2):
    """計算2點之間的距離"""
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    """對元素執行分群"""
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 為每個點找群集
        distance = INF  # 設定最初距離
        for j in range(cluster_number):  # 計算每個點與群集中心的距離
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此點加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    """建立群集和繪製各群集點和線條"""
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心

    c = ["r", "g", "y"]  # 群集的線條顏色
    for index, node in enumerate(clusters):  # 為每個群集中心建立線條
        linex = []  # 線條的 x 座標
        liney = []  # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])  # 建立線條x座標串列
            liney.append([n[1], cy[index]])  # 建立線條y座標串列
        color_c = c[index]  # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 為第i群集繪線條
    plt.show()
    return clusters


def get_new_cluster(clusters):
    """計算各群集中心的點"""
    new_x = []  # 新群集中心 x 座標
    new_y = []  # 新群集中心 y 座標
    for index, node in enumerate(clusters):  # 逐步計算各群集
        nx, ny = 0, 0
        for n in node:
            nx += n[0]
            ny += n[1]
        new_x.append([])
        new_x[index] = int(nx / len(node))  # 計算群集中心 x 座標
        new_y.append([])
        new_y[index] = int(ny / len(node))  # 計算群集中心 y 座標
    return new_x, new_y


# 群集中心, 元素的數量, 數據最大範圍
INF = 999  # 假設最大距離
cluster_number = 3  # 群集中心數量
seeds = 50  # 元素數量
limits = 100  # 值在(100, 100)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

clusters = kmeans(x, y, cluster_x, cluster_y)

while True:  # 收斂迴圈
    new_x, new_y = get_new_cluster(clusters)
    x_list = list(cluster_x)  # 將np.array轉成串列
    y_list = list(cluster_y)  # 將np.array轉成串列
    if new_x == x_list and new_y == y_list:  # 如果相同代表收斂完成
        break
    else:
        cluster_x = new_x  # 否則重新收斂
        cluster_y = new_y
        clusters = kmeans(x, y, cluster_x, cluster_y)


print("------------------------------------------------------------")  # 60個

import numpy as np
import matplotlib.pyplot as plt


def length(x1, y1, x2, y2):
    """計算2點之間的距離"""
    return int(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5)


def clustering(x, y, cx, cy):
    """對元素執行分群"""
    clusters = []
    for i in range(cluster_number):  # 建立群集
        clusters.append([])
    for i in range(seeds):  # 為每個點找群集
        distance = INF  # 設定最初距離
        for j in range(cluster_number):  # 計算每個點與群集中心的距離
            dist = length(x[i], y[i], cx[j], cy[j])
            if dist < distance:
                distance = dist
                cluster_index = j  # 分群的索引
        clusters[cluster_index].append([x[i], y[i]])  # 此點加入此索引的群集
    return clusters


def kmeans(x, y, cx, cy):
    """建立群集和繪製各群集點和線條"""
    clusters = clustering(x, y, cx, cy)
    plt.scatter(x, y, color="b")  # 繪製元素點
    plt.scatter(cx, cy, color="r")  # 用紅色繪群集中心

    c = ["r", "g", "y"]  # 群集的線條顏色
    for index, node in enumerate(clusters):  # 為每個群集中心建立線條
        linex = []  # 線條的 x 座標
        liney = []  # 線條的 y 座標
        for n in node:
            linex.append([n[0], cx[index]])  # 建立線條x座標串列
            liney.append([n[1], cy[index]])  # 建立線條y座標串列
        color_c = c[index]  # 選擇顏色
        for i in range(len(linex)):
            plt.plot(linex[i], liney[i], color=color_c)  # 為第i群集繪線條
    plt.show()
    return clusters


def get_new_cluster(clusters):
    """計算各群集中心的點"""
    new_x = []  # 新群集中心 x 座標
    new_y = []  # 新群集中心 y 座標
    for index, node in enumerate(clusters):  # 逐步計算各群集
        nx, ny = 0, 0
        for n in node:
            nx += n[0]
            ny += n[1]
        new_x.append([])
        new_x[index] = int(nx / len(node))  # 計算群集中心 x 座標
        new_y.append([])
        new_y[index] = int(ny / len(node))  # 計算群集中心 y 座標
    return new_x, new_y


# 群集中心, 元素的數量, 數據最大範圍
INF = 999  # 假設最大距離
cluster_number = 3  # 群集中心數量
seeds = 100  # 元素數量
limits = 500  # 值在(300, 300)內
# 使用隨機數建立seeds數量的種子元素
x = np.random.randint(0, limits, seeds)
y = np.random.randint(0, limits, seeds)
# 使用隨機數建立cluster_number數量的群集中心
cluster_x = np.random.randint(0, limits, cluster_number)
cluster_y = np.random.randint(0, limits, cluster_number)

clusters = kmeans(x, y, cluster_x, cluster_y)

while True:  # 收斂迴圈
    new_x, new_y = get_new_cluster(clusters)
    x_list = list(cluster_x)  # 將np.array轉成串列
    y_list = list(cluster_y)  # 將np.array轉成串列
    if new_x == x_list and new_y == y_list:  # 如果相同代表收斂完成
        break
    else:
        cluster_x = new_x  # 否則重新收斂
        cluster_y = new_y
        clusters = kmeans(x, y, cluster_x, cluster_y)


print("------------------------------------------------------------")  # 60個


import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # Colab 換路徑使用，本機或 Jupyter 環境可以刪除

import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

img = Image.open("oxxostudio.jpg")
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




print("------------------------------------------------------------")  # 60個

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


visualize("oxxostudio.wav")  # 讀取聲音



print("------------------------------------------------------------")  # 60個


import os

os.chdir("/content/drive/MyDrive/Colab Notebooks")  # 使用 Colab 要換路徑使用，本機環境可以刪除

import matplotlib.pyplot as plt
import numpy as np
import wave
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")  # 轉換並儲存為 wav

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


visualize("oxxostudio.wav")


print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



