"""
新進綜合

"""
import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個
# gtts ST
# gTTS：文字轉語音
# pip install gTTS
# zh-tw:正中, zh-cn:簡中, en:英文, ja:日文
print("------------------------------------------------------------")  # 60個


def text2mp3(filename, text, lang):
    from gtts import gTTS

    tts = gTTS(text=text, lang=lang)
    tts.save(filename)


# 播放mp3
def play_audio_file(filename):
    from pygame import mixer

    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():
        continue


import gtts

print("目前支援的語音種類 :")
print(gtts.lang.tts_langs())

filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"
text = "黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"
text = "LANDrop 輕鬆實現跨系統無線傳輸資料、照片的免費工具"
lang = "zh-tw"
text2mp3(filename, text, lang)
play_audio_file(filename)

time.sleep(1)  # 1秒

filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"
text = "Welcome to the United States"
lang = "en"
text2mp3(filename, text, lang)
play_audio_file(filename)

time.sleep(1)  # 1秒

filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"
text = "ありがとう"
lang = "ja"
text2mp3(filename, text, lang)
play_audio_file(filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("------------------------------------------------------------")  # 60個
# gtts SP
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

print("使用 ffmpeg.exe 將 .wav 轉成 .mp3")

wav_filename = "老北京.wav"
mp3_filename = "老北京.mp3"

# 讀取.wav文件
wav_audio = AudioSegment.from_wav(wav_filename)

# 轉換為.mp3
wav_audio.export(mp3_filename, format="mp3")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 無麥克風
import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "tmp_record1.wav"

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
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 無麥克風
import speech_recognition as sr

r = sr.Recognizer()

# 設定錄音檔案的儲存路徑
audio_file_path = "tmp_record2.wav"

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

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 很多mp3不能播放

filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"
filename = "D:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav"
filename = "D:/_git/vcs/_1.data/______test_files1/_wav/tone.wav"

import playsound

# 不能使用中文檔名
playsound.playsound(filename, block=True)

playsound.playsound(filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" TBD
#声音录制
import pyaudio
import wave

CHUNK = 1024

wav_filename = "tmp_test_wave.wav"

wf = wave.open(wav_filename, "rb")
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != "":
    print("c")
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#简洁回调函数版音频录制

#錄10秒

import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, "wb")
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)

time_count = 0
def callback(in_data, frame_count, time_info, status):
    wf.writeframes(in_data)
    if(time_count < 10):
        return (in_data, pyaudio.paContinue)
    else:
        return (in_data, pyaudio.paComplete)

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)

stream.start_stream()
print("* recording")
while stream.is_active():
    time.sleep(1)  # 1秒
    time_count += 1

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
print("* recording done!")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 久
# 製作影片字幕
# 聲音轉字幕

# 影片轉wav, 要跑很久

video_filename = "D:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

from moviepy.editor import *

