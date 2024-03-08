"""
新進綜合

"""

import sys


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個

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


print("------------------------------------------------------------")  # 60個
"""
#很多mp3不能播放

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"

import playsound
playsound.playsound(filename, block=True)
"""
print("------------------------------------------------------------")  # 60個

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(filename)
pygame.mixer.music.play()


print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個



print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個



