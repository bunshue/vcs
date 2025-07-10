"""
新進綜合

"""
import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

print('使用 ffmpeg.exe 將 .wav 轉成 .mp3')

wav_filename = '老北京.wav'
mp3_filename = '老北京.mp3'

# 讀取.wav文件
wav_audio = AudioSegment.from_wav(wav_filename)

# 轉換為.mp3
wav_audio.export(mp3_filename, format="mp3")

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

# fail
filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

# ok
filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"

import playsound
playsound.playsound(filename, block=True)

filename = "C:/_git/vcs/_1.data/______test_files1/_wav/tone.wav"
import playsound
playsound.playsound(filename, block=True)

"""

print("------------------------------------------------------------")  # 60個
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

""" fail
import pyautogui
import cv2
import numpy as np
import sounddevice as sd
import wave

# 設定螢幕解析度（根據需要調整）
W, H = pyautogui.size()

# 設定輸出影片檔名
record_filename = (
    "tmp_screen_recording2_" + time.strftime("%Y%m%d_%H%M%S", time.localtime()) + ".mp4"
)

# 設定音訊錄製參數
SAMPLE_RATE = 44100 #取樣率
RECORD_TIME_SECOND = 10  # 錄製時間（秒）

# 初始化audio_buffer
audio_buffer = []#音訊緩衝區

# 開始音訊錄製
def 音訊回呼(indata, frames, time, status):
    if status:
        print("錄製音訊時發生錯誤:", status)
    audio_buffer.extend(indata)

with sd.InputStream(callback=音訊回呼, channels=2, samplerate=SAMPLE_RATE):
    # 初始化影片寫入器 out
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(record_filename, fourcc, 20.0, (W, H))

    # 錄製螢幕並儲存到影片
    while True:
        screen_picture = pyautogui.screenshot() #螢幕截圖
        frame = np.array(screen_picture)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

        # 錄製指定時間後中斷迴圈
        if len(audio_buffer) >= SAMPLE_RATE * RECORD_TIME_SECOND:
            break

# 將音訊嵌入到影片中
audio_buffer = np.array(audio_buffer)
audio_buffer = np.int16(audio_buffer * 32767)
audio_buffer = audio_buffer.tobytes()
out.write(audio_buffer)

print(f"螢幕錄影已儲存為 {record_filename}")
"""

print("------------------------------------------------------------")  # 60個

""" TBD
#声音录制
import pyaudio
import wave

CHUNK = 1024

wav_filename = 'test_wave.wav'

wf = wave.open(wav_filename, 'rb')
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True)

data = wf.readframes(CHUNK)

while data != '':
    print('c')
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

"""
製作影片字幕

聲音轉字幕

"""

#影片轉wav, 但是要跑很久

video_filename = 'C:/_git/vcs/_1.data/______test_files1/_video/spiderman.mp4'

from moviepy.editor import *
audio1 = AudioFileClip('老北京.mp4')
audio1.write_audiofile('老北京22222.wav')

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

def emptydir(dirname):  #清空資料夾
    if os.path.isdir(dirname):  #資料夾存在就刪除
        shutil.rmtree(dirname)
        sleep(2)  #需延遲,否則會出錯
    os.mkdir(dirname)  #建立資料夾

wave_filename = "老北京.wav"

cc = OpenCC('s2twp')
delay = 1300  #聲音延遟時間
fname = '老北京'
sound = AudioSegment.from_file(fname + ".wav", format="wav")
start_end = detect_silence(sound, delay, sound.dBFS, 1)  #偵測靜音

#每個分割區間的結束位置
mslist = []
for i in range(len(start_end)):
    if i== (len(start_end)-1): data = start_end[i][1]  #最後一筆不必減1秒
    else:  data = start_end[i][1] - delay  #結束位置提前1秒
    mslist.append(data)

#毫秒轉為xx:xx.xxx字串
timelist = []
for sss in mslist: 
    h,ms = divmod(float(sss),3600000)  #時
    m,ms = divmod(float(ms),60000)  #分
    s,ms = divmod(float(ms),1000)  #秒
    ts="%02d:%02d:%02d.%03d" % (h,m,s,ms)
    timelist.append(ts)

#分割聲音檔
emptydir('tmp_分割聲音檔')
for i in range(len(timelist)):  
    if i==0:  start = 0
    else:  start = mslist[i-1]
    end = mslist[i]
    filename = 'tmp_分割聲音檔/slice{:0>3d}.wav'.format(i+1)
    sound[start:end].export(filename, format='wav')


print('對 tmp_分割聲音檔 進行語音辨識')
r = sr.Recognizer()  #建立語音辨識物件
file = open(fname + '.srt', 'w', encoding='UTF-8')  #儲存辨識結果

# 撈出單層wav檔
wavfiles = glob.glob('tmp_分割聲音檔/*.wav')
data = ''
count = 1
for i in range(len(wavfiles)):
    try:
        with sr.WavFile("tmp_分割聲音檔/slice{:0>3d}.wav".format(i+1)) as source: 
            audio = r.record(source)
        result = r.recognize_google(audio, language="zh-TW")  #辨識結果
        result = cc.convert(result)  #轉繁體中文
        print('{}. {}'.format(count, result))
        #組合SRT格式
        data += str(count) + '\n'
        if i==0: start = '00:00:00,000'
        else: start = timelist[i-1].replace('.', ',')
        end = timelist[i].replace('.', ',')
        data += (start + ' --> ' + end + '\n')
        data += (result + '\n\n')
        count +=1
    except sr.UnknownValueError:
        print("Google Speech Recognition 無法辨識此語音！")
    except sr.RequestError as e:
        print("無法由 Google Speech Recognition 取得結果; {0}".format(e))
file.write(data)
file.close()

print('完成')

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
sys.exit()



print("------------------------------------------------------------")  # 60個