audio1 = AudioFileClip("老北京.mp4")
audio1.write_audiofile("老北京22222.wav")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
!pip install pydub
!pip install SpeechRecognition
!pip install opencc-python-reimplemented
"""

from pydub import AudioSegment
from pydub.silence import detect_silence
import speech_recognition as sr
from opencc import OpenCC
import glob
import shutil
from time import sleep


def emptydir(dirname):  # 清空資料夾
    print("dirname :", dirname)
    if os.path.isdir(dirname):  # 資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  # 2秒  # 需延遲,否則會出錯
    os.mkdir(dirname)  # 建立資料夾


wave_filename = "老北京.wav"

cc = OpenCC("s2twp")
delay = 1300  # 聲音延遟時間
fname = "老北京"
sound = AudioSegment.from_file(fname + ".wav", format="wav")
start_end = detect_silence(sound, delay, sound.dBFS, 1)  # 偵測靜音

print("偵測靜音, 個數 :", len(start_end))
print("偵測靜音, 在 :", start_end)

# 每個分割區間的結束位置
mslist = []
for i in range(len(start_end)):
    if i == (len(start_end) - 1):
        data = start_end[i][1]  # 最後一筆不必減1秒
    else:
        data = start_end[i][1] - delay  # 結束位置提前1秒
    mslist.append(data)

print("每個分割區間的結束位置 :", mslist)

# 毫秒轉為xx:xx.xxx字串
timelist = []
for sss in mslist:
    h, ms = divmod(float(sss), 3600000)  # 時
    m, ms = divmod(float(ms), 60000)  # 分
    s, ms = divmod(float(ms), 1000)  # 秒
    ts = "%02d:%02d:%02d.%03d" % (h, m, s, ms)
    timelist.append(ts)

print("分割聲音檔")
emptydir("tmp_分割聲音檔")

for i in range(len(timelist)):
    if i == 0:
        start = 0
    else:
        start = mslist[i - 1]
    end = mslist[i]
    filename = "tmp_分割聲音檔/slice{:0>3d}.wav".format(i + 1)
    print("ST :", start, ", SP :", end)
    sound[start:end].export(filename, format="wav")


print("對 tmp_分割聲音檔 進行語音辨識")
r = sr.Recognizer()  # 建立語音辨識物件
file = open(fname + ".srt", "w", encoding="UTF-8")  # 儲存辨識結果

# 撈出單層wav檔
wavfiles = glob.glob("tmp_分割聲音檔/*.wav")
data = ""
count = 1
for i in range(len(wavfiles)):
    try:
        with sr.WavFile("tmp_分割聲音檔/slice{:0>3d}.wav".format(i + 1)) as source:
            audio = r.record(source)
        result = r.recognize_google(audio, language="zh-TW")  # 辨識結果
        result = cc.convert(result)  # 轉繁體中文
        print("{}. {}".format(count, result))
        # 組合SRT格式
        data += str(count) + "\n"
        if i == 0:
            start = "00:00:00,000"
        else:
            start = timelist[i - 1].replace(".", ",")
        end = timelist[i].replace(".", ",")
        data += start + " --> " + end + "\n"
        data += result + "\n\n"
        count += 1
    except sr.UnknownValueError:
        print("Google Speech Recognition 無法辨識此語音！")
    except sr.RequestError as e:
        print("無法由 Google Speech Recognition 取得結果; {0}".format(e))
file.write(data)
file.close()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
SpeechRecognition：語音轉文字(聲音檔)
pip install SpeechRecognition
"""

print("語音轉文字 wave 轉 文字")

import speech_recognition

r = speech_recognition.Recognizer()
with speech_recognition.WavFile("record1.wav") as source:  # 讀取wav檔
    audio = r.record(source)
try:
    word = r.recognize_google(audio, language="zh-TW")
    print("語音辨識OK, 內容 :")
    print(word)
except:
    print("語音辨識失敗！")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個
"""
#SpeechRecognition：語音轉文字(麥克風)
!pip install pydub
!pip install ffmpeg
"""
import speech_recognition
from pydub import AudioSegment

# from google.colab.output import eval_js
from base64 import b64decode


def record_audio(filename):
    try:
        data = eval_js("recordAudio({})")
        binary = b64decode(data)
        with open(filename, "wb") as audio_file:
            audio_file.write(binary)
    except Exception as err:
        print(str(err))


"""
#record.webm 無此檔
record_audio("record.webm")
sound = AudioSegment.from_file("tmp_record.webm")
sound.export("record.wav", format ="wav")
r = speech_recognition.Recognizer()
with speech_recognition.WavFile("record.wav") as source:
    audio = r.record(source)
try:
    word = r.recognize_google(audio, language="zh-TW")
    print("語音辨識結果：\n" + word)
except:
    print("語音辨識失敗！")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
應用：AI智慧讀報機
!pip install newspaper3k
"""

print("newspaper3k a")

import newspaper
from newspaper import Article

# paper = newspaper.build("http://cnn.com", language="en")
paper = newspaper.build("http://www.cnbc.com", language="en")
# paper = newspaper.build("http://www.bbc.co.uk", language="en")
# paper = newspaper.build("http://www.foxnews.com", language="en")

print(type(paper.articles))
print("文章數目 :", len(paper.articles))

count = 0
urls = []
for article in paper.articles:
    url = article.url
    if ".html" in url:
        print(url)
        count += 1
        if count > 5:
            break
        try:  # 有時會產生無法擷取的錯誤,故使用try
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
            if len(content) > 0:
                if len(content) > 5000:
                    content = content[:4999]
                print(content)
        except:
            print("XXXXXXXXXXX")
            pass

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

print("newspaper3k b")

import newspaper
from newspaper import Article

paper = newspaper.build("http://cnn.com", language="en")
# paper = newspaper.build("http://www.cnbc.com", language="en")
# paper = newspaper.build("http://www.bbc.co.uk", language="en")
# paper = newspaper.build("http://www.foxnews.com", language="en")

print(type(paper.articles))
print("文章數目 :", len(paper.articles))

