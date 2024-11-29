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

font_filename = "C:/_git/vcs/_1.data/______test_files1/_font/msch.ttf"
# 設定中文字型及負號正確顯示
# 設定中文字型檔
plt.rcParams["font.sans-serif"] = "Microsoft JhengHei"  # 將字體換成 Microsoft JhengHei
# 設定負號
plt.rcParams["axes.unicode_minus"] = False  # 讓負號可正常顯示
plt.rcParams["font.size"] = 12  # 設定字型大小

print("------------------------------------------------------------")  # 60個

import scipy
import pylab as pl

print("------------------------------------------------------------")  # 60個

print("np.fft 01")

np.set_printoptions(precision=3, linewidth=120, suppress=False)

# 頻域訊號處理
# FFT

X = np.random.rand(8)
X = np.arange(10)
# X = np.ones(8)

X_FFT = np.fft.fft(X)

X_FFT_IFFT = np.fft.ifft(X_FFT)

print("X :", X)
print("X_FFT = fft(X) :", X_FFT)
print("DC =", X_FFT[0].real)

print("X_FFT_IFFT = ifft(X_FFT) :", X_FFT_IFFT)

plt.scatter(X, X, c="g", s=200, label="原資料")
plt.scatter(X_FFT.real, X_FFT.imag, c="r", s=200, label="FFT")
plt.legend()
plt.grid()
plt.show()

X = np.ones(8)
np.fft.fft(X) / len(X)  # 為了計算各個成分的能量，需要將FFT的結果除以FFT的長度

# array([ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j])

X = np.arange(0, 2 * np.pi, 2 * np.pi / 8)
Y = np.sin(X)
tmp = np.fft.fft(Y) / len(Y)
print(np.array_str(tmp, suppress_small=True))

# [ 0.+0.j  -0.-0.5j  0.-0.j   0.-0.j   0.+0.j   0.-0.j   0.+0.j   0.+0.5j]

tmp = np.fft.fft(np.cos(X)) / len(X)
print(np.array_str(tmp, suppress_small=True))

# [-0.0+0.j  0.5-0.j  0.0+0.j  0.0+0.j  0.0+0.j -0.0+0.j  0.0+0.j  0.5-0.j]

tmp = np.fft.fft(2 * np.sin(2 * X)) / len(X)
print(np.array_str(tmp, suppress_small=True))
tmp = np.fft.fft(0.8 * np.cos(2 * X)) / len(X)
print(np.array_str(tmp, suppress_small=True))

"""
[ 0.+0.j  0.+0.j -0.-1.j  0.-0.j  0.+0.j  0.+0.j -0.+1.j  0.-0.j]
[-0.0+0.j -0.0+0.j  0.4-0.j  0.0-0.j  0.0+0.j  0.0-0.j  0.4+0.j -0.0+0.j]
"""
X = np.arange(0, 2 * np.pi, 2 * np.pi / 128)
Y = 0.3 * np.cos(X) + 0.5 * np.cos(2 * X + np.pi / 4) + 0.8 * np.cos(3 * X - np.pi / 3)
Y_FFT = np.fft.fft(Y) / len(Y)
print(np.array_str(Y_FFT[:4], suppress_small=True))
print(np.abs(Y_FFT[1]), np.rad2deg(np.angle(Y_FFT[1])))  # 周期為128取樣點的余弦波的振幅和相位
print(np.abs(Y_FFT[2]), np.rad2deg(np.angle(Y_FFT[2])))  # 周期為64取樣點的余弦波的振幅和相位
print(np.abs(Y_FFT[3]), np.rad2deg(np.angle(Y_FFT[3])))  # 周期為42.667取樣點的余弦波的振幅和相位

"""
[ 0.000+0.j     0.150+0.j     0.177+0.177j  0.200-0.346j]
0.15 2.48480834489e-15
0.25 45.0
0.4 -60.0
"""
X1 = np.random.random(4096)
X2 = np.random.random(4093)

# %timeit np.fft.fft(X1)
# %timeit np.fft.fft(X2)

# 10000 loops, best of 3: 183 μs per loop
# 10 loops, best of 3: 69.6 ms per loop

print("------------------------------------------------------------")  # 60個

print("np.fft 02 合成時域訊號")


# 三角波的頻譜（上）、使用頻譜中的部分頻率重建的三角波（下）
def triangle_wave(size):  # ❶
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, x, 0)
    y = np.where(x >= 0.5, 1 - x, y)
    return x, y


