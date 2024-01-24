import sys

print("------------------------------------------------------------")  # 60個

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4))
print("x= ", str(x2).rjust(4))
print("x= ", str(x3).rjust(4))
print("x= ", str(x4).rjust(4))

print("------------------------------------------------------------")  # 60個

import time, sys

x1 = 1
x2 = 11
x3 = 111
x4 = 1111
print("x= ", str(x1).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x2).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x3).rjust(4), end="\r", flush=True)
time.sleep(1)
print("x= ", str(x4).rjust(4), end="\r", flush=True)

print("------------------------------------------------------------")  # 60個

# ch25_1.py
from twilio.rest import Client

# 你從twilio.com申請的帳號
accountSid='AC6fdc3efffd15cabcdee8b361e9d4e67'
# 你從twilio.com獲得的圖騰
authToken='9a6dfab51a342a480e7cf9c1f88d3e638'

client = Client(accountSid, authToken)
message = client.messages.create (
            from_ = "+12512548607",         # 這是twilio.com給你的號碼
            to = "+886952000000",           # 這是收簡訊方的號碼
            body = "Python王者歸來" )       # 發送的訊息


print("------------------------------------------------------------")  # 60個
from deep_translator import GoogleTranslator

# 要翻譯的文本
text = '早安'

# 翻譯成英文
translator = GoogleTranslator(source='auto', target='en')
translation_en = translator.translate(text)
print("英文:", translation_en)

# 翻譯成日文, 另一種寫法
translation_ja = GoogleTranslator(source='auto', target='ja').translate(text)
print("日文:", translation_ja)

# 翻譯成韓文
translation_ko = GoogleTranslator(source='auto', target='ko').translate(text)
print("韓文:", translation_ko)

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Waveform of nofity.wav file')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()


sys.exit()

print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

mywav = r'C:Windows\Media\notify.wav'
# 讀取.wav文件
wav_audio = AudioSegment.from_wav(mywav)

# 轉換為.mp3
wav_audio.export("notify.mp3", format="mp3")

print("------------------------------------------------------------")  # 60個

import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_7.wav"

