"""

Python 聲音處理 pyaudio

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

import pyaudio
import wave

chunk = 1024  # 記錄聲音的樣本區塊大小
sample_format = (
    pyaudio.paInt16
)  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 2  # 聲道數量
fs = 44100  # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5  # 錄音秒數
filename = "tmp_audio01.wav"  # 錄音檔名

p = pyaudio.PyAudio()  # 建立 pyaudio 物件

print("開始錄音...")

# 開啟錄音串流
stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []  # 建立聲音串列

for i in range(0, int(fs / chunk * seconds)):
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

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import pyaudio
import wave
from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

chunk = 1024
sample_format = pyaudio.paInt16
channels = 2
fs = 44100
seconds = 5
filename = "tmp_audio02.wav"

p = pyaudio.PyAudio()

print("開始錄音...")

stream = p.open(
    format=sample_format,
    channels=channels,
    rate=fs,
    frames_per_buffer=chunk,
    input=True,
)

frames = []

for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print("錄音結束...")

wf = wave.open(filename, "wb")
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b"".join(frames))
wf.close()

song = AudioSegment.from_mp3("song.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_wav("tmp_audio03.wav")  # 讀取錄音 wav 檔案
output = voice.overlay(song, loop=True)  # 混合錄音和背景音樂
play(output)  # 播放聲音
output.export("tmp_output.mp3")  # 輸出為 mp3
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import numpy as np

samplerate = 44100  # 取樣頻率


def get_wave(freq, duration=0.5):
    amplitude = 4096  # 震幅 ( 音量大小 )
    t = np.linspace(
        0, duration, int(samplerate * duration)
    )  # 使用等差級數，在指定時間長度裡，根據取樣頻率建立區間
    wave = amplitude * np.sin(2 * np.pi * freq * t)  # 在每個區間裡放入指定頻率的波形
    return wave


def get_piano_notes():
    octave = ["C", "c", "D", "d", "E", "F", "f", "G", "g", "A", "a", "B"]  # 建立音符英文字對照表
    base_freq = 261.63  # 預設為 C4 的頻率
    note_freqs = {
        octave[i]: base_freq * pow(2, (i / 12)) for i in range(len(octave))
    }  # 產生頻率和英文字的對照
    note_freqs[""] = 0.0  # 如果是空值則為 0 ( 無聲音 )
    return note_freqs


def get_song_data(music_notes):
    note_freqs = get_piano_notes()  # 取的英文與音符對照表
    song = [
        get_wave(note_freqs[note]) for note in music_notes.split("-")
    ]  # 根據音樂的音符，對應到對照表產生指定串列
    song = np.concatenate(song)  # 連接為新陣列
    return song


# 音樂的音符表
music_notes = "C-C-G-G-A-A-G--F-F-E-E-D-D-C--G-G-F-F-E-E-D--G-G-F-F-E-E-D--C-C-G-G-A-A-G--F-F-E-E-D-D-C"
data = get_song_data(music_notes)  # 轉換成頻率對照表
data = data * (16300 / np.max(data))  # 調整震幅 ( 音量大小 )

from scipy.io.wavfile import write

write("twinkle-twinkle.wav", samplerate, data.astype(np.int16))  # 寫入檔案

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
{
    A0: {frequency: "27.50", wavelength: "1254.55"},
    A1: {frequency: "55.00", wavelength: "627.27"},
    A2: {frequency: "110.00", wavelength: "313.64"},
    A3: {frequency: "220.00", wavelength: "156.82"},
    A4: {frequency: "440.00", wavelength: "78.41"},
    A5: {frequency: "880.00", wavelength: "39.20"},
    A6: {frequency: "1760.00", wavelength: "19.60"},
    A7: {frequency: "3520.00", wavelength: "9.80"},
    A8: {frequency: "7040.00", wavelength: "4.90"},
    B0: {frequency: "30.87", wavelength: "1117.67"},
    B1: {frequency: "61.74", wavelength: "558.84"},
    B2: {frequency: "123.47", wavelength: "279.42"},
    B3: {frequency: "246.94", wavelength: "139.71"},
    B4: {frequency: "493.88", wavelength: "69.85"},
    B5: {frequency: "987.77", wavelength: "34.93"},
    B6: {frequency: "1975.53", wavelength: "17.46"},
    B7: {frequency: "3951.07", wavelength: "8.73"},
    B8: {frequency: "7902.13", wavelength: "4.37"},
    C0: {frequency: "16.35", wavelength: "2109.89"},
    C1: {frequency: "32.70", wavelength: "1054.94"},
    C2: {frequency: "65.41", wavelength: "527.47"},
    C3: {frequency: "130.81", wavelength: "263.74"},
    C4: {frequency: "261.63", wavelength: "131.87"},
    C5: {frequency: "523.25", wavelength: "65.93"},
    C6: {frequency: "1046.50", wavelength: "32.97"},
    C7: {frequency: "2093.00", wavelength: "16.48"},
    C8: {frequency: "4186.01", wavelength: "8.24"},
    D0: {frequency: "18.35", wavelength: "1879.69"},
    D1: {frequency: "36.71", wavelength: "939.85"},
    D2: {frequency: "73.42", wavelength: "469.92"},
    D3: {frequency: "146.83", wavelength: "234.96"},
    D4: {frequency: "293.66", wavelength: "117.48"},
    D5: {frequency: "587.33", wavelength: "58.74"},
    D6: {frequency: "1174.66", wavelength: "29.37"},
    D7: {frequency: "2349.32", wavelength: "14.69"},
    D8: {frequency: "4698.63", wavelength: "7.34"},
    E0: {frequency: "20.60", wavelength: "1674.62"},
    E1: {frequency: "41.20", wavelength: "837.31"},
    E2: {frequency: "82.41", wavelength: "418.65"},
    E3: {frequency: "164.81", wavelength: "209.33"},
    E4: {frequency: "329.63", wavelength: "104.66"},
    E5: {frequency: "659.25", wavelength: "52.33"},
    E6: {frequency: "1318.51", wavelength: "26.17"},
    E7: {frequency: "2637.02", wavelength: "13.08"},
    E8: {frequency: "5274.04", wavelength: "6.54"},
    F0: {frequency: "21.83", wavelength: "1580.63"},
    F1: {frequency: "43.65", wavelength: "790.31"},
    F2: {frequency: "87.31", wavelength: "395.16"},
    F3: {frequency: "174.61", wavelength: "197.58"},
    F4: {frequency: "349.23", wavelength: "98.79"},
    F5: {frequency: "698.46", wavelength: "49.39"},
    F6: {frequency: "1396.91", wavelength: "24.70"},
    F7: {frequency: "2793.83", wavelength: "12.35"},
    F8: {frequency: "5587.65", wavelength: "6.17"},
    G0: {frequency: "24.50", wavelength: "1408.18"},
    G1: {frequency: "49.00", wavelength: "704.09"},
    G2: {frequency: "98.00", wavelength: "352.04"},
    G3: {frequency: "196.00", wavelength: "176.02"},
    G4: {frequency: "392.00", wavelength: "88.01"},
    G5: {frequency: "783.99", wavelength: "44.01"},
    G6: {frequency: "1567.98", wavelength: "22.00"},
    G7: {frequency: "3135.96", wavelength: "11.00"},
    G8: {frequency: "6271.93", wavelength: "5.50"},
    "A#0": {frequency: "29.14", wavelength: "1184.13"},
    "Bb0": {frequency: "29.14", wavelength: "1184.13"},
    "A#1": {frequency: "58.27", wavelength: "592.07"},
    "Bb1": {frequency: "58.27", wavelength: "592.07"},
    "A#2": {frequency: "116.54", wavelength: "296.03"},
    "Bb2": {frequency: "116.54", wavelength: "296.03"},
    "A#3": {frequency: "233.08", wavelength: "148.02"},
    "Bb3": {frequency: "233.08", wavelength: "148.02"},
    "A#4": {frequency: "466.16", wavelength: "74.01"},
    "Bb4": {frequency: "466.16", wavelength: "74.01"},
    "A#5": {frequency: "932.33", wavelength: "37.00"},
    "Bb5": {frequency: "932.33", wavelength: "37.00"},
    "A#6": {frequency: "1864.66", wavelength: "18.50"},
    "Bb6": {frequency: "1864.66", wavelength: "18.50"},
    "A#7": {frequency: "3729.31", wavelength: "9.25"},
    "Bb7": {frequency: "3729.31", wavelength: "9.25"},
    "A#8": {frequency: "7458.62", wavelength: "4.63"},
    "Bb8": {frequency: "7458.62", wavelength: "4.63"},
    "C#0": {frequency: "17.32", wavelength: "1991.47"},
    "Db0": {frequency: "17.32", wavelength: "1991.47"},
    "C#1": {frequency: "34.65", wavelength: "995.73"},
    "Db1": {frequency: "34.65", wavelength: "995.73"},
    "C#2": {frequency: "69.30", wavelength: "497.87"},
    "Db2": {frequency: "69.30", wavelength: "497.87"},
    "C#3": {frequency: "138.59", wavelength: "248.93"},
    "Db3": {frequency: "138.59", wavelength: "248.93"},
    "C#4": {frequency: "277.18", wavelength: "124.47"},
    "Db4": {frequency: "277.18", wavelength: "124.47"},
    "C#5": {frequency: "554.37", wavelength: "62.23"},
    "Db5": {frequency: "554.37", wavelength: "62.23"},
    "C#6": {frequency: "1108.73", wavelength: "31.12"},
    "Db6": {frequency: "1108.73", wavelength: "31.12"},
    "C#7": {frequency: "2217.46", wavelength: "15.56"},
    "Db7": {frequency: "2217.46", wavelength: "15.56"},
    "C#8": {frequency: "4434.92", wavelength: "7.78"},
    "Db8": {frequency: "4434.92", wavelength: "7.78"},
    "D#0": {frequency: "19.45", wavelength: "1774.20"},
    "Eb0": {frequency: "19.45", wavelength: "1774.20"},
    "D#1": {frequency: "38.89", wavelength: "887.10"},
    "Eb1": {frequency: "38.89", wavelength: "887.10"},
    "D#2": {frequency: "77.78", wavelength: "443.55"},
    "Eb2": {frequency: "77.78", wavelength: "443.55"},
    "D#3": {frequency: "155.56", wavelength: "221.77"},
    "Eb3": {frequency: "155.56", wavelength: "221.77"},
    "D#4": {frequency: "311.13", wavelength: "110.89"},
    "Eb4": {frequency: "311.13", wavelength: "110.89"},
    "D#5": {frequency: "622.25", wavelength: "55.44"},
    "Eb5": {frequency: "622.25", wavelength: "55.44"},
    "D#6": {frequency: "1244.51", wavelength: "27.72"},
    "Eb6": {frequency: "1244.51", wavelength: "27.72"},
    "D#7": {frequency: "2489.02", wavelength: "13.86"},
    "Eb7": {frequency: "2489.02", wavelength: "13.86"},
    "D#8": {frequency: "4978.03", wavelength: "6.93"},
    "Eb8": {frequency: "4978.03", wavelength: "6.93"},
    "F#0": {frequency: "23.12", wavelength: "1491.91"},
    "Gb0": {frequency: "23.12", wavelength: "1491.91"},
    "F#1": {frequency: "46.25", wavelength: "745.96"},
    "Gb1": {frequency: "46.25", wavelength: "745.96"},
    "F#2": {frequency: "92.50", wavelength: "372.98"},
    "Gb2": {frequency: "92.50", wavelength: "372.98"},
    "F#3": {frequency: "185.00", wavelength: "186.49"},
    "Gb3": {frequency: "185.00", wavelength: "186.49"},
    "F#4": {frequency: "369.99", wavelength: "93.24"},
    "Gb4": {frequency: "369.99", wavelength: "93.24"},
    "F#5": {frequency: "739.99", wavelength: "46.62"},
    "Gb5": {frequency: "739.99", wavelength: "46.62"},
    "F#6": {frequency: "1479.98", wavelength: "23.31"},
    "Gb6": {frequency: "1479.98", wavelength: "23.31"},
    "F#7": {frequency: "2959.96", wavelength: "11.66"},
    "Gb7": {frequency: "2959.96", wavelength: "11.66"},
    "F#8": {frequency: "5919.91", wavelength: "5.83"},
    "Gb8": {frequency: "5919.91", wavelength: "5.83"},
    "G#0": {frequency: "25.96", wavelength: "1329.14"},
    "Ab0": {frequency: "25.96", wavelength: "1329.14"},
    "G#1": {frequency: "51.91", wavelength: "664.57"},
    "Ab1": {frequency: "51.91", wavelength: "664.57"},
    "G#2": {frequency: "103.83", wavelength: "332.29"},
    "Ab2": {frequency: "103.83", wavelength: "332.29"},
    "G#3": {frequency: "207.65", wavelength: "166.14"},
    "Ab3": {frequency: "207.65", wavelength: "166.14"},
    "G#4": {frequency: "415.30", wavelength: "83.07"},
    "Ab4": {frequency: "415.30", wavelength: "83.07"},
    "G#5": {frequency: "830.61", wavelength: "41.54"},
    "Ab5": {frequency: "830.61", wavelength: "41.54"},
    "G#6": {frequency: "1661.22", wavelength: "20.77"},
    "Ab6": {frequency: "1661.22", wavelength: "20.77"},
    "G#7": {frequency: "3322.44", wavelength: "10.38"},
    "Ab7": {frequency: "3322.44", wavelength: "10.38"},
    "G#8": {frequency: "6644.88", wavelength: "5.19"},
    "Ab8": {frequency: "6644.88", wavelength: "5.19"},
}
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("錄音程式, 從麥克風收音")

import pyaudio
import wave

CHUNK = 1024  # 每个缓冲区的帧数
FORMAT = pyaudio.paInt16  # 采样位数
CHANNELS = 1  # 单声道
RATE = 44100  # 采样频率


def record_audio(wave_out_path, record_second):
    """录音功能"""
    p = pyaudio.PyAudio()  # 实例化对象
    stream = p.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )  # 打开流，传入响应参数
    wf = wave.open(wave_out_path, "wb")  # 打开 wav 文件。
    wf.setnchannels(CHANNELS)  # 声道设置
    wf.setsampwidth(p.get_sample_size(FORMAT))  # 采样位数设置
    wf.setframerate(RATE)  # 采样频率设置

    for _ in range(0, int(RATE * record_second / CHUNK)):
        data = stream.read(CHUNK)
        wf.writeframes(data)  # 写入数据
    stream.stop_stream()  # 关闭流
    stream.close()
    p.terminate()
    wf.close()


"""
wave_out_path = "ccccc10.wav"
record_second = 10
record_audio(wave_out_path, record_second)
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
import pyaudio
import sys, wave, threading, random
import time

