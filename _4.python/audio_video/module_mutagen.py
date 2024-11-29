"""
# Python標籤編輯庫,mutagen

Mutagen介绍
Mutagen是一个Python库,用于处理音频文件元数据。
它可以读取并写入popular音频格式的元数据,比如MP3,Ogg Vorbis,FLAC,WAV等。
"""

import os
import sys
import time
import random
import datetime

print("------------------------------------------------------------")  # 60個

# 读取MP3文件的元数据:

filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"
filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/aaaa.mp3"


from mutagen.easyid3 import EasyID3

tags = EasyID3(filename)
print(tags)

""" 所有標籤
for key in EasyID3.valid_keys.keys():
    print(key)
"""

# 標籤讀出 顯示

tags = EasyID3(filename)
print(type(tags))
print(tags.pprint())

import mutagen

audio = mutagen.File(filename, easy=True)

# print(type(audio))
print(audio)
print(audio["album"])
print(audio["title"])
print(audio["artist"])
print(audio["tracknumber"])
print(audio["genre"])

"""
#修改并保存MP3文件的元数据:
audio["artist"] = "harumi"
audio.save()
"""

"""
#将FLAC文件转换为WAV,并复制其元数据:

flac = mutagen.File("song.flac", easy=True)
flac.delete()  # 删除FLAC音频流
flac.save(filename="song.wav")  # 将FLAC容器保存为WAV格式
"""

"""
#读取MP3文件的专辑封面图片:
audio = mutagen.File('song.mp3', easy=True)
pic = audio.tags.getall('APIC')[0]
with open('cover.jpg', 'wb') as f:
f.write(pic.data)
"""

print("取得 mp3 的長度")
filename = "C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3"

from mutagen.mp3 import MP3

audio = MP3(filename)  # 載入檔案
sec = audio.info.length  # 播放時間（秒）
timestr = str(datetime.timedelta(seconds=sec))  # 轉換成時分秒格式
print("播放時間=", timestr)

audio = MP3(filename)
length = audio.info.length
print("duration sec: " + str(length))
print("duration min: " + str(int(length / 60)) + ":" + str(int(length % 60)))

print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個


print("------------------------------------------------------------")  # 60個
print("作業完成")
print("------------------------------------------------------------")  # 60個