with sr.Microphone() as source:
    print("請說英文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio)  
        print("你說的英文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")

print("------------------------------------------------------------")  # 60個

import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "out33_8.wav"

with sr.Microphone() as source:
    print("請說中文 ...")
    audio = r.listen(source)

    # 將聲音保存為 WAV 檔案
    with open(audio_file_path, "wb") as file:
        file.write(audio.get_wav_data())

    try:
        # 使用Google的語音識別API
        text = r.recognize_google(audio, language="zh-TW")  
        print("你說的中文是 : {}".format(text))
    except:
        print("抱歉無法聽懂你的語音")

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_7.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('Good Morning聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()

print("------------------------------------------------------------")  # 60個

import matplotlib.pyplot as plt
from scipy.io import wavfile

mywav = 'out33_8.wav'
# 讀取.wav文件
sample_rate, data = wavfile.read(mywav)

# 繪製聲波圖
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False
plt.figure(figsize=(10, 4))
plt.plot(data)
plt.title('早安 聲波圖')
plt.ylabel('Amplitude')
plt.xlabel('Sample')
plt.show()

print("------------------------------------------------------------")  # 60個







print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


import yfinance as yf

apple = yf.Ticker("AAPL")                           # 建立Apple物件
print("Apple公司財務報表")
financials = apple.financials                       # 獲取財務報表
print(financials)
quarterly_financials = apple.quarterly_financials   # 獲取季度財務報表
print(quarterly_financials)

tsmc = yf.Ticker("2330.TW")                         # 建立Apple物件
print("台積電財務報表")
financials = tsmc.financials                        # 獲取財務報表
print(financials)
quarterly_financials = tsmc.quarterly_financials    # 獲取季度財務報表
print(quarterly_financials)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_2.py

# ch32_2.py
import yfinance as yf

def fetch_apple_stock_price():
    # 獲取Apple股票資料
    apple = yf.Ticker("AAPL")
    
    # 獲取即時股價
    apple_stock_info = apple.history(period="1d")
    
    # 輸出股價
    print("Apple公司的股價(目前或最近交易日) : ")
    print("開盤價：", apple_stock_info['Open'].iloc[0])
    print("收盤價：", apple_stock_info['Close'].iloc[0])
    print("最高價：", apple_stock_info['High'].iloc[0])
    print("最低價：", apple_stock_info['Low'].iloc[0])
    print("交易量：", apple_stock_info['Volume'].iloc[0])

fetch_apple_stock_price()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_3.py

# ch32_3.py
import yfinance as yf
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載蘋果公司最近三個月的股價數據
apple = yf.Ticker("AAPL")
data = apple.history(period="3mo")

# 計算5天和20天移動平均線
data['MA5'] = data['Close'].rolling(window=5).mean()
data['MA20'] = data['Close'].rolling(window=20).mean()

# 繪製股價和移動平均線
plt.figure(figsize=(10,6))
plt.plot(data['Close'], label='AAPL Close', color='blue')
plt.plot(data['MA5'], label='5-Day MA', color='green')
plt.plot(data['MA20'], label='20-Day MA', color='red')

# 標題和圖例
plt.title('Apple公司股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()

# 顯示圖表
plt.show()



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\ch32\ch32_4.py

# ch32_4.py
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載台積電最近三個月的股價數據
tsmc = yf.Ticker("2330.TW")                 
data = tsmc.history(period='1y')

# 計算5日和20日的簡單移動平均
data['SMA5'] = data['Close'].rolling(window=5).mean()
data['SMA20'] = data['Close'].rolling(window=20).mean()

# 繪製收盤價和移動平均線
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Close Price', alpha=0.5)
plt.plot(data['SMA5'], label='5-Day SMA', alpha=0.8)
plt.plot(data['SMA20'], label='20-Day SMA', alpha=0.8)
plt.title('台積電股價 5 日和 20 日移動平均線')
plt.xlabel('日期')
plt.ylabel('價格')
plt.legend()
plt.grid(True)
plt.show()

# 移動平均生成交易信號
# 買入信號: 5日均線從下方突破20日均線
# 賣出信號: 5日均線從上方跌破20日均線
data['Signal'] = 0.0
data.iloc[5:, data.columns.get_loc('Signal')] =\
    np.where(data['SMA5'].iloc[5:] > data['SMA20'].iloc[5:], 1.0, 0.0)
data['Signal_change'] = data['Signal'].diff()

# 找出買入和賣出的日期
buy_dates = data[data['Signal_change'] == 1].index
sell_dates = data[data['Signal_change'] == -1].index

print(f"買入日期: {buy_dates.tolist()}")
print(f"賣出日期: {sell_dates.tolist()}")

print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個










from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
print("下載中   ... ")
yt.streams[0].download()
print("下載完成 ... ")

print("------------------------------------------------------------")  # 60個

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
videoViews = yt.views
print(f"影片觀賞次數 : {videoViews}")
videoSeconds = yt.length
print(f"影片長度(秒) : {videoSeconds}")
videoRating = yt.rating
print(f"影片評價     : {videoRating}")
videoTitle = yt.title
print(f"影片標題     : {videoTitle}\n下載中 ... ")
yt.streams[0].download()
print("下載完成 ... ")

print("------------------------------------------------------------")  # 60個

from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):         # 如果不存在則建立此資料夾
    os.mkdir(path)

yt = YouTube("https://www.youtube.com/watch?v=dhzsf5QXmns")
videoViews = yt.views
print(f"影片觀賞次數 : {videoViews}")
videoSeconds = yt.length
print(f"影片長度(秒) : {videoSeconds}")
videoRating = yt.rating
print(f"影片評價     : {videoRating}")
videoTitle = yt.title
print(f"影片標題     : {videoTitle}\n下載中 ... ")
yt.streams[0].download(path)        # 所下載影音檔案儲存在path
print("下載完成 ... ")

print("------------------------------------------------------------")  # 60個

from pytube import YouTube
import os

path = r"d:\myYouTube"
if not os.path.isdir(path):             # 如果不存在則建立此資料夾
    os.mkdir(path)

links = ["https://www.youtube.com/watch?v=dhzsf5QXmns",
         "https://www.youtube.com/watch?v=z8eE3CGyQiE"]
for video in links:
    yt = YouTube(video)
    videoViews = yt.views
    print(f"影片觀賞次數 : {videoViews}")
    videoSeconds = yt.length
    print(f"影片長度(秒) : {videoSeconds}")
    videoRating = yt.rating
    print(f"影片評價     : {videoRating}")
    videoTitle = yt.title
    print(f"影片標題     : {videoTitle}\n下載中 ... ")
    print(f"影片格式數量 : {len(yt.streams)}")
    yt.streams[0].download(path)        # 所下載影音檔案儲存在path
    print("下載完成 ... ")

print("------------------------------------------------------------")  # 60個

import threading 
import os  
from pytube import YouTube  

def download_video(url):
    try:
        yt = YouTube(url)                       # 建立 YouTube 物件
        yt.streams[0].download(download_path)   # 選擇第1個並下載
        print(f"下載完成 : {url}")              # 輸出下載完成的訊息
    except Exception as e:
        print(f"錯誤下載 {url}: {str(e)}")      # 如果錯誤, 輸出錯誤訊息

# 下載影片的 URL 列表
urls = [
    "https://www.youtube.com/watch?v=dhzsf5QXmns",
    "https://www.youtube.com/watch?v=z8eE3CGyQiE",
    "https://www.youtube.com/watch?v=GLlsu31FBt8",
    "https://www.youtube.com/watch?v=VMCk7fh9SGw",
    "https://www.youtube.com/watch?v=_32sspKCF8Y",
]

# 定義當前目錄下的 out36_5 資料夾作為下載路徑
download_path = os.path.join(os.getcwd(), 'out36_5')

# 檢查該資料夾是否存在，如果不存在則建立
if not os.path.exists(download_path):
    os.makedirs(download_path)

threads = []                                    # 建立一個空串列儲存執行緒

# 為每個 URL 建立一個新的執行緒
for url in urls:
    thread = threading.Thread(target=download_video, args=(url,))
    threads.append(thread)                      # 將執行緒添加到串列中
    thread.start()                              # 開始執行緒的執行

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("所有影片下載完成")                       

print("------------------------------------------------------------")  # 60個

from tkinter import *
from pytube import YouTube

def loadVideo():                    # 列印下載資訊
    vlinks = "https//www.youtube.com/watch?v="
    vlinks = vlinks + links.get()   # 影音檔案網址
    yt = YouTube(vlinks)
    yt.streams[0].download()
    x.set("影音檔案下載完成 ...")
          
window = Tk()
window.title("ch35_6")              # 視窗標題

x = StringVar()
x.set("請輸入影音檔案序列碼")
links = StringVar()

lab1 = Label(window,text="輸入影音檔案序列碼 : ").grid(row=0)
lab2 = Label(window,text="請輸入儲存的資料夾 : ").grid(row=1)
lab3 = Label(window,textvariable=x,
             height=3).grid(row=2,column=0,columnspan=2)
             
e1 = Entry(window,textvariable=links)   # 文字方塊1
e2 = Entry(window)                      # 文字方塊2
e1.grid(row=0,column=1)                 # 定位文字方塊1
e2.grid(row=1,column=1)                 # 定位文字方塊2

btn1 = Button(window,text="下載",command=loadVideo)
btn1.grid(row=3,column=0)
btn2 = Button(window,text="結束",command=window.destroy)
btn2.grid(row=3,column=1)

window.mainloop()


