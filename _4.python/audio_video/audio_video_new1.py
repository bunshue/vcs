"""
新進綜合

"""
import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

""" NG
from pydub import AudioSegment

mywav = 'notify1.wav'
# 讀取.wav文件
wav_audio = AudioSegment.from_wav(mywav)

# 轉換為.mp3
wav_audio.export("notify.mp3", format="mp3")
"""

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
"""
#很多mp3不能播放

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"

import playsound
playsound.playsound(filename, block=True)
"""
print("------------------------------------------------------------")  # 60個

from mutagen.mp3 import MP3
import datetime

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

audio = MP3(filename)             #載入檔案
sec = audio.info.length         #播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
print("播放時間=",timestr)

print("------------------------------------------------------------")  # 60個

import cv2
import datetime

filename = "C:/_git/vcs/_1.data/______test_files1/_video/i2c.avi"

cap = cv2.VideoCapture(filename)

frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)       #總影格數
fps = cap.get(cv2.CAP_PROP_FPS)                 #影格速率
sec = int(frame / fps)                          #播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
print("播放時間=",timestr)

print("------------------------------------------------------------")  # 60個

from pathlib import Path
import cv2
import datetime

infolder = "C:/_git/vcs/_1.data/______test_files1/_video"
extlist = ["*.mp4", "*.mov"]

#【函數: 取得影片檔的播放時間】
def getplaytime(readfile):
    try:
        cap = cv2.VideoCapture(readfile)            #載入檔案
        frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)   #總影格數
        fps = cap.get(cv2.CAP_PROP_FPS)             #影格速率
        sec = int(frame / fps)                        #播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"
#【函數: 搜尋資料夾與子資料夾的影片檔】
def findfiles(infolder):
    totalsec = 0
    msg = ""
    for ext in extlist:                     #以多個副檔名調查
        filelist = []
        for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
            filelist.append(str(p))         #新增至列表
        for filename in sorted(filelist):   #再替每個檔案排序
            val1, val2 = getplaytime(filename)
            totalsec += val1
            msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=totalsec))
    msg += "總播放時間 " + totaltimestr
    return msg

#【執行函數】
msg = findfiles(infolder)
print(msg)

print("------------------------------------------------------------")  # 60個

from pathlib import Path
from mutagen.mp3 import MP3
import datetime

infolder = "C:/_git/vcs/_1.data/______test_files1/_mp3"
ext = "*.mp3"

#【函數: 取得MP3檔案的播放時間】
def getplaytime(readfile):
    try:
        audio = MP3(readfile)   #載入檔案
        sec = audio.info.length #播放時間（秒）
        timestr = str(datetime.timedelta(seconds=sec))  #轉換成時分秒格式
        return sec, readfile + " " + timestr
    except:
        return 0, readfile + "：程式執行失敗。"
#【函數：搜尋資料夾與子資料夾MP3檔案】
def findfiles(infolder):
    totalsec = 0
    msg = ""
    filelist = []
    for p in Path(infolder).rglob(ext): #將這個資料夾以及子資料夾的所有檔案
        filelist.append(str(p))         #新增至列表
    for filename in sorted(filelist):   #再替每個檔案排序
        val1, val2 = getplaytime(filename)
        totalsec += val1
        msg += val2 + "\n"
    totaltimestr = str(datetime.timedelta(seconds=totalsec))
    msg += "總播放時間 " + totaltimestr
    return msg

#【執行】
msg = findfiles(infolder)
print(msg)

