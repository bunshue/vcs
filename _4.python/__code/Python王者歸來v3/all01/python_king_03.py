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




print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_19.py

# ch13_19.py
import random                               # 導入模組random

lotterys = random.sample(range(1,50), 7)    # 7組號碼
specialNum = lotterys.pop()                 # 特別號

print("第xxx期大樂透號碼 ", end="")
for lottery in sorted(lotterys):            # 排序列印大樂透號碼
    print(lottery, end=" ")
print(f"\n特別號:{specialNum}")             # 列印特別號














print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_20.py

# ch13_20.py
import random
random.seed(5)
for i in range(5):
    print(random.random())
    






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_21.py

# ch13_21.py
import random                       # 導入模組random
import time                         # 導入模組time

min, max = 1, 10
ans = random.randint(min, max)      # 隨機數產生答案
yourNum = int(input("請猜1-10之間數字: "))
starttime = int(time.time())        # 起始秒數
while True:    
    if yourNum == ans:
        print("恭喜!答對了")
        endtime = int(time.time())  # 結束秒數
        print("所花時間: ", endtime - starttime, " 秒")
        break
    elif yourNum < ans:
        print("請猜大一些")
    else:
        print("請猜小一些")
    yourNum = int(input("請猜1-10之間數字: "))
        



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_22.py

# ch13_22.py
import time                         # 導入模組time

xtime = time.localtime()
print(xtime)                        # 列出目前系統時間
print("年 ", xtime[0])
print("年 ", xtime.tm_year)         # 物件設定方式顯示
print("月 ", xtime[1])
print("日 ", xtime[2])
print("時 ", xtime[3])
print("分 ", xtime[4])
print("秒 ", xtime[5])
print("星期幾   ", xtime[6])
print("第幾天   ", xtime[7])
print("夏令時間 ", xtime[8])





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_23.py

# ch13_23.py
import time
x = 1000000
pi = 0
time.process_time()
for i in range(1,x+1):
    pi += 4*((-1)**(i+1) / (2*i-1))
    if i != 1 and i % 100000 == 0:      # 隔100000執行一次
        e_time = time.process_time()
        print(f"當 {i=:7d} 時 PI={pi:8.7f}, 所花時間={e_time}")


  













          



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_23_1.py

# ch13_23_1.py
import time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(formatted_time)


print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_24.py

# ch13_24.py
import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline()
print(msg)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_25.py

# ch13_25.py
import sys
print("請輸入字串, 輸入完按Enter = ", end = "")
msg = sys.stdin.readline(8)         # 讀8個字
print(msg)






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_26.py

# ch13_26.py
import sys

sys.stdout.write("I like Python")






print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_27.py

# ch13_27.py
import sys
for dirpath in sys.path:
    print(dirpath)













print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_28.py

# ch13_28.py
import sys
print("命令列參數 : ", sys.argv)




print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_29.py

# ch13_29.py
import keyword

keywordLists = ['as', 'while', 'break', 'sse', 'Python']
for x in keywordLists:
    print(f"{x:>8s} {keyword.iskeyword(x)}")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_30.py

# ch13_30.py
import sys
from pprint import pprint
print("使用print")
print(sys.path)
print("使用pprint")
pprint(sys.path)















print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_31.py

# ch13_31.py
import random                       # 導入模組random
money = 300                         # 賭金總額
bet = 100                           # 賭注
min, max = 1, 100                   # 隨機數最小與最大值設定
winPercent = int(input("請輸入莊家贏的比率(0-100)之間 :"))

while True:
    print(f"歡迎光臨 : 目前籌碼金額 {money} 美金 ")
    print(f"每次賭注 {bet} 美金 ")
    print("猜大小遊戲: L或l表示大,  S或s表示小, Q或q則程式結束")
    customerNum = input("= ")       # 讀取玩家輸入
    if customerNum == 'Q' or customerNum == 'q':    # 若輸入Q或q
        break                                       # 程式結束
    num = random.randint(min, max)  # 產生是否讓玩家答對的隨機數
    if num > winPercent:            # 隨機數在此區間回應玩家猜對
        print("恭喜!答對了\n")
        money += bet                # 賭金總額增加
    else:                           # 隨機數在此區間回應玩家猜錯
        print("答錯了!請再試一次\n")
        money -= bet                # 賭金總額減少
    if money <= 0:
        break