# 取FFT計算的結果bins中的前n項進行合成，傳回合成結果，計算loops個周期的波形
def fft_combine(bins, n, loops=1):  # ❷
    length = len(bins) * loops
    data = np.zeros(length)
    index = loops * np.arange(0, length, 1.0) / length * (2 * np.pi)
    for k, p in enumerate(bins[:n]):
        if k != 0:
            p *= 2  # 除去直流成分之外，其余的系數都*2
        data += np.real(p) * np.cos(k * index)  # 余弦成分的系數為實數部
        data -= np.imag(p) * np.sin(k * index)  # 正弦成分的系數為負的虛數部
    return index, data


fft_size = 256

# 計算三角波和其FFT
x, y = triangle_wave(fft_size)
fy = np.fft.fft(y) / fft_size

# 繪制三角波的FFT的前20項的振幅，由於不含索引為偶數的值均為0， 因此取
# log之後無窮小，無法繪圖，用np.clip函數設定陣列值的上下限，確保繪圖正確
fig, axes = pl.subplots(2, 1, figsize=(8, 6))
axes[0].plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
axes[0].set_xlabel("頻率視窗(frequency bin)")
axes[0].set_ylabel("幅值(dB)")

# 繪制原始的三角波和用正弦波逐級合成的結果，使用取樣點為x軸座標
axes[1].plot(y, label="原始三角波", linewidth=2)
for i in [0, 1, 3, 5, 7, 9]:
    index, data = fft_combine(fy, i + 1, 2)  # 計算兩個周期的合成波形
    axes[1].plot(data, label="N=%s" % i, alpha=0.6)
axes[1].legend(loc="best")

plt.show()

print("------------------------------------------------------------")  # 60個

print("np.fft 03")


# 方波的頻譜、合成方波在跳變處出現抖動
def square_wave(size):
    x = np.arange(0, 1, 1.0 / size)
    y = np.where(x < 0.5, 1.0, 0)
    return x, y


x, y = square_wave(fft_size)
fy = np.fft.fft(y) / fft_size

fig, axes = pl.subplots(2, 1, figsize=(8, 6))
axes[0].plot(np.clip(20 * np.log10(np.abs(fy[:20])), -120, 120), "o")
axes[0].set_xlabel("頻率視窗(frequency bin)")
axes[0].set_ylabel("幅值(dB)")
axes[1].plot(y, label="原始方波", linewidth=2)
for i in [0, 1, 3, 5, 7, 9]:
    index, data = fft_combine(fy, i + 1, 2)  # 計算兩個周期的合成波形
    axes[1].plot(data, label="N=%s" % i)
axes[1].legend(loc="best")

plt.show()

"""
scpy2.examples.fft_demo：使用該程式可以交談式地觀察各種三角波和方波的頻譜以及其正弦合成的近似波形
"""
print("------------------------------------------------------------")  # 60個

print("np.fft 04 觀察訊號的頻譜")


def show_fft(x):
    XS = x[:fft_size]
    xf = np.fft.rfft(XS) / fft_size  # ❹
    freqs = np.linspace(0, sampling_rate / 2, fft_size // 2 + 1)  # ❺
    xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))  # ❻
    pl.figure(figsize=(8, 4))
    pl.subplot(211)
    pl.plot(T[:fft_size], XS)
    pl.xlabel("時間(秒)")
    pl.subplot(212)
    pl.plot(freqs, xfp)
    pl.xlabel("頻率(Hz)")
    pl.subplots_adjust(hspace=0.4)
    print(xfp[[10, 15]])


# 156.25Hz和234.375Hz的波形（上）和頻譜（下）
sampling_rate, fft_size = 8000, 512  # ❶
T = np.arange(0, 1.0, 1.0 / sampling_rate)  # ❷
X = np.sin(2 * np.pi * 156.25 * T) + 2 * np.sin(2 * np.pi * 234.375 * T)  # ❸

show_fft(X)
plt.show()

# [ -6.021e+00  -9.643e-16]

freqs = np.fft.fftfreq(fft_size, 1.0 / sampling_rate)
for i in [
    0,
    1,
    fft_size // 2 - 1,
    fft_size // 2,
    fft_size // 2 + 1,
    fft_size - 2,
    fft_size - 1,
]:
    print(i, "\t", freqs[i])


