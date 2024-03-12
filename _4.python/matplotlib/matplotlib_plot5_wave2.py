# plot 集合 5 畫 wave

import sys
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示

print("------------------------------------------------------------")  # 60個

import wave

# 定義繪製圖表函式
def visualize(path):
    print("畫圖...")
    fig, ax = plt.subplots()  # 建立單一圖表
    
    raw = wave.open(path)  # 開啟聲音
    signal = raw.readframes(-1)  # 讀取全部聲音採樣
    signal = np.frombuffer(signal, dtype="int16")  # 將聲音採樣轉換成 int16 的格式所組成的 np 陣列
    f_rate = raw.getframerate()  # 取得 framerate
    time = np.linspace(0, len(signal) / f_rate, num=len(signal))  # 根據聲音採樣產生成對應的時間

    ax.plot(time, signal)  # 畫線，橫軸時間，縱軸陣列值
    plt.title("Sound Wave")  # 圖表標題
    plt.xlabel("Time")  # 橫軸標題
    plt.show()

filename = '_data/notify1.wav'
visualize(filename)  # 執行畫圖函式

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
