"""

Python 聲音處理

"""

import os
import sys
import time
import random

print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
print(song)  # <pydub.audio_segment.AudioSegment object at 0x7faaa545a7f0>

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("oxxostudio.wav", format="wav")  # 輸出為 wav
print("ok")  # 輸出後印出 ok

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song.export("output.wav", bitrate="96k")  # 輸出壓縮比率為 96k 的 mp3 檔案
print("ok")  # 輸出後印出 ok

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
duration = song.duration_seconds  # 讀取長度
channels = song.channels  # 讀取聲道數量
print(channels, duration)  # 印出資訊

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
song[1500:5500].export("output.mp3")  # 取出 1500 毫秒～5500 毫秒長度的聲音，輸出為 output.mp3
print("ok")  # 輸出後印出 ok

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song1 = AudioSegment.from_mp3("oxxo1.mp3")  # 讀取第一個 mp3 檔案
song2 = AudioSegment.from_mp3("oxxo2.mp3")  # 讀取第二個 mp3 檔案
output = song1 + song2  # 串接兩段聲音
output.export("output.mp3")  # 輸出為 output.mp3
print("ok")  # 輸出後印出 ok

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3 檔案
output = song * 3  # 乘以 3，重複三次變成三倍長
output.export("output.mp3")
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取 mp3
output1 = song[:] + 10  # 將所有陣列中的資料增加 10 ( 變大聲 )
output2 = song[:] - 10  # 將所有陣列中的資料減少 10 ( 變小聲 )
output1.export("output1.mp3")  # 輸出聲音
output2.export("output2.mp3")
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.apply_gain(10)  # 將音量增加 10 ( 變大聲 )
output2 = song.apply_gain(-10)  # 將音量減少 10 ( 變小聲 )
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")
output1 = song.fade_in(3000)  # 開頭三秒 ( 3000ms ) 淡入
output2 = song.fade_out(3000)  # 結尾三秒 ( 3000ms ) 淡出
output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("oxxostudio.mp3")

output1 = song.fade(to_gain=15, start=1000, duration=2000)
# 從 1 秒的位置開始，慢慢變大聲到增加 15，過程持續 2 秒

output2 = song.fade(to_gain=-30, end=3000, duration=2000)
# 從 1 秒的位置開始 ( 3000-2000 )，慢慢變小聲到減少 30，過程持續 2 秒

output1.export("output1.mp3")
output2.export("output2.mp3")
print("ok")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 讀取背景音樂 mp3 檔案
voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.overlay(song, loop=True)  # 混合說話聲音和背景音樂
output.export("output.mp3")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組

voice = AudioSegment.from_mp3("voice.mp3")  # 讀取說話聲音 mp3 檔案
output = voice.reverse()  # 反轉說話聲音
output.export("output.mp3")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment

song = AudioSegment.from_mp3("test.mp3")  # 讀取聲音檔案


# 定義加速與減速的函式
def speed_change(sound, speed=1.0):
    rate = sound._spawn(
        sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)}
    )
    return rate.set_frame_rate(sound.frame_rate)


song_slow = speed_change(song, 0.75)  # 聲音減速
song_fast = speed_change(song, 2.0)  # 聲音加速

song_slow.export("song_slow.mp3")
song_fast.export("song_fast.mp3")

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from pydub import AudioSegment  # 載入 pydub 的 AudioSegment 模組
from pydub.playback import play  # 載入 pydub.playback 的 play 模組

song = AudioSegment.from_mp3("oxxostudio.mp3")  # 開啟聲音檔案
output = song * 2  # 讓聲音檔案變成兩倍長
play(output)  # 播放聲音

print("------------------------------------------------------------")  # 60個
print("------------------------------------------------------------")  # 60個

from IPython.display import Audio  # 載入 IPython.display 的 Audio模組  # 用IPython

Audio("output.mp3")  # 播放聲音


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