chunk = 1024                     # 記錄聲音的樣本區塊大小
sample_format = pyaudio.paInt16  # 樣本格式，可使用 paFloat32、paInt32、paInt24、paInt16、paInt8、paUInt8、paCustomFormat
channels = 1                     # 聲道數量
fs = 44100                       # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
seconds = 5                      # 錄音秒數

p = pyaudio.PyAudio()   # 建立 pyaudio 物件
stream = p.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
frames = []
cnt = 0
while True:
    data = stream.read(chunk)
    frames.append(data)          # 將聲音記錄到串列中
    cnt += 1
    print(cnt)
    if cnt > 10:
        break
    time.sleep(1)
    
    
print('停止錄音')
stream.stop_stream()             # 停止錄音
stream.close()                   # 關閉串流
p.terminate()

wf = wave.open(f'cccccddddaaa10.wav', 'wb')   # 開啟聲音記錄檔
wf.setnchannels(channels)             # 設定聲道
wf.setsampwidth(p.get_sample_size(sample_format))  # 設定格式
wf.setframerate(fs)                   # 設定取樣頻率
wf.writeframes(b''.join(frames))      # 存檔
wf.close()

"""
print("------------------------------------------------------------")  # 60個
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
channels = 1  # 聲道數量
fs = 44100  # 取樣頻率，常見值為 44100 ( CD )、48000 ( DVD )、22050、24000、12000 和 11025。
filename = "tmp_audio04.wav"  # 錄音檔名

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
    # visualize(filename)  # 執行畫圖函式


# 定義鍵盤按鍵函式
def keyin():
    global run
    if input() == "a":
        run = False  # 如果按下 a，就上 run 等於 False


executor = ThreadPoolExecutor()  # 平行任務處理
e2 = executor.submit(keyin)
e1 = executor.submit(record)
executor.shutdown()


print("------------------------------------------------------------")  # 60個
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