print("歡迎下次再來")





print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_32.py

# ch13_32.py
import random

trials = 1000000
Hits = 0
for i in range(trials):
    x = random.random() * 2 - 1     # x軸座標
    y = random.random() * 2 - 1     # y軸座標
    if x * x + y * y <= 1:          # 判斷是否在圓內
        Hits += 1
PI = 4 * Hits / trials

print("PI = ", PI)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_33.py

# ch13_33.py
import string

def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
subText = abc[-3:] + abc[:-3]           # 加密字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_34.py

# ch13_34.py
import string
import random
def encrypt(text, encryDict):           # 加密文件
    cipher = []
    for i in text:                      # 執行每個字元加密
        v = encryDict[i]                # 加密
        cipher.append(v)                # 加密結果
    return ''.join(cipher)              # 將串列轉成字串
    
abc = string.printable[:-5]             # 取消不可列印字元
newAbc = abc[:]                         # 產生新字串拷貝
abclist = list(newAbc)                  # 轉成串列
random.shuffle(abclist)                 # 打亂串列順序
subText = ''.join(abclist)              # 轉成字串
encry_dict = dict(zip(subText, abc))    # 建立字典
print("列印編碼字典\n", encry_dict)     # 列印字典

msg = 'If the implementation is easy to explain, it may be a good idea.'
ciphertext = encrypt(msg, encry_dict)

print("原始字串 ", msg)
print("加密字串 ", ciphertext)









print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_35.py

# ch13_35.py
import random

# 假設一家公司想要測試兩種不同的廣告設計, 以看哪一種效果更好
ad_designs = ['Design A', 'Design B']

# 公司有一個1000人的郵件列表, 想要隨機選擇一半接收A廣告, 一半接收B廣告
recipients = {'Design A': [], 'Design B': []}

# 隨機分配郵件
for i in range(1, 1001):
    chosen_design = random.choice(ad_designs)       # 隨機選擇一種設計
    recipients[chosen_design].append(f'user_{i}')

# 確保每種設計都有500個用戶
while len(recipients['Design A']) != 500:
    if len(recipients['Design A']) > 500:
        user_to_move = recipients['Design A'].pop()
        recipients['Design B'].append(user_to_move)
    else:
        user_to_move = recipients['Design B'].pop()
        recipients['Design A'].append(user_to_move)

# 假設這裡會發送郵件，然後根據用戶反饋進行分析

# 輸出每種設計的接收者數量，確保它們是平均分配的
print(f"A 廣告接收者數量 : {len(recipients['Design A'])}")
print(f"B 廣告接收者數量 : {len(recipients['Design B'])}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_36.py

# ch13_36.py
import random

# 假設有一組伺服器
servers = ['Server1', 'Server2', 'Server3', 'Server4']

# 模擬1000次請求, 隨機分配到這些伺服器
requests = {server:0 for server in servers}
for _ in range(1000):
    selected_server = random.choice(servers)
    requests[selected_server] += 1

print(requests)         # 顯示每個伺服器獲得的請求數



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_37.py

# ch13_37.py
import random

# 假設生產線上有一批產品序列號
product_serials = list(range(1000, 2000))

# 抽檢10個產品進行品質檢查
samples = random.sample(product_serials, 10)

for serial in samples:
    # 這裡會有一個品質檢查的函數
    print(f"檢查序列號 : {serial}")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_38.py

# ch13_38.py
import time

def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"{timestamp} : {event}")

# 假設發生了一個事件
log_event("User login")



print("------------------------------------------------------------")  # 60個

#檔案 : C:\_git\vcs\_4.python\__code\Python王者歸來v3\all02\ch13_39.py

# ch13_39.py
import time

def database_backup():
    # 執行備份邏輯
    print("資料庫備份 ... ")

# 每天凌晨1點執行備份
while True:
    current_time = time.strftime("%H:%M", time.localtime())
    if current_time == "01:00":
        database_backup()
    time.sleep(60)              # 每分鐘檢查一次



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



