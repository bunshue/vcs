"""
新進綜合

"""
import os
import sys
import time
import random

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

"""
#很多mp3不能播放

# fail
filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

# ok
filename = "D:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"

import playsound
playsound.playsound(filename, block=True)

filename = "D:/_git/vcs/_1.data/______test_files1/_wav/tone.wav"
import playsound
playsound.playsound(filename, block=True)

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pathlib import Path
from mutagen.mp3 import MP3
import datetime

infolder = "D:/_git/vcs/_1.data/______test_files1/_mp3"
ext = "*.mp3"


# 【函數: 取得MP3檔案的播放時間】
def getplaytime(readfile):
    try:
        audio = MP3(readfile)  # 載入檔案
        sec = audio.info.length  # 播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  # 轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"


# 【函數：搜尋資料夾與子資料夾MP3檔案】
def findfiles(infolder):
    totalsec = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext):  # 將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))  # 新增至列表
    for filename in sorted(filelist):  # 再替每個檔案排序
        val1, val2 = getplaytime(filename)
        totalsec += val1
        msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=totalsec))
    msg += "總播放時間 " + totaltimestr
    return msg


# 【執行】
msg = findfiles(infolder)
print(msg)

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
    time.sleep(1)
    time_count += 1

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
print("* recording done!")
"""

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
製作影片字幕
聲音轉字幕
"""

# 影片轉wav, 但是要跑很久

video_filename = "D:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

from moviepy.editor import *

audio1 = AudioFileClip("老北京.mp4")
audio1.write_audiofile("老北京22222.wav")

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
    if os.path.isdir(dirname):  # 資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  # 需延遲,否則會出錯
    os.mkdir(dirname)  # 建立資料夾


wave_filename = "老北京.wav"

cc = OpenCC("s2twp")
delay = 1300  # 聲音延遟時間
fname = "老北京"
sound = AudioSegment.from_file(fname + ".wav", format="wav")
start_end = detect_silence(sound, delay, sound.dBFS, 1)  # 偵測靜音

# 每個分割區間的結束位置
mslist = []
for i in range(len(start_end)):
    if i == (len(start_end) - 1):
        data = start_end[i][1]  # 最後一筆不必減1秒
    else:
        data = start_end[i][1] - delay  # 結束位置提前1秒
    mslist.append(data)

# 毫秒轉為xx:xx.xxx字串
timelist = []
for sss in mslist:
    h, ms = divmod(float(sss), 3600000)  # 時
    m, ms = divmod(float(ms), 60000)  # 分
    s, ms = divmod(float(ms), 1000)  # 秒
    ts = "%02d:%02d:%02d.%03d" % (h, m, s, ms)
    timelist.append(ts)

# 分割聲音檔
emptydir("tmp_分割聲音檔")
for i in range(len(timelist)):
    if i == 0:
        start = 0
    else:
        start = mslist[i - 1]
    end = mslist[i]
    filename = "tmp_分割聲音檔/slice{:0>3d}.wav".format(i + 1)
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

print("OK")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
"""
zh-tw : 正中
zh-cn : 簡中
en : 英文
ja : 日文
"""
print("------------------------------------------------------------")  # 60個

from pygame import mixer  # 匯入 mixer 物件

from gtts import gTTS

tts = gTTS(text="LANDrop 輕鬆實現跨系統無線傳輸資料、照片的免費工具", lang="zh-tw")
tts.save("tmp_aaaa.mp3")

# 播放mp3
mixer.init()  # 初始化
mixer.music.load("tmp_aaaa.mp3")  # 讀取聲音檔
mixer.music.play()  # 播放 聲音檔

from pygame import mixer
from gtts import gTTS

mixer.init()  # 初始化
if not os.path.isfile("tmp.mp3"):  # 不重要的聲音檔產生器
    tts = gTTS(text="不重要的語音檔", lang="zh-tw")
    tts.save("tmp.mp3")
    print("已產生不重要的語音檔 tmp.mp3")


# -----------------#
def bot_speak(text, lang):  # 建立自訂函式
    try:
        mixer.music.load("tmp.mp3")  # 讀取不重要的聲音檔
        tts = gTTS(text=text, lang=lang)
        tts.save("speak.mp3")
        mixer.music.load("speak.mp3")
        mixer.music.play()  # 播放重要的聲音檔
        while mixer.music.get_busy():
            continue
    except:
        print("播放音效失敗")


# -----------------#
bot_speak("我是萱萱", "zh-tw")  # 說出我是萱萱

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
gTTS：文字轉語音
pip install gTTS
"""

import gtts

print("目前支援的語音種類 :")
print(gtts.lang.tts_langs())