count = 0
urls = []
for article in paper.articles:
    url = article.url
    if ".html" in url:
        print(url)
        count += 1
        if count > 5:
            break
        try:  # 有時會產生無法擷取的錯誤,故使用try
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
            if len(content) > 0:
                urls.append(url)
                if len(urls) > 10:
                    break
        except:
            print("XXXXXXXXXXX")
            pass

if len(urls) > 0:
    r = random.randint(0, len(urls) - 1)
    url = urls[r]
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    if len(content) > 5000:
        content = content[:4999]
    print(content)
else:
    ret = "無可用新聞！"

print("找到文字 :", ret)


sys.exit()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

""" 無麥克風
import speech_recognition

r = speech_recognition.Recognizer()        
r.energy_threshold = 4000   #設定聲音辨識的靈敏度
while True:           
    try:
        with speech_recognition.Microphone() as source:  # 打開麥克風
            print("請開始說話:")
            audio = r.listen(source) #等待語音輸入        
            listen_text = r.recognize_google(audio, language="zh-TW")
            print(listen_text + "\n")
            if listen_text=="結束":
                break
    except:
        print("語音無法辨識\n")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment
from pydub.playback import play

print("播放wav檔")
record1 = AudioSegment.from_wav("record1.wav")
play(record1)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

import moviepy.editor

video_filename = "D:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

print("播放影片檔")

vsr = moviepy.editor.VideoFileClip(video_filename)
vsr.preview()

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# pydub：聲音處理

#!pip install pydub
#!pip install pydub==0.24.1

from pydub import AudioSegment

record1 = AudioSegment.from_wav("record1.wav")

print(record1.duration_seconds)

# record2 = record1[3000:9000]

# record2 = record1[:6000]

record2 = record1[-5000:]

print(record2.duration_seconds)

record2.export("tmp_record2.wav", format="wav")

# record3 = record1 + 8

record3 = record1 - 5

record3.export("tmp_record3.wav", format="wav")

birth = AudioSegment.from_wav("birth.wav")

print("birth 長度：" + str(birth.duration_seconds))

record4 = birth + record1

print("合併長度：" + str(record4.duration_seconds))

record4.export("tmp_record4.wav", format="wav")

# record5 = record1.fade_in(5000)  #5秒淡入

# record5 = record1.fade_out(3000)  #3秒淡出

record5 = record1.fade_in(5000).fade_out(3000)  # 5秒淡入,3秒淡出

record5.export("tmp_record5.wav", format="wav")

record6 = record1.reverse()

record6.export("tmp_record6.wav", format="wav")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# moviepy：影片處理

video_filename = "D:/_git/vcs/_big_files/holo1.mp4"

from base64 import b64encode

mp4 = open(video_filename, "rb").read()

data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

from moviepy.editor import *

vsr = VideoFileClip(video_filename)

print("長度：" + str(vsr.duration))

print("幀數：" + str(vsr.fps))

print("解析度：" + str(vsr.size))

clip1 = vsr.subclip(10, 20)

print("clip1 長度：" + str(clip1.duration))

clip1.write_videofile("tmp_clip1.mp4")  # 有點久

clip2 = vsr.subclip(30, 50)

print("clip2 長度：" + str(clip2.duration))

"""
#clip2.write_videofile("tmp_clip2.mp4")  #做很久

clip1 = VideoFileClip("tmp_clip1.mp4")

clip2 = VideoFileClip("tmp_clip2.mp4")

clip3 = concatenate_videoclips([clip1, clip2])

print("clip3 長度：" + str(clip3.duration))

clip3.write_videofile("tmp_clip3.mp4")

audio1 = AudioFileClip("tmp_holo1.mp4")

audio1.write_audiofile("tmp_holo1.mp3")

clip1_margin = clip1.margin(20)  #加黑邊

clip1_margin.write_videofile("tmp_clip1_margin.mp4")

clip1_mirrorx = clip1.fx(vfx.mirror_x)  #水平翻轉

clip1_mirrorx.write_videofile("tmp_clip1_mirrorx.mp4")

clip1_mirrory = clip1.fx(vfx.mirror_y)  #垂直翻轉

clip1_mirrory.write_videofile("tmp_clip1_mirrory.mp4")

clip1_resize = clip1.resize(0.50)  #改變尺寸

clip1_resize.write_videofile("tmp_clip1_resize.mp4")

clip1_mir_size = clip1.fx(vfx.mirror_x).resize(0.50)  #水平翻轉並改變尺寸

clip1_resize.write_videofile("tmp_clip1_resize.mp4")
"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


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

print("------------------------------------------------------------")  # 60個


# 3030
print("------------------------------")  # 30個