# 非完整周期（200Hz和300Hz）的正弦波經由FFT變換之後出現頻譜洩漏
X = np.sin(2 * np.pi * 200 * T) + 2 * np.sin(2 * np.pi * 300 * T)

show_fft(X)
plt.show()

print("------------------------------------------------------------")  # 60個

print("np.fft 05")

# 50Hz正弦波的512點FFT所計算的頻譜的實際波形
pl.figure(figsize=(6, 2))
T = np.arange(0, 1.0, 1.0 / 8000)
X = np.sin(2 * np.pi * 50 * T)[:512]
pl.plot(np.hstack([X, X, X]))

plt.show()

print("------------------------------------------------------------")  # 60個

print("np.fft 06")

"""
解決 : AttributeError: module 'scipy.signal' has no attribute 'hann'

pip install numpy==1.23.4
pip install scipy==1.12.0
pip install librosa(==0.10.1)
"""

# Hann窗函數

pl.figure(figsize=(6, 2))
pl.plot(scipy.signal.windows.hann(512))
plt.show()

print(scipy.signal.windows.hann(8))
print(scipy.signal.windows.hann(8, sym=0))

# 加Hann窗的50Hz正弦波的512點FFT所計算的實際波形
pl.figure(figsize=(6, 2))
T = np.arange(0, 1.0, 1.0 / 8000)
X = np.sin(2 * np.pi * 50 * T)[:512] * scipy.signal.windows.hann(512, sym=0)
pl.plot(np.hstack([X, X, X]))

plt.show()

print("------------------------------")  # 30個

# 加Hann窗前後的頻譜，Hann窗能降低頻譜洩漏

sampling_rate, fft_size = 8000, 512  # ❶
T = np.arange(0, 1.0, 1.0 / sampling_rate)
X = np.sin(2 * np.pi * 200 * T) + 2 * np.sin(2 * np.pi * 300 * T)

XS = X[:fft_size]
YS = XS * scipy.signal.windows.hann(fft_size, sym=0)

xf = np.fft.rfft(XS) / fft_size
yf = np.fft.rfft(YS) / fft_size