print("------------------------------------------------------------")  # 60個
"""
import pyautogui
import cv2
import numpy as np
import sounddevice as sd
import wave

# 設定螢幕解析度（根據需要調整）
螢幕寬度, 螢幕高度 = pyautogui.size()

# 設定輸出影片檔名
輸出影片檔名 = "螢幕錄影.mp4"

# 設定音訊錄製參數
取樣率 = 44100
錄製時間 = 10  # 錄製時間（秒）

# 初始化音訊緩衝區
音訊緩衝區 = []

# 開始音訊錄製
def 音訊回呼(indata, frames, time, status):
    if status:
        print("錄製音訊時發生錯誤:", status)
    音訊緩衝區.extend(indata)

with sd.InputStream(callback=音訊回呼, channels=2, samplerate=取樣率):
    # 初始化影片寫入器
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    影片寫入器 = cv2.VideoWriter(輸出影片檔名, fourcc, 20.0, (螢幕寬度, 螢幕高度))

    # 錄製螢幕並儲存到影片
    while True:
        螢幕截圖 = pyautogui.screenshot()
        影格 = np.array(螢幕截圖)
        影格 = cv2.cvtColor(影格, cv2.COLOR_RGB2BGR)
        影片寫入器.write(影格)

        # 錄製指定時間後中斷迴圈
        if len(音訊緩衝區) >= 取樣率 * 錄製時間:
            break

# 將音訊嵌入到影片中
音訊緩衝區 = np.array(音訊緩衝區)
音訊緩衝區 = np.int16(音訊緩衝區 * 32767)
音訊緩衝區 = 音訊緩衝區.tobytes()
影片寫入器.write(音訊緩衝區)

print(f"螢幕錄影已儲存為 {輸出影片檔名}")
"""

print("------------------------------------------------------------")  # 60個

"""

#声音录制
import pyaudio
import wave

CHUNK = 1024
if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)
while data != '':
    stream.write(data)
    data = wf.readframes(CHUNK)

stream.stop_stream()
stream.close()
p.terminate()
"""


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
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
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
"""
#视频录制（无声音）

from PIL import ImageGrab
import numpy as np
import cv2

image = ImageGrab.grab()#获得当前屏幕
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:",image.mode)
k=np.zeros((width,height),np.uint8)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height))
#输出文件命名为test.mp4,帧率为16，可以自己设置
while True:
    img_rgb = ImageGrab.grab()
    img_bgr=cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
    video.write(img_bgr)
    cv2.imshow('imm', img_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
"""
print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

""" TBD
#录制的音频与视频合成为带声音的视频
#录制200帧，带音频的MP4视频，单线程

import pyaudio
import wave
from pyaudio import PyAudio,paInt16
from PIL import ImageGrab
import numpy as np
import cv2
from moviepy.editor import *
from moviepy.audio.fx import all

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
audio_record_flag = True
def callback(in_data, frame_count, time_info, status):
    wf.writeframes(in_data)
    if audio_record_flag:
        return (in_data, pyaudio.paContinue)
    else:
        return (in_data, pyaudio.paComplete)
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)
image = ImageGrab.grab()#获得当前屏幕
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:",image.mode)
k=np.zeros((width,height),np.uint8)

fourcc = cv2.VideoWriter_fourcc(*'XVID')#编码格式
video = cv2.VideoWriter('test.mp4', fourcc, 9.5, (width, height))
#经实际测试，单线程下最高帧率为10帧/秒，且会变动，因此选择9.5帧/秒
#若设置帧率与实际帧率不一致，会导致视频时间与音频时间不一致

print("video recording!!!!!")
stream.start_stream()
print("audio recording!!!!!")
record_count = 0
while True:
    img_rgb = ImageGrab.grab()
    img_bgr=cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
    video.write(img_bgr)
    record_count += 1
    if(record_count > 200):
        break
    print(record_count, time.time())

audio_record_flag = False
while stream.is_active():
    time.sleep(1)

stream.stop_stream()
stream.close()
wf.close()
p.terminate()
print("audio recording done!!!!!")

video.release()
cv2.destroyAllWindows()
print("video recording done!!!!!")
"""

""" 影音合併有問題
print("video audio merge!!!!!")
audioclip = AudioFileClip("output.wav")
videoclip = VideoFileClip("test.mp4")
videoclip2 = videoclip.set_audio(audioclip)
video = CompositeVideoClip([videoclip2])
video.write_videofile("test2.mp4",codec='mpeg4')
"""

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