print("gTTS可以透過線上翻譯，將文字轉換為語音，並將語音存檔")
print("將文字分解為多個段落，分別轉換為語音")

txt1 = "王之渙 涼州詞"
txt2 = "黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"

filename = "tmp_gtts1.mp3"
tts = gtts.gTTS(text=txt2, lang="zh-tw")
tts.save(filename)
print("存檔完成, 檔名 :", filename)

filename = "tmp_gtts2.mp3"
f = open(filename, "wb")

tts1 = gtts.gTTS(text=txt1, lang="zh-tw")
tts1.write_to_fp(f)

tts2 = gtts.gTTS(text=txt2, lang="zh-tw")
tts2.write_to_fp(f)

print("存檔完成, 檔名 :", filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mp3_filename = "tmp_mp3_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"

import gtts

text = "Welcome to the United States and have a nice day."
tts = gtts.gTTS(text=text, lang="en")
tts.save(mp3_filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

mp3_filename = "tmp_mp3_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"

import gtts

text = "黃河遠上白雲間，一片孤城萬仞山。羌笛何須怨楊柳？春風不度玉門關。"

tts = gtts.gTTS(text=text, lang="zh-tw")
tts.save(mp3_filename)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# http://yhhuang1966.blogspot.com/2017/08/google-gtts-api.html
# 利用 Google gTTS 文字轉語音 API 讓電腦說話

from gtts import gTTS
from pygame import mixer


def speak(sentence, lang, loops=1):
    filename = "tmp_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp3"
    tts = gTTS(text=sentence, lang=lang)
    print(filename)
    tts.save(filename)
    mixer.init()
    mixer.music.load(filename)
    mixer.music.play()


speak("ありがとう", "ja")
time.sleep(5)
speak("本软件验证和确认报告包括以下信息", "zh-tw")
time.sleep(5)
speak("Picture Archiving & Communication System", "en")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
SpeechRecognition：語音轉文字(聲音檔)
pip install SpeechRecognition

"""

print("語音轉文字")

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
from IPython.display import display  # 用IPython
from IPython.display import Javascript  # 用IPython

# from google.colab.output import eval_js
from base64 import b64decode


def record_audio(filename):
    js = Javascript(
        """
    async function recordAudio() {
      const div = document.createElement("div");
      const capture = document.createElement("button");
      capture.textContent = "開始錄音";
      capture.style.background = "orange";
      capture.style.color = "white";
      div.appendChild(capture);
      const stopCapture = document.createElement("button");
      stopCapture.textContent = "停止錄音";
      stopCapture.style.background = "red";
      stopCapture.style.color = "white";
      const audio = document.createElement("audio");
      const recordingVid = document.createElement("audio");
      audio.style.display = "block";
      const stream = await navigator.mediaDevices.getUserMedia({audio:true});
     
      let recorder = new MediaRecorder(stream);
      document.body.appendChild(div);
      div.appendChild(audio);
      audio.srcObject = stream;
      audio.muted = true;
      await audio.play();
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);
      await new Promise((resolve) => {capture.onclick = resolve; });
      recorder.start();
      capture.replaceWith(stopCapture);
      await new Promise((resolve) => stopCapture.onclick = resolve);
      recorder.stop();
      let recData = await new Promise((resolve) => recorder.ondataavailable = resolve);
      let arrBuff = await recData.data.arrayBuffer();
      stream.getAudioTracks()[0].stop();
      div.remove();
 
      let binaryString = "";
      let bytes = new Uint8Array(arrBuff);
      bytes.forEach((byte) => {
        binaryString += String.fromCharCode(byte);
      })
    return btoa(binaryString);
    }
"""
    )
    try:
        display(js)
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
google_trans_new：文字翻譯
pip install google_trans_new

"""

"""fail
from google_trans_new import google_translator
translator = google_translator()
text="今天天氣很好"
word = translator.translate(text, lang_src="zh-TW", lang_tgt="ja", pronounce=True)
print(word)

from google_trans_new import google_translator
translator = google_translator()
print(translator.translate("今日の天気は良いです"))

lang = translator.detect("今日の天気は良いです")
print(lang)
"""

print("------------------------------------------------------------")  # 60個

"""
應用：AI智慧讀報機
!pip install newspaper3k
!pip install gTTS
!pip install google_trans_new
"""

""" fail
import newspaper
from newspaper import Article
from google_trans_new import google_translator
import gtts
import IPython.display as display

paper = newspaper.build("http://cnn.com", language="en")
# paper = newspaper.build("http://www.cnbc.com", language="en")
# paper = newspaper.build("http://www.bbc.co.uk", language="en")
# paper = newspaper.build("http://www.foxnews.com", language="en")
urls = []
for article in paper.articles:
    url = article.url
    if ".html" in url:
        try:  #有時會產生無法擷取的錯誤,故使用try
          article = Article(url)
          article.download()
          article.parse()
          content = article.text
          if len(content)>0:
              urls.append(url)
              if len(urls)>10:
                break
        except: pass
if len(urls)>0:
    r = random.randint(0,len(urls)-1)
    url = urls[r]
    article = Article(url)
    article.download()
    article.parse()
    content = article.text
    if len(content)>5000: content = content[:4999]
    translator = google_translator()
    ret = translator.translate(content, lang_tgt="zh-TW")
    print(ret)
else: 
  ret = "無可用新聞！"
tts = gtts.gTTS(text=ret, lang="zh-tw")
tts.save("tmp_news.mp3")
display.Audio("tmp_news.mp3", autoplay=True)

"""
print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# 需安裝playsound
# pip install playsound

import newspaper
from newspaper import Article
from google_trans_new import google_translator
import gtts
from playsound import playsound

# paper = newspaper.build("http://cnn.com", language="en")
paper = newspaper.build("http://www.cnbc.com", language="en")
# paper = newspaper.build("http://www.bbc.co.uk", language="en")
# paper = newspaper.build("http://www.foxnews.com", language="en")

print(type(paper.articles))
print(len(paper.articles))
print(paper.articles)

for article in paper.articles:
    url = article.url
    if ".html" in url:
        print(url)
        """
        try:  #有時會產生無法擷取的錯誤,故使用try
            article = Article(url)
            article.download()
            article.parse()
            content = article.text
            if len(content)>0:
                if len(content)>5000: content = content[:4999]
                translator = google_translator()
                ret = translator.translate(content, lang_tgt="zh-TW")
                print(ret)
                tts = gtts.gTTS(text=ret, lang="zh-tw")
                tts.save("tmp_news.mp3")
                playsound("tmp_news.mp3")
        except:
            pass
        """

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

"""
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

""" 播放OK
from pydub import AudioSegment
from pydub.playback import play

print("播放wav檔")
record1 = AudioSegment.from_wav("record1.wav")
play(record1)

print("------------------------------------------------------------")	#60個
print("------------------------------------------------------------")  # 60個

import moviepy.editor

video_filename = "D:/_git/vcs/_4.python/opencv/data/_video/spiderman.mp4"

print("播放影片檔")

vsr = moviepy.editor.VideoFileClip(video_filename)
vsr.preview()
"""

print("------------------------------------------------------------")  # 60個

# pydub：聲音處理

import IPython.display as display

display.Audio("record1.wav", autoplay=True)

#!pip install pydub
#!pip install pydub==0.24.1

from pydub import AudioSegment

record1 = AudioSegment.from_wav("record1.wav")

print(record1.duration_seconds)

display.Audio("record1.wav", autoplay=True)

# record2 = record1[3000:9000]

# record2 = record1[:6000]

record2 = record1[-5000:]

print(record2.duration_seconds)

record2.export("tmp_record2.wav", format="wav")

display.Audio("tmp_record2.wav", autoplay=True)

# record3 = record1 + 8

record3 = record1 - 5

record3.export("tmp_record3.wav", format="wav")

display.Audio("tmp_record3.wav", autoplay=True)

birth = AudioSegment.from_wav("birth.wav")

print("birth 長度：" + str(birth.duration_seconds))

record4 = birth + record1

print("合併長度：" + str(record4.duration_seconds))

record4.export("tmp_record4.wav", format="wav")

display.Audio("tmp_record4.wav", autoplay=True)

# record5 = record1.fade_in(5000)  #5秒淡入

# record5 = record1.fade_out(3000)  #3秒淡出

record5 = record1.fade_in(5000).fade_out(3000)  # 5秒淡入,3秒淡出

record5.export("tmp_record5.wav", format="wav")

display.Audio("tmp_record5.wav", autoplay=True)

record6 = record1.reverse()

record6.export("tmp_record6.wav", format="wav")

display.Audio("tmp_record6.wav", autoplay=True)

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

# moviepy：影片處理

video_filename = "D:/_git/vcs/_big_files/holo1.mp4"

from IPython.display import HTML  # 用IPython

from base64 import b64encode

mp4 = open(video_filename, "rb").read()

data_url = "data:video/mp4;base64," + b64encode(mp4).decode()

HTML(
    """

<video width=400 controls>

      <source src="%s" type="video/mp4">

</video>

"""
    % data_url
)

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