freqs = np.linspace(0, sampling_rate // 2, fft_size // 2 + 1)

xfp = 20 * np.log10(np.clip(np.abs(xf), 1e-20, 1e100))
yfp = 20 * np.log10(np.clip(np.abs(yf), 1e-20, 1e100))
pl.figure(figsize=(8, 4))
pl.plot(freqs, xfp, label="矩形窗")
pl.plot(freqs, yfp, label="hann窗")
pl.legend()
pl.xlabel("頻率(Hz)")

a = pl.axes([0.4, 0.2, 0.4, 0.4])
a.plot(freqs, xfp, label="矩形窗")
a.plot(freqs, yfp, label="hann窗")
a.set_xlim(100, 400)
a.set_ylim(-40, 0)

plt.show()

cc = np.mean(scipy.signal.windows.hann(512, sym=0))
print(cc)

print("------------------------------------------------------------")  # 60個

print("np.fft 07 頻譜平均")


def average_fft(x, fft_size):
    n = len(x) // fft_size * fft_size
    tmp = x[:n].reshape(-1, fft_size)  # ❶
    tmp *= scipy.signal.windows.hann(fft_size, sym=0)  # ❷
    xf = np.abs(np.fft.rfft(tmp) / fft_size)  # ❸
    avgf = np.mean(xf, axis=0)
    return 20 * np.log10(avgf)


# 白色噪聲的頻譜接近水平直線（注意Y軸的範圍）
x = np.random.randn(100000)
xf = average_fft(x, 512)
pl.figure(figsize=(7, 3.5))
pl.plot(xf)
pl.xlabel("頻率視窗(Frequency Bin)")
pl.ylabel("幅值(dB)")
pl.xlim([0, 257])
pl.subplots_adjust(bottom=0.15)

plt.show()

print("------------------------------------------------------------")  # 60個

print("np.fft 08 經由低通濾波器的白噪聲的頻譜")

B, A = scipy.signal.iirdesign(1000 / 4000.0, 1100 / 4000.0, 1, 40, 0, "cheby1")
X = np.random.randn(100000)
Y = scipy.signal.filtfilt(B, A, X)
Y_FFT = average_fft(Y, 512)
pl.figure(figsize=(7, 3.5))
pl.plot(Y_FFT)
pl.xlabel("頻率視窗(Frequency Bin)")
pl.ylabel("幅值(dB)")
pl.xlim(0, 257)
pl.subplots_adjust(bottom=0.15)

plt.show()

print("------------------------------------------------------------")  # 60個

print("np.fft 09 譜圖, 頻率掃描波的譜圖")

sampling_rate = 8000.0
fft_size = 1024
step = fft_size / 16
time = 2

t = np.arange(0, time, 1 / sampling_rate)
sweep = scipy.signal.chirp(
    t, f0=100, t1=time, f1=0.8 * sampling_rate / 2, method="logarithmic"
)

# NGpl.specgram(sweep, fft_size, sampling_rate, noverlap = 1024-step)
pl.xlabel("時間(秒)")
pl.ylabel("頻率(Hz)")

plt.show()

"""
scpy2.examples.spectrogram_realtime：實時觀察音效訊號譜圖的示範程式，
使用TraitsUI、PyAudio等庫實現
"""
print("------------------------------------------------------------")  # 60個

# %hide
# %exec_python -m scpy2.examples.spectrogram_realtime

print("np.fft 10 精確測量訊號頻率")


def make_wave(amp, freq, phase, tend, rate):
    period = 1.0 / rate
    t = np.arange(0, tend, period)
    x = np.zeros_like(t)
    for a, f, p in zip(amp, freq, phase):
        x += a * np.sin(2 * np.pi * f * t + p)
    return t, x


RATE = 8000
t, x = make_wave([1, 2, 0.5], [44, 150, 330], [1, 1.4, 1.8], 0.3, RATE)
x += np.random.randn(len(x))

FFT_SIZE = 1024
spect1 = np.fft.rfft(x[:FFT_SIZE] * np.hanning(FFT_SIZE))
freqs = np.fft.fftfreq(FFT_SIZE, 1.0 / RATE)

bin_width = freqs[1] - freqs[0]

amp_spect1 = np.abs(spect1)
(loc,) = scipy.signal.argrelmax(amp_spect1, order=3)  # ❶
mask = amp_spect1[loc] > amp_spect1.mean() * 3  # ❷
loc = loc[mask]
peak_freqs = freqs[loc]
print("bin width:", bin_width)
print("Peak Frequencies:", peak_freqs)

# bin width: 7.8125
# Peak Frequencies: [  46.875  148.438  328.125]

COUNT = FFT_SIZE // 4
dt = COUNT / 8000.0

spect2 = np.fft.rfft(x[COUNT : COUNT + FFT_SIZE] * np.hanning(FFT_SIZE))

phase1 = np.angle(spect1[loc])
phase2 = np.angle(spect2[loc])

phase_delta = phase2 - phase1
print(phase_delta)

# [ 2.595 -1.29  -2.899]

max_n = (peak_freqs.max() + 3 * bin_width) * dt  # ❶
n = np.arange(max_n)

possible_freqs = (phase_delta + 2 * np.pi * n[:, None]) / (2 * np.pi * dt)  # ❷

idx = np.argmin(np.abs(peak_freqs - possible_freqs), axis=0)  # ❸
peak_freqs2 = possible_freqs[idx, np.arange(len(peak_freqs))]
print("Peak Frequencies:", peak_freqs2)

# Peak Frequencies: [  44.155  149.833  329.33 ]

print("------------------------------------------------------------")  # 60個

print("np.fft 11")

# 卷冊積運算
# 快速卷冊積


def fft_convolve(a, b):
    n = len(a) + len(b) - 1
    N = 2 ** (int(np.log2(n)) + 1)  # ❶
    A = np.fft.fft(a, N)  # ❷
    B = np.fft.fft(b, N)
    return np.fft.ifft(A * B)[:n]  # ❸


a = np.random.rand(128)
b = np.random.rand(128)
c = np.convolve(a, b)
np.allclose(c, fft_convolve(a, b))

# True

a = np.random.rand(10000)
b = np.random.rand(10000)
print(np.allclose(np.convolve(a, b), fft_convolve(a, b)))

# %timeit np.convolve(a, b)
# %timeit fft_convolve(a, b)

# True
# 10 loops, best of 3: 36.5 ms per loop
# 100 loops, best of 3: 6.43 ms per loop

# 比較直接卷冊積和FFT卷冊積的運算速度  skip 速度
for n in range(4, 14):
    N = 2**n
    a = np.random.rand(N)
    b = np.random.rand(N)
    np.convolve(a, b)
    fft_convolve(a, b)

print("fft SP")

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()

print("------------------------------------------------------------")  # 60個
